"""FLR: Fieller's theorem followed to its conclusion (plans/flr-plan.md, predictions F1–F5).

Run from the repository's root: python3 runs/flr/flr.py
"""
import math
import time

import numpy as np
from scipy import stats

T0 = time.time()
rng = np.random.default_rng(20261026)
T2 = 3.8415
T = math.sqrt(T2)
verdict = {}
K = 3600
TH = np.arange(K) * (math.pi / K)          # directions 0° … 179.95°, 90° at index 1800
V90 = K // 2


def say(*a):
    print(*a, flush=True)


def rand_case(M):
    """z = (b, a) uniform in a disc of radius 6; V random with eigenvalues in [0.1, 4] (V ordered (b, a))."""
    r = 6 * np.sqrt(rng.uniform(size=M))
    ph = rng.uniform(0, 2 * math.pi, M)
    z = np.stack([r * np.cos(ph), r * np.sin(ph)], axis=1)
    ev = rng.uniform(0.1, 4, (M, 2))
    al = rng.uniform(0, math.pi, M)
    c, s = np.cos(al), np.sin(al)
    v22 = ev[:, 0] * c * c + ev[:, 1] * s * s          # Var b
    v11 = ev[:, 0] * s * s + ev[:, 1] * c * c          # Var a
    v12 = (ev[:, 0] - ev[:, 1]) * c * s                # Cov(b, a)
    return z[:, 0], z[:, 1], v11, v22, v12


def fieller_quad(b, a, v11, v22, v12):
    """Coefficients of A ρ² + B ρ + C ≤ 0."""
    return b * b - T2 * v22, -2 * (a * b - T2 * v12), a * a - T2 * v11


def in_F_classical(b, a, v11, v22, v12, th):
    """Fieller's set as the classical quadratic in ρ = tan θ; the vertical by its limit b² ≤ t² v₂₂."""
    A, B, C = fieller_quad(b, a, v11, v22, v12)
    rho = np.tan(th)
    val = A[:, None] * rho ** 2 + B[:, None] * rho + C[:, None]
    m = val <= 0
    m[:, V90] = A <= 0
    scale = np.abs(A)[:, None] * rho ** 2 + np.abs(B)[:, None] * np.abs(rho) + np.abs(C)[:, None]
    near = np.abs(val) <= 1e-9 * np.maximum(scale, 1)
    near[:, V90] = np.abs(A) <= 1e-9
    return m, near


def in_F_homog(b, a, v11, v22, v12, th):
    """Homogeneous form, every θ alike: normal w = (−sin θ, cos θ), (wᵀz)² ≤ t² wᵀVw."""
    s, c = np.sin(th), np.cos(th)
    wz = -s * b[:, None] + c * a[:, None]
    wVw = s * s * v22[:, None] - 2 * s * c * v12[:, None] + c * c * v11[:, None]
    return wz ** 2 <= T2 * wVw


def meets_ellipse(b, a, v11, v22, v12, th):
    """Least Mahalanobis distance² from z to the line through home at θ: zᵀV⁻¹z − (uᵀV⁻¹z)²/(uᵀV⁻¹u)."""
    det = v11 * v22 - v12 * v12
    # V = [[v22, v12], [v12, v11]] in the order (b, a); V⁻¹ = [[v11, −v12], [−v12, v22]]/det
    i11, i12, i22 = v11 / det, -v12 / det, v22 / det
    zVz = i11 * b * b + 2 * i12 * b * a + i22 * a * a
    u0, u1 = np.cos(th), np.sin(th)
    uVz = (i11[:, None] * b[:, None] + i12[:, None] * a[:, None]) * u0 + (i12[:, None] * b[:, None] + i22[:, None] * a[:, None]) * u1
    uVu = i11[:, None] * u0 * u0 + 2 * i12[:, None] * u0 * u1 + i22[:, None] * u1 * u1
    d2 = zVz[:, None] - uVz ** 2 / uVu
    return d2 <= T2, np.abs(d2 - T2) <= 1e-9 * T2, zVz


# ---------------------------------------------------------------- F1: Fieller's set is the cone of the ellipse
bad = 0
for _ in range(10):
    b, a, v11, v22, v12 = rand_case(1000)
    m1, near1 = in_F_classical(b, a, v11, v22, v12, TH)
    m2, near2, _ = meets_ellipse(b, a, v11, v22, v12, TH)
    bad += int(np.sum((m1 != m2) & ~near1 & ~near2))
verdict["F1"] = bad == 0
say(f"F1  10,000 cases × 3,600 directions: θ in Fieller's set ≠ its line meets the ellipse in {bad} places "
    f"(away from the boundary)")

