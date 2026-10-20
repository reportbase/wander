"""RWT run 1 (plans/rwt-plan.md): reading is free; writing one breadth in one's own H takes one known move; writing for
another reader one exchanged number more; writing in a public unit one agreed notch more. Exact, mpmath at 40 digits;
what is not fixed is counted as the nullity of the Jacobian of the log-readings (and known values) in the log-amounts.
Run: python3 runs/rwt/rwt.py
"""
import random
from mpmath import mp, mpf, matrix, cos, sin, log, exp, atan2, sqrt, pi, fabs, diff, svd_r
mp.dps = 40
TOL = mpf(10)**-30
ZERO = mpf(10)**-25
ok = {}
K = 4
rng = random.Random(13)
def scene():
    return [(mpf(rng.uniform(0.5, 3)), mpf(rng.uniform(20, 200)), mpf(rng.uniform(0.3, 2.8))) for _ in range(K)]  # a, d, φ

def readings_from(targets, px, py):
    """bearing and log half-angle reading of each target (a, d, φ given from the origin) seen from (px, py)"""
    out = []
    for a, d, ph in targets:
        x, y = d * cos(ph) - px, d * sin(ph) - py
        out += [atan2(y, x), log(a) - log(sqrt(x * x + y * y))]
    return out

def nullity(F, u):
    n = len(u); rows = len(F(u))
    J = matrix(rows, n)
    for j in range(n):
        def fj(t, j=j):
            v = list(u); v[j] = t; return F(v)
        h = mpf(10)**-12
        up = fj(u[j] + h); dn = fj(u[j] - h); up2 = fj(u[j] + 2 * h); dn2 = fj(u[j] - 2 * h)
        for i in range(rows):
            J[i, j] = (8 * (up[i] - dn[i]) - (up2[i] - dn2[i])) / (12 * h)
    S = svd_r(J, compute_uv=False)
    sv = [S[i] for i in range(min(rows, n))]
    return n - sum(1 for x in sv if x > ZERO), min(sv) if rows >= n else mpf(0)

def unpack(u):
    t = [(exp(u[3 * k]), exp(u[3 * k + 1]), u[3 * k + 2]) for k in range(K)]
    return t
def pack(targets): return [x for a, d, ph in targets for x in (log(a), log(d), ph)]

# T1
tg = scene()
e1 = mpf(0)
base = readings_from(tg, 0, 0)
for lam in (mpf('1e-3'), mpf(7), mpf('1e6')):
    sc = [(lam * a, lam * d, ph) for a, d, ph in tg]
    e1 = max(e1, max(fabs(x - y) for x, y in zip(readings_from(sc, 0, 0), base)))
n1, _ = nullity(lambda u: readings_from(unpack(u), 0, 0), pack(tg))
ok['T1'] = e1 <= TOL and n1 == K
print(f"T1 one standpoint: readings unchanged by λ (worst {mp.nstr(e1, 3)}); nullity {n1} (predicted {K})")

# T2: one move of length H (=1 in the reader's breadth), toward target 0 or sideways
def two_views(u, psi, known=True, gauge=True):
    t = unpack(u); lD = u[3 * K]; lH = mpf(0) if gauge else u[3 * K + 1]
    D = exp(lD)
    r = readings_from(t, 0, 0) + readings_from(t, D * cos(psi), D * sin(psi))
    if known: r.append(lD - lH)
    return r
def recover(r1, r2, psi, D=mpf(1)):
    out = []
    for k in range(K):
        b1, ls1 = r1[2 * k], r1[2 * k + 1]; b2, ls2 = r2[2 * k], r2[2 * k + 1]
        s1, s2 = exp(ls1), exp(ls2)
        if fabs(sin(b2 - b1)) < mpf('1e-20'):          # along the line of sight: d = D·s₂/(s₂ − s₁)
            d = D * s2 / (s2 - s1)
        else:                                            # triangulation across the baseline (law of sines)
            d = D * sin(b2 - psi) / sin(b2 - b1)
        out.append((s1 * d, d))                          # half-breadth a = s·d, distance d, in units of D = H
    return out
e2 = mpf(0); n2s = []
for sc_i in range(10):
    H = mpf(rng.uniform(0.5, 2))
    tg = scene()
    for psi in (tg[0][2], tg[0][2] + pi / 2):            # toward target 0, then sideways to it
        r1 = readings_from(tg, 0, 0); r2 = readings_from(tg, H * cos(psi), H * sin(psi))
        rec = recover(r1, r2, psi)
        for (a, d, ph), (ar, dr) in zip(tg, rec):
            e2 = max(e2, fabs(ar - a / H), fabs(dr - d / H))
        if sc_i < 3:
            u = pack([(a / H, d / H, ph) for a, d, ph in tg]) + [mpf(0)]
            n2s.append(nullity(lambda u, psi=psi: two_views(u, psi), u)[0])
ok['T2'] = e2 <= TOL and all(n == 0 for n in n2s)
print(f"T2 one known move: V*/H and d/H recovered, worst {mp.nstr(e2, 3)}; nullities {n2s} (predicted 0)")

