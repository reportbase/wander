# FCL run 11: the depth rule on a measured gravity profile (plans/fcl-plan.md, "Run 11").
# Run from the repository's root: python3 runs/fcl/fcl11.py
# Data: Blecha and Masin, Brezno railway tunnel, Figure 2a/2b, residual anomaly in mGal, read from the figure
# (not published as a table). Medford: Butler 1983, WES TR GL-83-1 report 1, Figure 43, microGal, read by eye.
import numpy as np
from scipy.optimize import least_squares

X = np.arange(0, 101, 5.0)
P1 = np.array([-0.0046, 0.0075, 0.0045, -0.0028, -0.0053, -0.0059, -0.0187, -0.0269, -0.0273, -0.0334, -0.0455,
               -0.0444, -0.0388, -0.0289, -0.0153, -0.0129, 0.0054, -0.0072, 0.0000, -0.0062, 0.0079])
P2 = np.array([0.0010, -0.0016, -0.0024, -0.0019, 0.0048, -0.0074, -0.0213, -0.0182, -0.0320, -0.0402, -0.0431,
               -0.0291, -0.0271, -0.0107, -0.0096, -0.0033, 0.0018, 0.0037, -0.0009, -0.0072, 0.0026])
SIG = 0.004
MID = {'P1': 16.25, 'P2': 17.25}
BOX = {'P1': (12.5, 20.0), 'P2': (13.5, 21.0)}

def line(p, x):  c, A, x0, d = p; return c - A * d / ((x - x0) ** 2 + d * d)
def ball(p, x):  c, A, x0, d = p; return c - A * d ** 3 / ((x - x0) ** 2 + d * d) ** 1.5

def fit(model, x, y, sig, start):
    best = None
    for d0 in (start, start / 2, start * 2):
        A0 = -y.min() * (d0 if model is line else 1)
        r = least_squares(lambda p: (model(p, x) - y) / sig, [0.0, A0, x[np.argmin(y)], d0])
        if best is None or r.cost < best.cost: best = r
    cov = np.linalg.inv(best.jac.T @ best.jac)
    return best.x, np.sqrt(np.diag(cov)), 2 * best.cost

def boot(model, x, y, sig, p, n=2000, seed=11):
    rng = np.random.default_rng(seed); res = y - model(p, x); out = []
    for _ in range(n):
        yb = model(p, x) + rng.choice(res, len(res))
        r = least_squares(lambda q: (model(q, x) - yb) / sig, p)
        out.append(r.x[3])
    return np.std(out)

print("FCL run 11: Brezno tunnel")
fits = {}
for name, y in (('P1', P1), ('P2', P2)):
    pl, el, chl = fit(line, X, y, SIG, 16.0)
    pb, eb, chb = fit(ball, X, y, SIG, 20.0)
    bl = boot(line, X, y, SIG, pl)
    fits[name] = (pl, el, chl, pb, eb, chb, bl)
    dof = len(X) - 4
    print(f"\n{name}: mid-height {MID[name]} m, roof-floor {BOX[name]}")
    print(f"  line: d = {abs(pl[3]):.2f} +- {el[3]:.2f} m (bootstrap {bl:.2f}), x0 = {pl[2]:.2f} +- {el[2]:.2f} m, "
          f"A = {pl[1]:.4f} mGal m, c = {pl[0]:.4f}, chi2 = {chl:.1f} on {dof}, per dof {chl/dof:.2f}")
    print(f"  ball: d = {abs(pb[3]):.2f} +- {eb[3]:.2f} m, x0 = {pb[2]:.2f}, chi2 = {chb:.1f}; "
          f"ratio ball/line = {abs(pb[3])/abs(pl[3]):.3f}; chi2 ball - line = {chb-chl:+.2f}")
    print(f"  (d - mid)/se = {(abs(pl[3]) - MID[name])/el[3]:+.2f} (covariance), {(abs(pl[3]) - MID[name])/bl:+.2f} (bootstrap)")
    # D5: every value times 7
    p7, _, _ = fit(line, X, 7 * y, 7 * SIG, 16.0)
    print(f"  D5: values x 7: d changes by {abs(abs(p7[3]) - abs(pl[3]))/abs(pl[3]):.1e}, x0 by {abs(p7[2]-pl[2])/pl[2]:.1e}")
    G = 6.6743e-11
    lam = pl[1] * 1e-5 / (2 * G)          # kg per metre (A in mGal m -> m/s2 m)
    print(f"  missing mass per metre A/(2G) = {lam/1000:.1f} t/m; over 43.7 m2 that is {lam/43.7:.0f} kg/m3")

w = {n: 1 / fits[n][1][3] ** 2 for n in fits}
dm = sum(w[n] * abs(fits[n][0][3]) for n in fits) / sum(w.values())
wb = {n: 1 / fits[n][4][3] ** 2 for n in fits}
db = sum(wb[n] * abs(fits[n][3][3]) for n in fits) / sum(wb.values())
print(f"\nweighted mean, line: {dm:.2f} +- {sum(w.values())**-0.5:.2f} m against 16.75 m ({100*(dm/16.75-1):+.1f}%)")
print(f"weighted mean, ball: {db:.2f} m (floors 20 and 21 m)")

# the regional's pull on the width (reported, not predicted): a noise-free line curve of depth 16.25 treated as the
# authors treated theirs (a straight line fitted on 0-20 and 80-100 taken out), then fitted
yt = line([0, 16.25 * 0.045, 50, 16.25], X)
ends = (X <= 20) | (X >= 80)
k = np.polyfit(X[ends], yt[ends], 1); yr = yt - np.polyval(k, X)
pr, _, _ = fit(line, X, yr, SIG, 16.0)
print(f"\nregional check: a true depth 16.25 with the ends' straight line removed fits as d = {abs(pr[3]):.2f} m "
      f"with the free constant c = {pr[0]:.4f}")

print("\nMedford Cave, 80 N-S line (counter-case)")
xf = np.arange(40, 261, 10.0)
gm = np.array([13, 14, 8, 11.5, 10, -3, -37, -2, 30, 22, 18, 17, -3, -7, -6, 5, 15, 14, -7, 4, 13, -8, -27.0])
sel = (xf >= 60) & (xf <= 140)
pm, em, chm = fit(line, xf[sel], gm[sel], 5.0, 8.0)
print(f"  line fit on 60-140 ft: d = {abs(pm[3]):.1f} +- {em[3]:.1f} ft, x0 = {pm[2]:.1f} ft, against 24 ft to centre; "
      f"chi2 = {chm:.1f} on {sel.sum()-4}")
