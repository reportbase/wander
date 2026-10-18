# SUM (plans/sum-plan.md): a sum of Cauchys read as a relay of addresses. Exact (mpmath) and seeded (numpy).
# Run: python3 sum/sum.py [run], run 1 the first thresholds, run 2 those in standard errors (plan's run 2)
import numpy as np, mpmath as mp
mp.mp.dps = 200
import sys
RUN = int(sys.argv[1]) if len(sys.argv) > 1 else 1
rng = np.random.default_rng(20261018 + 1000 * (RUN - 1))   # run 2: fresh seeds
se = lambda g, M: 2 * np.pi * g * np.sqrt(3 / (16 * M))   # a Cauchy quartile's standard error
near = lambda x, g, M: (abs(abs(x) - g) <= 0.01) if RUN == 1 else (abs(abs(x) - g) <= 3 * se(g, M))
turn = lambda n: np.tan(rng.uniform(-np.pi / 2, np.pi / 2, n))          # a uniform turn's landing from height 1
q = lambda x: (np.quantile(x, 0.25), np.quantile(x, 0.75))
def ks2(a, b):
    a, b = np.sort(a), np.sort(b); z = np.concatenate([a, b])
    return np.max(np.abs(np.searchsorted(a, z, 'right') / len(a) - np.searchsorted(b, z, 'right') / len(b)))
ok = {}
# P1: exact, then the two-stage relay against one turn from height 3
ex = max(abs(mp.e ** (-1 * abs(t)) * mp.e ** (-2 * abs(t)) - mp.e ** (-3 * abs(t))) for t in map(mp.mpf, ['0.1', '0.5', '1', '2', '5']))
N = 10 ** 6
relay = 1 * turn(N) + 2 * turn(N)       # from height 3 to the line at height 2 (a drop of 1), then from height 2 to 0
direct = 3 * turn(N)
qr, qd, d1 = q(relay), q(direct), ks2(relay, direct)
ok['P1'] = ex < mp.mpf(10) ** -190 and all(near(x, 3, N) for x in qr + qd) and d1 < (0.003 if RUN == 1 else 1.63 * np.sqrt(2 / N))
print(f'P1 exact: characteristic functions e^-|t|·e^-2|t| − e^-3|t| at most {mp.nstr(ex, 3)}; relay quartiles {qr[0]:.4f} {qr[1]:.4f}, '
      f'one turn from 3: {qd[0]:.4f} {qd[1]:.4f}; KS {d1:.5f}')
# P2: the sum against tangent addition
x1, x2 = turn(N), turn(N)
qs, qt = q(x1 + x2), q((x1 + x2) / (1 - x1 * x2))
ok['P2'] = all(near(x, 2, N) for x in qs) and all(near(x, 1, N) for x in qt)
print(f'P2 X1 + X2 quartiles {qs[0]:.4f} {qs[1]:.4f}; tangent addition (X1 + X2)/(1 − X1X2) {qt[0]:.4f} {qt[1]:.4f}')
# P3: the mean of n standard Cauchys
p3 = []
for n in (1, 10, 1000):
    m = np.empty(10 ** 5)
    for i in range(0, 10 ** 5, 1000): m[i:i + 1000] = turn((1000, n)).mean(axis=1)
    p3.append((n, q(m)))
ok['P3'] = all(near(x, 1, 10 ** 5) for _, qq in p3 for x in qq)
print('P3 the mean of n: ' + '; '.join(f'n={n} quartiles {a:.4f} {b:.4f}' for n, (a, b) in p3))
# P4: normalized sums of symmetric Pareto(1) against Cauchy(0, π/2); then the landing of a planar Brownian motion
G = np.pi / 2
cdfC = lambda x: 0.5 + np.arctan(x / G) / np.pi
def ks1(x): x = np.sort(x); n = len(x); F = cdfC(x); return max(np.max(np.arange(1, n + 1) / n - F), np.max(F - np.arange(n) / n))
p4 = []
for n in (10, 100, 1000):
    s = np.empty(10 ** 5)
    for i in range(0, 10 ** 5, 100):
        y = 1 / rng.uniform(0, 1, (100, n)) * rng.choice([-1, 1], (100, n))
        s[i:i + 100] = y.sum(axis=1) / n
    p4.append((n, ks1(s)))
# the plan asked for a stepped Brownian motion (steps of 1e-3, 1e4 paths); its hitting time has no mean and a median of
# about 5.5e6 such steps a path, so this script uses the exact construction instead: the hitting time of height h is
# h²/Z² (Z standard normal) and the horizontal place then is √τ·N
tau = G ** 2 / rng.standard_normal(10 ** 6) ** 2
land = np.sqrt(tau) * rng.standard_normal(10 ** 6)
ql = q(land)
falls = p4[0][1] > p4[1][1] > p4[2][1]
ok['P4'] = (falls and p4[2][1] <= 0.02 and all(abs(abs(x) - G) <= 0.05 for x in ql)) if RUN == 1 else (p4[2][1] < 1.63 / np.sqrt(10 ** 5) and all(near(x, G, 10 ** 6) for x in ql))
print('P4 KS to Cauchy(0, π/2) of S_n/n: ' + ', '.join(f'n={n} {d:.4f}' for n, d in p4) + f'; Brownian landing from π/2 (exact construction) quartiles {ql[0]:.4f} {ql[1]:.4f}')
for k in ('P1', 'P2', 'P3', 'P4'): print(k, 'not killed' if ok[k] else 'KILLED')
