"""CAH run 1: the Circle probe's purity (plans/cah-plan.md, C5 and C6).

Run from the repository's root after runs/cah/cah.py:  python3 runs/cah/probe.py
probe_circle_attention is cauchy_horizon_sweep_2.py's, changed only where marked "CAH".
"""
import json, math, os, sys, random, copy
import numpy as np
import torch
from torch.utils.data import DataLoader
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cah
from cah import SmallLM, ModelConfig, CKPT, BLOCK_SIZE


class TextDataset(torch.utils.data.Dataset):   # the script's, every offset
    def __init__(self, tokens, block_size):
        self.tokens = tokens; self.block_size = block_size
    def __len__(self):
        return len(self.tokens) - self.block_size
    def __getitem__(self, idx):
        x = torch.tensor(self.tokens[idx:idx + self.block_size], dtype=torch.long)
        y = torch.tensor(self.tokens[idx + 1:idx + self.block_size + 1], dtype=torch.long)
        return x, y


def probe_circle_attention(cauchy_model, val_dataset, device, block_size,
                           d=6, hs=None, p_star=0.27,
                           n_retrofit_epochs=20, neg_k=16, lr_cw=0.003,
                           n_eval=2000, max_train=None):
    """
    PROBE 4: Circle Attention on Cauchy-trained embeddings

    THE QUESTION:
      The Cauchy model trained with bounded observation geometry.
      Its embeddings should have angular structure that Circle can read.
      Can a tiny projection W (D x E, trained with InfoNCE on frozen embeddings)
      match Cauchy attention accuracy at O(1)?

    METRICS:
      - Purity → should approach 2/pi = 0.6366
      - Product = purity * pi/2 → should approach 1.0
      - Circle accuracy on committed queries vs Cauchy accuracy on same queries
      - Delta = Circle_acc - Cauchy_acc  (positive = Circle wins)
    """
    import math as _math
    import numpy as _np
    from collections import defaultdict as _dd, Counter as _Counter
    import random as _random

    PI = _math.pi
    if hs is None:
        hs = PI / 4.0
    cpd = int(_math.ceil(PI / hs)) + 1  # 5

    cauchy_model.eval()
    E_DIM = cauchy_model.config.n_embd

    # Extract token embedding matrix from Cauchy-trained model
    E_mat = cauchy_model.wte.weight.detach().cpu().numpy().astype(_np.float64)
    CE_DIM = 2 * E_DIM

    print(f"\n  ── Circle Attention Probe ──────────────────────────────")
    print(f"  Embeddings from Cauchy-trained model: {E_mat.shape}")
    print(f"  D={d}  hs=pi/4  CPD={cpd}  Buckets={cpd**d}  p*={p_star}")
    print(f"  Retrofit epochs: {n_retrofit_epochs}  LR={lr_cw}  NEG_K={neg_k}")

    # Build bigram triples from val dataset for InfoNCE training
    # Use context window: for each position, (token[t-1], token[t]) -> token[t+1]
    print(f"\n  Building bigram index from val data...")
    loader = DataLoader(val_dataset, batch_size=32, shuffle=False, num_workers=0)
    triples = []  # (w0, w1, tgt)
    for i, (x, y) in enumerate(loader):
        if i >= 200: break  # enough for InfoNCE
        xn = x.numpy(); yn = y.numpy()
        B, T = xn.shape
        for b in range(B):
            for t in range(T - 1):
                triples.append((int(xn[b, t]), int(xn[b, t+1]), int(yn[b, t+1])))

    _random.shuffle(triples)
    n_eval_triples = min(n_eval, len(triples) // 5)
    train_triples = triples[n_eval_triples:]
    if max_train: train_triples = train_triples[:max_train]   # CAH: cap (plan)
    eval_triples  = triples[:n_eval_triples]

    # Positive-pair index
    tgt_idx = _dd(list)
    for i, (w0, w1, tgt) in enumerate(train_triples):
        tgt_idx[tgt].append(i)

    print(f"  Train triples: {len(train_triples):,}  Eval: {len(eval_triples):,}")

    # Circle projection W (D x CE_DIM)
    rng = _np.random.RandomState(42)
    W    = rng.randn(d, CE_DIM).astype(_np.float64)
    G2_W = _np.full_like(W, 1e-6)
    for di in range(d):
        W[di] /= _np.linalg.norm(W[di]); W[di] *= 1.5

    def get_ctx(w0, w1):
        c = _np.empty(CE_DIM)
        c[:E_DIM] = E_mat[w0]; c[E_DIM:] = E_mat[w1]
        return c

    def project(ctx):
        return (PI/2.0)*(1.0 + _np.tanh(W @ ctx))

    def bucket(th):
        k, b, base = 0, 1, cpd + 1
        for di in range(d):
            c = max(0, min(cpd-1, int(th[di]/hs)))
            k += c*b; b *= base
        return k

    def infonce_step(anchor, pos, negs, temp):
        ta = project(anchor); tp = project(pos)
        sp = float(_np.sum(_np.cos(ta-tp)))/temp
        denom = _math.exp(min(sp, 50))
        tns = [project(n) for n in negs]
        for tn in tns:
            denom += _math.exp(min(float(_np.sum(_np.cos(ta-tn)))/temp, 50))
        gp = -(1.0 - _math.exp(min(sp,50))/denom)
        for di in range(d):
            tv = _math.tanh(float(W[di]@anchor)); dt = 1.0-tv*tv
            sth = _math.sin(ta[di]-tp[di])/temp*gp
            g = sth*dt*anchor
            nm = _np.linalg.norm(g)
            if nm > 1.0: g *= 1.0/nm
            G2_W[di] += g*g; W[di] -= lr_cw*g/_np.sqrt(G2_W[di])

    # KV store
    kv_win = {}; kv_pur = {}

    def build_kv():
        vc = _dd(_Counter)
        for w0,w1,tgt in train_triples:
            vc[bucket(project(get_ctx(w0,w1)))][tgt] += 1
        kv_win.clear(); kv_pur.clear()
        for bk, counts in vc.items():
            tot = sum(counts.values()); t,tc = counts.most_common(1)[0]
            kv_win[bk]=t; kv_pur[bk]=tc/tot

    def mean_purity():
        if not kv_pur: return 0.0
        return sum(kv_pur.values())/len(kv_pur)

    def kv_query(th):
        bk = bucket(th)
        if bk not in kv_win: return -1, 0.0
        return kv_win[bk], kv_pur[bk]

    # Cauchy model prediction for comparison
    def cauchy_predict(w0, w1):
        ids = torch.tensor([[w0, w1]], dtype=torch.long, device=device)
        with torch.no_grad():
            logits, _ = cauchy_model(ids)
        return int(logits[0, -1, :].argmax().item())

    # Measure product BEFORE retrofit
    build_kv()
    pur_before = mean_purity()
    n_buckets_before = len(kv_pur)   # CAH
    prod_before = pur_before * (PI/2)
    print(f"  Product BEFORE retrofit: {prod_before:.4f}  "
          f"(CE-only would be >1, Cauchy-trained TBD)")

    # Retrofit W with InfoNCE
    print(f"\n  {'ep':<4}  {'purity':<8}  {'product':<8}  "
          f"{'commits':<10}  {'circ_acc':<10}  {'cau_acc':<10}  {'delta':<8}")
    print(f"  " + "-"*68)

    temp = 2.0
    for ep in range(1, n_retrofit_epochs+1):
        if ep == 8:  temp = 1.5
        if ep == 14: temp = 1.0
        if ep == 18: temp = 0.5

        _random.shuffle(train_triples)
        for i, (w0, w1, tgt) in enumerate(train_triples):
            same = tgt_idx[tgt]
            if len(same) < 2: continue
            ji = _random.randrange(len(same))
            tries = 0
            while train_triples[same[ji]][:2]==(w0,w1) and tries<5:
                ji=_random.randrange(len(same)); tries+=1
            anchor = get_ctx(w0, w1)
            pw0,pw1,_ = train_triples[same[ji]]
            pos = get_ctx(pw0, pw1)
            negs = []
            for _ in range(neg_k):
                ri = _random.randrange(len(train_triples))
                if train_triples[ri][2] != tgt:
                    negs.append(get_ctx(train_triples[ri][0],
                                        train_triples[ri][1]))
            if negs: infonce_step(anchor, pos, negs, temp)

        if ep == 1 or ep % 5 == 0 or ep == n_retrofit_epochs:
            build_kv()
            pur = mean_purity()
            # Eval on held-out triples
            nc = nd = circ_ok = cau_ok_on_commit = 0
            sample = eval_triples[:min(500, len(eval_triples))]
            for w0,w1,tgt in sample:
                ctx = get_ctx(w0, w1)
                pred, pur_q = kv_query(project(ctx))
                if pred >= 0 and pur_q > p_star:
                    nc += 1
                    if pred == tgt: circ_ok += 1
                    if cauchy_predict(w0, w1) == tgt: cau_ok_on_commit += 1
                else:
                    nd += 1
            circ_acc = circ_ok/nc if nc>0 else 0
            cau_acc  = cau_ok_on_commit/nc if nc>0 else 0
            delta    = circ_acc - cau_acc
            pct = 100*nc/(nc+nd) if nc+nd>0 else 0
            marker = " ***" if delta > 0.01 else ""
            print(f"  {ep:<4}  {pur:<8.4f}  {pur*(PI/2):<8.4f}  "
                  f"{nc}/{nc+nd}({pct:.0f}%)   "
                  f"{circ_acc:<10.4f}  {cau_acc:<10.4f}  "
                  f"{delta:+.4f}{marker}")

    build_kv()
    fp = mean_purity(); fprod = fp*(PI/2)

    # Final eval
    nc=nd=circ_ok=cau_ok=0
    for w0,w1,tgt in eval_triples:
        ctx = get_ctx(w0,w1)
        pred,pur_q = kv_query(project(ctx))
        if pred>=0 and pur_q>p_star:
            nc+=1
            if pred==tgt: circ_ok+=1
            if cauchy_predict(w0,w1)==tgt: cau_ok+=1
        else: nd+=1

    circ_acc = circ_ok/nc if nc>0 else 0
    cau_acc  = cau_ok/nc  if nc>0 else 0
    delta    = circ_acc - cau_acc

    print(f"\n  ── Circle Probe Results ──────────────────────────────")
    print(f"  Product BEFORE retrofit:  {prod_before:.4f}")
    print(f"  Product AFTER  retrofit:  {fprod:.4f}")
    print(f"  Purity:                   {fp:.4f}  (target 2/pi={2/PI:.4f})")
    print(f"  Circle commits:           {nc}/{nc+nd} ({100*nc/(nc+nd):.1f}%)")
    print(f"  Circle acc on commits:    {circ_acc:.4f}")
    print(f"  Cauchy acc on same:       {cau_acc:.4f}")
    print(f"  Delta (Circle - Cauchy):  {delta:+.4f}  "
          f"{'*** CIRCLE MATCHES/BEATS CAUCHY' if delta >= -0.02 else 'Cauchy wins'}")
    print(f"  ─────────────────────────────────────────────────────")

    return {
        'purity_before': round(prod_before, 4),
        'purity_before_raw': round(pur_before, 4),   # CAH: the purity itself
        'n_buckets_before': n_buckets_before,   # CAH

        'purity_after':  round(fp, 4),
        'product_after': round(fprod, 4),
        'n_commits':     nc,
        'n_total':       nc+nd,
        'commit_rate':   round(nc/(nc+nd) if nc+nd>0 else 0, 4),
        'circle_acc':    round(circ_acc, 4),
        'cauchy_acc':    round(cau_acc,  4),
        'delta':         round(delta, 4),
    }



def model(name, K):
    m = SmallLM(ModelConfig(horizon_k=K or BLOCK_SIZE), use_softmax=K is None)
    m.load_state_dict(torch.load(os.path.join(CKPT, f"{name}-42.pt"))); m.eval(); return m


if __name__ == "__main__":
    tr, va = cah.tokens()
    val = TextDataset(va.tolist(), BLOCK_SIZE)
    cau = model("cauchy-K163", 163); sm = model("softmax", None)
    rnd = copy.deepcopy(cau)
    torch.manual_seed(7)
    sd = float(cau.wte.weight.std())
    with torch.no_grad():
        rnd.wte.weight.copy_(torch.randn_like(rnd.wte.weight) * sd)
    out = {"C5": {}, "C6": None, "two_over_pi": 2 / math.pi}
    for D in (4, 6, 8):
        for name, m in (("cauchy-K163", cau), ("softmax", sm), ("random", rnd)):
            random.seed(42)
            r = probe_circle_attention(m, val, "cpu", BLOCK_SIZE, d=D, n_retrofit_epochs=0, max_train=20000, n_eval=500)
            out["C5"][f"{name} D={D}"] = r
            print(f"C5 {name} D={D}: purity {r['purity_before_raw']:.4f}, occupied cells {r['n_buckets_before']}", flush=True)
            json.dump(out, open(os.path.join(cah.HERE, "cah-probe.json"), "w"), indent=1)
    random.seed(42)
    out["C6"] = probe_circle_attention(cau, val, "cpu", BLOCK_SIZE, d=6, n_retrofit_epochs=5, max_train=20000, n_eval=500)
    json.dump(out, open(os.path.join(cah.HERE, "cah-probe.json"), "w"), indent=1)
    print("C6", out["C6"], flush=True)
