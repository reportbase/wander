"""RAT: attention as a read (plans/rat-plan.md).

Run from the repository's root:
  python3 runs/rat/rat.py exact     # A1, before training
  python3 runs/rat/rat.py train     # four arms x three seeds (resumes)
  python3 runs/rat/rat.py back      # A4 on the trained softmax models
  python3 runs/rat/rat.py report    # A2, A3, A5
The model, data and training are CAH's (runs/cah/cah.py), unchanged except the attention module.
"""
import json, math, os, sys, time
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cah"))
import cah  # noqa: E402  (ModelConfig, MLP, SoftmaxAttention, tokens, batch, evaluate, set_seed, constants)

torch.set_num_threads(4)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "rat-results.json")
CKPT = os.environ.get("RAT_CKPT", "/tmp/rat-ckpt")
os.makedirs(CKPT, exist_ok=True)
cah.CKPT = os.environ.get("CAH_CKPT", "/tmp/cah-ckpt"); os.makedirs(cah.CKPT, exist_ok=True)
ARMS = ["softmax", "cauchy-amount", "read-front", "read-both"]
SEEDS = [42, 137, 2024]
EPS = 1e-12


# ---- the weights, as plain functions (used by the modules and by A1) ----
def w_softmax(q, k, scale):
    return (q @ k.transpose(-2, -1)) * scale  # scores; softmax applied after masking


def w_amount(q, k, gamma_sq):
    d2 = (q * q).sum(-1, keepdim=True) + (k * k).sum(-1, keepdim=True).transpose(-2, -1) - 2 * q @ k.transpose(-2, -1)
    return 1.0 / (1.0 + d2.clamp(min=0) / gamma_sq)


def w_read(q, k, H, front):
    """The plane's Cauchy heat on the slope s = v/h read from the query: h^2 / (h^2 + v^2/H^2)."""
    qn = q / (q.norm(dim=-1, keepdim=True) + EPS)
    h = qn @ k.transpose(-2, -1)                                  # reach along the look
    k2 = (k * k).sum(-1, keepdim=True).transpose(-2, -1)
    v2 = (k2 - h * h).clamp(min=0)                                # reach square to the look, squared
    w = h * h / (h * h + v2 / (H * H) + EPS)
    if front:
        w = w * (h > 0).to(w.dtype)
    return w, h


class Attn(nn.Module):
    def __init__(self, cfg, arm):
        super().__init__()
        self.arm, self.nh, self.ne = arm, cfg.n_head, cfg.n_embd
        self.hd = cfg.n_embd // cfg.n_head
        self.c_attn = nn.Linear(cfg.n_embd, 3 * cfg.n_embd)
        self.c_proj = nn.Linear(cfg.n_embd, cfg.n_embd)
        self.drop_a, self.drop_r = nn.Dropout(cfg.dropout), nn.Dropout(cfg.dropout)
        if arm == "cauchy-amount":
            self.temperature = nn.Parameter(torch.ones(self.nh, 1, 1))
        if arm.startswith("read"):
            self.thumb = nn.Parameter(torch.ones(self.nh, 1, 1))
        self.register_buffer("mask", torch.tril(torch.ones(cfg.block_size, cfg.block_size)).view(1, 1, cfg.block_size,
                                                                                              cfg.block_size))
        self.last_back = None

    def forward(self, x):
        B, T, C = x.shape
        q, k, v = self.c_attn(x).split(self.ne, dim=-1)
        q, k, v = (t.view(B, T, self.nh, self.hd).transpose(1, 2) for t in (q, k, v))
        m = self.mask[:, :, :T, :T]
        if self.arm == "softmax":
            s = w_softmax(q, k, 1.0 / math.sqrt(self.hd)).masked_fill(m == 0, float("-inf"))
            att = F.softmax(s, dim=-1)
            if not self.training:
                behind = ((q @ k.transpose(-2, -1)) <= 0).to(att.dtype) * m
                self.last_back = float((att * behind).sum() / att.sum())
        else:
            if self.arm == "cauchy-amount":
                att = w_amount(q, k, self.temperature.abs() + 1e-6)
            else:
                att, _ = w_read(q, k, self.thumb.abs() + 1e-6, front=self.arm == "read-front")
            att = att * m
            att = att / (att.sum(-1, keepdim=True) + 1e-8)
        y = self.drop_a(att) @ v
        return self.drop_r(self.c_proj(y.transpose(1, 2).contiguous().view(B, T, C)))


