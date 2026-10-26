"""CCA: canonical correlation followed to its conclusion (plans/cca-plan.md, predictions C1–C7).

Run from the repository's root: python3 runs/cca/cca.py
"""
import math
import time

import numpy as np
from scipy import stats

T0 = time.time()
rng = np.random.default_rng(20261026)
verdict = {}
pi = math.pi
# GRS run 3's exact law of the number of angles inside the corner, n = 2k (j = 0 … k)
LAW = {
    1: [1 / 2, 1 / 2],
    2: [1 / 2 - pi / 8, pi / 4, 1 / 2 - pi / 8],
    3: [(pi - 3) / (4 * pi), (pi + 3) / (4 * pi), (pi + 3) / (4 * pi), (pi - 3) / (4 * pi)],
    4: [19 / 256 - 3 * pi / 128, 3 * pi / 64, 109 / 128 - 3 * pi / 64, 3 * pi / 64, 19 / 256 - 3 * pi / 128],
}


def say(*a):
    print(*a, flush=True)


def canon(X, Y):
    """Sample canonical correlations, the textbook way: centre, QR each block, singular values of QxᵀQy.
    X (..., N, p), Y (..., N, q); returns (..., min(p, q)) in decreasing order."""
    X = X - X.mean(axis=-2, keepdims=True)
    Y = Y - Y.mean(axis=-2, keepdims=True)
    Qx, _ = np.linalg.qr(X)
    Qy, _ = np.linalg.qr(Y)
    return np.linalg.svd(np.swapaxes(Qx, -1, -2) @ Qy, compute_uv=False)


def spread_cov(d, rng, span=1e4):
    """A covariance with eigenvalues spread over `span`, in a random orientation."""
    Q, _ = np.linalg.qr(rng.standard_normal((d, d)))
    ev = np.logspace(0, math.log10(span), d)
    return (Q * ev) @ Q.T


def draw_h0(M, N, p, q, Sx=None, Sy=None):
    X = rng.standard_normal((M, N, p))
    Y = rng.standard_normal((M, N, q))
    if Sx is not None:
        X = X @ np.linalg.cholesky(Sx).T
    if Sy is not None:
        Y = Y @ np.linalg.cholesky(Sy).T
    return X, Y


def se_ok(freq, p, M, tag):
    z = (freq - p) / math.sqrt(max(p * (1 - p), 1e-12) / M)
    say(f"    {tag}: exact {p:.6f}, drawn {freq:.6f}, z {z:+.2f}")
    return abs(z) < 4


# ---------------------------------------------------------------- C1: the amounts cancel
worst = 0.0
for _ in range(1000):
    N, p, q = rng.integers(8, 40), rng.integers(1, 5), rng.integers(1, 5)
    X = rng.standard_normal((N, p)) @ rng.standard_normal((p, p))
    Y = 0.5 * X[:, :1] @ rng.standard_normal((1, q)) + rng.standard_normal((N, q))
    A = rng.standard_normal((p, p)) * 10 ** rng.uniform(-3, 3, (1, p))
    B = rng.standard_normal((q, q)) * 10 ** rng.uniform(-3, 3, (1, q))
    r0 = canon(X, Y)
    r1 = canon(X @ A + rng.normal(0, 1e3, (1, p)), Y @ B + rng.normal(0, 1e3, (1, q)))
    worst = max(worst, float(np.max(np.abs(r0 - r1))))
verdict["C1"] = worst < 1e-9
say(f"C1  r_i under X ↦ XA + shift, Y ↦ YB + shift (scales 10⁻³ … 10³), 1,000 datasets: largest change {worst:.2e}")

# ---------------------------------------------------------------- C2: no association is the uniform Grassmannian
M = 200_000
c2 = True
for k in (2, 3):
    N = 2 * k + 1
    for name, Sx, Sy in (("identity", None, None), ("spread 10⁴", spread_cov(k, rng), spread_cov(k, rng))):
        r = canon(*draw_h0(M, N, k, k, Sx, Sy))
        inside = (r >= 1 / math.sqrt(2)).sum(axis=1)
        say(f"C2  k = {k}, N = {N}, within-set covariances {name}:")
        for j in range(k + 1):
            c2 &= se_ok(np.mean(inside == j), LAW[k][j], M, f"{j} of {k} with r ≥ 1/√2")
verdict["C2"] = c2

# ---------------------------------------------------------------- C3: pure noise reads as shared variance
c3 = True
for k in (1, 2, 3, 4):
    N = 2 * k + 1
    r = canon(*draw_h0(M, N, k, k))
    c3 &= se_ok(np.mean(r[:, 0] ** 2 >= 0.5), 1 - LAW[k][0], M, f"C3  k = {k}, N = {N}: P(r₁² ≥ ½) under H₀")
verdict["C3"] = c3

# ---------------------------------------------------------------- C4: Wilks' Λ against ∏ r², the exchange
c4 = True
for k in (1, 2, 3, 4):
    N = 2 * k + 1
    r = canon(*draw_h0(M, N, k, k))
    lam, pr = np.prod(1 - r ** 2, axis=1), np.prod(r ** 2, axis=1)
    c4 &= se_ok(np.mean(lam <= pr), 0.5, M, f"C4  N − 1 = 2k = {2 * k}: P(Λ ≤ ∏r²)")
