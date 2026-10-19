"""HZT: the horizon test, the exact checks. See plans/hzt-plan.md (predictions written before the search).

For each entry of plans/hzt/neutral-list.md, the law is computed from the derivation step the list gives (a change of
variables, a quadrature, a Fourier transform, a pole, a field sum) and compared with the formula as the list writes it,
at sample points. Then, for the law once matched: the share within one half-width of the centre (H4: 1/2 for the Cauchy),
the angle or phase at the half-width where the step has one (H4: 45 degrees from the sweep's middle or start), and the
growth of the first moment over a decade of range (H5: gamma*ln(10)/pi for the Cauchy, so no mean). mpmath, 30 digits.
The mechanism assigned to each entry is a judgment read from its derivation step; the computations check the
constants, not the judgment. Run: python3 -I runs/hzt/hzt.py [1|2]  (run 1 as first run; run 2 takes oscillatory integrals by quadosc)
"""
import sys
from mpmath import mp, mpf, pi, quad, quadosc, atan, tan, sin, cos, exp, sqrt, log, inf, diff, cosh, fabs, mpc, arg, gamma as G

mp.dps = 25
RUN = int(sys.argv[1]) if len(sys.argv) > 1 else 2   # run 2: oscillatory integrals to infinity by quadosc
TOL = mpf(10) ** -18
XS = [mpf(x) for x in ('0', '0.3', '1', '2.5', '7')]
cauchy = lambda x, x0=0, g=1: g / (pi * ((x - x0) ** 2 + g ** 2))

def share(f, g):            # mass within one half-width of the centre (centre 0)
    return quad(f, [-g, 0, g])
def decade(f, S=mpf(10) ** 4):   # growth of the first moment (one side) from S to 10 S
    return quad(lambda x: x * f(x), [S, 10 * S])

# each mechanism returns the law computed from the step, as a function of x, for scale g (centre 0)
def m_turn(g):              # x = g tan(theta), theta uniform on (-pi/2, pi/2): density = (1/pi) dtheta/dx
    return lambda x: diff(lambda u: atan(u / g), x) / pi
def m_half_angle(g):        # stereographic: x = g tan(phi/2), phi uniform on (-pi, pi)
    return lambda x: diff(lambda u: 2 * atan(u / g), x) / (2 * pi)
def m_ratio(g):             # X/Y, X ~ N(0, g^2), Y ~ N(0, 1): integrate |y| out
    return lambda r: quad(lambda y: abs(y) * exp(-(r * y) ** 2 / (2 * g ** 2)) / g * exp(-y ** 2 / 2) / (2 * pi), [-inf, 0, inf])
def m_mixture(g):           # normal with variance s * g^2, s ~ inverse-gamma(1/2, 1/2): Student t1 / Zellner-Siow
    ig = lambda s: (mpf(1) / 2) ** mpf('0.5') / G(mpf('0.5')) * s ** mpf('-1.5') * exp(-1 / (2 * s))
    return lambda x: quad(lambda s: ig(s) * exp(-x ** 2 / (2 * s * g ** 2)) / sqrt(2 * pi * s * g ** 2), [0, 1, inf])
def m_ft(g):                # spectrum of a decaying exponential: (1/2pi) int e^(-g|t|) e^(-ixt) dt
    if RUN >= 2:
        return lambda x: (quadosc(lambda t: exp(-g * t) * cos(x * t), [0, inf], omega=x) if x != 0 else quad(lambda t: exp(-g * t), [0, inf])) / pi
    return lambda x: quad(lambda t: exp(-g * t) * cos(x * t), [0, inf]) / pi
def m_pole(g):              # |1/(x + i g)|^2, normalised: (g/pi) / |x + i g|^2
    return lambda x: g / pi / abs(mpc(x, g)) ** 2
def m_harmonic(g):          # harmonic measure of the half-plane from (0, g): the angle subtended, uniform from the point
    return lambda x: diff(lambda u: atan(u / g), x) / pi
def m_image(g):             # line charge at height g above a grounded plane: normal field of the charge and its image
    return lambda x: (g / (x ** 2 + g ** 2) + g / (x ** 2 + g ** 2)) / (2 * pi)    # (E_y of each line ~ (1/2pi) g/r^2)
def m_line_source(g):       # isotropic points along an infinite line at height g: integrate along the line
    return lambda x: quad(lambda z: g / (x ** 2 + g ** 2 + z ** 2) ** mpf('1.5'), [-inf, 0, inf]) / (2 * pi)
def m_kacrice(g):           # Kostlan zeros: (1/pi) sqrt(d_x d_y log K) at y = x, K = (1 + xy)^n, normalised by sqrt(n)
    n = 7
    return lambda x: sqrt(diff(lambda a, b: n * log(1 + a * b), (x, x), (1, 1))) / (pi * sqrt(n))
