# MNY run 1: many observers reading each other, facings and heat. Predictions in plans/mny-plan.md.
import random
import itertools
import mpmath as mp
import numpy as np

mp.mp.dps = 60
rng = random.Random(20261117)
out = []
TOL = mp.mpf(10) ** -40


def rep(code, ok, msg):
    line = f"{code}: {'not killed' if ok else 'KILLED'}  {msg}"
    print(line)
    out.append(line)


def unit(v): return v / mp.norm(v)
def dot(a, b): return (a.T * b)[0]
def cross(a, b): return mp.matrix([a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]])


def rand_unit():
    while True:
        v = mp.matrix([mp.mpf(rng.gauss(0, 1)) for _ in range(3)])
        if mp.norm(v) > 0.1:
            return unit(v)


def frame(P): return unit(cross(P, rand_unit()))


def bearing(Pi, ei, Pj):
    t = Pj - (dot(Pi, Pj) / dot(Pi, Pi)) * Pi
    return mp.atan2(dot(t, cross(Pi, ei) / mp.norm(Pi)), dot(t, ei))


def wrap(x):
    x = mp.fmod(x + mp.pi, 2 * mp.pi)
    if x < 0:
        x += 2 * mp.pi
    return x - mp.pi


def r_edge(P, e, i, j):
    return wrap(bearing(P[i], e[i], P[j]) - bearing(P[j], e[j], P[i]) + mp.pi)


def excess_tri(A, B, C):
    a = mp.acos(dot(B, C)); b = mp.acos(dot(A, C)); c = mp.acos(dot(A, B))
    s = (a + b + c) / 2
    return 4 * mp.atan(mp.sqrt(mp.tan(s / 2) * mp.tan((s - a) / 2) * mp.tan((s - b) / 2) * mp.tan((s - c) / 2)))


def polygon(N):
    c = rand_unit()
    u = unit(cross(c, rand_unit())); w = cross(c, u)
    rad = mp.mpf(rng.uniform(0.2, 0.9))
    angs = sorted(2 * mp.pi * (k + mp.mpf(rng.uniform(-0.2, 0.2))) / N for k in range(N))
    return [unit(mp.cos(rad) * c + mp.sin(rad) * (mp.cos(t) * u + mp.sin(t) * w)) for t in angs]


def poly_excess(P):
    N = len(P); tot = 0
    for i in range(N):
        A, B, C = P[i - 1], P[i], P[(i + 1) % N]
        t1 = unit(A - dot(B, A) * B); t2 = unit(C - dot(B, C) * B)
        tot += mp.acos(dot(t1, t2))
    return tot - (N - 2) * mp.pi


def modwrap(x): return abs(wrap(x))


# ---------- A1 ----------
worst = 0
for N in (4, 5, 6):
    for trial in range(20):
        P = polygon(N); e = [frame(p) for p in P]
        S = sum(r_edge(P, e, i, (i + 1) % N) for i in range(N))
        E = poly_excess(P)
        worst = max(worst, min(modwrap(S - E), modwrap(S + E)))
rep('A1', worst < TOL, f"60 convex spherical polygons, N = 4, 5, 6: | |loop sum| - excess | (mod 2 pi) at most {mp.nstr(worst, 3)}")

# ---------- A2 ----------
ok = True; msgs = []
for N in (4, 5, 6):
    P = [rand_unit() for _ in range(N)]; e = [frame(p) for p in P]
    r = {}
    for i in range(N):
        for j in range(N):
            if i != j: r[(i, j)] = r_edge(P, e, i, j)
    L = lambda a, b, c: r[(a, b)] + r[(b, c)] + r[(c, a)]
    worst = 0
    for i, j, k in itertools.combinations(range(1, N), 3):
        worst = max(worst, modwrap(L(i, j, k) - (L(0, i, j) + L(0, j, k) + L(0, k, i))))
    edges = list(itertools.combinations(range(N), 2))
    Bm = np.zeros((N, len(edges)))
    for col, (i, j) in enumerate(edges): Bm[i, col] = -1; Bm[j, col] = 1
    dim = len(edges) - np.linalg.matrix_rank(Bm)
    ok = ok and worst < TOL and dim == (N - 1) * (N - 2) // 2
    msgs.append(f"K{N}: cycle space {dim} (predicted {(N - 1) * (N - 2) // 2}), every triangle from those through 1 to {mp.nstr(worst, 3)}")
