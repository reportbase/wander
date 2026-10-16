"""PAM run 1 (plans/pam-plan.md): the addresses' median follows the weight's symmetry, the payload's mean and law follow
the payload. A1–A3 exact (mpmath quadrature, 30 digits); A4 a seeded simulation (numpy).
Run: python3 pam/pam.py   (about a minute)
"""
import numpy as np
from mpmath import mp, mpf, quad, findroot, sin, cos, tan, atan, pi, log, degrees, fabs
mp.dps = 30
rng = np.random.default_rng(7)
PH = rng.uniform(0, 2 * np.pi, 12)
def relief(t):
    return 1 + sum(mpf('0.3') / n * cos(n * t + mpf(PH[n - 1])) for n in range(1, 13))
W = {
    '(i) even': lambda t: mpf(1),
    '(ii) 1 + cos4θ/2': lambda t: 1 + cos(4 * t) / 2,
    '(iii) relief, symmetrised': lambda t: (relief(t) + relief(pi / 2 - t)) / 2,
    '(iv) (2 + cos2θ)/3': lambda t: (2 + cos(2 * t)) / 3,
    '(v) relief': relief,
    '(vi) sin²2θ': lambda t: sin(2 * t)**2,
}
ok = {}
def median_dir(rho):
    pts = [mpf(0)] + [pi / 2 * k / 24 for k in range(1, 24)] + [pi / 2]
    tot = quad(rho, pts)
    F = lambda x: quad(rho, [0, x]) - tot / 2
    lo, hi = mpf(0), pi / 2                       # bisection to a bracket, then a root
    for _ in range(60):
        mid = (lo + hi) / 2
        if F(mid) < 0: lo = mid
        else: hi = mid
    return findroot(F, (lo + hi) / 2), tot
print('A1, A2: the median direction')
med = {}
for k, rho in W.items():
    th, tot = median_dir(rho)
    med[k] = (th, tot)
    print(f"  {k:28} θ_m = {mp.nstr(degrees(th), 15)}°  s_m = {mp.nstr(tan(th), 12)}  off π/4 by {mp.nstr(fabs(th - pi/4), 3)}")
ok['A1'] = all(fabs(med[k][0] - pi / 4) <= mpf(10)**-20 for k in ('(i) even', '(ii) 1 + cos4θ/2', '(iii) relief, symmetrised', '(vi) sin²2θ'))
th5 = med['(v) relief'][0]
left = quad(relief, [0, pi / 4]); right = quad(relief, [pi / 4, pi / 2])
side_ok = (th5 < pi / 4) == (left > right)          # the median moves toward the heavier side
print(f"  (v): weight below 45° {mp.nstr(left, 8)}, above {mp.nstr(right, 8)}; median moved toward the heavier side: {side_ok}")
ok['A2'] = fabs(degrees(med['(iv) (2 + cos2θ)/3'][0]) - mpf('32.103')) <= mpf('0.001') and \
    fabs(degrees(th5) - 45) > mpf('0.1') and side_ok
print('A3: the truncated mean of s')
def tmean(rho, S, tot):
    a = atan(S)
    return quad(lambda t: tan(t) * rho(t), [0, pi / 4, a - (a - pi / 4) / 2, a]) / tot
a3 = True
for k, pred in (('(i) even', 2 / pi * log(10)), ('(ii) 1 + cos4θ/2', 2 / pi * (mpf(3) / 2) * log(10)),
                ('(iv) (2 + cos2θ)/3', 2 / pi * ((mpf(1) / 3) / (mpf(2) / 3)) * log(10))):
    tot = med[k][1]
    climb = tmean(W[k], mpf(10)**7, tot) - tmean(W[k], mpf(10)**6, tot)
    good = fabs(climb - pred) <= mpf(10)**-5; a3 &= good
    print(f"  {k:28} climb 10⁶→10⁷ {mp.nstr(climb, 12)} predicted {mp.nstr(pred, 12)} {'ok' if good else 'OFF'}")
tot6 = med['(vi) sin²2θ'][1]
m6 = quad(lambda t: tan(t) * sin(2 * t)**2, [0, pi / 4, pi / 2]) / tot6
good = fabs(m6 - 4 / pi) <= mpf(10)**-20; a3 &= good
print(f"  (vi) sin²2θ mean {mp.nstr(m6, 25)} against 4/π {mp.nstr(4 / pi, 25)} {'ok' if good else 'OFF'}")
ok['A3'] = a3
print('A4: the payload at θ = 0.3, a_n, b_n uniform on (−1, 1), standardised by √(K/3)')
from math import erf, sqrt
r2 = np.random.default_rng(11); M = 2_000_000; th = 0.3; a4 = True
Phi = np.vectorize(lambda z: 0.5 * (1 + erf(z / sqrt(2))))
for K in (1, 2, 4, 8, 16, 32, 64):
    n = np.arange(1, K + 1)
    p = np.zeros(M)
    for j in range(K):   # accumulate term by term to bound memory
        p += r2.uniform(-1, 1, M) * np.cos(n[j] * th) + r2.uniform(-1, 1, M) * np.sin(n[j] * th)
    z = np.sort(p / np.sqrt(K / 3)); F = Phi(z); i = np.arange(1, M + 1)
    D = max((i / M - F).max(), (F - (i - 1) / M).max())
    bound = 0.03 / K + 0.003; good = D <= bound and (K != 1 or D > 0.01); a4 &= good
    print(f"  K {K:3}: Kolmogorov distance {D:.5f}  bound {bound:.5f}{'  (and > 0.01)' if K == 1 else ''} {'ok' if good else 'OFF'}")
t = np.linspace(0, 2 * np.pi, 4097)[:-1]
worst = 0.0
for _ in range(200):
    K = 64; a = r2.uniform(-1, 1, K); b = r2.uniform(-1, 1, K); n = np.arange(1, K + 1)
    pt = (a[:, None] * np.cos(np.outer(n, t)) + b[:, None] * np.sin(np.outer(n, t))).sum(0)
    worst = max(worst, abs(pt.mean()))
print(f"  the full-turn mean of p over 200 reliefs (K = 64, 4,096 even points): at most {worst:.2e}")
a4 &= worst <= 1e-12
ok['A4'] = a4
for k in ('A1', 'A2', 'A3', 'A4'):
    print(k, 'not killed' if ok[k] else 'KILLED')
