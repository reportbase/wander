"""RHO run 1 (plans/rho-plan.md): OFS's two ρ joined. A shape ln r = a0 + ε f(θ) laid along its outline is the
density ρ(θ) = σ/max σ, σ = √(r² + r′²), on the inscribed sweep's addresses; the median moves only by the shape's
exchange-reversed part, the size a0 cancels, and ln ρ gives the shape back to O(ε²). Exact, mpmath at 40 digits.
Run: python3 -I rho/rho.py
"""
import random
from mpmath import mp, mpf, cos, sin, exp, atan, pi, quad, sqrt, fabs, log, findroot, degrees
mp.dps = 40
TOL = mpf(10)**-30
ok = {}

def f1(t): return mpf('0.3') * cos(2 * t) + mpf('0.1') * cos(3 * t + mpf('0.4'))
def f1p(t): return -mpf('0.6') * sin(2 * t) - mpf('0.3') * sin(3 * t + mpf('0.4'))
def f2(t): return mpf('0.25') * cos(4 * t)
def f2p(t): return -sin(4 * t)
rng = random.Random(11)
G = [(rng.randint(1, 8), mpf(rng.uniform(-0.3, 0.3)), mpf(rng.uniform(0, 6.283))) for _ in range(4)]
def g(t): return sum(a * cos(n * t + p) for n, a, p in G)
def gp(t): return sum(-a * n * sin(n * t + p) for n, a, p in G)
def f3(t): return g(t) + g(pi / 2 - t)
def f3p(t): return gp(t) - gp(pi / 2 - t)
SH = {'f1': (f1, f1p), 'f2': (f2, f2p), 'f3': (f3, f3p)}

def r_of(f, eps, a0): return lambda t: exp(a0 + eps * f(t))
def sigma(f, fp, eps, a0):           # √(r² + r′²), r′ = r·ε f′
    return lambda t: exp(a0 + eps * f(t)) * sqrt(1 + (eps * fp(t))**2)
QPTS = [0, pi / 8, pi / 4, 3 * pi / 8, pi / 2]
def integ(w, a, b): return quad(w, [a, b]) if b > a else mpf(0)
def law(w, t):                      # use 1: share of the arrivals with v/h ≤ t
    return integ(w, 0, atan(t)) / quad(w, QPTS)
def median(w):
    tot = quad(w, QPTS)
    return findroot(lambda x: integ(w, 0, x) - tot / 2, pi / 4)
def maxof(w, n=2000): return max(w((pi / 2) * (k + mpf('0.5')) / n) for k in range(n))
def cauchy(t): return (2 / pi) * atan(t)

def outline_law(f, eps, a0, t):     # laid evenly along the outline: arc length, by the polar points themselves
    r = r_of(f, eps, a0)
    def speed(u):                   # |d/du (r cos u, r sin u)| computed from the point, not from σ's formula
        x = lambda v: r(v) * cos(v); y = lambda v: r(v) * sin(v)
        return sqrt(mp.diff(x, u)**2 + mp.diff(y, u)**2)
    return integ(speed, 0, atan(t)) / quad(speed, QPTS)

EPSS = (mpf(1) / 4, mpf(1) / 2, mpf(1))
TS = (mpf(1) / 4, mpf(1), mpf(4))

# P1: identity
e1 = mpf(0); shg = []
for name in ('f1', 'f2'):
    f, fp = SH[name]
    for eps in EPSS:
        s = sigma(f, fp, eps, 0); m = maxof(s, 400)
        rho = lambda t, s=s, m=m: s(t) / m
        for t in TS:
            a, b = law(rho, t), outline_law(f, eps, 0, t)
            e1 = max(e1, fabs(a - b))
            if name == 'f1' and t == 1: shg.append(a)
want = ('0.529', '0.563', '0.632')
shg_ok = all(mp.nstr(v, 3) == w for v, w in zip(shg, want))
ok['P1'] = e1 <= TOL and shg_ok
print(f"P1 density σ/max σ against arc length along the outline: worst {mp.nstr(e1, 3)}; f1 at t = 1: "
      f"{', '.join(mp.nstr(v, 12) for v in shg)} (SHG {', '.join(want)})")

# P2: the exchange
p2 = True; rows = []
for name in ('f2', 'f3', 'f1'):
    f, fp = SH[name]
    for eps in EPSS:
        s = sigma(f, fp, eps, 0)
        md = median(s); off = degrees(md) - 45
        q = law(s, mpf(1) / 4) - cauchy(mpf(1) / 4)
        rows.append((name, eps, off, q))
        if name == 'f1': p2 &= fabs(off) > mpf('0.1')
        else: p2 &= fabs(off) <= TOL and fabs(q) > mpf('1e-3')
