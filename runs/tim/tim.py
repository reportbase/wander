# TIM (plans/tim-plan.md): how a Cauchy keeps time. Exact (mpmath) and seeded (numpy). Run: python3 runs/tim/tim.py
import numpy as np, mpmath as mp
from scipy.stats import ks_2samp, spearmanr
rng = np.random.default_rng(20261018 + 7)
ok = {}
cauchy = lambda g, n: g * np.tan(rng.uniform(-np.pi / 2, np.pi / 2, n))
hiqr = lambda x: (np.quantile(x, .75) - np.quantile(x, .25)) / 2
qse = lambda g, N: 2 * np.pi * g * np.sqrt(3 / (16 * N))   # standard error of a Cauchy's sample quartile
ks_lim = lambda N: 1.63 * np.sqrt(2 / N)
# T1: time turns z
mp.mp.dps = 60
m, g = mp.mpf('0.7'), mp.mpf('0.3')
C = lambda x: g / (mp.pi * ((x - m) ** 2 + g * g))
def ft(t):          # ∫ e^{itx} C(x) dx, real and imaginary parts, each side of m, by quadosc
    w = abs(t)
    re = mp.quadosc(lambda x: mp.cos(t * x) * C(x), [m, mp.inf], omega=w) + mp.quadosc(lambda x: mp.cos(t * x) * C(x), [-mp.inf, m], omega=w)
    im = mp.quadosc(lambda x: mp.sin(t * x) * C(x), [m, mp.inf], omega=w) + mp.quadosc(lambda x: mp.sin(t * x) * C(x), [-mp.inf, m], omega=w)
    return mp.mpc(re, im)
t1a = max(abs(ft(mp.mpf(t)) - mp.exp(1j * m * mp.mpf(t) - g * abs(mp.mpf(t)))) for t in ['0.1', '1', '5', '-2'])
def spec(w):        # |∫_0^∞ e^{(im − γ)t} e^{−iωt} dt|², by quadrature over [0, 480] in unit pieces (e^{−0.3·480} < 10⁻⁶²)
    f = lambda t: mp.exp((1j * (m - w) - g) * t)
    return abs(mp.quad(f, mp.linspace(0, 480, 481))) ** 2
t1b = max(abs(spec(mp.mpf(w)) - 1 / ((mp.mpf(w) - m) ** 2 + g * g)) for w in ['-1', '0', '0.7', '2'])
ok['T1'] = t1a < mp.mpf(10) ** -40 and t1b < mp.mpf(10) ** -40
print(f'T1 (a) the transform of C(0.7, 0.3) against e^(izt): {mp.nstr(t1a, 3)}; (b) the phasor\'s power spectrum against the Lorentzian: {mp.nstr(t1b, 3)}')
# T2: time raises the standpoint (unit rate; sample times 1, 4, 16)
N = 10 ** 5
def paths(n):
    x1 = cauchy(1, n); x4 = x1 + cauchy(3, n); x16 = x4 + cauchy(12, n); return x1, x4, x16