# K4 containing the centre: a near-regular tetrahedron, turned at random
base = [mp.matrix([1, 1, 1]), mp.matrix([1, -1, -1]), mp.matrix([-1, 1, -1]), mp.matrix([-1, -1, 1])]
ax = rand_unit(); th = mp.mpf(rng.uniform(0, 3))
K = mp.matrix([[0, -ax[2], ax[1]], [ax[2], 0, -ax[0]], [-ax[1], ax[0], 0]])
R = mp.eye(3) + mp.sin(th) * K + (1 - mp.cos(th)) * K * K
P = [unit(R * (b + mp.matrix([mp.mpf(rng.uniform(-0.2, 0.2)) for _ in range(3)]))) for b in base]
e = [frame(p) for p in P]
faces = []
for f in itertools.combinations(range(4), 3):
    a, b, c = f
    if dot(cross(P[b] - P[a], P[c] - P[a]), P[a] + P[b] + P[c]) < 0: b, c = c, b
    faces.append((a, b, c))
exsum = sum(excess_tri(P[a], P[b], P[c]) for a, b, c in faces)
lsum = sum(r_edge(P, e, a, b) + r_edge(P, e, b, c) + r_edge(P, e, c, a) for a, b, c in faces)
ok = ok and abs(exsum - 4 * mp.pi) < TOL and modwrap(lsum) < TOL
msgs.append(f"K4 round the centre: excesses add to 4 pi to {mp.nstr(abs(exsum - 4 * mp.pi), 3)}, outward loop sums to 0 mod 2 pi to {mp.nstr(modwrap(lsum), 3)}")
rep('A2', ok, "; ".join(msgs))


# ---------- A3 ----------
def run_graph(r0, edges, N, alpha, rounds, rule='mutual'):
    phi = [mp.mpf(0)] * N; dev = []
    for n in range(rounds):
        res = [r0[k] + phi[j] - phi[i] for k, (i, j) in enumerate(edges)]
        if rule == 'mutual':
            d = [mp.mpf(0)] * N
            for k, (i, j) in enumerate(edges):
                d[i] += res[k]; d[j] -= res[k]
            d = [alpha * x for x in d]
        else:
            d = [alpha * res[i] for i in range(N)]      # ring: edge i is (i, i+1)
        phi = [phi[i] + d[i] for i in range(N)]
        dev.append((res, phi[:]))
    return dev


def rest_projection(r0, edges, N):
    div = [mp.mpf(0)] * N
    for k, (i, j) in enumerate(edges):
        div[i] += r0[k]; div[j] -= r0[k]
    Lm = mp.zeros(N, N)
    for i, j in edges:
        Lm[i, i] += 1; Lm[j, j] += 1; Lm[i, j] -= 1; Lm[j, i] -= 1
    # L phi = -div... rest: div(r0 + G phi) = 0; div(G phi)_i = sum_j (phi_j - phi_i) over edges, signs as above
    # div(G phi)_i = -(L phi)_i, so L phi = div(r0); pin phi_0 = 0
    A = mp.matrix(N - 1, N - 1); b = mp.matrix(N - 1, 1)
    for a in range(1, N):
        b[a - 1] = div[a]
        for c in range(1, N): A[a - 1, c - 1] = Lm[a, c]
    sol = mp.lu_solve(A, b)
    phi = [mp.mpf(0)] + [sol[a] for a in range(N - 1)]
    return [r0[k] + phi[j] - phi[i] for k, (i, j) in enumerate(edges)], Lm


def loops_of(edges, N):
    # fundamental cycles from a spanning tree rooted at 0 (BFS)
    adj = {i: [] for i in range(N)}
    for k, (i, j) in enumerate(edges): adj[i].append((j, k, 1)); adj[j].append((i, k, -1))
    parent = {0: None}; order = [0]
    for u in order:
        for v, k, s in adj[u]:
            if v not in parent: parent[v] = (u, k, s); order.append(v)
    tree = {parent[v][1] for v in parent if parent[v]}
    def path(v):   # signed edges from root to v
        p = []
        while parent[v]:
            u, k, s = parent[v]; p.append((k, -s)); v = u   # traverse u->v is +s... collect as signed edge from v back
        return p
    cyc = []
    for k, (i, j) in enumerate(edges):
        if k in tree: continue
        c = {}
        for kk, s in path(i): c[kk] = c.get(kk, 0) - s       # root -> i
        for kk, s in path(j): c[kk] = c.get(kk, 0) + s       # j -> root reversed
        c[k] = c.get(k, 0) + 1
        cyc.append(c)
    return cyc


def loopsum(res, c): return sum(s * res[k] for k, s in c.items())


