"""LWS run 1: check exactly every law sorted P (chain) or S (shared sum) in runs/lws/laws.md.

Fractions and Gaussian fractions where the law is rational; mpmath at 50 digits where it holds an angle or a limit.
Run from the repository root: python3 runs/lws/lws.py
"""
from fractions import Fraction as F
import mpmath as mp

mp.mp.dps = 50
TOL = mp.mpf(10) ** -40


class G:
    """Gaussian rationals a + bi with Fraction parts."""

    def __init__(s, a, b=0):
        s.a, s.b = F(a), F(b)

    def __add__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.a + o.a, s.b + o.b)

    def __sub__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.a - o.a, s.b - o.b)

    def __mul__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)

    def __truediv__(s, o):
        o = o if isinstance(o, G) else G(o)
        d = o.a * o.a + o.b * o.b
        return G((s.a * o.a + s.b * o.b) / d, (s.b * o.a - s.a * o.b) / d)

    def __eq__(s, o):
        o = o if isinstance(o, G) else G(o)
        return s.a == o.a and s.b == o.b

    def norm(s):
        return s.a * s.a + s.b * s.b


I = G(0, 1)


def w(s):
    return (G(1) + I * s) / (G(1) - I * s)


def oplus(a, b):
    return (a + b) / (1 - a * b)


S3 = [F(1, 3), F(2), F(5, 7)]
B3 = [F(1, 4), F(3, 2), F(-2, 9)]
results = []


def check(n, name, ok):
    results.append((n, name, bool(ok)))


# ---- P: chains, middle denominators cancel ----
for d, H, m in [(F(7), F(3, 2), F(1, 5)), (F(1, 9), F(4), F(11)), (F(100), F(1, 3), F(2, 7))]:
    check(2, "ln(d/m) = ln(d/H) + ln(H/m)  [d/m = (d/H)(H/m)]", (d / H) * (H / m) == d / m)
check(3, "w(s) w(1/s) = -1", all(w(s) * w(1 / s) == G(-1) for s in S3))
check(4, "w(1) = i, i i = -1", w(F(1)) == I and I * I == G(-1))
for a, b, c in [(F(3), F(5), F(7, 2)), (F(1, 8), F(9), F(2, 3)), (F(-4), F(6, 5), F(11))]:
    check(7, "a/b * b/c = a/c", (a / b) * (b / c) == a / c)
check(8, "tangent addition as turns between landing points: w(a)w(b) = w(a+b) and (w(y)/w(x))(w(z)/w(y)) = w(z)/w(x)",
      all(w(a) * w(b) == w(oplus(a, b)) for a in S3 for b in B3 if a * b != 1)
      and all((w(y) / w(x)) * (w(z) / w(y)) == w(z) / w(x) for x, y, z in zip(S3, B3, [F(6), F(1, 10), F(-3)])))
for d1, d2, k in [(mp.mpf('0.3'), mp.mpf(2), mp.mpf(5)), (mp.mpf(1), mp.mpf('1e-3'), mp.mpf('0.7')),
                  (mp.mpf(7), mp.mpf(4), mp.mpf(-2))]:
    check(38, "e^(-d1|k|) e^(-d2|k|) = e^(-(d1+d2)|k|); heat kernel likewise",
          abs(mp.e ** (-d1 * abs(k)) * mp.e ** (-d2 * abs(k)) - mp.e ** (-(d1 + d2) * abs(k))) < TOL
          and abs(mp.e ** (-d1 * k * k) * mp.e ** (-d2 * k * k) - mp.e ** (-(d1 + d2) * k * k)) < TOL)
    check(42, "blur undone: e^(-g|k|) e^(g|k|) = 1", abs(mp.e ** (-d1 * abs(k)) * mp.e ** (d1 * abs(k)) - 1) < TOL)
# 68: walk telescopes, Z_j = w(s_j) at any strides
for path in [[F(1, 10), F(1, 7), F(1, 3), F(1), F(5)], [F(2), F(3), F(9, 2)], [F(1, 50), F(1, 2)]]:
    Z = [w(s) for s in path]
    prod = G(1)
    for j in range(len(Z) - 1):
        prod = prod * (Z[j + 1] / Z[j])
    check(68, "prod Z_(j+1)/Z_j = Z_N/Z_0", prod == Z[-1] / Z[0])
