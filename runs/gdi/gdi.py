# GDI run 1: what directions give, for a ball, a lens and a pair in orbit. Exact where it can be (sympy), mpmath at 50
# digits for numeric identities, a seeded least squares for D7. Usage: python3 -I runs/gdi/gdi.py
import sympy as sp, mpmath as mp, numpy as np
from scipy.optimize import least_squares
mp.mp.dps = 50
out = []
def say(s): print(s, flush=True); out.append(s)

# ---- D1, D2: the ball
x, y, z, R, G, M, k = sp.symbols('x y z R G M k', positive=True)
cx, cy, cz = sp.Rational(3, 7), sp.Rational(-2, 5), sp.Rational(1, 3)
def g_ball(p, inside):
    d = sp.Matrix(p) - sp.Matrix([cx, cy, cz]); r = sp.sqrt(d.dot(d))
    return (-G*M*d/r**3) if not inside else (-G*M*d/R**3)
def unit(v): return v/sp.sqrt(v.dot(v))
P1 = (sp.Integer(5), sp.Integer(1), sp.Integer(-2)); P2 = (sp.Integer(-4), sp.Integer(3), sp.Integer(2))
u1, u2 = unit(g_ball(P1, False)), unit(g_ball(P2, False))
# intersect the two lines p + t u: least squares closed form, exact
A = sp.Matrix.hstack(u1, -u2); bvec = sp.Matrix(P2) - sp.Matrix(P1)
t = (A.T*A).inv()*A.T*bvec
c1 = sp.simplify(sp.Matrix(P1) + t[0]*u1); miss = sp.simplify(c1 - sp.Matrix([cx, cy, cz]))
say('D1 outside: centre from two directions, error %s (exact zero: %s)' % (list(miss), all(sp.simplify(m) == 0 for m in miss)))
uo = unit(g_ball(P1, False)); ui = unit(g_ball(P1, True))
say('D1 the direction at one place is the same inside and outside: %s; R appears in neither direction: %s'
    % (sp.simplify(uo - ui) == sp.zeros(3, 1), not uo.has(R) and not ui.has(R)))
# D2: along a line through c, the strength times distance squared
s = sp.symbols('s', positive=True)
def gr(rr): return sp.Piecewise((G*M*rr/R**3, rr < R), (G*M/rr**2, True))
q = lambda rr: gr(rr)*rr**2
Rv = sp.Rational(7, 3)
vals = [sp.simplify((q(sp.Rational(n, 2))/q(sp.Integer(10))).subs(R, Rv)) for n in range(1, 12)]
ok_out = all(vals[n-1] == 1 for n in range(1, 12) if sp.Rational(n, 2) >= Rv)
ok_in = all(sp.simplify(vals[n-1] - (sp.Rational(n, 2)/Rv)**3) == 0 for n in range(1, 12) if sp.Rational(n, 2) < Rv)
# R from two inside ratios: (r/R)^3 = ratio -> R = r / ratio^(1/3)
Rrec = sp.Rational(3, 2)/sp.cbrt(vals[2])
scaled = [sp.simplify((q(k*sp.Rational(n, 2))/q(k*10)).subs(R, k*Rv)) for n in (1, 3, 7, 11)]
say('D2 ratios 1 outside: %s; (r/R)^3 inside: %s; R recovered from one inside ratio %s (true %s); scaled by k: %s'
    % (ok_out, ok_in, sp.nsimplify(Rrec), Rv, [sp.simplify(sv) for sv in scaled] == [vals[0], vals[2], vals[6], vals[10]]))

# ---- D3, D4: point lens
b, tE = sp.symbols('beta theta_E', positive=True)
tp = (b + sp.sqrt(b**2 + 4*tE**2))/2; tm = (b - sp.sqrt(b**2 + 4*tE**2))/2
mu = lambda th: 1/(1 - (tE/th)**4)
say('D3 sqrt(th+ |th-|) - thE = %s; th+ + th- - beta = %s' % (sp.simplify(sp.sqrt(tp*(-tm)) - tE), sp.simplify(tp + tm - b)))
qr = tp/(-tm); ratio = sp.simplify(sp.Abs(mu(tp)/mu(tm)))
say('D3 |mu+/mu-| against q^2: %s; against q^4: %s'
    % (sp.simplify(ratio - qr**2) == 0, sp.simplify(ratio - qr**4) == 0))
for bv, tv in ((sp.Rational(1, 3), 1), (2, sp.Rational(3, 2)), (sp.Rational(1, 100), 5)):
    r_n = mp.mpf(sp.N(ratio.subs({b: bv, tE: tv}), 60)); q_n = mp.mpf(sp.N(qr.subs({b: bv, tE: tv}), 60))
    say('   beta %s thE %s: |mu+/mu-| %s, q^2 %s, diff %.1e' % (bv, tv, mp.nstr(r_n, 20), mp.nstr(q_n**2, 20), float(abs(r_n - q_n**2))))