ok['P2'] = p2
for name, eps, off, q in rows:
    print(f"   {name} ε={mp.nstr(eps, 3)}: median − 45° = {mp.nstr(off, 6)}°, P(v/h ≤ ¼) − Cauchy = {mp.nstr(q, 6)}")
print(f"P2 exchange-symmetric shapes keep the corner, f1 moves it: {p2}")

# P3: first order
f, fp = SH['f1']
D = (quad(f, [pi / 4, pi / 2]) - quad(f, [0, pi / 4])) / 2
errs = []
for eps in (mpf('0.1'), mpf('0.05'), mpf('0.025'), mpf('0.0125')):
    d = median(sigma(f, fp, eps, 0)) - pi / 4
    errs.append((eps, d, eps * D, fabs(d - eps * D) / fabs(eps * D)))
fall = [errs[i][3] / errs[i + 1][3] for i in range(3)]
ok['P3'] = D < 0 and all(x >= mpf('1.8') for x in fall) and errs[-1][3] < mpf('0.02')
for eps, d, d1, re in errs:
    print(f"   ε={mp.nstr(eps, 4)}: δ {mp.nstr(d, 10)}, δ₁ {mp.nstr(d1, 10)}, relative error {mp.nstr(re, 5)}")
print(f"P3 first order δ₁ = ε·{mp.nstr(D, 10)}; the error falls by {', '.join(mp.nstr(x, 4) for x in fall)} per halving")

# P4: no size
e4 = mpf(0)
for name in ('f1', 'f2', 'f3'):
    f, fp = SH[name]
    for eps in EPSS:
        base = [law(sigma(f, fp, eps, 0), t) for t in TS] + [median(sigma(f, fp, eps, 0))]
        for a0 in (mpf(-5), mpf(5)):
            s = sigma(f, fp, eps, a0)
            other = [law(s, t) for t in TS] + [median(s)]
            e4 = max(e4, max(fabs(x - y) for x, y in zip(base, other)))
ok['P4'] = e4 <= TOL
print(f"P4 a0 = −5, 0, 5: worst change {mp.nstr(e4, 3)}")

# P5: other payloads
f, fp = SH['f1']
p5 = True; diffs = []
for k in (1, 2):
    eps = mpf('0.0125')
    d = median(lambda t: exp(k * eps * f(t))) - pi / 4
    re = fabs(d - k * eps * D) / fabs(k * eps * D)
    p5 &= re < mpf('0.02')
    print(f"   r^{k}: δ {mp.nstr(d, 10)} against {k}·δ₁ {mp.nstr(k * eps * D, 10)}, relative error {mp.nstr(re, 5)}")
for eps in (mpf('0.1'), mpf('0.05'), mpf('0.025'), mpf('0.0125')):
    da = median(sigma(f, fp, eps, 0)); dr = median(lambda t: exp(eps * f(t)))
    diffs.append(fabs(da - dr))
fall5 = [diffs[i] / diffs[i + 1] for i in range(3)]
p5 &= all(x >= 3 for x in fall5)
ok['P5'] = p5
print(f"P5 arc element against radius: |Δ median| {', '.join(mp.nstr(x, 5) for x in diffs)}; "
      f"falls by {', '.join(mp.nstr(x, 4) for x in fall5)} per halving")

# P6: the shape read back
p6 = True
for name in ('f1', 'f3'):
    f, fp = SH[name]
    fbar = quad(f, QPTS) / (pi / 2)
    ratios = []
    for eps in (mpf('0.1'), mpf('0.0125')):
        s = sigma(f, fp, eps, 0); m = maxof(s, 400)
        lr = lambda t: log(s(t) / m)
        lbar = quad(lr, QPTS) / (pi / 2)
        worst = max(fabs(lr(th) - lbar - eps * (f(th) - fbar)) for th in ((pi / 2) * (k + mpf('0.5')) / 200 for k in range(200)))
        ratios.append(worst / eps**2)
    q = ratios[0] / ratios[1]
    p6 &= mpf(1) / mpf('1.5') <= q <= mpf('1.5')
    print(f"   {name}: max error / ε² = {mp.nstr(ratios[0], 6)} at ε = 0.1, {mp.nstr(ratios[1], 6)} at ε = 0.0125")
ok['P6'] = p6
print(f"P6 ln ρ − mean = ε(f − f̄) + O(ε²): {p6}")

for k in ('P1', 'P2', 'P3', 'P4', 'P5', 'P6'):
    print(k, 'not killed' if ok[k] else 'KILLED')
