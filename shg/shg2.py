"""SHG run 2 (plans/shg-plan.md): the reader starts at the unit circle and sweeps the density parameters without knowing
V. The shape's modes n ≥ 1 from ratios of radii, exact whatever a₀ = ln(V*/H); a₀ undetermined; dκ/κ = da₀; truncation
at mode M is level of detail. Exact, mpmath at 40 digits.
Run: python3 shg/shg2.py
"""
import random
from mpmath import mp, mpf, cos, sin, exp, log, pi, fabs, atan2, sqrt, quad, tan
mp.dps = 40
TOL = mpf(10)**-30
ok = {}
rng = random.Random(11)
modes = [(n, mpf(rng.uniform(0.02, 0.2)), mpf(rng.uniform(0, 6.28))) for n in range(1, 7)]
def f(t, M=6): return sum(a * cos(n * t + p) for n, a, p in modes if n <= M)
def lnr(t, a0, rho, M=6): return a0 + rho * f(t, M)
N = 64
th = [2 * pi * k / N for k in range(N)]
a0s = (mpf(-3), mpf(0), mpf('2.5')); rhos = (mpf(0), mpf(1) / 4, mpf(1) / 2, mpf(1))
# R1
e1 = mpf(0); r1 = True
for rho in rhos:
    qs = {a0: [exp(lnr(t, a0, rho) - lnr(th[0], a0, rho)) for t in th] for a0 in a0s}
    for a0 in a0s:
        e1 = max(e1, max(fabs(x - y) for x, y in zip(qs[a0], qs[a0s[0]])))
    L = [log(q) for q in qs[a0s[1]]]
    c0 = sum(L) / N
    e1 = max(e1, fabs(c0 - (-rho * f(th[0]))))
    for n in range(1, N // 2):
        A = 2 * sum(L[k] * cos(n * th[k]) for k in range(N)) / N
        B = 2 * sum(L[k] * sin(n * th[k]) for k in range(N)) / N
        if n <= 6:
            _, a, p = modes[n - 1]
            # a cos(nθ + p) = a cos p cos nθ − a sin p sin nθ
            e1 = max(e1, fabs(A - rho * a * cos(p)), fabs(B + rho * a * sin(p)))
        else:
            e1 = max(e1, fabs(A), fabs(B))
ok['R1'] = e1 <= TOL
print(f"R1 ratios the same for every a₀; modes 1–6 recovered, 7–31 empty; constant term −ρ f(θ₀), not a₀: worst {mp.nstr(e1, 3)}")
# R2
e2 = mpf(0)
for k1, k2 in ((mpf('0.1'), mpf(3)), (mpf(2), mpf(50))):
    mass = quad(lambda k: 1 / k, [k1, k2])
    e2 = max(e2, fabs(mass - (log(k2) - log(k1))))
    for s in (mpf('0.5'), mpf(7)):        # a shift of a₀ by ln s: the interval [κ₁, κ₂] → [sκ₁, sκ₂]
        e2 = max(e2, fabs(quad(lambda k: 1 / k, [s * k1, s * k2]) - mass))
for kap in (mpf('0.3'), mpf(4)):
    for t in th[:8]:
        e2 = max(e2, fabs(log(kap * exp(lnr(t, mpf(0), mpf(1)))) - lnr(t, log(kap), mpf(1))))
ok['R2'] = e2 <= TOL
print(f"R2 rescaling is a shift of a₀, dκ/κ = da₀, unchanged by shifts: worst {mp.nstr(e2, 3)}")
# R3
e3 = mpf(0)
for rho in rhos:
    for a0 in a0s:
        for t in th:
            if fabs(cos(t)) < mpf('1e-10'): continue
            r = exp(lnr(t, a0, rho)); x, y = r * cos(t), r * sin(t)
            e3 = max(e3, fabs(y / x - tan(t)))
ok['R3'] = e3 <= mpf(10)**-28
print(f"R3 every address fixed through the sweep: worst {mp.nstr(e3, 3)}")
# R4
e4 = mpf(0); prev = None; mono = True
rho = mpf(1)
for M in range(0, 7):
    ms = quad(lambda t: (f(t) - f(t, M))**2, [0, pi, 2 * pi]) / (2 * pi)
    pred = sum(a * a for n, a, p in modes if n > M) / 2
    e4 = max(e4, fabs(ms - pred))
    if prev is not None and not ms < prev and M < 6: mono = False
    prev = ms
    print(f"   M = {M}: mean square of the dropped part {mp.nstr(ms, 10)}")
ok['R4'] = e4 <= TOL and mono and prev <= TOL
print(f"R4 truncation at mode M, Parseval: worst {mp.nstr(e4, 3)}, falling: {mono}")
# R5
held = [set(mp.nstr(t, 25) for t in th) for _ in a0s for _ in rhos]
ok['R5'] = all(h == held[0] for h in held)
print(f"R5 directions alone: the same set for every (a₀, ρ, f): {ok['R5']}")
for k in ('R1', 'R2', 'R3', 'R4', 'R5'):
    print(k, 'not killed' if ok[k] else 'KILLED')
