"""DYH run 3: geometry, payload or kernel (plans/dyh-plan.md). Exact (mpmath) but for C3, C4 (double precision)."""
import mpmath as mp
import numpy as np
mp.mp.dps = 60
pi = mp.pi
ok = {}

# ---- A: the address window, open and closed
def W_closed(g):
    return 2 / pi * mp.atan(mp.tanh(pi * g))
def W_series(g):  # the wrapped density 1 + 2 sum rho^k cos(2 pi k x); middle half by its own series
    rho = mp.e ** (-2 * pi * g)
    K = int(mp.ceil(70 / (2 * pi * g))) + 10
    def mass(w):
        return w + 2 * mp.fsum(rho ** k * mp.sin(pi * k * w) / (pi * k) for k in range(1, K))
    return mp.findroot(lambda w: mass(w) - mp.mpf(1) / 2, 2 * g if g < 0.2 else mp.mpf(0.4))
worst = 0
for g in ('0.01', '0.1', '0.25', '1'):
    g = mp.mpf(g); worst = max(worst, abs(W_closed(g) - W_series(g)))
ok['A1'] = worst < mp.mpf(10) ** -25
print('A1 closed line: middle half (2/pi) atan(tanh(pi g)) against the wrapped series, worst %s; W at 0.01, 0.1, 0.25, 1: %s'
      % (mp.nstr(worst, 3), [mp.nstr(W_closed(mp.mpf(g)), 8) for g in ('0.01', '0.1', '0.25', '1')]), ok['A1'])
g = mp.mpf(10) ** -6
a2 = (1 - W_closed(g) / (2 * g)) / g ** 2 / (2 * pi ** 2 / 3)
far = abs(W_closed(mp.mpf(10)) - mp.mpf(1) / 2)
ok['A2'] = abs(a2 - 1) < mp.mpf(10) ** -6 and far < mp.mpf(10) ** -10
print('A2 near the open line: deficit/g^2 over 2pi^2/3 = %s; at g = 10, |W - 1/2| = %s' % (mp.nstr(a2, 12), mp.nstr(far, 3)), ok['A2'])

# ---- B: variation
def G(t, s):
    return (t * mp.atan(t / s) - s / 2 * mp.log(t * t + s * s)) / pi
def box(a, b, c, d, s):
    return G(b - c, s) - G(a - c, s) - G(b - d, s) + G(a - d, s)
def R_H(u):
    s = 2 * mp.mpf(u); h = mp.mpf(1) / 2
    I = [(0, h, 1), (h, 1, -1)]
    return sum(si * sj * box(p, q, r, t, s) for (p, q, si) in I for (r, t, sj) in I)

def J(t, a, b):  # int_0^inf cos(t eta) e^{-b eta - a eta^2} d eta
    z = (b - 1j * t) / (2 * mp.sqrt(a))
    return mp.re(mp.sqrt(pi / a) / 2 * mp.exp(z * z) * mp.erfc(z))
def I(c, a, b):  # int_0^inf (1 - cos c eta) eta^-2 e^{-b eta - a eta^2} d eta = int_0^c (c - t) J(t) dt
    return mp.quad(lambda t: (c - t) * J(t, a, b), mp.linspace(0, c, 9))
def Phi(a, b):
    return (4 * I(pi, a, b) - I(2 * pi, a, b)) / pi ** 2
def R_s(u, s):
    a = 4 * pi ** 2 * mp.mpf(s) ** 2
    return Phi(a, 4 * pi * mp.mpf(u)) / Phi(a, 0)
s = mp.mpf(10) ** -6
check = abs(Phi(4 * pi ** 2 * mp.mpf(10) ** -40, 4 * pi * mp.mpf('0.1')) - R_H(mp.mpf('0.1')))
print('   (the frequency route with s = 1e-20 against the closed form at u = 0.1: %s)' % mp.nstr(check, 3))
d1 = max(abs(R_s(u, s) - R_H(u)) for u in (mp.mpf('1e-3'), mp.mpf('1e-2'), mp.mpf('0.1')))
u = mp.mpf(10) ** -12
a = 4 * pi ** 2 * s ** 2
E = -mp.diff(lambda b: Phi(a, b), 0) / Phi(a, 0)   # E_s|eta| = -d/db ln Phi at b = 0 (Phi counts both sides)
near = (1 - R_s(u, s)) / u / (4 * pi * E)
ok['B1'] = d1 < mp.mpf(10) ** -3 and abs(near - 1) < 0.01
print('B1 softened step, s = 1e-6: |R_s - R_H| at u = 1e-3..0.1 at most %s; at u = 1e-12, (1 - R_s)/u over 4 pi E|eta| = %s (E|eta| = %s)'
      % (mp.nstr(d1, 3), mp.nstr(near, 8), mp.nstr(E, 6)), ok['B1'])
for uu in ('1e-9', '1e-7', '1e-6', '1e-5', '1e-4'):
    uu = mp.mpf(uu); print('   u = %s: (1 - R_s)/u = %s, step law (12/pi) ln(1/u) = %s' % (mp.nstr(uu, 2), mp.nstr((1 - R_s(uu, s)) / uu, 6), mp.nstr(12 / pi * mp.log(1 / uu), 6)))

