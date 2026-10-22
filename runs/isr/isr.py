"""ISR: the inverse square revisited as addresses and payload (plans/isr-plan.md). Exact (mpmath, 50 digits).
Run from the repository's root: python3 runs/isr/isr.py"""
from mpmath import mp, mpf, pi, gamma, sqrt, atan, quad, diff, log, inf, findroot
mp.dps = 50
TOL40, TOL30 = mpf(10) ** -40, mpf(10) ** -30
verdict = {}

def sphere_area(D):            # |S^{D-1}|
    return 2 * pi ** (mpf(D) / 2) / gamma(mpf(D) / 2)

def cauchy_n(n, r, d):         # n-dimensional Cauchy density of scale d at radius r
    return gamma(mpf(n + 1) / 2) * d / (pi ** (mpf(n + 1) / 2) * (d * d + r * r) ** (mpf(n + 1) / 2))

# P1: the point source's light on a flat receiver is half the (D-1)-dim Cauchy; its height the inverse (D-1)-th power
print('P1  the inverse square as the Cauchy\'s height')
worst = mpf(0)
for D in (2, 3, 4, 5):
    n, P = D - 1, mpf(1)
    for d in (mpf('0.3'), mpf(1), mpf('2.7')):
        for r in (mpf(0), d / 3, d, 3 * d, 17 * d):
            R = sqrt(d * d + r * r)
            first = P * (d / R) / (sphere_area(D) * R ** (D - 1))     # P cos(theta) / (|S| R^(D-1)): from first principles
            worst = max(worst, abs(first - P / 2 * cauchy_n(n, r, d)) / first)
        height = P / 2 * cauchy_n(n, 0, d)
        worst = max(worst, abs(height * sphere_area(D) * d ** (D - 1) - P))
    # the receiver catches exactly half (the Cauchy integrates to 1 over the plane)
    tot = quad(lambda r: sphere_area(n) * r ** (n - 1) * cauchy_n(n, r, 1), [0, 1, 10, inf]) if n > 1 else 2 * quad(lambda r: cauchy_n(1, r, 1), [0, 1, inf])
    print(f'   D = {D}: receiver catches {mp.nstr(tot / 2, 20)} of P (half)')
    worst = max(worst, abs(tot - 1))
print(f'   worst miss {mp.nstr(worst, 5)}')
verdict['P1'] = worst < TOL40

# P2 (a): the isotropic line; (b) the Lambertian disc; (c) NRF's slope mixes address and payload
print('P2  the corner in the address count, the fall-off in the payload')
lam, w2 = mpf(1), mpf(0)
E_line = lambda b, d: lam / (4 * pi * d) * 2 * atan(b / d)
for b, d in ((mpf(1), mpf(1)), (mpf('0.4'), mpf(3)), (mpf(5), mpf('0.7'))):
    num = quad(lambda l: lam / (4 * pi * (d * d + l * l)), [-b, 0, b])
    w2 = max(w2, abs(num - E_line(b, d)))
    for phi in (mpf('0.1'), mpf('0.6'), atan(b / d) * mpf('0.99')):   # received power per unit angle at the address phi
        l = d * mp.tan(phi); dl = d / mp.cos(phi) ** 2
        w2 = max(w2, abs(lam * dl / (4 * pi * (d * d + l * l)) - lam / (4 * pi * d)))
f = lambda s: 2 / pi * atan(s)
for s in (mpf('0.01'), mpf('0.3'), mpf(1), mpf(7), mpf(1000)):
    w2 = max(w2, abs(f(s) + f(1 / s) - 1))
w2 = max(w2, abs(f(1) - mpf(1) / 2))
L = mpf(1)
for a, d in ((mpf(1), mpf(1)), (mpf('0.2'), mpf(4)), (mpf(3), mpf('0.5'))):
    num = quad(lambda rho: L * 2 * pi * rho * d * d / (d * d + rho * rho) ** 2, [0, a])
    w2 = max(w2, abs(num - pi * L * a * a / (a * a + d * d)))
g = lambda s: s * s / (1 + s * s)
for s in (mpf('0.01'), mpf('0.3'), mpf(1), mpf(7)):
    w2 = max(w2, abs(g(s) + g(1 / s) - 1))
sig1 = diff(lambda ld: log(E_line(mpf(1), mp.e ** ld)), 0)          # slope of E in ln d at b = d
addr = diff(lambda ld: log(f(1 / mp.e ** ld)), 0)                    # the address factor's own slope, s = b/d
print(f'   line: sigma(1) = {mp.nstr(sig1, 15)} (-1 - 2/pi = {mp.nstr(-1 - 2 / pi, 15)}); address factor alone {mp.nstr(addr, 15)} (-2/pi)')
w2 = max(w2, abs(sig1 - (-1 - 2 / pi)), abs(addr + 2 / pi))
print(f'   worst miss {mp.nstr(w2, 5)}')
verdict['P2'] = w2 < TOL40

