# FCL run 1: what a place with no facing takes in. See plans/fcl-plan.md (predictions committed first).
# Run from the repository root: python3 runs/fcl/fcl.py
import random
from mpmath import mp, mpf, matrix, sqrt, pi, sin, cos, quad, log, svd_r, norm

mp.dps = 50
R = random.Random(20261124)


def rnd(a, b):
    return mpf(R.randrange(10**9)) / 10**9 * (b - a) + a


def vec(*a):
    return matrix([mpf(x) for x in a])


def nrm(v):
    return sqrt(sum(x * x for x in v))


def pull(p, scene):
    g = vec(0, 0, 0)
    for m, x in scene:
        u = x - p
        g += m * u / nrm(u) ** 3
    return g


def scene_of(n):
    return [(rnd(0.5, 2), vec(rnd(-1, 1), rnd(-1, 1), rnd(-1, 1))) for _ in range(n)]


def take_at():
    while True:
        v = vec(rnd(-1, 1), rnd(-1, 1), rnd(-1, 1))
        if nrm(v) > 0.2:
            return v / nrm(v) * rnd(3, 5)


def slope(xs, ys):
    lx = [log(x) for x in xs]
    ly = [log(y) for y in ys]
    n = len(xs)
    mx, my = sum(lx) / n, sum(ly) / n
    return sum((a - mx) * (b - my) for a, b in zip(lx, ly)) / sum((a - mx) ** 2 for a in lx)


def verdict(name, ok, note=""):
    print(f"{name}: {'not killed' if ok else 'KILLED'} {note}")


print("FCL run 1, mpmath", mp.dps, "digits\n")

# F1 the shell: surface density 1/(4 pi) on the unit sphere, total mass 1; pull at (0,0,a) by quadrature.
worst = mpf(0)
for a in (mpf(0), mpf("0.3"), mpf("0.9")):
    f = lambda th: (cos(th) - a) * sin(th) / (1 + a * a - 2 * a * cos(th)) ** mpf("1.5") / 2
    gz = quad(f, [0, pi / 4, pi / 2, 3 * pi / 4, pi])
    print(f"  F1 inside the shell at {a}: pull {mp.nstr(gz, 5)}")
    worst = max(worst, abs(gz))
verdict("F1", worst < mpf(10) ** -25, f"(largest {mp.nstr(worst, 3)}; a look meets the shell in every direction)")

# F2 amount against distance, and the two scalings.
p = vec(0, 0, 0)
u = vec(2, -1, 3)
u = u / nrm(u)
d, m = mpf("1.7"), mpf("0.9")
g1 = pull(p, [(m, d * u)])
g2 = pull(p, [(4 * m, 2 * d * u)])
k = mpf(7)
sc = scene_of(5)
t = take_at()
g = pull(t, sc)
gk = pull(k * t, [(mm, k * x) for mm, x in sc])
gd = pull(k * t, [(mm * k ** 3, k * x) for mm, x in sc])
e = [nrm(g1 - g2), nrm(gk / nrm(gk) - g / nrm(g)), abs(nrm(gk) * k * k / nrm(g) - 1), abs(nrm(gd) / (k * nrm(g)) - 1)]
verdict("F2", max(e) < mpf(10) ** -40,
        f"(m at d against 4m at 2d: {mp.nstr(e[0], 3)}; direction under k: {mp.nstr(e[1], 3)}; length x k^-2: {mp.nstr(e[2], 3)}; one density, x k: {mp.nstr(e[3], 3)})")

# F3 what a far body leaves.
body = [(rnd(0.5, 2), vec(rnd(-1, 1), rnd(-1, 1), rnd(-1, 1)) * mpf("0.57")) for _ in range(12)]
M = sum(mm for mm, _ in body)
com = sum((mm * x for mm, x in body), vec(0, 0, 0)) / M
Q = matrix(3, 3)
for mm, x in body:
    y = x - com
    y2 = sum(c * c for c in y)
    for i in range(3):
        for j in range(3):
            Q[i, j] += mm * (3 * y[i] * y[j] - (y2 if i == j else 0))
