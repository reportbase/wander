# LDL run 1: light's delay past a lens, exact (sympy). Usage: python3 -I runs/ldl/ldl.py
import sympy as sp, mpmath as mp
mp.mp.dps = 50
out = []
def say(s): print(s, flush=True); out.append(s)
th, b = sp.symbols('theta beta', real=True)
q = sp.symbols('q', positive=True)
# point mass
tp = (b + sp.sqrt(b**2 + 4))/2; tm = (b - sp.sqrt(b**2 + 4))/2
geo = lambda t_: sp.Rational(1, 2)*(t_ - b)**2
t_pm = lambda t_: geo(t_) - sp.log(sp.Abs(t_))
# images are stationary points
say('T1 stationary: %s %s' % (sp.simplify(sp.diff(geo(th) - sp.log(th), th).subs(th, tp)), sp.simplify(sp.diff(geo(th) - sp.log(-th), th).subs(th, tm))))
qq = tp/(-tm)
dgeo = geo(tm) - geo(tp); dsha = -(sp.log(-tm) - sp.log(tp))    # image minus arrives later: t(minus) - t(plus)
for bv in (sp.Rational(1, 7), sp.Rational(1, 2), sp.Integer(1), sp.Integer(3), sp.Rational(25, 2)):
    qv = qq.subs(b, bv)
    e_g = sp.N((dgeo - (qq - 1/qq)/2).subs(b, bv), 60); e_s = sp.N((dsha - sp.log(qq)).subs(b, bv), 60)
    ratio = sp.N(((qq - 1/qq)/(2*sp.log(qq))).subs(b, bv), 20)
    say('T1 beta %s (q %s): geometric - (q - 1/q)/2 = %.1e; Shapiro - ln q = %.1e; T2 ratio geo/Shapiro %s'
        % (bv, sp.N(qv, 12), float(e_g), float(e_s), ratio))
f = (q - 1/q)/2 + sp.log(q)
say('T1 odd under q -> 1/q: %s; zero at q = 1: %s' % (sp.simplify(f.subs(q, 1/q) + f) == 0, f.subs(q, 1) == 0))
g = (q - 1/q) - 2*sp.log(q)                       # T2: geometric minus Shapiro, times 2
say('T2 g(1) = %s, g\'(q) = %s (>= 0 for q > 0), limit of ratio at q -> 1: %s, at q -> oo: %s'
    % (g.subs(q, 1), sp.factor(sp.diff(g, q)), sp.limit((q - 1/q)/(2*sp.log(q)), q, 1), sp.limit((q - 1/q)/(2*sp.log(q)), q, sp.oo)))
# SIS
tpS, tmS = b + 1, b - 1
say('T3 SIS stationary: %s %s' % (sp.diff(geo(th) - th, th).subs(th, tpS), sp.diff(geo(th) + th, th).subs(th, tmS)))
say('T3 SIS geometric difference %s; potential difference %s; total %s'
    % (sp.simplify(geo(tmS) - geo(tpS)), sp.simplify(-(sp.Abs(tmS) - tpS).subs(b, sp.Rational(1, 3))), sp.simplify((geo(tmS) + tmS) - (geo(tpS) - tpS))))
# T4 scale: in physical units t = (D_dt/c)[ (theta-beta)^2/2 - psi ], angles fixed; for the point mass T = 4GM(1+z)/c^3
k, G, M, c, z = sp.symbols('k G M c z', positive=True)
T = 4*G*M*(1 + z)/c**3
say('T4 point mass: T under lengths and times scaled by k (GM -> k GM, c fixed): %s; q depends only on beta/theta_E: angles unchanged'
    % sp.simplify(T.subs(M, k*M)/T))
dt = sp.symbols('Delta_t', positive=True)
Mrec = c**3*dt/(4*G*(1 + z)*f)
say('T4 M from a counted delay and q: M = %s (no distance)' % Mrec)
# T5
r = sp.symbols('r', positive=True)
say('T5 f(sqrt r) - [ (sqrt r - 1/sqrt r)/2 + ln r / 2 ] = %s' % sp.simplify(f.subs(q, sp.sqrt(r)) - ((sp.sqrt(r) - 1/sp.sqrt(r))/2 + sp.log(r)/2)))
# brute check: the delay from the Fermat time at numeric images, 50 digits
for bv in (mp.mpf(1)/3, mp.mpf(2)):
    tpn = (bv + mp.sqrt(bv**2 + 4))/2; tmn = (bv - mp.sqrt(bv**2 + 4))/2
    T_ = lambda t_: (t_ - bv)**2/2 - mp.log(abs(t_))
    qn = tpn/(-tmn)
    say('   beta %s: t(-) - t(+) = %s; f(q) = %s' % (mp.nstr(bv, 6), mp.nstr(T_(tmn) - T_(tpn), 30), mp.nstr((qn - 1/qn)/2 + mp.log(qn), 30)))
open('runs/ldl/ldl-run1.txt', 'w').write('\n'.join(out) + '\n')
