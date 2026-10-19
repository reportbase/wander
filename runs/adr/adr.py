# ADR (plans/adr-plan.md): the address as a primitive. Exact (mpmath) and seeded (numpy). Run: python3 runs/adr/adr.py
import numpy as np, mpmath as mp
from scipy.optimize import minimize
rng = np.random.default_rng(20261018)
ok = {}
cauchy = lambda z, n: z.real + z.imag * np.tan(rng.uniform(-np.pi / 2, np.pi / 2, n))
se = lambda g, N: np.pi * g / (2 * np.sqrt(N))          # a Cauchy's median, and its half-IQR, standard error
read = lambda x: complex(np.median(x), (np.quantile(x, .75) - np.quantile(x, .25)) / 2)
def mle(x):
    m0, g0 = np.median(x), (np.quantile(x, .75) - np.quantile(x, .25)) / 2
    def nll(p):
        m, lg = p; g = np.exp(lg); d = x - m; q = g * g + d * d
        return (-np.sum(lg - np.log(q)), np.array([-np.sum(2 * d / q), -np.sum(1 - 2 * g * g / q)]))
    r = minimize(nll, [m0, np.log(g0)], jac=True, method='BFGS', options={'gtol': 1e-11, 'maxiter': 10000})
    return complex(r.x[0], np.exp(r.x[1]))
# A1: combination is linear in z
mp.mp.dps = 100
Z = [mp.mpc(1, 0.5), mp.mpc(-2, 1), mp.mpc('0.3', 2)]; W = [mp.mpf('0.5'), mp.mpf(-2), mp.mpf('1.5')]
phi = lambda z, t: mp.exp(1j * z.real * t - z.imag * abs(t))
ex = max(abs(mp.fprod(phi(z, w * t) for z, w in zip(Z, W)) - phi(mp.mpc('4.95', '5.25'), t)) for t in map(mp.mpf, ['0.1', '1', '3']))
N = 10 ** 6
s = sum(float(w) * cauchy(complex(z), N) for z, w in zip(Z, W)); r = read(s)
ok['A1'] = ex < mp.mpf(10) ** -90 and abs(r.real - 4.95) <= 3 * se(5.25, N) and abs(r.imag - 5.25) <= 3 * se(5.25, N)
print(f'A1 exact: characteristic functions differ by at most {mp.nstr(ex, 3)}; sample read {r.real:.4f} + {r.imag:.4f}i against 4.95 + 5.25i (3 se = {3 * se(5.25, N):.4f})')
# A2: Möbius maps
mp.mp.dps = 50
z0 = mp.mpc('0.5', '0.8'); g = lambda x: (2 * x + 1) / (x + 3); gi = lambda y: (1 - 3 * y) / (y - 2)
F = lambda x, z: mp.mpf(1) / 2 + mp.atan((x - z.real) / z.imag) / mp.pi
def FY(y):      # P(g(X) ≤ y) from X's own law: g rises on each side of its pole at −3, from 2 to ∞ left of it, −∞ to 2 right
    y = mp.mpf(y)
    if y < 2: return F(gi(y), z0) - F(-3, z0)
    return (1 - F(-3, z0)) + F(gi(y), z0)
gz = g(z0); a2a = max(abs(FY(y) - F(mp.mpf(y), gz)) for y in np.linspace(-20, 20, 20))
x = cauchy(complex(z0), 10 ** 5); rx = read(x); ra = read(3 * x - 2)
a2b = abs(ra - (3 * rx.real - 2 + 3j * rx.imag))
gc = lambda z: (2 * z + 1) / (z + 3)
y = (2 * x + 1) / (x + 3); ry = read(y); gq = gc(rx); a2c_q = abs(ry - gq) / se(abs(complex(gz).imag), 10 ** 5)
mx, my = mle(x), mle(y); a2c_m = abs(my - gc(mx)) / abs(my)
ok['A2'] = a2a < mp.mpf(10) ** -40 and a2b < 1e-9 and a2c_q > 10 and a2c_m < 1e-6
print(f'A2 (a) the law of g(X) against C(g(z)): {mp.nstr(a2a, 3)}; (b) the quartile read under x → 3x − 2 off by {a2b:.2e}; '
      f'(c) under g, the quartile read {ry.real:.4f} + {ry.imag:.4f}i against g(read) {gq.real:.4f} + {gq.imag:.4f}i, {a2c_q:.1f} se apart; '
      f'the likelihood read {my.real:.6f} + {my.imag:.6f}i against g(mle) {gc(mx).real:.6f} + {gc(mx).imag:.6f}i, relative {a2c_m:.1e} (true g(z) = {complex(gz):.4f})')
