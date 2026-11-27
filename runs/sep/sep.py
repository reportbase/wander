"""SEP: separating overlapping Cauchys (SPN R1272; plans/sep-plan.md). Run from the root: python3 runs/sep/sep.py"""
import numpy as np, mpmath as mp
from scipy.optimize import minimize, least_squares
out = []
def say(s): print(s, flush=True); out.append(s)

def pair(d, r):
    g1, g2 = 1 / np.sqrt(r), np.sqrt(r)
    dm2 = 2 * (np.cosh(d) - 1) - (g1 - g2) ** 2
    assert dm2 >= -1e-12, (d, r)
    dm = np.sqrt(max(dm2, 0))
    return (-dm / 2, g1), (dm / 2, g2)
def hyp(z1, z2): return np.arccosh(1 + abs(z1 - z2) ** 2 / (2 * z1.imag * z2.imag))

# S1: Prony on the noiseless phasor, 50 digits
mp.mp.dps = 50
rng = np.random.default_rng(1272)
worst = mp.mpf(0)
for K in (1, 2, 3, 4):
    ms = [mp.mpf(x) for x in rng.uniform(-2, 2, K)]; gs = [mp.mpf(x) for x in rng.uniform(0.3, 2, K)]
    As = [mp.mpf(x) for x in rng.uniform(0.2, 1, K)]; dt = mp.mpf('0.3')
    lam = [mp.exp((1j * m - g) * dt) for m, g in zip(ms, gs)]
    c = [sum(a * l ** n for a, l in zip(As, lam)) for n in range(2 * K)]
    H = mp.matrix(K, K); rhs = mp.matrix(K, 1)
    for i in range(K):
        for j in range(K): H[i, j] = c[i + j]
        rhs[i] = -c[i + K]
    p = mp.lu_solve(H, rhs)
    roots = mp.polyroots([1] + [p[K - 1 - j] for j in range(K)], maxsteps=200, extraprec=200)
    V = mp.matrix(K, K); cc = mp.matrix(K, 1)
    for i in range(K):
        for j in range(K): V[i, j] = roots[j] ** i
        cc[i] = c[i]
    a_hat = mp.lu_solve(V, cc)
    rec = sorted([(mp.im(mp.log(l)) / dt, -mp.re(mp.log(l)) / dt, mp.re(a)) for l, a in zip(roots, a_hat)], key=lambda t: t[0])
    tru = sorted(zip(ms, gs, As), key=lambda t: t[0])
    e = max(max(abs(x - y) for x, y in zip(u, v)) for u, v in zip(rec, tru)); worst = max(worst, e)
    say(f"S1 K = {K}: worst error in m, gamma, amount {mp.nstr(e, 3)}")
S1 = worst < 1e-8

# draws
def draws(n, comps, w, rng):
    k = rng.random(n) < w
    (m1, g1), (m2, g2) = comps
    t = np.tan(np.pi * (rng.random(n) - 0.5))
    return np.where(k, m1 + g1 * t, m2 + g2 * t)
def nll(th, x):
    m1, l1, m2, l2, q = th; g1, g2 = np.exp(l1), np.exp(l2); w = 1 / (1 + np.exp(-q))
    p = w * g1 / (np.pi * ((x - m1) ** 2 + g1 ** 2)) + (1 - w) * g2 / (np.pi * ((x - m2) ** 2 + g2 ** 2))
    return -np.sum(np.log(p))
def fit(x, comps, w):
    (m1, g1), (m2, g2) = comps
    th0 = np.array([m1, np.log(g1), m2, np.log(g2), np.log(w / (1 - w))])
    r = minimize(nll, th0, args=(x,), method='BFGS', options={'gtol': 1e-9, 'maxiter': 2000})
    m1, l1, m2, l2, q = r.x
    return complex(m1, np.exp(l1)), complex(m2, np.exp(l2)), 1 / (1 + np.exp(-q))
def mob(z, a=1.0, b=1.0, c=-0.5, d=1.0): return (a * z + b) / (c * z + d)

# S2: equivariance under a non-affine Moebius map
worst_w, worst_z = 0, 0
comps = pair(2.0, 2.0)
for trial in range(20):
    x = draws(2000, comps, 0.5, rng)
    z1, z2, w = fit(x, comps, 0.5)
    gz = [mob(complex(m, g)) for m, g in comps]
    gcomps = [(z.real, z.imag) for z in gz]
    y = mob(x)
    y1, y2, wy = fit(y, gcomps, 0.5)
    worst_w = max(worst_w, abs(w - wy)); worst_z = max(worst_z, abs(mob(z1) - y1), abs(mob(z2) - y2))
