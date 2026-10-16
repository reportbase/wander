"""TWS, post hoc: on the stretched drawing (the ellipse x² − x + y²/c² = 0, c = 2) neither the end A = (0, 0) nor the
middle M = (½, 0) turns equal steps of a ray into equal steps of arc. Exact, mpmath.
Run: python3 tws/ellipse.py
"""
from mpmath import mp, mpf, sqrt, cos, sin, pi, quad, diff
mp.dps = 30
c = mpf(2)
def point_from_A(t):                    # A's ray at angle t meets the ellipse at (1, c²tan t ...) solved exactly
    k = sin(t) / cos(t)                 # y = kx; x² − x + k²x²/c² = 0 → x = 1/(1 + k²/c²)
    x = 1 / (1 + k * k / (c * c)); return x, k * x
def point_from_M(t):                    # (½ + r cos t)² − (½ + r cos t) + (r sin t)²/c² = 0 → r² (cos² t + sin² t/c²) = ¼
    r = mpf(1) / 2 / sqrt(cos(t)**2 + sin(t)**2 / c**2); return mpf(1) / 2 + r * cos(t), r * sin(t)
def speed(f, t):                        # arc length per unit of turn
    dx = diff(lambda u: f(u)[0], t); dy = diff(lambda u: f(u)[1], t); return sqrt(dx * dx + dy * dy)
for name, f, lo, hi in (('from A', point_from_A, mpf('0.05'), pi / 2 - mpf('0.05')), ('from M', point_from_M, mpf('0.05'), pi - mpf('0.05'))):
    sp = [speed(f, lo + (hi - lo) * k / 20) for k in range(21)]
    print(f"{name}: arc per turn from {mp.nstr(min(sp), 8)} to {mp.nstr(max(sp), 8)} (ratio {mp.nstr(max(sp) / min(sp), 6)})")
c = mpf(1)                              # the circle, for comparison
for name, f, lo, hi in (('circle from A', point_from_A, mpf('0.05'), pi / 2 - mpf('0.05')), ('circle from M', point_from_M, mpf('0.05'), pi - mpf('0.05'))):
    sp = [speed(f, lo + (hi - lo) * k / 20) for k in range(21)]
    print(f"{name}: arc per turn from {mp.nstr(min(sp), 12)} to {mp.nstr(max(sp), 12)}")