for k, target in ((2, 0.25), (3, 0.228)):
    N = 2 * k + 2
    r = canon(*draw_h0(M, N, k, k))
    lam, pr = np.prod(1 - r ** 2, axis=1), np.prod(r ** 2, axis=1)
    f = np.mean(lam <= pr)
    if k == 2:
        c4 &= se_ok(f, target, M, f"C4  N − 1 = 2k + 1 = {2 * k + 1}: P(Λ ≤ ∏r²)")
    else:  # 0.228 is run 2's Monte Carlo value (±0.0004), not exact: allow its error too
        z = (f - target) / math.sqrt(target * (1 - target) / M + 0.0004 ** 2)
        say(f"    C4  N − 1 = {2 * k + 1}: P(Λ ≤ ∏r²) drawn {f:.5f} against run 2's 0.228, z {z:+.2f}")
        c4 &= abs(z) < 4
verdict["C4"] = c4

# ---------------------------------------------------------------- C5: a forced fit is geometry
c5 = True
for (N, p, q) in ((6, 3, 4), (5, 3, 3), (10, 5, 6), (8, 4, 4)):
    for assoc in (False, True):
        X, Y = draw_h0(2000, N, p, q)
        if assoc:
            Y[..., :1] += 3 * X[..., :1]
        r = canon(X, Y)
        need = max(0, p + q - (N - 1))
        ones = (np.abs(r - 1) < 1e-9).sum(axis=1)
        ok = bool(np.all(ones == need))
        c5 &= ok
        say(f"C5  N = {N}, p = {p}, q = {q}{' with association' if assoc else ''}: r_i = 1 exactly in "
            f"{need} places in {np.mean(ones == need):.4f} of datasets (largest r ≠ 1 kept: "
            f"{np.max(np.where(np.abs(r - 1) < 1e-9, 0, r)):.4f})")
verdict["C5"] = c5


# ---------------------------------------------------------------- C6: association is an angle
def draw_h1(M, N, rho, Ax, By):
    """x = Ax u, y = By w, (u, w) with cov [[I, D], [D, I]], D = diag(rho)."""
    k = len(rho)
    u = rng.standard_normal((M, N, k))
    e = rng.standard_normal((M, N, k))
    rho = np.asarray(rho)
    w = u * rho + e * np.sqrt(1 - rho ** 2)
    return u @ Ax.T, w @ By.T


M6 = 50_000
I2 = np.eye(2)
Ax = np.linalg.cholesky(spread_cov(2, rng)) @ np.linalg.qr(rng.standard_normal((2, 2)))[0]
By = np.linalg.cholesky(spread_cov(2, rng)) @ np.linalg.qr(rng.standard_normal((2, 2)))[0]
ra = canon(*draw_h1(M6, 30, (0.8, 0.3), I2, I2))
rb = canon(*draw_h1(M6, 30, (0.8, 0.3), Ax, By))
rc = canon(*draw_h1(M6, 30, (0.6, 0.3), Ax, By))
p1, p2 = stats.ks_2samp(ra[:, 0], rb[:, 0]).pvalue, stats.ks_2samp(ra[:, 1], rb[:, 1]).pvalue
p3 = stats.ks_2samp(rb[:, 0], rc[:, 0]).pvalue
verdict["C6"] = p1 > 1e-3 and p2 > 1e-3 and p3 < 1e-6
say(f"C6  ρ = (0.8, 0.3), N = 30: two different (Σ₁₁, Σ₂₂), KS on r₁ p = {p1:.3f}, on r₂ p = {p2:.3f}; "
    f"against ρ = (0.6, 0.3), KS on r₁ p = {p3:.1e}")
say(f"    median r₁ {np.median(ra[:, 0]):.4f} and {np.median(rb[:, 0]):.4f} (ρ₁ = 0.8); {np.median(rc[:, 0]):.4f} (ρ₁ = 0.6)")

# ---------------------------------------------------------------- C7: Bartlett's χ² as the near-horizon chart
N, p, q, M7 = 2001, 3, 4, 20_000
chunks = []
for _ in range(10):
    chunks.append(canon(*draw_h0(M7 // 10, N, p, q)))
r = np.concatenate(chunks)
T = (N - 1) * np.sum(r ** 2, axis=1)
pk = stats.kstest(T, stats.chi2(p * q).cdf).pvalue
theta = np.degrees(np.arccos(r))
verdict["C7"] = pk > 1e-3
say(f"C7  N = {N}, p = {p}, q = {q}: the angles sit at {theta.min():.1f}° … {theta.max():.1f}° (median "
    f"{np.median(theta):.2f}°); (N − 1)·Σ r² against χ²₁₂, KS p = {pk:.3f}, mean {T.mean():.3f} (12)")

say("")
for kk in ["C1", "C2", "C3", "C4", "C5", "C6", "C7"]:
    say(f"{kk}: {'not killed' if verdict[kk] else 'KILLED'}")
say(f"({time.time() - T0:.0f} s)")
