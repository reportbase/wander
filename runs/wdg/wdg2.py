"""WDG run 2: n other parties. See plans/wdg-plan.md (P7-P10).

The reader's h and n other parties' v_1..v_n, unit relations, every party drawn at V_i = H; the attitudes are the unit
sphere in n + 1 dimensions, one facing of each its positive orthant, swept evenly (uniform by area). Readings
a_i = v_i/h. P7, P8 in mpmath at 40 digits (derivatives and quadrature, never the closed forms being tested); P9, P10 by
product Gauss-Legendre quadrature in float64 and by drawing even points (numpy, seed 21).
Run: python3 runs/wdg/wdg2.py   (about a minute; needs mpmath and numpy)
"""
import random
import mpmath as mp
import numpy as np

mp.mp.dps = 40
def verdict(ok): return "not killed" if ok else "KILLED"
NS = range(1, 6)
c = lambda n: 2 ** n * mp.gamma(mp.mpf(n + 1) / 2) / mp.pi ** (mp.mpf(n + 1) / 2)           # P7's constant
sphere = lambda m: 2 * mp.pi ** (mp.mpf(m) / 2) / mp.gamma(mp.mpf(m) / 2)                     # area of S^(m-1)
print("c_n:", ", ".join(f"n={n} {mp.nstr(c(n), 10)}" for n in NS),
      f"(2/pi {mp.nstr(2 / mp.pi, 6)}, 8/pi^2 {mp.nstr(8 / mp.pi ** 2, 6)}, 12/pi^2 {mp.nstr(12 / mp.pi ** 2, 6)}, 64/pi^3 {mp.nstr(64 / mp.pi ** 3, 6)})")

# ---------------------------------------------------------------- P7: the even orthant is the n-dimensional Cauchy
def F(a):
    r = mp.sqrt(1 + sum(x * x for x in a)); return [1 / r] + [x / r for x in a]
def area_element(a):
    n = len(a)
    J = [[mp.diff(lambda s: F(a[:j] + [s] + a[j + 1:])[i], a[j]) for j in range(n)] for i in range(n + 1)]
    G = mp.matrix(n, n)
    for p in range(n):
        for q in range(n):
            G[p, q] = sum(J[i][p] * J[i][q] for i in range(n + 1))
    return mp.sqrt(mp.det(G))
rng = random.Random(21)
w7, tot7 = mp.mpf(0), mp.mpf(0)
for n in NS:
    for _ in range(20):
        a = [mp.mpf(2) ** mp.mpf(rng.uniform(-6, 6)) for _ in range(n)]
        w7 = max(w7, abs(area_element(a) / (1 + sum(x * x for x in a)) ** (-mp.mpf(n + 1) / 2) - 1))
    tot = c(n) * sphere(n) / 2 ** n * mp.quad(lambda r: r ** (n - 1) * (1 + r * r) ** (-mp.mpf(n + 1) / 2), [0, 1, mp.inf])
    tot7 = max(tot7, abs(tot - 1))
ok7 = w7 <= mp.mpf('1e-20') and tot7 <= mp.mpf('1e-25')
print(f"P7 area element vs (1+|a|^2)^(-(n+1)/2), n = 1..5, 100 points: worst {mp.nstr(w7, 3)}; totals off 1 by at most {mp.nstr(tot7, 3)} ->", verdict(ok7))

# ---------------------------------------------------------------- P8: every reading and every pair keeps its corner
grid = [mp.mpf(2) ** j for j in range(-8, 9, 2)]
def marginal(n, fixed):
    """Integrate out the n - len(fixed) other readings, radially."""
    m, s2 = n - len(fixed), sum(x * x for x in fixed)
    return c(n) * sphere(m) / 2 ** m * mp.quad(lambda r: r ** (m - 1) * (1 + s2 + r * r) ** (-mp.mpf(n + 1) / 2), [0, 1, mp.inf])
w8a = max(abs(marginal(n, [x]) / (2 / (mp.pi * (1 + x * x))) - 1) for n in range(2, 6) for x in grid)
w8b = max(abs(marginal(n, [x, y]) / (2 / (mp.pi * (1 + x * x + y * y) ** mp.mpf(1.5))) - 1)
          for n in range(3, 6) for x in grid for y in grid)
ok8 = w8a <= mp.mpf('1e-25') and w8b <= mp.mpf('1e-25')
print(f"P8 one-reading marginal vs 2/(pi(1+x^2)), n = 2..5: worst {mp.nstr(w8a, 3)}; two-reading vs run 1's wedge, n = 3..5:"
      f" worst {mp.nstr(w8b, 3)} ->", verdict(ok8))

# ---------------------------------------------------------------- P9, P10: shares by quadrature and by drawing
t, w = np.polynomial.legendre.leggauss(24)
def box_share(n, ends):
    """The n-dimensional Cauchy's mass on prod [0, ends_i], by product Gauss-Legendre."""
    R2, W = np.zeros(()), np.ones(())
    for e in ends:
        x, wx = (t + 1) / 2 * e, w / 2 * e
        R2 = np.add.outer(R2, x * x); W = np.multiply.outer(W, wx)
    return float(c(n)) * float(np.sum(W * (1 + R2) ** (-(n + 1) / 2)))
near = {n: box_share(n, [1.0] * n) for n in NS}
w9a = max(abs(near[n] - 1 / (n + 1)) for n in NS)
gen = np.random.default_rng(21)
N, z9, counts = 10_000_000, 0.0, {}
for n in NS:
    k = np.zeros(n + 1, dtype=np.int64)
    for _ in range(N // 1_000_000):
        X = np.abs(gen.standard_normal((1_000_000, n + 1)))         # the orthant's even points, up to their length
        k += np.bincount((X[:, 1:] > X[:, :1]).sum(axis=1), minlength=n + 1)
    p, se = k / N, np.sqrt((1 / (n + 1)) * (1 - 1 / (n + 1)) / N)
    counts[n] = p
    z9 = max(z9, float(np.max(np.abs(p - 1 / (n + 1)) / se)))
ok9 = w9a <= 1e-12 and z9 <= 5
for n in NS:
    print(f"   n={n}: near in all {near[n]:.15f} (1/(n+1) = {1 / (n + 1):.15f}); past the corner in k = 0..{n}: "
          + " ".join(f"{q:.4f}" for q in counts[n]))
print(f"P9 near in all 1/(n+1) to {w9a:.1e}; the count past the corner even, worst {z9:.2f} standard errors ->", verdict(ok9))

draws = [(1, 1, 1, 1, 1), (2, 1, 1, 1, 1), (2, 2, 2, 2, 2), (0.5, 1, 1, 1, 3), (0.5, 0.5, 2, 2, 1)]
sh = {d: box_share(5, d) for d in draws}
ok10 = abs(sh[draws[0]] - 1 / 6) <= 1e-12 and all(abs(sh[d] - 1 / 6) > 1e-6 for d in draws[1:])
print("P10 n = 5, near in all at V_i = c_i H: " + "; ".join(f"{d}: {sh[d]:.6f}" for d in draws), "->", verdict(ok10))
