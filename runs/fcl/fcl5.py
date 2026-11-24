# FCL run 5: light past a mass. See plans/fcl-plan.md (predictions committed first).
# Run from the repository root: python3 runs/fcl/fcl5.py
import math
import random
from mpmath import mp, mpf, mpc, sqrt, pi, atan, quad, inf, im

mp.dps = 30
R = random.Random(20261126)


def verdict(name, ok, note=""):
    print(f"{name}: {'not killed' if ok else 'KILLED'} {note}")


def images(y):
    s = sqrt(y * y + 4)
    return (y + s) / 2, (y - s) / 2


def cdf(t, z):
    return mpf(1) / 2 + atan((t - z.real) / z.imag) / pi


def pdf(t, z):
    return z.imag / pi / ((t - z.real) ** 2 + z.imag**2)


print("FCL run 5, mpmath", mp.dps, "digits\n")

# L1
worst = mpf(0)
for ys in ("0.01", "0.3", "1", "2.5", "17", "-4"):
    y = mpf(ys)
    up, um = images(y)
    worst = max(worst, abs(up * um + 1), abs(up - 1 / up - y), abs(um - 1 / um - y))
verdict("L1", worst < mpf(10) ** -25, f"(u+ u- off -1, or the lens equation, by at most {mp.nstr(worst, 3)})")

# L2 (floats for the counts; the magnification identity exact)
def sky(kind):
    if kind == "cauchy":
        while True:
            g = [R.gauss(0, 1) for _ in range(3)]
            if abs(g[2]) > 1e-9:
                return 0.8 + 1.5 * g[0] / abs(g[2]), -0.4 + 1.5 * g[1] / abs(g[2])
    if kind == "gauss":
        return R.gauss(0.3, 2), R.gauss(0, 0.5)
    while True:
        a, b = R.uniform(-3, 3), R.uniform(-3, 3)
        if a * a + b * b <= 9:
            return a, b


counts = []
for kind in ("cauchy", "gauss", "disc"):
    inside = outside = 0
    for _ in range(20000):
        a, b = sky(kind)
        y = math.hypot(a, b)
        s = math.sqrt(y * y + 4)
        for r in ((y + s) / 2, (s - y) / 2):
            if r < 1:
                inside += 1
            elif r > 1:
                outside += 1
    counts.append((kind, inside, outside))
wm = mpf(0)
for ys in ("0.05", "0.7", "3", "40"):
    y = mpf(ys)
    up, um = images(y)
    mag = lambda u: 1 / abs(1 - 1 / u**4)
    wm = max(wm, abs(mag(up) - mag(um) - 1))
verdict("L2", all(i == 20000 and o == 20000 for _, i, o in counts) and wm < mpf(10) ** -20,
        f"(inside, outside of 20,000 sources: {counts}; magnifications differ from 1 by {mp.nstr(wm, 3)})")

# L3 images Cauchy(z) -> sources Cauchy(z - 1/z)
worst = mpf(0)
for z in (mpc(0, 1), mpc(0, "0.3"), mpc("0.7", "0.4"), mpc(-2, "1.5")):
    w = z - 1 / z
    for ts in ("-9", "-2", "-0.4", "0", "0.6", "3", "25"):
        t = mpf(ts)
        up, um = images(t)                      # f(u) <= t  <=>  u <= um  or  0 < u <= up
        got = cdf(um, z) + cdf(up, z) - cdf(mpf(0), z)
        worst = max(worst, abs(got - cdf(t, w)))
    print(f"  L3 images at z = {mp.nstr(z, 4)}: sources at {mp.nstr(w, 8)}")
sc = [(g, mpf(g) + 1 / mpf(g)) for g in ("0.25", "0.5", "1", "2", "4")]
print("  L3 images centred on the mass, scale -> sources' scale:", ", ".join(f"{g} -> {mp.nstr(v, 6)}" for g, v in sc))
verdict("L3", worst < mpf(10) ** -20, f"(largest gap in the distribution function {mp.nstr(worst, 3)})")

# L4 sources Cauchy(w) -> images: C(z1) + C(z2), z2 = -1/z1
worst = mpf(0)
for w in (mpc(0, 2), mpc(1, "0.5"), mpc(-3, "0.2")):
    z1 = (w + sqrt(w * w + 4)) / 2
    z2 = -1 / z1
    assert z1.imag > 0 and z2.imag > 0 and abs(z2 - 1 / z2 - w) < mpf(10) ** -25
    for us in ("-12", "-3", "-1", "-0.5", "-0.1", "0.02", "0.3", "1", "1.4", "2", "6", "30"):
        u = mpf(us)
        got = pdf(u - 1 / u, w) * (1 + 1 / u**2)
        worst = max(worst, abs(got - pdf(u, z1) - pdf(u, z2)))
    print(f"  L4 sources at w = {mp.nstr(w, 4)}: images' two points {mp.nstr(z1, 8)} and {mp.nstr(z2, 8)}")
verdict("L4", worst < mpf(10) ** -20, f"(largest gap in the density {mp.nstr(worst, 3)})")

# L5 the whole screen: sky a centred 2D Cauchy of scale 1
G = mpf(1)
src = lambda y: G / (2 * pi * (G * G + y * y) ** mpf("1.5"))            # per unit area
img = lambda r: src(abs(r - 1 / r)) * abs(1 - 1 / r**4)                 # images per unit screen area
ring = img(mpf(1))
tot_in = quad(lambda r: 2 * pi * r * img(r), [0, mpf("0.5"), 1])
tot_out = quad(lambda r: 2 * pi * r * img(r), [1, 2, 10, inf])
outer = lambda r: 1 - G / sqrt(G * G + (r - 1 / r) ** 2)                 # outer images' radial distribution function
rs = [1 + mpf(10) ** (mpf(k) / 40 - 3) for k in range(0, 281)]


def gap(g):
    return max(abs(outer(r) - (1 - g / sqrt(g * g + r * r))) for r in rs)


best = min((gap(mpf(k) / 100), mpf(k) / 100) for k in range(20, 601))
print(f"  L5 images inside and outside the ring: {mp.nstr(tot_in, 12)}, {mp.nstr(tot_out, 12)}; density on the ring {mp.nstr(ring, 3)}")
print(f"  L5 least gap from a centred 2D Cauchy: {mp.nstr(best[0], 6)} at scale {mp.nstr(best[1], 4)}")
verdict("L5", ring == 0 and best[0] >= mpf("0.08"))

# L6
verdict("L6", True, "(an identity; nothing run)")
