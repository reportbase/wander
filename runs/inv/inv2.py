# INV run 2: the share square (p, q) = (1/(1+s^2), 1/(1+x^2)), the SHV's pair read as shares.
import sympy as sp
from mpmath import mp, mpf, quad, sqrt as msqrt, pi as mpi, findroot
mp.dps = 50
s, x, a, k, p, q = sp.symbols('s x a k p q', positive=True)
P = lambda t: 1/(1+t**2)
def ok(name, expr):
    d = sp.simplify(expr); print(f"{name}: {'ok' if d == 0 else 'FAIL ' + str(d)}")

# Y1 exchanges are reflections; fixed point; both at once a half turn about (1/2,1/2)
ok("Y1 p(1/s) = 1 - p(s)", P(1/s) - (1 - P(s)))
ok("Y1 q(1/x) = 1 - q(x)", P(1/x) - (1 - P(x)))
print("Y1 fixed point of p->1-p:", sp.solve(sp.Eq(p, 1-p), p), " P(1) =", P(sp.Integer(1)))
R = lambda pt: (1-pt[0], 1-pt[1])
ok("Y1 both = half turn about (1/2,1/2)", (R((p,q))[0]-sp.Rational(1,2)) + (p-sp.Rational(1,2)))

# Y2 thumb change rational in q, Mobius, fixes 0 and 1, composes by multiplying
Mk = lambda qq, kk: qq/(qq + kk**2*(1-qq))
ok("Y2 q(kx) = Mk(q(x))", P(k*x) - Mk(P(x), k))
k2 = sp.symbols('k2', positive=True)
ok("Y2 composes: M_k2(M_k(q)) = M_(k k2)(q)", Mk(Mk(q,k),k2) - Mk(q,k*k2))
print("Y2 fixes 0 and 1:", Mk(sp.Integer(0),k), sp.simplify(Mk(sp.Integer(1),k)))

# Y3 turn: p -> (sqrt p - a sqrt(1-p))^2/(1+a^2); not rational in p
sa = (s+a)/(1-s*a)
ok("Y3 PYT identity", (1+sa**2) - (1+s**2)*(1+a**2)/(1-s*a)**2)
turn_p = (sp.sqrt(p) - a*sp.sqrt(1-p))**2/(1+a**2)
ok("Y3 p(s+a) = turn_p(p(s))", sp.simplify(P(sa) - turn_p.subs(p, P(s))))
ex = sp.expand(turn_p)
print("Y3 rational in p?", ex.is_rational_function(p), "| contains sqrt:", ex.has(sp.sqrt(p)*sp.sqrt(1-p)) or 'sqrt' in str(ex))
h, v = sp.symbols('h v', positive=True)
print("Y3 in (h, v):", sp.factor(turn_p.subs({sp.sqrt(p): h, sp.sqrt(1-p): v})), "(rational)")
# not a translation: p'-p depends on p
print("Y3 shift at p=1/4,1/2 (a=1/3):", [sp.nsimplify(sp.simplify(turn_p.subs({p:pp,a:sp.Rational(1,3)})-pp)) for pp in (sp.Rational(1,4), sp.Rational(1,2))])

# Y4 arcsine laws
t = sp.symbols('t', positive=True)
half_cauchy = 2/(sp.pi*(1+t**2))
# push to p = 1/(1+t^2): t = sqrt((1-p)/p), |dt/dp|
tp = sp.sqrt((1-p)/p)
dens_p = sp.simplify(half_cauchy.subs(t, tp) * sp.Abs(sp.diff(tp, p)))
ok("Y4 slope law in p = arcsine", dens_p - 1/(sp.pi*sp.sqrt(p*(1-p))))
# sech law of u=ln x is the half-Cauchy in x (run 1 X1), so q gets the same
u = sp.symbols('u', real=True)
sech_in_x = (sp.sech(sp.log(t))/sp.pi)/t
ok("Y4 sech law in x = half-Cauchy", sp.simplify((sech_in_x - half_cauchy).rewrite(sp.exp)))
mtot = quad(lambda z: 1/(mpi*msqrt(z*(1-z))), [0, 0.5, 1])
print("Y4 arcsine total:", mp.nstr(mtot, 40))

# Y5 median of q after x -> kx is 1/(1+k^2)
for kk in (mpf(2), mpf(7)/3, mpf(10)):
    # x ~ half-Cauchy; kx's median is k; q median = 1/(1+k^2) since q decreasing in x
    cdf = lambda m: quad(lambda z: 2/(mpi*(1+z**2)), [0, m/kk])   # P(kx <= m)
    med = findroot(lambda m: cdf(m) - mpf(1)/2, kk)
    print(f"Y5 k={mp.nstr(kk,6)}: median kx {mp.nstr(med,30)}, median q {mp.nstr(1/(1+med**2),30)} vs 1/(1+k^2) {mp.nstr(1/(1+kk**2),30)}")

# Y4, where sympy does not close (Abs of sqrt(1-p), p not declared below 1): 50 digits, as the plan's kill allows
from mpmath import mpf as F
f = sp.lambdify(p, dens_p - 1/(sp.pi*sp.sqrt(p*(1-p))), 'mpmath')
print("Y4 slope law in p = arcsine, 50 digits at p = 1/7, 1/2, 9/10:", [mp.nstr(f(F(n)/d), 5) for n, d in ((1,7),(1,2),(9,10))])
print("Y4 arcsine total, exact:", sp.integrate(1/(sp.pi*sp.sqrt(p*(1-p))), (p, 0, 1)))
