"""JAY: building on Jaynes, the reader's ignorance as a group. See plans/jay-plan.md (P1-P7).

The method is Jaynes's (1968, 1973): state what an observer cannot tell apart as a group of transformations and use the
measure the group leaves unchanged. The reader's unknowns: its attitude theta (a turn), the other party's size
kappa = V*/H (a rescaling), and which party is which (the exchange). Rational points in exact arithmetic (fractions);
the rest with mpmath at 60 digits.
Run: python3 runs/jay/jay.py   (a few minutes; needs mpmath). Run 2: hq() for the singular quadratures (plans/jay-plan.md).
"""
from fractions import Fraction as F
import random
import mpmath as mp
mp.mp.dps = 60
M = mp.mpf
def verdict(ok): return "not killed" if ok else "KILLED"
def hq(f, pts, dps=200):
    """quadrature at 200 working digits, for densities with an algebraic singularity at an end of the range (run 2).
    mpmath caches the nodes of every interval it meets; at 200 digits 2,000 intervals fill memory, so each interval's
    nodes are dropped after use (the standard nodes on [-1, 1] are kept). Memory only; the rule is unchanged."""
    with mp.workdps(dps):
        v = +mp.quad(f, pts)
    cache = mp.mp._tanh_sinh.transformed_cache
    for key in [k for k in cache if (k[0], k[1]) != (-1, 1)]:
        del cache[key]
    return v
results = {}
rng = random.Random(20261014)

def rat(lo=1, hi=60):
    return F(rng.randint(lo, hi), rng.randint(lo, hi))

# ---------------------------------------------------------------- P1: rescaling fixes the levels; Haldane on a share
pairs = []
while len(pairs) < 200:
    x, lam = rat(), rat()
    if lam != 1: pairs.append((x, lam))
cands_exact = {'1/x': lambda x: 1 / x, '1/x^2': lambda x: 1 / x ** 2,
               '1/(1+x^2)': lambda x: 1 / (1 + x * x), '1/(1+x)^2': lambda x: 1 / (1 + x) ** 2}
cands_mp = {'x^(-1/2)': lambda x: 1 / mp.sqrt(x), 'e^(-x)': lambda x: mp.exp(-x)}
passes = {}
for name, f in cands_exact.items():
    passes[name] = all(f(x) == lam * f(lam * x) for x, lam in pairs)
for name, f in cands_mp.items():
    passes[name] = all(abs(f(M(x.numerator) / x.denominator) - M(lam.numerator) / lam.denominator
                           * f(M((lam * x).numerator) / (lam * x).denominator)) < M('1e-50') for x, lam in pairs)
ok1a = passes['1/x'] and not any(v for k, v in passes.items() if k != '1/x')
lv = max(abs(mp.quad(lambda x: 1 / x, [M(2) ** k, M(2) ** (k + 1)]) - mp.log(2)) for k in range(-30, 31))
ok1b = lv < M('1e-50')
ok1c = True
for _ in range(200):
    t = F(rng.randint(1, 59), 60); lam = rat()
    g = lam * t / (1 - t + lam * t)                       # the rescaling of the odds, acting on the share
    dg = lam / (1 - t + lam * t) ** 2                     # dg/dt
    hald = lambda u: 1 / (u * (1 - u))
    if hald(t) != hald(g) * dg: ok1c = False             # f(t) = f(gt)|g'(t)|
    s = t / (1 - t)                                       # odds; t = s/(1+s), dt/ds = 1/(1+s)^2
    if (1 / s) != hald(t) * (1 / (1 + s) ** 2): ok1c = False   # ds/s = dt/(t(1-t))
ok1 = ok1a and ok1b and ok1c
results['P1'] = (ok1, f"invariant candidates: {[k for k, v in passes.items() if v]}; worst level mass - ln 2: "
                      f"{mp.nstr(lv, 3)}; Haldane invariant and ds/s = dt/(t(1-t)) exactly: {ok1c}")

# ---------------------------------------------------------------- P2: turns fix the even turn, i, and Jeffreys
def mob(g, z):
    a, b, c, d = g
    return (a * z + b) / (c * z + d)
def cauchy_pdf(z, y):
    m, gm = mp.re(z), mp.im(z)
    return gm / (mp.pi * ((y - m) ** 2 + gm ** 2))