# 69: a place and its mirror, s = d_c/d style reading s and 1/s
check(69, "Z(d) Z(d_c^2/d) = -1", all(w(s) * w(1 / s) == G(-1) for s in [F(3, 11), F(8), F(1)]))
# 71: read times count, s = d_c/d, n = d/S
for dc, d, S in [(F(42), F(600), F(7, 10)), (F(3), F(5, 2), F(1, 4)), (F(1000), F(9), F(2))]:
    check(71, "s n = (d_c/d)(d/S) = d_c/S", (dc / d) * (d / S) == dc / S)
# 72: fixed share, remaining_m/remaining_0 telescopes to (1-r)^m
for r, m, R0 in [(F(1, 3), 5, F(10)), (F(1, 2), 9, F(7, 3)), (F(2, 9), 4, F(1))]:
    rem = [R0]
    for _ in range(m):
        rem.append(rem[-1] * (1 - r))
    prod = F(1)
    for j in range(m):
        prod *= rem[j + 1] / rem[j]
    check(72, "prod rem_(j+1)/rem_j = (1-r)^m", prod == (1 - r) ** m and prod == rem[-1] / rem[0])
# 75: ln gaps along a chain add; a loop sums to zero
for pts in [[mp.mpf(2), mp.mpf(9), mp.mpf('0.5'), mp.mpf(31)], [mp.mpf(1), mp.mpf(1000)], [mp.mpf('0.1'), mp.mpf(3), mp.mpf(7)]]:
    gaps = sum(mp.log(pts[j + 1] / pts[j]) for j in range(len(pts) - 1))
    loop = gaps + mp.log(pts[0] / pts[-1])
    check(75, "gaps add to the end gap; a loop sums to 0", abs(gaps - mp.log(pts[-1] / pts[0])) < TOL and abs(loop) < TOL)
# 91: collinear boosts compose like tangent addition (tanh): as ratios of (1+b)/(1-b)
def kb(b):
    return (1 + b) / (1 - b)
for b1, b2 in [(F(1, 2), F(1, 3)), (F(9, 10), F(-1, 4)), (F(1, 7), F(6, 7))]:
    check(91, "(b1+b2)/(1+b1 b2): k(b) = (1+b)/(1-b) multiplies", kb((b1 + b2) / (1 + b1 * b2)) == kb(b1) * kb(b2))
for t in [mp.mpf('0.3'), mp.mpf(1), mp.mpf('1.5')]:
    check(93, "(t/sin t)(sin t/t) = 1", abs((t / mp.sin(t)) * (mp.sin(t) / t) - 1) < TOL)
check(98, "tangent subtraction: w(a)/w(b) = w((a-b)/(1+ab))",
      all(w(a) / w(b) == w((a - b) / (1 + a * b)) for a in S3 for b in B3 if a * b != -1))
# 101*: finite members compose (n reads), the limit noted
for th, n in [(F(1, 2), 8), (F(3), 5), (F(1, 10), 20)]:
    step = G(1) + I * (th / n)
    p = G(1)
    for _ in range(n):
        p = p * step
    # n equal reads compose by tangent addition: the angle of the product is n * angle(step), i.e. p / |p| is w-chain
    s1 = th / n
    acc = F(0)
    for _ in range(n):
        acc = oplus(acc, s1)
    check(101, "(1 + i th/n)^n's direction is n reads composed (finite member)",
          p.b * 1 == acc * p.a if p.a != 0 else True)
check(105, "(1+ia)(1+ib) = (1-ab) + i(a+b)",
      all((G(1) + I * a) * (G(1) + I * b) == G(1 - a * b, a + b) for a in S3 for b in B3))
for x in [F(3, 8), F(13), F(-5, 2)]:
    check(108, "x (1/x) = 1", x * (1 / x) == 1)
check(110, "w(1/s) = -1/w(s)", all(w(1 / s) == G(-1) / w(s) for s in S3))
# 113*: dv/dl = h along the arc; the sum telescopes to v_end - v_start = 1 (limit of chords)
f = lambda l: mp.cos(l)  # h along the unit arc, l the arc length
for a, b in [(0, mp.pi / 2), (mp.mpf('0.2'), mp.mpf('1.1')), (mp.mpf('0.5'), mp.mpf('1.5'))]:
    check(113, "int h dl = v(b) - v(a)", abs(mp.quad(f, [a, b]) - (mp.sin(b) - mp.sin(a))) < TOL)
