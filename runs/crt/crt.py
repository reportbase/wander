"""CRT: the routes into the Cauchy, checked (plans/cauchy-routes.md).

Every route below is compared, at 30 digits, with the Poisson kernel of the upper half-plane seen from z = m + i*gamma,
    p(x) = (1/pi) * gamma / ((x - m)^2 + gamma^2) = (1/pi) * Im 1/(x - z),
its distribution function F(x) = 1/2 + atan((x - m)/gamma)/pi, or its n-dimensional form. Each check prints the largest
difference found. All are classical; the point is to have them side by side and exact.

    python3 runs/crt/crt.py
"""
from mpmath import mp, mpf, pi, atan, tan, sqrt, exp, quad, inf, gamma as G, cos, sin, log, im, mpc, fabs

mp.dps = 30
m, g = mpf('0.7'), mpf('1.3')            # the standpoint z = m + i*g
z = mpc(m, g)
XS = [mpf(x) for x in ('-7.5', '-2', '-0.3', '0.7', '1.9', '4', '25')]


def p(x, m=m, g=g):
    return g / (pi * ((x - m) ** 2 + g ** 2))


def F(x, m=m, g=g):
    return mpf(1) / 2 + atan((x - m) / g) / pi


def report(name, worst):
    print(f'{name:58s} max |difference| {mp.nstr(worst, 3)}')
    return worst


out = {}

# 1. The turn: a uniform direction from z, straight to the line, lands at x = m + g*tan(theta).
#    P(landing <= x) is the share of the half turn below that ray.
out['turn'] = report('1 turn: uniform direction from z, straight to the line',
                     max(fabs((atan((x - m) / g) + pi / 2) / pi - F(x)) for x in XS))

# 2. Isotropic ratio, not Gaussian: (X, Y) uniform on the unit disc (rotation-invariant). P(Y/X <= s) for X > 0 half.
def disc_ratio_cdf(s):
    # P(Y <= s X | X > 0) on the right half disc, in polar: share of the angle (-pi/2, atan s]
    return quad(lambda t: quad(lambda r: r, [0, 1]), [-pi / 2, atan(s)]) / quad(lambda t: quad(lambda r: r, [0, 1]), [-pi / 2, pi / 2])
out['ratio'] = report('2 ratio Y/X of a rotation-invariant (uniform-disc) pair',
                      max(fabs(disc_ratio_cdf(s) - F(s, 0, 1)) for s in (mpf(-3), mpf('-0.5'), mpf(0), mpf(2), mpf(10))))

# 3. Diffusion / hitting-time mixture: N(m, T) mixed over T, the first time a standard Brownian motion falls by g
#    (the Levy law, density g/sqrt(2 pi T^3) exp(-g^2/(2T))). This is where Brownian motion from z exits the half-plane.
def levy(t):
    return g / sqrt(2 * pi * t ** 3) * exp(-g ** 2 / (2 * t))
def mix(x):
    return quad(lambda t: exp(-(x - m) ** 2 / (2 * t)) / sqrt(2 * pi * t) * levy(t), [0, 1, 10, inf])
out['hit'] = report('3 normal mixed over the Levy hitting time (Brownian exit)', max(fabs(mix(x) - p(x)) for x in XS))

# 4. Pole / resonance: (g/pi)*|1/(x - z)|^2 is p(x), an identity; and the Fourier pair, int p(x) e^{ixt} dx = e^{imt - g|t|}.
out['pole'] = report('4a pole: (g/pi)|1/(x - z)|^2 = p(x) = (1/pi) Im 1/(x - z)',
                     max(max(fabs(g / pi / abs(x - z) ** 2 - p(x)), fabs(im(1 / (x - z)) / pi - p(x))) for x in XS))
def cf(t):
    # run 2: an oscillating integrand over an infinite range needs quadosc (run 1's quad missed by 1.6e-3)
    re = mp.quadosc(lambda x: p(x) * cos(x * t), [-inf, inf], omega=t)
    imv = mp.quadosc(lambda x: p(x) * sin(x * t), [-inf, inf], omega=t)
    return mpc(re, imv)
out['fourier'] = report('4b Fourier pair: e^{imt - g|t|}, a damped oscillation',
                        max(abs(cf(t) - exp(mpc(0, m * t) - g * abs(t))) for t in (mpf('0.5'), mpf('1.7'))))

# 5. Stable sums: C(z1) * C(z2) = C(z1 + z2).
z1, z2 = (mpf('0.4'), mpf('0.5')), (mpf('-1.1'), mpf('1.2'))
def conv(x):
    # run 2: both peaks as breakpoints (run 1 gave only the first, 1.9e-19)
    return quad(lambda y: p(y, *z1) * p(x - y, *z2), sorted([-inf, z1[0], x - z2[0], inf]))
out['sum'] = report('5 stable sum: C(z1)*C(z2) = C(z1 + z2)',
                    max(fabs(conv(x) - p(x, z1[0] + z2[0], z1[1] + z2[1])) for x in XS[:5]))

# 6. Moebius closure: X ~ C(z), Y = (aX + b)/(cX + d), ad - bc > 0, is C(g(z)) with g(z) = (az + b)/(cz + d).
a, b, c, d = mpf(2), mpf(1), mpf('0.5'), mpf(3)
w = (a * z + b) / (c * z + d)
def push_cdf(y):
    # Y <= y  <=>  X <= x(y) on the branch where cX + d > 0, plus the part beyond the pole
    xy = (d * y - b) / (a - c * y)
    pole = -d / c
    if a - c * y > 0:
        return F(xy) - F(pole) + 1 if xy < pole else F(xy) - F(pole)
    return 1 - F(pole) + F(xy)
