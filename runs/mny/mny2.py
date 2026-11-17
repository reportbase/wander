# MNY run 2: B1' only (medians within 4 standard errors). Predictions in plans/mny-plan.md.
import numpy as np
out = []
def rep(code, ok, msg):
    line = f"{code}: {'not killed' if ok else 'KILLED'}  {msg}"
    print(line); out.append(line)
# ---------- Part B: the heat among many ----------
def chain(N, seed):
    from fractions import Fraction as F
    H = [F(2 + (7 * i + seed) % 5, 1 + (3 * i + seed) % 4) for i in range(N)]
    t = [F(1, 10 + (5 * i + 2 * seed) % 7) for i in range(N)]
    R = np.array([float(H[i + 1] / t[i]) for i in range(N - 1)])
    L = np.array([float(H[i - 1] / t[i]) for i in range(1, N)])
    return R, L


def matrices(N):
    # gaps g (N-1); reads: right read of gap i by observer i (noise index i), left read of gap i by observer i+1 (index N-1+i)
    n = N - 1
    A = np.zeros((n, n)); B = np.zeros((n, 2 * n))
    # dp_i = 1/2 (g_i + xR_i - R_i) [i<N-1]  - 1/2 (g_{i-1} + xL_{i-1} - L_{i-1}) [i>0];   dg_i = dp_{i+1} - dp_i
    def dp_coeffs(i):
        cg = np.zeros(n); cx = np.zeros(2 * n)
        if i < N - 1: cg[i] += 0.5; cx[i] += 0.5
        if i > 0: cg[i - 1] -= 0.5; cx[n + i - 1] -= 0.5
        return cg, cx
    for gi in range(n):
        a1, b1 = dp_coeffs(gi + 1); a0, b0 = dp_coeffs(gi)
        A[gi] = a1 - a0; B[gi] = b1 - b0
    return A, B


def const(N, R, L):
    n = N - 1; c = np.zeros(n)
    def dpc(i):
        v = 0.0
        if i < N - 1: v -= 0.5 * R[i]
        if i > 0: v += 0.5 * L[i - 1]
        return v
    for gi in range(n): c[gi] = dpc(gi + 1) - dpc(gi)
    return c


def scale_formula(M, Bs, kmax=200000):
    tot = np.zeros(M.shape[0]); P = Bs.copy()
    for k in range(kmax):
        add = np.abs(P).sum(axis=1); tot += add
        if add.max() < 1e-15: break
        P = M @ P
    return tot


gam = 0.05; nrng = np.random.default_rng(20261118)
ok = True; msgs = []; b3 = []
for N, seed in ((5, 1), (8, 2)):
    R, L = chain(N, seed)
    A, B = matrices(N); c = const(N, R, L)
    lam = np.linalg.eigvals(A).real; crit = 2 / max(-lam)
    for frac in (0.1, 0.5, 0.9):
        al = frac * crit
        M = np.eye(N - 1) + al * A; Bs = al * B; cs = al * c
        gstar = np.linalg.solve(np.eye(N - 1) - M, cs)
        pred = gam * scale_formula(M, Bs)
        S = 100000
        g = np.tile(gstar, (S, 1))
        for n in range(600):
            xi = nrng.standard_cauchy((S, 2 * (N - 1)))
            g = g @ M.T + cs + gam * xi @ Bs.T
        q1, med, q3 = np.quantile(g, [0.25, 0.5, 0.75], axis=0)
        hiqr = (q3 - q1) / 2
        relerr = np.max(np.abs(hiqr / pred - 1)); mederr = np.max(np.abs(med - gstar)) / gam
        # partial sums to 600 against the full: how much of the scale 600 rounds reach
        part = gam * scale_formula(M, Bs, kmax=600)
        se = np.pi * pred / (2 * np.sqrt(S)); zs = np.max(np.abs(med - gstar) / se)
        ok = ok and relerr < 0.03 and zs < 4
        msgs.append(f"N={N} at {frac} of 2/lambda_max: medians off by {mederr:.4f} gamma ({zs:.2f} standard errors), half-IQR off formula by {100 * relerr:.2f}% "
                    f"(600 rounds reach {100 * np.min(part / pred):.2f}% of it)")
        b3.append(f"N={N}, {frac}: half-widths / gamma {np.round(pred / gam, 3).tolist()}")
rep("B1'", ok, "; ".join(msgs))
open('runs/mny/mny-run2.txt', 'w').write("\n".join(out) + "\n")
