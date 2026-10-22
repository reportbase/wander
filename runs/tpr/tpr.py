"""TPR: 2/π revisited, as address and payload. See plans/tpr-plan.md (predictions written before this script).

A fair weight w(θ) on the quadrant [0, π/2]: reciprocal-symmetric (w(θ) = w(π/2 − θ)), mean 1 (total π/2, as the
uniform turn's); extended to the whole turn with period π/2 where an entry needs it. mpmath, 50 digits (quadratures at
100, split at every multiple of π/4 and at every kink of the integrand).
Run from the repository's root: python3 runs/tpr/tpr.py | tee runs/tpr/tpr-run1.txt
"""
from mpmath import (mp, mpf, pi, quad, sin, cos, tan, atan, asin, acos, sqrt, log, agm, findroot, nstr, floor, inf)

mp.dps = 50
TWO_PI = 2 / pi
Q4 = pi / 4

def Q(f, pts):
    pts = sorted(set(pts))
    with mp.workdps(100):
        return +quad(f, pts)

def grid(a, b, extra=()):
    """Breakpoints: a, b, every multiple of π/4 between, and any extra kinks."""
    pts = [a, b] + [k * Q4 for k in range(int(floor(a / Q4)), int(floor(b / Q4)) + 2) if a < k * Q4 < b]
    pts += [x for x in extra if a < x < b]
    return pts

# ---- the weights (on the quadrant; each of mean 1 there) ----
def fold(th):           # θ reduced to [0, π/2): the weight's period
    return th - (pi / 2) * floor(th / (pi / 2))
def w_line(th):         # the line h + v = 1 swept uniformly along its length: dl/dθ ∝ 1/(cos θ + sin θ)²; ∫ = 1
    t = fold(th); return (pi / 2) / (cos(t) + sin(t)) ** 2
def w_square(th):       # the square's edges, length 2; dl/dθ = sec²θ to the corner, mirrored past it
    t = fold(th); t = min(t, pi / 2 - t); return (pi / 2) / cos(t) ** 2 / 2
NORM_A = {}
def w_pow(a):           # w_a ∝ sin^a(2θ), normalised to mean 1 on the quadrant
    a = mpf(a)
    if a not in NORM_A:
        NORM_A[a] = (pi / 2) / Q(lambda t: abs(sin(2 * t)) ** a, [0, Q4, pi / 2])
    c = NORM_A[a]
    return lambda th: c * abs(sin(2 * fold(th))) ** a if a != 0 else mpf(1)   # (abs: rounding left sin(2θ) a hair below 0 at an end, and a negative a then gave a complex power; the first launch crashed there, before any P2 value)
def w_unif(th): return mpf(1)

def E(f, w, extra=()):  # mean over the quadrant under w
    return Q(lambda t: f(t) * w(t), grid(0, pi / 2, extra)) / (pi / 2)
def W(w, th):           # the share of the quadrant's weight below θ
    return Q(w, grid(0, th)) / (pi / 2) if th > 0 else mpf(0)
def theta_med(w):       # the θ where half the weight lies below
    lo, hi = mpf(0), pi / 2
    for _ in range(190):
        mid = (lo + hi) / 2
        if W(w, mid) < mpf(1) / 2: lo = mid
        else: hi = mid
    return (lo + hi) / 2

verdicts = {}
def say(*a): print(*a)

