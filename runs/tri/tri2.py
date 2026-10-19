"""TRI run 2: the payload reader beside the address reader (plans/tri-plan.md, run 2 predictions).
Exact (mpmath) where a closed form exists, seeded samples elsewhere."""
import numpy as np, mpmath as mp
from scipy.stats import kstest, cauchy
mp.mp.dps = 50
rng = np.random.default_rng(20261019 + 2)
b = 1.0
ok = {}
Q = 0.6744897501960817  # the normal's upper quartile

def cauchy_ang(g, n):  # tan(delta) ~ Cauchy(0, g)
    return np.arctan(g * rng.standard_cauchy(n))

def bipolar(sig, tau):  # the pair's coordinates, foci at (-b, 0) and (b, 0)
    den = np.cosh(tau) - np.cos(sig)
    return b * np.sinh(tau) / den, b * np.sin(sig) / den

def cross(aA, aB):  # the crossing of the two read rays (interior angles); NaN where not in front
    fwd = (aA > 0) & (aA < np.pi) & (aB > 0) & (aB < np.pi) & (aA + aB < np.pi)
    ca, cb = 1 / np.tan(aA), 1 / np.tan(aB)
    y = 2 * b / (ca + cb)
    x = -b + y * ca
    return np.where(fwd, x, np.nan), np.where(fwd, y, np.nan)

hq = lambda v: (np.nanpercentile(v, 75) - np.nanpercentile(v, 25)) / 2

def boot_se(fn, *arrs, n=100):  # paired bootstrap
    N = len(arrs[0]); out = []
    for i in range(n):
        ix = rng.integers(0, N, N)
        out.append(fn(*[a[ix] for a in arrs]))
    return np.std(out)

# ---------------- U1: the coordinates, exact
M = 10**4
xs = rng.uniform(-3, 3, M); ys = rng.uniform(0.05, 5, M)
aA = np.arctan2(ys, xs + b); aB = np.arctan2(ys, b - xs)
rA = np.hypot(xs + b, ys); rB = np.hypot(b - xs, ys)
sig = np.pi - aA - aB; tau = np.log(rA / rB)
X, Y = bipolar(sig, tau)
e_back = np.max(np.hypot(X - xs, Y - ys) / np.hypot(xs, ys).clip(1e-3))
e_sine = np.max(np.abs(np.log(np.sin(aB) / np.sin(aA)) - tau))
def xy_mp(s_, t_):
    den = mp.cosh(t_) - mp.cos(s_)
    return b * mp.sinh(t_) / den, b * mp.sin(s_) / den
e_jac = 0
for i in range(M):
    s0, t0 = mp.mpf(sig[i]), mp.mpf(tau[i])
    xs_ = mp.diff(lambda s_: xy_mp(s_, t0)[0], s0); xt_ = mp.diff(lambda t_: xy_mp(s0, t_)[0], t0)
    ys_ = mp.diff(lambda s_: xy_mp(s_, t0)[1], s0); yt_ = mp.diff(lambda t_: xy_mp(s0, t_)[1], t0)
    h = b / (mp.cosh(t0) - mp.cos(s0))
    # h times a rotation (or a reflection of one): columns orthogonal, each of length h
    e = max(abs(xs_**2 + ys_**2 - h**2), abs(xt_**2 + yt_**2 - h**2), abs(xs_ * xt_ + ys_ * yt_)) / h**2
    e_jac = max(e_jac, float(e))
    if i == 0: sgn = float(xs_ * yt_ - xt_ * ys_)
ok['U1'] = e_back < 1e-12 and e_sine < 1e-12 and e_jac < 1e-9
print('U1 back to the target %.1e, sine law %.1e, Jacobian h*rotation %.1e (det sign %+d)'
      % (e_back, e_sine, e_jac, np.sign(sgn)), ok['U1'])

# ---------------- U2: on the bisector, depth is sigma's alone
N = 10**6; g = 1e-4; worst = 0
for k in (1/8, 1, 8):
    a = np.arctan(k)
    A_ = a + cauchy_ang(g, N); B_ = a + cauchy_ang(g, N)
    s_hat = np.pi - A_ - B_
    y_comb = np.where(s_hat > 0, 1 / np.tan(s_hat / 2), np.nan) / k - 1  # sigma read, tau given exactly (0)
    y_bear = cross(A_, B_)[1] / k - 1
    d = hq(y_comb) - hq(y_bear)
    se = boot_se(lambda u, v: hq(u) - hq(v), y_comb, y_bear)
    z = d / se if se > 0 else 0.0
    worst = max(worst, abs(z) if se > 0 else (0 if d == 0 else np.inf))
    print('   k=%-5g half-IQR with tau exact %.6e, bearings alone %.6e, difference %.1e (se %.1e)'
          % (k, hq(y_comb), hq(y_bear), d, se))
ok['U2'] = worst < 3
print('U2', ok['U2'])

