# ORD: is a map between reads an order? Exact rationals. Run: python3 runs/ord/ord.py
from fractions import Fraction as F
from itertools import combinations

ok = True
def check(name, cond):
    global ok; ok &= bool(cond); print(("  ok   " if cond else "  FAIL ") + name)

# Moebius maps on the slope chart as integer/rational 2x2 matrices, s -> (a s + b)/(c s + d)
def mul(g, h): (a, b), (c, d) = g; (e, f), (p, q) = h; return ((a*e + b*p, a*f + b*q), (c*e + d*p, c*f + d*q))
def same(g, h):  # equal as maps: proportional matrices
    (a, b), (c, d) = g; (e, f), (p, q) = h
    return a*f == b*e and a*p == c*e and a*q == d*e and b*p == c*f and b*q == d*f and c*q == d*p
def ap(g, s): (a, b), (c, d) = g; return (a*s + b)/(c*s + d)
I = ((F(1), F(0)), (F(0), F(1)))
def turn(t): t = F(t); return ((F(1), t), (-t, F(1)))       # tangent addition by slope t
def boost(k): k = F(k); return ((k, F(0)), (F(0), F(1)))
EXCH = ((F(0), F(1)), (F(1), F(0)))                          # s -> 1/s
def xr(a, b, c, d): return (a - c)*(b - d)/((a - d)*(b - c))
S = [F(1, 5), F(1, 2), F(2, 3), F(3, 2), F(4), F(7)]         # test slopes, increasing

print("N1 a turn is not an order")
t = turn(1); p = I
for n in range(1, 5):
    p = mul(t, p)
    if n < 4: check(f"turn by slope 1, {n} times: not the identity", not same(p, I))
check("four times: the identity (a cycle)", same(p, I))
t34 = turn(F(3, 4)); p = I; cyc = False
for n in range(1, 200):
    p = mul(t34, p); cyc |= same(p, I)
check("turn by slope 3/4: no return in 199 steps (reported, not predicted)", not cyc)

print("N2 a boost is not an order")
for k in (F(2), F(7, 5)):
    check(f"boost {k} then 1/{k}: the identity (a cycle of two)", same(mul(boost(1/k), boost(k)), I))

print("N3 a coordinate may be ordered without the map being an order")
check("boosts on one axis commute", same(mul(boost(2), boost(3)), mul(boost(3), boost(2))))
check("and are ordered by k: 2 < 3 < 6 = 2*3", F(2) < F(3) < F(6) and same(mul(boost(2), boost(3)), boost(6)))
check("turns of the plane commute", same(mul(turn(1), turn(F(1, 2))), mul(turn(F(1, 2)), turn(1))))

print("N4 keeping order does not single out maps between reads")
cube = lambda s: s**3
inc = lambda f: all(f(a) < f(b) for a, b in zip(S, S[1:]))
dec = lambda f: all(f(a) > f(b) for a, b in zip(S, S[1:]))
keeps_xr = lambda f: all(xr(*q) == xr(*map(f, q)) for q in combinations(S, 4))
check("s^3 keeps the order of the slopes", inc(cube))
check("s^3 moves a cross ratio", not keeps_xr(cube))
check("boost 3 keeps order and every cross ratio", inc(lambda s: ap(boost(3), s)) and keeps_xr(lambda s: ap(boost(3), s)))
tt = turn(F(1, 10))
check("turn by slope 1/10 keeps every cross ratio", keeps_xr(lambda s: ap(tt, s)))
vals = [ap(tt, s) for s in S]
check("  and the order of these slopes on the chart is broken where one passes the horizon",
      not all(a < b for a, b in zip(vals, vals[1:])))
check("the exchange keeps every cross ratio and reverses the order", keeps_xr(lambda s: ap(EXCH, s)) and dec(lambda s: ap(EXCH, s)))

print("N5 an order and a map are two variables")
def mm(A, B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def tr(A): return tuple(tuple(A[j][i] for j in range(3)) for i in range(3))
X = ((1, 0, 0), (0, 0, -1), (0, 1, 0)); Y = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))
XY, YX = mm(X, Y), mm(Y, X)
check("quarter turns about two thumbs: the two orders give two composites", XY != YX)
R = mm(XY, tr(YX))
check("the turn between them has trace 0: 120 degrees", sum(R[i][i] for i in range(3)) == 0)
check("in the plane the two orders give one composite", same(mul(turn(1), turn(2)), mul(turn(2), turn(1))))

print("N6 a general map does not count merely by being a function on directions")
maps = {
    "turn by slope 1/10": (lambda s: ap(tt, s), True),
    "boost 3": (lambda s: ap(boost(3), s), True),
    "boost then turn": (lambda s: ap(mul(tt, boost(3)), s), True),
    "exchange 1/s": (lambda s: ap(EXCH, s), True),
    "s + 1": (lambda s: s + 1, True),
    "2s/(1+s)": (lambda s: 2*s/(1 + s), True),
    "s^3": (cube, False),
    "s^2": (lambda s: s*s, False),
    "s/(1+s^2)": (lambda s: s/(1 + s*s), False),
}
for name, (f, moebius) in maps.items():
    check(f"{name}: keeps every cross ratio = {moebius}", keeps_xr(f) == moebius)

print("all exact" if ok else "SOMETHING FAILED")
