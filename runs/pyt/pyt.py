"""PYT run 1 (plans/pyt-plan.md): Pythagoras from one standpoint, explored.
Run from the repository's root: python3 runs/pyt/pyt.py"""
import math, random, sys
sys.set_int_max_str_digits(0)
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp
import sympy as sp

mp.mp.dps = 60
V = {}
s, a, t = sp.symbols("s a t", real=True)

def oplus(x, y):
    return (x + y) / (1 - x * y)

print("== P1. The shares ==")
lo, hi = 1 / (1 + s**2), s**2 / (1 + s**2)
p1a = sp.simplify(lo + hi - 1) == 0
p1b = sp.simplify(lo.subs(s, 1 / s) - hi) == 0 and sp.simplify(hi.subs(s, 1 / s) - lo) == 0
eq = sp.solve(sp.Eq(lo, hi), s)
rng = random.Random(1057)
p1c = True
for _ in range(10000):
    q = Fr(rng.randint(-10**6, 10**6), rng.randint(1, 10**6))
    L, H = 1 / (1 + q * q), q * q / (1 + q * q)
    p1c &= (L + H == 1) and ((L == H) == (abs(q) == 1))
    if q != 0:
        p1c &= (1 / (1 + 1 / q**2) == H)
print(f"P1 shares add to 1: {p1a}; exchange swaps them: {p1b}; equal only at s = {eq}; 10,000 rationals exact: {p1c}")
V["P1"] = p1a and p1b and sorted(eq) == [-1, 1] and p1c

print("== P2. Composition is the product of sums of two squares ==")
p2a = sp.simplify(1 + oplus(s, a)**2 - (1 + s**2) * (1 + a**2) / (1 - s * a)**2) == 0
x, y, u, v = sp.symbols("x y u v", real=True)
p2b = sp.expand((x**2 + y**2) * (u**2 + v**2) - ((x*u - y*v)**2 + (x*v + y*u)**2)) == 0
# the link: s = y/x, a = v/u; the composed direction is (xu - yv : xv + yu)
p2c = sp.simplify((x*v + y*u) / (x*u - y*v) - oplus(y / x, v / u)) == 0
print(f"P2 1 + (s+a)^2 = (1+s^2)(1+a^2)/(1-sa)^2: {p2a}; Brahmagupta-Fibonacci: {p2b}; its direction the composed slope: {p2c}")
V["P2"] = p2a and p2b and p2c

print("== P3. The heat is unchanged by composing ==")
sa_ = oplus(s, a)
p3a = sp.simplify(sp.diff(sa_, s) / (1 + sa_**2) * (1 + s**2) - 1) == 0
p3b = sp.simplify(sp.diff(1 / s, s) / (1 + 1 / s**2) + 1 / (1 + s**2)) == 0
print(f"P3 d(s+a)/(1+(s+a)^2) = ds/(1+s^2): {p3a}; the exchange reverses it: {p3b}")
V["P3"] = p3a and p3b

print("== P4. The landing point ==")
w = lambda z: (1 + sp.I * z) / (1 - sp.I * z)
p4a = sp.simplify(sp.expand((1 + sp.I * s) * (1 - sp.I * s)) - (1 + s**2)) == 0
p4b = sp.simplify(w(s) * sp.conjugate(w(s)) - 1) == 0
p4c = sp.simplify(w(s) * w(a) - w(oplus(s, a))) == 0
p4d = sp.simplify(w(s) * w(1 / s) + 1) == 0
p4e = sp.simplify(w(1) - sp.I) == 0
print(f"P4 (1+is)(1-is) = 1+s^2: {p4a}; |w|^2 = 1: {p4b}; w(s)w(a) = w(s+a): {p4c}; w(s)w(1/s) = -1: {p4d}; w(1) = i: {p4e}")
V["P4"] = all((p4a, p4b, p4c, p4d, p4e))

print("== P5. The rational directions ==")
pts = set()
for c in range(1, 2001):
    for A in range(0, c + 1):
        B2 = c * c - A * A
        B = math.isqrt(B2)
        if B * B == B2:
            for sx in (1, -1):
                for sy in (1, -1):
                    pts.add((Fr(sx * A, c), Fr(sy * B, c)))
p5a = True; ts = set()
for (X, Y) in pts:
    if (X, Y) == (-1, 0):
        continue
    T = Y / (1 + X)
    ts.add(T)
    p5a &= ((1 - T * T) / (1 + T * T) == X) and (2 * T / (1 + T * T) == Y)
p5u = len(ts) == len(pts) - 1   # one t a point
p5b = True; ngen = 0
for P in range(-60, 61):
    for Q in range(1, 61):
        T = Fr(P, Q)
        X, Y = (1 - T * T) / (1 + T * T), 2 * T / (1 + T * T)
        p5b &= (X * X + Y * Y == 1); ngen += 1
p5c = True
for (X, Y) in pts:
    if X > 0 and Y >= 0:
        S = Y / X
        r2 = 1 + S * S
        rn, rd = math.isqrt(r2.numerator), math.isqrt(r2.denominator)
        T = Y / (1 + X)
        p5c &= (rn * rn == r2.numerator and rd * rd == r2.denominator) and (2 * T / (1 - T * T) == S if T * T != 1 else True)
print(f"P5 {len(pts)} rational points with denominator <= 2000: each from one half-slope t: {p5a and p5u}; {ngen} t's all on the circle: {p5b}; triples = rational s with rational root, s = 2t/(1-t^2): {p5c}")
V["P5"] = p5a and p5u and p5b and p5c

