"""SHD: one shared denominator against orthogonal axes (plans/shd-plan.md).

Part 1 seeded checks E1, E2. Part 2 on GloVe 50d and two human similarity lists: E3, D1-D5.
Run from the repository's root: python3 runs/shd/shd.py DATA_DIR
DATA_DIR holds glove50.gz (gensim-data glove-wiki-gigaword-50), simlex.txt, ws353.txt (sha256s in the plan).
"""
import gzip, sys
import numpy as np
from scipy.special import betainc
from scipy.stats import spearmanr

rng = np.random.default_rng(20261116)
N = 400_000
LAWS = {
    "normal": lambda size: rng.standard_normal(size),
    "uniform": lambda size: rng.uniform(0, 1, size),
    "exponential": lambda size: rng.exponential(1, size),
}

print("== Part 1 ==")
print("E1: correlation of ln|v_i/h| and ln|v_j/h| (shared) and with own denominators")
e1 = True
for name, law in LAWS.items():
    h, v1, v2, h2 = (np.abs(law(N)) for _ in range(4))
    a, b, c = np.log(v1 / h), np.log(v2 / h), np.log(v2 / h2)
    rs, ro = np.corrcoef(a, b)[0, 1], np.corrcoef(a, c)[0, 1]
    se = (1 - 0.25) / np.sqrt(N)  # se of r near 1/2
    ok = abs(rs - 0.5) < 3 * se and abs(ro) < 3 / np.sqrt(N)
    e1 &= ok
    print(f"  {name:12s} shared {rs:.4f}  own {ro:+.4f}  {'ok' if ok else 'MISS'}")
print("  E1", "not killed" if e1 else "KILLED")

print("E2: share with every |s_i| <= 1, shared h against own h")
e2 = True
for name, law in LAWS.items():
    for n in range(1, 9):
        h = np.abs(law(N)); x = np.abs(law((N, n))); ho = np.abs(law((N, n)))
        ps = (x <= h[:, None]).all(1).mean(); po = (x <= ho).all(1).mean()
        es, eo = 1 / (n + 1), 0.5 ** n
        ok = abs(ps - es) < 3 * np.sqrt(es * (1 - es) / N) and abs(po - eo) < 3 * np.sqrt(eo * (1 - eo) / N)
        e2 &= ok
        if n in (1, 2, 4, 8):
            print(f"  {name:12s} n={n}: shared {ps:.4f} (1/(n+1) {es:.4f})  own {po:.4f} (1/2^n {eo:.4f})  {'ok' if ok else 'MISS'}")
print("  E2", "not killed" if e2 else "KILLED")

print("== Part 2 ==")
d = sys.argv[1]
words, rows = [], []
with gzip.open(f"{d}/glove50.gz", "rt", encoding="utf8") as f:
    next(f)
    for line in f:
        p = line.rstrip().split(" ")
        words.append(p[0]); rows.append(np.array(p[1:], dtype=np.float64))
E = np.vstack(rows); idx = {w: i for i, w in enumerate(words)}
print(f"  {E.shape[0]} words, {E.shape[1]} dimensions")

def pairs(path):
    out = []
    for line in open(path, encoding="utf8"):
        a, b, s = line.split()
        if a.lower() in idx and b.lower() in idx:
            out.append((idx[a.lower()], idx[b.lower()], float(s)))
    return out

def m_cos(A, B): return np.sum(A * B, 1) / np.linalg.norm(A, axis=1) / np.linalg.norm(B, axis=1)
def m_euc(A, B): return -np.linalg.norm(A - B, axis=1)
def m_s(A, B):
    """|s| = |v|/h in a's frame (h along a, v the rest); similarity = -|s|, h <= 0 behind the look (-inf)."""
    q = A / np.linalg.norm(A, axis=1)[:, None]
    h = np.sum(B * q, 1); v = np.linalg.norm(B - h[:, None] * q, axis=1)
    return np.where(h > 0, -v / np.where(h > 0, h, 1), -np.inf), h > 0
