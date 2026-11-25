# ORB run 2: the orbit as a stage (the wrapped Cauchy of an even eccentric anomaly) and a payload (r/a).
# Predictions P1-P7 in plans/orb-plan.md, committed before this ran. Run from the repository's root:
#   python3 runs/orb/orb2.py
import sympy as sp
import mpmath as mp

mp.mp.dps = 50
ES = ['0.01', '0.1', '0.3', '0.6', '0.9', '0.99']
TOL = mp.mpf('1e-45')
out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

# ---- symbolic identities
e, nu, E = sp.symbols('e nu E', positive=True)
beta = (1 - sp.sqrt(1 - e**2)) / e
stage = sp.sqrt(1 - e**2) / (2*sp.pi*(1 + e*sp.cos(nu)))
wc = (1 - beta**2) / (2*sp.pi*(1 + beta**2 + 2*beta*sp.cos(nu)))      # wrapped Cauchy, rho = beta, centre pi
p1sym = sp.simplify(sp.together(wc - stage))
# the stage from E uniform: (1/2pi) dE/dnu, with tan(nu/2) = k tan(E/2)
k = sp.sqrt((1 + e)/(1 - e))
Eofnu = 2*sp.atan(sp.tan(nu/2)/k)
stageE = sp.simplify(sp.diff(Eofnu, nu)/(2*sp.pi))
p1sym2 = sp.simplify(sp.trigsimp(stageE - stage))
say('P1 symbolic: wrapped Cauchy - stage =', p1sym, '; (1/2pi)dE/dnu - stage =', p1sym2)

a, GM = sp.symbols('a GM', positive=True)
r = a*(1 - e**2)/(1 + e*sp.cos(nu))
h = sp.sqrt(GM*a*(1 - e**2))
T = 2*sp.pi*sp.sqrt(a**3/GM)
clock = r**2/h / T                                                    # time per direction, as a share of the period
p2sym = sp.simplify(clock/stage - r/a)
say('P2 symbolic: clock/stage - r/a =', p2sym)

p7sym = sp.simplify(sp.integrate(1 - e*sp.cos(E), (E, 0, E)) - (E - e*sp.sin(E)))
rE = a*(1 - e*sp.cos(E))
say('P7 symbolic: r/a in E =', sp.simplify(rE/a), '; its integral from 0 - (E - e sin E) =', p7sym)

# ---- numeric, at 50 digits
def stage_n(e, n): return mp.sqrt(1 - e*e)/(2*mp.pi*(1 + e*mp.cos(n)))
def wc_n(rho, mu, n): return (1 - rho*rho)/(2*mp.pi*(1 + rho*rho - 2*rho*mp.cos(n - mu)))
def rr(a, e, n): return a*(1 - e*e)/(1 + e*mp.cos(n))
def clock_n(a, GM, e, n):
    h = mp.sqrt(GM*a*(1 - e*e)); T = 2*mp.pi*mp.sqrt(a**3/GM)
    return rr(a, e, n)**2/h/T
nus = [-mp.pi + 2*mp.pi*(i + mp.mpf('0.5'))/200 for i in range(200)]