out['mobius'] = report('6 Moebius image: (aX + b)/(cX + d) of C(z) is C(g(z))',
                       max(fabs(push_cdf(y) - F(y, w.real, w.imag)) for y in (mpf(-2), mpf('0.1'), mpf('0.6'), mpf(2), mpf(9))))

# 7. Stereographic / inscribed: phi uniform on the circle, x = tan(phi/2) from a point of the circle: C(0, 1).
out['stereo'] = report('7 stereographic: uniform on a circle seen from a point of it',
                       max(fabs((2 * atan(s) + pi) / (2 * pi) - F(s, 0, 1)) for s in (mpf(-4), mpf(-1), mpf('0.3'), mpf(5))))

# 8. Flat boundary, any dimension: the uniform hemisphere landing from height g on R^(n-1) equals the half-space's
#    Poisson kernel, Gamma(n/2)/pi^(n/2) * g / (r^2 + g^2)^(n/2). Compared as the share inside radius R.
def hemi_share(n, R):
    # uniform direction on the lower hemisphere of S^(n-1); polar angle a from the downward normal has density prop. sin^(n-2) a
    A = atan(R / g)
    return quad(lambda t: sin(t) ** (n - 2), [0, A]) / quad(lambda t: sin(t) ** (n - 2), [0, pi / 2])
def kernel_share(n, R):
    cst = G(mpf(n) / 2) / pi ** (mpf(n) / 2)
    surf = 2 * pi ** (mpf(n - 1) / 2) / G(mpf(n - 1) / 2)   # area of the unit sphere in R^(n-1)
    return quad(lambda r: cst * g / (r ** 2 + g ** 2) ** (mpf(n) / 2) * surf * r ** (n - 2), [0, R])
out['flat'] = report('8 flat boundary, n = 3, 4, 5: hemisphere landing = Poisson kernel',
                     max(fabs(hemi_share(n, R) - kernel_share(n, R)) for n in (3, 4, 5) for R in (mpf('0.5'), mpf(2), mpf(9))))

# 9. Curved boundary: from a point at radius r0 = 1/2 inside the unit ball in R^3, the uniform straight-line landing and
#    harmonic measure part. Share landing in the polar cap within angle alpha of the point's direction.
r0, alpha = mpf('0.5'), pi / 4
def harmonic_cap():
    # Poisson kernel of the unit ball in R^3: (1 - r0^2) / (4 pi |x - y|^3)
    return quad(lambda t: (1 - r0 ** 2) / (4 * pi) / (1 + r0 ** 2 - 2 * r0 * cos(t)) ** mpf(1.5) * 2 * pi * sin(t), [0, alpha])
def straight_cap():
    # a ray from y at polar angle u (from the axis) meets the sphere at angle t with cos t = r0 sin^2 u + cos u sqrt(1 - r0^2 sin^2 u)
    def t_of(u):
        return mp.acos(r0 * sin(u) ** 2 + cos(u) * sqrt(1 - r0 ** 2 * sin(u) ** 2))
    # t increases with u; find u* with t(u*) = alpha, then the share of directions within u* is (1 - cos u*)/2
    ustar = mp.findroot(lambda u: t_of(u) - alpha, alpha)
    return (1 - cos(ustar)) / 2
hc, sc = harmonic_cap(), straight_cap()
print(f'{"9 curved boundary (ball, r0 = 1/2, cap 45 deg): harmonic":58s} {mp.nstr(hc, 8)}   straight turn {mp.nstr(sc, 8)}'
      f'   they part by {mp.nstr(fabs(hc - sc), 3)}')
out['curved_gap'] = fabs(hc - sc)

# 10. The 2Dt as a Gaussian scale mixture: p/(pi u) (1 + r^2/u)^-(p+1) = int N2(0, s I) InvGamma(s; p, u/2) ds.
#     At p = 1/2 the mixing is the Levy hitting time of height sqrt(u): the hemisphere landing (route 8, n = 3).
def t2d(r, pp, u):
    return pp / (pi * u) * (1 + r ** 2 / u) ** (-(pp + 1))
def mix2d(r, pp, u):
    beta = u / 2
    ig = lambda s: beta ** pp / G(pp) * s ** (-pp - 1) * exp(-beta / s)
    return quad(lambda s: exp(-r ** 2 / (2 * s)) / (2 * pi * s) * ig(s), [0, 1, 10, inf])
worst = 0
for pp in (mpf('0.1'), mpf('0.5'), mpf(2)):
    for r in (mpf('0.2'), mpf(1), mpf(5)):
        worst = max(worst, fabs(mix2d(r, pp, mpf('1.69')) - t2d(r, pp, mpf('1.69'))))
out['mix'] = report('10 2Dt(p) = Gaussian mixed over InvGamma(p): p = 0.1, 0.5, 2', worst)
lev = max(fabs(mix2d(r, mpf('0.5'), g ** 2) - g / (2 * pi * (r ** 2 + g ** 2) ** mpf(1.5))) for r in (mpf('0.2'), mpf(1), mpf(5)))
out['mix_half'] = report('10b at p = 1/2, u = g^2: the 3D hemisphere/hitting law', lev)

print()
bad = [k for k, v in out.items() if k != 'curved_gap' and v > mpf('1e-20')]
print('all routes land on the Poisson kernel to 1e-20' if not bad else f'NOT within 1e-20: {bad}')
print('the curved boundary parts the turn from harmonic measure' if out['curved_gap'] > mpf('1e-3') else 'curved: no gap found')