# P3: pairs at their corner on the plane (D = 3)
print('P3  every pair at its corner on the receiver')
iso = lambda x, y: 1 / (2 * pi) * (1 + x * x + y * y) ** mpf('-1.5')          # d = 1, normalized over the plane
lam_ = lambda x, y: 1 / pi * (1 + x * x + y * y) ** -2                       # cos-weighted
marg = lambda dens, x: 2 * quad(lambda y: dens(x, y), [0, 1, inf])
P_abs_x_lt1_iso = 2 * quad(lambda x: marg(iso, x), [0, 1])
rad_iso = lambda s: 1 - 1 / sqrt(1 + s * s)                                   # radial CDF, isotropic
rad_iso_num = quad(lambda r: 2 * pi * r * iso(r, 0), [0, sqrt(3)])
rad_lam_num = quad(lambda r: 2 * pi * r * lam_(r, 0), [0, 1])
med_x_lam = findroot(lambda t: 2 * quad(lambda x: marg(lam_, x), [0, t]) - mpf(1) / 2, mpf('0.6'))
p_yx = mpf(1) / 2   # |y/x| < 1: the azimuth is uniform for both laws, so the share within 45 degrees of the x axis is 1/2
print(f'   isotropic: P(|x|/d < 1) = {mp.nstr(P_abs_x_lt1_iso, 20)}; P(r/d < sqrt 3) = {mp.nstr(rad_iso_num, 20)}')
print(f'   cos-weighted: P(r/d < 1) = {mp.nstr(rad_lam_num, 20)}; median |x|/d = {mp.nstr(med_x_lam, 20)} (predicted sqrt(2/3) = {mp.nstr(sqrt(mpf(2) / 3), 20)}; 1/sqrt 3 = {mp.nstr(1 / sqrt(3), 20)})')
w3a = max(abs(P_abs_x_lt1_iso - mpf(1) / 2), abs(rad_iso_num - mpf(1) / 2), abs(rad_lam_num - mpf(1) / 2))
w3b = abs(med_x_lam - sqrt(mpf(2) / 3))
print(f'   isotropic pairs and radial, Lambertian radial: worst miss {mp.nstr(w3a, 5)}; Lambertian per-axis: miss {mp.nstr(w3b, 5)}')
verdict['P3'] = w3a < TOL30 and w3b < TOL30

# P4: cos-weighted share sin^(D-1) theta reciprocal-symmetric only at D = 3; uniform emission's 1-D marginal Cauchy in every D
print('P4  the weighting and the dimension')
sym = []
for D in range(2, 7):
    h = lambda s: (s / sqrt(1 + s * s)) ** (D - 1)
    sym.append((D, h(1)))
fair = [D for D, v in sym if abs(v - mpf(1) / 2) < TOL30]
print('   cos-weighted share at the corner s = 1: ' + ', '.join(f'D={D}: {mp.nstr(v, 6)}' for D, v in sym))
w4 = mpf(0)
for D in range(2, 7):
    n = D - 1
    if n == 1:
        m = lambda x: cauchy_n(1, x, 1)
    else:
        m = lambda x, n=n: quad(lambda r: sphere_area(n - 1) * r ** (n - 2) * cauchy_n(n, sqrt(x * x + r * r), 1), [0, 1, 10, inf])
    for x in (mpf(0), mpf('0.5'), mpf(2)):
        w4 = max(w4, abs(m(x) - cauchy_n(1, x, 1)))
    w4 = max(w4, abs(2 * quad(m, [0, 1]) - mpf(1) / 2))
print(f'   reciprocal-symmetric only at D = {fair}; uniform emission\'s 1-D marginal: worst miss from the Cauchy {mp.nstr(w4, 5)}')
verdict['P4'] = fair == [3] and w4 < TOL30

# P5: counts by flux are a reading
print('P5  counts by flux')
kinds = ((mpf(1), mpf('0.7')), (mpf(30), mpf('0.3')))
def N_gt(S, k=mpf(1), n0=mpf(1)):
    return sum(w * n0 / k ** 3 * 4 * pi / 3 * (k * k * Lk / (4 * pi * S)) ** mpf('1.5') for Lk, w in kinds)
sl = [diff(lambda lS: log(N_gt(mp.e ** lS)), log(S)) for S in (mpf('1e-6'), mpf(1), mpf(1000))]
mv = max(abs(N_gt(S, k) / N_gt(S) - 1) for S in (mpf('1e-3'), mpf(2)) for k in (mpf('0.01'), mpf(7), mpf(100)))
T = mpf(1)
def slab(S):
    tot = mpf(0)
    for Lk, w in kinds:
        R = sqrt(Lk / (4 * pi * S))
        tot += w * ((4 * pi / 3) * R ** 3 if R <= T / 2 else pi * (R * R * T - T ** 3 / 12))
    return tot
grid = [mp.e ** x for x in mp.linspace(-14, 6, 81)]
ss = [diff(lambda lS: log(slab(mp.e ** lS)), log(S)) for S in grid]
mono = all(ss[i] >= ss[i + 1] - mpf(10) ** -20 for i in range(len(ss) - 1))   # from about -1 (S small) down to -3/2 (S large)
print(f'   homogeneous: slopes {[mp.nstr(x, 12) for x in sl]}; scaling moves N by {mp.nstr(mv, 5)}')
print(f'   slab: slope {mp.nstr(ss[0], 6)} at small S, {mp.nstr(ss[-1], 6)} at large S, monotone {mono}, within (-3/2, -1): {all(-1.5 - 1e-20 <= x <= -1 + 1e-20 for x in ss)}')
verdict['P5'] = max(abs(x + mpf('1.5')) for x in sl) < TOL30 and mv < TOL30 and mono and all(-1.5 - 1e-20 <= x <= -1 + 1e-20 for x in ss)

print()
for k, v in verdict.items():
    print(f'{k}: {"not killed" if v else "KILLED"}')
