"""PXC run 2: depth along the line of sight, the round error at the corner, and run 1's P4 explained. See
plans/pxc-plan.md, "Run 2: predictions". Same set-up as P4 of pxc.py; numpy only.
"""
import numpy as np
rng = np.random.default_rng(14)
def verdict(ok): return "not killed" if ok else "KILLED"
eps, N = 1e-6, 20000
A, Bp = np.array([-1.0, 0.0]), np.array([1.0, 0.0])                # half-baseline 1
r5 = []; r6 = []; r7 = []
for j in range(-8, 9):
    k = 2.0 ** j; d = 1.0 / k
    ta = np.arctan2(d, 1.0) + rng.normal(0, eps / np.sqrt(2), N)
    tb = np.arctan2(d, -1.0) + rng.normal(0, eps / np.sqrt(2), N)
    ca, sa, cb, sb = np.cos(ta), np.sin(ta), np.cos(tb), np.sin(tb)
    det = -ca * sb + sa * cb
    s = ((Bp[0] - A[0]) * (-sb) - (Bp[1] - A[1]) * (-cb)) / det
    px, py = A[0] + s * ca, A[1] + s * sa
    sy, sx = np.sqrt(np.mean((py - d) ** 2)), np.sqrt(np.mean(px ** 2))
    r5.append(sy / d / (eps * np.cosh(np.log(k))))
    r6.append((sy / sx) / d)
    SY = (1 + d * d) * eps / 2; SX = SY / d
    r7.append(np.sqrt(np.mean((np.hypot(px, py) / d - 1) ** 2)) / (np.sqrt(SY ** 2 + 3 * SX ** 4 / (4 * d * d)) / d))
fmt = lambda r: ", ".join(f"2^{j}: {x:.3f}" for j, x in zip(range(-8, 9), r))
ok5 = max(abs(x - 1) for x in r5) <= 0.03
ok6 = max(abs(x - 1) for x in r6) <= 0.03
ok7 = max(abs(x - 1) for x in r7) <= 0.03
print("P5 depth's rms relative error over eps*cosh(ln k):", fmt(r5), "->", verdict(ok5))
print("P6 (sigma along the line of sight / sigma along the baseline) over d:", fmt(r6), "->", verdict(ok6))
print("P7 distance from the middle over the second-order prediction:", fmt(r7), "->", verdict(ok7))
