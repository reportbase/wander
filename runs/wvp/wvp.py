"""WVP run 1: the interior reader's arrivals building the exterior reader's pattern (plans/wvp-plan.md, SPN R270).
Each arrival is a direction θ even on [0, π/2]; reading s = tan θ, square h² = cos²θ. 400 seeded runs per N.
Run: python3 runs/wvp/wvp.py   (numpy; under a minute)
"""
import numpy as np
from math import pi, log, sqrt, asin

R, Ns = 400, [10**2, 10**3, 10**4, 10**5]
out = {}
for N in Ns:
    D, med, mean, sq, share, shadow = [], [], [], [], [], []
    for seed in range(R):
        th = np.random.default_rng(seed * 1000 + int(log(N, 10))).uniform(0, pi / 2, N)
        u = np.sort(th) / (pi / 2)
        i = np.arange(1, N + 1)
        D.append(max((i / N - u).max(), (u - (i - 1) / N).max()))
        s = np.tan(th)
        med.append(np.median(np.log(s))); mean.append(s.mean())
        h2 = np.cos(th) ** 2
        sq.append(h2.mean()); share.append((h2 <= 0.25).mean()); shadow.append(np.cos(th).mean())
    out[N] = dict(D=np.mean(D), med=np.mean(med), medsd=np.std(med, ddof=1), meanmed=np.median(mean),
                  meaniqr=np.subtract(*np.percentile(mean, [75, 25])), sq=np.mean(sq), share=np.mean(share),
                  prod=np.mean([(pi / 2) * x for x in shadow]))
    o = out[N]
    print(f"N={N:>6}: D {o['D']:.5f} (√N·D {sqrt(N)*o['D']:.4f}); median ln s {o['med']:+.5f}, √N·sd {sqrt(N)*o['medsd']:.4f}; "
          f"mean s median {o['meanmed']:.3f} IQR {o['meaniqr']:.3f}; h² {o['sq']:.5f}; share≤¼ {o['share']:.5f}; "
          f"π/2·shadow {o['prod']:.5f}")

v = {}
lx = np.log(Ns); ly = np.log([out[N]['D'] for N in Ns])
slope = np.polyfit(lx, ly, 1)[0]; k = sqrt(1e5) * out[10**5]['D']
v['P1'] = (-0.55 <= slope <= -0.45) and abs(k - sqrt(pi / 2) * log(2)) <= 0.05
print(f"P1: slope {slope:.4f}, √N·mean D at 1e5 {k:.4f} vs {sqrt(pi/2)*log(2):.4f}")
ok2 = all(abs(out[N]['med']) <= 3 * out[N]['medsd'] / sqrt(R) for N in Ns)
sp = [sqrt(N) * out[N]['medsd'] for N in Ns if N >= 10**3]
v['P2'] = ok2 and all(abs(x / (pi / 2) - 1) <= 0.05 for x in sp)
print(f"P2: medians within 3 se: {ok2}; √N·sd at 1e3..1e5 {[round(x,4) for x in sp]} vs π/2 = {pi/2:.4f}")
steps = [out[Ns[j + 1]]['meanmed'] - out[Ns[j]]['meanmed'] for j in range(3)]
ratio = out[10**2]['meaniqr'] / out[10**5]['meaniqr']
v['P3'] = all(abs(st - 2 / pi * log(10)) <= 0.15 for st in steps) and ratio <= 2
print(f"P3: decade steps {[round(x,3) for x in steps]} vs {2/pi*log(10):.3f}; IQR shrink 1e2→1e5 ×{ratio:.2f}")
o = out[10**5]; n = R * 10**5
e1 = abs(o['sq'] - 0.5) / sqrt(1 / 8 / n); e2 = abs(o['share'] - 1 / 3) / sqrt(2 / 9 / n)
v['P4'] = e1 <= 4 and e2 <= 4
print(f"P4: h² mean off ½ by {e1:.2f} se; share≤¼ off ⅓ by {e2:.2f} se (arcsine (2/π)asin(½) = {2/pi*asin(0.5):.6f})")
e5 = abs(o['prod'] - 1) / ((pi / 2) * sqrt((0.5 - 4 / pi**2) / n))
v['P5'] = e5 <= 4
print(f"P5: (π/2)·mean shadow off 1 by {e5:.2f} se")
for p, ok in v.items(): print(p, 'not killed' if ok else 'KILLED')