ok = {k: True for k in ['P1', 'P2', 'P3a', 'P3b', 'P4', 'P5']}
for es in ES:
    ev = mp.mpf(es); b = (1 - mp.sqrt(1 - ev*ev))/ev
    d1 = max(abs(wc_n(b, mp.pi, n) - stage_n(ev, n)) for n in nus)
    # the stage also as the push-forward of uniform E (derivative of E(nu))
    k_ = mp.sqrt((1 + ev)/(1 - ev))
    d1b = max(abs(mp.diff(lambda x: 2*mp.atan(mp.tan(x/2)/k_), n)/(2*mp.pi) - stage_n(ev, n)) for n in nus)
    d2 = max(abs(clock_n(1, 1, ev, n)/stage_n(ev, n) - rr(1, ev, n)) for n in nus)
    m_stage = mp.quad(lambda n: rr(1, ev, n)*stage_n(ev, n), [-mp.pi, 0, mp.pi])
    m_clock = mp.quad(lambda n: rr(1, ev, n)*clock_n(1, 1, ev, n), [-mp.pi, 0, mp.pi])
    d3a = abs(m_stage - 1); d3b = abs(m_clock - (1 + ev*ev/2))
    d4 = mp.mpf(0)
    for av in ['1', '7', '1000']:
        for gm in ['1', '3']:
            A = mp.mpf(av); G = mp.mpf(gm)
            h_ = mp.sqrt(G*A*(1 - ev*ev))
            per = mp.quad(lambda n: rr(A, ev, n)**2/h_, [-mp.pi, 0, mp.pi])
            d4 = max(d4, abs(per/(2*mp.pi*mp.sqrt(A**3/G)) - 1))
    # P5: a scaled by 1e3 at GM = 1
    d5s = max(abs(rr(1000, ev, n)/1000 - rr(1, ev, n)) for n in nus)
    per1 = mp.quad(lambda n: rr(1, ev, n)**2/mp.sqrt(1*(1 - ev*ev)), [-mp.pi, 0, mp.pi])
    perk = mp.quad(lambda n: rr(1000, ev, n)**2/mp.sqrt(1000*(1 - ev*ev)), [-mp.pi, 0, mp.pi])
    d5t = abs(perk/per1 - mp.mpf(1000)**mp.mpf('1.5'))/mp.mpf(1000)**mp.mpf('1.5')
    say(f'e={es}: P1 {mp.nstr(max(d1, d1b), 3)}  P2 {mp.nstr(d2, 3)}  P3 stage-mean-1 {mp.nstr(d3a, 3)}  '
        f'clock-mean-(1+e^2/2) {mp.nstr(d3b, 3)} [clock mean {mp.nstr(m_clock, 12)}]  P4 {mp.nstr(d4, 3)}  '
        f'P5 payload {mp.nstr(d5s, 3)} period {mp.nstr(d5t, 3)}')
    ok['P1'] &= max(d1, d1b) < TOL; ok['P2'] &= d2 < TOL; ok['P3a'] &= d3a < TOL; ok['P3b'] &= d3b < TOL
    ok['P4'] &= d4 < TOL; ok['P5'] &= d5s < TOL and d5t < TOL

# P6: best wrapped Cauchy against the clock law, largest relative difference over 2,000 nu (double precision is
# enough here: the question is whether the gap is above 1%)
import numpy as np
from scipy.optimize import minimize
nn = -np.pi + 2*np.pi*(np.arange(2000) + 0.5)/2000
p6 = {}
for ev in [0.3, 0.6, 0.9]:
    c = (1 - ev*ev)**1.5/(2*np.pi*(1 + ev*np.cos(nn))**2)
    def worst(x):
        rho = np.tanh(x[0]); mu = x[1]
        w = (1 - rho*rho)/(2*np.pi*(1 + rho*rho - 2*rho*np.cos(nn - mu)))
        return np.max(np.abs(w/c - 1))
    best = min((minimize(worst, [np.arctanh(r0), m0], method='Nelder-Mead',
                         options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 20000})
                for r0 in [-0.9, -0.5, -0.2, 0.2, 0.5, 0.9] for m0 in [0.0, np.pi]), key=lambda s: s.fun)
    p6[ev] = (best.fun, np.tanh(best.x[0]), best.x[1] % (2*np.pi))
    say(f'P6 e={ev}: best wrapped Cauchy misses the clock by {best.fun:.4f} at most (rho {p6[ev][1]:.4f}, '
        f'centre {p6[ev][2]:.4f})')
ok['P6'] = all(v[0] >= 0.01 for v in p6.values())
ok['P1'] &= p1sym == 0 and p1sym2 == 0
ok['P2'] &= p2sym == 0
ok['P7'] = p7sym == 0 and sp.simplify(rE/a - (1 - e*sp.cos(E))) == 0
say('verdicts:', ', '.join(f'{k} {"not killed" if v else "KILLED"}' for k, v in ok.items()))
open('runs/orb/orb-run2.txt', 'w').write('\n'.join(out) + '\n')
