"""NRF run 1 (plans/nrf-plan.md): where an extended source turns from near to far, in levels. Exact arithmetic (sympy),
and 50-digit numerics (mpmath) where a closed form needs arctan."""
import sympy as sp, mpmath as mp
mp.mp.dps = 50
d, a, r, l, s, x = sp.symbols('d a rho l s x', positive=True)
def sigma(E, var):   # local slope in levels: d log2 E / d log2 var
    return sp.simplify(sp.diff(sp.log(E), var) * var)
print('Derivations (each from an integral over the source; L or lambda per unit area or length set to 1)')
# Lambertian disc, flat detector on axis: L cos(src) cos(det) dA / r^2, both cosines d/r
E_lam = sp.simplify(sp.integrate(2 * sp.pi * r * d**2 / (d**2 + r**2)**2, (r, 0, a)))
print('  Lambertian disc, flat patch:', E_lam, '  plan:', sp.simplify(E_lam - sp.pi * a**2 / (a**2 + d**2)) == 0)
# isotropic emitter per area, flat detector: cos(det) dA / r^2
E_iso_flat = sp.simplify(sp.integrate(2 * sp.pi * r * d / (d**2 + r**2)**sp.Rational(3, 2), (r, 0, a)))
print('  isotropic disc, flat patch:', E_iso_flat, '  = 2*pi*(1 - d/sqrt(d^2+a^2)):', sp.simplify(E_iso_flat - 2 * sp.pi * (1 - d / sp.sqrt(d**2 + a**2))) == 0)
E_iso_sph = sp.simplify(sp.integrate(2 * sp.pi * r / (d**2 + r**2), (r, 0, a)))
print('  isotropic disc, every direction (small sphere):', E_iso_sph)
# isotropic line, length 2b (b = 1 here, s = d): every direction and flat patch
E_line_sph = sp.simplify(sp.integrate(1 / (d**2 + l**2), (l, -1, 1)))
E_line_flat = sp.simplify(sp.integrate(d / (d**2 + l**2)**sp.Rational(3, 2), (l, -1, 1)))
print('  isotropic line, every direction:', E_line_sph, '  plan form (2/d)*atan(1/d):', sp.simplify(E_line_sph - 2 * sp.atan(1 / d) / d) == 0)
print('  isotropic line, flat patch:', E_line_flat)
print('  Lambertian sphere from its centre: E = pi*L*(R/d)^2 for d >= R (standard; the sphere subtends sin^2 = (R/d)^2)')
print()
res = {}
def check(name, E, var, near, far, plan_form=True):
    sg = sigma(E, var)
    at1 = sp.nsimplify(sp.simplify(sg.subs(var, 1)))
    flip = sp.simplify(sg + sg.subs(var, 1 / var))
    # numeric checks too (atan forms may not simplify)
    f = sp.lambdify(var, sg, 'mpmath')
    g1 = f(mp.mpf(1)); worst = max(abs(f(mp.mpf(t)) + f(1 / mp.mpf(t)) - (near + far)) for t in ['0.01', '0.1', '0.37', '2', '7.5', '30', '1000'])
    frac = lambda t: (f(t) - near) / (far - near)
    s10 = mp.findroot(lambda t: frac(t) - mp.mpf('0.1'), mp.mpf('0.3')); s90 = mp.findroot(lambda t: frac(t) - mp.mpf('0.9'), mp.mpf('3'))
    w = mp.log(s90 / s10, 2)
    print(f'{name}: sigma(s) = {sg}')
    print(f'   sigma(1) = {mp.nstr(g1, 15)} (halfway {(near + far) / 2}); sigma(s)+sigma(1/s) symbolic: {flip}; worst numeric miss from {near + far}: {mp.nstr(worst, 3)}')
    print(f'   10%-90% from s = {mp.nstr(s10, 6)} to {mp.nstr(s90, 6)}: width {mp.nstr(w, 6)} levels')
    return g1, worst, w
S = sp.symbols('s', positive=True)
P1 = check('P1 Lambertian disc', 1 / (1 + S**2), S, 0, -2)
Rr = sp.symbols('R', positive=True)
sc = sigma((Rr / d)**2, d); print(f'P2 sphere from its centre: sigma = {sc} at every d >= R')
P2 = check('P2 Lambertian sphere, from its surface (s = gap/R)', 1 / (1 + S)**2, S, 0, -2)
P3 = check('P3 isotropic line, every direction (plan form)', sp.atan(1 / S) / S, S, -1, -2)
P4 = check('P4 isotropic disc, flat patch (plan form)', 1 - S / sp.sqrt(1 + S**2), S, 0, -2)
print('information (not predictions):')
I1 = check('  isotropic line, flat patch', 1 / (S * sp.sqrt(1 + S**2)), S, -1, -2)
I2 = check('  isotropic disc, every direction', sp.log(1 + 1 / S**2), S, 0, -2)
print()
ok = lambda g, want, w: abs(g - want) < mp.mpf('1e-12') and w < mp.mpf('1e-12')
print('P1:', 'not killed' if ok(P1[0], -1, P1[1]) else 'KILLED', '(disc: sigma(1) = -1 and the flip identity)')
print('P2:', 'not killed' if sc == -2 and ok(P2[0], -1, P2[1]) else 'KILLED', '(sphere: -2 from the centre; from the surface sigma(1) = -1 and the flip)')
print('P3:', 'not killed' if ok(P3[0], mp.mpf('-1.5'), P3[1]) else 'KILLED', f'(line: sigma(1) = {mp.nstr(P3[0], 12)}, flip miss {mp.nstr(P3[1], 3)})')
print('P4:', 'not killed' if ok(P4[0], -1, P4[1]) else 'KILLED', f'(solid-angle disc: sigma(1) = {mp.nstr(P4[0], 12)}, flip miss {mp.nstr(P4[1], 3)})')
ws = [P1[2], P2[2], P3[2], P4[2]]
print('P5:', 'not killed' if abs(P1[2] - mp.log(9, 2)) < 1e-9 and all(2 <= w <= 5 for w in ws) else 'KILLED', '(widths', ', '.join(mp.nstr(w, 4) for w in ws), 'levels)')