w2a = M(0)
for _ in range(50):
    while True:
        g = [M(rng.uniform(-3, 3)) for _ in range(4)]
        if abs(g[0] * g[3] - g[1] * g[2]) > M('0.1'): break
    det = g[0] * g[3] - g[1] * g[2]
    a, b, c, d = g
    ginv = (d, -b, -c, a)
    for _ in range(1):
        z = mp.mpc(rng.uniform(-3, 3), rng.uniform(0.05, 3))
        w = mob(g, z)
        w = w if det > 0 else mp.conj(w)                  # determinant < 0: the mirror of g(z)
        for _ in range(20):
            y = M(rng.uniform(-20, 20))
            x = mob(ginv, y)
            jac = abs(det) / (-c * y + a) ** 2            # |d g^{-1}(y)/dy|
            push = cauchy_pdf(z, x) * jac
            w2a = max(w2a, abs(push / cauchy_pdf(w, y) - 1))
# the exchange x -> 1/x explicitly: Cauchy(z) goes to Cauchy(1/conj z)
for _ in range(50):
    z = mp.mpc(rng.uniform(-3, 3), rng.uniform(0.05, 3))
    for _ in range(20):
        y = M(rng.uniform(-20, 20))
        push = cauchy_pdf(z, 1 / y) / y ** 2
        w2a = max(w2a, abs(push / cauchy_pdf(1 / mp.conj(z), y) - 1))
ok2a = w2a < M('1e-45')
turn = lambda al: (mp.cos(al), mp.sin(al), -mp.sin(al), mp.cos(al))
mi = max(abs(mob(turn(M(rng.uniform(0, 6.3))), mp.mpc(0, 1)) - mp.mpc(0, 1)) for _ in range(100))
moved = M(10)
for _ in range(200):
    z = mp.mpc(rng.uniform(-3, 3), rng.uniform(0.05, 3))
    if abs(z - mp.mpc(0, 1)) < M('1e-3'): continue
    al = M(rng.uniform(0.1, float(mp.pi) - 0.1))
    moved = min(moved, abs(mob(turn(al), z) - z))
exch_i = abs(1 / mp.conj(mp.mpc(0, 1)) - mp.mpc(0, 1))
dil_i = max(abs(mob((lam, 0, 0, 1), mp.mpc(0, 1)) - mp.mpc(0, lam)) for lam in [M('0.001'), M(2), M(7)])
# fixed points of a turn: -z^2 sin a = sin a  ->  z = +-i
ok2b = mi < M('1e-50') and moved > M('1e-30') and exch_i < M('1e-55') and dil_i < M('1e-55')
half_med = abs(2 / mp.pi * mp.atan(1) - M('0.5'))
ok2b = ok2b and half_med < M('1e-55')
# (c) the foot t = v^2 = sin^2(theta) under the even turn: CDF (2/pi) asin(sqrt t) = Jeffreys / arcsine
def arcsine_gap(i):
    """|even turn's CDF - Jeffreys's CDF| at t = i/2001 (a top-level function, so the 2,000 can run on every core)"""
    mp.mp.dps = 60
    t = M(i) / 2001
    even = (2 / mp.pi) * mp.asin(mp.sqrt(t))             # P(sin^2 theta <= t), theta even on [0, pi/2]
    jeff = hq(lambda u: 1 / (mp.pi * mp.sqrt(u * (1 - u))), [0, t])
    return abs(even - jeff)
if __name__ == '__main__':
    import multiprocessing
    with multiprocessing.get_context('fork').Pool(3) as pool:      # fork: workers skip the rest
        w2c = max(pool.map(arcsine_gap, range(1, 2001), chunksize=50))
w2fr = M(0)
for i in range(1, 200):
    th = M(i) / 200 * mp.pi / 2
    # Fisher-Rao length from t = 1 to cos^2 theta, sqrt(I) = 1/sqrt(t(1-t)); reflected by w = 1 - u (run 2)
    fr = hq(lambda w: 1 / mp.sqrt(w * (1 - w)), [0, mp.sin(th) ** 2])
    w2fr = max(w2fr, abs(fr - 2 * th))
