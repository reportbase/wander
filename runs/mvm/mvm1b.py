# MVM run 1, post hoc (after M1 was killed): the triangle's own relation, sin(delta) = beta*R_r*sin(theta_r)/R_present,
# and where the boosted pull's radial part changes sign. Usage: python3 -I runs/mvm/mvm1b.py
import sympy as sp
out = []
def say(s): print(s, flush=True); out.append(s)
def ang(u, v): return sp.atan2(u[0]*v[1] - u[1]*v[0], u[0]*v[0] + u[1]*v[1])
for b, X, Y in [(sp.Rational(1, 10), 3, 4), (sp.Rational(1, 2), -2, 5), (sp.Rational(9, 10), 7, 1), (sp.Rational(3, 5), 0, 2)]:
    tr = sp.symbols('tr'); tr = [s_ for s_ in sp.solve(sp.Eq((X - b*tr)**2 + Y**2, tr**2), tr) if s_.is_real and s_ < 0][0]
    rr = sp.Matrix([b*tr, 0]); x0 = sp.Matrix([X, Y])
    look = x0 - rr; Rr = sp.sqrt(look.dot(look)); Rp = sp.sqrt(x0.dot(x0))
    d = ang(-x0, rr - x0); th = ang(sp.Matrix([1, 0]), look)
    say('beta %s at (%s, %s): sin(delta) - beta*R_r*sin(theta_r)/R_p = %.1e' % (b, X, Y, float(sp.N(sp.sin(sp.Abs(d)) - b*Rr*sp.sin(sp.Abs(th))/Rp, 60))))
b, x, y = sp.symbols('b x y', positive=True)
# radial factor from run 1: b^4 y^2 + 3 b^2 x^2 - x^2 - y^2; on the line of motion (y = 0) it changes sign at b^2 = 1/3
say('on the line of motion the pull reverses at beta^2 = %s; square to it (x = 0) at beta = %s'
    % (sp.solve(sp.Eq(3*b**2 - 1, 0), b), sp.solve(sp.Eq(b**4 - 1, 0), b)))
open('runs/mvm/mvm-run1b.txt', 'w').write('\n'.join(out) + '\n')
