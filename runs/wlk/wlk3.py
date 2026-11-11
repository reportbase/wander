"""WLK run 3: the shrinking stride. Run from the repo root."""
import random
from fractions import Fraction as F
from mpmath import mp, mpf, atan, pi, quad
mp.dps = 50; random.seed(13)
def Z(x): return ((x*x - 1) / (x*x + 1), 2*x / (x*x + 1))
def mul(a, b): return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])
def div(a, b): n = b[0]*b[0] + b[1]*b[1]; return ((a[0]*b[0] + a[1]*b[1]) / n, (a[1]*b[0] - a[0]*b[1]) / n)
def tadd(a, b): return (a + b) / (1 - a*b)
def walk(x0, ds):
    xs = [x0]
    for d in ds: xs.append(xs[-1] - d)
    return xs
C1 = C3 = C6 = True
walks = [walk(F(3), [F(3, 50)] * 50)]
for _ in range(200):
    x0 = F(random.randint(1, 4000), 100); n = random.randint(2, 40)
    cuts = sorted(F(random.randint(1, 10**6), 10**6) for _ in range(n - 1)); cuts = [F(0)] + cuts + [F(1)]
    walks.append(walk(x0, [x0 * (cuts[i+1] - cuts[i]) for i in range(n) if cuts[i+1] > cuts[i]]))
for xs in walks:
    prod = (F(1), F(0)); comp = None; arcs = []
    for a, b in zip(xs, xs[1:]):
        f = div(Z(b), Z(a)); prod = mul(prod, f); C6 &= f[0]*f[0] + f[1]*f[1] == 1
        t = (a - b) / (1 + a*b); arcs.append(t); comp = t if comp is None else (tadd(comp, t) if comp*t != 1 else None)
    C1 &= prod == div(Z(xs[-1]), Z(xs[0]))
    if comp is not None: C3 &= comp == (xs[0] - xs[-1]) / (1 + xs[0]*xs[-1])
eq = walks[0]; a_eq = [(a - b) / (1 + a*b) for a, b in zip(eq, eq[1:])]
C6 &= len(set(a_eq)) == len(a_eq) and a_eq[-1] == max(a_eq)
# from the corner to the foot, three stride sizes: half-arc slope exactly 1
for n in (7, 100, 1000):
    xs = walk(F(1), [F(1, n)] * n); comp = None
    for a, b in zip(xs, xs[1:]):
        t = (a - b) / (1 + a*b)
        if comp is None: comp = t
        elif comp * t == 1: comp = 'inf'
        else: comp = tadd(comp, t)
    C3 &= comp == 1
C2 = True
for k in range(1, 31):
    d = F(1, 2) ** k if k < 30 else F(1, 10**9)
    for m in (1, 2, 17, 1000):
        x2 = m * d; x1 = x2 + d
        C2 &= x2 / (x1 - x2) == m and x1 / (x1 - x2) == m + 1
print('C1, C2, C3, C6 (exact):', C1, C2, C3, C6)
C4 = True
for x0 in (1, 30, 10**6):
    sums = []
    for N in (10, 1000, 100000):
        d = mpf(x0) / N; s = mpf(0)
        for j in range(N):
            a = mpf(x0) - j*d; b = a - d; s += 2*atan(d / (1 + a*b))
        sums.append(s)
    C4 &= all(abs(s - 2*atan(mpf(x0))) < mpf(10)**-45 for s in sums)
    short = pi - 2*atan(mpf(x0)); print(f'  x0={x0}: arc gathered 2·arctan(x0) = {float(2*atan(mpf(x0))):.9f}, short of pi by {float(short):.3e} (2/x0 = {2/x0:.3e}), spread over N: {float(max(sums)-min(sums)):.1e}')
    if x0 > 1: C4 &= abs(short * x0 / 2 - 1) < 1.0 / x0
print('C4:', C4)
C5 = True; prev = None; x0 = mpf(1)
I = quad(lambda x: 1 / (1 + x*x)**3, [0, x0])
for N in (250, 500, 1000, 2000, 4000):
    d = x0 / N; s = sum(d / (1 + (x0 - j*d) * (x0 - (j+1)*d)) for j in range(N)); ex = s - atan(x0)
    lead = d*d/3 * I; ratio = (prev / ex) if prev else None
    print(f'  N={N}: sum of slopes - arctan = {float(ex):.6e}, leading term {float(lead):.6e}' + (f', ratio to previous {float(ratio):.4f}' if ratio else ''))
    C5 &= ex > 0 and abs(ex / lead - 1) < 0.01
    if ratio is not None and N >= 1000: C5 &= 3.9 < ratio < 4.1
    prev = ex
print('C5:', C5)
th = F(1); n = 10; print('Euler factor modulus^2 (theta=1, n=10):', 1 + (th/n)**2, '> 1 :', 1 + (th/n)**2 > 1)
print('ALL:', C1 and C2 and C3 and C4 and C5 and C6)