class Block(nn.Module):
    def __init__(self, cfg, arm):
        super().__init__()
        self.ln_1, self.ln_2 = nn.LayerNorm(cfg.n_embd), nn.LayerNorm(cfg.n_embd)
        self.attn, self.mlp = Attn(cfg, arm), cah.MLP(cfg)

    def forward(self, x):
        x = x + self.attn(self.ln_1(x))
        return x + self.mlp(self.ln_2(x))


class LM(cah.SmallLM):
    def __init__(self, cfg, arm):
        super().__init__(cfg, use_softmax=True)
        self.blocks = nn.ModuleList([Block(cfg, arm) for _ in range(cfg.n_layer)])
        self.apply(self._init_weights)


def exact():
    g = torch.Generator().manual_seed(7)
    q = torch.randn(1, 1, 12, 16, dtype=torch.float64, generator=g)
    k = torch.randn(1, 1, 12, 16, dtype=torch.float64, generator=g)
    fk = torch.exp(torch.rand(1, 1, 12, 1, dtype=torch.float64, generator=g) * 4 - 2)
    fq = torch.exp(torch.rand(1, 1, 12, 1, dtype=torch.float64, generator=g) * 4 - 2)
    H = torch.tensor(0.7, dtype=torch.float64)
    norm = lambda w: w / w.sum(-1, keepdim=True)
    out = {}
    for front in (True, False):
        a, h = w_read(q, k, H, front)
        b, _ = w_read(q, k * fk, H, front)
        c, _ = w_read(q * fq, k, H, front)
        out["read-front" if front else "read-both"] = {
            "keys scaled": float((norm(a) - norm(b)).abs().max()), "query scaled": float((norm(a) - norm(c)).abs().max())}
    a, h = w_read(q, k, H, True)
    out["read-front weight on h<=0"] = float(a[h <= 0].abs().max())
    s1 = F.softmax(w_softmax(q, k, 0.25), -1); s2 = F.softmax(w_softmax(q, k * fk, 0.25), -1)
    out["softmax keys scaled"] = float((s1 - s2).abs().max())
    out["softmax min weight on q.k<=0"] = float(s1[(q @ k.transpose(-2, -1)) <= 0].min())
    c1 = norm(w_amount(q, k, 1.0)); c2 = norm(w_amount(q, k * fk, 1.0))
    out["amount keys scaled"] = float((c1 - c2).abs().max())
    ok = (all(v < 1e-12 for d in ("read-front", "read-both") for v in out[d].values())
          and out["read-front weight on h<=0"] == 0 and out["softmax keys scaled"] > 1e-3
          and out["amount keys scaled"] > 1e-3 and out["softmax min weight on q.k<=0"] > 0)
    out["A1"] = "not killed" if ok else "KILLED"
    print(json.dumps(out, indent=1))
    return out


