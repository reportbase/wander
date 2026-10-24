"""CAH run 1: the Cauchy attention horizon sweep at a reduced scale (plans/cah-plan.md).

Run from the repository's root:  python3 runs/cah/cah.py [train|probe|report]
Needs torch (CPU), transformers, datasets. HF_HOME may point outside the repo.
The attention modules, MLP, Block and SmallLM are copied unchanged from cauchy_horizon_sweep_2.py
(sha256 a75f629d…f1); the scale, data and evaluation are the plan's.
"""
import json, math, os, sys, time, random
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from dataclasses import dataclass

torch.set_num_threads(4)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "cah-results.json")
CKPT = os.environ.get("CAH_CKPT", "/tmp/cah-ckpt")
os.makedirs(CKPT, exist_ok=True)

N_LAYER, N_HEAD, N_EMBD, BLOCK_SIZE, DROPOUT = 4, 4, 128, 256, 0.1
LR, WD, WARMUP, BATCH = 3e-3, 0.1, 100, 16
STEPS = int(os.environ.get("CAH_STEPS", 400))
HORIZONS = [96, 128, 148, 163, 180, 210, 256]
SEEDS = [42, 137, 2024]


@dataclass
class ModelConfig:
    vocab_size: int = 50257
    n_layer: int = N_LAYER
    n_head: int = N_HEAD
    n_embd: int = N_EMBD
    block_size: int = BLOCK_SIZE
    horizon_k: int = 163
    dropout: float = DROPOUT


# >>> copied from cauchy_horizon_sweep_2.py, unchanged
class SoftmaxAttention(nn.Module):
    """Standard causal softmax attention — the baseline."""

    def __init__(self, config: ModelConfig):
        super().__init__()
        self.n_head = config.n_head
        self.n_embd = config.n_embd
        self.head_dim = config.n_embd // config.n_head

        self.c_attn = nn.Linear(config.n_embd, 3 * config.n_embd)
        self.c_proj = nn.Linear(config.n_embd, config.n_embd)
        self.attn_dropout = nn.Dropout(config.dropout)
        self.resid_dropout = nn.Dropout(config.dropout)

        # Causal mask
        mask = torch.tril(torch.ones(config.block_size, config.block_size))
        self.register_buffer("mask", mask.view(1, 1, config.block_size, config.block_size))

    def forward(self, x):
        B, T, C = x.shape

        qkv = self.c_attn(x)
        q, k, v = qkv.split(self.n_embd, dim=-1)

        q = q.view(B, T, self.n_head, self.head_dim).transpose(1, 2)
        k = k.view(B, T, self.n_head, self.head_dim).transpose(1, 2)
        v = v.view(B, T, self.n_head, self.head_dim).transpose(1, 2)

        # Scaled dot-product attention
        att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(self.head_dim))
        att = att.masked_fill(self.mask[:, :, :T, :T] == 0, float('-inf'))
        att = F.softmax(att, dim=-1)
        att = self.attn_dropout(att)

        y = att @ v
        y = y.transpose(1, 2).contiguous().view(B, T, C)
        y = self.resid_dropout(self.c_proj(y))
        return y


