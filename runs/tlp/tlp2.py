# TLP run 2: T5' only, the bearing for a sphere of any radius. Prediction in plans/tlp-plan.md.
import random
import mpmath as mp

mp.mp.dps = 60
rng = random.Random(20261118)


def unit(v): return v / mp.norm(v)
def dot(a, b): return (a.T * b)[0]
def cross(a, b): return mp.matrix([a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]])


def rand_unit():
    while True:
        v = mp.matrix([mp.mpf(rng.gauss(0, 1)) for _ in range(3)])
        if mp.norm(v) > 0.1: return unit(v)


def bearing(Pi, ei, Pj):
    t = Pj - (dot(Pi, Pj) / dot(Pi, Pi)) * Pi
    return mp.atan2(dot(t, cross(Pi, ei) / mp.norm(Pi)), dot(t, ei))


def wrap(x):
    x = mp.fmod(x + mp.pi, 2 * mp.pi)
    if x < 0: x += 2 * mp.pi
    return x - mp.pi


def loop_sum(P, e):
    return sum(wrap(bearing(P[i], e[i], P[(i + 1) % 3]) - bearing(P[(i + 1) % 3], e[(i + 1) % 3], P[i]) + mp.pi) for i in range(3))


worst = 0
for trial in range(20):
    P = [rand_unit() for _ in range(3)]
    e = [unit(cross(p, rand_unit())) for p in P]
    S = loop_sum(P, e)
    for k in (mp.mpf(7), mp.mpf(1) / 3, mp.mpf(1000)):
        worst = max(worst, abs(loop_sum([k * p for p in P], e) - S))
line = f"T5': {'not killed' if worst < mp.mpf(10) ** -40 else 'KILLED'}  20 triangles, the world scaled by 7, 1/3, 1000: S moved at most {mp.nstr(worst, 3)}"
print(line)
open('runs/tlp/tlp-run2.txt', 'w').write(line + "\n")
