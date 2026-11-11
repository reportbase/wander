# Numerical checks for the fifteen constants in list.md / answers.md.
# Run: python3 runs/twc/check.py
from fractions import Fraction
from mpmath import mp, mpf, mpc, quad, quadosc, nsum, findroot, primezeta, inf, pi, e, sqrt, log, exp, cos, sin, \
    atan, asin, catalan, factorial, nstr
mp.dps = 30
R = []
def rec(i, name, closed, check):
    R.append((i, name, closed, check, abs(closed - check)))

# 1 squarefree density: prod_p (1 - p^-2) = exp(-sum_k P(2k)/k)
chk = exp(-nsum(lambda k: primezeta(2 * k) / k, [1, inf]))
rec(1, "squarefree density", 6 / pi**2, chk)

# 2 mean distance of two uniform points in the unit disc
def inner(r):
    return quad(lambda t: (-r * cos(t) + sqrt(1 - r * r * sin(t)**2))**3 / 3, [0, pi / 2, pi, 3 * pi / 2, 2 * pi]) / pi
chk = quad(lambda r: 2 * r * inner(r), [0, 1])
rec(2, "disc mean distance", 128 / (45 * pi), chk)

# 3 black-body integral
chk = quad(lambda x: x**3 / (exp(x) - 1), [0, 1, 10, 50, inf])
rec(3, "x^3/(exp(x)-1)", pi**4 / 15, chk)

# 4 product of logs
chk = quad(lambda x: log(x) * log(1 - x), [0, mpf(1) / 2, 1])
rec(4, "ln x ln(1-x)", 2 - pi**2 / 6, chk)

# 5 expected number of uniforms until the sum passes 1: sum_n P(S_n <= 1),
#   P(S_n <= t) for t <= 1 by exact polynomial integration F_n(t) = int_0^t F_{n-1}(t-u) du
poly = [Fraction(1)]            # F_0(t) = 1
tot = Fraction(1)
for n in range(1, 40):
    poly = [Fraction(0)] + [c / (k + 1) for k, c in enumerate(poly)]   # valid on t<=1: F_n = int_0^t F_{n-1}(s) ds
    tot += sum(poly)
rec(5, "draws to exceed 1", e, mpf(tot.numerator) / tot.denominator)

# 6 derangements
d0, d1 = 1, 0
for n in range(2, 41):
    d0, d1 = d1, (n - 1) * (d0 + d1)
rec(6, "derangements", 1 / e, mpf(d1) / factorial(40))

# 7 lower end of convergence of x -> a^x : fixed point x = a^x with multiplier ln(a)*x = -1
a, x = findroot(lambda a, x: (a**x - x, log(a) * x + 1), (mpf("0.07"), mpf("0.35")))
rec(7, "tower lower bound", exp(-e), a)

# 8 sum n^3/n!
chk = nsum(lambda n: n**3 / factorial(n), [0, inf])
rec(8, "sum n^3/n!", 5 * e, chk)

# 9 cos x/(1+x^2) over the line
chk = 2 * quadosc(lambda x: cos(x) / (1 + x * x), [0, inf], omega=1)
rec(9, "cos/(1+x^2)", pi / e, chk)

# 10 i^i principal value: exp(i*Log i), Log i = int_1^i dz/z along the straight segment
L = quad(lambda t: (mpc(0, 1) - 1) / (1 + t * (mpc(0, 1) - 1)), [0, 1])
chk = exp(mpc(0, 1) * L)
assert abs(chk.imag) < mpf(10)**-25
rec(10, "i^i", exp(-pi / 2), chk.real)

# 11 Levy: ln L = -(1/ln 2) int_0^1 ln x/(1+x) dx  (mean of -ln x under the Gauss measure)
chk = exp(-quad(lambda x: log(x) / (1 + x), [0, 1]) / log(2))
rec(11, "Levy", exp(pi**2 / (12 * log(2))), chk)

# 12 arcsine law at 1/4: discrete walk, 2n steps, P(time positive = 2k) = u_{2k} u_{2n-2k}
n = 200000
u = [mpf(1)]
for k in range(1, n + 1):
    u.append(u[-1] * (2 * k - 1) / (2 * k))
s = sum(u[k] * u[n - k] for k in range(0, n // 4)) + u[n // 4] * u[n - n // 4] / 2
rec(12, "arcsine 1/4 (walk, 4e5 steps)", mpf(1) / 3, s)
# 12b the limit law itself: density of the fraction of time positive, 1/(B(1/2,1/2) sqrt(x(1-x))), B by quadrature
dens = lambda x: 1 / sqrt(x * (1 - x))
chk = quad(dens, [0, mpf(1) / 4]) / quad(dens, [0, mpf(1) / 2, 1])
rec(12, "arcsine 1/4 (limit law, quad)", mpf(1) / 3, chk)

# 13 mean distance in the unit square
chk = quad(lambda x, y: 4 * (1 - x) * (1 - y) * sqrt(x * x + y * y), [0, 1], [0, 1])
rec(13, "square mean distance", (2 + sqrt(2) + 5 * log(1 + sqrt(2))) / 15, chk)

# 14 arctan x / x
chk = quad(lambda x: atan(x) / x, [0, 1])
rec(14, "arctan x/x", catalan, chk)

# 15 infinite ladder of unit resistors
r = mpf(1)
for _ in range(200):
    r = 1 + r / (1 + r)
rec(15, "ladder", (1 + sqrt(5)) / 2, r)

for i, name, c, k, d in R:
    print(f"{i:2d} {name:32s} closed {nstr(c, 15):>20s}  check {nstr(k, 15):>20s}  diff {nstr(d, 3)}")
print("worst:", nstr(max(r[4] for r in R), 3))
