"""TWS run 1 (plans/tws-plan.md): only the centre and the points of the circle turn an even sweep into an even arc;
the two sweeps are the stereographic chart (from A) and its square (from M). Exact, mpmath at 40 digits.
Run: python3 tws/tws.py   (about half a minute)
"""
from mpmath import mp, mpf, mpc, sqrt, cos, sin, tan, atan2, pi, diff, quad, log, fabs, atan
mp.dps = 40
TOL = mpf(10)**-30
ok = {}

def hit(p, psi, far=False):
    """Q's angle about O for the ray from (p, 0) at direction psi; the hit ahead, or the far one."""
    c, s = cos(psi), sin(psi)
    disc = 1 - p * p * s * s
    lam = -p * c + sqrt(disc) if not far else -p * c - sqrt(disc)
    if p == 1 and far:
        lam = -2 * c
    return atan2(lam * s, p + lam * c)

def rate(p, psi, far=False):
    return diff(lambda x: hit(p, x, far), psi)

# T1, T2
psis = [pi * k / 50 + mpf('0.013') for k in range(50)]
r0 = [rate(0, x) for x in psis]
ok['T1'] = max(fabs(r - 1) for r in r0) <= TOL
into = [pi / 2 + mpf('0.02') + (pi - mpf('0.04')) * k / 49 for k in range(50)]          # cos ψ < 0: into the circle
r1 = [rate(1, x, far=False) for x in into]                                             # from P on the circle the hit ahead is the far one
ok['T2'] = max(fabs(r - 2) for r in r1) <= TOL
print(f"T1 centre: r in [{mp.nstr(min(r0), 12)}, {mp.nstr(max(r0), 12)}]")
print(f"T2 on the circle: r in [{mp.nstr(min(r1), 12)}, {mp.nstr(max(r1), 12)}]")
# T3
t3 = True
for p in (mpf('0.1'), mpf('0.5'), mpf('0.9')):
    worst = mpf(0); rs = []
    for x in psis:
        c, s = cos(x), sin(x); root = sqrt(1 - p * p * s * s)
        t, tp = -p * c + root, p * c + root
        r = rate(p, x); rs.append(r)
        worst = max(worst, fabs(r - 2 * t / (t + tp)))
    lo, hi = rate(p, mpf(0)), rate(p, pi)
    good = worst <= TOL and fabs(lo - (1 - p)) <= TOL and fabs(hi - (1 + p)) <= TOL
    t3 &= good
    print(f"T3 p={p}: r against 2t/(t+t′) off at most {mp.nstr(worst, 3)}; outward {mp.nstr(lo, 12)}, inward {mp.nstr(hi, 12)}")
ok['T3'] = t3
# T4
t4 = True
for p in (mpf('1.5'), mpf(2), mpf(5)):
    a = pi - atan(1 / sqrt(p * p - 1))                 # the tangent rays make angle asin(1/p) with the line to O
    xs = [pi - (pi - a) * (k + 1) / 41 for k in range(40)] + [pi + (pi - a) * (k + 1) / 41 for k in range(40)]
    rs = [rate(p, x, far=True) for x in xs]          # the minus root: the near hit
    near_tan = rate(p, a + (pi - a) * mpf(10)**-8, far=True)
    spread = max(rs) - min(rs)
    t4 &= spread > mpf('1e-3')
    print(f"T4 p={p}: r in [{mp.nstr(min(rs), 8)}, {mp.nstr(max(rs), 8)}], spread {mp.nstr(spread, 6)}; near a tangent ray {mp.nstr(near_tan, 6)}")
ok['T4'] = t4
# T5
mp.dps = 30
flat = []
dirs = [pi * k / 100 + mpf('0.0071') for k in range(200)]
for k in range(301):
    p = mpf(k) / 100
    if p < 1:
        rs = [rate(p, x) for x in dirs]
    elif p == 1:
        rs = [rate(p, x) for x in dirs if cos(x) < -mpf('0.01')]
    else:
        lim = 1 / p
        rs = [rate(p, x, far=True) for x in dirs if fabs(sin(x)) < lim * mpf('0.999') and cos(x) < 0]
    spread = max(rs) - min(rs)
    if spread <= mpf(10)**-20:
        flat.append(float(p))
    elif spread <= mpf('1e-4'):
        flat.append(('small', float(p), float(spread)))
mp.dps = 40
print(f"T5 pivots with a constant rate, p in 0 … 3: {flat}")
ok['T5'] = flat == [0.0, 1.0]
# T6
t6 = True
for k in range(40):
    th = (pi / 2) * (k + mpf('0.5')) / 40
    h, v = cos(th), sin(th)
    P = (h * h, h * v); M = (mpf(1) / 2, 0)
    z = mpc(2 * (P[0] - M[0]), 2 * (P[1] - M[1]))
    e1 = fabs(z - mpc(h, v)**2)
    e2 = fabs(atan2(z.imag, z.real) - 2 * th)
    s_on_tangent = tan(th) * 1                       # the ray y = x·tan θ meets x = 1 at height tan θ
    e3 = fabs(s_on_tangent - v / h) + fabs(s_on_tangent - tan(atan2(z.imag, z.real) / 2))
    t6 &= max(e1, e2, e3) <= TOL
ok['T6'] = t6
print(f"T6 two charts on the chord: {'every check within 1e-30' if t6 else 'OFF'}")
# T7
cdf_ok = all(fabs((2 / pi) * atan(x) - quad(lambda s: 2 / (pi * (1 + s * s)), [0, x])) <= TOL for x in (mpf('0.3'), mpf(1), mpf(7)))
med = (2 / pi) * atan(1)
tm = lambda S: quad(lambda t: tan(t), [0, atan(S)]) / (pi / 2)
climb = tm(mpf(10)**7) - tm(mpf(10)**6)
mc = quad(cos, [0, pi]) / pi; ms = quad(sin, [0, pi]) / pi
ok['T7'] = cdf_ok and fabs(med - mpf(1) / 2) <= TOL and fabs(climb - 2 / pi * log(10)) <= mpf(10)**-9 and \
    fabs(mc) <= TOL and fabs(ms - 2 / pi) <= TOL
print(f"T7 inscribed: Cauchy law {cdf_ok}, P(s ≤ 1) = {mp.nstr(med, 12)}, mean climb 10⁶→10⁷ {mp.nstr(climb, 12)} "
      f"(2/π·ln 10 = {mp.nstr(2 / pi * log(10), 12)}); central: means {mp.nstr(mc, 5)}, {mp.nstr(ms, 15)} (2/π {mp.nstr(2 / pi, 15)})")
for k in ('T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7'):
    print(k, 'not killed' if ok[k] else 'KILLED')
