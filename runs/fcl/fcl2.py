# FCL run 2: does the pull have a corner? See plans/fcl-plan.md (predictions committed first).
# Run from the repository root: python3 runs/fcl/fcl2.py
from mpmath import mp, mpf, sqrt, pi, asin, quad, inf, sin, cos, findroot

mp.dps = 30
TOL = mpf(10) ** -18


def K(x, y, d):
    return d / (2 * pi * (d * d + x * x + y * y) ** mpf("1.5"))


def strip(x0, d):
    # the kernel itself, integrated over the strip |x| <= x0 (y over the whole line)
    f = lambda x: quad(lambda y: K(x, y, d), [-inf, -d, 0, d, inf])
    return quad(f, [-x0, -x0 / 2, 0, x0 / 2, x0])


def disc(rho, d):
    return quad(lambda q: 2 * pi * q * K(q, 0, d), [0, rho / 2, rho])


def square(a, d):
    f = lambda x: quad(lambda y: K(x, y, d), [-a, 0, a])
    return quad(f, [-a, 0, a])


def verdict(name, ok, note=""):
    print(f"{name}: {'not killed' if ok else 'KILLED'} {note}")


print("FCL run 2, mpmath", mp.dps, "digits\n")
d = mpf(1)

# C1
half = strip(d, d)
worst = abs(half - mpf(1) / 2)
print(f"  C1 strip |x| <= d: {mp.nstr(half, 22)}")
for r in ("0.2", "0.5", "2", "7"):
    x0 = mpf(r) * d
    s = strip(x0, d) + strip(d * d / x0, d)
    print(f"  C1 x0 = {r} d: shares of x0 and d^2/x0 add to {mp.nstr(s, 22)}")
    worst = max(worst, abs(s - 1))
verdict("C1", worst < TOL, f"(largest miss {mp.nstr(worst, 3)})")

# C2
worst = mpf(0)
for r in ("0.3", "1", "1.7320508075688772935274463415", "4", "20"):
    r = mpf(r)
    got, want = disc(r * d, d), 1 - 1 / sqrt(1 + r * r)
    worst = max(worst, abs(got - want))
print(f"  C2 disc at sqrt(3): {mp.nstr(disc(sqrt(3) * d, d), 22)}")
F = lambda r: 1 - 1 / sqrt(1 + r * r)
miss = lambda r: F(r) + F(3 / r) - 1
grid = [mpf(10) ** (mpf(k) / 200) for k in range(-600, 601)]
big = max(grid, key=lambda r: abs(miss(r)))
# the complementing pairing: c -> 1 - c, c = 1/sqrt(1 + r^2)
comp = max(abs(F(r) + F(sqrt(1 / (1 - 1 / sqrt(1 + r * r)) ** 2 - 1)) - 1) for r in (mpf("0.3"), mpf(1), mpf(4)))
print(f"  C2 reciprocal r -> 3/r misses 1 by at most {mp.nstr(abs(miss(big)), 6)} (at r = {mp.nstr(big, 5)}); c -> 1 - c misses by {mp.nstr(comp, 3)}")
verdict("C2", worst < TOL and mpf("0.01") <= abs(miss(big)) <= mpf("0.05"), f"(disc off the formula by {mp.nstr(worst, 3)})")

# C3
third = square(d, d)
shalf = sqrt(1 + sqrt(2))
at = square(shalf * d, d)
ok3 = abs(third - mpf(1) / 3) < mpf(10) ** -12 and abs(at - mpf(1) / 2) < mpf(10) ** -12
w = max(abs(square(mpf(s) * d, d) - 2 / pi * asin(mpf(s) ** 2 / (1 + mpf(s) ** 2))) for s in ("0.4", "1", "3"))
verdict("C3", ok3, f"(square of one thumb each way {mp.nstr(third, 15)}; at s = {mp.nstr(shalf, 8)}: {mp.nstr(at, 15)}; formula off by {mp.nstr(w, 3)})")

# C4: a uniform ball of radius 1 and mass 1, by its shells
mp.dps = 20


def shell_pull(x, rp):
    # pull toward the centre at distance x from a thin shell of radius rp and unit mass
    f = lambda th: (x - rp * cos(th)) * sin(th) / 2 / (x * x + rp * rp - 2 * x * rp * cos(th)) ** mpf("1.5")
    return quad(f, [0, pi / 8, pi / 2, pi])


def ball_pull(x):
    dens = lambda rp: 3 * rp * rp          # mass per unit radius, total 1
    pts = [0, x / 2, x, (x + 1) / 2, 1] if x < 1 else [0, mpf(1) / 2, 1]
    if x < 1:
        # split at rp = x, where a shell's pull jumps from its full value to zero
        inner = quad(lambda rp: dens(rp) * shell_pull(x, rp), [0, x / 2, x * (1 - mpf(10) ** -6)])
        outer = quad(lambda rp: dens(rp) * shell_pull(x, rp), [x * (1 + mpf(10) ** -6), (x + 1) / 2, 1])
        return inner + outer
    return quad(lambda rp: dens(rp) * shell_pull(x, rp), pts)


worst = mpf(0)
for xs in ("0.2", "0.5", "0.9", "1.1", "2", "5"):
    x = mpf(xs)
    got = ball_pull(x)
    want = x if x < 1 else 1 / x ** 2
    print(f"  C4 x = {xs}: pull {mp.nstr(got, 12)} (x inside, 1/x^2 outside: {mp.nstr(want, 12)})")
    worst = max(worst, abs(got - want))
print("  C4 equal pulls at x and x^(-1/2):", ", ".join(f"{a} and {mp.nstr(mpf(a) ** -mpf('0.5'), 6)}" for a in ("0.25", "0.5", "0.81")))
verdict("C4", worst < mpf(10) ** -5 if False else worst < mpf(10) ** -10, f"(largest miss {mp.nstr(worst, 3)}; the gap left at rp = x is 2e-6 of x)")
mp.dps = 30

# C5
k = mpf(7)
ch = [abs(strip(k * mpf("0.5"), k) - strip(mpf("0.5"), 1)), abs(disc(k * 2, k) - disc(2, 1)), abs(square(k * mpf("1.3"), k) - square(mpf("1.3"), 1))]
verdict("C5", max(ch) < TOL, f"(strip, disc, square under x7: {', '.join(mp.nstr(c, 3) for c in ch)}; no share carries M)")