class BoundedCauchyAttention(nn.Module):
    """
    Cauchy kernel attention with bounded horizon.

    Each query attends to at most K previous tokens.
    Kernel: 1 / (1 + d²/γ²) where d² is squared Euclidean distance.
    """

    def __init__(self, config: ModelConfig):
        super().__init__()
        self.n_head = config.n_head
        self.n_embd = config.n_embd
        self.head_dim = config.n_embd // config.n_head
        self.horizon_k = config.horizon_k

        self.c_attn = nn.Linear(config.n_embd, 3 * config.n_embd)
        self.c_proj = nn.Linear(config.n_embd, config.n_embd)
        self.attn_dropout = nn.Dropout(config.dropout)
        self.resid_dropout = nn.Dropout(config.dropout)

        # Learnable temperature per head
        self.temperature = nn.Parameter(torch.ones(self.n_head, 1, 1))

        # Bounded causal mask: 1s within horizon, 0s outside
        mask = torch.zeros(config.block_size, config.block_size)
        for t in range(config.block_size):
            start = max(0, t - self.horizon_k + 1)
            mask[t, start:t + 1] = 1.0
        self.register_buffer("mask", mask.view(1, 1, config.block_size, config.block_size))

    def forward(self, x):
        B, T, C = x.shape

        qkv = self.c_attn(x)
        q, k, v = qkv.split(self.n_embd, dim=-1)

        q = q.view(B, T, self.n_head, self.head_dim).transpose(1, 2)
        k = k.view(B, T, self.n_head, self.head_dim).transpose(1, 2)
        v = v.view(B, T, self.n_head, self.head_dim).transpose(1, 2)

        # Squared Euclidean distance via expansion
        # d²(q,k) = ||q||² + ||k||² - 2(q·k)
        q_sq = (q ** 2).sum(dim=-1, keepdim=True)          # (B, H, T, 1)
        k_sq = (k ** 2).sum(dim=-1, keepdim=True)          # (B, H, T, 1)
        dot = q @ k.transpose(-2, -1)                       # (B, H, T, T)
        dist_sq = q_sq + k_sq.transpose(-2, -1) - 2 * dot  # (B, H, T, T)
        dist_sq = torch.clamp(dist_sq, min=0.0)

        # Cauchy kernel
        gamma_sq = self.temperature.abs() + 1e-6
        att = 1.0 / (1.0 + dist_sq / gamma_sq)

        # Apply bounded horizon mask
        att = att * self.mask[:, :, :T, :T]

        # Normalize over visible tokens
        att = att / (att.sum(dim=-1, keepdim=True) + 1e-8)
        att = self.attn_dropout(att)

        y = att @ v
        y = y.transpose(1, 2).contiguous().view(B, T, C)
        y = self.resid_dropout(self.c_proj(y))
        return y


# ═══════════════════════════════════════════════════════════════════════════
# MODEL
# ═══════════════════════════════════════════════════════════════════════════

class MLP(nn.Module):
    def __init__(self, config: ModelConfig):
        super().__init__()
        self.c_fc = nn.Linear(config.n_embd, 4 * config.n_embd)
        self.gelu = nn.GELU()
        self.c_proj = nn.Linear(4 * config.n_embd, config.n_embd)
        self.dropout = nn.Dropout(config.dropout)

    def forward(self, x):
        return self.dropout(self.c_proj(self.gelu(self.c_fc(x))))


class Block(nn.Module):
    def __init__(self, config: ModelConfig, use_softmax=False):
        super().__init__()
        self.ln_1 = nn.LayerNorm(config.n_embd)
        self.attn = SoftmaxAttention(config) if use_softmax else BoundedCauchyAttention(config)
        self.ln_2 = nn.LayerNorm(config.n_embd)
        self.mlp = MLP(config)

    def forward(self, x):
        x = x + self.attn(self.ln_1(x))
        x = x + self.mlp(self.ln_2(x))
        return x


class SmallLM(nn.Module):
    def __init__(self, config: ModelConfig, use_softmax=False):
        super().__init__()
        self.config = config

        self.wte = nn.Embedding(config.vocab_size, config.n_embd)
        self.wpe = nn.Embedding(config.block_size, config.n_embd)
        self.drop = nn.Dropout(config.dropout)
        self.blocks = nn.ModuleList([Block(config, use_softmax) for _ in range(config.n_layer)])
        self.ln_f = nn.LayerNorm(config.n_embd)
        self.lm_head = nn.Linear(config.n_embd, config.vocab_size, bias=False)

        # Weight tying
        self.wte.weight = self.lm_head.weight

        self.apply(self._init_weights)

        n_params = sum(p.numel() for p in self.parameters())
        attn_type = "softmax" if use_softmax else f"cauchy K={config.horizon_k}"
        print(f"  Model: {n_params / 1e6:.1f}M params | {attn_type}")

    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def forward(self, idx, targets=None):
        B, T = idx.shape

        pos = torch.arange(0, T, dtype=torch.long, device=idx.device)
        x = self.drop(self.wte(idx) + self.wpe(pos))

        for block in self.blocks:
            x = block(x)

        logits = self.lm_head(self.ln_f(x))

        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1))

        return logits, loss


# ═══════════════════════════════════════════════════════════════════════════
# DATA
# ═══════════════════════════════════════════════════════════════════════════
# <<< end of copy


