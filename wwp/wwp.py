"""WWP: water and wine, Jaynes's open case. See plans/wwp-plan.md (P1-P4).

x is the ratio of wine to water. A change of one party's unit multiplies x by a constant; the exchange of the parties
sends x to 1/x. Rational candidates in exact arithmetic (fractions); the rest with mpmath at 50 digits.
Run: python3 wwp/wwp.py   (a few seconds; needs mpmath)
"""
from fractions import Fraction as F
import random
import mpmath as mp
mp.mp.dps = 50
M = mp.mpf
rng = random.Random(1928)
def rat(lo=1, hi=60): return F(rng.randint(lo, hi), rng.randint(lo, hi))
def verdict(ok): return "not killed" if ok else "KILLED"
results = {}

# ---------------------------------------------------------------- P1: the unit leaves the powers; the exchange picks 1/x
powers = {p: (lambda p: (lambda x: x ** p))(p) for p in [F(-3), F(-2), F(-1), F(-1, 2), F(0), F(1)]}
others_exact = {'even share 2/(1+x)^2': lambda x: 2 / (1 + x) ** 2, 'even turn 1/(1+x^2)': lambda x: 1 / (1 + x * x),
                'average 1+1/x^2': lambda x: 1 + 1 / (x * x)}
others_mp = {'hyperbola sqrt(1+1/x^4)': lambda x: mp.sqrt(1 + 1 / x ** 4), 'exp(-x)': lambda x: mp.exp(-x)}
triples = [(rat(), rat(), rat()) for _ in range(200)]
triples = [(a, b, l) for a, b, l in triples if a != b and l != 1]
def scale_ok_exact(f):
    out = True
    for x1, x2, lam in triples:
        if isinstance(f(F(4)), F):                       # a rational function: exact
            if f(lam * x1) * f(x2) != f(lam * x2) * f(x1): out = False
        else:
            v = lambda x: mp.mpf(x.numerator) / x.denominator
            if abs(f(v(lam * x1)) * f(v(x2)) - f(v(lam * x2)) * f(v(x1))) > M('1e-40') * abs(f(v(lam * x1)) * f(v(x2))):
                out = False
    return out
def scale_ok_mp(f):
    v = lambda x: mp.mpf(x.numerator) / x.denominator
    return all(abs(f(v(lam * x1)) * f(v(x2)) - f(v(lam * x2)) * f(v(x1))) <= M('1e-40') * abs(f(v(lam * x1)) * f(v(x2)))
               for x1, x2, lam in triples)
pass_scale = {}
for p, f in powers.items():
    if p.denominator == 1:
        pass_scale[f'x^{p}'] = scale_ok_exact(f)
    else:
        pass_scale[f'x^{p}'] = scale_ok_mp(lambda x, p=p: mp.power(x, mp.mpf(p.numerator) / p.denominator))
for k, f in others_exact.items(): pass_scale[k] = scale_ok_exact(f)
for k, f in others_mp.items(): pass_scale[k] = scale_ok_mp(f)
ok1a = all(v for k, v in pass_scale.items() if k.startswith('x^')) and not any(v for k, v in pass_scale.items() if not k.startswith('x^'))
# (b) the exchange: density f(x) dx goes to f(1/y)/y^2 dy; a power x^p goes to y^(-2-p)
self_image = []
for p in [F(n, 4) for n in range(-16, 9)]:
    img = -2 - p
    same = (img == p)
    # and check pointwise on rationals that x^p, pushed through the exchange, is y^(-2-p)
    if p.denominator == 1:
        for _ in range(20):
            y = rat()
            if (1 / y) ** p / y ** 2 != y ** img: same = None
    if same: self_image.append(p)
ok1b = self_image == [F(-1)]
ok1 = ok1a and ok1b
results['P1'] = (ok1, f"pass the unit's change: {[k for k, v in pass_scale.items() if v]}; powers their own image under the exchange: {[str(p) for p in self_image]}")

# ---------------------------------------------------------------- P2: fairness fixes the corner
a, b = M(1) / 3, M(3)
def prob(f, lo, c, hi):
    return mp.quad(f, [lo, min(c, hi)]) / mp.quad(f, [lo, hi])
