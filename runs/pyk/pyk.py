"""PYK run 1 (plans/pyk-plan.md): the turn's, the boost's and the stride's Pythagoras.
Run from the repository's root: python3 runs/pyk/pyk.py"""
import math, sys
sys.set_int_max_str_digits(0)
from fractions import Fraction as Fr
import mpmath as mp
import sympy as sp

mp.mp.dps = 60
V = {}
s, a, k, eps = sp.symbols("s a kappa epsilon", real=True)
x, y, u, v = sp.symbols("x y u v", real=True)

def op(p, q, kap):
    return (p + q) / (1 - kap * p * q)

KAPPAS = {"turn": 1, "boost": -1, "stride": 0}

print("== K1. One identity, three signs ==")
k1a = sp.simplify(1 + k * op(s, a, k)**2 - (1 + k * s**2) * (1 + k * a**2) / (1 - k * s * a)**2) == 0
k1b = sp.expand((x**2 + k * y**2) * (u**2 + k * v**2) - ((x*u - k*y*v)**2 + k * (x*v + y*u)**2)) == 0
k1c = sp.simplify(op(s, a, -1) - (s + a) / (1 + s * a)) == 0
print(f"K1 identity in kappa: {k1a}; norms multiply: {k1b}; kappa = -1 is velocity addition: {k1c}")
V["K1"] = k1a and k1b and k1c

print("== K2. The heat each kind keeps ==")
k2 = True
for name, kap in KAPPAS.items():
    c = op(s, a, kap)
    kept = sp.simplify(sp.diff(c, s) / (1 + kap * c**2) * (1 + kap * s**2) - 1) == 0
    others = {}
    for p in (sp.Rational(1, 2), 2):
        ratio = sp.diff(c, s) * (1 + kap * c**2)**(-p) / (1 + kap * s**2)**(-p)
        val = ratio.subs({s: sp.Rational(1, 3), a: sp.Rational(1, 5)})
        others[str(p)] = sp.nsimplify(val) == 1
    print(f"   {name}: ds/(1 + kappa s^2) kept: {kept}; (1 + kappa s^2)^(-p) also kept at p = 1/2, 2: {others}")
    k2 &= kept and not any(others.values())
V["K2"] = k2

print("== K3. Only the turn has a total ==")
t1 = sp.integrate(1 / (1 + s**2), (s, -sp.oo, sp.oo))
t2 = sp.integrate(1 / (1 - s**2), (s, 0, 1))
t3 = sp.integrate(1, (s, 0, sp.oo))
print(f"K3 turn {t1}; boost on [0, 1): {t2}; stride on [0, oo): {t3}")
V["K3"] = t1 == sp.pi and t2 in (sp.oo, sp.zoo) and t3 == sp.oo

print("== K4. Shares and the corner ==")
k4a = sp.simplify(1 / (1 - s**2) - s**2 / (1 - s**2) - 1) == 0
eqsol = sp.solve(sp.Eq(1 / (1 - s**2), s**2 / (1 - s**2)), s)
k4b = sp.simplify(op(1, a, -1) - 1) == 0 and sp.simplify(op(-1, a, -1) + 1) == 0
# never reached from |s| < 1: composing two slopes inside stays inside (checked on a grid of fractions)
inside = all(abs(op(Fr(p, 50), Fr(q, 50), -1)) < 1 for p in range(-49, 50) for q in range(-49, 50))
print(f"K4 gamma^2 - (gamma beta)^2 = 1: {k4a}; the two terms equal at: {eqsol}; light cone fixed by every boost: {k4b}; composition keeps |s| < 1: {inside}")
V["K4"] = k4a and eqsol == [] and k4b and inside

print("== K5. The exchange in each kind ==")
K2f = lambda z: (1 + z) / (1 - z)
k5a = sp.simplify(K2f(op(s, a, -1)) - K2f(s) * K2f(a)) == 0
k5b = sp.simplify(K2f(-s) * K2f(s) - 1) == 0
k5c = sp.solve(sp.Eq(K2f(s), 1), s) == [0]
print(f"K5 Doppler factors multiply: {k5a}; s -> -s sends k to 1/k: {k5b}; its fixed point s = 0 (rest): {k5c}")
V["K5"] = k5a and k5b and k5c

