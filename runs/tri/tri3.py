"""TRI run 3: run 2 with its set-up faults mended (plans/tri-plan.md, run 3 predictions).
Exact (mpmath) where a closed form exists, seeded samples elsewhere."""
import numpy as np, mpmath as mp
from scipy.stats import kstest, cauchy
mp.mp.dps = 50
rng = np.random.default_rng(20261019 + 3)
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

ok['U1'] = True  # run 2

# ---------------- U2': the bearings' tau error enters the depth at second order
N = 10**6; g = 1e-4; worst = 0
for k in (1/8, 1, 8):
    a = np.arctan(k)
    A_ = a + cauchy_ang(g, N); B_ = a + cauchy_ang(g, N)
    s_hat = np.pi - A_ - B_
    y_comb = np.where(s_hat > 0, 1 / np.tan(s_hat / 2), np.nan)
    y_bear = cross(A_, B_)[1]
    t_b = np.log(np.sin(B_) / np.sin(A_))
    r = (y_bear - y_comb) / (k * (1 + k**2) * t_b**2 / 4)
    m = np.nanmedian(r); worst = max(worst, abs(m + 1))
    print("   k=%-5g median of the depth difference over y0 (1 + k^2) tau^2 / 4: %+.5f" % (k, m))
ok['U2'] = worst < 0.02
print("U2'", ok['U2'])

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
g = 1e-4; worst = 0; worst_raw = 0
for k in (1/8, 1, 8):
    a = np.arctan(k); A_ = a + cauchy_ang(g, N)
    rel = np.where((A_ > 0) & (A_ < np.pi / 2), np.tan(A_), np.nan) / k - 1  # A's ray meets the bisector (tau = 0)
    ks = kstest(rel[~np.isnan(rel)], cauchy(0, 2 * g * np.cosh(np.log(k))).cdf).statistic
    raw = kstest(np.tan(A_ - a), cauchy(0, g).cdf).statistic
    worst = max(worst, ks); worst_raw = max(worst_raw, abs(ks - raw))
    print('   k=%-5g one bearing + exact ratio: KS %.5f, the draw itself %.5f' % (k, ks, raw))
ok['U4a'] = worst < 1.63 / np.sqrt(N) and worst_raw < 2e-4
print("U4a' (limit %.5f; largest gap to the draw %.1e)" % (1.63 / np.sqrt(N), worst_raw), ok['U4a'])

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
    worst_b = max(worst_b, abs(z2))
    yr = np.where(vA, np.tan(A_), np.tan(B_))[resc]  # in the no-crossing set at most one bearing is in (0, pi/2)
    m_res = np.median(np.abs(yr / k - 1)); m_fwd = np.median(np.abs(yc[~nc] / k - 1))
    worst_c = max(worst_c, abs(m_res / m_fwd - 1))
    print('   k=%d g=1e-2: P(no crossing) %s; rescued %.5f of %d, predicted %s (z %+.2f), with bearings <= 0 counted %s (z %+.2f)'
          % (k, mp.nstr(Pnc, 6), share, nc.sum(), mp.nstr(share_pred, 6), z1, mp.nstr(share_full, 6), z2))
    print('       median |rel err| rescued %.5f, forward crossings %.5f, ratio %.4f' % (m_res, m_fwd, m_res / m_fwd))
ok['U4b'] = worst_b < 3; ok['U4c'] = worst_c < 0.10
print("U4b'", ok['U4b'], 'U4c', ok['U4c'])

# ---------------- U5: detection without location (at 50 digits)
mp.mp.dps = 50; worst = mp.mpf(0)
for i in range(10**3):
    x, y = mp.mpf(rng.uniform(-3, 3)), mp.mpf(rng.uniform(0.05, 5))
    rA2, rB2 = (x + b)**2 + y**2, (b - x)**2 + y**2
    G = mp.matrix([[-y / rA2, (x + b) / rA2],
                   [y / rB2, (b - x) / rB2],
                   [(x + b) / rA2 + (b - x) / rB2, y / rA2 - y / rB2]])
    sb, s_ = mp.mpf(10)**rng.uniform(-5, -2), mp.mpf(10)**rng.uniform(-5, -2)
    Wi = mp.diag([sb**2, sb**2, s_**2]); W = Wi**-1
    l = mp.matrix([rng.normal() * float(sb), rng.normal() * float(sb), rng.normal() * float(s_)])
    Ninv = (G.T * W * G)**-1
    e = l - G * Ninv * G.T * W * l
    Qe = Wi - G * Ninv * G.T
    w = [abs(e[j] / mp.sqrt(Qe[j, j])) for j in range(3)]
    worst = max(worst, (max(w) - min(w)) / max(w))
ok['U5a'] = worst < mp.mpf('1e-30')
print("U5a' the three w-tests equal in magnitude to %s" % mp.nstr(worst, 3), ok['U5a'])
g = 1e-4; s = 1e-3; worst = 0
for k in (1/2, 2, 8):
    a = np.arctan(k)
    dA = cauchy_ang(g, N); dB = cauchy_ang(g, N); tr = rng.normal(0, s, N)
    def clo(D):  # a bearing outside (0, pi): no triangle in front, caught (|c| infinite)
        A_, B_ = a + dA + D, a + dB
        bad = (A_ <= 0) | (A_ >= np.pi) | (B_ <= 0) | (B_ >= np.pi)
        with np.errstate(invalid='ignore', divide='ignore'):
            c = np.log(np.abs(np.sin(B_) / np.sin(A_))) - tr
        return np.where(bad, np.inf, c)
    thr = np.percentile(np.abs(clo(0.0)), 99.9)
    assert np.isfinite(thr)
    lo, hi = 0.0, 0.5
    for it in range(60):
        m = (lo + hi) / 2
        (hi, lo) = (m, lo) if np.mean(np.abs(clo(m)) > thr) >= 0.5 else (hi, m)
    D50 = hi; pred = k * thr
    worst = max(worst, abs(D50 / pred - 1))
    print('   k=%-4g threshold |c| %.4e; misread caught half the time %.4e rad, k*thr %.4e, ratio %.4f'
          % (k, thr, D50, pred, D50 / pred))
ok['U5b'] = worst < 0.05
print("U5b'", ok['U5b'])

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

ok['U7'] = ok['U1'] and ok['U2'] and ok['U4a'] and ok['U4b']
print("U7'", ok['U7'], ok)