# ---------------- U3: the ratio fixes the lateral coordinate
g = 1e-4; s = 1e-4; kstar = 2 * g / (Q * s); worst = 0; better = {}
print('   k* = %.4f' % kstar)
for k in (1/8, 1/2, 1, 2, 8):
    a = np.arctan(k)
    A_ = a + cauchy_ang(g, N); B_ = a + cauchy_ang(g, N)
    xb = cross(A_, B_)[0]
    s_hat = np.pi - A_ - B_
    xr = bipolar(s_hat, rng.normal(0, s, N))[0]
    pb = 2 * g * np.cosh(np.log(k)); pr = Q * s * k * np.cosh(np.log(k))
    zb = (hq(xb) - pb) / boot_se(hq, xb); zr = (hq(xr) - pr) / boot_se(hq, xr)
    worst = max(worst, abs(zb), abs(zr))
    better[k] = 'ratio' if hq(xr) < hq(xb) else 'bearings'
    print('   k=%-5g lateral half-IQR: bearings %.4e (pred %.4e, z %+.2f), ratio %.4e (pred %.4e, z %+.2f); better: %s'
          % (k, hq(xb), pb, zb, hq(xr), pr, zr, better[k]))
switch = all(better[k] == 'ratio' for k in (1/8, 1/2, 1, 2)) and better[8] == 'bearings'
ok['U3'] = worst < 3 and switch
print('U3', ok['U3'])

# ---------------- U4: one bearing and the ratio
g = 1e-4; worst = 0
for k in (1/8, 1, 8):
    a = np.arctan(k); A_ = a + cauchy_ang(g, N)
    rel = np.where((A_ > 0) & (A_ < np.pi / 2), np.tan(A_), np.nan) / k - 1  # A's ray meets the bisector (tau = 0)
    ks = kstest(rel[~np.isnan(rel)], cauchy(0, 2 * g * np.cosh(np.log(k))).cdf).statistic
    worst = max(worst, ks)
    print('   k=%-5g one bearing + exact ratio: KS %.5f' % (k, ks))
ok['U4a'] = worst < 1.36 / np.sqrt(N)
print('U4a (limit %.5f)' % (1.36 / np.sqrt(N)), ok['U4a'])

def F(x, g):
    if x <= -mp.pi / 2: return mp.mpf(0)
    if x >= mp.pi / 2: return mp.mpf(1)
    return mp.mpf(1) / 2 + mp.atan(mp.tan(x) / g) / mp.pi
def f(x, g): return (g / mp.pi) / (g**2 * mp.cos(x)**2 + mp.sin(x)**2)
def p_fwd(al, g):  # run 1's exact probability of a forward crossing
    lo = -al; hi = min(mp.pi / 2, mp.pi - al)
    def inner(dA):
        top = min(mp.pi - 2 * al - dA, mp.pi / 2)
        return max(mp.mpf(0), F(top, g) - F(-al, g))
    pts = [lo, mp.pi / 2 - 2 * al if lo < mp.pi / 2 - 2 * al < hi else None, -0.0, hi]
    pts = sorted(set([p for p in pts if p is not None]))
    return mp.quad(lambda x: f(x, g) * inner(x), pts)
mp.mp.dps = 40
worst_b, worst_c = 0, 0
for k in (1, 8):
    g = 1e-2; a = np.arctan(k)
    gm = mp.mpf('1e-2'); al = mp.atan(k)
    Pnc = 1 - p_fwd(al, gm)
    p = mp.atan(k * gm) / mp.pi              # the prediction's: a bearing at or past pi/2
    q = p + mp.atan(gm / k) / mp.pi          # also at or below 0, which meets the bisector behind
    share_pred = 1 - p**2 / Pnc; share_full = 1 - q**2 / Pnc
    A_ = a + cauchy_ang(g, N); B_ = a + cauchy_ang(g, N)
    xc, yc = cross(A_, B_); nc = np.isnan(yc)
    vA = (A_ > 0) & (A_ < np.pi / 2); vB = (B_ > 0) & (B_ < np.pi / 2)
    resc = nc & (vA | vB)
    share = resc.sum() / nc.sum()
    se = np.sqrt(float(share_pred) * (1 - float(share_pred)) / nc.sum())
    z1 = (share - float(share_pred)) / se; z2 = (share - float(share_full)) / se
    worst_b = max(worst_b, abs(z1))
    yr = np.where(vA, np.tan(A_), np.tan(B_))[resc]  # in the no-crossing set at most one bearing is in (0, pi/2)
    m_res = np.median(np.abs(yr / k - 1)); m_fwd = np.median(np.abs(yc[~nc] / k - 1))
    worst_c = max(worst_c, abs(m_res / m_fwd - 1))
    print('   k=%d g=1e-2: P(no crossing) %s; rescued %.5f of %d, predicted %s (z %+.2f), with bearings <= 0 counted %s (z %+.2f)'
          % (k, mp.nstr(Pnc, 6), share, nc.sum(), mp.nstr(share_pred, 6), z1, mp.nstr(share_full, 6), z2))
    print('       median |rel err| rescued %.5f, forward crossings %.5f, ratio %.4f' % (m_res, m_fwd, m_res / m_fwd))