print("== K6. The rational lattice on the hyperbola ==")
pts = set()
for d in range(1, 2001):
    D2 = d * d
    f = 1
    while f * f <= D2:
        if D2 % f == 0:
            g = D2 // f
            if (f + g) % 2 == 0:
                c, e = (f + g) // 2, (g - f) // 2
                pts.add((Fr(c, d), Fr(e, d))); pts.add((Fr(c, d), Fr(-e, d)))
        f += 1
k6a = True; ts = set()
for (X, Y) in pts:
    T = Y / (1 + X)
    ts.add(T)
    k6a &= abs(T) < 1 and (1 + T * T) / (1 - T * T) == X and 2 * T / (1 - T * T) == Y and X * X - Y * Y == 1
k6u = len(ts) == len(pts)
k6b = all(((1 + Fr(p, q)**2) / (1 - Fr(p, q)**2))**2 - (2 * Fr(p, q) / (1 - Fr(p, q)**2))**2 == 1
          for q in range(1, 61) for p in range(-q + 1, q))
print(f"K6 {len(pts)} rational points (x > 0, denominator <= 2000), each from one t in (-1, 1): {k6a and k6u}; every t lands on it: {k6b}")
V["K6"] = k6a and k6u and k6b

print("== K7. Nothing closes ==")
closers = []; checked = 0; kgrow = True
for q in range(2, 41):
    for p in range(1, q):
        if math.gcd(p, q) != 1:
            continue
        re, im, N = q * q + p * p, 2 * p * q, q * q - p * p
        zr, zi, Nn = 1, 0, 1
        for n in range(1, 201):
            zr, zi = zr * re + zi * im, zr * im + zi * re      # split-complex product, j^2 = +1
            Nn *= N
            if zi == 0 and zr == Nn:
                closers.append((p, q, n)); break
        kk = Fr(q + p, q - p)                                   # Doppler factor (1 + t)/(1 - t)
        kgrow &= kk > 1 and kk**200 > 10**10
        checked += 1
print(f"K7 {checked} rational half-slopes in (0, 1) tried to n = 200: closing ones {closers}; Doppler factor grows without bound: {kgrow}")
V["K7"] = closers == [] and kgrow

print("== K8. Only the square, for boosts too ==")
tt = mp.mpf(1) / 3
worst = {}
for p in (1, 2, 3, 4):
    p = mp.mpf(p)
    lam = 1 / (1 - tt**p)**(1 / p)
    mx = mp.mpf(0)
    for kk in range(1000):
        Y = -3 + 6 * (kk + mp.mpf(1) / 7) / 1000
        X = (1 + abs(Y)**p)**(1 / p)
        Xn, Yn = lam * (X + tt * Y), lam * (Y + tt * X)
        mx = max(mx, abs(abs(Xn)**p - abs(Yn)**p - 1))
    worst[int(p)] = mx
print("K8 worst departure from |x|^p - |y|^p = 1 after one composed boost:", {kk: mp.nstr(val, 5) for kk, val in worst.items()})
V["K8"] = worst[2] < mp.mpf(10)**-50 and all(worst[p] > mp.mpf(10)**-6 for p in (1, 3, 4))

print("== K9. The limits ==")
ser = sp.series(op(eps * s, eps * a, k), eps, 0, 5).removeO()
k9a = sp.simplify(ser - (eps * (s + a) + eps**3 * k * s * a * (s + a))) == 0
lhs = (1 + op(s, a, 1)**2).subs({s: sp.I * s, a: sp.I * a}, simultaneous=True)
rhs = ((1 + s**2) * (1 + a**2) / (1 - s * a)**2).subs({s: sp.I * s, a: sp.I * a}, simultaneous=True)
k9b = sp.simplify(lhs - (1 - op(s, a, -1)**2)) == 0 and sp.simplify(rhs - (1 - s**2) * (1 - a**2) / (1 + s * a)**2) == 0
print(f"K9 series s + a + kappa sa(s + a) + O(5): {k9a}; the turn's identity at s -> is is the boost's: {k9b}")
V["K9"] = k9a and k9b

print("== verdicts ==")
for kk, val in V.items():
    print(f"  {kk}: {'not killed' if val else 'KILLED'}")
