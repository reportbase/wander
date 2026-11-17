# MRL run 1: laws of systems reading each other. Predictions in plans/mrl-plan.md.
from fractions import Fraction as F
import random
import mpmath as mp

mp.mp.dps = 60
rng = random.Random(20261117)
out = []


def rep(code, ok, msg):
    line = f"{code}: {'not killed' if ok else 'KILLED'}  {msg}"
    print(line)
    out.append(line)


def rq(lo=1, hi=50):
    return F(rng.randint(lo, hi), rng.randint(lo, hi))


def rpt(dim):
    return tuple(F(rng.randint(-60, 60), rng.randint(1, 9)) for _ in range(dim))


def D2(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q))


# readings squared are rational: s_ij^2 = H_j^2 / (t_i^2 D_ij)
def sq(H, t, P, i, j):
    return H[j] ** 2 / (t[i] ** 2 * D2(P[i], P[j]))


# ---------- L1 ----------
ok = True
for trial in range(200):
    dim = rng.choice((2, 3))
    H, t, P = [rq(), rq()], [rq(), rq()], [rpt(dim), rpt(dim)]
    if D2(P[0], P[1]) == 0:
        continue
    prod2 = sq(H, t, P, 0, 1) * sq(H, t, P, 1, 0)                  # (s_01 s_10)^2
    dA, dB = H[1] / t[0], H[0] / t[1]
    if prod2 != (dA * dB) ** 2 / D2(P[0], P[1]) ** 2 or prod2 != (H[0] * H[1] / (t[0] * t[1] * D2(P[0], P[1]))) ** 2:
        ok = False
rep('L1', ok, "200 random pairs (plane and space): (s_ij s_ji)^2 = (d_ij* d_ji* / D_ij)^2 = (H_i H_j/(t_i t_j D_ij))^2 exactly")