def set_seed(seed):
    random.seed(seed); np.random.seed(seed); torch.manual_seed(seed)


def tokens():
    path = os.path.join(CKPT, "tokens.npz")
    if os.path.exists(path):
        z = np.load(path); return z["train"], z["val"]
    from datasets import load_dataset
    from transformers import GPT2Tokenizer
    d = load_dataset("Salesforce/wikitext", "wikitext-2-v1")
    tok = GPT2Tokenizer.from_pretrained("gpt2")
    tr = np.array(tok.encode("\n".join(d["train"]["text"])), dtype=np.int64)
    va = np.array(tok.encode("\n".join(d["validation"]["text"])), dtype=np.int64)
    np.savez(path, train=tr, val=va)
    return tr, va


def batch(tr, rng):
    ix = rng.integers(0, len(tr) - BLOCK_SIZE - 1, BATCH)
    x = np.stack([tr[i:i + BLOCK_SIZE] for i in ix]); y = np.stack([tr[i + 1:i + 1 + BLOCK_SIZE] for i in ix])
    return torch.from_numpy(x), torch.from_numpy(y)


@torch.no_grad()
def evaluate(model, va):
    """Non-overlapping blocks; mean loss over all, and by position within the block."""
    model.eval()
    nb = (len(va) - 1) // BLOCK_SIZE
    xs = va[:nb * BLOCK_SIZE].reshape(nb, BLOCK_SIZE); ys = va[1:nb * BLOCK_SIZE + 1].reshape(nb, BLOCK_SIZE)
    by_pos = torch.zeros(BLOCK_SIZE, dtype=torch.float64)
    for i in range(0, nb, 32):
        x = torch.from_numpy(xs[i:i + 32]); y = torch.from_numpy(ys[i:i + 32])
        logits, _ = model(x)
        l = F.cross_entropy(logits.reshape(-1, logits.size(-1)), y.reshape(-1), reduction="none").view(y.shape)
        by_pos += l.double().sum(0)
    by_pos /= nb
    model.train()
    return float(by_pos.mean()), by_pos.tolist()


def train_one(name, horizon, seed, tr, va):
    set_seed(seed)
    cfg = ModelConfig(horizon_k=horizon if horizon else BLOCK_SIZE)
    model = SmallLM(cfg, use_softmax=horizon is None)
    opt = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WD)
    lam = lambda s: s / WARMUP if s < WARMUP else max(0.1, 1.0 - (s - WARMUP) / max(1, STEPS - WARMUP))
    sch = torch.optim.lr_scheduler.LambdaLR(opt, lam)
    rng = np.random.default_rng(seed)
    t0 = time.time()
    for s in range(STEPS):
        x, y = batch(tr, rng)
        _, loss = model(x, y)
        opt.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step(); sch.step()
        if s % 250 == 0:
            print(f"  {name} seed {seed} step {s} loss {loss.item():.3f} {time.time() - t0:.0f}s", flush=True)
    vl, pos = evaluate(model, va)
    r = {"name": name, "K": horizon, "seed": seed, "val_loss": vl, "val_ppl": math.exp(vl), "by_pos": pos,
         "minutes": (time.time() - t0) / 60}
    if horizon is not None:
        r["gamma_sq"] = [(b.attn.temperature.detach().abs() + 1e-6).squeeze().tolist() for b in model.blocks]
    torch.save(model.state_dict(), os.path.join(CKPT, f"{name}-{seed}.pt"))
    print(f"  {name} seed {seed}: val loss {vl:.4f} ppl {math.exp(vl):.2f} ({r['minutes']:.1f} min)", flush=True)
    return r


def load():
    return json.load(open(OUT)) if os.path.exists(OUT) else {"steps": STEPS, "runs": []}


def train_all():
    tr, va = tokens()
    print(f"train {len(tr)} tokens, val {len(va)} tokens, {STEPS} steps a run", flush=True)
    res = load()
    done = {(r["name"], r["seed"]) for r in res["runs"]}
    configs = [("softmax", None)] + [(f"cauchy-K{K}", K) for K in HORIZONS]
    for seed in SEEDS:
        for name, K in configs:
            if (name, seed) in done: continue
            res["runs"].append(train_one(name, K, seed, tr, va))
            json.dump(res, open(OUT, "w"))


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "train"
    if what == "train": train_all()
