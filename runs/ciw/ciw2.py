"""CIW run 2: K1's arcs with the kernel's peak as a breakpoint (plans/ciw-plan.md, run 2 predictions)."""
import numpy as np, mpmath as mp
mp.mp.dps = 50
rng = np.random.default_rng(20261019 + 85)
def P(z, phi): return abs(1 - abs(z)**2) / abs(mp.expj(phi) - z)**2 / (2 * mp.pi)
worst = mp.mpf(0)
for i in range(10**3):
    z = mp.mpf(rng.uniform(0, 0.99)) * mp.expj(mp.mpf(rng.uniform(0, 2 * np.pi)))
    p1 = mp.mpf(rng.uniform(0, 2 * np.pi)); a = mp.mpf(rng.uniform(0.01, 2 * np.pi - 0.01)); p2 = p1 + a
    c = mp.arg(z)
    pts = [p1] + [c + 2 * mp.pi * j for j in range(-1, 3) if p1 < c + 2 * mp.pi * j < p2] + [p2]
    om = mp.quad(lambda p: P(z, p), pts)
    tz = mp.arg((mp.expj(p2) - z) / (mp.expj(p1) - z)) % (2 * mp.pi)
    worst = max(worst, abs(om - (tz / mp.pi - a / (2 * mp.pi))))
ok = worst < mp.mpf('1e-30')
print("K1' arcs omega = theta_z/pi - alpha/2pi to %s" % mp.nstr(worst, 3), ok)
print("K6'", ok)