def cross(g):
    s = 2 * mp.mpf(g); A = mp.mpf(2) ** 1.5
    P = [(0, mp.mpf(1) / 2, 1), (mp.mpf(1) / 2, 1, -1)]
    Q = [(0, mp.mpf(1) / 16, A), (mp.mpf(1) / 16, mp.mpf(1) / 8, -A)]
    return sum(si * sj * box(p, q, r, t, s) for (p, q, si) in P for (r, t, sj) in Q)
c0 = sum(si * sj * max(0, min(q, t) - max(p, r)) for (p, q, si) in [(0, .5, 1), (.5, 1, -1)] for (r, t, sj) in [(0, 1 / 16, 2 ** 1.5), (1 / 16, 1 / 8, -2 ** 1.5)])
c6, c1 = cross(mp.mpf(10) ** -6), cross(mp.mpf('0.1'))
ok['B2'] = abs(c0) < 1e-12 and abs(c6) < 1e-4 and abs(c1) > 1e-3
print('B2 cross term level 0 with level 3: at 0 %s, at 1e-6 %s, at 0.1 %s' % (c0, mp.nstr(c6, 4), mp.nstr(c1, 6)), ok['B2'])

# ---- C: telling apart
cau = 2 / mp.sqrt(3)  # 2a with h''(a) = 0 for h = 1/(1 + x^2): 3a^2 = 1
gau = mp.mpf(2)       # h = e^{-x^2/2}: a = 1
f_c = lambda a: mp.diff(lambda x: 1 / (1 + x * x), a, 2)
f_g = lambda a: mp.diff(lambda x: mp.e ** (-x * x / 2), a, 2)
f_s = lambda a: mp.diff(lambda x: mp.sech(x) ** 2, a, 2)
tc, tg, ts = 2 * mp.findroot(f_c, 0.5), 2 * mp.findroot(f_g, 0.9), 2 * mp.findroot(f_s, 0.6)
lap = all((1 + mp.e ** (-2 * a)) > 2 * mp.e ** (-a) for a in (mp.mpf('1e-6'), mp.mpf('1e-3'), mp.mpf(1)))
ok['C1'] = abs(tc - cau) < mp.mpf(10) ** -40 and abs(tg - gau) < mp.mpf(10) ** -40 and 0 < ts < 10 and lap
print('C1 equal thresholds: Cauchy %s (2/sqrt3 to %s), Gaussian %s, sech^2 %s (2 atanh(1/sqrt3) = %s), Laplace 0 (peaks at every separation: %s)'
      % (mp.nstr(tc, 10), mp.nstr(abs(tc - cau), 3), mp.nstr(tg, 10), mp.nstr(ts, 10), mp.nstr(2 * mp.atanh(1 / mp.sqrt(3)), 10), lap), ok['C1'])
hw_c, hw_g = tc / 1, tg / mp.sqrt(2 * mp.log(2))
ok['C2'] = abs(hw_g / hw_c - 1) > 0.1
print('C2 in half-widths at half maximum: Cauchy %s, Gaussian %s' % (mp.nstr(hw_c, 6), mp.nstr(hw_g, 6)), ok['C2'])

def nmax(prof, d, A=1.0, r=1.0):
    x = np.linspace(-d / 2 - 6 * max(1, r), d / 2 + 6 * max(1, r), 400001)
    y = prof(x + d / 2, 1.0) + A * prof(x - d / 2, r)
    dy = np.diff(y)
    return int(np.sum((dy[:-1] > 0) & (dy[1:] <= 0)))
cauchy = lambda x, w: 1 / (1 + (x / w) ** 2)
gauss = lambda x, w: np.exp(-(x / w) ** 2 / 2)
def thresh(prof, A=1.0, r=1.0):
    lo, hi = 0.0, 1.0
    while nmax(prof, hi, A, r) < 2:
        hi *= 2
        if hi > 1e4: return float('inf')
    while hi - lo > 1e-6:
        mid = (lo + hi) / 2
        (hi, lo) = (mid, lo) if nmax(prof, mid, A, r) >= 2 else (hi, mid)
    return hi
rows = {}
for name, prof in (('Cauchy', cauchy), ('Gaussian', gauss)):
    rows[name] = [thresh(prof, A) for A in (1, 2, 4, 10)]
inc = all(np.isfinite(v).all() and all(v[i] < v[i + 1] for i in range(3)) for v in rows.values())
ok['C3'] = inc
print('C3 unequal amplitudes A = 1, 2, 4, 10:', {k: [round(t, 5) for t in v] for k, v in rows.items()}, ok['C3'])
w4 = [thresh(cauchy, 1.0, r) for r in (2.0, 4.0)]
ok['C4'] = all(np.isfinite(w4))
print('C4 Cauchy heights 1 and r = 2, 4:', [round(t, 5) for t in w4], ok['C4'])
ok['D'] = all(ok.values())
print('D', ok['D'], ok)
