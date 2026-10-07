"""Checks for plans/normalizations.md (6 October): one relation (h, v) normalized three ways (by h, by the sum v + h,
by the whole sqrt(h^2 + v^2)), and what dividing by a noisy h does to the reading.

    python3 plans/normalizations/checks.py
"""
import math, random

print("1. Three normalizations of one relation s = v/h")
print("   s        odds (by h)  probability (by v+h)  circle share g (by the whole)  logit ln s")
for s in (0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 1e9):
    p = s / (1 + s); g = math.atan(s) / (math.pi / 2)
    print(f"   {s:<8g} {s:<12g} {p:<21.4f} {g:<30.4f} {math.log(s) if s > 0 else float('-inf'):.4f}")

print("\n   the flip s -> 1/s, in each:")
for s in (0.25, 0.5, 2.0):
    p, pf = s/(1+s), (1/s)/(1+1/s); g, gf = math.atan(s)/(math.pi/2), math.atan(1/s)/(math.pi/2)
    print(f"   s={s}: p + p(1/s) = {p+pf:.12f}   g + g(1/s) = {g+gf:.12f}")

print("\n2. The two bells on the log axis x = ln s (density of each share per unit of x)")
print("   x/ln2   circle: (1/pi) sech x   ratio   probability: p(1-p) = (1/4) sech^2(x/2)   ratio")
pc = pp = None
for n in range(0, 9):
    x = n * math.log(2)
    c = (1 / math.pi) / math.cosh(x); q = 0.25 / math.cosh(x / 2) ** 2
    print(f"   {n:<6d} {c:<24.6f} {'' if pc is None else f'{pc/c:.3f}':<7} {q:<41.6f} {'' if pp is None else f'{pp/q:.3f}'}")
    pc, pp = c, q
# areas
N = 400000; L = 60; dx = 2 * L / N
ac = sum((1 / math.pi) / math.cosh(-L + i * dx) for i in range(N)) * dx
ap = sum(0.25 / math.cosh((-L + i * dx) / 2) ** 2 for i in range(N)) * dx
print(f"   areas: circle {ac:.6f}, probability {ap:.6f} (both 1)")

print("\n3. Dividing by a noisy h: the reading's far tail")
random.seed(1)
for sigma in (0.05, 0.2, 0.5):
    M = 2_000_000
    r = [(1.0 + random.gauss(0, sigma * 1.0)) for _ in range(M)]
    vv = [(1.0 + random.gauss(0, sigma)) for _ in range(M)]
    s = [abs(b / a) for a, b in zip(r, vv)]
    t10 = sum(1 for x in s if x > 10) / M; t100 = sum(1 for x in s if x > 100) / M
    tail = f"{t10/t100:.1f}" if t100 > 0 else "n/a (none past 100)"
    print(f"   sigma={sigma}: P(s>10)={t10:.2e}  P(s>100)={t100:.2e}  ratio {tail}  (Cauchy-like tail: about 10)")