ok2c = w2c < M('1e-50') and w2fr < M('1e-40')
# (d) the even octant's squares are Dirichlet(1/2, 1/2, 1/2)
w2d = M(0)
for p in range(5):
    for q in range(5):
        for r in range(5):
            ia = mp.quad(lambda a: mp.cos(a) ** (2 * p + 2 * r + 1) * mp.sin(a) ** (2 * q), [0, mp.pi / 2])
            iz = mp.quad(lambda z: mp.cos(z) ** (2 * p) * mp.sin(z) ** (2 * r), [0, mp.pi / 2])
            octm = ia * iz / (mp.pi / 2)
            dirm = (mp.gamma(M('0.5') + p) * mp.gamma(M('0.5') + q) * mp.gamma(M('0.5') + r) * mp.gamma(M('1.5'))
                    / (mp.gamma(M('0.5')) ** 3 * mp.gamma(M('1.5') + p + q + r)))
            w2d = max(w2d, abs(octm / dirm - 1))
ok2d = w2d < M('1e-40')
ok2 = ok2a and ok2b and ok2c and ok2d
results['P2'] = (ok2, f"pushforward = Cauchy(g(z)) to {mp.nstr(w2a, 3)}; turns move i by {mp.nstr(mi, 3)}, "
                      f"least move of z != i {mp.nstr(moved, 3)}; arcsine = even turn's foot to {mp.nstr(w2c, 3)}; "
                      f"Fisher-Rao length - 2θ {mp.nstr(w2fr, 3)}; octant moments = Dirichlet(½,½,½) to {mp.nstr(w2d, 3)}")

# ---------------------------------------------------------------- P3: the exchange fixes the corner and the median
ok3a = all((s == 1) == (1 / s == s) for s in [rat() for _ in range(200)] + [F(1)])
ok3b = True
for _ in range(200):
    s = rat()
    if 1 / (1 + s) ** 2 != (1 / (1 + 1 / s) ** 2) / s ** 2: ok3b = False      # the line, read as v/h
    if 1 / (1 + s * s) != (1 / (1 + 1 / s ** 2)) / s ** 2: ok3b = False        # the even turn, read as v/h
    if 1 / s != (1 / (1 / s)) / s ** 2: ok3b = False                            # the levels
# the arcsine through its CDF: F(t) + F(1 - t) = 1
arc = lambda t: (2 / mp.pi) * mp.asin(mp.sqrt(t))
w3 = max(abs(arc(M(i) / 1000) + arc(1 - M(i) / 1000) - 1) for i in range(1, 1000))
K = M(1000)
hald_below = lambda t: (mp.log(t / (1 - t)) + mp.log(K)) / (2 * mp.log(K))     # ds/s on [1/K, K], s = t/(1-t)
med = [abs(M('0.5') - M('0.5')), abs(arc(M('0.5')) - M('0.5')), abs(hald_below(M('0.5')) - M('0.5'))]
below = [M('0.25'), arc(M('0.25')), hald_below(M('0.25'))]
ok3 = ok3a and ok3b and w3 < M('1e-50') and max(med) < M('1e-50') and len({mp.nstr(b, 10) for b in below}) == 3
results['P3'] = (ok3, f"fixed point only at 1; f(s) = f(1/s)/s² exactly for the line, the turn, the levels: {ok3b}; "
                      f"arcsine symmetric to {mp.nstr(w3, 3)}; medians at ½; below t = ¼: "
                      f"{', '.join(mp.nstr(b, 4) for b in below)}")

# ---------------------------------------------------------------- P4: the location-scale prior on (theta, kappa)
ok4a = True
for _ in range(200):
    th, ka, al, lam = rat(), rat(), rat(), rat()
    f = lambda th_, ka_: 1 / ka_                        # density of d theta d kappa / kappa
    # a turn: (th + al, ka), Jacobian 1
    if f(th, ka) != f(th + al, ka) * 1: ok4a = False
    # a rescaling: (th, lam ka), Jacobian lam
    if f(th, ka) != f(th, lam * ka) * lam: ok4a = False
    # the exchange: (1/4 - th, 1/ka) in turns, Jacobian |-1| * 1/ka^2
    if f(th, ka) != f(F(1, 4) - th, 1 / ka) * (1 / ka ** 2): ok4a = False
ok4b = (F(1, 4) - F(1, 8) == F(1, 8)) and (1 / F(1) == F(1))      # 45 degrees = 1/8 turn; kappa = 1
def qlog(lo, hi):
    """the integral of 1/k from lo to hi by quadrature, split at every power of 10 between"""
    pts = [lo] + [M(10) ** e for e in range(int(mp.ceil(mp.log10(lo))), int(mp.floor(mp.log10(hi))) + 1)
                  if lo < M(10) ** e < hi] + [hi]
    return mp.quad(lambda k: 1 / k, pts)