# ---------- L2 ----------
def cm(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def w(s):  # (1 + is)/(1 - is) = (1 - s^2 + 2is)/(1 + s^2)
    den = 1 + s * s
    return ((1 - s * s) / den, 2 * s / den)


def oplus(s, a):
    return (s + a) / (1 - s * a)


ok = True
neg = 0
for trial in range(200):
    s = rq(1, 99)
    a = 1 / s
    if cm(w(s), w(a)) != (F(-1), F(0)):
        ok = False
    a2 = rq(1, 99)
    while s * a2 == 1:
        a2 = rq(1, 99)
    if cm(w(s), w(a2)) != w(oplus(s, a2)):
        ok = False
    if cm(w(s), w(a2)) == (F(-1), F(0)):
        neg += 1
rep('L2', ok and neg == 0, f"w(s)w(1/s) = -1 exactly on 200 pairs; w(s)w(a) = w(s (+) a) exactly on 200 pairs with sa != 1, of which {neg} gave -1")

# ---------- L2b ----------
a, b = mp.mpf(0), mp.mpf(3)
fs = {'x/2': lambda x: x / 2, 'tanh': mp.tanh, 'x^3/3': lambda x: x ** 3 / 3, 'atan': mp.atan}
ok = True
rows = []
for name, f in fs.items():
    g = lambda x, f=f: f(a - x) + f(b - x)
    grid = [mp.mpf(-10) + k * mp.mpf(23) / 4000 for k in range(4001)]
    crossings = sum(1 for u, v in zip(grid, grid[1:]) if g(u) * g(v) < 0 or g(u) == 0)
    x0 = mp.findroot(g, mp.mpf(1))
    sA, sB = mp.e ** (a - x0), mp.e ** (b - x0)
    wA = (1 + 1j * sA) / (1 - 1j * sA)
    wB = (1 + 1j * sB) / (1 - 1j * sB)
    err = abs(wA * wB + 1)
    rows.append((name, crossings, x0, err))
    ok = ok and crossings == 1 and abs(x0 - (a + b) / 2) < mp.mpf(10) ** -50 and err < mp.mpf(10) ** -50
sg = lambda x: mp.sign(a - x) + mp.sign(b - x)
inside = sum(1 for k in range(1, 300) if sg(a + (b - a) * k / 300) == 0)
outside = sum(1 for x in (mp.mpf(-5), mp.mpf(-0.1), mp.mpf(3.1), mp.mpf(8)) if sg(x) == 0)
ok = ok and inside == 299 and outside == 0
rep('L2b', ok, "; ".join(f"f={n}: {c} rest point, at {mp.nstr(x0, 12)}, |w_A w_B + 1| {mp.nstr(e, 3)}" for n, c, x0, e in rows)
    + f"; f=sign: rest at {inside} of 299 points between the corners, {outside} of 4 outside")

# ---------- L3 ----------
ok = True
for dim in (2, 3):
    for L in (3, 4, 5):
        for trial in range(40):
            H = [rq() for _ in range(L)]
            t = [rq() for _ in range(L)]
            P = [rpt(dim) for _ in range(L)]
            if any(D2(P[i], P[(i + 1) % L]) == 0 for i in range(L)):
                continue
            prod = F(1)
            for i in range(L):
                j = (i + 1) % L
                r2 = sq(H, t, P, i, j) / sq(H, t, P, j, i)         # (s_ij/s_ji)^2
                if r2 != (H[j] * t[j] / (H[i] * t[i])) ** 2:
                    ok = False
                prod *= r2
            if prod != 1:
                ok = False
rep('L3', ok, "(s_ij/s_ji)^2 = (H_j t_j/(H_i t_i))^2 exactly; the product round every loop of 3, 4, 5 systems 1 exactly, plane and space, 40 loops each")

# ---------- L4 ----------
def rank(M):
    M = [row[:] for row in M]
    r = 0
    cols = len(M[0])
    for c in range(cols):
        p = next((k for k in range(r, len(M)) if M[k][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        for k in range(len(M)):
            if k != r and M[k][c] != 0:
                fct = M[k][c] / M[r][c]
                M[k] = [M[k][j] - fct * M[r][j] for j in range(cols)]
        r += 1
    return r


ok = True
rows = []
for dim, want in ((2, lambda N: 4 * N - 5), (3, lambda N: 5 * N - 8)):
    for N in (5, 10, 20):
        P = [rpt(dim) for _ in range(N)]
        ncol = 2 * N + dim * N  # ln H (N), ln t (N), coordinates
        J = []
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                row = [F(0)] * ncol
                row[j] += 1                 # d/d ln H_j
                row[N + i] -= 1             # d/d ln t_i
                D = D2(P[i], P[j])
                for c in range(dim):        # -1/2 ln D_ij
                    g = (P[i][c] - P[j][c]) / D
                    row[2 * N + dim * i + c] -= g
                    row[2 * N + dim * j + c] += g
                J.append(row)
        rk = rank(J)
        rows.append((dim, N, len(J), rk, want(N)))
        ok = ok and rk == want(N)
rep('L4', ok, "; ".join(f"{d}D N={N}: {m} readings, rank {r} (predicted {p})" for d, N, m, r, p in rows))

# ---------- L5 ----------
ok = True
for trial in range(50):
    N = 4
    dim = rng.choice((2, 3))
    H = [rq() for _ in range(N)]
    t = [rq() for _ in range(N)]
    P = [rpt(dim) for _ in range(N)]
    k = rq(1, 30)
    Hk = [h * k for h in H]
    Pk = [tuple(c * k for c in p) for p in P]
    for i in range(N):
        for j in range(N):
            if i != j and D2(P[i], P[j]) != 0:
                if sq(H, t, P, i, j) != sq(Hk, t, Pk, i, j):
                    ok = False
    if [Hk[i] * t[i] for i in range(N)] != [k * H[i] * t[i] for i in range(N)]:
        ok = False
rep('L5', ok, "world scaled by random rational k: every reading unchanged exactly (so every product and loop), each q_i = H_i t_i moved by k")

open('runs/mrl/mrl-run1.txt', 'w').write("\n".join(out) + "\n")
