# CNB run 1: a cannonball under quadratic drag; predictions in plans/cnb-plan.md
from fractions import Fraction as F
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar

def fly(s, v0=1.0, g=1.0, L=np.inf):
    c = 1/np.sqrt(1+s*s)
    def f(t, y):
        x, z, vx, vz = y; sp = np.hypot(vx, vz); k = 0 if np.isinf(L) else sp/L
        return [vx, vz, -k*vx, -g - k*vz]
    def hit(t, y): return y[1]
    hit.terminal = True; hit.direction = -1
    def top(t, y): return y[3]
    top.direction = -1
    T = 10*v0/g*s*c+10
    r = solve_ivp(f, [0, T], [0, 0, v0*c, v0*s*c], events=[hit, top], rtol=1e-12, atol=1e-14,
                  method='DOP853', dense_output=True)
    y_end = r.y_events[0][0]; y_top = r.y_events[1][0]
    R = y_end[0]; scale = v0*v0/g
    return dict(R=R/scale, land=y_end[3]/y_end[2], apex_share=y_top[0]/R,
                apex_h=y_top[1]/R, apex_seen=y_top[1]/y_top[0])

def best(beta):
    o = minimize_scalar(lambda u: -fly(np.exp(u), L=1/beta if beta else np.inf)['R'],
                        bracket=(-1, 0), tol=1e-12)
    return np.exp(o.x)

out = []
p = lambda *a: (print(*a), out.append(' '.join(map(str, a))))
# C1 exact
ok = True
for s in [F(1,4), F(1,2), F(2,3), F(1), F(3,2), F(4)]:
    Rx = 2*s/(1+s*s); Rinv = 2*(1/s)/(1+1/(s*s))
    tmax = s  # vz0/g with c factored: x(t)=c t, z=s c t - t^2/2 ; apex t=s c, x=s c^2 ; R=2 s c^2
    c2 = 1/(1+s*s); xa = s*c2; za = s*s*c2/2; R = 2*s*c2
    ok &= (R == Rx == Rinv) and xa/R == F(1,2) and za/R == s/4 and za/xa == s/2
    d = fly(float(s))
    ok &= abs(d['R']-float(Rx)) < 1e-10 and abs(d['land']+float(s)) < 1e-10 and abs(d['apex_share']-.5) < 1e-10 \
        and abs(d['apex_h']-float(s)/4) < 1e-10
p('C1 exact and integrated:', 'ok' if ok else 'FAIL', '; best s at beta 0:', round(best(0), 10))
# C2
worst = 0
for beta in [0.1, 1, 10]:
    ref = None
    for v0, g in [(1, 1), (7.3, 9.81), (300, 1.62), (0.02, 274)]:
        L = v0*v0/(g*beta)
        ds = [fly(s, v0, g, L) for s in (0.5, 1.0, 2.0)]
        vec = np.array([[d[k] for k in ('R', 'land', 'apex_share', 'apex_seen')] for d in ds]).ravel()
        if ref is None: ref = vec
        worst = max(worst, np.max(np.abs(vec-ref)))
p('C2 worst spread over four (v0, g, L) per beta:', f'{worst:.2e}', 'not killed' if worst < 1e-8 else 'KILLED')
# C3
betas = np.exp(np.linspace(np.log(0.01), np.log(100), 20))
ss = [best(b) for b in betas]
p('C3 s* over beta:', ' '.join(f'{b:.3g}:{s:.5f}' for b, s in zip(betas, ss)))
p('C3', 'not killed' if all(s < 1 for s in ss) and all(np.diff(ss) < 0) else 'KILLED')
# C4, C5
k4 = k5 = True; rows = []
for b in betas:
    L = 1/b
    for s in (0.25, 0.5, 0.75):
        a, c = fly(s, L=L)['R'], fly(1/s, L=L)['R']; k4 &= a > c
    for s in (0.25, 0.5, 1, 2):
        d = fly(s, L=L); k5 &= -d['land'] > s and d['apex_share'] > 0.5
d = fly(1, L=1.0); rows.append(f"beta 1, s 1: R {d['R']:.6f} land {d['land']:.6f} apex share {d['apex_share']:.6f} apex seen {d['apex_seen']:.6f}")
p('C4', 'not killed' if k4 else 'KILLED', '; C5', 'not killed' if k5 else 'KILLED'); [p(r) for r in rows]
for s in (0.5, 1):
    for b in (0.1, 1, 10):
        a, c = fly(s, L=1/b)['R'], fly(1/s, L=1/b)['R']
        p(f'  R({s})/R({1/s}) at beta {b}: {a/c:.6f}')
# C6
s6 = [best(b) for b in (4, 2, 1)]; a6 = [fly(1, L=1/b)['apex_share'] for b in (4, 2, 1)]
p('C6 s* at beta 4,2,1:', [round(x, 6) for x in s6], 'apex share at s=1:', [round(x, 6) for x in a6],
  'not killed' if s6[0] < s6[1] < s6[2] and a6[0] > a6[1] > a6[2] else 'KILLED')
# C7
for b in (1e-4, 3e-4, 1e-3, 3e-3, 1e-2):
    p(f'C7 beta {b:g}: (1 - s*)/beta = {(1-best(b))/b:.6f}')
open('runs/cnb/cnb-run1.txt', 'w').write('\n'.join(out)+'\n')
