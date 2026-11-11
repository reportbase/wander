# ONE run 1: plans/one-plan.md. Run from the repository root: python3 runs/one/one.py
from fractions import Fraction as F
import random
from mpmath import mp, mpf, sqrt, pi, atan, cos, sin, asinh
mp.dps = 50
HL = F(1, 30); S = F(7, 10)
THINGS = {'house': F(12), 'tower': F(60), 'mountain': F(3000)}
res = {}
def say(k, ok, msg):
    res[k] = res.get(k, True) and ok
    print(f"  {k} {'ok    ' if ok else 'KILLED'} {msg}")

print("J1 the twin: |dh| and dv each sum to 1 on the three paths")
n = 2000
# chord (1-t, t), square (1,t) then (1-t,1): exact
for name, pts in (('chord', [(1 - F(i, n), F(i, n)) for i in range(n + 1)]),
                  ('square', [(F(1), F(i, n)) for i in range(n + 1)] + [(1 - F(i, n), F(1)) for i in range(1, n + 1)])):
    dv = sum(b[1] - a[1] for a, b in zip(pts, pts[1:])); dh = sum(abs(b[0] - a[0]) for a, b in zip(pts, pts[1:]))
    L = sum(sqrt(mpf((b[0]-a[0])**2 + (b[1]-a[1])**2)) for a, b in zip(pts, pts[1:]))
    want = sqrt(2) if name == 'chord' else mpf(2)
    say('J1', dv == 1 and dh == 1 and abs(L - want) < mpf(10)**-40, f"{name}: sum dv {dv}, sum |dh| {dh}, length {mp.nstr(L, 12)}, mean {mp.nstr(1/L, 12)}")
pts = [(cos(pi/2*i/n), sin(pi/2*i/n)) for i in range(n + 1)]
dv = sum(b[1]-a[1] for a, b in zip(pts, pts[1:])); dh = sum(abs(b[0]-a[0]) for a, b in zip(pts, pts[1:]))
say('J1', abs(dv-1) < mpf(10)**-45 and abs(dh-1) < mpf(10)**-45, f"circle: sum dv {mp.nstr(dv, 15)}, sum |dh| {mp.nstr(dh, 15)}, length pi/2, mean 2/pi = {mp.nstr(2/pi, 12)}")

print("J2 corner to foot: the square's far edge, evenly")
for name, V in THINGS.items():
    dc = V / HL; d = S / dc; N = 1 / d
    xs = [1 - k * d for k in range(int(N) + 1)] + [F(0)]
    capped = [(x, F(1)) for x in xs]               # past the corner v = 1, h = x
    steps = {a[0] - b[0] for a, b in zip(capped[:-2], capped[1:-1])}
    last = capped[-2][0] - capped[-1][0]
    total = sum(a[0] - b[0] for a, b in zip(capped, capped[1:]))
    say('J2', steps == {d} and d * N == 1 and total == 1 and 0 <= last <= d,
        f"{name}: delta {d}, count {N}, delta x count {d*N}, whole steps all delta, part stride {last/d} of one, sum |dh| {total}")

print("J3 pointwise = summed over what is left")
random.seed(7)
for name, V in THINGS.items():
    dc = V / HL; d = S / dc; ok = True
    for _ in range(1000):
        x = F(random.randint(1, 10**9), random.randint(1, 10**7))   # places before and after the corner
        s = 1 / x; left = (x * dc) / S
        ok = ok and s * left * d == 1 and left * d == x
    say('J3', ok, f"{name}: s x strides-left x delta = 1 at 1,000 places (x from 1e-7 to 1e9)")

print("J4 far start to the corner: the near edge, uneven, short by 1/x0")
for name, V in THINGS.items():
    dc = V / HL; d = S / dc
    for x0 in (F(2), F(30), F(10**6)):
        m = int((x0 - 1) / d); m = min(m, 20000)            # count the first strides, then jump: the sum telescopes
        xs = [x0 - k * d for k in range(m + 1)]
        vs = [1 / x for x in xs]
        st = [b - a for a, b in zip(vs, vs[1:])]
        form = all(st[k] == d / (xs[k] * (xs[k] - d)) for k in range(len(st)))
        uneven = len(set(st)) == len(st)
        total = (1 / F(1)) - 1 / x0                          # ends: v = 1 at the corner, 1/x0 at the start
        partial = sum(st)
        say('J4', form and uneven and partial == vs[-1] - vs[0] and total == 1 - 1 / x0,
            f"{name}, x0 {x0}: first {m} steps uneven, each delta/(x(x-delta)); sum to the corner {total} = 1 - 1/x0")
print("   whole walk on the capped chart: near edge 1 (x0 -> infinity) + far edge 1 = length 2, dv 1 then -dh 1: 1/2 x 2")

print("J5 the walk's split is not the turn's")
for name, V in THINGS.items():
    dc = V / HL; d = mpf(S.numerator) / S.denominator / (mpf(dc.numerator) / dc.denominator)
    N = int(1 / d)
    xs = [1 - k * d for k in range(N + 1)]
    th = [atan(1 / x) if x > 0 else pi / 2 for x in xs]
    arcs = [b - a for a, b in zip(th, th[1:])]
    ratio = arcs[0] / arcs[-1]
    mh = sum(x / sqrt(1 + x * x) for x in xs) / len(xs)
    mv = sum(1 / sqrt(1 + x * x) for x in xs) / len(xs)
    okr = abs(ratio - mpf(1) / 2) < mpf('0.005') if name == 'mountain' else True
    ok = abs(mh - 2 / pi) > mpf(10)**-10 and abs(mv - 2 / pi) > mpf(10)**-10 and okr
    say('J5', ok, f"{name}: first arc / last arc {mp.nstr(ratio, 8)}; stride-weighted mean h {mp.nstr(mh, 10)}, mean v {mp.nstr(mv, 10)}; 2/pi {mp.nstr(2/pi, 10)}")
print(f"   limits: mean h -> sqrt2 - 1 = {mp.nstr(sqrt(2)-1, 12)}, mean v -> asinh 1 = {mp.nstr(asinh(1), 12)}")
print(f"   round chart corner to foot: dv = 1 - 1/sqrt2 = {mp.nstr(1-1/sqrt(2), 12)}, -dh = 1/sqrt2 = {mp.nstr(1/sqrt(2), 12)}, sum 1, arc pi/4")
for X in (10, 1000, 10**6):
    # stride-weighted mean of v from X corners out to the foot: (1/X) * asinh(X)
    print(f"   from {X} corners out to the foot: stride-weighted mean v = asinh(X)/X = {mp.nstr(asinh(X)/X, 8)}; times length X = {mp.nstr(asinh(X), 8)} (not 1: v is not the walk's coordinate)")

print("J6 the fixed share never closes the 1")
for r in (F(1, 10), F(1, 2)):
    x = F(1); tot = F(0); ok = True
    for m in range(1, 501):
        nx = x * (1 - r); tot += x - nx; x = nx
        ok = ok and tot < 1 and tot == 1 - (1 - r)**m
    say('J6', ok, f"share {r}: after 500 steps sum |dh| = 1 - (1-r)^500, short of 1 by {float((1-r)**500):.3e}; mean step {float(tot/500):.3e}")

print()
for k in sorted(res): print(k, 'not killed' if res[k] else 'KILLED')