w4 = M(0)
for _ in range(100):
    lo = M(10) ** M(rng.uniform(-6, 6)); hi = lo * M(10) ** M(rng.uniform(0.01, 6))
    half = qlog(lo, hi) / 2
    m = mp.findroot(lambda x: qlog(lo, x) - half, (lo, hi), solver='illinois')   # bracketed, never leaves [lo, hi]
    w4 = max(w4, abs(m / mp.sqrt(lo * hi) - 1))
ok4 = ok4a and ok4b and w4 < M('1e-45')
results['P4'] = (ok4, f"dθ·dκ/κ unchanged by turns, rescalings and the exchange, exactly: {ok4a}; fixed point "
                      f"(45°, κ = 1); median of dκ/κ on bounds = √(V₋V₊) to {mp.nstr(w4, 3)}")

# ---------------------------------------------------------------- P5: Jaynes 1973 rederived; the situated version
ok5a = True
for _ in range(50):
    m_, k_ = rng.randint(1, 30), rng.randint(1, 30)
    n = (F(m_ * m_ - k_ * k_, m_ * m_ + k_ * k_), F(2 * m_ * k_, m_ * m_ + k_ * k_))   # a rational unit normal
    c = (F(rng.randint(-60, 60), rng.randint(1, 9)), F(rng.randint(-60, 60), rng.randint(1, 9)))
    R = rat()
    cn = c[0] * n[0] + c[1] * n[1]
    cut = (cn - R, cn + R)                                   # the p whose line cuts the circle
    longer = (cn - R / 2, cn + R / 2)                         # distance from the centre below R/2
    if (longer[1] - longer[0]) / (cut[1] - cut[0]) != F(1, 2): ok5a = False
w5b = M(0)
for q in [M('0.3'), M(1), M(2), M('3.7')]:
    R = M('2.5')
    f = lambda r: q * r ** (q - 2) / (2 * mp.pi * R ** q)
    w5b = max(w5b, abs(hq(lambda r: f(r) * 2 * mp.pi * r, [0, R]) - 1))
    for a in [M('0.2'), M('0.5'), M('0.9')]:
        inner = hq(lambda r: f(r) * 2 * mp.pi * r, [0, a * R])
        for r in [M('0.1'), M('0.3') * a * R]:
            same = q * r ** (q - 2) / (2 * mp.pi * (a * R) ** q)
            w5b = max(w5b, abs(f(r) / inner / same - 1))
    w5b = max(w5b, abs(hq(lambda r: f(r) * 2 * mp.pi * r, [0, R / 2]) - M(2) ** (-q)))
# the random-endpoint law, per unit area: (2/pi)/sqrt(R^2 - r^2) / (2 pi r)
R = M(1)
g = lambda r: (2 / mp.pi) / mp.sqrt(R * R - r * r) / (2 * mp.pi * r)
endp = hq(lambda r: g(r) * 2 * mp.pi * r, [0, R / 2])
r1, r2, r3 = M('0.2'), M('0.5'), M('0.8')
qfit = 2 + mp.log(g(r2) / g(r1)) / mp.log(r2 / r1)          # q - 2 is the slope of log f against log r
fits = abs(g(r3) / g(r1) - (r3 / r1) ** (qfit - 2)) < M('1e-6')
ok5b = w5b < M('1e-50') and abs(endp - M(1) / 3) < M('1e-50') and not fits
sit = lambda R_, D_: mp.asin(R_ / (2 * D_)) / mp.asin(R_ / D_)
on_circle = abs(sit(M(1), M(1)) - M(1) / 3)
Ds = [M(1) + M(10) ** M(-3 + 12 * i / 199) for i in range(200)]
incr = all(sit(M(1), Ds[i + 1]) > sit(M(1), Ds[i]) for i in range(199))
far = abs(sit(M(1), M(10) ** 8) - M('0.5'))
scale_free = max(abs(sit(M(7) * R_, M(7) * D_) - sit(R_, D_)) for R_, D_ in [(M(1), M(2)), (M(3), M(5))])
# a seeded count of even rays from home at D = 2R
mc = random.Random(1973)
D, Rr = 2.0, 1.0
cutn = longn = 0
import math
for _ in range(10 ** 6):
    phi = mc.uniform(-math.pi / 2, math.pi / 2)             # a line through home, by its angle to the centre
    dist = D * abs(math.sin(phi))                            # the centre's distance from the line
    if dist < Rr:
        cutn += 1
        if dist < Rr / 2: longn += 1