ok['U4b'] = worst_b < 3; ok['U4c'] = worst_c < 0.10
print('U4b', ok['U4b'], 'U4c', ok['U4c'])

# ---------------- U5: detection without location
worst = 0
for i in range(10**4):
    x, y = rng.uniform(-3, 3), rng.uniform(0.05, 5)
    rA2, rB2 = (x + b)**2 + y**2, (b - x)**2 + y**2
    G = np.array([[-y / rA2, (x + b) / rA2],
                  [y / rB2, (b - x) / rB2],
                  [(x + b) / rA2 + (b - x) / rB2, y / rA2 - y / rB2]])
    sb, s_ = 10**rng.uniform(-5, -2), 10**rng.uniform(-5, -2)
    Wi = np.diag([sb**2, sb**2, s_**2]); W = np.linalg.inv(Wi)
    l = rng.normal(size=3) * np.array([sb, sb, s_])
    N_ = G.T @ W @ G
    Pm = G @ np.linalg.solve(N_, G.T @ W)
    e = l - Pm @ l
    Qe = Wi - G @ np.linalg.solve(N_, G.T)
    w = np.abs(e / np.sqrt(np.diag(Qe)))
    worst = max(worst, (w.max() - w.min()) / w.max())
ok['U5a'] = worst < 1e-12
print('U5a the three w-tests equal in magnitude to %.1e' % worst, ok['U5a'])
g = 1e-4; s = 1e-3; worst = 0
for k in (1/2, 2, 8):
    a = np.arctan(k)
    dA = cauchy_ang(g, N); dB = cauchy_ang(g, N); tr = rng.normal(0, s, N)
    clo = lambda D: np.log(np.sin(a + dB) / np.sin(a + dA + D)) - tr
    thr = np.percentile(np.abs(clo(0.0)), 99.9)
    lo, hi = 0.0, 0.5
    for it in range(60):
        m = (lo + hi) / 2
        (hi, lo) = (m, lo) if np.mean(np.abs(clo(m)) > thr) >= 0.5 else (hi, m)
    D50 = hi; pred = k * thr
    worst = max(worst, abs(D50 / pred - 1))
    print('   k=%-4g threshold |c| %.4e; misread caught half the time %.4e rad, k*thr %.4e, ratio %.4f'
          % (k, thr, D50, pred, D50 / pred))
ok['U5b'] = worst < 0.05
print('U5b', ok['U5b'])

# ---------------- U6: the breadth, and a ratio without a bridge
def edges(al, beta, g, n):
    e1 = al + beta + cauchy_ang(g, n); e2 = al - beta + cauchy_ang(g, n)
    return (e1 + e2) / 2, (e1 - e2) / 2
g = 1e-5; R = 0.05; worst = 0
for k in (1/8, 1, 8):
    a = np.arctan(k); r = np.hypot(1, k); beta = np.arcsin(R / r)
    A_, bA = edges(a, beta, g, N); B_, bB = edges(a, beta, g, N)
    xc, yc = cross(A_, B_)
    Rh = np.hypot(xc + b, yc) * np.sin(bA)
    rel = Rh / R - 1
    cot = 1 / np.tan(beta); lk = np.log(k)
    assert cot >= abs(np.sinh(lk))
    ks = kstest(rel[~np.isnan(rel)], cauchy(0, g * (cot + np.cosh(lk))).cdf).statistic
    worst = max(worst, ks)
    print('   k=%-5g cot beta %.2f: R in b, KS against Cauchy(0, g(cot beta + cosh ln k)) %.5f, median R %.8f b'
          % (k, cot, ks, np.nanmedian(Rh)))
ok['U6a'] = worst < 1.36 / np.sqrt(N)
print('U6a (limit %.5f)' % (1.36 / np.sqrt(N)), ok['U6a'])
k = 0.5; a = np.arctan(k); r = np.hypot(1, k); worst = 0
for R in (0.4, 0.6):
    beta = np.arcsin(R / r)
    A_, bA = edges(a, beta, g, N); B_, bB = edges(a, beta, g, N)
    t_size = np.log(np.sin(bB) / np.sin(bA)); t_bear = np.log(np.sin(B_) / np.sin(A_))
    rat = hq(t_size) / hq(t_bear); pred = k / np.tan(beta)
    se = boot_se(lambda u, v: hq(u) / hq(v), t_size, t_bear)
    z = (rat - pred) / se; worst = max(worst, abs(z))
    print('   R=%.1f b (d = %.1f b): half-IQR of tau, size/bearings %.4f, predicted k cot beta %.4f (se %.4f, z %+.2f)'
          % (R, k, rat, pred, se, z))
ok['U6b'] = worst < 3
print('U6b', ok['U6b'])

ok['U7'] = ok['U1'] and ok['U2'] and ok['U4a'] and ok['U4b'] and ok['U4c']
print('U7', ok['U7'], ok)