dirn = vec(3, 5, -2)
dirn = dirn / nrm(dirn)
rs, e1, e2 = [], [], []
for j in range(8):
    r = mpf(10) * 2 ** j
    x = r * dirn                       # the take's place, from the centre of mass
    gt = pull(com + x, body)
    g0 = -M * x / r ** 3
    Qx = Q * x
    xQx = sum(x[i] * Qx[i] for i in range(3))
    gq = g0 + Qx / r ** 5 - mpf(5) / 2 * xQx * x / r ** 7
    rs.append(r)
    e1.append(nrm(gt - g0) / nrm(g0))
    e2.append(nrm(gt - gq) / nrm(g0))
    print(f"  F3 r = {int(r):5d}: off the monopole {mp.nstr(e1[-1], 4)}, with the quadrupole {mp.nstr(e2[-1], 4)}")
s1, s2 = slope(rs, e1), slope(rs, e2)
verdict("F3", abs(s1 + 2) < 0.05 and abs(s2 + 3) < 0.05, f"(slopes {mp.nstr(s1, 5)} and {mp.nstr(s2, 5)}; predicted -2, -3)")


def skew(pa, ga, pb, gb):
    # distance between the lines pa + t ga and pb + u gb, and the point nearest both
    c = vec(ga[1] * gb[2] - ga[2] * gb[1], ga[2] * gb[0] - ga[0] * gb[2], ga[0] * gb[1] - ga[1] * gb[0])
    w = pb - pa
    dist = abs(sum(w[i] * c[i] for i in range(3))) / nrm(c)
    A = matrix([[sum(ga[i] * ga[i] for i in range(3)), -sum(ga[i] * gb[i] for i in range(3))],
                [sum(ga[i] * gb[i] for i in range(3)), -sum(gb[i] * gb[i] for i in range(3))]])
    b = matrix([sum(w[i] * ga[i] for i in range(3)), sum(w[i] * gb[i] for i in range(3))])
    tu = A ** -1 * b
    return dist, (pa + tu[0] * ga + pb + tu[1] * gb) / 2


# F4 two takes sharing a frame, one mass.
worst = mpf(0)
for seed in range(5):
    sc = scene_of(1)
    m, x = sc[0]
    pa, pb = take_at(), take_at()
    ga, gb = pull(pa, sc), pull(pb, sc)
    dist, where = skew(pa, ga, pb, gb)
    da, db = nrm(where - pa), nrm(where - pb)
    B = nrm(pb - pa)
    errs = [dist / B, nrm(where - x) / B, abs(nrm(ga) / nrm(gb) / (db / da) ** 2 - 1), abs(nrm(ga) * da * da / m - 1)]
    worst = max(worst, *errs)
verdict("F4", worst < mpf(10) ** -40, f"(largest of skew, place, the length-ratio check and the mass over five scenes: {mp.nstr(worst, 3)})")

# F5 two takes detect that a scene is not one mass.
ax = vec(1, 2, -1)
ax = ax / nrm(ax)
ua = vec(2, 1, 1)
ua = ua / nrm(ua)
ub = vec(-1, 2, 2)
ub = ub / nrm(ub)


def miss(s, r):
    sc = [(mpf(1), ax * s / 2), (mpf("1.7"), -ax * s / 2)]
    pa, pb = r * ua, r * ub
    return skew(pa, pull(pa, sc), pb, pull(pb, sc))[0]


ss = [mpf("0.01") * 2 ** j for j in range(7)]
rr = [mpf(10) * 2 ** j for j in range(7)]
ms = [miss(s, mpf(10)) for s in ss]
mr = [miss(mpf("0.1"), r) for r in rr]
for s, v in zip(ss, ms):
    print(f"  F5 s = {mp.nstr(s, 3):>5}, r = 10: lines miss by {mp.nstr(v, 4)}")
for r, v in zip(rr, mr):
    print(f"  F5 s = 0.1, r = {int(r):4d}: lines miss by {mp.nstr(v, 4)}")
