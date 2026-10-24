"""CAH: CH1' (plans/cah-plan.md), the effective-key count with the corrected exponent.

Run from the repository's root:  python3 runs/cah/effkeys2.py
"""
import numpy as np

def eff(w):
    return w.sum() ** 2 / (w ** 2).sum()

rng = np.random.default_rng(2)

def keys(N, D):
    u = rng.standard_normal((N, D)); u /= np.linalg.norm(u, axis=1, keepdims=True)
    return ((u * (N ** (1 / D) * rng.random(N) ** (1 / D))[:, None]) ** 2).sum(1)

def slope(Ns, D, kern, reps):
    ys = []
    for N in Ns:
        vals = []
        for _ in range(reps):
            d2 = keys(N, D)
            vals.append(eff(1 / (1 + d2)) if kern == "cauchy" else eff(np.exp(-d2 / 2)))
        ys.append(np.mean(vals))
    return np.polyfit(np.log(Ns), np.log(ys), 1)[0], ys

Ns = [500, 1000, 2000, 4000, 8000]
mid = np.exp(np.mean(np.log(Ns)))
checks = []
for D, pred, tol in ((3, 2 / 3, 0.1), (4, 1 - 1 / np.log(mid), 0.1), (8, 1.0, 0.05)):
    s, ys = slope(Ns, D, "cauchy", 20)
    ok = abs(s - pred) <= tol; checks.append(ok)
    print(f"Cauchy D'={D}: eff {' '.join(f'{y:.1f}' for y in ys)}; slope {s:.3f}, predicted {pred:.3f} ± {tol}: {'ok' if ok else 'KILLED'}")
NG = [65536, 131072, 262144, 524288]
s, ys = slope(NG, 8, "gauss", 4)
ok = s < 0.1; checks.append(ok)
print(f"Gaussian D'=8: eff {' '.join(f'{y:.1f}' for y in ys)}; slope {s:.3f}, predicted < 0.1: {'ok' if ok else 'KILLED'}")
print("CH1'", "not killed" if all(checks) else "KILLED")
