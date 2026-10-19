"""CIW run 1: the head's turn on an object combined with the central sweep (plans/ciw-plan.md). Exact (mpmath) and seeded."""
import numpy as np, mpmath as mp
from scipy.optimize import least_squares
mp.mp.dps = 50
rng = np.random.default_rng(20261019 + 84)
ok = {}

def P(z, phi):  # the Poisson kernel on the unit circle, from z inside or outside
    zeta = mp.expj(phi)
    return abs(1 - abs(z)**2) / abs(zeta - z)**2 / (2 * mp.pi)
def theta(z, phi): return mp.arg(mp.expj(phi) - z)
def dtheta(z, phi):  # closed form; K1 checks it against numerical differentiation too
    zeta = mp.expj(phi)
    return (1 - mp.re(mp.conj(z) * zeta)) / abs(zeta - z)**2

# ---------------- K1
worst = mp.mpf(0); worst_d = mp.mpf(0)
for i in range(10**4):
    r = rng.uniform(0, 0.99) if i % 2 == 0 else rng.uniform(1.01, 20)
    z = mp.mpf(r) * mp.expj(mp.mpf(rng.uniform(0, 2 * np.pi)))
    phi = mp.mpf(rng.uniform(0, 2 * np.pi))
    num = mp.diff(lambda p: theta(z, p), phi)
    worst_d = max(worst_d, abs(num - dtheta(z, phi)))
    comb = (2 * num - 1) if abs(z) < 1 else (1 - 2 * num)
    worst = max(worst, abs(2 * mp.pi * P(z, phi) - comb))
worst_arc = mp.mpf(0)
for i in range(10**3):
    z = mp.mpf(rng.uniform(0, 0.99)) * mp.expj(mp.mpf(rng.uniform(0, 2 * np.pi)))
    p1 = mp.mpf(rng.uniform(0, 2 * np.pi)); a = mp.mpf(rng.uniform(0.01, 2 * np.pi - 0.01)); p2 = p1 + a
    om = mp.quad(lambda p: P(z, p), [p1, p2])
    tz = mp.arg((mp.expj(p2) - z) / (mp.expj(p1) - z)) % (2 * mp.pi)  # from inside theta rises by 2pi round the circle
    worst_arc = max(worst_arc, abs(om - (tz / mp.pi - a / (2 * mp.pi))))
ok['K1'] = worst < mp.mpf('1e-40') and worst_arc < mp.mpf('1e-30')
print('K1 2pi P = +/-(2 dtheta/dphi - 1) to %s (closed form of dtheta to %s); arcs omega = theta_z/pi - alpha/2pi to %s'
      % (mp.nstr(worst, 3), mp.nstr(worst_d, 3), mp.nstr(worst_arc, 3)), ok['K1'])

# ---------------- K2
def land_inside(z, th):  # a uniform head turn from z inside the unit circle: where each ray meets it
    u = np.exp(1j * th)
    b = np.real(np.conj(z) * u)
    t = -b + np.sqrt(b * b + 1 - abs(z)**2)
    return z + t * u
N = 10**6; worst = 0
for r in (0.1, 0.5, 0.9):
    z = r * np.exp(0.7j)
    zeta = land_inside(z, rng.uniform(0, 2 * np.pi, N))
    c = 2 * zeta.mean()
    se = 2 * np.array([zeta.real.std(), zeta.imag.std()]) / np.sqrt(N)
    zc = (np.array([c.real, c.imag]) - np.array([z.real, z.imag])) / se
    th1 = (1 - np.real(np.conj(z) * zeta)) / np.abs(zeta - z)**2      # dtheta/dphi at each landing
    w = (2 * th1 - 1) / th1                                            # 2pi P over the landing density (1/2pi) dtheta/dphi
    wz = w * zeta
    m = wz.mean(); sew = np.array([wz.real.std(), wz.imag.std()]) / np.sqrt(N)
    zw = (np.array([m.real, m.imag]) - np.array([z.real, z.imag])) / sew
    worst = max(worst, np.max(np.abs(zc)), np.max(np.abs(zw)))
    print('   |z|=%.1f: 2 x centroid %.5f%+.5fi (z %.5f%+.5fi, z-scores %+.2f %+.2f); weighted by the kernel %.5f%+.5fi (%+.2f %+.2f)'
          % (r, c.real, c.imag, z.real, z.imag, zc[0], zc[1], m.real, m.imag, zw[0], zw[1]))
ok['K2'] = worst < 3
print('K2', ok['K2'])

