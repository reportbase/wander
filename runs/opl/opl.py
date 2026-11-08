# OPL run 1: plans/opl-plan.md. Run from the repository root: python3 runs/opl/opl.py
import mpmath as mp, sympy as sp
mp.mp.dps = 30
pi = mp.pi
K = {
 'C':  lambda s: 1/(pi*(1+s*s)),
 'G':  lambda s: mp.e**(-s*s/2)/mp.sqrt(2*pi),
 'S':  lambda s: mp.sech(pi*s/2)/2,
 'L':  lambda s: mp.e**(-abs(s))/2,
 'T3': lambda s: 2/(pi*(1+s*s)**2),
 'R2': lambda s: (1/(pi*(1+(s-1)**2)) + 1/(pi*(1+(s+1)**2)))/2,
}
CLOSED = {
 'C': lambda t: mp.e**(-t), 'G': lambda t: mp.e**(-t*t/2), 'S': lambda t: mp.sech(t),
 'L': lambda t: 1/(1+t*t), 'T3': lambda t: (1+t)*mp.e**(-t), 'R2': lambda t: mp.cos(t)*mp.e**(-t),
}
def phi(k, t):
    f = K[k]
    if t == 0: return mp.quad(f, [-mp.inf, -1, 0, 1, mp.inf])
    re = mp.quadosc(lambda s: f(s)*mp.cos(t*s), [-mp.inf, mp.inf], omega=t)
    im = mp.quadosc(lambda s: f(s)*mp.sin(t*s), [-mp.inf, mp.inf], omega=t)
    return mp.mpc(re, im)
print('O1: quadrature against closed form')
o1 = True
for k in K:
    worst = max(abs(phi(k, mp.mpf(t)) - CLOSED[k](mp.mpf(t))) for t in [0, 0.5, 1, 2, 4])
    print(f'  {k:3s} worst |diff| = {mp.nstr(worst, 3)}'); o1 &= worst < 1e-10
print('  O1', 'held' if o1 else 'KILLED')

print('O2: pure phasor test on t in [0.25, 5] (closed forms, checked in O1)')
ts = [mp.mpf(0.25) + i*mp.mpf(4.75)/40 for i in range(41)]
def linfit_resid(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    b = sum((x-mx)*(y-my) for x, y in zip(xs, ys))/sum((x-mx)**2 for x in xs); a = my - b*mx
    return max(abs(y - a - b*x) for x, y in zip(xs, ys))
passing = []
for k in K:
    v = [mp.mpc(CLOSED[k](t)) for t in ts]
    if any(abs(x) < mp.mpf(10)**-25 for x in v): r1 = r2 = mp.inf
    else:
        lm = [mp.log(abs(x)) for x in v]; ar = [mp.arg(x) for x in v]
        r1, r2 = linfit_resid(ts, lm), linfit_resid(ts, ar)
    ok = r1 < 1e-9 and r2 < 1e-9
    print(f'  {k:3s} ln|phi| resid {mp.nstr(r1,3):>10s}  arg resid {mp.nstr(r2,3):>10s}  pure phasor: {ok}')
    if ok: passing.append(k)
print('  O2', 'held' if passing == ['C'] else 'KILLED', passing)

print('O3: residue sums above the line')
s_ = sp.symbols('s'); t_ = sp.symbols('t', positive=True)
def res_sum(expr, poles, t):
    tot = 0
    for p in poles: tot += sp.residue(sp.exp(sp.I*t_*s_)*expr, s_, p)
    return complex(sp.N((2*sp.pi*sp.I*tot).subs(t_, t), 30))
symb = {'C': 1/(sp.pi*(1+s_**2)), 'T3': 2/(sp.pi*(1+s_**2)**2),
        'R2': (1/(sp.pi*(1+(s_-1)**2)) + 1/(sp.pi*(1+(s_+1)**2)))/2}
poles = {'C': [sp.I], 'T3': [sp.I], 'R2': [1+sp.I, -1+sp.I]}
o3 = True
for k in symb:
    worst = max(abs(res_sum(symb[k], poles[k], t) - complex(CLOSED[k](mp.mpf(t)))) for t in [0.5, 1, 2, 4])
    print(f'  {k:3s} poles {poles[k]} worst {worst:.2e}'); o3 &= worst < 1e-10
def sech_series(t, n=200): return 2*sum((-1)**k*mp.e**(-(2*k+1)*t) for k in range(n))
worst = max(abs(sech_series(mp.mpf(t)) - mp.sech(t)) for t in [0.5, 1, 2, 4])
print(f'  S   poles i(2k+1), 200 terms, worst {mp.nstr(worst,3)}'); o3 &= worst < 1e-10
print('  O3', 'held' if o3 else 'KILLED')

print('O4: the total at t = 0 as residues')
parts = [sech_series(mp.mpf(0), n) for n in (10, 11, 100, 101)]
print('  S partial sums at t = 0 (10, 11, 100, 101 terms):', [mp.nstr(p, 3) for p in parts])
abel = mp.limit(lambda x: 2*mp.nsum(lambda k: (-1)**k*x**(2*k+1), [0, mp.inf]), 1, direction=-1)
print('  S Abel sum:', mp.nstr(abel, 10))
for k in ('C', 'T3'):
    tot = complex(sp.N(2*sp.pi*sp.I*sp.residue(symb[k], s_, sp.I), 20))
    print(f'  {k:3s} total from one residue at i: {tot.real:.12f}')
o4 = abs(parts[2] - parts[3]) > 1   # not converging
print('  O4', 'held' if o4 else 'KILLED')

print('O5: real, positive, even rational kernels with one simple pole above the line')
a, b, c, d = sp.symbols('a b c d', real=True)
m, g = sp.symbols('m g', real=True)
P = a + b*s_
f = P/((s_-m)**2 + g**2)
even = sp.solve(sp.Poly(sp.expand(sp.numer(sp.together(f - f.subs(s_, -s_)))), s_).coeffs(), [b, m], dict=True)
print('  evenness forces:', even)
print('  with b = 0 the kernel is a/((s - m)^2 + g^2): the Cauchy (positivity a > 0, decay as 1/s^2 forbids deg P >= 1)')
o5 = all(sol.get(b, None) == 0 for sol in even if b in sol) and len(even) > 0
print('  O5', 'held' if o5 else 'KILLED (or needs reading)')