X1, X4, X16 = paths(N)
qs = {t: (np.quantile(x, .25), np.quantile(x, .75)) for t, x in [(1, X1), (4, X4), (16, X16)]}
t2a = all(abs(lo + t) <= 3 * qse(t, N) and abs(hi - t) <= 3 * qse(t, N) for t, (lo, hi) in qs.items())
_, Y4, Y16 = paths(N)                     # an independent set, so the KS test's two samples are independent
ks2 = ks_2samp(Y16 / 4, X4).statistic
rho = spearmanr(X4 - X1, X1).statistic
ok['T2'] = t2a and ks2 < ks_lim(N) and abs(rho) < 3 / np.sqrt(N)
for t, (lo, hi) in qs.items(): print(f'T2 (a) t = {t:2d}: quartiles {lo:.4f}, {hi:.4f} (3 se {3 * qse(t, N):.4f})')
print(f'T2 (b) X(16)/4 against X(4), independent paths: KS {ks2:.5f} (limit {ks_lim(N):.5f}); (c) rank correlation of X(4) − X(1) with X(1): {rho:.5f} (limit {3 / np.sqrt(N):.5f})')
# T3: order and ratios free; durations amounts
P = np.stack([X1, X4, X16], 1); T = np.array([1., 4., 16.]); order0 = np.argsort(P, 1)
ratio0 = hiqr(X16) / hiqr(X4); v0 = hiqr(X16) / 16; T0 = 2.5
worst = dict(a=0, b=0., c=0., d=0.)
for c in [1e-3, 7., 1e3]:
    for k in [1e-3, 7., 1e3]:
        Pk = k * P; Tc = c * T          # world by k; clock by c (rate v/c, so the values at clock times ct are k·X)
        worst['a'] += int((np.argsort(Pk, 1) != order0).sum())
        worst['b'] = max(worst['b'], abs(hiqr(Pk[:, 2]) / hiqr(Pk[:, 1]) / ratio0 - 1))
        v = hiqr(Pk[:, 2]) / Tc[2]
        worst['c'] = max(worst['c'], abs(v / (k / c * v0) - 1))
        worst['d'] = max(worst['d'], abs(v * c * T0 / (k * v0 * T0) - 1))
ok['T3'] = worst['a'] == 0 and max(worst['b'], worst['c'], worst['d']) < 1e-12
print(f"T3 (a) orders changed: {worst['a']}; (b) ratio of spreads off by {worst['b']:.1e}; (c) rate off k/c by {worst['c']:.1e}; (d) rate × duration off k by {worst['d']:.1e}")
# T4: the hidden clock (Spitzer's landing from h = 1, exact construction)
h = 1.0; q = float(mp.erfinv(mp.mpf('0.5')) ** 2 * 2)   # median of Z²: (Φ⁻¹(¾))² = 2·erfinv(½)²
levy_f = lambda t, a: np.sqrt(a / (2 * np.pi)) * np.exp(-a / (2 * t)) / t ** 1.5   # density of a/Z²
land, t4 = {}, True
for D in [0.1, 1., 10.]:
    r = np.random.default_rng(int(1000 * D) + 41)
    Z = r.standard_normal(N); Nn = r.standard_normal(N)
    place = h * Nn / np.abs(Z); tau = h * h / (2 * D * Z * Z); land[D] = place
    lo, hi = np.quantile(place, [.25, .75]); a = h * h / (2 * D); med = a / q
    se_t = 0.5 / (np.sqrt(N) * levy_f(med, a))
    okD = abs(lo + h) <= 3 * qse(h, N) and abs(hi - h) <= 3 * qse(h, N) and abs(np.median(tau) - med) <= 3 * se_t
    t4 = t4 and okD
    print(f'T4 D = {D:4}: landing quartiles {lo:.4f}, {hi:.4f} (3 se {3 * qse(h, N):.4f}); median passage {np.median(tau):.4f} against h²/(2Dq) = {med:.4f} (3 se {3 * se_t:.4f})')
ksD = ks_2samp(land[0.1], land[10.]).statistic; t4 = t4 and ksD < ks_lim(N)
print(f'T4 (b) landings at D = 0.1 and 10: KS {ksD:.5f} (limit {ks_lim(N):.5f})')
r = np.random.default_rng(4242); B = 1000; a = h * h / 2
for M in [10, 100, 1000]:
    Z = r.standard_normal((B, M)); bm = (a / (Z * Z)).mean(1)
    med = M * a / q; se_m = 0.5 / (np.sqrt(B) * levy_f(med, M * a))
    t4 = t4 and abs(np.median(bm) - med) <= 3 * se_m
    print(f'T4 (d) M = {M:4d}: median batch mean {np.median(bm):.3f} against M·h²/(2q) = {med:.3f} (3 se {3 * se_m:.3f})')
ok['T4'] = t4
print('verdicts: ' + ', '.join(f'{k} {"not killed" if v else "killed"}' for k, v in ok.items()))
