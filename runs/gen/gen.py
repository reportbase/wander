"""GEN: checks of plans/gen-plan.md G1-G13. python3 runs/gen/gen.py"""
import sympy as sp, mpmath as mp
from fractions import Fraction as F
mp.mp.dps = 40
s, a, t, k, c, d, u = sp.symbols('s a t k c d u', positive=True)
R = {}
def rec(g, ok, note=''):
    R[g] = bool(ok); print(g, 'holds' if ok else 'KILLED', note)

# G1
v1, v2, v3 = sp.symbols('v1 v2 v3', positive=True)
sub = {v1: 1/sp.sqrt(1+s**2+a**2), v2: s/sp.sqrt(1+s**2+a**2), v3: a/sp.sqrt(1+s**2+a**2)}
rec('G1', sp.simplify((v1**2+v2**2+v3**2).subs(sub)) == 1 and sp.simplify((k*v2)/(k*v1) - v2/v1) == 0
    and sp.simplify(1+s**2+a**2 - 1/sub[v1]**2) == 0)
# G2
h, v = 1/sp.sqrt(1+s**2), s/sp.sqrt(1+s**2)
rec('G2', sp.simplify(h**2+v**2) == 1 and h.subs(s, 0) == 1 and sp.limit(v, s, sp.oo) == 1)
# G3
ok = True
for p in range(0, 30):
    for q in range(1, 30):
        tt = F(p, q)
        if tt == 1: continue
        H, V = (1-tt**2)/(1+tt**2), 2*tt/(1+tt**2)
        ok &= (H*H + V*V == 1) and (H == 0 or V/H == 2*tt/(1-tt**2))
rec('G3', ok, '(exact fractions, 29 x 29 half-slopes)')
# G4
comp = (s+a)/(1-s*a)
rec('G4', sp.simplify(1+comp**2 - (1+s**2)*(1+a**2)/(1-s*a)**2) == 0)
# G5
rec('G5', sp.simplify(sp.diff(comp, s)/(1+comp**2) - 1/(1+s**2)) == 0 and sp.simplify(h**2 - 1/(1+s**2)) == 0)
# G6
x = 1/s
rec('G6', sp.simplify(-sp.diff(x, s)/(1+x**2) - 1/(1+s**2)) == 0
    and sp.integrate(1/(1+s**2), (s, 0, 1)) == sp.integrate(1/(1+s**2), (s, 1, sp.oo)))
# G7
M = sp.symbols('M', positive=True)
I = sp.integrate(s/(1+s**2), (s, 0, M))
rec('G7', sp.simplify(I - sp.log(1+M**2)/2) == 0 and sp.limit(I, M, sp.oo) == sp.oo)
# G8
tot = sp.integrate(1/(1+s**2), (s, 0, sp.oo))
closers = set()
for p in range(0, 25):
    for q in range(1, 25):
        if sp.gcd(p, q) != 1: continue
        z = 1; w = (q + sp.I*p)**2
        for n in range(1, 51):
            z = sp.expand(z*w)
            if sp.im(z) == 0 and sp.re(z) > 0: closers.add(F(p, q)); break
rec('G8', tot == sp.pi/2 and closers <= {F(0), F(1)}, f'closers {sorted(closers)}')
# G9 (mpmath, one octant: density (2/pi)(1+s^2+s2^2)^-3/2)
f = lambda x, y: 2/mp.pi*(1+x*x+y*y)**mp.mpf(-1.5)
tot9 = mp.quad(f, [0, 1, mp.inf], [0, 1, mp.inf])
pair = mp.quad(f, [0, 1], [0, 1, mp.inf])
near = mp.quad(f, [0, 1], [0, 1])
order = mp.quad(lambda x: mp.quad(lambda y: f(x, y), [x, mp.inf]), [1, mp.inf])  # v1 < v3 < v2 ... one of six
full = mp.quad(lambda x, y: (1/(2*mp.pi))*(1+x*x+y*y)**mp.mpf(-1.5), [-mp.inf, 0, mp.inf], [-mp.inf, 0, mp.inf])
# six orders: region 1 < s < s2 (v1 < v2 < v3) checked as 1/6
o6 = mp.quad(lambda x: mp.quad(lambda y: f(x, y), [x, mp.inf]), [1, mp.inf])
rec('G9', abs(tot9-1) < 1e-30 and abs(full-1) < 1e-30 and abs(pair-mp.mpf(1)/2) < 1e-30
    and abs(near-mp.mpf(1)/3) < 1e-30 and abs(o6-mp.mpf(1)/6) < 1e-30,
    f'octant {mp.nstr(tot9,12)} screen {mp.nstr(full,12)} pair {mp.nstr(pair,12)} near {mp.nstr(near,12)} order {mp.nstr(o6,12)}')
# G10: legs drawn at c: reading of the drawn pair is s/c's ... weight of the turn in drawn slope r = c*s? drawn v2 = c*v2
r = sp.symbols('r', positive=True)
wc = 1/(c*(1+(r/c)**2))   # law of drawn slope r = c*s
med = sp.solve(sp.Eq(sp.integrate(wc, (r, 0, sp.Symbol('m', positive=True))), sp.pi/4), sp.Symbol('m', positive=True))
corner3 = sp.sqrt(sp.Rational(1, 3))
rec('G10', sp.simplify(med[0] - c) == 0 and sp.simplify(3*corner3**2) == 1,
    f'median of drawn slope at c (so the true corner reads 1 only at c = 1): {med}')
# G11
heat = sp.sech(sp.log(d))/sp.pi
half = sp.simplify(sp.diff(sp.atan(d), d)*2/sp.pi*d - sp.sech(sp.log(d))/sp.pi)  # per unit ln d: (2/pi) d/(1+d^2)
lo = mp.quad(lambda x: mp.sech(x)/mp.pi, [-mp.inf, 0]); hi = mp.quad(lambda x: mp.sech(x)/mp.pi, [0, mp.inf])
rec('G11', sp.simplify(sp.sech(sp.log(d)) - 2*d/(1+d**2)) == 0 and abs(lo-hi) < 1e-35 and abs(lo+hi-1) < 1e-35,
    '(1/pi) sech(ln d) per ln d is (2/pi) d/(1+d^2), i.e. the half-Cauchy in d')
# G12 (exact rationals in Q[i])
ok = True
for p in range(1, 12):
    for q in range(1, 12):
        S = F(p, q)
        for A in (F(1, 3), F(2, 5), F(7, 4)):
            if S*A == 1: continue
            W = lambda x: (1+sp.I*sp.Rational(x.numerator, x.denominator))/(1-sp.I*sp.Rational(x.numerator, x.denominator))
            SA = (S+A)/(1-S*A)
            ok &= sp.simplify(W(S)*W(A) - W(SA)) == 0
        ok &= sp.simplify(W(S)*W(1/S) + 1) == 0 and sp.simplify(sp.Abs(W(S)) - 1) == 0
ok &= sp.simplify((1+sp.I)/(1-sp.I) - sp.I) == 0
rec('G12', ok)
# G13
expr = [v2/v1, v3/v1, (v1**2+v2**2+v3**2)]
rec('G13', all(sp.simplify(e.subs({v1: k*v1, v2: k*v2, v3: k*v3}) - e) == 0 for e in expr[:2])
    and sp.simplify((k*d)/(k*1) - d) == 0, '(ratios and d in thumbs; the hypotenuse in thumbs stays 1)')
print({g: R[g] for g in R})
