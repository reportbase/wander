"""CAH: effective keys of the Cauchy and Gaussian kernels against N (plans/cah-plan.md, CH1).

Run from the repository's root:  python3 runs/cah/effkeys.py
Keys at fixed density about the query (a uniform ball whose volume grows with N), D' dimensions, seeded.
"""
import numpy as np

def eff(w):
    return w.sum() ** 2 / (w ** 2).sum()

rng = np.random.default_rng(1)
Ns = [500, 1000, 2000, 4000, 8000]
for D in (1, 2, 4, 8):
    rows = {"cauchy": [], "gauss": []}
    for N in Ns:
        ec, eg = [], []
        for rep in range(20):
            R = N ** (1 / D)                      # fixed density: volume ∝ N
            u = rng.standard_normal((N, D)); u /= np.linalg.norm(u, axis=1, keepdims=True)
            k = u * (R * rng.random(N) ** (1 / D))[:, None]
            d2 = (k ** 2).sum(1)
            g2 = np.median(np.sort(d2)[:1]) if False else 1.0   # γ = 1 at unit density: the nearest-key scale
            ec.append(eff(1 / (1 + d2 / g2))); eg.append(eff(np.exp(-d2 / (2 * g2))))
        rows["cauchy"].append(np.mean(ec)); rows["gauss"].append(np.mean(eg))
    for kern in rows:
        s = np.polyfit(np.log(Ns), np.log(rows[kern]), 1)[0]
        pred = (D - 2) / D if kern == "cauchy" and D > 2 else 0.0
        print(f"D'={D} {kern:6s} eff keys " + " ".join(f"{v:8.1f}" for v in rows[kern]) + f"  slope {s:+.3f} (pred {pred:+.3f})")