# =====================================================================================================================
say("P1: the three paths, each swept uniformly along its own length")
paths = {'circle': w_unif, 'line': w_line, 'square': w_square}
want = {
    'circle': {'cos': TWO_PI, 'sin2': TWO_PI},
    'line':   {'cos': sqrt(2) / 2 * log(1 + sqrt(2)), 'sin2': pi / 2 - 1},
    'square': {'cos': (log(1 + sqrt(2)) + sqrt(2) - 1) / 2, 'sin2': log(2)},
}
p1 = True
for name, w in paths.items():
    ec, es = E(cos, w), E(lambda t: sin(2 * t), w)
    ec2, ec2t = E(lambda t: cos(t) ** 2, w), E(lambda t: cos(2 * t), w)
    tm = theta_med(w); medcos = cos(tm)
    say(f"  {name:6s}: E[cos θ] = {nstr(ec, 20)} (stated {nstr(want[name]['cos'], 20)}); "
        f"E[sin 2θ] = {nstr(es, 20)} (stated {nstr(want[name]['sin2'], 20)})")
    say(f"          E[cos²θ] = {nstr(ec2, 20)}, E[cos 2θ] = {nstr(ec2t, 5)}, median θ = {nstr(tm, 20)}, median cos θ = {nstr(medcos, 20)}")
    tol = mpf(10) ** -30
    ok = abs(ec - want[name]['cos']) < tol and abs(es - want[name]['sin2']) < tol and abs(ec2 - mpf(1) / 2) < tol \
        and abs(ec2t) < tol and abs(medcos - 1 / sqrt(2)) < tol
    if name != 'circle':
        ok = ok and abs(ec - TWO_PI) > mpf(10) ** -3 and abs(es - TWO_PI) > mpf(10) ** -3
    p1 &= ok
verdicts['P1'] = p1
say(f"P1: {'not killed' if p1 else 'KILLED'}\n")

# =====================================================================================================================
say("P2: the family w_a ∝ sin^a(2θ)")
A = ['-0.9', '-0.5', '0', '0.5', '1', '2', '4']
rows = []
p2 = True
for a in A:
    w = w_pow(a)
    tm = theta_med(w)
    meds = [cos(tm), sin(tm) ** 2, tan(tm) / (1 + tan(tm)), tm / (pi / 2)]
    corner = [1 / sqrt(2), mpf(1) / 2, mpf(1) / 2, mpf(1) / 2]
    dmed = max(abs(m - c) for m, c in zip(meds, corner))
    ec2 = E(lambda t: cos(t) ** 2, w)
    ec, es = E(cos, w), E(lambda t: sin(2 * t), w)
    rows.append((mpf(a), ec, es))
    say(f"  a = {a:>5s}: median off the corner by {nstr(dmed, 3)}; E[cos²θ] − ½ = {nstr(ec2 - mpf(1)/2, 3)}; "
        f"E[cos θ] = {nstr(ec, 15)}; E[sin 2θ] = {nstr(es, 15)}")
    p2 &= dmed < mpf(10) ** -30 and abs(ec2 - mpf(1) / 2) < mpf(10) ** -30
    if a != '0':
        p2 &= abs(ec - TWO_PI) > mpf(10) ** -6 and abs(es - TWO_PI) > mpf(10) ** -6
    else:
        p2 &= abs(ec - TWO_PI) < mpf(10) ** -30 and abs(es - TWO_PI) < mpf(10) ** -30
inc = all(rows[i + 1][1] > rows[i][1] and rows[i + 1][2] > rows[i][2] for i in range(len(rows) - 1))
say(f"  both means strictly increasing in a: {inc}")
p2 &= inc
verdicts['P2'] = p2
say(f"P2: {'not killed' if p2 else 'KILLED'}\n")

# =====================================================================================================================
say("P3: a fair, non-uniform weight with E[cos θ] = 2/π")
w2 = w_pow('2')
EL, E2 = E(cos, w_line), E(cos, w2)
lam = (TWO_PI - EL) / (E2 - EL)
mix = lambda t: (1 - lam) * w_line(t) + lam * w2(t)
emix = E(cos, mix)
c4 = E(lambda t: cos(4 * t), mix)
s2 = E(lambda t: sin(2 * t), mix)
say(f"  λ = {nstr(lam, 20)}; E_mix[cos θ] − 2/π = {nstr(emix - TWO_PI, 3)}; E_mix[cos 4θ] = {nstr(c4, 15)} "
    f"(uniform 0); E_mix[sin 2θ] = {nstr(s2, 15)} (uniform {nstr(TWO_PI, 15)})")
p3 = 0 < lam < 1 and abs(emix - TWO_PI) < mpf(10) ** -30 and abs(c4) > mpf(10) ** -3
verdicts['P3'] = p3
say(f"P3: {'not killed' if p3 else 'KILLED'}\n")