# A3: the distance
def fisher(m, gm):
    f = lambda x: gm / (mp.pi * (gm ** 2 + (x - m) ** 2))
    dm = lambda x: 2 * (x - m) / (gm ** 2 + (x - m) ** 2); dg = lambda x: 1 / gm - 2 * gm / (gm ** 2 + (x - m) ** 2)
    q = lambda h: mp.quad(lambda x: h(x) * f(x), [-mp.inf, m, mp.inf])
    return q(lambda x: dm(x) ** 2), q(lambda x: dg(x) ** 2), q(lambda x: dm(x) * dg(x))
a3f = 0
for m, gm in [(0, 1), (2, mp.mpf('0.3')), (-1, 5)]:
    Imm, Igg, Img = fisher(mp.mpf(m), mp.mpf(gm)); a3f = max(a3f, abs(Imm * 2 * gm ** 2 - 1), abs(Igg * 2 * gm ** 2 - 1), abs(Img))
dH = lambda a, b: mp.acosh(1 + abs(a - b) ** 2 / (2 * a.imag * b.imag))
lev = abs(dH(mp.mpc(0, 1), mp.mpc(0, 2)) - mp.log(2))
maps = [lambda z: (2 * z + 1) / (z + 3), lambda z: -1 / z, lambda z: (5 * z - 2) / (z + 1)]
pairs = [(mp.mpc(0, 1), mp.mpc(1, 2)), (mp.mpc(-2, '0.1'), mp.mpc(3, 4)), (mp.mpc('0.5', '0.5'), mp.mpc('0.6', '0.4'))]
inv = max(abs(dH(G(a), G(b)) - dH(a, b)) for G in maps for a, b in pairs)
ok['A3'] = a3f < mp.mpf(10) ** -30 and lev < mp.mpf(10) ** -45 and inv < mp.mpf(10) ** -40
print(f'A3 Fisher information against I/(2γ²): {mp.nstr(a3f, 3)}; d_H(i, 2i) − ln 2 = {mp.nstr(lev, 3)}; Möbius invariance {mp.nstr(inv, 3)}')
# A4: height is level of detail
mp.mp.dps = 30
x0 = mp.mpf('0.3'); a4 = 0
for gm in [mp.mpf(1) / 8, mp.mpf(1) / 2, 1]:
    for j in range(7):
        k = 2 ** j
        v = mp.quadosc(lambda u: mp.cos(k * (x0 - u)) * gm / (mp.pi * (gm ** 2 + u ** 2)), [-mp.inf, mp.inf], omega=k)
        a4 = max(a4, abs(v - mp.e ** (-k * gm) * mp.cos(k * x0)))
counts = [sum(1 for j in range(7) if mp.e ** (-(2 ** j) * mp.mpf(2) ** (-kk)) > 1 / mp.e) for kk in range(8)]
ok['A4'] = a4 < mp.mpf(10) ** -20 and counts == list(range(8))
print(f'A4 each mode multiplied by e^(−kγ): worst {mp.nstr(a4, 3)}; modes kept above 1/e at γ = 2^-k, k = 0…7: {counts}')
# A5: errors along a chain
M = 10 ** 5; a5 = True; rows = []
for n in (1, 4, 16):
    relay = sum(cauchy(1j, M) for _ in range(n)); mean = sum(cauchy(1j, M) for _ in range(n)) / n
    gr, gmn = read(relay).imag, read(mean).imag
    gs = rng.standard_normal((M, n)); ss, sm = gs.sum(axis=1).std(), gs.mean(axis=1).std()
    sse = lambda s: s / np.sqrt(2 * M)
    a5 &= abs(gr - n) <= 3 * se(n, M) and abs(gmn - 1) <= 3 * se(1, M) and abs(ss - np.sqrt(n)) <= 3 * sse(np.sqrt(n)) and abs(sm - 1 / np.sqrt(n)) <= 3 * sse(1 / np.sqrt(n))
    rows.append(f'n={n}: relay {gr:.3f}, mean {gmn:.3f}; Gaussian sum {ss:.3f}, mean {sm:.4f}')
ok['A5'] = a5
print('A5 half-IQR of the relay and of the mean, against Gaussian sd: ' + '; '.join(rows))
for k in ('A1', 'A2', 'A3', 'A4', 'A5'): print(k, 'not killed' if ok[k] else 'KILLED')
