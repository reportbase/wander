# FCL run 6: what a facing adds to a pull. See plans/fcl-plan.md (predictions committed first).
# Run from the repository root: python3 runs/fcl/fcl6.py
import random
from mpmath import mp, mpf, matrix, sqrt, pi, sin, cos, quad, inf

mp.dps = 30
R = random.Random(20261127)


def rnd(a, b):
    return mpf(R.randrange(10**12)) / 10**12 * (b - a) + a


def vec(*a):
    return matrix([mpf(x) for x in a])


def nrm(v):
    return sqrt(sum(x * x for x in v))


def dot(a, b):
    return sum(a[i] * b[i] for i in range(3))


def unit():
    while True:
        v = vec(rnd(-1, 1), rnd(-1, 1), rnd(-1, 1))
        if mpf("0.2") < nrm(v) < 1:
            return v / nrm(v)


def scene(n=8):
    return [(rnd(0.5, 2), unit() * rnd(1, 4)) for _ in range(n)]


def g_of(sc):
    return sum((m * x / nrm(x) ** 3 for m, x in sc), vec(0, 0, 0))     # the take is at the origin


def F(n, sc):
    t = mpf(0)
    for m, x in sc:
        c = dot(n, x) / nrm(x)
        if c > 0:
            t += m * c / nrm(x) ** 2
    return t


