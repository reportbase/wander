"""TRI run 1: triangulation read from a height (plans/tri-plan.md). Exact (mpmath) and seeded samples."""
import numpy as np, mpmath as mp
from scipy.stats import kstest, cauchy
mp.mp.dps = 40
rng = np.random.default_rng(20261019)
b = 1.0
ok = {}

def depth(aA, aB):  # interior angles to the baseline; NaN where the rays do not cross in front
    fwd = (aA > 0) & (aA < np.pi) & (aB > 0) & (aB < np.pi) & (aA + aB < np.pi)
    d = 2 * b / (1 / np.tan(aA) + 1 / np.tan(aB))
    return np.where(fwd, d, np.nan)

def cauchy_ang(g, n):  # tan(delta) ~ Cauchy(0, g)
    return np.arctan(g * rng.standard_cauchy(n))

# T1
N = 10**6; g = 1e-4; worst_ks, worst_med = 0, 0; rows = []
for k in (1/8, 1/2, 1, 2, 8):
    a = np.arctan(k)
    d = depth(a + cauchy_ang(g, N), a + cauchy_ang(g, N))
    rel = d / k - 1
    s = 2 * g * np.cosh(np.log(k))
    ks = kstest(rel[~np.isnan(rel)], cauchy(0, s).cdf).statistic
    med = np.nanmedian(rel); se = s * np.pi / (2 * np.sqrt(N))
    rows.append((k, ks, med / se, np.nanpercentile(rel, 75) / s))
    worst_ks = max(worst_ks, ks); worst_med = max(worst_med, abs(med / se))
ok['T1'] = worst_ks < 1.36 / np.sqrt(N) and worst_med < 3
print('T1 KS limit %.5f' % (1.36 / np.sqrt(N)))
for r in rows: print('   k=%-6g KS %.5f  median/se %+.2f  upper quartile/(2g cosh) %.4f' % r)
print('T1', ok['T1'])

# T2
a = np.pi / 4; sig = np.arctan(g) / 0.6744897501960817
hq = lambda x: (np.nanpercentile(x, 75) - np.nanpercentile(x, 25)) / 2
rc = depth(a + cauchy_ang(g, N), a + cauchy_ang(g, N)) - 1
rn = depth(a + rng.normal(0, sig, N), a + rng.normal(0, sig, N)) - 1
ratio = hq(rc) / hq(rn)
boots = []
for i in range(200):
    ic = rng.integers(0, N, N); inn = rng.integers(0, N, N)
    boots.append(hq(rc[ic]) / hq(rn[inn]))
se2 = np.std(boots)
ok['T2'] = abs(ratio - np.sqrt(2)) < 3 * se2
print('T2 ratio of half-IQRs Cauchy/normal %.4f (sqrt2 %.4f, se %.4f)' % (ratio, np.sqrt(2), se2), ok['T2'])

# T3 (a): exact P(no forward crossing): forward iff thA, thB in (0, pi) and thA + thB < pi, th = alpha + delta
def F(x, g):  # CDF of delta, delta in (-pi/2, pi/2)
    if x <= -mp.pi / 2: return mp.mpf(0)
    if x >= mp.pi / 2: return mp.mpf(1)
    return mp.mpf(1) / 2 + mp.atan(mp.tan(x) / g) / mp.pi
def f(x, g): return (g / mp.pi) / (g**2 * mp.cos(x)**2 + mp.sin(x)**2)
def p_fwd(al, g):
    # integrate over dA in (-al, pi/2): need dB in (-al, pi - 2 al - dA), also dB < pi/2
    lo = -al; hi = min(mp.pi / 2, mp.pi - al)
    def inner(dA):
        top = min(mp.pi - 2 * al - dA, mp.pi / 2)
        return max(mp.mpf(0), F(top, g) - F(-al, g))
    pts = [lo, mp.pi / 2 - 2 * al if lo < mp.pi / 2 - 2 * al < hi else None, -0.0, hi]
    pts = sorted(set([p for p in pts if p is not None]))
    return mp.quad(lambda x: f(x, g) * inner(x), pts)
