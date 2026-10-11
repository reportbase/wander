"""OMM stage 1, run 1 (10 Oct 2026): the share one reading holds, tried both ways (Tom: "lets not rule, but try it both
ways, see what falls out"). Exact arithmetic with sympy; no data.

The bar of length 1 sweeps from all of h (flat) to all of v (upright). Its share on h is h, on v is v.
Weight A, the turn: the bar stepped evenly in its turn, home to the far wall.
Weight B, the in-place lay: the reading stepped evenly on each side of the corner, t = v/h from 0 to 1 up to the corner,
          then t = h/v from 1 back to 0, each side half the weight (SPN's fold, the lay's near half).
psi2: one facing of the reader's two (1/2), or one quarter of the full turn's four (1/4).
"""
import sympy as sp
th, t = sp.symbols('theta t', nonnegative=True)
# weight A: h = cos(theta), theta even on [0, pi/2]
A = sp.simplify(sp.integrate(sp.cos(th), (th, 0, sp.pi/2)) / (sp.pi/2))
# weight B: near side h = 1/sqrt(1+t^2), far side h = t/sqrt(1+t^2), t even on [0,1], halves equal
near = sp.integrate(1/sp.sqrt(1+t**2), (t, 0, 1)); far = sp.integrate(t/sp.sqrt(1+t**2), (t, 0, 1))
B = sp.simplify((near + far) / 2)
print("psi1 by weight A (the turn):          ", A, "=", sp.N(A, 10))
print("psi1 by weight B (the in-place lay):  ", B, "=", sp.N(B, 10))
print("  near side mean h:", sp.simplify(near), "=", sp.N(near, 10), "  far side:", sp.simplify(far), "=", sp.N(far, 10))
for name, p1 in (("A", A), ("B", B)):
    for f2, p2 in (("one facing of two", sp.Rational(1, 2)), ("one quarter of four", sp.Rational(1, 4))):
        prod = sp.simplify(p1 * p2)
        print(f"  {name} x {f2:20s}: {prod} = {sp.N(prod, 10)}")
print("1/pi =", sp.N(1/sp.pi, 10))