p = float(sit(M(1), M(2)))
se = math.sqrt(p * (1 - p) / cutn)
ok5c = on_circle < M('1e-50') and incr and far < M('1e-15') and scale_free < M('1e-50') and abs(longn / cutn - p) < 4 * se
ok5 = ok5a and ok5b and ok5c
results['P5'] = (ok5, f"Crofton: ½ at every centre and radius, exactly: {ok5a}; the family normalized and kept under "
                      f"scale, 2^-q, to {mp.nstr(w5b, 3)}; endpoints ⅓ ({mp.nstr(endp, 6)}), fits a power: {fits}; "
                      f"situated: ⅓ on the circle ({mp.nstr(on_circle, 3)} off), rising: {incr}, "
                      f"½ − {mp.nstr(far, 3)} at 10⁸R, {mp.nstr(sit(M(1), M(2)), 6)} at D = 2R "
                      f"(counted {longn / cutn:.5f} ± {se:.5f})")

# ---------------------------------------------------------------- P6: the situated group's measure is log-polar
def invariant(f, x, y, ar, ai):
    """f(z) = f(az)·|J| for z -> az, the Jacobian |a|^2."""
    X, Y = ar * x - ai * y, ar * y + ai * x
    return f(x, y) == f(X, Y) * (ar * ar + ai * ai)
ok6 = True
area_passes = False
for _ in range(200):
    x, y = F(rng.randint(-60, 60), rng.randint(1, 9)), F(rng.randint(-60, 60), rng.randint(1, 9))
    if x == 0 and y == 0: continue
    ar, ai = F(rng.randint(-9, 9), rng.randint(1, 5)), F(rng.randint(-9, 9), rng.randint(1, 5))
    if ar == 0 and ai == 0: continue
    if not invariant(lambda x_, y_: 1 / (x_ * x_ + y_ * y_), x, y, ar, ai): ok6 = False
    if ar * ar + ai * ai != 1 and invariant(lambda x_, y_: F(1), x, y, ar, ai): area_passes = True
ok6 = ok6 and not area_passes
results['P6'] = (ok6, f"dx·dy/(x²+y²) unchanged by every z -> az, exactly: {ok6}; area passes for some |a| ≠ 1: {area_passes}")

# ---------------------------------------------------------------- P7: the drawings on a hyperbolic line
hdist = lambda z, w: mp.acosh(1 + abs(z - w) ** 2 / (2 * mp.im(z) * mp.im(w)))
w7a = M(0)
for c in [M('0.01'), M('0.5'), M(1), M(3), M(250)]:
    for i in range(1, 401):
        x = M(-50) + M(100) * i / 401
        even = (mp.atan(x / c) + mp.pi / 2) / mp.pi             # share of the even turn with c tan theta <= x
        cdf = mp.quad(lambda u: c / (mp.pi * (c * c + u * u)), [-mp.inf, min(x, M(0)), x] if x > 0 else [-mp.inf, x])
        w7a = max(w7a, abs(even - cdf))
w7b = max(abs(hdist(mp.mpc(0, 1), mp.mpc(0, c)) - abs(mp.log(c)))
          for c in [M(10) ** M(-9 + 18 * i / 199) for i in range(200)])
w7c = M(0)
for _ in range(100):
    while True:
        g = [M(rng.uniform(-3, 3)) for _ in range(4)]
        if g[0] * g[3] - g[1] * g[2] > M('0.1'): break
    for _ in range(100):
        z = mp.mpc(rng.uniform(-3, 3), rng.uniform(0.05, 3)); w = mp.mpc(rng.uniform(-3, 3), rng.uniform(0.05, 3))
        d0 = hdist(z, w)
        w7c = max(w7c, abs(hdist(mob(g, z), mob(g, w)) / d0 - 1), abs(hdist(1 / mp.conj(z), 1 / mp.conj(w)) / d0 - 1))
ok7 = w7a < M('1e-50') and w7b < M('1e-50') and w7c < M('1e-40')
results['P7'] = (ok7, f"readings at V = cH Cauchy(0, c) to {mp.nstr(w7a, 3)}; distance i to ci = |ln c| to "
                      f"{mp.nstr(w7b, 3)}; kept by maps and the exchange to {mp.nstr(w7c, 3)}")

for k, (ok, msg) in results.items():
    print(f"{k}: {verdict(ok)}. {msg}")