# =====================================================================================================================
say("P4: the whole turn, the mean shadow on the axis at φ, E|cos(θ − φ)|")
def Efull(f, w, extra=()):
    return Q(lambda t: f(t) * w(t), grid(0, 2 * pi, extra)) / (2 * pi)
def kinks(phi):          # where cos(θ − φ) changes sign in [0, 2π]
    return [fold_full(phi + pi / 2), fold_full(phi + 3 * pi / 2)]
def fold_full(x): return x - 2 * pi * floor(x / (2 * pi))
cases = [
    ('1 + ½cos θ', lambda t: 1 + cos(t) / 2, lambda phi: TWO_PI),
    ('1 + ½cos 2θ', lambda t: 1 + cos(2 * t) / 2, lambda phi: TWO_PI + cos(2 * phi) / (3 * pi)),
    ('1 + ½cos 4θ', lambda t: 1 + cos(4 * t) / 2, lambda phi: TWO_PI - cos(4 * phi) / (15 * pi)),
]
p4 = True
for name, w, f in cases:
    vals = []
    for phi in [mpf(0), mpf('0.3'), mpf(1), pi / 2]:
        v = Efull(lambda t: abs(cos(t - phi)), w, kinks(phi))
        vals.append(f"{nstr(v, 15)}")
        p4 &= abs(v - f(phi)) < mpf(10) ** -30
    say(f"  w = {name:12s}: φ = 0, 0.3, 1, π/2 → " + ", ".join(vals))
verdicts['P4'] = p4
say(f"P4: {'not killed' if p4 else 'KILLED'}\n")

# =====================================================================================================================
say("P6: the catalogue's constants under three fair, non-uniform weights (line, square, w₂)")
WEIGHTS = [('uniform', w_unif), ('line', w_line), ('square', w_square), ('w2', w2)]
T = mpf(1) / 2
sat = lambda x: max(-T, min(T, x))
k9 = mpf('0.6')
def wedge_D(w, alpha):   # share of directions g with sgn cos g ≠ sgn cos(g − α)
    ex = [pi / 2, pi / 2 + alpha, 3 * pi / 2, 3 * pi / 2 + alpha]
    return Q(lambda g: w(g) if (cos(g) > 0) != (cos(g - alpha) > 0) else 0, grid(0, 2 * pi, [fold_full(x) for x in ex])) / (2 * pi)
def kendall(w, rho):     # 4·P(positive whitened wedge) − 1, the wedge of angle acos(−ρ) set about the corner
    al = acos(-rho); a, b = Q4 - al / 2, Q4 + al / 2
    a2, b2 = fold_full(a), b
    if a < 0:
        P = (Q(w, grid(a2, 2 * pi)) + Q(w, grid(0, b))) / (2 * pi)
    else:
        P = Q(w, grid(a, b)) / (2 * pi)
    return 4 * P - 1
