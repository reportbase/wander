# FCL run 3: two masses on each other's stage. See plans/fcl-plan.md (predictions committed first).
# Run from the repository root: python3 runs/fcl/fcl3.py
import random
from mpmath import mp, mpf, matrix, sqrt, pi, quad, inf, findroot, sin, cos, acos

mp.dps = 40
TOL = mpf(10) ** -30
R = random.Random(20261124)
MUS = [mpf(1) / 4, mpf(1), mpf(4), mpf(9), mpf("81.3")]
D = mpf(1)


def rnd(a, b):
    return mpf(R.randrange(10**12)) / 10**12 * (b - a) + a


def vec(*a):
    return matrix([mpf(x) for x in a])


def nrm(v):
    return sqrt(sum(x * x for x in v))


def pulls(p, M1, M2, D=D):
    u1, u2 = -p, vec(D, 0, 0) - p
    return M1 * u1 / nrm(u1) ** 3, M2 * u2 / nrm(u2) ** 3


def verdict(name, ok, note=""):
    print(f"{name}: {'not killed' if ok else 'KILLED'} {note}")


def sphere_dir():
    z = rnd(-1, 1)
    t = rnd(0, 2 * pi)
    s = sqrt(1 - z * z)
    return vec(z, s * cos(t), s * sin(t))


print("FCL run 3, mpmath", mp.dps, "digits\n")

# T1
worst, second = mpf(0), []
for mu in MUS:
    M1, M2 = mu, mpf(1)
    x = findroot(lambda x: M1 / x**2 - M2 / (D - x) ** 2, mpf("0.5"))
    worst = max(worst, abs(x / (D - x) - sqrt(mu)))
    xm = D * sqrt(mu) / (1 + sqrt(mu))
    # search space for another zero: Newton on the net pull from seeded starts
    for _ in range(80):
        p0 = [rnd(-2, 3), rnd(-2, 2), rnd(-2, 2)]
        try:
            f = lambda a, b, c: list(sum(pulls(vec(a, b, c), M1, M2), vec(0, 0, 0)))
            s = findroot(f, p0, tol=mpf(10) ** -25, maxsteps=60)
            p = vec(*s)
            g1, g2 = pulls(p, M1, M2)
            if nrm(g1 + g2) < mpf(10) ** -20 * nrm(g1) and nrm(p - vec(xm, 0, 0)) > mpf(10) ** -15:
                second.append((mp.nstr(mu, 4), [mp.nstr(c, 6) for c in p]))
        except Exception:
            pass
    print(f"  T1 mu = {mp.nstr(mu, 5)}: the pulls cancel at x = {mp.nstr(x, 12)} D, rho = {mp.nstr(x / (D - x), 12)}")
verdict("T1", worst < TOL and not second, f"(rho off sqrt(mu) by {mp.nstr(worst, 3)}; other zeros found from 400 starts: {second[:3]})")

# T2
worst = mpf(0)
for mu in MUS:
    for rs in ("0.1", "0.5", "1", "2.3", "7", "40"):
        rho = mpf(rs)
        def ratio(rho):
            x = D * rho / (1 + rho)
            g1, g2 = pulls(vec(x, 0, 0), mu, 1)
            return nrm(g1) / nrm(g2)
        worst = max(worst, abs(ratio(rho) * ratio(mu / rho) - 1), abs(ratio(rho) - mu / rho**2) / ratio(rho))
verdict("T2", worst < TOL, f"(largest miss {mp.nstr(worst, 3)} over 30 pairs)")

# T3
worst, sides = mpf(0), True
k = mpf(7)
moved = []
for mu in MUS:
    rm, rc = sqrt(mu), 1 / mu
    worst = max(worst, abs(rm * rm * rc - 1))
    if mu != 1:
        sides = sides and (rm - 1) * (rc - 1) < 0
    else:
        sides = sides and rm == 1 and rc == 1
    # scaled lengths, scaled masses: the zero found afresh
    for (M1, M2, DD) in ((mu, mpf(1), k * D), (k * mu, k, D)):
        x = findroot(lambda x: M1 / x**2 - M2 / (DD - x) ** 2, DD / 2)
        worst = max(worst, abs(x / (DD - x) - rm))
        xc = DD * M2 / (M1 + M2)
        worst = max(worst, abs(xc / (DD - xc) - rc))
    x = findroot(lambda x: k * mu / x**2 - 1 / (D - x) ** 2, D / 2)
    moved.append(abs(x / (D - x) - rm))
