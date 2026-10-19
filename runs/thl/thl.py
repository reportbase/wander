"""THL: the arc from the chord, by two rays. See plans/thl-plan.md (P1-P8).

The chord AB, A = (0, 0), B = (1, 0), drawn at one unit (V = H). From A a ray reading s = v/h (slope s); from B a ray
reading the flip, h/v = 1/s, measured from BA. The crossing is found by intersecting the two lines, never from the
closed form being tested. Rational points in exact arithmetic (fractions); the rest with mpmath at 60 digits.
Run: python3 runs/thl/thl.py   (a few seconds; needs mpmath)
"""
from fractions import Fraction as F
import random
import mpmath as mp
mp.mp.dps = 60
M = mp.mpf
def verdict(ok): return "not killed" if ok else "KILLED"
results = {}

def cross(tA, tB, one=1):
    """Lines y = tA*x through A and y = tB*(1 - x) through B (tB the slope measured from BA); their crossing."""
    x = tB / (tA + tB)
    return x, tA * x

rational = [F(m, n) for m in range(1, 41) for n in range(1, 41)]
grid = [M(10) ** (M(-10) + M(20) * i / 1999) for i in range(2000)]

# ---------------------------------------------------------------- P1: the crossing traces the semicircle (Thales)
ok1 = True
for s in rational:
    x, y = cross(s, 1 / s)
    if (x - F(1, 2)) ** 2 + y ** 2 != F(1, 4): ok1 = False
    # directions of the two rays from P: towards A is (-x, -y), towards B is (1 - x, -y); perpendicular iff dot = 0
    if (-x) * (1 - x) + (-y) * (-y) != 0: ok1 = False
w1 = max(abs(mp.sqrt((cross(s, 1 / s)[0] - M('0.5')) ** 2 + cross(s, 1 / s)[1] ** 2) - M('0.5')) for s in grid)
ok1 = ok1 and w1 < M('1e-50')
results['P1'] = (ok1, f"exact on {len(rational)} rational readings; worst |PO - 1/2| over 1e-10..1e10: {mp.nstr(w1, 3)}")

# ---------------------------------------------------------------- P2: the two rays are h and v
ok2, w2 = True, M(0)
for s in grid:
    x, y = cross(s, 1 / s)
    h, v = 1 / mp.sqrt(1 + s * s), s / mp.sqrt(1 + s * s)
    AP, BP = mp.sqrt(x * x + y * y), mp.sqrt((1 - x) ** 2 + y * y)
    w2 = max(w2, abs(AP - h), abs(BP - v), abs(x - h * h), abs((1 - x) - v * v), abs(y - h * v), abs(h * h + v * v - 1))
for s in rational:
    x, y = cross(s, 1 / s)
    h2, v2 = 1 / (1 + s * s), s * s / (1 + s * s)                # h², v² exactly
    if x * x + y * y != h2 or (1 - x) ** 2 + y * y != v2 or x != h2 or 1 - x != v2 or y * y != h2 * v2: ok2 = False
ok2 = ok2 and w2 < M('1e-50')
results['P2'] = (ok2, f"AP = h, BP = v, foot h² | v², height hv; worst {mp.nstr(w2, 3)}; exact at the rationals: {ok2}")

# ---------------------------------------------------------------- P3: facing = 2 x the ray's angle; half-angle form
ok3, w3 = True, M(0)
for s in grid:
    x, y = cross(s, 1 / s)
    phi = mp.atan2(y, x - M('0.5'))
    w3 = max(w3, abs(phi - 2 * mp.atan(s)))
for s in rational:
    x, y = cross(s, 1 / s)
    if (2 * (x - F(1, 2)), 2 * y) != ((1 - s * s) / (1 + s * s), 2 * s / (1 + s * s)): ok3 = False
    m, n = s.numerator, s.denominator
    if (n * n - m * m) ** 2 + (2 * m * n) ** 2 != (n * n + m * m) ** 2: ok3 = False
ok3 = ok3 and w3 < M('1e-50')
results['P3'] = (ok3, f"worst |facing - 2 atan s| {mp.nstr(w3, 3)}; half-angle form and Euclid's triples exact: {ok3}")

# ---------------------------------------------------------------- P4: the corner at the top; the flip the mirror
ok4 = cross(F(1), F(1)) == (F(1, 2), F(1, 2))
for s in rational:
    x, y = cross(s, 1 / s)
    xf, yf = cross(1 / s, s)
    if (xf, yf) != (1 - x, y): ok4 = False
