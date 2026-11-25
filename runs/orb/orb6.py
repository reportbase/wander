# ORB run 6: the orbit at e >= 1. Predictions R1-R6 in plans/orb-plan.md, committed first.
#   python3 runs/orb/orb6.py
import sympy as sp
import mpmath as mp
mp.mp.dps = 50
TOL = mp.mpf('1e-40')
out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)
ok = {}

nu, p, D, F, a, e, eta = sp.symbols('nu p D F a e eta', positive=True)
# R1: parabola y = r sin(nu) = p tan(nu/2); nu uniform on (-pi, pi) -> y Cauchy(0, p)
r_par = p/(1 + sp.cos(nu))
y = r_par*sp.sin(nu)
r1a = sp.simplify(sp.trigsimp(y - p*sp.tan(nu/2)))
yy = sp.symbols('y', real=True)
nu_of_y = 2*sp.atan(yy/p)
dens = sp.simplify(sp.diff(nu_of_y, yy)/(2*sp.pi))
r1b = sp.simplify(dens - p/(sp.pi*(p**2 + yy**2)))
# uniform D pushed to nu: dD/dnu = (1 + D^2)/2, total infinite
dDdnu = sp.simplify(sp.diff(sp.tan(nu/2), nu) - (1 + sp.tan(nu/2)**2)/2)
tot = sp.integrate((1 + sp.tan(nu/2)**2)/2, (nu, 0, sp.pi - sp.Rational(1, 10**6)))
say('R1 y - p tan(nu/2) =', r1a, '; density of y - Cauchy(0,p) =', r1b, '; dD/dnu - (1+D^2)/2 =', dDdnu,
    '; uniform-D weight on (0, pi - 1e-6) =', sp.N(tot, 8), '(grows without bound)')
ok['R1'] = r1a == 0 and r1b == 0 and dDdnu == 0 and tot > 10**5

# R2: parabola time: dt/dnu ∝ r^2, nu = 2 atan D -> dt/dD ∝ (1+D^2); reciprocal of the Cauchy in y = pD
rD = (p/2)*(1 + D**2)
dt_dD = sp.simplify(rD**2 * sp.diff(2*sp.atan(D), D))
r2a = sp.simplify(dt_dD/(1 + D**2))                      # a constant
cauchy_y = 1/(sp.pi*p*(1 + D**2))                        # Cauchy(0,p) density in y at y = pD
r2b = sp.simplify(dt_dD*cauchy_y)
M = sp.integrate(1 + D**2, (D, 0, D))
say('R2 (dt/dD)/(1+D^2) =', r2a, '; clock x Cauchy density =', r2b, '; integral =', M)
ok['R2'] = r2a.free_symbols <= {p} and r2b.free_symbols <= {p} and sp.simplify(M - (D + D**3/3)) == 0

# R3: e_h = coth(eta) gives sqrt((e+1)/(e-1)) = exp(eta) = sqrt((1+e_e)/(1-e_e)) with e_e = tanh(eta) = 1/e_h
kh = sp.sqrt((sp.coth(eta) + 1)/(sp.coth(eta) - 1))
r3a = sp.simplify((kh - sp.exp(eta)).rewrite(sp.exp))
ee = sp.symbols('epsilon', positive=True)
r3b = sp.simplify(((1/ee + 1)/(1/ee - 1)) - (1 + ee)/(1 - ee))
# the hyperbolic map holds: check tan(nu/2) = K tanh(F/2) from r = a(e cosh F - 1), x, y coordinates numerically
worst3 = mp.mpf(0)
for es in ['1.01', '1.5', '3', '20']:
    ev = mp.mpf(es); K = mp.sqrt((ev + 1)/(ev - 1))
    for Fv in [mp.mpf(x) for x in ['-3', '-0.4', '0.1', '1.2', '5']]:
        x = ev - mp.cosh(Fv); yv = mp.sqrt(ev*ev - 1)*mp.sinh(Fv)   # focus at origin, a = 1
        nuv = mp.atan2(yv, x)
        worst3 = max(worst3, abs(mp.tan(nuv/2) - K*mp.tanh(Fv/2)))
say('R3 K(coth eta) - e^eta =', r3a, '; k(1/e)^2 - k(e)^2 =', r3b, '; hyperbolic map worst', mp.nstr(worst3, 3))
ok['R3'] = r3a == 0 and r3b == 0 and worst3 < TOL

# R4: nu uniform on (-nu_inf, nu_inf) -> t = tan(nu/2) Cauchy cut to |t| < K
worst4 = mp.mpf(0)
for es in ['1.01', '1.5', '3', '20']:
    ev = mp.mpf(es); K = mp.sqrt((ev + 1)/(ev - 1)); ninf = mp.acos(-1/ev)
    assert abs(mp.tan(ninf/2) - K) < TOL
    for i in range(200):
        t = -K + 2*K*(i + mp.mpf('0.5'))/200
        dens_t = (2/(1 + t*t))/(2*ninf)                       # dnu/dt / range
        cut = (1/(1 + t*t))/(2*mp.atan(K))
        worst4 = max(worst4, abs(dens_t - cut))
say('R4 uniform nu against the Cauchy cut at |t| < K, worst', mp.nstr(worst4, 3), '; tan(nu_inf/2) = K at all four')
ok['R4'] = worst4 < TOL

# R5: dM/dF = r/a for the hyperbola
Mh = e*sp.sinh(F) - F
r5 = sp.simplify(sp.diff(Mh, F) - (e*sp.cosh(F) - 1))
say('R5 dM/dF - r/a =', r5)
ok['R5'] = r5 == 0

# R6: share of the elliptic stage on |nu| < 1 as e -> 1-
shares = []
for n in [2, 4, 8]:
    ev = 1 - mp.mpf(10)**(-n)
    s = mp.quad(lambda x: mp.sqrt(1 - ev*ev)/(2*mp.pi*(1 + ev*mp.cos(x))), [-1, 1])
    shares.append(s)
say('R6 stage share on |nu| < 1 at e = 1 - 1e-2, 1e-4, 1e-8:', ', '.join(mp.nstr(s, 4) for s in shares))
ok['R6'] = shares[0] > shares[1] > shares[2] and shares[2] < mp.mpf('1e-3')
say('verdicts:', ', '.join(f'{k} {"not killed" if v else "KILLED"}' for k, v in ok.items()))
open('runs/orb/orb-run6.txt', 'w').write('\n'.join(out) + '\n')
