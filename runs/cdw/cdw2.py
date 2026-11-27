"""CDW run 2: a row of masses, read and pulled back out (SPN R1269; plans/cdw-plan.md, run 2).
Run from the repository's root: python3 runs/cdw/cdw2.py"""
import numpy as np
from mpmath import mp, mpf, nsum, inf, pi, sinh, cosh, cos, coth, tanh
mp.dps = 40

# Q1, Q2: an equal row, exact
w1 = w2 = mpf(0)
for u in [mpf('0.25'), mpf('0.5'), mpf(1), mpf(2)]:
    for x in [mpf(0), mpf('0.3'), mpf('0.5')]:
        s = nsum(lambda n: (u / pi) / (u ** 2 + (x - n) ** 2), [-inf, inf])
        w1 = max(w1, abs(s - sinh(2 * pi * u) / (cosh(2 * pi * u) - cos(2 * pi * x))))
    mx = sinh(2 * pi * u) / (cosh(2 * pi * u) - 1); mn = sinh(2 * pi * u) / (cosh(2 * pi * u) + 1)
    w2 = max(w2, abs((mx - mn) - 2 / sinh(2 * pi * u)), abs((coth(pi * u) - tanh(pi * u)) - 2 / sinh(2 * pi * u)))
print(f"Q1 sum vs closed form: {mp.nstr(w1, 3)}   Q2 ripple vs 2/sinh(2 pi u): {mp.nstr(w2, 3)}")
print("   ripple 2/sinh(2 pi u) at u = 0.25, 0.5, 1, 2:", [mp.nstr(2 / sinh(2 * pi * mpf(u)), 3) for u in ['0.25', '0.5', '1', '2']])

# Q3-Q5: unequal masses, recovered by least squares
P, L, NX = 16, 16.0, 256
rng = np.random.default_rng(1268)
M = 0.5 + rng.random(P)
xs = np.arange(NX) * L / NX
def pull_of(n, u):                      # one mass at x = n, repeated every L, read from u spacings deep (s = 1)
    t = 2 * np.pi * u / L
    return (1 / L) * np.sinh(t) / (np.cosh(t) - np.cos(2 * np.pi * (xs - n) / L))
us = np.round(np.arange(0.25, 8.01, 0.25), 2)
res = {}
for sig in [1e-6, 1e-3]:
    rows = []
    for u in us:
        A = np.stack([pull_of(n, u) for n in range(P)], axis=1)
        g = A @ M
        errs, tots = [], []
        for trial in range(20):
            gn = g + sig * g.max() * rng.standard_normal(NX)
            Mh = np.linalg.lstsq(A, gn, rcond=None)[0]
            errs.append(np.sqrt(np.mean((Mh - M) ** 2))); tots.append(abs(Mh.sum() - M.sum()) / M.sum())
        rows.append((u, np.median(errs), np.max(tots)))
    res[sig] = rows
spread = M.std()
print(f"masses' spread (sd) {spread:.4f}")
for sig, rows in res.items():
    sel = [(u, e) for u, e, _ in rows if 10 * sig < e < 0.05]
    k = np.polyfit([u for u, _ in sel], np.log([e for _, e in sel]), 1)[0] if len(sel) >= 3 else float('nan')
    fail = next((u for u, e, _ in rows if e > spread / 2), None)
    worst_tot = max(t for _, _, t in rows)
    print(f"sigma {sig:g}: slope of ln(err) vs u = {k:.4f} (pi = {np.pi:.4f}, ratio {k/np.pi:.3f}) over {len(sel)} points;"
          f" fails at u = {fail}; worst total-mass error {worst_tot:.2e} ({worst_tot/sig:.2f} sigma)")
    print("   u, rms err: " + ", ".join(f"{u:g}:{e:.1e}" for u, e, _ in rows[::2]))
f6 = next(u for u, e, _ in res[1e-6] if e > spread / 2); f3 = next(u for u, e, _ in res[1e-3] if e > spread / 2)
print(f"failure shift {f6 - f3:.2f} against ln(1000)/pi = {np.log(1000)/np.pi:.2f}")