verdict("T3", worst < TOL and sides and min(moved) > mpf("0.1"),
        f"(largest miss {mp.nstr(worst, 3)}; opposite sides: {sides}; one mass x7 moves the meeting point's rho by at least {mp.nstr(min(moved), 4)})")

# T4, T5
w4, w5, near = mpf(0), mpf(0), 0
for mu in MUS:
    M1, M2 = mu, mpf(1)
    xm = vec(D * sqrt(mu) / (1 + sqrt(mu)), 0, 0)
    for _ in range(40):
        if mu == 1:
            p = vec(D / 2, rnd(-3, 3), rnd(-3, 3))
        else:
            c = vec(D * mu / (mu - 1), 0, 0)
            p = c + D * sqrt(mu) / abs(mu - 1) * sphere_dir()
        g1, g2 = pulls(p, M1, M2)
        w4 = max(w4, abs(nrm(g1) - nrm(g2)) / nrm(g1))
        g = g1 + g2
        to = xm - p
        if nrm(to) > mpf(10) ** -10:
            w5 = max(w5, nrm(g / nrm(g) - to / nrm(to)))
        q = p + vec(rnd(-1, 1), rnd(-1, 1), rnd(-1, 1)) * mpf("0.3")
        if mu == 1:
            off = abs(q[0] - D / 2) / D
        else:
            off = abs(nrm(q - c) - D * sqrt(mu) / abs(mu - 1)) / D
        h1, h2 = pulls(q, M1, M2)
        if off > mpf("0.01") and abs(nrm(h1) - nrm(h2)) / nrm(h1) < mpf(10) ** -3:
            near += 1
    onsph = abs(nrm(xm - (vec(D * mu / (mu - 1), 0, 0) if mu != 1 else vec(D / 2, 0, 0))) - (D * sqrt(mu) / abs(mu - 1) if mu != 1 else 0))
    w4 = max(w4, onsph)
verdict("T4", w4 < TOL and near == 0, f"(equal pulls on the sphere to {mp.nstr(w4, 3)} at 200 points; equal at {near} of 200 points off it)")
verdict("T5", w5 < TOL, f"(net pull against the direction to the meeting point: {mp.nstr(w5, 3)} at 200 points)")

# T6
mp.dps = 30
ok6, notes = True, []
for mu in (mpf(4), mpf(9), mpf("81.3")):
    M1, M2 = mu, mpf(1)
    x = D * sqrt(mu) / (1 + sqrt(mu))
    y = D - x
    dens = lambda r, M, d: M * d / (d * d + r * r) ** mpf("1.5")       # the pull's crossing per unit area (G = 1)
    t1 = quad(lambda r: 2 * pi * r * dens(r, M1, x), [0, x, 10 * x, inf])
    t2 = quad(lambda r: 2 * pi * r * dens(r, M2, y), [0, y, 10 * y, inf])
    ratio = lambda r: dens(r, M1, x) / dens(r, M2, y)
    rs = [mpf(10) ** (mpf(j) / 6 - 3) for j in range(60)]
    vals = [ratio(r) for r in rs]
    inc = all(b > a for a, b in zip(vals, vals[1:]))
    far = ratio(mpf(10) ** 6)
    # another plane between the masses: totals do not depend on where it stands
    x2 = D * mpf("0.137")
    u1 = quad(lambda r: 2 * pi * r * dens(r, M1, x2), [0, x2, 10 * x2, inf])
    u2 = quad(lambda r: 2 * pi * r * dens(r, M2, D - x2), [0, 1, 10, inf])
    e = [abs(t1 / (2 * pi * M1) - 1), abs(t2 / (2 * pi * M2) - 1), abs(u1 - u2 - (t1 - t2)) / t1]
    ok6 = ok6 and max(e) < mpf(10) ** -20 and abs(ratio(0) - 1) < mpf(10) ** -25 and abs(far / mu ** mpf("1.5") - 1) < mpf(10) ** -6 and inc
    notes.append(f"mu {mp.nstr(mu, 4)}: totals off {mp.nstr(max(e), 2)}, ratio 1 at the foot, {mp.nstr(ratio(y), 6)} at one lighter-height out, {mp.nstr(far, 8)} far out (mu^1.5 = {mp.nstr(mu ** mpf('1.5'), 8)}), rising: {inc}")
for n in notes:
    print("  T6", n)
verdict("T6", ok6)
mp.dps = 40

# T7
worst = mpf(0)
for mu in MUS:
    g1at2 = mu / D**2
    g2at1 = 1 / D**2
    worst = max(worst, abs(1 * g1at2 - mu * g2at1), abs(g2at1 / g1at2 - 1 / mu))
verdict("T7", worst < TOL, "(an identity)")
