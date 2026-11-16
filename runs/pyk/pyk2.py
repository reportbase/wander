"""PYK run 2 (plans/pyk-plan.md): K2', K3', K7'. Run from the repository's root: python3 runs/pyk/pyk2.py"""
import math, random
from fractions import Fraction as Fr
import mpmath as mp
import sympy as sp
mp.mp.dps = 60
s, a, d = sp.symbols("s a delta", positive=True)
op = lambda p, q, kap: (p + q) / (1 - kap * p * q)
rng = random.Random(1058)
ok2 = True
for kap in (1, -1):
    for p in (sp.Rational(1, 2), 2):
        for _ in range(5):
            sv, av = sp.Rational(rng.randint(1, 9), 11), sp.Rational(rng.randint(1, 9), 13)
            c = op(s, a, kap)
            r = (sp.diff(c, s) * (1 + kap * c**2)**(-p) / (1 + kap * s**2)**(-p)).subs({s: sv, a: av})
            ok2 &= sp.nsimplify(sp.simplify(r)) != 1
print("K2' powers 1/2 and 2 not kept for kappa = +1, -1:", ok2)
I = sp.integrate(1 / (1 - s**2), (s, 0, 1 - d))
ok3a = sp.simplify(sp.expand_log(I - sp.log((2 - d) / d) / 2, force=True)) == 0
ok3b = all(abs(mp.quad(lambda z: 1 / (1 - z**2), [0, 1 - mp.mpf(10)**-n]) - mp.log(2 * mp.mpf(10)**n - 1) / 2) < mp.mpf(10)**-40
           for n in (1, 5, 10, 20, 50))
print("K3' integral to 1 - delta = (1/2) ln((2 - delta)/delta):", ok3a, "; numerically at delta = 10^-n:", ok3b)
ok7 = all((Fr(q + p, q - p) > 1) and Fr(q + p, q - p)**200 > Fr(q + p, q - p)**100 > 1
          for q in range(2, 41) for p in range(1, q) if math.gcd(p, q) == 1)
print("K7' every Doppler factor > 1, powers strictly increasing:", ok7)
for k_, v_ in (("K2'", ok2), ("K3'", ok3a and ok3b), ("K7'", ok7)):
    print(f"  {k_}: {'not killed' if v_ else 'KILLED'}")