# ---------------- K3
worst = mp.mpf(0); shares = {}
for r in (mp.mpf('1.5'), mp.mpf(2), mp.mpf(4), mp.mpf(100)):
    z = r * mp.expj(mp.mpf('0.7'))
    f = lambda p: mp.expj(p) * dtheta(z, p)
    half = mp.acos(1 / r); a0 = mp.arg(z)
    near = mp.quad(f, [a0 - half, a0, a0 + half])
    far = mp.quad(f, [a0 + half, a0 + mp.pi, a0 + 2 * mp.pi - half])
    full = -(near + far) / mp.pi
    worst = max(worst, abs(full - 1 / mp.conj(z)))
    sh = -near / mp.pi / full
    shares[float(r)] = sh
    print('   |z|=%s: -(1/pi) closed integral %s, 1/conj(z) %s; the near crossings\' share %s'
          % (mp.nstr(r, 4), mp.nstr(full, 12), mp.nstr(1 / mp.conj(z), 12), mp.nstr(sh, 8)))
s100 = shares[100.0]; s15 = shares[1.5]
ok['K3'] = worst < mp.mpf('1e-30') and abs(mp.re(s100) - 0.5) < 0.005 and abs(mp.im(s100)) < 1e-20 and abs(s15 - 0.5) > 0.005
print('K3 closed integral = 1/conj(z) to %s; near share at 100 %s, at 1.5 %s' % (mp.nstr(worst, 3), mp.nstr(s100, 8), mp.nstr(s15, 8)), ok['K3'])

# ---------------- K4
z = 0.5 * np.exp(0.7j); n = 10**4
th = rng.uniform(0, 2 * np.pi, n)
phi0 = np.angle(land_inside(z, th))
worst_k = 0
for k in (1e-3, 7.0, 1e3):
    u = np.exp(1j * th); zk = k * z
    b = np.real(np.conj(zk) * u); t = -b + np.sqrt(b * b + k * k - abs(zk)**2)
    phik = np.angle(zk + t * u)
    worst_k = max(worst_k, np.max(np.abs(np.angle(np.exp(1j * (phik - phi0))))))
est = []
for rep in range(200):
    zeta = land_inside(z, rng.uniform(0, 2 * np.pi, n))
    est.append(2 * zeta.mean())
est = np.array(est); se = np.array([est.real.std(), est.imag.std()]) / np.sqrt(len(est))
zs = (np.array([est.mean().real, est.mean().imag]) - np.array([z.real, z.imag])) / se
ok['K4'] = worst_k < 1e-12 and np.max(np.abs(zs)) < 3
print('K4 scaling moves no landing by more than %.1e rad; mean of z-hat %.5f%+.5fi over 200 (z-scores %+.2f %+.2f), each to %.4f'
      % (worst_k, est.mean().real, est.mean().imag, zs[0], zs[1], est.real.std()), ok['K4'])

# ---------------- K5: an ellipse, semi-axes 2 and 1, the standpoint at 0.8 on the major axis
M = 4096; ph = (np.arange(M) + 0.5) * 2 * np.pi / M
rr = 1 / np.sqrt(np.cos(ph)**2 / 4 + np.sin(ph)**2)
pt = rr * np.exp(1j * ph); z = 0.8
th = np.unwrap(np.angle(pt - z))
dth = np.gradient(th, ph, edge_order=2)
# the derivative across the seam, from the periodic neighbours
dth[0] = np.angle(np.exp(1j * (th[1] - th[-1]))) / (2 * (2 * np.pi / M))
dth[-1] = np.angle(np.exp(1j * (th[0] - th[-2]))) / (2 * (2 * np.pi / M))
g = (2 * dth - 1) / (2 * np.pi)
def wc(p, rho, mu): return (1 - rho**2) / (1 - 2 * rho * np.cos(p - mu) + rho**2) / (2 * np.pi)
fit = least_squares(lambda q: wc(ph, q[0], q[1]) - g, [0.3, 0.0], bounds=([0, -np.pi], [0.999, np.pi]))
res = np.sum(np.abs(wc(ph, *fit.x) - g)) / np.sum(np.abs(g))
ok['K5'] = res > 0.01
print('K5 ellipse: combined density integrates to %.6f, its least %.4f; best wrapped Cauchy rho %.4f mu %.4f, relative L1 residual %.4f'
      % (g.sum() * 2 * np.pi / M, g.min(), fit.x[0], fit.x[1], res), ok['K5'])

ok['K6'] = ok['K1'] and ok['K2'] and ok['K4']
print('K6', ok['K6'], ok)
