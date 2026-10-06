"""Checks behind plans/standpoint-axis.md: a ball of radius a seen from outside, at contact, and from inside.

    python3 plans/standpoint/checks.py
"""
import math

import numpy as np

a = 1.0
rng = np.random.default_rng(1)

print('1. Seen from outside, at distance d: the visible cap, its limb, and the inverse point d\' = a²/d.')
print(f'   {"d/a":>6} {"cap half-angle":>15} {"limb plane at":>14} {"a²/d":>8} {"share of the sphere seen":>25} {"sight cone half-angle":>22}')
for d in (1.0001, 1.1, 1.5, 2.0, 4.0, 10.0, 1e6):
    cap = math.degrees(math.acos(a / d))          # at the centre, from the direction of the observer to the limb
    plane = a * a / d                             # the limb circle lies in the plane x = a·cos(cap) = a²/d
    seen = (1 - a / d) / 2                        # area of the cap over the sphere's
    cone = math.degrees(math.asin(a / d))         # the half-angle the ball subtends at the observer
    print(f'   {d:6g} {cap:14.2f}° {a * math.cos(math.radians(cap)):14.4f} {plane:8.4f} {seen:25.4f} {cone:21.2f}°')
print('   the limb\'s plane passes through the observer\'s inverse point (pole and polar); far away the cap is a')
print('   hemisphere (90°, half the sphere), at contact nothing: "hemisphere" is the far limit of holding a thing.')

print('\n2. Brute force: from P = (d, 0, 0), which points of the sphere are visible (the segment to P leaves the ball)?')
pts = rng.normal(size=(200000, 3))
pts /= np.linalg.norm(pts, axis=1)[:, None]
for d in (1.5, 4.0):
    P = np.array([d, 0, 0])
    vis = (pts @ (P - 0)) - a * a > 0              # visible iff the outward normal faces P: n·(P − x) > 0, |x| = a
    print(f'   d = {d}: visible share {vis.mean():.4f} (formula {(1 - a / d) / 2:.4f}); every visible point has x ≥ a²/d: '
          f'{bool(np.all(pts[vis, 0] >= a * a / d - 1e-12))}')

print('\n3. Across the visible cap, the angle between the line of sight and the surface normal runs 0° to 90°:')
for d in (1.5, 4.0, 1e6):
    phis = np.linspace(0, math.acos(a / d), 7)                          # from the cap's centre to its limb
    x = np.stack([a * np.cos(phis), a * np.sin(phis), 0 * phis], 1)
    to_p = np.array([d, 0, 0]) - x
    inc = np.degrees(np.arccos(np.sum(x / a * to_p, 1) / np.linalg.norm(to_p, axis=1)))
    print(f'   d = {d:g}: incidence from centre to limb {np.round(inc, 1).tolist()} (a quarter turn whatever d)')

print('\n4. Inversion in the sphere, x -> a² x/|x|², swaps outside and inside and fixes the surface:')
for d in (0.25, 0.5, 1.0, 2.0, 4.0):
    print(f'   |x| = {d:<5g} -> {a * a / d:g}' + ('   (the surface: fixed; the corner, contact)' if d == 1.0 else ''))
print('   from inside, every direction meets the ball: the share of the view it fills is 1 (BAL: full at contact and past it).')