def frame():
    a = unit()
    b = unit()
    b = b - dot(a, b) * a
    b = b / nrm(b)
    c = vec(a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
    return a, b, c


def verdict(name, ok, note=""):
    print(f"{name}: {'not killed' if ok else 'KILLED'} {note}")


print("FCL run 6, mpmath", mp.dps, "digits\n")
scenes = [scene() for _ in range(10)]

# S1
worst = mpf(0)
for sc in scenes:
    g = g_of(sc)
    for _ in range(5):
        n = unit()
        worst = max(worst, abs(F(n, sc) - F(-n, sc) - dot(n, g)))
verdict("S1", worst < mpf(10) ** -25, f"(largest miss {mp.nstr(worst, 3)} over 50 facings)")

# S2 a uniform shell of radius 1 and mass 1, the take at distance a from the centre along z
w2 = mpf(0)
for a_s in ("0.3", "0.6", "0.9"):
    a = mpf(a_s)
    # by the shell's mass elements: front of +z is cos(th) > a
    f = lambda th: (cos(th) - a) * sin(th) / 2 / (1 + a * a - 2 * a * cos(th)) ** mpf("1.5")
    from mpmath import acos
    t0 = acos(a)
    up = quad(f, [0, t0 / 2, t0])
    dn = -quad(f, [t0, (t0 + pi) / 2, pi])
    # by directions: sky per solid angle 1/(4 pi cos i), cos i = sqrt(1 - a^2 sin^2 psi)
    along = quad(lambda p: cos(p) * sin(p) / sqrt(1 - a * a * sin(p) ** 2), [0, pi / 4, pi / 2]) / 2
    across = quad(lambda p: sin(p) ** 2 / sqrt(1 - a * a * sin(p) ** 2), [0, pi / 2, pi]) / (2 * pi)
    w2 = max(w2, abs(up - dn), abs(up - along))
    print(f"  S2 at {a_s} of the radius: toward the near side {mp.nstr(up, 12)}, toward the far side {mp.nstr(dn, 12)}; across the line {mp.nstr(across, 12)}")
    last = (along, across)
vary = abs(last[1] / last[0] - 1)
verdict("S2", w2 < mpf(10) ** -20 and vary > mpf("0.01"), f"(opposite takes differ by {mp.nstr(w2, 3)}; at 0.9 across against along differ by {mp.nstr(vary * 100, 4)}%)")

# S3 all facings at once: per mass, integrate over facings in the mass's own polar frame
m1 = quad(lambda t: cos(t) * sin(t) / 2, [0, pi / 2])                # mean of (n.u)+ over the sphere
m2 = quad(lambda t: cos(t) ** 2 * sin(t) / 2, [0, pi / 2])           # mean of (n.u)+ (n.u)
print(f"  S3 mean of (n.u)+ = {mp.nstr(m1, 15)}, mean of n (n.u)+ along u = {mp.nstr(m2, 15)}")
# and a direct check on one scene by a product rule over facings (kinked integrand, so a coarse check)
sc = scenes[0]
N = 200
accF, accV = mpf(0), vec(0, 0, 0)
mp.dps = 15
for i in range(N):
    z = (mpf(i) + mpf(1) / 2) / N * 2 - 1
    s = sqrt(1 - z * z)
    for j in range(2 * N):
        ph = (mpf(j) + mpf(1) / 2) / (2 * N) * 2 * pi
        n = vec(s * cos(ph), s * sin(ph), z)
        v = F(n, sc)
        accF += v
        accV += v * n
tot = N * 2 * N
mp.dps = 30
sky = sum(m / nrm(x) ** 2 for m, x in sc)
g = g_of(sc)
e3 = [abs(m1 - mpf(1) / 4), abs(m2 - mpf(1) / 6), abs(accF / tot / (sky / 4) - 1), nrm(accV / tot * 6 - g) / nrm(g)]
verdict("S3", e3[0] < mpf(10) ** -20 and e3[1] < mpf(10) ** -20,
        f"(exact means off by {mp.nstr(e3[0], 2)}, {mp.nstr(e3[1], 2)}; on a grid of 80,000 facings <F> off sky/4 by {mp.nstr(e3[2], 2)}, 6<nF> off g by {mp.nstr(e3[3], 2)})")

# S4 a sky alike in every direction on the facing's flat screen
dens = lambda r: 1 / (pi * (1 + r * r) ** 2)
share = lambda r: quad(lambda q: 2 * pi * q * dens(q), [0, r / 2, r])
w4 = abs(share(inf) - 1) if False else abs(quad(lambda q: 2 * pi * q * dens(q), [0, 1, 10, inf]) - 1)
for rs in ("0.25", "1", "3", "7.5"):
    r = mpf(rs)
    w4 = max(w4, abs(share(r) - r * r / (1 + r * r)), abs(share(r) + share(1 / r) - 1))
strip = lambda x0: 2 * quad(lambda x: quad(lambda y: dens(sqrt(x * x + y * y)), [-inf, -1, 0, 1, inf]), [0, x0 / 2, x0])
for xs in ("0.3", "1", "4"):
    x0 = mpf(xs)
    w4 = max(w4, abs(strip(x0) - x0 / sqrt(1 + x0 * x0)))
h = strip(1 / sqrt(mpf(3)))
look_half = 1 - 1 / sqrt(1 + mpf(3))
verdict("S4", w4 < mpf(10) ** -20 and abs(h - mpf(1) / 2) < mpf(10) ** -20,
        f"(largest miss {mp.nstr(w4, 3)}; share within one thumb {mp.nstr(share(mpf(1)), 15)}; strip to 1/sqrt 3 {mp.nstr(h, 15)}; the look's share within sqrt 3 is {mp.nstr(look_half, 6)})")

# S5 six facings
worst = mpf(0)
for sc in scenes:
    a, b, c = frame()
    g = g_of(sc)
    rebuilt = (F(a, sc) - F(-a, sc)) * a + (F(b, sc) - F(-b, sc)) * b + (F(c, sc) - F(-c, sc)) * c
    worst = max(worst, nrm(rebuilt - g))
verdict("S5", worst < mpf(10) ** -25, f"(g rebuilt from six takes, largest miss {mp.nstr(worst, 3)})")

# S6
k = mpf(7)
sc = scenes[1]
n = unit()
a = F(n, sc) / F(-n, sc)
b = F(n, [(m, k * x) for m, x in sc]) / F(-n, [(m, k * x) for m, x in sc])
c = F(n, [(k * m, x) for m, x in sc]) / F(-n, [(k * m, x) for m, x in sc])
d = F(n, [(m, k * x) for m, x in sc]) * k * k / F(n, sc)
verdict("S6", max(abs(a - b), abs(a - c), abs(d - 1)) < mpf(10) ** -25, f"(the ratio of opposite takes {mp.nstr(a, 8)} under both scalings; one take x k^2: {mp.nstr(d, 12)})")