worst = 0
for k in (1, 8):
    al = mp.atan(k)
    for g3 in (mp.mpf('1e-3'), mp.mpf('1e-2')):
        pex = 1 - p_fwd(al, g3)
        n = 10**6; aa = float(al)
        dd = depth(aa + cauchy_ang(float(g3), n), aa + cauchy_ang(float(g3), n))
        ps = np.mean(np.isnan(dd)); se = np.sqrt(float(pex) * (1 - float(pex)) / n)
        z = (ps - float(pex)) / se; worst = max(worst, abs(z))
        print('   k=%d g=%s: exact P(no forward crossing) %s, sample %.6f (z %+.2f)' % (k, mp.nstr(g3, 2), mp.nstr(pex, 8), ps, z))
ok['T3a'] = worst < 3
print('T3a', ok['T3a'])
# (b)
al = np.arctan(8); means, meds = [], []
for i in range(20):
    dd = depth(al + cauchy_ang(1e-2, 10**5), al + cauchy_ang(1e-2, 10**5))
    dd = np.where(np.isnan(dd), np.inf, dd)  # no crossing: the reading runs to the horizon
    fin = dd[np.isfinite(dd)]
    means.append(fin.mean()); meds.append(np.median(dd))
iqr = lambda x: np.percentile(x, 75) - np.percentile(x, 25)
rb = iqr(means) / iqr(meds)
ok['T3b'] = rb > 10
print('T3b batch means IQR / batch medians IQR = %.1f (means of the finite crossings; %d batches)' % (rb, 20), ok['T3b'])
# (c) normal: P(thA + thB >= pi) dominates; exact via the normal sum (angles' other limits negligible)
al = mp.atan(8); g3 = mp.mpf('1e-2'); sig = mp.atan(g3) / mp.mpf('0.6744897501960817')
pn = mp.erfc((mp.pi - 2 * al) / (mp.sqrt(2) * mp.sqrt(2) * sig)) / 2
pc = 1 - p_fwd(al, g3)
ok['T3c'] = pc / pn > 10**6
print('T3c no forward crossing at k=8, g=1e-2: Cauchy %s, normal %s, ratio %s' % (mp.nstr(pc, 6), mp.nstr(pn, 6), mp.nstr(pc / pn, 4)), ok['T3c'])

# T4: two targets on the bisector; A's screen at unit distance square to the line to the first target
worst = 0
for k in (mp.mpf(1) / 4, mp.mpf(1), mp.mpf(4)):
    g4 = mp.mpf('1e-3'); al = mp.atan(k)
    u_star = 2 * g4 / mp.sqrt(3)  # two maxima iff screen separation > u_star (equal Cauchy profiles)
    # exact: also by bisection on the count of maxima of the two profiles on the screen
    def two(Delta):
        u = mp.tan(mp.atan((k + Delta) / b) - al)
        prof = lambda x: 1 / (g4**2 + x**2) + 1 / (g4**2 + (x - u)**2)
        return mp.diff(prof, u / 2, 2) > 0
    lo, hi = mp.mpf(0), k
    for i in range(80):
        m = (lo + hi) / 2
        (hi, lo) = (m, lo) if two(m) else (hi, m)
    exact = hi / k
    closed = (b * mp.tan(al + mp.atan(u_star)) - k) / k
    first = 4 / mp.sqrt(3) * g4 * mp.cosh(mp.log(k))
    worst = max(worst, abs(exact / first - 1))
    print('   k=%s: Delta*/d exact %s (closed form %s), first order %s, ratio %s' % (mp.nstr(k, 3), mp.nstr(exact, 8), mp.nstr(closed, 8), mp.nstr(first, 8), mp.nstr(exact / first, 6)))
ok['T4'] = worst < 0.01
print('T4', ok['T4'])
ok['T5'] = ok['T1'] and ok['T2'] and ok['T4']
print('T5', ok['T5'], ok)