# T3: the move's length unknown
tg = scene(); psi = tg[0][2] + pi / 2
u = pack(tg) + [mpf(0)]
n3, _ = nullity(lambda u: two_views(u, psi, known=False), u)
e3 = mpf(0); D = mpf('1.3')
base = readings_from(tg, 0, 0) + readings_from(tg, D * cos(psi), D * sin(psi))
for lam in (mpf('1e-3'), mpf(7), mpf('1e6')):
    sc = [(lam * a, lam * d, ph) for a, d, ph in tg]
    rr = readings_from(sc, 0, 0) + readings_from(sc, lam * D * cos(psi), lam * D * sin(psi))
    e3 = max(e3, max(fabs(x - y) for x, y in zip(rr, base)))
ok['T3'] = n3 == 1 and e3 <= TOL
print(f"T3 move of unknown length: nullity {n3} (predicted 1); scenes ×λ read the same, worst {mp.nstr(e3, 3)}")

# T4: a second known move
tg = scene(); H = mpf('1.4')
p1, p2 = tg[0][2], tg[0][2] + pi / 2
r0 = readings_from(tg, 0, 0)
rA = recover(r0, readings_from(tg, H * cos(p1), H * sin(p1)), p1)
rB = recover(r0, readings_from(tg, H * cos(p2), H * sin(p2)), p2)
e4 = max(max(fabs(x[0] - y[0]), fabs(x[1] - y[1])) for x, y in zip(rA, rB))
def three_views(u):
    t = unpack(u); lD = u[3 * K]
    D = exp(lD)
    return (readings_from(t, 0, 0) + readings_from(t, D * cos(p1), D * sin(p1))
            + readings_from(t, D * (cos(p1) + cos(p2)), D * (sin(p1) + sin(p2))) + [lD])
n4, _ = nullity(three_views, pack([(a / H, d / H, ph) for a, d, ph in tg]) + [mpf(0)])
ok['T4'] = e4 <= TOL and n4 == 0
print(f"T4 a second known move: same V*/H (worst {mp.nstr(e4, 3)}); nullity {n4} (predicted 0)")

# T5, T6: readers A and B
tg = scene(); HA, HB = mpf('0.7'), mpf('1.9')
bx, by = mpf(15), mpf(-8)                       # B's first standpoint
qa, qb = mpf('0.4'), mpf('2.0')                 # move directions
ra = recover(readings_from(tg, 0, 0), readings_from(tg, HA * cos(qa), HA * sin(qa)), qa)
def shifted(t, ox, oy):                         # targets as seen from (ox, oy), re-expressed in polar from there
    out = []
    for a, d, ph in t:
        x, y = d * cos(ph) - ox, d * sin(ph) - oy
        out.append((a, sqrt(x * x + y * y), atan2(y, x)))
    return out
tgB = shifted(tg, bx, by)
rb = recover(readings_from(tgB, 0, 0), readings_from(tgB, HB * cos(qb), HB * sin(qb)), qb)
e5 = mpf(0)
for (aa, _), (ab, _) in zip(ra, rb):
    e5 = max(e5, fabs(aa / ab - HB / HA))
ratio = ra[0][0] / rb[0][0]                     # A reads H_B/H_A from B's one sent number
for (aa, _), (ab, _) in zip(ra, rb):
    e5 = max(e5, fabs(ab * ratio - aa))
# A's system with H_B as an unknown: without and with B's one number
uA = pack([(a / HA, d / HA, ph) for a, d, ph in tg]) + [mpf(0), log(HB / HA)]
def A_sys2(u, sent):
    t = unpack(u); D = exp(u[3 * K])
    r = readings_from(t, 0, 0) + readings_from(t, D * cos(qa), D * sin(qa)) + [u[3 * K]]
    if sent: r.append(u[0] - u[3 * K + 1] - log(rb[0][0]))
    return r
n5a, _ = nullity(lambda u: A_sys2(u, False), uA)
n5b, _ = nullity(lambda u: A_sys2(u, True), uA)
ok['T5'] = e5 <= TOL and n5a == 1 and n5b == 0
print(f"T5 two readers: written breadths differ by H_B/H_A, one number sent makes all {K} agree (worst {mp.nstr(e5, 3)});"
      f" nullity without {n5a}, with {n5b} (predicted 1, 0)")
# T6: in metres, log H_A an unknown too
def M_sys(u, notch):
    t = unpack(u); lD, lHB, lHA = u[3 * K], u[3 * K + 1], u[3 * K + 2]
    D = exp(lD)
    r = readings_from(t, 0, 0) + readings_from(t, D * cos(qa), D * sin(qa)) + [lD - lHA]
    r.append(u[0] - lHB - log(rb[0][0]))
    if notch: r.append(lHA - log(mpf('0.7')))
    return r
uM = pack(tg) + [log(HA), log(HB), log(HA)]
n6a, _ = nullity(lambda u: M_sys(u, False), uM)
n6b, _ = nullity(lambda u: M_sys(u, True), uM)
e6 = max(fabs(ra[k][0] * HA - tg[k][0]) for k in range(K))
ok['T6'] = n6a == 1 and n6b == 0 and e6 <= TOL
print(f"T6 in metres: nullity without a notch {n6a}, with H_A = 0.7 m {n6b} (predicted 1, 0); breadths in metres, worst {mp.nstr(e6, 3)}")
for k in ('T1', 'T2', 'T3', 'T4', 'T5', 'T6'):
    print(k, 'not killed' if ok[k] else 'KILLED')
