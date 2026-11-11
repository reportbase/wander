# CHS run 1: chaos as the turn doubled, in three charts. plans/chs-plan.md, predictions C1-C7.
import random, statistics
from fractions import Fraction as F
from mpmath import mp, mpf, atan, asin, sqrt, pi, log, quad, tan, cos, inf

ok = {}
def say(k, good, msg):
    ok[k] = ok.get(k, True) and bool(good)
    print(f"  {k} {'ok  ' if good else 'FAIL'} {msg}")
def T(s): return abs(2 * s / (1 - s * s))

rng = random.Random(833)
def rat():
    while True:
        s = F(rng.randint(1, 60), rng.randint(1, 60))
        if s != 1: return s

print("C1  three charts, one map (exact rationals)")
bad = 0
for _ in range(40):
    s = rat(); v2 = s * s / (1 + s * s); t = T(s); c = 1 / s
    a = (t * t / (1 + t * t) == 4 * v2 * (1 - v2))
    b = (abs(F(1, 2) * (c - 1 / c)) == 1 / t)
    n = (F(1, 2) * (c - 1 / c) == c - (c * c + 1) / (2 * c))
    bad += not (a and b and n)
say("C1", bad == 0, f"40 rational slopes: share -> 4v2(1-v2), reciprocal slope -> (c - 1/c)/2, Newton's step: {40 - bad} of 40 exact")

mp.dps = 60
G = lambda x: 2 * atan(x) / pi
print("C2  each chart's law is kept")
for x in ["0.2", "0.5", "1", "2", "7"]:
    x = mpf(x); a = (sqrt(1 + x * x) - 1) / x
    d = abs(G(a) + 1 - G(1 / a) - G(x))
    say("C2", d < mpf(10) ** -40, f"half-Cauchy, T(s) <= {x}: a = {mp.nstr(a, 8)}, diff {mp.nstr(d, 3)}")
A = lambda y: 2 * asin(sqrt(y)) / pi
for x in ["0.1", "0.5", "0.9"]:
    x = mpf(x); y = (1 - sqrt(1 - x)) / 2
    d = abs(A(y) + 1 - A(1 - y) - A(x))
    say("C2", d < mpf(10) ** -40, f"arcsine, 4y(1-y) <= {x}: diff {mp.nstr(d, 3)}")
C = lambda x: mpf(1) / 2 + atan(x) / pi
for x in ["-3", "-0.4", "0", "0.9", "5"]:
    x = mpf(x); r1 = x - sqrt(x * x + 1); r2 = x + sqrt(x * x + 1)      # (c - 1/c)/2 <= x  <=>  c <= r1 or 0 < c <= r2
    d = abs(C(r1) + C(r2) - C(0) - C(x))
    say("C2", d < mpf(10) ** -40, f"Cauchy, (c - 1/c)/2 <= {x}: diff {mp.nstr(d, 3)}")

print("C3  ln 2 a step in every chart")
L2 = log(2)
tent = log(mpf(2))
half = quad(lambda th: log(2 * (1 + tan(th) ** 2) / (1 - tan(th) ** 2) ** 2), [0, pi / 4, pi / 2]) * 2 / pi
boole = quad(lambda th: log((1 + 1 / tan(th) ** 2) / 2), [-pi / 2, 0, pi / 2]) / pi
logi = quad(lambda ph: log(abs(4 * cos(2 * ph))), [0, pi / 4, pi / 2]) * 2 / pi
for name, v in [("tent", tent), ("T on the half-Cauchy", half), ("(x - 1/x)/2 on the Cauchy", boole), ("4y(1-y) on the arcsine", logi)]:
    say("C3", abs(v - L2) < mpf(10) ** -20, f"{name}: {mp.nstr(v, 25)}, off ln 2 by {mp.nstr(abs(v - L2), 3)}")

print("C4  one digit a step at fixed K (exact)")
def tent_n(g, n):
    for _ in range(n): g = 1 - abs(1 - 2 * g)
    return g
offs = [F(1, 97), F(1, 3), F(1, 2), F(2, 3), F(96, 97)]
for m in [3, 4, 5]:
    K = 2 ** m
    for n in range(1, 7):
        fine = 2 ** (m + n); coarse = fine // 2
        fixed = all(len({int(K * tent_n((j + o) / fine, n)) for o in offs}) == 1 for j in range(fine))
        split = any(len({int(K * tent_n((j + o) / coarse, n)) for o in offs}) > 1 for j in range(coarse))
        ok["C4"] = ok.get("C4", True) and fixed and split
    print(f"  C4 {'ok  ' if ok['C4'] else 'FAIL'} K = {K}: n = 1..6, fixed by the cell among 2^(m+n), not among 2^(m+n-1)")

print("C5  no rational slope cycles; the orbit's cost doubles")
rep = corner = 0; ratios = []
for _ in range(200):
    s = rat(); seen = {s}; bits = []
    for n in range(12):
        if s == 1: corner += 1; break
        s = T(s); bits.append(s.denominator.bit_length())
        if s in seen: rep += 1; break
        seen.add(s)
    if len(bits) == 12: ratios.append(bits[11] / bits[10])
say("C5", rep == 0 and corner == 0, f"200 rational slopes, 12 steps: repeats {rep}, corners reached {corner}")
say("C5", len(ratios) == 200 and min(ratios) > 1.9 and max(ratios) < 2.1,
    f"denominator bits, step 12 over step 11: min {min(ratios):.4f}, max {max(ratios):.4f}; last denominators about {int(statistics.median([0])) or ''}2^{int(statistics.median([r for r in ratios]) * 0)}".rstrip("2^0") + f"(median bits at step 12: see below)")
s = F(3, 7); 
for n in range(12): s = T(s)
print(f"       from 3/7, step 12: a denominator of {s.denominator.bit_length()} bits")

print("C6  a count of p digits holds the orbit about p steps")
starts = ["0.3", "1.7", "0.428571", "2.2", "0.61"]
def orbit(s0, prec, steps):
    mp.prec = prec; s = mpf(s0); out = []
    for _ in range(steps):
        d = 1 - s * s
        s = abs(2 * s / d) if d != 0 else mpf(10) ** 30
        out.append(+s)
    return out
for p in [24, 53, 113]:
    steps = p + 40; firsts = []
    for s0 in starts:
        ref = orbit(s0, 2000, steps); low = orbit(s0, p, steps)
        mp.prec = 200
        f = next((i + 1 for i in range(steps) if abs(2 * atan(ref[i]) / pi - 2 * atan(low[i]) / pi) > mpf("0.1")), None)
        firsts.append(f)
    med = statistics.median(firsts)
    say("C6", p - 12 <= med <= p + 2, f"p = {p}: first steps apart {firsts}, median {med} (band {p - 12}..{p + 2})")

print()
for k in ["C1", "C2", "C3", "C4", "C5", "C6"]:
    print(f"{k}: {'not killed' if ok[k] else 'KILLED'}")
print(f"C7: {'not killed' if ok['C1'] and ok['C5'] and ok['C6'] else 'KILLED'}")
