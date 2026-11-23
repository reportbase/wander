# GRV: gravity sorted by direction (plans/grv-plan.md). Run from the repository's root: python3 runs/grv/grv.py
# mpmath at 50 digits; V3's pull over the sphere is a lattice sum in floats (its threshold is 1e-3).
from mpmath import mp, mpf, quad, quadosc, sqrt, sin, cos, asin, pi, exp, inf, fabs, nstr
from fractions import Fraction as F
import math, random
mp.dps = 50
out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)
e = lambda x: nstr(fabs(x), 3)

say('V1 a uniform ball by columns against (4/3) pi R^3 / d^2 and (4/3) R x pi (R/d)^2')
for dr in ['1.01', '2', '10', '1000']:
    R = mpf(1); d = mpf(dr) * R; a = asin(R / d)
    cols = 2 * pi * quad(lambda t: 2 * sqrt(max(R * R - d * d * sin(t) ** 2, 0)) * cos(t) * sin(t), [0, a / 2, a])
    newton = mpf(4) / 3 * pi * R ** 3 / d ** 2; share = mpf(4) / 3 * R * pi * (R / d) ** 2
    say('  d/R', dr, 'columns', nstr(cols, 20), 'rel miss', e((cols - newton) / newton), 'share form miss', e(share - newton))

def col_sphere(p, u, a, b):
    # the length of the ray from p along u inside the shell a < r < b (p inside a)
    pu = sum(x * y for x, y in zip(p, u)); pp = sum(x * x for x in p)
    t = lambda r: -pu + sqrt(pu * pu - pp + r * r)
    return t(b) - t(a)
def col_cube(p, u, a, b):
    t = lambda s: min(((s if ui > 0 else -s) - pi_) / ui for pi_, ui in zip(p, u) if ui != 0)
    return t(b) - t(a)
def dirs(n, seed):
    rnd = random.Random(seed); L = []
    while len(L) < n:
        v = [rnd.uniform(-1, 1) for _ in range(3)]; l = math.sqrt(sum(x * x for x in v))
        if 0.1 < l <= 1: L.append([mpf(x) / mpf(l) for x in v])
    return L

say('V2 inside a spherical shell (1, 1.5): the column toward u against the column toward -u, 40 seeded directions')
for r0 in ['0.3', '0.9']:
    p = [mpf(r0) * mpf(c) for c in ['0.6', '0.48', '0.64']]   # a point at distance r0 from the centre (0.6, 0.48, 0.64 is a unit vector)
    worst = max(fabs(col_sphere(p, u, mpf(1), mpf('1.5')) - col_sphere(p, [-x for x in u], mpf(1), mpf('1.5'))) for u in dirs(40, 7))
    say('  at', r0, 'the worst pair differs by', e(worst))

say('V3 inside a shell between cubes (1, 1.5) at (0.3, 0.2, 0.1)')
p = [mpf('0.3'), mpf('0.2'), mpf('0.1')]
diffs = [fabs(col_cube(p, u, mpf(1), mpf('1.5')) - col_cube(p, [-x for x in u], mpf(1), mpf('1.5'))) for u in dirs(40, 7)]
say('  pairs differing by more than 1e-3:', sum(1 for x in diffs if x > mpf('1e-3')), 'of 40; the largest', e(max(diffs)))
pf = [0.3, 0.2, 0.1]
def pull_cube(n):
    g = [0.0, 0.0, 0.0]; ga = math.pi * (3 - math.sqrt(5))
    for i in range(n):
        z = 1 - (2 * i + 1) / n; r = math.sqrt(1 - z * z); u = [r * math.cos(ga * i), r * math.sin(ga * i), z]
        t = lambda s: min(((s if ui > 0 else -s) - pi_) / ui for pi_, ui in zip(pf, u) if ui != 0)
        c = t(1.5) - t(1.0)
        for k in range(3): g[k] += c * u[k]
    return [x * 4 * math.pi / n for x in g]
for n in [100000, 400000]:
    g = pull_cube(n); say('  the pull over', n, 'directions', ['%.6f' % x for x in g], 'size %.6f' % math.sqrt(sum(x * x for x in g)))

