# INV run 3: Omega and 1/Omega, the pair with no fixed point.
import sympy as sp
from mpmath import mp, mpf, atan, sqrt, pi, findroot
mp.dps = 50
s = sp.symbols('s', positive=True)
Om = sp.pi/2
w = sp.atan(s)                      # weight chart: integral of dt/(1+t^2) from 0 to s
def ok(n, e):
    d = sp.simplify(e); print(f"{n}: {'ok' if d == 0 else 'FAIL '+str(d)}")
# Z1
ok("Z1 w(1/s) = Omega - w(s)", w.subs(s, 1/s) - (Om - w))
print("Z1 fixed point of w -> Omega - w:", sp.solve(sp.Eq(sp.Symbol('W'), Om - sp.Symbol('W')), sp.Symbol('W')), " w(1) =", w.subs(s, 1))
# Z2
g = w/Om
ok("Z2 g(1/s) = 1 - g(s)", g.subs(s, 1/s) - (1 - g))
print("Z2 total of g:", sp.limit(g, s, sp.oo), "| (Omega, 1/Omega) in the g chart: (", sp.limit(g, s, sp.oo), ",", 1/sp.limit(g, s, sp.oo), ")")
# Z3 family r(s) = w(s)*sqrt(1+s^2)/s (walk over chord), and 1/r
r = lambda x: atan(x)*sqrt(1+x*x)/x
print("Z3 product r*(1/r) = 1 identically (trivial)")
print("Z3 r at s->0:", mp.nstr(r(mpf('1e-30')), 20), " at corner s=1:", mp.nstr(r(mpf(1)), 20), " = Omega/sqrt2*sqrt2? pi/(2*sqrt2)*... check pi*sqrt2/4 =", mp.nstr(pi*sqrt(2)/4, 20))
print("Z3 r at s=1e30:", mp.nstr(r(mpf('1e30')), 20), " Omega =", mp.nstr(pi/2, 20))
# r is increasing, so r = 1 only as s -> 0
xs = [mpf(10)**k for k in range(-20, 21)]
vals = [r(x) for x in xs]
print("Z3 r increasing on 1e-20..1e20:", all(a < b for a, b in zip(vals, vals[1:])), "| min r - 1 over grid:", mp.nstr(min(vals) - 1, 5))
# Z4
for x in (mpf(1)/2, mpf(3), mpf('1e6'), mpf('1e30')):
    print(f"Z4 s={mp.nstr(x,6)}: r(1/s) = {mp.nstr(r(1/x),15)}, 1/r(s) = {mp.nstr(1/r(x),15)}, equal: {abs(r(1/x)-1/r(x)) < mpf(10)**-45}")
# Z5
print("Z5 Omega/2 =", mp.nstr(pi/4, 20), " 1/Omega =", mp.nstr(2/pi, 20), " equal:", abs(pi/4 - 2/pi) < mpf(10)**-45)
k = sp.symbols('k', positive=True)
ok("Z5 thumb change x -> kx leaves total of ds/(1+s^2) (a slope law is unmoved; Omega has no unit)", sp.integrate(1/(1+s**2), (s, 0, sp.oo)) - Om)

# Z1, Z2 where sympy does not close atan(1/s) + atan(s) = pi/2 for s > 0: 50 digits, and the derivative
for x in (mpf(1)/7, mpf(1), mpf(13)/5, mpf('1e12')):
    print(f"Z1/Z2 50 digits at s={mp.nstr(x,6)}: atan(1/s)+atan(s)-Omega = {mp.nstr(atan(1/x)+atan(x)-pi/2, 5)}")
ok("Z1 derivative of atan(1/s)+atan(s) is 0 (so the sum is constant, its value at s=1 Omega)", sp.diff(sp.atan(1/s)+sp.atan(s), s))