def m_agnesi(g):            # Agnesi: circle of diameter 2a tangent at the origin; line at angle theta from the y axis
    a = g / 2               # meets y = 2a at x = 2a tan(theta), the circle at height 2a cos^2(theta)
    def y(x):
        th = atan(x / (2 * a)); return 2 * a * cos(th) ** 2
    norm = quad(y, [-inf, 0, inf])
    return lambda x: y(x) / norm
def m_wrapped(g):           # unwrap the disc's Poisson kernel: wrapped Cauchy(0, g) at theta, against the sum of the line's
    return lambda th: sum(cauchy(th + 2 * pi * k, 0, g) for k in range(-2000, 2001))
def m_stable(g):            # characteristic function e^(-g|t|) inverted (as m_ft, written as the cf)
    return m_ft(g)
def m_dipole_cf():          # 3D uniform positions, shift ~ A/r^3: log cf = n int (1 - cos(t A / r^3)) d^3 r is linear in |t|
    if RUN >= 2:            # run 2: u = 1/r^3, d^3 r = (4 pi/3) u^-2 du
        f = lambda t: quadosc(lambda u: (1 - cos(t * u)) * 4 * pi / (3 * u ** 2), [0, inf], omega=t)
    else:
        f = lambda t: quad(lambda r: (1 - cos(t / r ** 3)) * 4 * pi * r ** 2, [0, 1, inf])
    return f(1), f(2)
def m_planar_cf():          # planar Poisson field, amplitude r^-2: int (1 - cos(t r^-2)) 2 pi r dr is linear in |t|
    if RUN >= 2:            # run 2: u = 1/r^2, 2 pi r dr = pi u^-2 du
        f = lambda t: quadosc(lambda u: (1 - cos(t * u)) * pi / u ** 2, [0, inf], omega=t)
    else:
        f = lambda t: quad(lambda r: (1 - cos(t / r ** 2)) * 2 * pi * r, [0, 1, inf])
    return f(1), f(2)

# the corner: the angle or phase at the half-width, measured from the sweep's middle (centre) direction
corner_angle = {
    'turn': lambda g: atan(g / g), 'half_angle': lambda g: 2 * atan(g / g) / 2, 'harmonic': lambda g: atan(g / g),
    'ratio': lambda g: atan(g / g), 'pole': lambda g: fabs(arg(mpc(g, g)) - 0), 'ft': lambda g: fabs(arg(mpc(g, g))),
    'agnesi': lambda g: atan(g / g), 'kacrice': lambda g: atan(mpf(1)),
}
MECH = {'turn': m_turn, 'half_angle': m_half_angle, 'ratio': m_ratio, 'mixture': m_mixture, 'ft': m_ft, 'pole': m_pole,
        'harmonic': m_harmonic, 'image': m_image, 'line_source': m_line_source, 'kacrice': m_kacrice, 'agnesi': m_agnesi,
        'stable': m_stable}

# entry: id -> (mechanism, note). 'cut' marks a law the list says is used near its centre only (H5 records it).
E = {
 'H1': ('stable', 'cf e^-|t| inverted'), 'H2': ('ratio', ''), 'H3': ('mixture', 't1 as normal over chi-square precision'),
 'H4': ('turn', ''), 'H5': ('agnesi', 'the curve normalised'), 'H6': ('harmonic', ''), 'H7': ('stable', ''),
 'H8': ('harmonic', ''), 'H9': ('stable', 'cf e^-a|t| from the passage time'), 'H10': (None, 'a limit law; not computed'),
 'H11': ('wrapped', ''), 'H12': ('half_angle', ''), 'H13': ('pole', 'Im 1/(x - theta)'), 'H14': ('turn', 'cot 2Theta'),
 'H15': ('pole', 'Cauchy transform 1/(z + i g)'), 'H16': ('kacrice', ''), 'H17': ('ft', 'cut'), 'H18': ('ft', 'cut'),
 'H19': ('pole', 'wings; cut'), 'H20': ('ft', 'cut'), 'H21': ('pole', 'near resonance; cut'), 'H22': ('pole', ''),
 'H23': ('pole', ''), 'H24': ('ft', 'cut'), 'H25': ('dipole', 'cut at the nearest neighbour'), 'H26': ('ft', 'convolution; cut'),
 'H27': ('pole', 'cut'), 'H28': ('pole', 'cut'), 'H29': ('ft', 'cut (bounded below)'), 'H30': ('pole', 'q -> inf; cut'),
 'H31': ('airy', 'periodic'), 'H32': ('ft', 'cut'), 'H33': ('ft', ''), 'H34': ('pole', ''), 'H35': ('pole', ''),
 'H36': ('pole', ''), 'H37': ('pole', 'cut'), 'H38': ('pole', 'contour at the Cauchy pole'), 'H39': ('pole', 'cut (band)'),
 'H40': ('pole', 'cut'), 'H41': ('pole', 'N = 1'), 'H42': ('pole', 'small q; cut'), 'H43': ('ft', ''), 'H44': ('ft', 'cut'),
 'H45': ('pole', 'cut'), 'H46': ('pole', 'cut'), 'H47': ('pole', 'cut (fitted band)'), 'H48': ('ft', 'cut (measured band)'),
 'H49': ('image', ''), 'H50': ('line_source', ''), 'H51': ('planar', 'guard zone may cut'), 'H52': (None, 'alpha ~ 1.7 fitted; Cauchy a member only'),
 'H53': (None, 'a tail exponent only'), 'H54': ('mixture', '2Dt/1D Cauchy kernel as a scale mixture; cut'),
 'H55': ('mixture', 'Zellner-Siow'), 'H56': ('mixture', 'folded'), 'H57': ('turn', 'tan((0.5 - p) pi)'),
 'H58': ('pole', 'the loss is -log of this law'),
}