fair = {
    'average': lambda x: 1 + 1 / x ** 2,
    'even share (Mikkelson)': lambda x: 2 / (1 + x) ** 2,
    'hyperbola (Burock)': lambda x: mp.sqrt(1 + 1 / x ** 4),
    'levels': lambda x: 1 / x,
    'even turn': lambda x: 1 / (1 + x * x),
}
unfair = {'over x': lambda x: M(1), 'over 1/x': lambda x: 1 / x ** 2}
P2 = {k: (prob(f, a, M(1), b), prob(f, a, M(2), b)) for k, f in {**fair, **unfair}.items()}
fair_mid = max(abs(P2[k][0] - M('0.5')) for k in fair)
# exact values
mik = F(3, 2) - F(2, 3)                       # P = 3/2 - 2/(x+1) at x = 2
avg = (F(5, 8) + F(15, 16)) / 2
ok2 = fair_mid < M('1e-45')
ok2 = ok2 and abs(P2['even share (Mikkelson)'][1] - M(5) / 6) < M('1e-45') and mik == F(5, 6)
ok2 = ok2 and abs(P2['average'][1] - M(25) / 32) < M('1e-45') and avg == F(25, 32)
ok2 = ok2 and mp.nstr(P2['hyperbola (Burock)'][1], 3) == '0.764'
ok2 = ok2 and abs(P2['levels'][1] - mp.log(6) / mp.log(9)) < M('1e-45')
ok2 = ok2 and abs(P2['even turn'][1] - (mp.pi / 4) / (mp.atan(3) - mp.atan(M(1) / 3))) < M('1e-45')
ok2 = ok2 and abs(mp.atan(2) - mp.atan(M(1) / 3) - mp.pi / 4) < M('1e-48')
ok2 = ok2 and abs(P2['over x'][1] - M(5) / 8) < M('1e-45') and abs(P2['over 1/x'][1] - M(15) / 16) < M('1e-45')
ok2 = ok2 and abs(P2['over x'][0] - M('0.25')) < M('1e-45') and abs(P2['over 1/x'][0] - M('0.75')) < M('1e-45')
# Parker and Jeynes's exponential law: fair for no lambda > 0
pj_fair = [lam for lam in [M('0.1'), M('0.5'), M(1), M(2)]
           if all(abs(mp.exp(-lam * x) - mp.exp(-lam / x) / x ** 2) < M('1e-30') for x in [M('0.5'), M(2), M('2.5')])]
ok2 = ok2 and pj_fair == []
results['P2'] = (ok2, "; ".join(f"{k}: P(x≤1) {mp.nstr(v[0], 6)}, P(x≤2) {mp.nstr(v[1], 6)}" for k, v in P2.items())
                 + f"; e^(-λx) fair at no λ tried: {pj_fair == []}")

# ---------------------------------------------------------------- P3: only the levels survive a change of one unit
def methods(lam):
    lo, c, hi = lam / 3, 2 * lam, 3 * lam
    t = lambda x: x / (1 + x)
    over_x = (c - lo) / (hi - lo)
    over_y = (1 / lo - 1 / c) / (1 / lo - 1 / hi)
    return {
        'levels': mp.log(c / lo) / mp.log(hi / lo),
        'even share': (t(c) - t(lo)) / (t(hi) - t(lo)),
        'even turn': (mp.atan(c) - mp.atan(lo)) / (mp.atan(hi) - mp.atan(lo)),
        'hyperbola': prob(lambda x: mp.sqrt(1 + 1 / x ** 4), lo, c, hi),
        'average': (over_x + over_y) / 2,
    }
base = methods(M(1))
lv_move = max(abs(methods(l)['levels'] - base['levels']) for l in [M(2), M('0.99'), M('1e-3'), M('1e3')])
at2 = methods(M(2)); at099 = methods(M('0.99'))
others_still = [k for k in base if k != 'levels' and abs(at2[k] - base[k]) < M('1e-6')]
ok3 = lv_move < M('1e-45') and others_still == []
results['P3'] = (ok3, f"levels move by {mp.nstr(lv_move, 3)}; at λ = 2: " + ", ".join(f"{k} {mp.nstr(base[k], 5)} -> {mp.nstr(at2[k], 5)}" for k in base)
                 + "; at λ = 0.99: " + ", ".join(f"{k} {mp.nstr(at099[k], 6)}" for k in base))

# ---------------------------------------------------------------- P4: Jaynes's form
w4 = M(0)
for L in [2, 10, 40]:
    hi = M(2) ** L
    pts = [M(3)] + [M(2) ** k for k in range(2, L + 1)]          # split at every doubling: a wide range, one level a piece
    lv = mp.quad(lambda x: 1 / x, pts) / (mp.quad(lambda x: 1 / x, [M(1), M(2)]) + mp.quad(lambda x: 1 / x, [M(2)] + pts[1:]) if L > 1 else 1)
    lv = mp.quad(lambda x: 1 / x, pts) / mp.quad(lambda x: 1 / x, [M(1), M(2)] + pts[1:]) if L >= 2 else lv
    w4 = max(w4, abs(lv - (1 - mp.log(3, 2) / L)))
share = (1 - M(3) / 4) / (1 - M(1) / 2)                     # wine share t even on [1/2, 1]; t >= 3/4
turn = (mp.pi / 2 - mp.atan(3)) / (mp.pi / 4)
ok4 = w4 < M('1e-45') and abs(share - M('0.5')) < M('1e-48')
results['P4'] = (ok4, f"levels on [1, 2^L] = 1 - log2(3)/L to {mp.nstr(w4, 3)} (L = 2: {mp.nstr(1 - mp.log(3, 2) / 2, 5)}, "
                      f"10: {mp.nstr(1 - mp.log(3, 2) / 10, 5)}, 40: {mp.nstr(1 - mp.log(3, 2) / 40, 5)}); even share {mp.nstr(share, 5)}; even turn {mp.nstr(turn, 6)}")

for k, (ok, msg) in results.items():
    print(f"{k}: {verdict(ok)}. {msg}")
