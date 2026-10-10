"""ISQ (plans/isq-plan.md): is the in-place lay the inverse square?
Three lays, corner at radius 1, horizon at 2: W (wander, 2 - 1/s), D (draw, linear within each level),
T (the sweep, 4/pi * atan(s), a control). Plain Python, exact where it can be (fractions for the walls)."""
import math
from fractions import Fraction as F

def W(s): return s if s <= 1 else 2 - 1 / s
def dW(s): return 1.0 if s < 1 else s ** -2
def D(s):
    if s <= 1: return s
    k = math.floor(math.log2(s)); lo = 2.0 ** k; a = 2 - 2.0 ** -k; b = 2 - 2.0 ** -(k + 1)
    return a + (b - a) * (s - lo) / lo
def dD(s):
    if s < 1: return 1.0
    k = math.floor(math.log2(s)); return 2.0 ** -(k + 1) / 2.0 ** k
def T(s): return 4 / math.pi * math.atan(s)
def dT(s): return 4 / math.pi / (1 + s * s)

out = []
# P1: W' = s^-2 at 2,000 points on (1, 2^30]; each level's room 2^-(k+1), exactly
pts = [2 ** (30 * (i + 1) / 2000) for i in range(2000)]
p1 = max(abs(dW(s) * s * s - 1) for s in pts)
# the derivative measured, not assumed: a central difference on W itself
p1n = max(abs((W(s * (1 + 1e-6)) - W(s * (1 - 1e-6))) / (2e-6 * s) * s * s - 1) for s in pts[:-1])
rooms = [F(2) - F(1, 2 ** (k + 1)) - (F(2) - F(1, 2 ** k)) for k in range(30)]
p1rooms = all(rooms[k] == F(1, 2 ** (k + 1)) for k in range(30))
per_unit = [rooms[k] / F(2 ** k) for k in range(30)]          # room per unit s, averaged over level k
p1quarter = all(per_unit[k + 1] / per_unit[k] == F(1, 4) for k in range(29))
out.append(('P1', p1 < 1e-12 and p1rooms and p1quarter,
            f'max |s^2 W\'(s) - 1| = {p1:.1e} (as written), {p1n:.1e} (central difference on W); level rooms 2^-(k+1) exactly: {p1rooms}; '
            f'room per unit s over level k = 1/2 * 4^-k, quartering per doubling exactly: {p1quarter}'))
# P2: in u = 1/s, W = 2 - u on (0, 1]
us = [(i + 1) / 2000 for i in range(2000)]
p2 = max(abs(W(1 / u) + u - 2) for u in us)
out.append(('P2', p2 < 1e-12, f'max |W(1/u) + u - 2| = {p2:.1e} on u in (0, 1]: the far field is proportion in h/v, room 1 per unit u'))
# P3: D, s^2 D' within [1/2, 2], exactly 1 at geometric middles
inside = [2 ** (25 * (i + 0.5) / 5000) for i in range(5000)]
r = [s * s * dD(s) for s in inside if s > 1]
mids = [abs((2 ** (k + 0.5)) ** 2 * dD(2 ** (k + 0.5)) - 1) for k in range(25)]
# D agrees with W at every wall
walls = max(abs(D(2.0 ** k) - W(2.0 ** k)) for k in range(30))
out.append(('P3', min(r) >= 0.5 - 1e-12 and max(r) <= 2 + 1e-12 and max(mids) < 1e-12,
            f's^2 D\'(s) from {min(r):.4f} to {max(r):.4f}; at the geometric middles misses 1 by at most {max(mids):.1e}; D - W at the walls {walls:.1e}'))
# P4: least-squares log-log slope of rho' against s over [2, 2^20], 400 log-spaced points
xs = [2 ** (1 + 19 * i / 399) for i in range(400)]
def slope(d):
    X = [math.log(s) for s in xs]; Y = [math.log(d(s)) for s in xs]; mx = sum(X) / len(X); my = sum(Y) / len(Y)
    return sum((a - mx) * (b - my) for a, b in zip(X, Y)) / sum((a - mx) ** 2 for a in X)
sW, sD, sT = slope(dW), slope(dD), slope(dT)
out.append(('P4', abs(sW + 2) < 0.005 and abs(sD + 2) < 0.02 and abs(sT + 2) < 0.02,
            f'slopes: W {sW:.4f}, D {sD:.4f}, T (the sweep) {sT:.4f}'))
# P5: the near field, room 1 per unit s
near = [i / 1000 for i in range(1, 1000)]
p5 = max(max(abs(dW(s) - 1), abs(dD(s) - 1)) for s in near)
p5n = max(abs((W(s + 1e-7) - W(s - 1e-7)) / 2e-7 - 1) for s in near[1:-1])
out.append(('P5', p5 < 1e-12 and p5n < 1e-6, f'max |rho\'(s) - 1| below the corner: {p5:.1e} (W and D), {p5n:.1e} (W, central difference)'))

for name, held, line in out:
    print(f'{name}: {"not killed" if held else "KILLED"}. {line}')
# for the reading: the sweep's room near the corner, where it is not 1/s^2
print(f'reading: the sweep T at s = 1 gives s^2 T\' = {dT(1):.4f}, at s = 2 {4 * dT(2):.4f}, at 2^10 {2**20 * dT(2**10):.6f} (-> 4/pi = {4/math.pi:.6f})')