print("== P6. Rational directions never close a turn, but at the axes ==")
closers = set(); p6_checked = 0
for Q in range(1, 41):
    for P in range(0, Q + 1):
        if math.gcd(P, Q) != 1:
            continue
        re, im, N = Q * Q - P * P, 2 * P * Q, P * P + Q * Q
        zr, zi, Nn = 1, 0, 1
        for n in range(1, 201):
            zr, zi = zr * re - zi * im, zr * im + zi * re
            Nn *= N
            if zi == 0 and zr == Nn:
                closers.add((Fr(P, Q), n)); break
        p6_checked += 1
print(f"P6 {p6_checked} rational half-slopes in [0, 1] tried to n = 200; closing ones (t, first n): {sorted(closers)}")
V["P6"] = {c[0] for c in closers} == {Fr(0), Fr(1)}

print("== P7. Space, and n parties ==")
p7 = True
for n in (1, 2, 3):
    ss = sp.symbols(f"s1:{n+1}", real=True)
    R2 = 1 + sum(q**2 for q in ss)
    uvec = sp.Matrix([1] + list(ss)) / sp.sqrt(R2)
    J = uvec.jacobian(sp.Matrix(ss))
    dens = sp.sqrt(sp.simplify((J.T * J).det()))
    ok = sp.simplify(dens - R2**sp.Rational(-(n + 1), 2)) == 0
    const = sp.gamma(sp.Rational(n + 1, 2)) / sp.pi**sp.Rational(n + 1, 2)
    area = 2 * sp.pi**sp.Rational(n + 1, 2) / sp.gamma(sp.Rational(n + 1, 2))
    ok2 = sp.simplify(2 / area - const) == 0     # both antipodes land on one point of the screen
    print(f"   n = {n}: surface element (1 + |s|^2)^(-{n+1}/2): {ok}; density constant Gamma((n+1)/2)/pi^((n+1)/2) = {const}: {ok2}")
    p7 &= ok and ok2
r = sp.symbols("r", positive=True)
tot1 = sp.integrate(1 / sp.pi / (1 + s**2), (s, -sp.oo, sp.oo))
tot2 = sp.integrate(2 * sp.pi * r / (2 * sp.pi) * (1 + r**2)**sp.Rational(-3, 2), (r, 0, sp.oo))
print(f"   totals: n = 1 {tot1}, n = 2 {tot2}")
g = np.random.default_rng(1057).standard_normal((200000, 3))
sx = np.hypot(g[:, 1], g[:, 2]) / np.abs(g[:, 0])
share = np.mean(sx <= 1); pred = 1 - 1 / math.sqrt(2); se = math.sqrt(pred * (1 - pred) / 200000)
print(f"   200,000 points on S^2: share within |s| <= 1 = {share:.5f}, 1 - 1/sqrt 2 = {pred:.5f}, {abs(share-pred)/se:.2f} standard errors")
V["P7"] = p7 and tot1 == 1 and tot2 == 1 and abs(share - pred) <= 3 * se

print("== P8. Rational points in space ==")
nq = 0; p8 = True
for d in range(1, 301):
    for A in range(0, d + 1):
        rem = d * d - A * A
        for B in range(0, math.isqrt(rem) + 1):
            C2 = rem - B * B
            C = math.isqrt(C2)
            if C * C != C2:
                continue
            for Cs in ({C, -C}):
                k = d + Cs
                if k == 0:
                    continue          # the south pole
                # t_i = A/k, B/k; the inverse stereographic image, cleared of denominators
                den = k * k + A * A + B * B
                p8 &= (2 * A * k * d == A * den) and (2 * B * k * d == B * den) and ((k * k - A * A - B * B) * d == Cs * den)
                nq += 1
print(f"P8 {nq} rational points on the unit sphere (d <= 300, a, b >= 0) from a rational pair (t1, t2): {p8}")
V["P8"] = p8

print("== P9. Only the square ==")
def lp(xx, yy, p):
    return (abs(xx)**p + abs(yy)**p)**(mp.mpf(1) / p)
tt = mp.mpf(1) / 3
worst = {}
for p in (1, 2, 3, 4):
    p = mp.mpf(p); lam = 1 / lp(1, tt, p); mx = mp.mpf(0)
    for k in range(1000):
        th = 2 * mp.pi * (k + mp.mpf(1) / 7) / 1000
        c_, s_ = mp.cos(th), mp.sin(th)
        X = mp.sign(c_) * abs(c_)**(2 / p); Y = mp.sign(s_) * abs(s_)**(2 / p)     # on |x|^p + |y|^p = 1
        mx = max(mx, abs(lp(lam * (X - tt * Y), lam * (Y + tt * X), p) - 1))
    worst[int(p)] = mx
print("P9 worst departure from the l_p unit circle after one composed step:", {k: mp.nstr(v, 5) for k, v in worst.items()})
V["P9"] = worst[2] < mp.mpf(10)**-50 and all(worst[p] > mp.mpf(10)**-6 for p in (1, 3, 4))

print("== P10. Where it stops ==")
c10a = sp.sqrt(sp.Rational(1, 2)).is_rational is False
c10b = sp.integrate(1 / (1 + s**2), (s, 0, sp.oo))
# the median by the exchange alone: the heat on (0, 1] carried by s -> 1/s onto [1, oo)
c10c = sp.simplify((1 / (1 + (1 / s)**2)) * sp.diff(1 / s, s) + 1 / (1 + s**2)) == 0
print(f"P10 (a) corner share 1/sqrt 2 irrational: {c10a}; (b) total of the heat = {c10b}, rational: {c10b.is_rational}; (c) heat below 1 equals heat above by the exchange alone: {c10c}")
V["P10"] = c10a and c10b == sp.pi / 2 and c10b.is_rational is False and c10c

print("== verdicts ==")
for k, val in V.items():
    print(f"  {k}: {'not killed' if val else 'KILLED'}")
