# MRL run 2: the rank with the conformal maps counted (L4'), and the special conformal null vector (L4'').
# Predictions in plans/mrl-plan.md, committed before this run.
from fractions import Fraction as F
import random
import sys
sys.path.insert(0, 'runs/mrl')
rng = random.Random(20261118)
out = []


def rep(code, ok, msg):
    line = f"{code}: {'not killed' if ok else 'KILLED'}  {msg}"
    print(line)
    out.append(line)


def rpt(dim):
    return tuple(F(rng.randint(-60, 60), rng.randint(1, 9)) for _ in range(dim))


def D2(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q))


def jac(P, dim):
    N = len(P)
    ncol = 2 * N + dim * N
    J = []
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            row = [F(0)] * ncol
            row[j] += 1
            row[N + i] -= 1
            D = D2(P[i], P[j])
            for c in range(dim):
                g = (P[i][c] - P[j][c]) / D
                row[2 * N + dim * i + c] -= g
                row[2 * N + dim * j + c] += g
            J.append(row)
    return J


def rank(M):
    M = [row[:] for row in M]
    r = 0
    for c in range(len(M[0])):
        p = next((k for k in range(r, len(M)) if M[k][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        for k in range(len(M)):
            if k != r and M[k][c] != 0:
                f = M[k][c] / M[r][c]
                M[k] = [M[k][j] - f * M[r][j] for j in range(len(M[0]))]
        r += 1
    return r


ok = True
rows = []
for dim, want in ((2, lambda N: 4 * N - 7), (3, lambda N: 5 * N - 11)):
    for N in (5, 10, 20):
        P = [rpt(dim) for _ in range(N)]
        rk = rank(jac(P, dim))
        rows.append((dim, N, rk, want(N)))
        ok = ok and rk == want(N)
rep("L4'", ok, "; ".join(f"{d}D N={N}: rank {r} (predicted {p})" for d, N, r, p in rows))


def null_test(P, dim, b, coef):
    N = len(P)
    J = jac(P, dim)
    v = [F(0)] * (2 * N + dim * N)
    for i in range(N):
        bx = sum(b[c] * P[i][c] for c in range(dim))
        xx = sum(P[i][c] ** 2 for c in range(dim))
        v[i] = coef * bx
        v[N + i] = -coef * bx
        for c in range(dim):
            v[2 * N + dim * i + c] = 2 * bx * P[i][c] - xx * b[c]
    return all(sum(r[k] * v[k] for k in range(len(v))) == 0 for r in J)


res = {}
for coef in (F(2), F(-2), F(1), F(-1)):
    good = True
    for dim in (2, 3):
        P = [rpt(dim) for _ in range(8)]
        for ax in range(dim):
            b = tuple(F(int(c == ax)) for c in range(dim))
            good = good and null_test(P, dim, b, coef)
    res[coef] = good
rep("L4''", res[F(2)] or res[F(-2)],
    f"special conformal map with dlnH = coef*(b.x), dlnt = -coef*(b.x): null exactly for coef 2: {res[F(2)]}, -2: {res[F(-2)]}"
    f"; post hoc, coef 1: {res[F(1)]}, -1: {res[F(-1)]}")
open('runs/mrl/mrl-run2.txt', 'w').write("\n".join(out) + "\n")
