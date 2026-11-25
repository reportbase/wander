# MVM run 1: a moving mass, a look and a pull. Exact (sympy); c = 1. Usage: python3 -I runs/mvm/mvm.py
import sympy as sp
out = []
def say(s): print(s, flush=True); out.append(s)
t, x, y, z = sp.symbols('t x y z', real=True)
G, M = sp.symbols('G M', positive=True)
cases = [(sp.Rational(1, 10), sp.Integer(3), sp.Integer(4)), (sp.Rational(1, 2), sp.Integer(-2), sp.Integer(5)),
         (sp.Rational(9, 10), sp.Integer(7), sp.Integer(1)), (sp.Rational(3, 5), sp.Integer(0), sp.Integer(2))]
def retarded(b, X, Y):
    tr = sp.symbols('tr')
    sols = [s_ for s_ in sp.solve(sp.Eq((X - b*tr)**2 + Y**2, tr**2), tr) if s_.is_real and s_ < 0]
    return sols[0]
def ang(u, v): return sp.atan2(u[0]*v[1] - u[1]*v[0], u[0]*v[0] + u[1]*v[1])
# M1, M2
for b, X, Y in cases:
    tr = retarded(b, X, Y); rr = sp.Matrix([b*tr, 0]); x0 = sp.Matrix([X, Y]); pres = sp.Matrix([0, 0])
    look = x0 - rr                                        # from the retarded place toward the place (light travel)
    nvec = look/sp.sqrt(look.dot(look))
    # M1: delta between the line to the retarded place and the line to the present place
    to_ret, to_pres = rr - x0, pres - x0
    delta = ang(to_pres, to_ret)
    thr = ang(sp.Matrix([1, 0]), look)                    # angle at the retarded place between v and the line to x0
    m1 = sp.N(sp.sin(sp.Abs(delta)) - b*sp.sin(sp.Abs(thr)), 60)
    # M2: Lienard-Wiechert velocity field E ∝ (n - beta)(1 - b^2)/(kappa^3 R^2)
    beta = sp.Matrix([b, 0]); kap = 1 - nvec.dot(beta); Rr = sp.sqrt(look.dot(look))
    E = (nvec - beta)*(1 - b**2)/(kap**3*Rr**2)
    cross = sp.N(E[0]*(x0 - pres)[1] - E[1]*(x0 - pres)[0], 60)
    say('beta %s at (%s, %s): M1 sin(delta) - beta sin(theta_r) = %.1e (delta %.6f rad); M2 E x (x0 - present) = %.1e'
        % (b, X, Y, float(m1), float(sp.N(delta)), float(cross)))
# M3: linearized gravity, boosted
b = sp.symbols('b', positive=True)
gam = 1/sp.sqrt(1 - b**2)
xp = gam*(x - b*t); Rp = sp.sqrt(xp**2 + y**2 + z**2); Phi = -G*M/Rp
h00 = -2*Phi*gam**2*(1 + b**2)
h0x = 4*Phi*gam**2*b
# h_0y = h_0z = 0
ax = sp.diff(h0x, t)*(-1) + sp.Rational(1, 2)*sp.diff(h00, x)
ay = sp.Rational(1, 2)*sp.diff(h00, y)
# the sign: d2x/dt2 = -Gamma^i_00 = -(d0 h_i0 - 1/2 d_i h00)
ax, ay = sp.simplify(ax.subs({t: 0, z: 0})), sp.simplify(ay.subs({t: 0, z: 0}))
# direction against the present place (origin): cross product with x0 - 0 = (x, y)
crossg = sp.simplify(ax*y - ay*x)
say('M3 pull x (x0 - present) at t = 0, as a function of beta: %s' % sp.factor(crossg))
ser = sp.series(crossg, b, 0, 4).removeO()
say('M3 series in beta: %s' % sp.simplify(ser))
radial = sp.simplify(ax*x + ay*y)
say('M3 the pull points at the present place (inward) : radial component %s' % sp.factor(radial))
for bv, X, Y in cases:
    th = sp.atan2(ay, ax).subs({b: bv, x: X, y: Y, G: 1, M: 1}); tp_ = sp.atan2(-Y, -X)
    say('   beta %s at (%s, %s): pull direction - present direction = %.3e rad' % (bv, X, Y, float(sp.N(th - tp_, 40))))
# M4: scaling lengths and times by k
k = sp.symbols('k', positive=True)
axk = (sp.diff(h0x, t)*(-1) + sp.Rational(1, 2)*sp.diff(h00, x))
ayk = sp.Rational(1, 2)*sp.diff(h00, y)
sub0 = {t: 0, z: 0}
r1 = sp.simplify((axk/ayk).subs(sub0)); r2 = sp.simplify((axk/ayk).subs(sub0).subs({x: k*x, y: k*y}))
say('M4 pull direction under scaling (ratio of components): unchanged %s; strength ratio %s'
    % (sp.simplify(r1 - r2) == 0, sp.simplify((ax.subs({x: k*x, y: k*y}))/ax)))
for bv, X, Y in cases[:2]:
    tr1 = retarded(bv, X, Y); tr2 = retarded(bv, 5*X, 5*Y)
    d1 = ang(sp.Matrix([0, 0]) - sp.Matrix([X, Y]), sp.Matrix([bv*tr1, 0]) - sp.Matrix([X, Y]))
    d2 = ang(sp.Matrix([0, 0]) - sp.Matrix([5*X, 5*Y]), sp.Matrix([bv*tr2, 0]) - sp.Matrix([5*X, 5*Y]))
    say('   look: delta at k = 1 and 5: %.12f, %.12f' % (float(sp.N(d1)), float(sp.N(d2))))
open('runs/mvm/mvm-run1.txt', 'w').write('\n'.join(out) + '\n')