def m_own(A, B): return -np.median(np.abs(np.log(np.abs(B) / np.abs(A))), 1)

res = {}
for name in ("simlex", "ws353"):
    P = pairs(f"{d}/{name}.txt")
    ia, ib, gold = (np.array(c) for c in zip(*P))
    A, B = E[ia], E[ib]
    k = np.exp(rng.uniform(-2, 2, E.shape[0]))  # each thing scaled by its own factor
    As, Bs = A * k[ia][:, None], B * k[ib][:, None]
    r = {}
    r["cos"] = spearmanr(m_cos(A, B), gold)[0]
    r["euc"] = spearmanr(m_euc(A, B), gold)[0]
    s, front = m_s(A, B)
    r["s"] = spearmanr(s, gold)[0]
    r["own"] = spearmanr(m_own(A, B), gold)[0]
    r["e3"] = spearmanr(s[front], m_cos(A, B)[front])[0]
    r["front"] = front.mean()
    r["cos_k"] = spearmanr(m_cos(As, Bs), gold)[0]
    r["s_k"] = spearmanr(m_s(As, Bs)[0], gold)[0]
    r["euc_k"] = spearmanr(m_euc(As, Bs), gold)[0]
    r["own_k"] = spearmanr(m_own(As, Bs), gold)[0]
    r["n"] = len(P)
    res[name] = r
    print(f"  {name}: {r['n']} pairs, front {r['front']:.3f}")
    print(f"    Spearman  cos {r['cos']:.4f}  euc {r['euc']:.4f}  |s| {r['s']:.4f}  own {r['own']:.4f}")
    print(f"    scaled    cos {r['cos_k']:.4f}  euc {r['euc_k']:.4f}  |s| {r['s_k']:.4f}  own {r['own_k']:.4f}")
    print(f"    E3 Spearman(|s|, cos) on pairs in front {r['e3']:.15f}")

e3 = all(abs(r["e3"] - 1) < 1e-12 for r in res.values())
d1 = all(r["cos"] > r["euc"] for r in res.values())
d2 = all(abs(r["cos_k"] - r["cos"]) < 1e-12 and abs(r["s_k"] - r["s"]) < 1e-12 and r["euc"] - r["euc_k"] >= 0.05
         for r in res.values())
d3 = all(r["cos"] - r["own"] >= 0.05 for r in res.values())
print("  E3", "not killed" if e3 else "KILLED")
print("  D1", "not killed" if d1 else "KILLED")
print("  D2", "not killed" if d2 else "KILLED")
print("  D3", "not killed" if d3 else "KILLED")

U = E / np.linalg.norm(E, axis=1)[:, None]
n = E.shape[1] - 1
uni = betainc(n / 2, 0.5, 0.5)
qs = rng.choice(E.shape[0], 1000, replace=False)
def share45(U, qs):
    c = np.cos(np.pi / 4); tot = 0.0
    for j in range(0, len(qs), 50):
        tot += (U @ U[qs[j:j + 50]].T > c).sum(0).astype(float).sum() / U.shape[0]
    return tot / len(qs)
s_raw = share45(U, qs)
C = E - E.mean(0); Uc = C / np.linalg.norm(C, axis=1)[:, None]
s_cen = share45(Uc, qs)
print(f"  uniform hemisphere share within 45 deg (n = {n}): {uni:.3e}")
print(f"  vocabulary within 45 deg of a query: raw {s_raw:.4e} ({s_raw/uni:.3g} x uniform), centred {s_cen:.4e} ({s_cen/uni:.3g} x)")
d4 = s_raw >= 10 * uni
d5 = s_cen <= 0.5 * s_raw
print("  D4", "not killed" if d4 else "KILLED")
print("  D5", "not killed" if d5 else "KILLED")
