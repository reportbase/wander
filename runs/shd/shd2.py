"""SHD run 2 (plans/shd-plan.md): E1' with spread from repeats; E3', D2' with readings rounded to 12 figures.
python3 runs/shd/shd2.py DATA_DIR"""
import sys, io, contextlib, runpy
import numpy as np
from scipy.stats import spearmanr

rng = np.random.default_rng(20261117)
N, R = 400_000, 200
laws = {"normal": lambda s: rng.standard_normal(s), "uniform": lambda s: rng.uniform(0, 1, s),
        "exponential": lambda s: rng.exponential(1, s)}
ok1 = True
for name, law in laws.items():
    sh, ow = [], []
    for _ in range(R):
        h, v1, v2, h2 = (np.abs(law(N)) for _ in range(4))
        a = np.log(v1 / h)
        sh.append(np.corrcoef(a, np.log(v2 / h))[0, 1]); ow.append(np.corrcoef(a, np.log(v2 / h2))[0, 1])
    sh, ow = np.array(sh), np.array(ow)
    o = abs(sh.mean() - .5) < 3 * sh.std() / np.sqrt(R) and abs(ow.mean()) < 3 * ow.std() / np.sqrt(R)
    ok1 &= o
    print(f"E1' {name:12s} shared mean {sh.mean():.5f} spread {sh.std():.5f}  own mean {ow.mean():+.5f} spread {ow.std():.5f}  {'ok' if o else 'MISS'}")
print("E1'", "not killed" if ok1 else "KILLED")

d = sys.argv[1]
sys.argv = ["shd.py", d]
with contextlib.redirect_stdout(io.StringIO()):
    g = runpy.run_path("runs/shd/shd.py")  # loads data and measures; its own seeded draws are discarded
E, m_cos, m_s, m_euc, pairs = g["E"], g["m_cos"], g["m_s"], g["m_euc"], g["pairs"]
r12 = lambda x: np.array([float(f"{v:.12g}") if np.isfinite(v) else v for v in x])
k = np.exp(np.random.default_rng(20261116).uniform(-2, 2, E.shape[0]))
ok3 = ok2 = True
for name in ("simlex", "ws353"):
    P = pairs(f"{d}/{name}.txt"); ia, ib, gold = (np.array(c) for c in zip(*P))
    A, B = E[ia], E[ib]; As, Bs = A * k[ia][:, None], B * k[ib][:, None]
    c, (s, f) = r12(m_cos(A, B)), m_s(A, B); s = r12(s)
    cs, ss, e, es = r12(m_cos(As, Bs)), r12(m_s(As, Bs)[0]), m_euc(A, B), m_euc(As, Bs)
    e3 = spearmanr(s[f], c[f])[0]
    dc = spearmanr(cs, gold)[0] - spearmanr(c, gold)[0]
    ds = spearmanr(ss, gold)[0] - spearmanr(s, gold)[0]
    de = spearmanr(e, gold)[0] - spearmanr(es, gold)[0]
    ok3 &= abs(e3 - 1) < 1e-12
    ok2 &= abs(dc) < 1e-12 and abs(ds) < 1e-12 and de >= 0.05
    print(f"{name}: E3' Spearman(|s|, cos) {e3:.15f}; D2' change cos {dc:.1e}, |s| {ds:.1e}, Euclidean fall {de:.4f}")
print("E3'", "not killed" if ok3 else "KILLED")
print("D2'", "not killed" if ok2 else "KILLED")