# D4: images at two sky points; lens unseen. Given the separation S = th+ + |th-| and the ratio r, th+ = S*sqrt(r)/(1+sqrt(r))
Ssym, rsym = sp.symbols('S r', positive=True)
thp_rec = Ssym*sp.sqrt(rsym)/(1 + sp.sqrt(rsym))
errs4 = []
for bv, tv in ((sp.Rational(1, 3), 1), (2, sp.Rational(3, 2)), (sp.Rational(1, 100), 5)):
    sub = {b: bv, tE: tv}
    errs4.append(abs(mp.mpf(sp.N((thp_rec.subs({Ssym: tp - tm, rsym: ratio}) - tp).subs(sub), 60))))
say('D4 lens placed from separation and magnification ratio: errors %s' % ['%.1e' % float(e) for e in errs4])
say('D4 without the ratio: any lens place on the segment gives th+ |th-| = some thE^2 and beta = th+ + th-: a one-parameter family (by construction)')
# ---- D5: SIS
tpS, tmS = b + tE, b - tE
say('D5 SIS: (th+ + |th-|)/2 - thE = %s; sqrt(th+|th-|) - thE = %s; equal at beta = 0: %s'
    % (sp.simplify((tpS + sp.Abs(tmS))/2 - tE).subs(b, sp.Rational(1, 10)*tE), sp.simplify(sp.sqrt(tpS*(tE - b)) - tE),
       sp.simplify(sp.sqrt(tpS*(tE - b)).subs(b, 0) - tE) == 0))

# ---- D6, D7: the pair in orbit, the turning frame, the plane
def geff(p, mu_, x1, x2, D, Om2, GM=1.0):
    # masses m1 = mu/(1+mu), m2 = 1/(1+mu) (total GM), at (x1,0) and (x2,0); centre of mass at origin assumed by x1, x2
    m1, m2 = GM*mu_/(1 + mu_), GM/(1 + mu_)
    gx = gy = 0.0
    for m, xm in ((m1, x1), (m2, x2)):
        dx, dy = p[0] - xm, p[1]; r3 = (dx*dx + dy*dy)**1.5
        gx -= m*dx/r3; gy -= m*dy/r3
    return np.array([gx + Om2*p[0], gy + Om2*p[1]])
def pair(mu_, D, cxm=0.0, cym=0.0, ang=0.0):
    x1 = -D/(1 + mu_); x2 = D*mu_/(1 + mu_)    # m1 at x1 heavier when mu>1; centre of mass at 0
    return x1, x2
rng = np.random.default_rng(1219)
def dirs(places, mu_, D, off, ang, GM=1.0):
    x1, x2 = pair(mu_, D); Om2 = GM/D**3
    c, s_ = np.cos(ang), np.sin(ang); res = []
    for p in places:
        q_ = np.array([c*(p[0]-off[0]) + s_*(p[1]-off[1]), -s_*(p[0]-off[0]) + c*(p[1]-off[1])])
        g = geff(q_, mu_, x1, x2, D, Om2, GM); g = np.array([c*g[0] - s_*g[1], s_*g[0] + c*g[1]])
        res.append(np.arctan2(g[1], g[0]))
    return np.array(res)
places = rng.uniform(-3, 3, (6, 2))
base = dirs(places, 0.3, 2.0, (0.4, -0.2), 0.5)
sc = [dirs(places*kk, 0.3, 2.0*kk, (0.4*kk, -0.2*kk), 0.5, GM=1.0) for kk in (0.1, 7.0)]
say('D6 directions unmoved by scaling lengths with the Kepler rate: max change %.2e' % max(np.max(np.abs(np.angle(np.exp(1j*(s2 - base))))) for s2 in sc))
for mu_t in (1.0, 0.3, 0.01):
    truth = np.array([np.log(mu_t), np.log(2.0), 0.4, -0.2, 0.5])
    obs = dirs(places, mu_t, 2.0, (0.4, -0.2), 0.5)
    def res(pv): return np.nan_to_num(np.angle(np.exp(1j*(dirs(places, np.exp(pv[0]), np.exp(pv[1]), (pv[2], pv[3]), pv[4]) - obs))), nan=10.0)
    sols = []
    for _ in range(300):
        st = np.array([rng.uniform(-5, 2), rng.uniform(-1, 2), rng.uniform(-2, 2), rng.uniform(-2, 2), rng.uniform(-np.pi, np.pi)])
        r_ = least_squares(res, st, bounds=([-7, -2, -4, -4, -4], [3, 3, 4, 4, 4]), xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
        if r_.cost < 1e-24: sols.append(r_.x)
    sols = np.array(sols)
    if len(sols) == 0: say('D7 mu %g: no exact solution found' % mu_t); continue
    # fold the angle; distinct solutions
    sols[:, 4] = np.angle(np.exp(1j*sols[:, 4]))
    uniq = []
    for sv in sols:
        if not any(np.max(np.abs(sv - u)) < 1e-6 for u in uniq): uniq.append(sv)
    errs = [np.max(np.abs(np.r_[np.exp(u[0]) - mu_t, u[1:] - truth[1:]])) for u in uniq]
    say('D7 mu %g: %d exact fits of 300 starts, %d distinct; errors %s' % (mu_t, len(sols), len(uniq), ['%.1e' % e for e in errs]))
    for u in uniq: say('    mu %.10g D %.10g centre (%.8g, %.8g) turn %.8g' % (np.exp(u[0]), np.exp(u[1]), u[2], u[3], u[4]))
open('runs/gdi/gdi-run1.txt', 'w').write('\n'.join(out) + '\n')
