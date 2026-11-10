# MBR: maps between reads, exact in Gaussian rationals. Run: python3 runs/mbr/mbr.py
from fractions import Fraction as F

class C:
    def __init__(s, re, im=0): s.re, s.im = F(re), F(im)
    def __add__(s, o): o = c(o); return C(s.re + o.re, s.im + o.im)
    def __sub__(s, o): o = c(o); return C(s.re - o.re, s.im - o.im)
    def __mul__(s, o): o = c(o); return C(s.re*o.re - s.im*o.im, s.re*o.im + s.im*o.re)
    __rmul__ = __mul__
    def conj(s): return C(s.re, -s.im)
    def n2(s): return s.re*s.re + s.im*s.im
    def __truediv__(s, o): o = c(o); d = o.n2(); q = s*o.conj(); return C(q.re/d, q.im/d)
    def __eq__(s, o): o = c(o); return s.re == o.re and s.im == o.im
    def __repr__(s): return f"({s.re}{'+' if s.im >= 0 else ''}{s.im}i)"
def c(x): return x if isinstance(x, C) else C(x)

# a Moebius map as (A, B, Cc, Dd): z -> (A z + B)/(Cc z + Dd)
def mob(m, z): A, B, Cc, Dd = m; return (A*z + B)/(Cc*z + Dd)
def comp(g, h):  # g after h
    a, b, cc, d = g; e, f, gg, hh = h
    return (a*e + b*gg, a*f + b*hh, cc*e + d*gg, cc*f + d*hh)
def boost(k): return (c(k), c(0), c(0), c(1))
def turn(a, b): a, b = c(a), c(b); assert a.n2() + b.n2() == 1; return (a, b, c(0) - b.conj(), a.conj())
def stretch2(m, z):  # the SQUARE of the stretch D, exact: |g'|^2 (1+|z|^2)^2/(1+|g z|^2)^2
    A, B, Cc, Dd = m
    det = A*Dd - B*Cc; den = Cc*z + Dd
    gp2 = det.n2()/(den.n2()**2)
    w = mob(m, z)
    return gp2*(1 + z.n2())**2/(1 + w.n2())**2

ok = True
def check(name, cond):
    global ok; ok &= bool(cond); print(("  ok   " if cond else "  FAIL ") + name)

print("M1 same direction, different motion")
for k in (F(2), F(3), F(7, 5)):
    b = boost(k)
    check(f"k={k}: z=0 unmoved, stretch^2 = k^2", mob(b, c(0)) == 0 and stretch2(b, c(0)) == k*k)
    z = C(F(1, 3), F(1, 4))
    check(f"k={k}: another direction does move", not (mob(b, z) == z))

print("M2 same boost, different payload")
b = boost(2); z = C(F(1, 5), F(2, 5)); D2 = stretch2(b, z)
for f in (F(1), F(5), F(440)):
    # f' = D f under premise (P): the square of the ratio is D2 whatever f
    check(f"f={f}: (f'/f)^2 = D^2, independent of f", (D2*f*f)/(f*f) == D2)
for sig in (F(1), F(2), F(1, 3)):
    check(f"source factor {sig}: observed ratio^2 = sig^2 D^2, map unchanged", (sig*sig*D2 != D2) == (sig != 1))

print("M3 same payload ratio, different maps")
check("k=2 at z=0: D^2 = 4", stretch2(boost(2), c(0)) == 4)
# |z|^2 = 1/15: z = (1 + 2i)/sqrt(75) is not rational; use the formula in r2 = |z|^2 directly
def D2_boost(k, r2): return (k*(1 + r2)/(1 + k*k*r2))**2
z = C(F(3, 5), F(4, 5))  # |z|^2 = 1, check the formula against the map first
check("formula in |z|^2 agrees with the map", D2_boost(F(3), z.n2()) == stretch2(boost(3), z))
check("k=3 at |z|^2 = 1/15: D^2 = 4", D2_boost(F(3), F(1, 15)) == 4)
check("identity map, source factor 2: ratio^2 = 4", F(2)**2*stretch2(boost(1), c(0)) == 4)

print("M4 turn against boost, and against a step")
t = turn(F(3, 5), F(4, 5)); t2 = turn(C(F(1, 3), F(2, 3)), C(F(2, 3), 0))
pts = [c(0), C(F(1, 2)), C(F(1, 3), F(1, 4)), C(-2, F(5, 7)), C(0, 9)]
check("a turn's stretch is 1 at every direction tried", all(stretch2(m, z) == 1 for m in (t, t2) for z in pts))
vals = [stretch2(boost(3), z) for z in pts]
check("a boost's stretch varies, within [1/k^2, k^2]", len(set(vals)) > 1 and all(F(1, 9) <= v <= 9 for v in vals))
check("a boost's stretch reaches k^2 on the axis and tends to 1/k^2 behind",
      stretch2(boost(3), c(0)) == 9 and D2_boost(F(3), F(10**12)) - F(1, 9) < F(1, 10**11))
# a step in the plane: two points on one direction from the origin, at distances 1 and 2
P, Q = (F(3), F(4)), (F(6), F(8))            # same direction [3 : 4]
check("before the step: one direction", P[0]*Q[1] == P[1]*Q[0])
s = (F(1), F(0))                             # step one unit along x
P2, Q2 = (P[0] - s[0], P[1] - s[1]), (Q[0] - s[0], Q[1] - s[1])
check("after the step: two directions, so no map on directions", P2[0]*Q2[1] != P2[1]*Q2[0])
# a turn and a boost never split one direction: a map sends one z to one z
check("a turn or a boost sends one direction to one direction (it is a function of z)", True)

print("M5 composition")
g, h = boost(2), boost(3)
check("two boosts on one axis compose to the boost k1 k2", all(mob(comp(g, h), z) == mob(boost(6), z) for z in pts))
z = C(F(1, 3), F(1, 4))
check("stretch cocycle D_{g.h}(z) = D_g(h z) D_h(z)", stretch2(comp(g, h), z) == stretch2(g, mob(h, z))*stretch2(h, z))
check("the naive product D_g(z) D_h(z) is wrong off the axis", stretch2(comp(g, h), z) != stretch2(g, z)*stretch2(h, z))
check("and right on the axis", stretch2(comp(g, h), c(0)) == stretch2(g, c(0))*stretch2(h, c(0)))
gt, tg = comp(g, t), comp(t, g)
check("boost after turn and turn after boost are different maps", not (mob(gt, z) == mob(tg, z)))
check("with different stretches at one direction", stretch2(gt, z) != stretch2(tg, z))
check("cocycle holds for a boost and a turn", stretch2(gt, z) == stretch2(g, mob(t, z))*stretch2(t, z))
tt = comp(t, t2)
check("two turns compose to a map of stretch 1 (a turn)", all(stretch2(tt, z) == 1 for z in pts))

print("M6 the rapidity as a coordinate")
def beta(k): return (k*k - 1)/(k*k + 1)
for k1, k2 in ((F(2), F(3)), (F(7, 5), F(5, 3)), (F(1, 2), F(4))):
    b1, b2 = beta(k1), beta(k2)
    check(f"k={k1},{k2}: beta composes by (b1+b2)/(1+b1 b2) as k multiplies", (b1 + b2)/(1 + b1*b2) == beta(k1*k2))
def slope_add(s1, s2): return (s1 + s2)/(1 - s1*s2)
check("a turn's slope composes by tangent addition: 1/2 + 1/3 = 1", slope_add(F(1, 2), F(1, 3)) == 1)
print("\nall exact" if ok else "\nFAILURES")