say('V4 above a sheet: the vertical pull against 2 pi (1 + eps e^(-kh) cos kx)')
eps = mpf('0.3')
for k, h, x in [('1', '1', '0'), ('3', '0.5', '0.7'), ('0.2', '4', '2')]:
    k, h, x = mpf(k), mpf(h), mpf(x)
    ker = lambda u: 2 * h / (u * u + h * h)
    flat = quad(ker, [-inf, -h, 0, h, inf])
    osc = quadosc(lambda u: cos(k * (x + u)) * ker(u), [0, inf], omega=k) + quadosc(lambda u: cos(k * (x - u)) * ker(u), [0, inf], omega=k)
    got = flat + eps * osc; want = 2 * pi * (1 + eps * exp(-k * h) * cos(k * x))
    say('  k', k, 'h', h, 'x', x, 'pull', nstr(got, 20), 'miss', e(got - want))
for h in ['0.001', '1', '1000']:
    h = mpf(h); flat = quad(lambda u: 2 * h / (u * u + h * h), [-inf, -h, 0, h, inf])
    say('  uniform sheet, h', h, 'pull over 2 pi', nstr(flat / (2 * pi), 20), 'the Cauchy totals 1 within', e(flat / (2 * pi) - 1))
for h in ['0.5', '1', '3']:
    h = mpf(h); two = quad(lambda r: h * r / (r * r + h * h) ** mpf('1.5'), [0, h, inf])
    say('  in the plane, h', h, 'the kernel h/(2 pi (r^2+h^2)^(3/2)) totals', nstr(two, 20), 'miss', e(two - 1))
a, b = mpf('0.7'), mpf('1.3'); say('  at h = 1, four times the kernel against the wedge law at (0.7, 1.3): miss', e(4 / (2 * pi * (1 + a * a + b * b) ** mpf('1.5')) - 2 / (pi * (1 + a * a + b * b) ** mpf('1.5'))))

say('V5 the scale test on the ball, test points at 2R and 5R (exact fractions; pi left out of the pull)')
def pull(R, d, rho): return F(4, 3) * rho * R ** 3 / d ** 2
for kk in [F(1, 1000), F(7), F(10 ** 6)]:
    R = F(1); g2, g5 = pull(R, 2 * R, 1), pull(R, 5 * R, 1)
    a2, a5 = pull(kk * R, 2 * kk * R, 1), pull(kk * R, 5 * kk * R, 1)                                # the same density
    m2, m5 = pull(kk * R, 2 * kk * R, F(1) / kk ** 3), pull(kk * R, 5 * kk * R, F(1) / kk ** 3)      # the same mass
    say('  k', kk, 'same density: pull x', a2 / g2, a5 / g5, '| same mass: pull x', m2 / g2, m5 / g5, '| ratio of the two pulls', g2 / g5, a2 / a5, m2 / m5,
        '| share (R/d)^2', (R / (2 * R)) ** 2, (kk * R / (2 * kk * R)) ** 2)

say('V6 a half-ball from the centre of its flat face: by columns, by cylinders, against pi R; the whole ball')
for Rs in ['1', '10', '1000000']:
    R = mpf(Rs)
    cols = 2 * pi * quad(lambda t: R * cos(t) * sin(t), [0, pi / 2])
    cyl = 2 * pi * quad(lambda z: quad(lambda s: s * z / (s * s + z * z) ** mpf('1.5'), [0, z, sqrt(R * R - z * z)]) if z < R else mpf(0), [0, R / 1000, R / 10, R])
    whole = 2 * pi * quad(lambda t: R * cos(t) * sin(t), [0, pi / 2, pi])
    say('  R', Rs, 'columns', nstr(cols, 20), 'rel miss', e((cols - pi * R) / (pi * R)), 'cylinders rel miss', e((cyl - pi * R) / (pi * R)), 'the whole ball', e(whole / R))

say('V7 a thin cap of a sphere about the standpoint, half-angle 0.4: over its area with 1/r^2, against pi sin^2(0.4)')
al = mpf('0.4')
for Ds in ['1', '10', '1000']:
    D = mpf(Ds); got = quad(lambda t: (1 / D ** 2) * cos(t) * 2 * pi * D * sin(t) * D, [0, al])
    say('  radius', Ds, 'pull', nstr(got, 20), 'miss', e(got - pi * sin(al) ** 2))
open('runs/grv/grv-run1.txt', 'w').write('\n'.join(out) + '\n')