ENTRIES = [
    # (class, name, f(w), uniform value as written)
    ('M', 'K5/C14/C34 mean |sin| (full turn)', lambda w: Efull(lambda t: abs(sin(t)), w, [pi]), TWO_PI),
    ('M', 'K2/K6/C20/C33 mean |cos| (full turn)', lambda w: Efull(lambda t: abs(cos(t)), w, [pi / 2, 3 * pi / 2]), TWO_PI),
    ('M', 'C15/C43/K12 mean half-angle chord, heading on [0, π]', lambda w: Q(lambda p: sin(p / 2) * w(p), grid(0, pi)) / pi, TWO_PI),
    ('M', 'C9 (2/π)K(0.6) as a mean = 1/agm', lambda w: E(lambda t: 1 / sqrt(1 - k9 ** 2 * sin(t) ** 2), w), 1 / agm(1, sqrt(1 - k9 ** 2))),
    ('M', 'C35 saturation describing function, T/A = ½',
     lambda w: Q(lambda t: sat(sin(t)) * sin(t) * w(t), grid(0, 2 * pi, [asin(T), pi - asin(T), pi + asin(T), 2 * pi - asin(T)])) / pi,
     TWO_PI * (asin(T) + T * sqrt(1 - T ** 2))),
    ('M', 'C3 square-wave coefficient ∫sin/(2∫sin²) on [0, π]',
     lambda w: Q(lambda t: sin(t) * w(t), grid(0, pi)) / (2 * Q(lambda t: sin(t) ** 2 * w(t), grid(0, pi))), TWO_PI),
    ('L', 'K15 Flamant 1/∫cos² over the half turn', lambda w: 1 / Q(lambda t: cos(t) ** 2 * w(t), grid(-pi / 2, pi / 2)) if True else 0, TWO_PI),
    ('L', 'K18 Sato–Tate 1/∫sin² on [0, π]', lambda w: 1 / Q(lambda t: sin(t) ** 2 * w(t), grid(0, pi)), TWO_PI),
    ('L', 'C28 Irwin 1/∫dφ over the quarter turn', lambda w: 1 / Q(w, grid(0, pi / 2)), TWO_PI),
    ('Bc', 'K1 half-Cauchy P(v/h ≤ 1)', lambda w: W(w, atan(1)), mpf(1) / 2),
    ('Bc', 'K4 arcsine P(x ≤ ½)', lambda w: W(w, asin(sqrt(mpf(1) / 2))), mpf(1) / 2),
    ('Bc', 'K7 Van Vleck E[sgn sgn] at ρ = 0', lambda w: 1 - 2 * wedge_D(w, pi / 2), mpf(0)),
    ('Bc', 'C21 Bell P + 1 at θ = π/2', lambda w: 2 * wedge_D(w, pi / 2), mpf(1)),
    ('Bc', "C13 Kendall's τ at ρ = 0", lambda w: kendall(w, mpf(0)), mpf(0)),
    ('Bo', 'K1 half-Cauchy P(v/h ≤ 3)', lambda w: W(w, atan(3)), TWO_PI * atan(3)),
    ('Bo', 'K4 arcsine P(x ≤ 0.3)', lambda w: W(w, asin(sqrt(mpf('0.3')))), TWO_PI * asin(sqrt(mpf('0.3')))),
    ('Bo', 'K7 Van Vleck at α = 0.9', lambda w: 1 - 2 * wedge_D(w, mpf('0.9')), TWO_PI * asin(cos(mpf('0.9')))),
    ('Bo', 'C21 Bell P + 1 at θ = 1.1', lambda w: 2 * wedge_D(w, mpf('1.1')), TWO_PI * mpf('1.1')),
    ('Bo', "C13 Kendall's τ at ρ = ½", lambda w: kendall(w, mpf(1) / 2), TWO_PI * asin(mpf(1) / 2)),
]
p6 = True
for cls, name, f, target in ENTRIES:
    vals = {wn: f(w) for wn, w in WEIGHTS}
    ok_u = abs(vals['uniform'] - target) < mpf(10) ** -30
    moves = {wn: vals[wn] - vals['uniform'] for wn in ('line', 'square', 'w2')}
    if cls in ('M', 'Bo'):
        ok = all(abs(d) > mpf(10) ** -6 for d in moves.values()); expect = 'moves'
    else:
        ok = all(abs(d) < mpf(10) ** -40 for d in moves.values()); expect = 'stays'
    p6 &= ok and ok_u
    say(f"  [{cls:2s}] {name}: uniform {nstr(vals['uniform'], 12)} ({'matches' if ok_u else 'DOES NOT MATCH'} as written); "
        f"shift line {nstr(moves['line'], 4)}, square {nstr(moves['square'], 4)}, w2 {nstr(moves['w2'], 4)} "
        f"→ predicted {expect}: {'yes' if ok else 'NO'}")
verdicts['P6'] = p6
say(f"P6: {'not killed' if p6 else 'KILLED'}\n")

say("verdicts: " + ", ".join(f"{k} {'not killed' if v else 'KILLED'}" for k, v in verdicts.items()))
say("(P5 is the classification count, scored in runs/tpr/sorted.md)")