a1, a2 = slope(ss, ms), slope(rr, mr)
verdict("F5", abs(a1 - 2) < 0.05 and abs(a2 + 1) < 0.05, f"(slopes {mp.nstr(a1, 5)} in s and {mp.nstr(a2, 5)} in r; predicted +2, -1)")


def jac(scene, takes, framed):
    rows = []
    for p in takes:
        g = pull(p, scene)
        cols = []
        for m, x in scene:
            u = x - p
            r = nrm(u)
            cols.append(u / r ** 3)                                   # d g / d m
            for a in range(3):                                       # d g / d x_a
                ea = vec(*[1 if i == a else 0 for i in range(3)])
                cols.append(m * (ea / r ** 3 - 3 * u[a] * u / r ** 5))
        if framed:
            for i in range(3):
                rows.append([c[i] for c in cols])
        else:
            gh = g / nrm(g)
            rows.append([sum(gh[i] * c[i] for i in range(3)) for c in cols])
    return matrix(rows)


def rank(J):
    S = svd_r(J, compute_uv=False)
    top = max(S)
    return sum(1 for s in S if s > top * mpf(10) ** -30)


# F6 counting with a shared frame.
bad = []
for n in range(1, 5):
    for K in range(1, 7):
        for seed in range(5):
            sc = scene_of(n)
            tk = [take_at() for _ in range(K)]
            rk = rank(jac(sc, tk, True))
            if rk != min(3 * K, 4 * n):
                bad.append((n, K, seed, rk))
verdict("F6", not bad, f"(rank min(3K, 4n) in {4 * 6 * 5} cases; short: {bad[:6]})")

# F7 counting with no shared frame, and the coplanar twin.
bad = []
for n in (1, 2):
    for K in range(1, 11):
        for seed in range(5):
            sc = scene_of(n)
            tk = [take_at() for _ in range(K)]
            rk = rank(jac(sc, tk, False))
            if rk != min(K, 4 * n):
                bad.append((n, K, seed, rk))
sc = scene_of(3)
mir = [(m, vec(x[0], x[1], -x[2])) for m, x in sc]
tk = []
for _ in range(8):
    t = take_at()
    tk.append(vec(t[0], t[1], 0) * 2)
dl = max(abs(nrm(pull(t, sc)) - nrm(pull(t, mir))) for t in tk)
dv = max(nrm(pull(t, sc) - pull(t, mir)) for t in tk)
verdict("F7", not bad and dl < mpf(10) ** -40,
        f"(rank min(K, 4n) in {2 * 10 * 5} cases, short: {bad[:6]}; mirrored scene, coplanar takes: lengths differ by {mp.nstr(dl, 3)}, arrows by {mp.nstr(dv, 3)})")

# F8 the scale test, sorted.
sc = scene_of(1)
m, x = sc[0]
pa, pb = take_at(), take_at()
ga, gb = pull(pa, sc), pull(pb, sc)
sck = [(m, k * x)]
gak, gbk = pull(k * pa, sck), pull(k * pb, sck)
_, w = skew(pa, ga, pb, gb)
_, wk = skew(k * pa, gak, k * pb, gbk)
B, Bk = nrm(pb - pa), k * nrm(pb - pa)
unm = [nrm(gak / nrm(gak) - ga / nrm(ga)), abs(nrm(gak) / nrm(gbk) - nrm(ga) / nrm(gb)), nrm((wk - k * pa) / Bk - (w - pa) / B)]
mov = [nrm(gak) / nrm(ga), (nrm(gak) * nrm(wk - k * pa) ** 2 / Bk ** 2) / (nrm(ga) * nrm(w - pa) ** 2 / B ** 2)]
verdict("F8", max(unm) < mpf(10) ** -40 and abs(mov[0] - 1 / k ** 2) < mpf(10) ** -40 and abs(mov[1] - 1 / k ** 2) < mpf(10) ** -40,
        f"(unmoved: direction {mp.nstr(unm[0], 3)}, length ratio {mp.nstr(unm[1], 3)}, place in baselines {mp.nstr(unm[2], 3)}; moved: |g| x {mp.nstr(mov[0], 6)}, m/B^2 x {mp.nstr(mov[1], 6)})")
