"""The lighthouse and Mercator's map: the numbers in observation-from-somewhere.md, Proposition 5(f) and (g).

Each value is measured from the construction (an even half turn of flashes cast on a straight shore; a course of
constant bearing integrated over the globe and drawn on each chart) and compared with the closed form the paper states.
Unit relations h, v in [0, 1]; on the globe v = sin(latitude), h = cos(latitude). The lamp's distance beta and the
shore's point alpha are amounts used only to draw the picture; every stated result is a ratio.
Run: python3 runs/ofs/charts.py   (mpmath, 30 digits; a few seconds)
"""
from mpmath import mp, mpf, pi, tan, atan, cos, sin, sec, asinh, log, quad, odefun, degrees, diff

mp.dps = 30
ok = True
def check(name, got, want, tol=mpf(10) ** -20):
    global ok
    good = abs(got - want) <= tol
    ok &= good
    print(f"{'ok ' if good else 'BAD'} {name}: {mp.nstr(got, 12)} (stated {mp.nstr(want, 12)})")

# (f) the lighthouse. Flashes at theta even on (-pi/2, pi/2); a flash lands at x = alpha + beta tan(theta).
alpha, beta = mpf(3), mpf(2)
share = lambda pred: quad(lambda t: 1 if pred(t) else 0, [-pi / 2, -pi / 4, 0, pi / 4, pi / 2]) / pi
for c in (mpf(1), mpf(2), mpf('0.5')):
    # drawn with the shore at c times the sea: the drawn reading is c (x - alpha)/beta
    within = lambda r: quad(lambda t: 1, [-atan(r / c), atan(r / c)]) / pi       # P(|drawn reading| <= r), by measure
    check(f"c = {mp.nstr(c, 2)}: landings within one drawn lamp-distance", within(1), 2 * atan(1 / c) / pi)
    check(f"c = {mp.nstr(c, 2)}: median of |drawn reading|", within(c), mpf(1) / 2)
    check(f"c = {mp.nstr(c, 2)}: the 45-degree flash drawn at (degrees)", degrees(atan(c * tan(pi / 4))), degrees(atan(c)))
    flip = max(abs(within(r) - (1 - within(1 / r))) for r in (mpf('0.3'), mpf(3)))
    print(f"    flip defect (law of r against law of 1/r): {mp.nstr(flip, 6)}{'  (none only at c = 1)' if c == 1 else ''}")
x = lambda t: alpha + beta * tan(t)
for t in (mpf('0.3'), mpf('1.2')):
    path = beta / cos(t)
    check(f"theta {t}: the path cancels from the legs' ratio", (path * sin(t)) / (path * cos(t)), (x(t) - alpha) / beta)
H = mpf(5)                                                                         # any H in place of beta
check("drawn at H: a similar figure, angle of the 45-degree flash", degrees(atan((H * tan(pi / 4)) / H)), mpf(45))

# (g) Mercator's map. A chart x = longitude, y = f(latitude); scales sec(phi) east, f'(phi) north; c = f'(phi) cos(phi).
charts = {'plate carree': (lambda p: p, lambda p: cos(p)),
          "Lambert's equal-area": (lambda p: sin(p), lambda p: cos(p) ** 2),
          'central cylindrical': (lambda p: tan(p), lambda p: sec(p)),
          "Mercator's": (lambda p: asinh(tan(p)), lambda p: mpf(1))}
psi = pi / 4                                                                      # the course northeast
lam = odefun(lambda p, l: tan(psi) / cos(p), 0, 0)                                 # cos(phi) dlambda = tan(psi) dphi
p60, d = pi / 3, mpf(10) ** -8
for name, (f, cform) in charts.items():
    c = diff(f, p60) * cos(p60)
    check(f"{name}: c at 60 degrees", c, cform(p60))
    dx = lam(p60 + d) - lam(p60 - d); dy = f(p60 + d) - f(p60 - d)
    drawn = degrees(atan(dx / dy))
    check(f"{name}: the course northeast drawn at 60 degrees (bearing, degrees)", drawn, degrees(atan(tan(psi) / c)),
          tol=mpf(10) ** -6)
    axes = (diff(f, p60), sec(p60))                                                 # a small circle drawn: north and east axes
    print(f"    indicatrix at 60 degrees: north {mp.nstr(axes[0], 6)}, east {mp.nstr(axes[1], 6)}, area {mp.nstr(axes[0] * axes[1], 6)}")
check("Mercator's height is the integral of sec", quad(sec, [0, p60]), asinh(tan(p60)))
check("and ln tan(pi/4 + phi/2)", log(tan(pi / 4 + p60 / 2)), asinh(tan(p60)))
check("an equal-area chart has c = cos^2: k_E k_N = 1 at 60 degrees", sec(p60) * (cos(p60) ** 2 / cos(p60)), mpf(1))
print('all match' if ok else 'MISMATCH')
