"""HZN (plans/hzn-plan.md): standing on the outline is standing on a planet. Ratios of the radius only."""
import math
out = []
# P1: the chord 2 sin(phi) toward the tangent; log-log slope over phi in [2^-20, 2^-10]
a, b = 2.0 ** -20, 2.0 ** -10
slope1 = (math.log(2 * math.sin(b)) - math.log(2 * math.sin(a))) / (math.log(b) - math.log(a))
out.append(('P1', abs(slope1 - 1) < 1e-6, f'log-log slope of the chord against phi, phi in [2^-20, 2^-10]: {slope1:.9f}'))
# P2: geometric mean of chords over (0, pi) at 10^6 directions (midpoints); the corner's angle
N = 10 ** 6
gm2 = math.exp(sum(math.log(2 * math.sin((i + 0.5) * math.pi / N)) for i in range(N)) / N)
corner = math.degrees(math.asin(gm2 / 2))
deepest = math.log2(2 / gm2)
out.append(('P2', abs(gm2 - 1) < 1e-6 and abs(corner - 30) < 0.01,
            f'geometric mean of the chords {gm2:.9f} of the radius; the corner at {corner:.5f} deg from the tangent; the diameter {deepest:.6f} levels past it'))
# P3: on a ball, weighted by solid angle cos(phi) dphi over (0, pi/2)
M = 10 ** 6; num = den = 0.0
for i in range(M):
    p = (i + 0.5) * (math.pi / 2) / M; w = math.cos(p); num += w * math.log(2 * math.sin(p)); den += w
gm3 = math.exp(num / den)
out.append(('P3', abs(gm3 - 2 / math.e) < 1e-6, f'geometric mean on the ball {gm3:.9f} of the radius; 2/e = {2 / math.e:.9f}; its depression {math.degrees(math.asin(gm3 / 2)):.4f} deg'))
# P4: rising: t(e) = sqrt(2e + e^2), against sqrt(2e)
es = [2.0 ** -k for k in range(1, 31)]
worst = max(abs(math.sqrt(2 * e + e * e) / math.sqrt(2 * e) - 1) - e for e in es)
lo, hi = 2.0 ** -30, 2.0 ** -20
t = lambda e: math.sqrt(2 * e + e * e)
slope4 = (math.log(t(hi)) - math.log(t(lo))) / (math.log(hi) - math.log(lo))
out.append(('P4', worst <= 0 and abs(slope4 - 0.5) < 1e-6,
            f'max of |t/sqrt(2e) - 1| - e over e = 2^-1 .. 2^-30: {worst:.3e} (<= 0 holds); log-log slope over [2^-30, 2^-20]: {slope4:.9f}'))
for name, held, line in out: print(f'{name}: {"not killed" if held else "KILLED"}. {line}')
