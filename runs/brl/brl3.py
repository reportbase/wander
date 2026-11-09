# BRL run 3: the unsteady breath, a turn and a stretch (B7-B12). See plans/brl-plan.md.
import random
from mpmath import mp, mpf, matrix, cos, sin, exp, sinh, acosh, log, pi, fabs, eye, svd_r
mp.dps = 60
rng = random.Random(20261110)
def r(a, b): return mpf(a) + (mpf(b)-mpf(a))*mpf(rng.random())
def R2(a): return matrix([[cos(a), -sin(a)], [sin(a), cos(a)]])
def S2(c): return matrix([[c, 0], [0, 1]])
def loop(A, B): return (B**-1)*(A**-1)*B*A          # A first, then B, then back, back
def mx(M): return max(fabs(M[i,j]) for i in range(M.rows) for j in range(M.cols))
def zeta_of(M): t = (M[0,0]+M[1,1])/2; return acosh(t) if t >= 1 else mpf(0)
out = []
def say(s): print(s); out.append(s)
I2 = eye(2)
draws = [(r(-pi, pi), r(-3, 3)) for _ in range(40)]
w7 = wd = w10 = 0; open8 = True
for a, lam in draws:
    M = loop(R2(a), S2(exp(lam)))
    tr = M[0,0]+M[1,1]; pred = 2 + 4*sin(a)**2*sinh(lam/2)**2
    w7 = max(w7, fabs(tr-pred)); wd = max(wd, fabs(mp.det(M)-1))
    if fabs(lam) > 0.05 and fabs(sin(a)) > 0.05 and mx(M-I2) < 1e-3: open8 = False
    z = zeta_of(M); psi = r(-pi, pi); k = exp(r(-2, 2))
    for S in (S2(exp(-lam)), R2(psi)*S2(exp(lam))*R2(-psi), k*S2(exp(lam))):
        w10 = max(w10, fabs(zeta_of(loop(R2(a), S)) - z))
say(f"B7 trace vs 2+4 sin^2a sinh^2(l/2): max diff {mp.nstr(w7,3)}; |det-1| {mp.nstr(wd,3)} -> {'held' if max(w7,wd) < 1e-50 else 'KILLED'}")
c1 = max(mx(loop(R2(r(-pi,pi)), S2(1))-I2) for _ in range(20))
cpi = max(mx(loop(R2(pi), S2(exp(r(-3,3))))-I2) for _ in range(20))
say(f"B8 closes at c=1: {mp.nstr(c1,3)}; at alpha=pi: {mp.nstr(cpi,3)}; open at every other draw: {open8} -> {'held' if max(c1,cpi) < 1e-50 and open8 else 'KILLED'}")
say(f"B10 zeta the same at 1/c, the stretch turned, a scaling put in: max diff {mp.nstr(w10,3)} -> {'held' if w10 < 1e-50 else 'KILLED'}")
say("B9 small loops, alpha = lambda = eps: zeta/(alpha*lambda)")
ok9 = True
for p in range(1, 7):
    e = mpf(10)**-p; q = zeta_of(loop(R2(e), S2(exp(e))))/(e*e)
    say(f"   eps=1e-{p}: {mp.nstr(q, 15)}")
    if p == 6 and fabs(q-1) > 1e-6: ok9 = False
say("   -> " + ("held" if ok9 else "KILLED"))
w11 = 0; n11 = 0
for a, lam in draws[:12]:
    M = loop(R2(a), S2(exp(lam))); z = zeta_of(M)
    if z < mpf('0.01'): continue
    smax = max(svd_r(M**400, compute_uv=False)); n11 += 1
    w11 = max(w11, fabs(log(smax)/400 - z))
say(f"B11 growth per loop ln sigma_max(M^400)/400 vs zeta, {n11} draws: max diff {mp.nstr(w11,3)} -> {'held' if w11 < 1e-2 else 'KILLED'}")
def R3z(a): return matrix([[cos(a),-sin(a),0],[sin(a),cos(a),0],[0,0,1]])
def S3(a,b,c): return matrix([[a,0,0],[0,b,0],[0,0,c]])
I3 = eye(3); bad = 0
for _ in range(20):
    a = r(0.1, pi-mpf('0.1')); c1, c3 = exp(r(-2,2)), exp(r(-2,2)); c2 = c1*exp(r(0.2, 2))
    if mx(loop(R3z(a), S3(c1, c2, c3)) - I3) < 1e-3: bad += 1
    if mx(loop(R3z(a), S3(c1, c1, c3)) - I3) > 1e-50: bad += 1
    if mx(loop(R3z(pi), S3(c1, c2, c3)) - I3) > 1e-50: bad += 1
say(f"B12 space: {bad} failures over 60 cases -> {'held' if bad == 0 else 'KILLED'}")
open('runs/brl/brl-run3.txt','w').write('\n'.join(out)+'\n')