# ---------------------------------------------------------------- F2, F3: one arc; the three shapes
counts = {"bounded": 0, "exclusive": 0, "whole": 0}
f2_bad = f3_bad = 0
for _ in range(100):
    b, a, v11, v22, v12 = rand_case(1000)
    m = in_F_homog(b, a, v11, v22, v12, TH)
    rises = np.sum(m & ~np.roll(m, 1, axis=1), axis=1)       # 0 → 1 steps round the circle
    whole_arc = m.all(axis=1)
    empty = ~m.any(axis=1)
    one_arc = (rises == 1) | whole_arc
    A, B, C = fieller_quad(b, a, v11, v22, v12)
    disc = B * B - 4 * A * C
    shape = np.where(A > 0, "bounded", np.where(disc > 0, "exclusive", "whole"))
    f2_bad += int(np.sum(~one_arc | empty))
    has90 = m[:, V90]
    f2_bad += int(np.sum((shape == "bounded") != (~has90)))
    f2_bad += int(np.sum((shape == "exclusive") != (has90 & ~whole_arc)))
    _, _, zVz = meets_ellipse(b, a, v11, v22, v12, TH[:1])
    f3_bad += int(np.sum((shape == "whole") != (zVz <= T2)))
    f3_bad += int(np.sum(whole_arc != (zVz <= T2)))
    for k in counts:
        counts[k] += int(np.sum(shape == k))
verdict["F2"] = f2_bad == 0
verdict["F3"] = f3_bad == 0
say(f"F2  100,000 cases: {counts['bounded']} bounded, {counts['exclusive']} exclusive, {counts['whole']} whole; "
    f"not one arc, or a shape not matching where 90° lies: {f2_bad}")
say(f"F3  the whole line ≠ home inside the ellipse (zᵀV⁻¹z ≤ t²) in {f3_bad} cases")

# ---------------------------------------------------------------- F4: coverage is the direction's
M = 100_000
DIRS = [0, 45, 80, 89, 90]


def se_line(p, M):
    return math.sqrt(p * (1 - p) / M)


rows = []
for deg in DIRS:
    th0 = math.radians(deg)
    mu = 3 * np.array([math.cos(th0), math.sin(th0)])
    z = mu + rng.standard_normal((M, 2))
    b, a = z[:, 0], z[:, 1]
    one, zero = np.ones(M), np.zeros(M)
    fc = in_F_homog(b, a, one, one, zero, np.array([th0]))[:, 0].mean()
    if deg == 90:
        dsl = 0.0
    else:
        rho0 = math.tan(th0)
        rh = a / b
        se = np.sqrt(1 + rh ** 2) / np.abs(b)
        dsl = float(np.mean(np.abs(rho0 - rh) <= T * se))
    thh = np.arctan2(a, b)
    d = (thh - th0 + math.pi / 2) % math.pi - math.pi / 2
    dan = float(np.mean(np.abs(d) <= T / np.hypot(a, b)))
    rows.append((deg, fc, dsl, dan))
pooled = np.mean([r[3] for r in rows])
f4a = all(abs(r[1] - 0.95) < 4 * se_line(0.95, M) for r in rows)
f4b = rows[0][2] >= 0.90 and rows[1][2] >= 0.90 and rows[3][2] <= 0.50 and rows[4][2] == 0.0
f4c = all(abs(r[3] - pooled) < 4 * se_line(pooled, M) for r in rows)
verdict["F4"] = f4a and f4b and f4c
say("F4  V = I, |μ| = 3: coverage of the true direction")
for deg, fc, dsl, dan in rows:
    say(f"    {deg:>2}°: Fieller {fc:.4f}   delta in the slope chart {dsl:.4f}   delta in the angle chart {dan:.4f}")
say(f"    (a) {f4a}, (b) {f4b}, (c) {f4c} (angle chart pooled {pooled:.4f})")

# ---------------------------------------------------------------- F5: no information is the distance from home
pw = stats.ncx2.cdf(T2, 2, 4)
f5a, excl = True, []
for deg in DIRS:
    th0 = math.radians(deg)
    mu = 2 * np.array([math.cos(th0), math.sin(th0)])
    z = mu + rng.standard_normal((M, 2))
    b, a = z[:, 0], z[:, 1]
    r2 = b * b + a * a
    whole = np.mean(r2 <= T2)
    ex = np.mean((b * b < T2) & (r2 > T2))
    zz = (whole - pw) / se_line(pw, M)
    f5a &= abs(zz) < 4
    excl.append(ex)
    say(f"F5  {deg:>2}°, |μ| = 2: whole line {whole:.4f} (noncentral χ²₂ {pw:.4f}, z {zz:+.2f}), exclusive {ex:.4f}")
f5b = all(excl[i + 1] >= excl[i] - 4 * se_line(max(excl[i], 1e-4), M) for i in range(len(excl) - 1))
verdict["F5"] = f5a and f5b

say("")
for kk in ["F1", "F2", "F3", "F4", "F5"]:
    say(f"{kk}: {'not killed' if verdict[kk] else 'KILLED'}")
say(f"({time.time() - T0:.0f} s)")
