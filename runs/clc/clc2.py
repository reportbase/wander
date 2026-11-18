"""CLC run 2 (run 1's D1, D2, I2 killed by my code: nsimplify; improper fractions): calculus from one standpoint (plans/clc-plan.md). Exact arithmetic, seeded."""
import random
from fractions import Fraction as Q
import sympy as sp

random.seed(1099)
x = sp.symbols('x')


class D:
    """Dual number a + b·eps, eps² = 0, in exact fractions."""
    def __init__(s, a, b=Q(0)): s.a, s.b = Q(a), Q(b)
    def __add__(s, o): o = o if isinstance(o, D) else D(o); return D(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __sub__(s, o): o = o if isinstance(o, D) else D(o); return D(s.a - o.a, s.b - o.b)
    def __mul__(s, o): o = o if isinstance(o, D) else D(o); return D(s.a * o.a, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __truediv__(s, o):
        o = o if isinstance(o, D) else D(o)
        return D(s.a / o.a, (s.b * o.a - s.a * o.b) / (o.a * o.a))


def horner(c, t):
    r = D(0) if isinstance(t, D) else Q(0)
    for k in reversed(c): r = r * t + k
    return r


def rpoly(lo, hi):
    while True:
        d = random.randint(lo, hi)
        c = [random.randint(-9, 9) for _ in range(d + 1)]
        if c[-1] != 0: return c


def rpt():
    return Q(random.choice([-1, 1]) * random.randint(1, 20), random.randint(1, 20))


def sym(c): return sum(sp.Integer(k) * x**i for i, k in enumerate(c))


def rfun():
    while True:
        n, d = rpoly(0, 4), rpoly(1, 3)
        p = rpt()
        if horner(d, p) != 0: return n, d, p


def ev(n, d, t): return horner(n, t) / horner(d, t)


def tosym(v): return sp.Rational(v.numerator, v.denominator)


out = []
def say(*a):
    s = ' '.join(str(t) for t in a); print(s); out.append(s)

# D1
ok = 0
for _ in range(300):
    n, d, p = rfun()
    b = ev(n, d, D(p, 1)).b
    ref = sp.diff(sym(n) / sym(d), x).subs(x, tosym(p))
    ok += (tosym(b) == sp.Rational(ref))
say('D1 dual derivative = sympy, exact:', ok, '/ 300')

# D2
ok = ok2 = 0
for _ in range(200):
    while True:
        n1, d1, _p = rfun(); n2, d2, p = rfun()
        g = ev(n2, d2, p)
        if horner(d1, g) != 0: break
    comp = ev(n1, d1, ev(n2, d2, D(p, 1))).b
    gp = ev(n2, d2, D(p, 1)).b
    fp = ev(n1, d1, D(g, 1)).b
    F = (sym(n1) / sym(d1)).subs(x, sym(n2) / sym(d2))
    ref = sp.diff(F, x).subs(x, tosym(p))
    ok += (tosym(comp) == sp.Rational(ref)); ok2 += (comp == fp * gp)
say('D2 chain by duals = sympy:', ok, '/ 200; = product of links:', ok2, '/ 200')

# S1, S2
s1_first = s1_high = s1_high_n = 0; s2 = s2r = s2n = 0
for _ in range(100):
    n, d, p = rfun()
    f = sym(n) / sym(d)
    der = [sp.diff(f, x, m) for m in range(5)]
    for k in [sp.Integer(2), sp.Rational(7, 3), sp.Integer(10)]:
        g = k * f.subs(x, x / k)
        for m in range(1, 5):
            lhs = sp.simplify(sp.diff(g, x, m).subs(x, k * tosym(p)))
            fm = sp.simplify(der[m].subs(x, tosym(p)))
            if sp.simplify(lhs - k**(1 - m) * fm) != 0: raise SystemExit('S1 identity fails')
            if m == 1: s1_first += (lhs == fm)
            elif fm != 0: s1_high_n += 1; s1_high += (lhs != fm)
        n2, d2, _ = rfun()
        f2 = sym(n2) / sym(d2)
        if sym(d2).subs(x, tosym(p)) == 0: continue
        for m in range(1, 5):
            a1 = (k * der[m]).subs(x, tosym(p)); b1 = der[m].subs(x, tosym(p))
            a2 = (k * sp.diff(f2, x, m)).subs(x, tosym(p)); b2 = sp.diff(f2, x, m).subs(x, tosym(p))
            if b1 == 0 or b2 == 0: continue
            s2n += 1; s2 += (sp.simplify(a1 - k * b1) == 0) and (a1 != b1)
            s2r += (sp.simplify(a1 / a2 - b1 / b2) == 0)
say('S1 first derivative unmoved:', s1_first, '/ 300; higher moved:', s1_high, '/', s1_high_n)
say('S2 time-rates moved by k:', s2, '/', s2n, '; ratios of rates unmoved:', s2r, '/', s2n)

# I1
rat = 0; drat = 0; m = 0
while m < 200:
    n, d = rpoly(0, 4), rpoly(1, 3)
    D_ = sym(d)
    if sp.degree(sp.gcd(D_, sp.diff(D_, x)), x) > 0: continue
    if sp.rem(sym(n), sp.diff(D_, x), x) == 0 and sp.degree(sym(n), x) >= 0 and sp.diff(D_, x) != 0 \
       and sp.simplify(sym(n) / sp.diff(D_, x)).is_number: continue
    f = sym(n) / D_
    if sp.simplify(f).is_polynomial(x): continue
    m += 1
    I = sp.integrate(f, x)
    rat += not (I.has(sp.log) or I.has(sp.atan) or I.has(sp.RootSum))
    drat += sp.diff(f, x).is_rational_function(x)
say('I1 antiderivative rational:', rat, '/ 200; derivative rational:', drat, '/ 200')

# I2
from sympy.integrals.rationaltools import ratint_ratpart
back = logpart = 0
for _ in range(100):
    while True:
        a, b = rpoly(1, 2), rpoly(1, 2)
        D_ = sp.expand(sym(a)**2 * sym(b))
        n = rpoly(0, 4)
        if sp.gcd(sym(n), D_) == 1: break
    f = sym(n) / D_
    q, rr = sp.div(sym(n), D_, x)
    P, L = ratint_ratpart(sp.Poly(rr, x), sp.Poly(D_, x), x)
    P = P + sp.integrate(q, x)
    back += sp.cancel(sp.diff(P, x) + L - f) == 0
    logpart += sp.simplify(L) != 0
say('I2 rational part + log integrand back to f:', back, '/ 100; log part nonzero:', logpart, '/ 100')

# F1
tel = riem_inexact = riem_n = em = 0
for _ in range(100):
    n = rpoly(1, 4)
    r = random.randint(-5, 5); c = random.randint(1, 9)
    d = [r * r + c, -2 * r, 1]          # (x - r)^2 + c > 0, no real poles
    Fs = sym(n) / sym(d); fs = sp.cancel(sp.diff(Fs, x))
    fn, fd = sp.fraction(fs)
    fnc = [Q(int(t)) for t in reversed(sp.Poly(fn, x).all_coeffs())]
    fdc = [Q(int(t)) for t in reversed(sp.Poly(fd, x).all_coeffs())]
    a = Q(random.randint(-10, 0), random.randint(1, 5)); bb = a + Q(random.randint(1, 20), random.randint(1, 5))
    good = True
    for steps in range(1, 51):
        pts = sorted({a, bb} | {a + (bb - a) * Q(random.randint(1, 999), 1000) for _ in range(steps - 1)})
        good &= sum(ev(n, d, pts[i + 1]) - ev(n, d, pts[i]) for i in range(len(pts) - 1)) == ev(n, d, bb) - ev(n, d, a)
    tel += good
    exact = ev(n, d, bb) - ev(n, d, a)
    nonconst = sp.diff(fs, x) != 0
    if nonconst:
        riem_n += 1
        h = (bb - a) / 7
        riem_inexact += sum(h * ev(fnc, fdc, a + i * h) for i in range(7)) != exact
    N = 1000; h = (bb - a) / N
    err = sum(h * ev(fnc, fdc, a + i * h) for i in range(N)) - exact
    pred = -(bb - a) * (ev(fnc, fdc, bb) - ev(fnc, fdc, a)) / 2
    if pred != 0 and abs(float(err * N / pred) - 1) <= 0.05: em += 1
say('F1 telescoping exact at every partition:', tel, '/ 100; Riemann (n = 7) inexact:', riem_inexact, '/', riem_n,
    '; n·error within 5% of Euler–Maclaurin at n = 1000:', em, '/ 100')

open('runs/clc/clc-run2.txt', 'w').write('\n'.join(out) + '\n')