rows, kills = [], {'H4': [], 'H5': [], 'law': []}
XL = XS + [mpf(50), mpf(400)]
for k, (m, note) in E.items():
    g = mpf('1.7')
    if m in MECH:
        if m == 'kacrice': g = mpf(1)
        f = MECH[m](g)
        # the law from the step against the list's formula, at sample points out to 400/g half-widths (relative error)
        err = max(fabs(f(x) / cauchy(x, 0, g) - 1) for x in XL)
        # with the law matched, the matched law's half-width share and its first moment's growth over a decade, by
        # quadrature: share 1/2 and growth g*ln(10)/pi, so no mean
        c = lambda x: cauchy(x, 0, g)
        sh, dec = share(c, g), decade(c)
        ca = corner_angle[m](g) * 180 / pi if m in corner_angle else None
        okl = err < mpf(10) ** -12
        ok4 = fabs(sh - mpf(1) / 2) < mpf(10) ** -20 and (ca is None or fabs(ca - 45) < mpf(10) ** -20)
        ok5 = fabs(dec / (g * log(10) / pi) - 1) < mpf(10) ** -6
        rows.append((k, m, mp.nstr(err, 3), mp.nstr(sh, 12), None if ca is None else mp.nstr(ca, 12), mp.nstr(dec / (g * log(10) / pi), 10), note))
        if not okl: kills['law'].append(k)
        if not ok4: kills['H4'].append(k)
        if not ok5: kills['H5'].append(k)
    elif m == 'wrapped':
        f = m_wrapped(mpf('0.4'))
        rho = exp(-mpf('0.4'))
        disc = lambda th: (1 - rho ** 2) / (2 * pi * (1 + rho ** 2 - 2 * rho * cos(th)))
        err = max(fabs(f(x) - disc(x)) for x in [mpf(0), mpf('0.5'), mpf(2), pi])
        rows.append((k, m, mp.nstr(err, 3), 'on the circle', None, 'a mean direction exists (circle)', note))
        if err > mpf(10) ** -5: kills['law'].append(k)
    elif m in ('dipole', 'planar'):
        a, b = (m_dipole_cf() if m == 'dipole' else m_planar_cf())
        lin = b / a
        rows.append((k, m, f'log cf at 2t over at t: {mp.nstr(lin, 15)} (Cauchy: 2)', 'from the cf', None, 'no mean (index 1)', note))
        if fabs(lin - 2) > mpf(10) ** -10: kills['law'].append(k)
    elif m == 'airy':
        F = mpf(400)
        airy = lambda d: 1 / (1 + F * sin(d / 2) ** 2)
        hw = 2 / sqrt(F)
        lor = lambda d: 1 / (1 + (F / 4) * d ** 2)
        err = max(fabs(airy(d) - lor(d)) for d in [mpf(0), hw / 2, hw])
        rows.append((k, m, f'near the peak {mp.nstr(err, 3)} (F = 400)', 'periodic', None, 'periodic: the mean over a period exists', note))
    else:
        rows.append((k, None, 'not computed', '', None, '', note))

print(f"{'id':5s} {'mechanism':12s} {'law err':>12s} {'share':>16s} {'corner deg':>14s} {'decade/(g ln10/pi)':>20s}  note")
for r in rows:
    print(f"{r[0]:5s} {str(r[1]):12s} {r[2]:>12s} {r[3]:>16s} {str(r[4]):>14s} {r[5]:>20s}  {r[6]}")
print('\nlaw off:', kills['law'] or 'none'); print('H4 off:', kills['H4'] or 'none'); print('H5 off:', kills['H5'] or 'none')