ok = True; msgs = []
for name, N, edges, alpha, world in (("ring 5, sphere", 5, [(i, (i + 1) % 5) for i in range(5)], mp.mpf('0.1'), 'sphere'),
                                     ("K5, sphere", 5, list(itertools.combinations(range(5), 2)), mp.mpf('0.1'), 'sphere'),
                                     ("K5, plane", 5, list(itertools.combinations(range(5), 2)), mp.mpf('0.1'), 'plane')):
    if world == 'sphere':
        P = [rand_unit() for _ in range(N)]; e = [frame(p) for p in P]
        r0 = [r_edge(P, e, i, j) for i, j in edges]
    else:
        th = [mp.mpf(rng.uniform(-0.5, 0.5)) for _ in range(N)]
        r0 = [th[j] - th[i] for i, j in edges]              # the plane's owned turn, exactly f_j/f_i
    rstar, Lm = rest_projection(r0, edges, N)
    lam = sorted(mp.eig(Lm)[0], key=lambda z: mp.re(z))
    nz = [mp.re(l) for l in lam if abs(l) > 1e-30]
    rate = max(abs(1 - alpha * l) for l in nz)
    cyc = loops_of(edges, N)
    h = run_graph(r0, edges, N, alpha, 900)
    loopdrift = max(abs(loopsum(h[n][0], c) - loopsum(r0, c)) for n in (0, 100, 899) for c in cyc)
    resdev = max(abs(h[-1][0][k] - rstar[k]) for k in range(len(edges)))
    stop = max(abs(h[-1][1][i] - h[-2][1][i]) for i in range(N))
    d1 = mp.sqrt(sum((h[150][0][k] - rstar[k]) ** 2 for k in range(len(edges))))
    d2 = mp.sqrt(sum((h[151][0][k] - rstar[k]) ** 2 for k in range(len(edges))))
    measured = d2 / d1
    zero = max(abs(x) for x in rstar)
    good = loopdrift < TOL and resdev < TOL and stop < TOL and abs(measured - rate) < mp.mpf('1e-6')
    if world == 'plane': good = good and zero < TOL
    ok = ok and good
    msgs.append(f"{name}: loop sums kept to {mp.nstr(loopdrift, 3)}, rest = projection to {mp.nstr(resdev, 3)}, frames stopped to "
                f"{mp.nstr(stop, 3)}, rate {mp.nstr(measured, 8)} against {mp.nstr(rate, 8)}, largest resting residual {mp.nstr(zero, 4)}")
rep('A3', ok, "; ".join(msgs))

# ---------- A4 ----------
ok = True; msgs = []
for N in (4, 5, 6):
    edges = [(i, (i + 1) % N) for i in range(N)]
    for world in ('sphere', 'plane'):
        if world == 'sphere':
            P = polygon(N); e = [frame(p) for p in P]
            r0 = [r_edge(P, e, i, j) for i, j in edges]
        else:
            th = [mp.mpf(rng.uniform(-0.5, 0.5)) for _ in range(N)]
            r0 = [th[j] - th[i] for i, j in edges]
        S = sum(r0); alpha = mp.mpf('0.2')
        h = run_graph(r0, edges, N, alpha, 2000, rule='oneway')
        resid = max(abs(x - S / N) for x in h[-1][0])
        drift = max(abs((h[-1][1][i] - h[-2][1][i]) - alpha * S / N) for i in range(N))
        kept = abs(sum(h[-1][0]) - S)
        good = resid < TOL and drift < TOL and kept < TOL
        if world == 'plane': good = good and abs(S) < TOL
        ok = ok and good
        msgs.append(f"N={N} {world}: S {mp.nstr(S, 8)}, residuals at S/N to {mp.nstr(resid, 3)}, frames turning alpha S/N = "
                    f"{mp.nstr(alpha * S / N, 8)} a round to {mp.nstr(drift, 3)}")
rep('A4', ok, "; ".join(msgs))

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


gam = 0.05; nrng = np.random.default_rng(20261117)
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
        ok = ok and relerr < 0.03 and mederr < 0.02
        msgs.append(f"N={N} at {frac} of 2/lambda_max: medians off by {mederr:.4f} gamma, half-IQR off formula by {100 * relerr:.2f}% "
                    f"(600 rounds reach {100 * np.min(part / pred):.2f}% of it)")
        b3.append(f"N={N}, {frac}: half-widths / gamma {np.round(pred / gam, 3).tolist()}")
rep('B1', ok, "; ".join(msgs))

# B2: the pair
A, B = matrices(2)
ok2 = True; rows = []
for al in (0.1, 0.25, 0.5, 0.7, 0.9, 1.3):
    M = np.eye(1) + al * A; Bs = al * B
    f = scale_formula(M, Bs)[0]
    ess = (al) / (1 - abs(1 - al))          # essay 30: alpha + beta = al, each share al/2
    rows.append(f"{al}: {f:.12f} vs {ess:.12f}")
    ok2 = ok2 and abs(f - ess) < 1e-9
rep('B2', ok2, "N = 2, the formula's half-width / gamma against essay 30's (a + b)/(1 - |1 - a - b|): " + "; ".join(rows))
line = "B3 (measured): " + "; ".join(b3)
print(line); out.append(line)

open('runs/mny/mny-run1.txt', 'w').write("\n".join(out) + "\n")
