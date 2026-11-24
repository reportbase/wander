# FCL run 4: the pair in orbit. See plans/fcl-plan.md (predictions committed first).
# Run from the repository root: python3 runs/fcl/fcl4.py
import random
from mpmath import mp, mpf, sqrt, findroot, log

mp.dps = 30
R = random.Random(20261124)


def rnd(a, b):
    return mpf(R.randrange(10**12)) / 10**12 * (b - a) + a


def acc(x, y, M1, M2, D=mpf(1), w2=None):
    # net acceleration at rest in the turning frame; M1 at (0,0), M2 at (D,0), centre of mass at (D*M2/(M1+M2), 0)
    if w2 is None:
        w2 = (M1 + M2) / D**3
    cx = D * M2 / (M1 + M2)
    a3 = (x * x + y * y) ** mpf("1.5")
    b3 = ((x - D) ** 2 + y * y) ** mpf("1.5")
    return (-M1 * x / a3 - M2 * (x - D) / b3 + w2 * (x - cx), -M1 * y / a3 - M2 * y / b3 + w2 * y)


def line_points(M1, M2, D=mpf(1), w2=None):
    f = lambda x: acc(x, mpf(0), M1, M2, D, w2)[0]
    m = M2 / (M1 + M2)
    rh = (m / 3) ** (mpf(1) / 3) * D
    inner = findroot(f, (D - rh * mpf("1.3"), D - rh * mpf("0.5")), solver="anderson", tol=mpf(10) ** -27)
    outer = findroot(f, (D + rh * mpf("0.5"), D + rh * mpf("1.5")), solver="anderson", tol=mpf(10) ** -27)
    far = findroot(f, (-D * mpf("1.3"), -D * mpf("0.5")), solver="anderson", tol=mpf(10) ** -27)
    return inner, outer, far


def verdict(name, ok, note=""):
    print(f"{name}: {'not killed' if ok else 'KILLED'} {note}")


print("FCL run 4, mpmath", mp.dps, "digits\n")
MS = [mpf(1) / 2, mpf("0.2"), mpf("0.01"), mpf(10) ** -3, mpf(10) ** -6]

# M1 count, M2 the off-line pair
counts, w2 = [], mpf(0)
for m in MS:
    M1, M2 = 1 - m, m
    found = []
    for _ in range(120):
        p0 = (rnd(-2, 2.5), rnd(-2, 2))
        try:
            s = findroot(lambda x, y: acc(x, y, M1, M2), p0, tol=mpf(10) ** -24, maxsteps=80)
        except Exception:
            continue
        x, y = s[0], s[1]
        ax, ay = acc(x, y, M1, M2)
        if abs(ax) + abs(ay) > mpf(10) ** -18 or abs(x) + abs(y) > 50:
            continue
        if not any(abs(x - u) + abs(y - v) < mpf(10) ** -8 for u, v in found):
            found.append((x, y))
    counts.append(len(found))
    off = [(x, y) for x, y in found if abs(y) > mpf(10) ** -8]
    for x, y in off:
        a, b = sqrt(x * x + y * y), sqrt((x - 1) ** 2 + y * y)
        w2 = max(w2, abs(a - 1), abs(b - 1))
    print(f"  M1 m = {mp.nstr(m, 3)}: {len(found)} balance points, {len(off)} off the line; on the line at x = {', '.join(mp.nstr(x, 8) for x, y in sorted(found) if abs(y) <= mpf(10) ** -8)}")
verdict("M1", all(c == 5 for c in counts), f"(counts {counts})")
verdict("M2", w2 < mpf(10) ** -25 and w2 == w2, f"(a and b off D by at most {mp.nstr(w2, 3)})")

# M3
ms = [mpf(10) ** -k for k in range(6, 13)]
ds = []
for m in ms:
    inner, outer, far = line_points(1 - m, m)
    ds.append(1 - inner)
lx, ly = [log(m) for m in ms], [log(d) for d in ds]
n = len(ms)
mx, my = sum(lx) / n, sum(ly) / n
sl = sum((a - mx) * (b - my) for a, b in zip(lx, ly)) / sum((a - mx) ** 2 for a in lx)
m9 = mpf(10) ** -9
i9, o9, f9 = line_points(1 - m9, m9)
rh9 = (m9 / 3) ** (mpf(1) / 3)
r9 = (1 - i9) / rh9
print(f"  M3 slope {mp.nstr(sl, 8)}; at m = 1e-9 the distance is {mp.nstr(1 - i9, 10)}, over (m/3)^(1/3): {mp.nstr(r9, 10)}; at rest it stood at {mp.nstr(1 / (1 + sqrt((1 - m9) / m9)), 6)}")
verdict("M3", abs(sl - mpf(1) / 3) < mpf("0.005") and abs(r9 - 1) < mpf("0.01"))

# M4
a4 = ((o9 - 1) - (1 - i9)) / rh9**2
m6 = mpf(10) ** -6
i6, o6, f6 = line_points(1 - m6, m6)
b4 = (1 - (-f6)) / m6
print(f"  M4 (a) (outer - inner)/r_H^2 at m = 1e-9: {mp.nstr(a4, 10)} (predicted 2/3); (b) (1 - distance)/m at m = 1e-6: {mp.nstr(b4, 10)} (predicted 7/12 = 0.583333)")
verdict("M4", abs(a4 - mpf(2) / 3) < mpf("0.01") and abs(b4 - mpf(7) / 12) < mpf("0.001"))

# M5
ih, oh, fh = line_points(mpf(1) / 2, mpf(1) / 2)
verdict("M5", abs(ih - mpf(1) / 2) < mpf(10) ** -25, f"(the point between at {mp.nstr(ih, 20)})")

# M6
k = mpf(7)
worst, moved = mpf(0), []
for m in (mpf("0.2"), mpf("0.01")):
    base = line_points(1 - m, m)
    big = line_points(1 - m, m, D=k)
    heavy = line_points(k * (1 - m), k * m)
    worst = max(worst, max(abs(b / k - a) for a, b in zip(base, big)), max(abs(b - a) for a, b in zip(base, heavy)))
    # the off-line pair under the same two scalings
    for (M1, M2, DD) in ((1 - m, m, k), (k * (1 - m), k * m, mpf(1))):
        s = findroot(lambda x, y: acc(x, y, M1, M2, DD), (DD / 2, DD * mpf("0.85")), tol=mpf(10) ** -24)
        worst = max(worst, abs(sqrt(s[0] ** 2 + s[1] ** 2) / DD - 1), abs(sqrt((s[0] - DD) ** 2 + s[1] ** 2) / DD - 1))
    f = lambda x: acc(x, mpf(0), 1 - m, m, mpf(1), mpf(2))[0]
    hand = findroot(f, (mpf("0.3"), mpf("0.95")), solver="anderson", tol=mpf(10) ** -27)
    moved.append(abs(hand - base[0]))
verdict("M6", worst < mpf(10) ** -20 and min(moved) > mpf("0.01"),
        f"(largest move under either scaling {mp.nstr(worst, 3)}; rate doubled by hand moves the inner point by {', '.join(mp.nstr(v, 4) for v in moved)})")
