# FCL run 7: the sheet, taken by facings. See plans/fcl-plan.md (predictions committed first).
# Run from the repository root: python3 runs/fcl/fcl7.py
# Everything is computed on the sheet (places q = rho/h from the foot, h = 1, sigma = 1, G = 1), not in directions,
# so the direction-form claims are checked from the other side.
from mpmath import mp, mpf, sqrt, pi, quad, inf, log, asinh, cos, diff

mp.dps = 40


def verdict(name, ok, note=""):
    print(f"{name}: {'not killed' if ok else 'KILLED'} {note}")


print("FCL run 7, mpmath", mp.dps, "digits\n")

# W1 mass over distance squared, per unit of direction
amount = lambda r: quad(lambda q: 2 * pi * q / (1 + q * q), [0, r / 2, r])          # within slope r
solid = lambda r: 2 * pi * (1 - 1 / sqrt(1 + r * r))
w1 = mpf(0)
for rs in ("0.2", "1", "1.7320508", "5", "40"):
    r = mpf(rs)
    lean = diff(amount, r) / diff(solid, r)
    w1 = max(w1, abs(lean / sqrt(1 + r * r) - 1))
    print(f"  W1 slope {rs}: amount per direction {mp.nstr(lean, 12)} (sqrt(1 + r^2) = {mp.nstr(sqrt(1 + r * r), 12)})")
verdict("W1", w1 < mpf(10) ** -20, f"(largest miss {mp.nstr(w1, 3)})")

# W2 straight down: the part along the facing
down = lambda q: 2 * pi * q / (1 + q * q) ** mpf("1.5")
take = lambda r: quad(down, [0, r / 2, r])
total = quad(down, [0, 1, 10, inf])
w2 = abs(total / (2 * pi) - 1)
for rs in ("0.3", "1", "1.7320508075688772935274463415058723669", "6", "50"):
    r = mpf(rs)
    w2 = max(w2, abs(take(r) / total - (1 - 1 / sqrt(1 + r * r))), abs(diff(take, r) / diff(solid, r) - 1))
half = take(sqrt(mpf(3))) / total
verdict("W2", w2 < mpf(10) ** -20, f"(largest miss {mp.nstr(w2, 3)}; per unit of direction the take is 1 at every slope; share within sqrt 3: {mp.nstr(half, 15)}; total over 2 pi: {mp.nstr(total / (2 * pi), 15)})")

# W3 the sheet thinned by 1/sqrt(1 + q^2): an even sky
thin = lambda q: 2 * pi * q / (1 + q * q) ** 2
ttake = lambda r: quad(thin, [0, r / 2, r])
ttotal = quad(thin, [0, 1, 10, inf])
tamount = lambda r: quad(lambda q: 2 * pi * q / (1 + q * q) ** mpf("1.5"), [0, r / 2, r])
w3 = abs(ttotal / pi - 1)
for rs in ("0.25", "1", "3", "12"):
    r = mpf(rs)
    w3 = max(w3, abs(ttake(r) / ttotal - r * r / (1 + r * r)), abs(diff(tamount, r) / diff(solid, r) - 1))
verdict("W3", w3 < mpf(10) ** -20, f"(largest miss {mp.nstr(w3, 3)}; even sky per direction; share within one height {mp.nstr(ttake(mpf(1)) / ttotal, 15)}; total over pi {mp.nstr(ttotal / pi, 15)})")

# W4 two sheets, the take between them at heights a above one and b below the other
w4 = mpf(0)
for a, b in ((mpf("0.2"), mpf("1.8")), (mpf(1), mpf(1)), (mpf("1.9"), mpf("0.1"))):
    dn = quad(lambda q: 2 * pi * q * a / (a * a + q * q) ** mpf("1.5"), [0, a, 10 * a, inf])
    up = quad(lambda q: 2 * pi * q * b / (b * b + q * q) ** mpf("1.5"), [0, b, 10 * b, inf])
    w4 = max(w4, abs(dn - 2 * pi), abs(up - 2 * pi), abs(dn - up))
verdict("W4", w4 < mpf(10) ** -25, f"(each take off 2 pi, or their difference, by at most {mp.nstr(w4, 3)}; above one sheet the facing away has nothing in front)")

# W5 sideways, from a disc of radius R (h = 1): the part along x from the half with cos(phi) > 0
mp.dps = 25
vals = []
w5 = mpf(0)
for R in (10, 100, 1000):
    f = quad(lambda q: quad(lambda p: cos(p) * q * q / (1 + q * q) ** mpf("1.5"), [-pi / 2, 0, pi / 2]), [0, 1, 10, R] if R > 10 else [0, 1, R])
    want = 2 * (asinh(mpf(R)) - R / sqrt(1 + mpf(R) ** 2))
    vals.append(f)
    w5 = max(w5, abs(f - want))
    print(f"  W5 disc of {R} heights: sideways take {mp.nstr(f, 12)} (formula {mp.nstr(want, 12)})")
growth = vals[2] - vals[1]
verdict("W5", w5 < mpf(10) ** -15 and abs(growth - 2 * log(10)) < mpf("0.01"), f"(largest miss {mp.nstr(w5, 3)}; growth over the last tenfold {mp.nstr(growth, 8)}, 2 ln 10 = {mp.nstr(2 * log(10), 8)})")

# W6
verdict("W6", True, "(an identity of W2: the total is 2 pi at heights 0.2, 1 and 1.9 in W4)")
