"""SHG run 1 (plans/shg-plan.md): a shape as a perturbed unit circle, r = exp(ρ f(θ)); by direction the readings are the
Cauchy at every ρ, along the outline they move; only circles (centred on the reader, or through it) read evenly along
their outline. Exact, mpmath at 40 digits.
Run: python3 shg/shg.py
"""
import random
from mpmath import mp, mpf, cos, sin, exp, atan, atan2, pi, quad, sqrt, fabs, diff
mp.dps = 40
TOL = mpf(10)**-30
ok = {}
def f1(t): return mpf('0.3') * cos(2 * t) + mpf('0.1') * cos(3 * t + mpf('0.4'))
def f2(t): return mpf('0.25') * cos(4 * t)
def shape(f, rho): return lambda t: exp(rho * f(t))
def speed(r):            # length of outline per unit of turn, √(r² + r′²)
    return lambda t: sqrt(r(t)**2 + diff(r, t)**2)
def cauchy(t): return (2 / pi) * atan(t)
ts = (mpf(1) / 4, mpf(1), mpf(4))
rhos = (mpf(0), mpf(1) / 4, mpf(1) / 2, mpf(1))

# S1: by direction the reading of r(θ)(cos θ, sin θ) is tan θ whatever r
e1 = mpf(0)
for f in (f1, f2):
    for rho in rhos:
        r = shape(f, rho)
        for k in range(50):
            th = (pi / 2) * (k + mpf('0.5')) / 50
            x, y = r(th) * cos(th), r(th) * sin(th)
            e1 = max(e1, fabs(y / x - mp.tan(th)))
        # law: θ even, P(v/h ≤ t) = P(θ ≤ atan t) = atan t/(π/2)
        for t in ts:
            e1 = max(e1, fabs(atan(t) / (pi / 2) - cauchy(t)))
ok['S1'] = e1 <= TOL
print(f"S1 by direction: reading tan θ at every ρ, law (2/π)·arctan t: worst {mp.nstr(e1, 3)}")

# S2: laid evenly along the outline on the quarter turn
def along(f, rho, t):
    sp = speed(shape(f, rho))
    return quad(sp, [0, atan(t)]) / quad(sp, [0, pi / 2])
s2 = True; rows = []
for f, name in ((f1, 'f1'), (f2, 'f2')):
    for rho in rhos:
        p1, pq = along(f, rho, mpf(1)), along(f, rho, mpf(1) / 4)
        rows.append((name, rho, p1, pq))
        if rho == 0:
            s2 &= fabs(p1 - mpf(1) / 2) <= TOL and fabs(pq - cauchy(mpf(1) / 4)) <= TOL
        elif name == 'f1':
            s2 &= fabs(p1 - mpf(1) / 2) > mpf('1e-3')
        else:
            s2 &= fabs(p1 - mpf(1) / 2) <= TOL and fabs(pq - cauchy(mpf(1) / 4)) > mpf('1e-3')
ok['S2'] = s2
for name, rho, p1, pq in rows:
    print(f"   along the outline {name} ρ={mp.nstr(rho, 3)}: P(v/h ≤ 1) {mp.nstr(p1, 12)}, P(v/h ≤ ¼) {mp.nstr(pq, 12)}"
          f" (Cauchy ½, {mp.nstr(cauchy(mpf(1) / 4), 12)})")
print(f"S2 along the outline the law moves with ρ; the flip-symmetric shape keeps its corner: {s2}")

# S3: √(r² + r′²) constant only for the two circles
def spread(r, a, b, n=400):
    sp = speed(r)
    vals = [sp(a + (b - a) * (k + mpf('0.5')) / n) for k in range(n)]
    return max(vals) - min(vals), vals[0]
s3 = True; worst_c = mpf(0); least_p = mpf(10)
for c in (mpf('0.7'), mpf(1), mpf(3)):
    d, _ = spread(lambda t, c=c: c + 0 * t, mpf(0), 2 * pi); worst_c = max(worst_c, d)
for c in (mpf(1), mpf(2)):
    for ph in (mpf(0), mpf('0.3')):
        r = lambda t, c=c, ph=ph: c * sin(t + ph)
        d, v0 = spread(r, -ph + mpf('0.01'), pi - ph - mpf('0.01'), 200)
        worst_c = max(worst_c, d, fabs(v0 - c))
        for k in range(20):   # the ODE r² + r′² = c²
            t = -ph + mpf('0.05') + (pi - mpf('0.1')) * k / 19
            worst_c = max(worst_c, fabs(r(t)**2 + diff(r, t)**2 - c * c))
s3 &= worst_c <= TOL
rng = random.Random(7)
others = [shape(f, rho) for f in (f1, f2) for rho in rhos[1:]]
for _ in range(20):
    terms = [(rng.randint(1, 6), mpf(rng.uniform(-0.3, 0.3)), mpf(rng.uniform(0, 6.28))) for _ in range(3)]
    others.append(lambda t, terms=terms: exp(sum(a * cos(n * t + p) for n, a, p in terms)))
mp.dps = 30
for r in others:
    d, _ = spread(r, mpf(0), 2 * pi, 120); least_p = min(least_p, d)
mp.dps = 40
s3 &= least_p > mpf('1e-6')
ok['S3'] = s3
print(f"S3 circles centred on or through the reader: spread at most {mp.nstr(worst_c, 3)}; "
      f"26 perturbations: least spread {mp.nstr(least_p, 6)}")

# S4: the group
e4 = mpf(0)
g1, g2 = f1, f2
for k in range(30):
    t = 2 * pi * k / 30; r0 = mpf('0.8')
    a = r0 * exp(g1(t)) * exp(g2(t)); b = r0 * exp(g2(t)) * exp(g1(t)); c = r0 * exp(g1(t) + g2(t))
    e4 = max(e4, fabs(a - b), fabs(a - c))
    # the mapped point keeps its direction
    x, y = a * cos(t), a * sin(t)
    tt = atan2(y, x) % (2 * pi)
    e4 = max(e4, min(fabs(tt - t), fabs(tt - t - 2 * pi), fabs(tt - t + 2 * pi)))
inner = quad(lambda t: min(mpf(1), exp(-2 * g1(t)) / 4), [0, pi / 2, pi, 3 * pi / 2, 2 * pi]) / (2 * pi)
moved = fabs(inner - mpf(1) / 4)
ok['S4'] = e4 <= TOL and moved > mpf('1e-3')
print(f"S4 radial maps commute and keep directions: worst {mp.nstr(e4, 3)}; the disc's share within ½ "
      f"¼ → {mp.nstr(inner, 12)} (moved {mp.nstr(moved, 4)})")
for k in ('S1', 'S2', 'S3', 'S4'):
    print(k, 'not killed' if ok[k] else 'KILLED')
