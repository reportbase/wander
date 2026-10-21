"""One figure, three rulers (OFS §6; SPN R422). Exact checks, mpmath at 50 digits.

The unit circle and the unit hyperbola u^2 - w^2 = 1 touch the same tangent line at the apex A = (1, 0). A reading
x = v/h sits on that line at T = (1, x). The circle's point P = (cos t, sin t) and the hyperbola's point
H = (cosh z, sinh z) beside T give x = tan t = sinh z, so t = gd(z). Three rulers of one reading:
  x itself (the writer's number line), t = arctan x (the turn), z = asinh x (the hyperbolic angle, Mercator's height).
Run 1 (rulers-run1.out) failed one check by my set-up: an absolute 1e-45 on tan t - sinh z at x = 1000, where the
error is 1e-48 relative. Run 2 checks it relative to x.
Run from the repository's root: python3 runs/ofs/rulers.py
"""
from mpmath import mp, mpf, atan, asinh, sinh, tan, cosh, sin, cos, log, pi, quad, findroot, diff
mp.dps = 50
ok = True
def check(name, err, tol):
    global ok
    good = abs(err) < tol
    ok &= good
    print(f"{'pass' if good else 'FAIL'}  {name}: {mp.nstr(err, 5)}")

xs = [mpf(1)/1000, mpf(1)/3, mpf(1), mpf(3), mpf(1000)]
gd = lambda z: atan(sinh(z))

# 1. One reading, three rulers: tan t = sinh z = x, t = gd(z); each angle twice its sector's area.
for x in xs:
    t, z = atan(x), asinh(x)
    check(f"x = {mp.nstr(x,4)}: (tan t - sinh z)/x", (tan(t) - sinh(z))/x, mpf(10)**-45)
    check(f"x = {mp.nstr(x,4)}: t - gd(z)", t - gd(z), mpf(10)**-45)
    # circle sector O-A-P: area t/2; hyperbola sector O-A-H: triangle O-(cosh z,0)-H minus the area under the curve
    hyp = cosh(z)*sinh(z)/2 - quad(lambda u: (u*u - 1)**0.5, [1, cosh(z)])
    check(f"x = {mp.nstr(x,4)}: 2*hyperbolic sector - z", 2*hyp - z, mpf(10)**-30)

# 2. The corner x = 1 is on every ruler: t = pi/4, z = asinh 1.
check("corner on the turn: atan 1 - pi/4", atan(1) - pi/4, mpf(10)**-45)
print("      corner on the hyperbola: asinh 1 =", mp.nstr(asinh(1), 12))

# 3. The reciprocal x -> 1/x is t -> pi/2 - t on the turn; on z it is not a reflection (no z0 with z -> 2 z0 - z).
for x in xs:
    check(f"reciprocal on the turn at x = {mp.nstr(x,4)}", atan(1/x) - (pi/2 - atan(x)), mpf(10)**-45)
z0 = asinh(1)
for x in [mpf(1)/3, mpf(3)]:
    print(f"      on z at x = {mp.nstr(x,4)}: asinh(1/x) = {mp.nstr(asinh(1/x),10)}, 2 asinh 1 - asinh x = {mp.nstr(2*z0-asinh(x),10)}")

# 4. z is the reader's lay (x to the corner, then 1 + ln x) made smooth: the gap is never more than 1 - ln 2,
#    approached far out; at the corner it is 1 - asinh 1.
lay = lambda x: x if x <= 1 else 1 + log(x)
gaps = [lay(x) - asinh(x) for x in [mpf(10)**k for k in range(-6, 13)]]
check("gap at the corner - (1 - asinh 1)", lay(mpf(1)) - asinh(1) - (1 - asinh(1)), mpf(10)**-45)
check("gap at x = 1e12 - (1 - ln 2)", gaps[-1] - (1 - log(2)), mpf(10)**-20)
check("every gap within [0, 1 - ln 2] (worst excess)", max(max(g - (1 - log(2)) for g in gaps), max(-g for g in gaps), 0), mpf(10)**-45)
print("      gap 1 - asinh 1 =", mp.nstr(1 - asinh(1), 10), "; 1 - ln 2 =", mp.nstr(1 - log(2), 10))

# 5. Only the turn's uniform measure has its median at the corner by itself. Uniform t on [0, pi/2]: median x = 1.
#    Uniform z on [0, Z]: median x = sinh(Z/2), the corner only at Z = 2 asinh 1. Uniform x on [0, X]: median X/2,
#    the corner only at X = 2.
check("uniform turn: median x - 1", tan(pi/4) - 1, mpf(10)**-45)
for Z in [mpf(1), 2*asinh(1), mpf(4), mpf(10)]:
    med = findroot(lambda m: asinh(m)/Z - mpf(1)/2, sinh(Z/2))
    check(f"uniform z on [0, {mp.nstr(Z,6)}]: median - sinh(Z/2)", med - sinh(Z/2), mpf(10)**-40)
    print(f"      median x = {mp.nstr(sinh(Z/2), 8)}")
print("      Z for the corner: 2 asinh 1 =", mp.nstr(2*asinh(1), 10))

# 6. The rulers' rates against each other: dt/dx = 1/(1 + x^2), dz/dx = 1/sqrt(1 + x^2), dt/dz = sech z = cos t.
for x in xs:
    t, z = atan(x), asinh(x)
    check(f"dt/dz - cos t at x = {mp.nstr(x,4)}", diff(gd, z) - cos(t), mpf(10)**-30)

# 7. Room for the near field (x <= 1) and the far field (x >= 1) on each ruler. The turn: pi/4 each. The hyperbolic
#    angle: asinh 1 near, unbounded far, the room per doubling asinh(2x) - asinh(x) tending to ln 2. The writer's line:
#    1 near, unbounded far.
check("turn: near room - pi/4", atan(1) - atan(0) - pi/4, mpf(10)**-45)
check("turn: far room - pi/4 (to the horizon)", pi/2 - atan(1) - pi/4, mpf(10)**-45)
for x in [mpf(1), mpf(2), mpf(4), mpf(8), mpf(16)]:
    print(f"      zeta room for the doubling {mp.nstr(x,3)} to {mp.nstr(2*x,3)}: {mp.nstr(asinh(2*x) - asinh(x), 6)}")
check("zeta room per doubling at x = 1e12 - ln 2", asinh(2*mpf(10)**12) - asinh(mpf(10)**12) - log(2), mpf(10)**-20)

print("ALL PASS" if ok else "SOME FAILED")