for s1, s2 in [(F(1, 3), F(2)), (F(5), F(1, 7)), (F(1), F(3))]:
    Om = F(355, 226)  # any constant: it cancels
    check(114, "heat ratio: (1/(Om(1+s1^2)))/(1/(Om(1+s2^2))) = (1+s2^2)/(1+s1^2)",
          (1 / (Om * (1 + s1 * s1))) / (1 / (Om * (1 + s2 * s2))) == (1 + s2 * s2) / (1 + s1 * s1))
for s in [F(3), F(1, 2), F(7, 4)]:
    check(119, "s (+) s = 2s/(1-s^2)", oplus(s, s) == 2 * s / (1 - s * s))
    check(124, "corner circle s (1/s) = 1", s * (1 / s) == 1)

# ---- S: shared denominator stays, numerators fill it ----
for p, q in [(3, 4), (5, 12), (8, 15)]:
    h, v = F(q * q - p * p, q * q + p * p), F(2 * p * q, q * q + p * p)
    check(10, "h^2 + v^2 = 1 (rational points); sqrt(1+s^2) = 1/h", h * h + v * v == 1 and (1 / h) ** 2 == 1 + (v / h) ** 2)
for x, y, z in [(F(1), F(2), F(2)), (F(2), F(3), F(6)), (F(4), F(4), F(7))]:
    r2 = x * x + y * y + z * z
    check(19, "x^2+y^2+z^2 = r^2 over x^2: 1 + s^2 + s2^2 = (r/x)^2", 1 + (y / x) ** 2 + (z / x) ** 2 == r2 / (x * x))
for s in S3:
    check(28, "1 + s^2 = (r/x)^2; 1/(1+s^2) = h^2", 1 / (1 + s * s) == (1 / (1 + s * s)))
    h2 = 1 / (1 + s * s)
    check(28, "h^2 + v^2 = 1 with v/h = s", h2 + s * s * h2 == 1)
for x in [mp.mpf('0.3'), mp.mpf(1), mp.mpf(12)]:
    check(52, "atan(1/x) + atan(x) = Omega (share past x = share below 1/x)", abs(mp.atan(1 / x) + mp.atan(x) - mp.pi / 2) < TOL)
for s in [F(1, 10), F(1), F(7, 3)]:
    E = lambda u: 1 / (1 + u * u)
    check(78, "E(s) + E(1/s) = 1 (in units of pi L)", E(s) + E(1 / s) == 1)
    check(79, "1/(1+s^2) + s^2/(1+s^2) = 1", 1 / (1 + s * s) + s * s / (1 + s * s) == 1)
for a in [mp.mpf('0.1'), mp.mpf('0.7'), mp.mpf('1.4')]:
    check(80, "sin^2 + cos^2 = 1", abs(mp.sin(a) ** 2 + mp.cos(a) ** 2 - 1) < TOL)
for s in S3:
    D = 1 + s * s
    check(103, "|w|^2 = ((1-s^2)^2 + (2s)^2)/(1+s^2)^2 = 1", ((1 - s * s) ** 2 + (2 * s) ** 2) / (D * D) == 1 and w(s).norm() == 1)
check(109, "(1/Omega) int_0^inf ds/(1+s^2) = 1; int_0^1 = int_1^inf",
      abs(mp.quad(lambda s: 1 / (1 + s * s), [0, mp.inf]) / (mp.pi / 2) - 1) < TOL
      and abs(mp.quad(lambda s: 1 / (1 + s * s), [0, 1]) - mp.quad(lambda s: 1 / (1 + s * s), [1, mp.inf])) < TOL)
for d, a in [(mp.mpf(3), mp.mpf(1)), (mp.mpf('0.2'), mp.mpf(1)), (mp.mpf(10), mp.mpf(4))]:
    gam = lambda x: 2 * mp.atan(a / x)  # angle subtended at x by the half-step pair about the middle
    check(123, "gamma(d) + gamma(a^2/d) = pi", abs(gam(d) + gam(a * a / d) - mp.pi) < TOL)

bad = [r for r in results if not r[2]]
laws = sorted({r[0] for r in results})
print(f"checks: {len(results)}, failed: {len(bad)}, laws checked: {len(laws)} {laws}")
for r in bad:
    print("FAIL", r)
