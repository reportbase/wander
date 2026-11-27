"""SEP run 2: exact Cramer-Rao bounds (SPN R1272; plans/sep-plan.md). Run from the root: python3 runs/sep/sep2.py"""
import numpy as np, mpmath as mp
mp.mp.dps = 30
out = []
def say(s): print(s, flush=True); out.append(s)
def pair(d, r):
    g1, g2 = 1 / mp.sqrt(r), mp.sqrt(r)
    dm = mp.sqrt(max(2 * (mp.cosh(d) - 1) - (g1 - g2) ** 2, 0))
    return (-dm / 2, g1), (dm / 2, g2)
cases = [(d, r) for d in (1.5, 2.0, 3.0) for r in (1, 2, 4)] + [(3.0, 16)]
def C(x, m, g): return g / (mp.pi * ((x - m) ** 2 + g ** 2))
def dC(x, m, g):  # derivatives w.r.t. m and log g
    D = (x - m) ** 2 + g ** 2
    return (2 * g * (x - m) / (mp.pi * D ** 2), g / (mp.pi * D) - 2 * g ** 3 / (mp.pi * D ** 2))
def draw_bound(d, r):
    (m1, g1), (m2, g2) = pair(mp.mpf(d), mp.mpf(r)); w = mp.mpf('0.5')
    def score(x):
        p1, p2 = C(x, m1, g1), C(x, m2, g2); p = w * p1 + (1 - w) * p2
        a, b = dC(x, m1, g1); c, e = dC(x, m2, g2)
        return [w * a / p, w * b / p, (1 - w) * c / p, (1 - w) * e / p, (p1 - p2) / p], p
    F = mp.matrix(5, 5)
    for i in range(5):
        for j in range(i, 5):
            f = lambda t: (lambda s, p: s[i] * s[j] * p)(*score(mp.tan(t))) / mp.cos(t) ** 2
            F[i, j] = F[j, i] = mp.quad(f, mp.linspace(-mp.pi / 2, mp.pi / 2, 9))
    return mp.sqrt((F ** -1)[4, 4])          # bound on w, per one draw
X = np.arange(-200, 200.0001, 0.05); SIG = 2e-3
def Cn(x, m, g): return g / (np.pi * ((x - m) ** 2 + g ** 2))
def spec_bound(d, r):
    (m1, g1), (m2, g2) = [(float(a), float(b)) for a, b in pair(mp.mpf(d), mp.mpf(r))]; h = 1e-6
    th = np.array([m1, np.log(g1), 0.5, m2, np.log(g2), 0.5])
    def f(t): return t[2] * Cn(X, t[0], np.exp(t[1])) + t[5] * Cn(X, t[3], np.exp(t[4]))
    J = np.stack([(f(th + h * e) - f(th - h * e)) / (2 * h) for e in np.eye(6)], 1)
    cov = SIG ** 2 * np.linalg.inv(J.T @ J)
    a1, a2 = 0.5, 0.5; gw = np.zeros(6); gw[2] = a2 / (a1 + a2) ** 2; gw[5] = -a1 / (a1 + a2) ** 2
    gt = np.zeros(6); gt[2] = gt[5] = 1
    return np.sqrt(gw @ cov @ gw), np.sqrt(gt @ cov @ gt)
Jg = np.stack([(lambda t: t[2] * Cn(X, t[0], np.exp(t[1])))(np.array([0, 0, 1.0]) + 1e-6 * e) -
               (lambda t: t[2] * Cn(X, t[0], np.exp(t[1])))(np.array([0, 0, 1.0]) - 1e-6 * e) for e in np.eye(3)], 1) / 2e-6
single = np.sqrt((SIG ** 2 * np.linalg.inv(Jg.T @ Jg))[2, 2])
db, sb = {}, {}
for d, r in cases:
    db[(d, r)] = draw_bound(d, r); sb[(d, r)] = spec_bound(d, r)
    say(f"d = {d}, r = {r:>2}: draws, weight bound per draw {mp.nstr(db[(d, r)], 12)}; spectrum, weight {sb[(d, r)][0]:.5e}, total {sb[(d, r)][1]:.3e}")
S3 = True; S4 = True
for d in (1.5, 2.0, 3.0):
    v = [db[(dd, r)] for dd, r in cases if dd == d]; rel = (max(v) - min(v)) / min(v)
    u = [sb[(dd, r)][0] for dd, r in cases if dd == d]; sp = max(u) / min(u)
    say(f"d = {d}: draws relative spread across r {mp.nstr(rel, 3)}; spectrum spread {sp:.4f}")
    S3 &= rel < 1e-8
    if d == 1.5: S4 = sp > 1.05
S3 &= db[(1.5, 1)] > db[(2.0, 1)] > db[(3.0, 1)]
worst = max(t for _, t in sb.values()) / single
say(f"one Cauchy alone, total bound {single:.3e}; worst pair over it {worst:.3f}")
S5 = worst < 3
for n, v in [("S3'", S3), ("S4'", S4), ("S5'", S5)]: say(f"{n}: {'not killed' if v else 'KILLED'}")
open('runs/sep/sep2-out.txt', 'w').write('\n'.join(out) + '\n')