def train_one(arm, seed, tr, va):
    cah.set_seed(seed)
    cfg = cah.ModelConfig(horizon_k=cah.BLOCK_SIZE)
    model = LM(cfg, arm)
    opt = torch.optim.AdamW(model.parameters(), lr=cah.LR, weight_decay=cah.WD)
    lam = lambda s: s / cah.WARMUP if s < cah.WARMUP else max(0.1, 1.0 - (s - cah.WARMUP) / max(1, cah.STEPS - cah.WARMUP))
    sch = torch.optim.lr_scheduler.LambdaLR(opt, lam)
    rng = np.random.default_rng(seed)
    t0 = time.time()
    for s in range(cah.STEPS):
        x, y = cah.batch(tr, rng)
        _, loss = model(x, y)
        opt.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step(); sch.step()
        if s % 100 == 0:
            print(f"  {arm} seed {seed} step {s} loss {loss.item():.3f} {time.time() - t0:.0f}s", flush=True)
    vl, _ = cah.evaluate(model, va)
    r = {"arm": arm, "seed": seed, "val_loss": vl, "val_ppl": math.exp(vl), "minutes": (time.time() - t0) / 60}
    if arm.startswith("read"):
        r["thumb"] = [(b.attn.thumb.detach().abs() + 1e-6).squeeze().tolist() for b in model.blocks]
    torch.save(model.state_dict(), os.path.join(CKPT, f"{arm}-{seed}.pt"))
    print(f"  {arm} seed {seed}: val loss {vl:.4f} ppl {math.exp(vl):.2f} ({r['minutes']:.1f} min)", flush=True)
    return r


def load():
    return json.load(open(OUT)) if os.path.exists(OUT) else {"steps": cah.STEPS, "runs": []}


def train_all():
    tr, va = cah.tokens()
    res = load(); done = {(r["arm"], r["seed"]) for r in res["runs"]}
    for seed in SEEDS:
        for arm in ARMS:
            if (arm, seed) in done: continue
            res["runs"].append(train_one(arm, seed, tr, va)); json.dump(res, open(OUT, "w"), indent=1)


@torch.no_grad()
def back():
    tr, va = cah.tokens(); res = load(); shares = []
    for seed in SEEDS:
        m = LM(cah.ModelConfig(horizon_k=cah.BLOCK_SIZE), "softmax")
        m.load_state_dict(torch.load(os.path.join(CKPT, f"softmax-{seed}.pt"))); m.eval()
        nb = (len(va) - 1) // cah.BLOCK_SIZE; xs = va[:nb * cah.BLOCK_SIZE].reshape(nb, cah.BLOCK_SIZE)
        vals = []
        for i in range(0, nb, 32):
            m(torch.from_numpy(xs[i:i + 32])); vals += [b.attn.last_back for b in m.blocks]
        shares.append(float(np.mean(vals)))
    res["A4"] = {"back share per seed": shares, "mean": float(np.mean(shares)),
                 "verdict": "not killed" if np.mean(shares) < 0.2 else "KILLED"}
    json.dump(res, open(OUT, "w"), indent=1); print(json.dumps(res["A4"], indent=1))


def report():
    res = load(); by = {}
    for r in res["runs"]: by.setdefault(r["arm"], []).append(r["val_ppl"])
    st = {a: (float(np.mean(v)), float(np.std(v, ddof=1) / math.sqrt(len(v))) if len(v) > 1 else float("nan"), v)
          for a, v in by.items()}
    for a, (m, se, v) in st.items(): print(f"{a:14s} mean ppl {m:8.2f}  se {se:.2f}  {['%.2f' % x for x in v]}")
    def diff(a, b): ma, sa, _ = st[a]; mb, sb, _ = st[b]; return ma / mb - 1, math.hypot(sa, sb) / mb
    rf, sm = st["read-front"][0], st["softmax"][0]
    A2 = "not killed" if rf <= sm * 1.05 else "KILLED"
    d3, e3 = diff("read-front", "read-both"); A3 = "KILLED" if (d3 > 0.01 and d3 > 2 * e3) else "not killed"
    d5, e5 = diff("read-front", "cauchy-amount"); A5 = "KILLED" if (d5 > 0.02 and d5 > 2 * e5) else "not killed"
    res["verdicts"] = {"A2": [A2, rf / sm - 1], "A3": [A3, d3, e3], "A5": [A5, d5, e5]}
    json.dump(res, open(OUT, "w"), indent=1); print(json.dumps(res["verdicts"], indent=1))


if __name__ == "__main__":
    {"exact": exact, "train": train_all, "back": back, "report": report}[sys.argv[1] if len(sys.argv) > 1 else "train"]()
