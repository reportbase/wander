# FCL run 4b: the count of balance points at small m. See plans/fcl-plan.md (prediction M1' committed first).
# Run from the repository root: python3 runs/fcl/fcl4b.py
import math
import random
from mpmath import mp, mpf, sqrt, findroot, cos, sin, pi

mp.dps = 30
R = random.Random(20261125)


def acc(x, y, M1, M2):
    a3 = (x * x + y * y) ** mpf("1.5")
    b3 = ((x - 1) ** 2 + y * y) ** mpf("1.5")
    return (-M1 * x / a3 - M2 * (x - 1) / b3 + (x - M2), -M1 * y / a3 - M2 * y / b3 + y)


ok = True
for m in (1e-6, 1e-9):
    # (a) sign changes along the line, in floats on a fine grid, skipping the two poles
    def f(x):
        return -(1 - m) * x / abs(x) ** 3 - m * (x - 1) / abs(x - 1) ** 3 + (x - m)
    n, changes, prev = 200000, 0, None
    for i in range(n + 1):
        x = -3 + 7 * i / n + 1.234e-7
        v = f(x)
        if prev is not None and (v > 0) != (prev > 0):
            # a jump through a pole is not a zero: both sides are huge there
            if min(abs(v), abs(prev)) < 1e3:
                changes += 1
        prev = v
    M2 = mpf(m)
    M1 = 1 - M2
    found = []
    for _ in range(400):
        r, t = 1 + R.uniform(-0.3, 0.3), R.uniform(0, 2 * math.pi)
        try:
            s = findroot(lambda x, y: acc(x, y, M1, M2), (mpf(r * math.cos(t)), mpf(r * math.sin(t))), tol=mpf(10) ** -24, maxsteps=400)
        except Exception:
            continue
        x, y = s[0], s[1]
        ax, ay = acc(x, y, M1, M2)
        if abs(ax) + abs(ay) > mpf(10) ** -20 or abs(y) < mpf(10) ** -8:
            continue
        if not any(abs(x - u) + abs(y - v) < mpf(10) ** -8 for u, v in found):
            found.append((x, y))
    w = max([abs(sqrt(x * x + y * y) - 1) + abs(sqrt((x - 1) ** 2 + y * y) - 1) for x, y in found] or [mpf(1)])
    print(f"  m = {m}: {changes} sign changes on the line; {len(found)} points off the line, a and b off D by {mp.nstr(w, 3)}")
    ok = ok and changes == 3 and len(found) == 2 and w < mpf(10) ** -20
print("M1':", "not killed" if ok else "KILLED")