say(f"S2 Moebius map (x + 1)/(1 - x/2): worst weight gap {worst_w:.2e}, worst standpoint gap {worst_z:.2e} over 20 trials")
S2 = worst_w < 1e-4 and worst_z < 1e-4

cases = [(d, r) for d in (1.5, 2.0, 3.0) for r in (1, 2, 4)] + [(3.0, 16)]
# S3: draws, median weight error by case
T = 200; med3 = {}
for d, r in cases:
    comps = pair(d, r)
    z = [complex(m, g) for m, g in comps]; assert abs(hyp(*z) - d) < 1e-9
    errs = [abs(fit(draws(2000, comps, 0.5, rng), comps, 0.5)[2] - 0.5) for _ in range(T)]
    med3[(d, r)] = np.median(errs)
    say(f"S3 draws d = {d}, r = {r:>2}: median weight error {med3[(d, r)]:.4f}")
S3 = True
for d in (1.5, 2.0, 3.0):
    v = [med3[(dd, r)] for dd, r in cases if dd == d]
    spread = max(v) / min(v); say(f"S3 d = {d}: spread across r {spread:.3f}"); S3 &= spread < 1.25
S3 &= med3[(1.5, 1)] > med3[(2.0, 1)] > med3[(3.0, 1)]

# S4, S5: a spectrum with additive noise
X = np.arange(-200, 200.0001, 0.05); SIG = 2e-3
def C(x, m, g): return g / (np.pi * ((x - m) ** 2 + g ** 2))
def fit_spec(yv, th0):
    def res(th):
        m1, l1, a1, m2, l2, a2 = th
        return a1 * C(X, m1, np.exp(l1)) + a2 * C(X, m2, np.exp(l2)) - yv
    return least_squares(res, th0, xtol=1e-12, ftol=1e-12).x
med4, tot4 = {}, {}
for d, r in cases:
    (m1, g1), (m2, g2) = pair(d, r)
    clean = 0.5 * C(X, m1, g1) + 0.5 * C(X, m2, g2)
    th0 = np.array([m1, np.log(g1), 0.5, m2, np.log(g2), 0.5])
    we, te = [], []
    for _ in range(T):
        th = fit_spec(clean + SIG * rng.standard_normal(X.size), th0)
        a1, a2 = th[2], th[5]; we.append(abs(a1 / (a1 + a2) - 0.5)); te.append(abs(a1 + a2 - 1))
    med4[(d, r)], tot4[(d, r)] = np.median(we), np.median(te)
    say(f"S4 spectrum d = {d}, r = {r:>2}: median weight error {med4[(d, r)]:.5f}, total-amount error {tot4[(d, r)]:.2e}")
single = []
for _ in range(T):
    yv = C(X, 0, 1) + SIG * rng.standard_normal(X.size)
    th = least_squares(lambda t: t[2] * C(X, t[0], np.exp(t[1])) - yv, [0, 0, 1], xtol=1e-12, ftol=1e-12).x
    single.append(abs(th[2] - 1))
s1 = np.median(single); say(f"S5 one Cauchy alone: total-amount error {s1:.2e}")
S4 = True
for d in (1.5, 2.0):
    v = [med4[(dd, r)] for dd, r in cases if dd == d]
    spread = max(v) / min(v); say(f"S4 d = {d}: spread across r {spread:.3f} (kill if within 1.2, predicted over 1.5)")
    S4 &= spread > 1.5
say(f"S4 d = 3.0: spread across r {max(med4[(3.0, r)] for r in (1, 2, 4, 16)) / min(med4[(3.0, r)] for r in (1, 2, 4, 16)):.3f}")
worst_tot = max(tot4.values()) / s1
grow_w = med4[(1.5, 1)] / med4[(3.0, 1)]; grow_t = tot4[(1.5, 1)] / tot4[(3.0, 1)]
say(f"S5 worst total-amount error over one Cauchy's: {worst_tot:.2f}; d 3 to 1.5 (r = 1): weight error x{grow_w:.2f}, total x{grow_t:.2f}")
S5 = worst_tot < 3 and grow_w > grow_t
for n, v in [('S1', S1), ('S2', S2), ('S3', S3), ('S4', S4), ('S5', S5)]: say(f"{n}: {'not killed' if v else 'KILLED'}")
open('runs/sep/sep-out.txt', 'w').write('\n'.join(out) + '\n')
