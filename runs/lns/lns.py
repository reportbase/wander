"""LNS run 1: a lens sees columns (plans/lns-plan.md). Exact (sympy) and mpmath quadrature."""
import sympy as sp
import mpmath as mp
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
G, M, c, b, z, k = sp.symbols('G M c b z k', positive=True)

def alpha_point(z0, m=M, bb=b):
    # Born deflection along x for a ray at impact bb along z, from a point mass m at (0, 0, z0)
    phi_x = G*m*bb/(bb**2 + (z - z0)**2)**sp.Rational(3, 2)   # d Phi / d x at the ray (Phi = -G m / r)
    return sp.simplify(2/c**2*sp.integrate(phi_x, (z, -sp.oo, sp.oo)))
vals = [alpha_point(z0*b) for z0 in (-5, 0, 7)]
split = sp.simplify(alpha_point(-3*b, M/3) + alpha_point(4*b, 2*M/3))
N1 = all(sp.simplify(v - vals[0]) == 0 for v in vals) and sp.simplify(split - vals[0]) == 0
say("N1: alpha at z0 = -5b, 0, 7b:", vals, "; split 1/3 at -3b and 2/3 at 4b:", split)
say("N1", "not killed" if N1 else "KILLED")
N2 = sp.simplify(vals[0] - 4*G*M/(c**2*b)) == 0
say("N2: alpha =", vals[0], "= 4GM/(c^2 b):", N2)
say("N2", "not killed" if N2 else "KILLED")

# N3: a ring of column, radius a, line density lam, on the sky; deflection at xi along x
mp.mp.dps = 40
def ring(xi, a=mp.mpf(1)):
    f = lambda ph: (xi - a*mp.cos(ph))/(xi**2 + a**2 - 2*a*xi*mp.cos(ph))*a
    return mp.quad(f, [0, mp.pi, 2*mp.pi])
ro, ri = ring(mp.mpf(2)), ring(mp.mpf('0.5'))
say(f"N3: ring (4G lam/c^2 units): outside at 2a {mp.nstr(ro, 30)} against 2 pi a/2 = {mp.nstr(mp.pi, 30)}; inside {mp.nstr(ri, 3)}")
N3 = abs(ro - mp.pi) < mp.mpf('1e-25') and abs(ri) < mp.mpf('1e-25')
say("  the kernel (xi - xi')/|xi - xi'|^2 is 1/r^(D-1) at D = 2: CLM's column premise on the sky's plane")
say("N3", "not killed" if N3 else "KILLED")

# N4: circularly symmetric columns; by rings (sympy for the ring law, then superposition)
a_, xi, ph, s_ = sp.symbols('a xi phi s', positive=True)
ring_out = sp.integrate(sp.Rational(1, 1), (ph, 0, 2*sp.pi))/xi   # the ring law shown in N3: 2 pi / xi outside, 0 inside
def alpha_sym(Sigma):
    inner = sp.integrate(Sigma.subs(s_, a_)*a_*2*sp.pi/xi, (a_, 0, xi))
    return sp.simplify(4*G/c**2*inner)
def Menc(Sigma):
    return sp.integrate(Sigma.subs(s_, a_)*2*sp.pi*a_, (a_, 0, xi))
N4 = True
for name, Sig in (("uniform disc of column 1 (inside its edge)", sp.Integer(1)), ("1/(1 + s^2)", 1/(1 + s_**2))):
    al, me = alpha_sym(Sig), Menc(Sig)
    ok = sp.simplify(al - 4*G*me/(c**2*xi)) == 0
    say(f"N4: {name}: alpha = {al}; 4 G M(<xi)/(c^2 xi) equal: {ok}")
    N4 = N4 and ok
say("N4", "not killed" if N4 else "KILLED")

# N5: scale
a0 = 4*G*M/(c**2*b)
N5 = sp.simplify(a0.subs({M: k*M, b: k*b}) - a0) == 0 and sp.simplify(a0.subs(M, k*M) - k*a0) == 0
say("N5: lengths and masses x k: alpha unmoved; masses x k alone: alpha x k:", N5)
say("N5", "not killed" if N5 else "KILLED")
open('runs/lns/lns-run1.txt', 'w').write("\n".join(out) + "\n")