results['P4'] = (ok4, f"P(1) = {cross(F(1), F(1))}; P(1/s) the mirror of P(s) at all {len(rational)} rationals: {ok4}")

# ---------------------------------------------------------------- P5: Steiner; a conic in every drawing, a circle only at V = H
ok5, w5, near5 = True, M(0), M(1)
for c in (M(2), M('0.5'), M(3), M('1.0001')):
    for s in grid:
        x, y = cross(c * s, c / s)
        w5 = max(w5, abs(x * x - x + y * y / (c * c)))
        if M('0.1') <= s <= 10:
            near5 = min(near5, abs(mp.sqrt((x - M('0.5')) ** 2 + y * y) - M('0.5')))
def cr(a, b, c_, d):                                             # cross-ratio of four points of the projective line
    return ((a - c_) * (b - d)) / ((a - d) * (b - c_))
random.seed(1)
w5c = M(0)
for c in (M(1), M(2), M('0.5')):
    for _ in range(50):
        ts = [M(random.uniform(0.01, 100)) for _ in range(4)]
        tb = [-(c * c) / t for t in ts]                          # B's lines' plane slopes (pointing back over A)
        w5c = max(w5c, abs(cr(*ts) - cr(*tb)))
# a perspectivity sends the common line AB to itself; here A's line of slope t -> 0 goes to B's line of slope -c²/t,
# which grows without bound (the vertical at B), not to AB's slope 0
perspective = any(abs(-(c * c) / M('1e-40')) < 1 for c in (M(1), M(2), M('0.5'), M(3), M('1.0001')))
ok5 = w5 < M('1e-45') and near5 > M('1e-6') and w5c < M('1e-50') and not perspective
results['P5'] = (ok5, f"ellipse x² - x + y²/c² = 0 to {mp.nstr(w5, 3)}; nearest to the circle at c ≠ 1, s in [0.1, 10]: "
                      f"{mp.nstr(near5, 3)} off; cross-ratio kept to {mp.nstr(w5c, 3)}; AB goes to the vertical at B")

# ---------------------------------------------------------------- P6: paired at equal angles, a line
w6 = M(0)
for s in grid:
    x, y = cross(s, s)
    w6 = max(w6, abs(x - M('0.5')), abs(y - s / 2))
results['P6'] = (w6 < M('1e-50'), f"every crossing on x = 1/2 at height s/2, worst {mp.nstr(w6, 3)}")

# ---------------------------------------------------------------- P7: the even sweep of one ray is the even turn
N = 10000
da = mp.pi / 2 / N
pts = []
for k in range(N + 1):
    a = k * da
    if k == 0: pts.append((M(1), M(0))); continue
    if k == N: pts.append((M(0), M(0))); continue
    s = mp.tan(a)
    pts.append(cross(s, 1 / s))
w7 = max(abs(mp.sqrt((pts[k + 1][0] - pts[k][0]) ** 2 + (pts[k + 1][1] - pts[k][1]) ** 2) - mp.sin(da)) for k in range(N))
mids = [mp.tan((k + M('0.5')) * da) for k in range(N)]
below1 = sum(1 for s in mids if s <= 1)
w7c = max(abs(M(sum(1 for m in mids if m <= q)) / N - 2 / mp.pi * mp.atan(q)) for q in (M('0.5'), M(2), M(10)))
ok7 = w7 < M('1e-50') and below1 == N // 2 and w7c <= M('1e-4')
results['P7'] = (ok7, f"10,000 chords equal to sin(Δα) to {mp.nstr(w7, 3)}; {below1} of {N} readings at or below the corner; "
                      f"share vs (2/π)atan s within {mp.nstr(w7c, 3)}")

# ---------------------------------------------------------------- P8: the mean proportional (Elements VI.13)
random.seed(2)
w8 = M(0)
for _ in range(100):
    x1, x2 = M(10) ** M(random.uniform(-6, 6)), M(10) ** M(random.uniform(-6, 6))
    L = x1 + x2
    s = mp.sqrt(x2 / x1)
    xf, yf = cross(s, 1 / s)                                     # on the chord scaled to 1
    foot, height = xf * L, yf * L
    w8 = max(w8, abs(foot - x1) / x1, abs(height - mp.sqrt(x1 * x2)) / mp.sqrt(x1 * x2))
results['P8'] = (w8 < M('1e-45'), f"foot at the join, height √(x₁x₂), worst relative {mp.nstr(w8, 3)} over 100 pairs")

for k, (ok, msg) in results.items():
    print(f"{k}: {verdict(ok)}. {msg}")
