# TLP run 1: three systems in a loop, reading each other's directions. Predictions in plans/tlp-plan.md.
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


# Gaussian rationals as pairs
def cm(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def cc(a): return (a[0], -a[1])
def cd(a, b):
    n = b[0] * b[0] + b[1] * b[1]
    return cm(a, cc(b))[0] / n, cm(a, cc(b))[1] / n
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def neg(a): return (-a[0], -a[1])
def rq(lo=-40, hi=40): return F(rng.randint(lo, hi), rng.randint(1, 9))
def rpt(): return (rq(), rq())
def rframe():
    t = F(rng.randint(-30, 30), rng.randint(1, 30))
    d = 1 + t * t
    return ((1 - t * t) / d, 2 * t / d)


def triangle():
    while True:
        P = [rpt() for _ in range(3)]
        x1, y1 = sub(P[1], P[0]); x2, y2 = sub(P[2], P[0])
        if x1 * y2 - x2 * y1 != 0:
            return P


# ---------- T1, T2 ----------
ok1 = ok2 = True
for trial in range(200):
    P = triangle()
    f = [rframe() for _ in range(3)]
    z = {(i, j): cm(sub(P[j], P[i]), cc(f[i])) for i in range(3) for j in range(3) if i != j}
    prod = (F(1), F(0))
    for i in range(3):
        j = (i + 1) % 3
        rho = neg(cd(z[(i, j)], z[(j, i)]))
        if rho != cd(f[j], f[i]) or rho[0] ** 2 + rho[1] ** 2 != 1:
            ok1 = False
        prod = cm(prod, rho)
    if prod != (F(1), F(0)):
        ok1 = False
    ang = (F(1), F(0))
    for i in range(3):
        ang = cm(ang, cd(z[(i, (i - 1) % 3)], z[(i, (i + 1) % 3)]))
    if ang != (F(-1), F(0)):
        ok2 = False
rep('T1', ok1, "200 triangles, rational frames: rho_ij = -z_ij/z_ji = f_j/f_i exactly, |rho| = 1, product round the loop 1 exactly")
rep('T2', ok2, "200 triangles: each system's own angle reading z_(i,i-1)/z_(i,i+1), multiplied over the three, -1 exactly")


# ---------- T3 ----------
def rank_exact(M):
    M = [r[:] for r in M]; r = 0
    for c in range(len(M[0])):
        p = next((k for k in range(r, len(M)) if M[k][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        for k in range(len(M)):
            if k != r and M[k][c] != 0:
                fc = M[k][c] / M[r][c]
                M[k] = [M[k][q] - fc * M[r][q] for q in range(len(M[0]))]
        r += 1
    return r


ranks2 = []
for trial in range(5):
    P = triangle()
    J = []
    for i in range(3):
        for j in range(3):
            if i == j: continue
            row = [F(0)] * 9          # phi_0..2, x0,y0,x1,y1,x2,y2
            row[i] = F(-1)
            wx, wy = sub(P[j], P[i]); n = wx * wx + wy * wy
            # d arg(w) = (wx dwy - wy dwx)/n, w = Pj - Pi
            row[3 + 2 * j] += -wy / n; row[3 + 2 * j + 1] += wx / n
            row[3 + 2 * i] -= -wy / n; row[3 + 2 * i + 1] -= wx / n
            J.append(row)
    ranks2.append(rank_exact(J))


def rot(axis_angle):
    a = mp.matrix(axis_angle); th = mp.norm(a)
    k = a / th
    K = mp.matrix([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    return mp.eye(3) + mp.sin(th) * K + (1 - mp.cos(th)) * K * K


def cross(a, b): return mp.matrix([a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]])


ranks3 = []
for trial in range(5):
    P = [mp.matrix([mp.mpf(rng.randint(-50, 50)) / 7 for _ in range(3)]) for _ in range(3)]
    R = [rot([mp.mpf(rng.random()) * 2 for _ in range(3)]) for _ in range(3)]
    rows = []
    for i in range(3):
        for j in range(3):
            if i == j: continue
            d = P[j] - P[i]; nd = mp.norm(d); u = R[i].T * d / nd
            # two tangent directions at u
            a = cross(u, mp.matrix([1, 0, 0])) if abs(u[0]) < 0.9 else cross(u, mp.matrix([0, 1, 0]))
            a = a / mp.norm(a); b = cross(u, a)
            # du = -omega_i x u (frame), and R_i^T (I - u u^T)/nd (dPj - dPi), in world terms d-projection
            for e in (a, b):
                row = [mp.mpf(0)] * 18     # omega_0..2 (3 each), P_0..2 (3 each)
                for c in range(3):
                    # d(e.u)/d omega_i,c : -(e_c x u) . e ... = -(omega x u).e -> -e.(E_c x u)
                    Ec = mp.matrix([1 if q == c else 0 for q in range(3)])
                    row[3 * i + c] = -(e.T * cross(Ec, u))[0]
                g = R[i] * e / nd           # e^T R_i^T (I - u u^T)/nd, and e is orthogonal to u
                for c in range(3):
                    row[9 + 3 * j + c] += g[c]
                    row[9 + 3 * i + c] -= g[c]
                rows.append(row)
    M = mp.matrix(rows)
    sv = mp.svd_r(M, compute_uv=False)
    ranks3.append((sum(1 for s in sv if s > mp.mpf(10) ** -40), mp.nstr(sorted(sv)[-12], 3) if len(sv) >= 12 else '-'))
rep('T3', all(r == 5 for r in ranks2) and all(r[0] == 11 for r in ranks3),
    f"plane, 6 bearings on 9 variables, exact ranks {ranks2} (predicted 5); space, 12 numbers on 18 variables, ranks "
    f"{[r[0] for r in ranks3]} (predicted 11), the 12th singular value {[r[1] for r in ranks3]}")


# ---------- T4, T5: the sphere ----------
def unit(v): return v / mp.norm(v)
def dot(a, b): return (a.T * b)[0]


def rand_unit():
    while True:
        v = mp.matrix([mp.mpf(rng.gauss(0, 1)) for _ in range(3)])
        if mp.norm(v) > 0.1: return unit(v)


def tangent_frame(Pp):
    return unit(cross(Pp, rand_unit()))


def bearing(Pi, ei, Pj):
    t = Pj - dot(Pi, Pj) * Pi
    return mp.atan2(dot(t, cross(Pi, ei)), dot(t, ei))


def wrap(x):
    x = mp.fmod(x + mp.pi, 2 * mp.pi)
    if x < 0: x += 2 * mp.pi
    return x - mp.pi


def loop_sum(P, e, order=(0, 1, 2)):
    S = 0
    for k in range(3):
        i, j = order[k], order[(k + 1) % 3]
        S += wrap(bearing(P[i], e[i], P[j]) - bearing(P[j], e[j], P[i]) + mp.pi)
    return S


def excess(P):
    a = mp.acos(dot(P[1], P[2])); b = mp.acos(dot(P[0], P[2])); c = mp.acos(dot(P[0], P[1]))
    s = (a + b + c) / 2
    return 4 * mp.atan(mp.sqrt(mp.tan(s / 2) * mp.tan((s - a) / 2) * mp.tan((s - b) / 2) * mp.tan((s - c) / 2)))


worst = 0; flips = True; rows = []
for trial in range(50):
    P = [rand_unit() for _ in range(3)]
    e = [tangent_frame(p) for p in P]
    S = loop_sum(P, e); Sr = loop_sum(P, e, (0, 2, 1)); E = excess(P)
    dev = min(abs(wrap(S - E)), abs(wrap(S + E)))
    worst = max(worst, dev)
    if abs(wrap(S + Sr)) > mp.mpf(10) ** -40: flips = False
    if trial < 3: rows.append((mp.nstr(S, 8), mp.nstr(E, 8)))
# shrinking
Pc = [rand_unit() for _ in range(3)]
centre = unit(Pc[0] + Pc[1] + Pc[2])
shr = []
for k in (mp.mpf(1) / 10, mp.mpf(1) / 100, mp.mpf(1) / 1000, mp.mpf(1) / 10000):
    P = [unit(centre + k * (p - centre)) for p in Pc]
    e = [tangent_frame(p) for p in P]
    shr.append(abs(loop_sum(P, e)) / k ** 2)
conv = abs(shr[-1] - shr[-2]) < abs(shr[1] - shr[0]) / 50
rep('T4', worst < mp.mpf(10) ** -40 and flips and conv,
    f"50 random triangles: | |S| - E | (mod 2 pi) at most {mp.nstr(worst, 3)}; reversed order -S every time {flips}; "
    f"first three S, E: {rows}; shrunk by k, |S|/k^2 = {[mp.nstr(x, 10) for x in shr]}")

# T5: plane S = 0 at every scale (T1 is scale-free: z_ij scale by k, rho unchanged); sphere radius
okp = True
for trial in range(50):
    P = triangle(); f = [rframe() for _ in range(3)]; k = F(rng.randint(1, 50), rng.randint(1, 50))
    Pk = [(p[0] * k, p[1] * k) for p in P]
    for i in range(3):
        j = (i + 1) % 3
        r1 = neg(cd(cm(sub(P[j], P[i]), cc(f[i])), cm(sub(P[i], P[j]), cc(f[j]))))
        r2 = neg(cd(cm(sub(Pk[j], Pk[i]), cc(f[i])), cm(sub(Pk[i], Pk[j]), cc(f[j]))))
        if r1 != r2: okp = False
# a 3-4-5 triangle (area 6) laid on spheres of radius R: excess * R^2 / 6 -> 1
rat = []
for R in (mp.mpf(10), mp.mpf(100), mp.mpf(1000)):
    a, b, c = mp.mpf(3) / R, mp.mpf(4) / R, mp.mpf(5) / R     # central angles opposite sides 3, 4, 5
    s = (a + b + c) / 2
    E = 4 * mp.atan(mp.sqrt(mp.tan(s / 2) * mp.tan((s - a) / 2) * mp.tan((s - b) / 2) * mp.tan((s - c) / 2)))
    rat.append(E * R ** 2 / 6)
# whole world scaled: places on a sphere of radius k, the same directions; bearings use only directions
P = [rand_unit() for _ in range(3)]; e = [tangent_frame(p) for p in P]
S1 = loop_sum(P, e); S2 = loop_sum([7 * p for p in P], e)
okR = abs(rat[-1] - 1) < abs(rat[0] - 1) / 100
rep('T5', okp and okR and abs(S1 - S2) < mp.mpf(10) ** -40,
    f"plane: rho unchanged by 50 random scalings exactly; sides 3, 4, 5 on spheres of radius 10, 100, 1000: E R^2 / area = "
    f"{[mp.nstr(x, 12) for x in rat]}; the world scaled by 7: S {mp.nstr(S1, 12)} unchanged ({mp.nstr(abs(S1 - S2), 3)})")


# ---------- T6, T7: the exchange ----------
def run(r0, alpha, rule, rounds, exact):
    phi = [F(0) if exact else mp.mpf(0)] * 3
    hist = []
    for n in range(rounds):
        e = [r0[i] + phi[(i + 1) % 3] - phi[i] for i in range(3)]
        hist.append((e, phi[:]))
        if rule == 'mutual':
            d = [alpha * (e[i] - e[(i - 1) % 3]) for i in range(3)]
        else:
            d = [alpha * e[i] for i in range(3)]
        phi = [phi[i] + d[i] for i in range(3)]
    return hist


ok6 = ok7 = True
msgs6, msgs7 = [], []
# plane, exact: frames as rational angles, so r0_ij = phi_j - phi_i exactly, S = 0
for alpha in (F(1, 10), F(1, 5), F(1, 2), F(3, 5)):
    th = [rq(), rq(), rq()]
    r0 = [th[(i + 1) % 3] - th[i] for i in range(3)]
    for rule in ('mutual', 'cyclic'):
        h = run(r0, alpha, rule, 30, True)
        fac = (1 - 3 * alpha) ** 2 if rule == 'mutual' else 1 - 3 * alpha + 3 * alpha ** 2
        for n in range(len(h) - 1):
            e0, e1 = h[n][0], h[n + 1][0]
            if sum(e1) != 0: (ok6 if rule == 'mutual' else ok7) and None
            n0 = sum(x * x for x in e0); n1 = sum(x * x for x in e1)
            if n1 != fac * n0 or sum(e1) != 0:
                if rule == 'mutual': ok6 = False
                else: ok7 = False
            if rule == 'mutual' and any(e1[i] != (1 - 3 * alpha) * e0[i] for i in range(3)):
                ok6 = False
        # frames settle in the plane: the last step's change
        last = max(abs(h[-1][1][i] - h[-2][1][i]) for i in range(3))
        (msgs6 if rule == 'mutual' else msgs7).append(f"alpha {alpha}: last frame step {float(last):.2e}")
# stability edge for the mutual rule
diverge = run([F(1), F(2), F(-3)], F(7, 10), 'mutual', 20, True)
ok6 = ok6 and sum(x * x for x in diverge[-1][0]) > sum(x * x for x in diverge[0][0])

# sphere, 50 digits
P = [rand_unit() for _ in range(3)]; ef = [tangent_frame(p) for p in P]
r0 = [wrap(bearing(P[i], ef[i], P[(i + 1) % 3]) - bearing(P[(i + 1) % 3], ef[(i + 1) % 3], P[i]) + mp.pi) for i in range(3)]
S = sum(r0)
alpha = mp.mpf(1) / 5
hm = run(r0, alpha, 'mutual', 400, False)
hc = run(r0, alpha, 'cyclic', 400, False)
em = max(abs(x - S / 3) for x in hm[-1][0]); stopm = max(abs(hm[-1][1][i] - hm[-2][1][i]) for i in range(3))
ec = max(abs(x - S / 3) for x in hc[-1][0]); driftc = [hc[-1][1][i] - hc[-2][1][i] for i in range(3)]
dd = max(abs(x - alpha * S / 3) for x in driftc)
cons = max(abs(sum(h[0]) - S) for h in hm + hc)
ok6 = ok6 and em < mp.mpf(10) ** -40 and stopm < mp.mpf(10) ** -40 and cons < mp.mpf(10) ** -50
ok7 = ok7 and ec < mp.mpf(10) ** -40 and dd < mp.mpf(10) ** -40 and abs(S) > mp.mpf(10) ** -3
rep('T6', ok6, "plane, exact: S = 0 kept, every residual times (1 - 3 alpha) a round exactly, alpha 1/10, 1/5, 1/2, 3/5 ("
    + "; ".join(msgs6) + "); alpha 7/10 diverges; sphere: S = " + mp.nstr(S, 12) + f" kept to {mp.nstr(cons, 3)}, residuals at S/3 to "
    f"{mp.nstr(em, 3)}, frames stopped to {mp.nstr(stopm, 3)}")
rep('T7', ok7, "plane, exact: squared deviation times (1 - 3 alpha + 3 alpha^2) a round exactly, S = 0 kept ("
    + "; ".join(msgs7) + f"); sphere: residuals at S/3 to {mp.nstr(ec, 3)}, every frame turning alpha S/3 = "
    f"{mp.nstr(alpha * S / 3, 12)} a round, off by {mp.nstr(dd, 3)} after 400 rounds")

open('runs/tlp/tlp-run1.txt', 'w').write("\n".join(out) + "\n")
