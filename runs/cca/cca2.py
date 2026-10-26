"""CCA run 2: C1′, the amounts cancel, in 60-digit arithmetic (plans/cca-plan.md).

Run from the repository's root: python3 runs/cca/cca2.py
"""
import time

import mpmath as mp
import numpy as np

T0 = time.time()
mp.mp.dps = 60
rng = np.random.default_rng(20261026)


def canon(X, Y):
    """Canonical correlations from the covariances: singular values of Lx⁻¹ Sxy Ly⁻ᵀ."""
    N = X.rows
    def centre(Z):
        m = [mp.fsum(Z[i, j] for i in range(N)) / N for j in range(Z.cols)]
        return mp.matrix([[Z[i, j] - m[j] for j in range(Z.cols)] for i in range(N)])
    X, Y = centre(X), centre(Y)
    Sxx, Syy, Sxy = X.T * X, Y.T * Y, X.T * Y
    Lx, Ly = mp.cholesky(Sxx), mp.cholesky(Syy)
    K = mp.inverse(Lx) * Sxy * mp.inverse(Ly).T
    s = mp.svd_r(K, compute_uv=False)
    return sorted([s[i] for i in range(len(s))], reverse=True)


def mat(a):
    return mp.matrix([[mp.mpf(float(x)) for x in row] for row in a])


worst = mp.mpf(0)
for _ in range(1000):
    N, p, q = int(rng.integers(8, 40)), int(rng.integers(1, 5)), int(rng.integers(1, 5))
    X = rng.standard_normal((N, p)) @ rng.standard_normal((p, p))
    Y = 0.5 * X[:, :1] @ rng.standard_normal((1, q)) + rng.standard_normal((N, q))
    A = rng.standard_normal((p, p)) * 10 ** rng.uniform(-3, 3, (1, p))
    B = rng.standard_normal((q, q)) * 10 ** rng.uniform(-3, 3, (1, q))
    a, b = rng.normal(0, 1e3, (1, p)), rng.normal(0, 1e3, (1, q))
    Xm, Ym, Am, Bm = mat(X), mat(Y), mat(A), mat(B)
    X2 = Xm * Am + mp.matrix([[mp.mpf(float(a[0, j])) for j in range(p)] for _ in range(N)])
    Y2 = Ym * Bm + mp.matrix([[mp.mpf(float(b[0, j])) for j in range(q)] for _ in range(N)])
    r0, r1 = canon(Xm, Ym), canon(X2, Y2)
    worst = max(worst, max(abs(u - v) for u, v in zip(r0, r1)))
ok = worst < mp.mpf(10) ** -40
print(f"C1′ 60 digits, 1,000 datasets, column scales 10⁻³ … 10³, shifts 10³: largest change in any r_i {mp.nstr(worst, 3)}")
print(f"\nC1′: {'not killed' if ok else 'KILLED'}")
print(f"({time.time() - T0:.0f} s)")
