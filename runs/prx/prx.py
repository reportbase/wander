# PRX run 1: which sources pair near with far. Predictions in plans/prx-plan.md.
# E(d)/(pi L) = (1/2pi) * integral of rho^2/(d^2 + rho^2) dphi (foot inside), or of f(rho2) - f(rho1) (a ring).
import mpmath as mp
import numpy as np
from scipy import integrate, optimize

mp.mp.dps = 40
DS = [mp.mpf(10) ** (mp.mpf(k) / 10 - 2) for k in range(41)]  # 1e-2 .. 1e2, even in ln d
out = []


def rep(code, ok, msg):
    line = f"{code}: {'not killed' if ok else 'KILLED'}  {msg}"
    print(line)
    out.append(line)


# ---------- shapes as radial functions (foot inside) ----------
def star(lnrho, splits=None):
    """E(d)/(pi L) for a source bounded by rho(phi) = exp(lnrho(phi))."""
    pts = splits or [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi]

    def E(d):
        f = lambda p: 1 / (1 + (d / mp.e ** lnrho(p)) ** 2)
        return mp.quad(f, pts) / (2 * mp.pi)
    return E


def ring(rho12, tmax):
    """E(d)/(pi L) for a source between rho1(t) and rho2(t), param t in [-tmax, tmax] with dphi/dt given."""
    def E(d):
        def g(t):
            r1, r2, jac = rho12(t)
            f = lambda u: u ** 2 / (d ** 2 + u ** 2)
            return (f(r2) - f(r1)) * jac
        return mp.quad(g, [-tmax, 0, tmax]) / (2 * mp.pi)
    return E


def dev_pair(E, c):
    return max(abs(E(d) + E(c ** 2 / d) - 1) for d in DS)


def dev_mirror(E, c):
    return max(abs(E(d) - E(c ** 2 / d)) for d in DS)


def gm(lnrho):
    return mp.e ** (mp.quad(lnrho, [0, mp.pi, 2 * mp.pi]) / (2 * mp.pi))


# ---------- double-precision versions for the scans over c ----------
def star_np(lnrho_np, n=4000):
    ph = (np.arange(n) + 0.5) * 2 * np.pi / n  # midpoint rule, spectral for smooth periodic integrands
    rho = np.exp(lnrho_np(ph))

    def E(d):
        return np.mean(1 / (1 + (d / rho) ** 2))
    return E, np.exp(np.mean(np.log(rho)))


def best_c(E, c0):
    dsn = np.array([float(x) for x in DS])
    def dev(lnc):
        c = np.exp(lnc)
        return max(abs(E(d) + E(c * c / d) - 1) for d in dsn)
    grid = np.linspace(np.log(c0) - 1.5, np.log(c0) + 1.5, 61)
    vals = [dev(g) for g in grid]
    i = int(np.argmin(vals))
    r = optimize.minimize_scalar(dev, bracket=(grid[max(i - 1, 0)], grid[i], grid[min(i + 1, 60)]),
                                 method='brent', tol=1e-10)
    return float(np.exp(r.x)), float(r.fun)


c = mp.mpf(3) / 2  # the corner for the family tests

# ---------- P1 ----------
res = []
for n in (1, 2, 3, 5):
    E = star(lambda p, n=n: mp.log(c) + mp.mpf(1) / 2 * mp.cos(n * p))
    dv = dev_pair(E, c)
    half = E(c)
    res.append((n, dv, half))
rep('P1', all(r[1] < 1e-25 for r in res),
    "ln rho = ln c + cos(n phi)/2: " + "; ".join(f"n={n} dev {mp.nstr(dv, 3)}, E(c) {mp.nstr(h, 12)}" for n, dv, h in res))

# ---------- P2 ----------
E = star(lambda p: mp.log(c) + mp.mpf('0.4') * mp.cos(p) + mp.mpf('0.3') * mp.cos(3 * p) + mp.mpf('0.2') * mp.sin(5 * p))
dv = dev_pair(E, c)
rep('P2', dv < 1e-25, f"odd modes 1, 3, 5: dev {mp.nstr(dv, 3)}, E(c) {mp.nstr(E(c), 12)}")

# ---------- P3 ----------
p3 = []
for name, f in (("0.5cos phi + 0.25cos 2phi", lambda p: 0.5 * np.cos(p) + 0.25 * np.cos(2 * p)),
                ("0.4cos 2phi + 0.3cos 4phi", lambda p: 0.4 * np.cos(2 * p) + 0.3 * np.cos(4 * p))):
    En, g = star_np(lambda p, f=f: np.log(1.5) + f(p))
    cb, dvb = best_c(En, g)
    third = np.mean((f((np.arange(4000) + 0.5) * 2 * np.pi / 4000)) ** 3)
    p3.append((name, cb, dvb, g, third))
rep('P3', all(r[2] > 1e-3 for r in p3),
    "; ".join(f"{n}: best c {cb:.5f} (gm {g:.5f}), least dev {dvb:.3e}, third moment {t:.4f}" for n, cb, dvb, g, t in p3))

# ---------- P4: disc off axis, foot inside ----------
a = mp.mpf(1)
p4 = []
for bb in ('0.3', '0.7', '0.95'):
    b = mp.mpf(bb)
    E = star(lambda p, b=b: mp.log(b * mp.cos(p) + mp.sqrt(a ** 2 - b ** 2 * mp.sin(p) ** 2)))
    c0 = mp.sqrt(a ** 2 - b ** 2)
    dv = dev_pair(E, c0)
    dvoff = dev_pair(E, c0 * (1 + mp.mpf(10) ** -20))
    g = gm(lambda p, b=b: mp.log(b * mp.cos(p) + mp.sqrt(a ** 2 - b ** 2 * mp.sin(p) ** 2)))
    # independent check: area integral in double precision, polar about the disc's centre
    bf = float(b)
    def Earea(d):
        f = lambda r, t: (d * d / (d * d + (r * np.cos(t) + bf) ** 2 + (r * np.sin(t)) ** 2) ** 2) * r / np.pi
        return integrate.dblquad(f, 0, 2 * np.pi, 0, 1, epsabs=1e-13, epsrel=1e-12)[0]
    chk = max(abs(Earea(dd) - float(E(mp.mpf(dd)))) for dd in (0.1, 0.5, 2.0))
    p4.append((bb, dv, dvoff, E(c0), abs(g - c0), chk))
rep('P4', all(r[1] < 1e-25 and r[2] > 1e-22 for r in p4),
    "; ".join(f"b={bb}: dev at sqrt(a^2-b^2) {mp.nstr(dv, 3)}, at c(1+1e-20) {mp.nstr(dvo, 3)}, E(c) {mp.nstr(h, 12)}, "
              f"|gm - c| {mp.nstr(gg, 3)}, area check {ck:.1e}" for bb, dv, dvo, h, gg, ck in p4))

# ---------- P5: disc with the foot outside ----------
p5 = []
for bb in ('1.5', '3'):
    b = mp.mpf(bb)
    k = a / b

    def r12(t, b=b, k=k):
        sp = k * mp.sin(t)              # sin phi
        cp = mp.sqrt(1 - sp ** 2)
        root = a * mp.cos(t)            # sqrt(a^2 - b^2 sin^2 phi)
        jac = k * mp.cos(t) / cp        # dphi/dt
        return b * cp - root, b * cp + root, jac
    E = ring(r12, mp.pi / 2)
    c0 = mp.sqrt(b ** 2 - a ** 2)
    dv = dev_mirror(E, c0)
    dmax = mp.findroot(lambda x: mp.diff(E, x), c0 * mp.mpf('1.05'))
    bf = float(b)
    def Earea(d):
        f = lambda r, t: (d * d / (d * d + (r * np.cos(t) + bf) ** 2 + (r * np.sin(t)) ** 2) ** 2) * r / np.pi
        return integrate.dblquad(f, 0, 2 * np.pi, 0, 1, epsabs=1e-13, epsrel=1e-12)[0]
    chk = max(abs(Earea(dd) - float(E(mp.mpf(dd)))) for dd in (0.3, 1.0, 4.0))
    p5.append((bb, dv, dmax, c0, E(c0), chk))
rep('P5', all(r[1] < 1e-25 and abs(r[2] / r[3] - 1) < 1e-10 for r in p5),
    "; ".join(f"b={bb}: mirror dev {mp.nstr(dv, 3)}, max at {mp.nstr(dm, 15)} vs sqrt(b^2-a^2) {mp.nstr(c0, 15)}, "
              f"E there {mp.nstr(e, 10)}, area check {ck:.1e}" for bb, dv, dm, c0, e, ck in p5))

# ---------- P6: annulus ----------
p6 = []
for r1, r2 in ((1, 4), (1, 10)):
    r1, r2 = mp.mpf(r1), mp.mpf(r2)
    E = lambda d, r1=r1, r2=r2: r2 ** 2 / (d ** 2 + r2 ** 2) - r1 ** 2 / (d ** 2 + r1 ** 2)
    c0 = mp.sqrt(r1 * r2)
    dv = dev_mirror(E, c0)
    dmax = mp.findroot(lambda x: mp.diff(E, x), c0 * mp.mpf('1.05'))
    Earea = lambda d, r1=float(r1), r2=float(r2): integrate.quad(lambda r: 2 * d * d * r / (d * d + r * r) ** 2, r1, r2,
                                                                epsabs=1e-14)[0]
    chk = max(abs(Earea(dd) - float(E(mp.mpf(dd)))) for dd in (0.5, 2.0, 8.0))
    p6.append((r2, dv, dmax, c0, E(c0), chk))
rep('P6', all(r[1] < 1e-25 and abs(r[2] / r[3] - 1) < 1e-10 for r in p6),
    "; ".join(f"1 to {mp.nstr(r2, 3)}: mirror dev {mp.nstr(dv, 3)}, max at {mp.nstr(dm, 15)} vs sqrt(r1 r2) {mp.nstr(c0, 15)}, "
              f"E there {mp.nstr(e, 10)}, area check {ck:.1e}" for r2, dv, dm, c0, e, ck in p6))

# ---------- P7: ellipse ----------
En, g = star_np(lambda p: np.log(2.0) - 0.5 * np.log(4 * np.cos(p) ** 2 + np.sin(p) ** 2))
cb, dvb = best_c(En, g)
rep('P7', dvb > 1e-3, f"semi-axes 1, 2: best c {cb:.5f} (gm {g:.5f}, sqrt(ab) {np.sqrt(2):.5f}), least dev {dvb:.3e}")

# ---------- P8: regular polygons ----------
p8 = []
for n in (3, 4, 6, 8):
    w = 2 * np.pi / n
    En, g = star_np(lambda p, w=w: -np.log(np.cos(np.mod(p, w) - w / 2)), n=n * 4000)
    cb, dvb = best_c(En, g)
    p8.append((n, cb, dvb, g))
# the square with c = half-side (inradius 1): ISX's sums at d = 10 and d = 1
Esq, _ = star_np(lambda p: -np.log(np.cos(np.mod(p, np.pi / 2) - np.pi / 4)), n=16000)
far = Esq(10.0) + Esq(0.1)
corner = 2 * Esq(1.0)
decr = all(p8[i][2] > p8[i + 1][2] for i in range(3))
rep('P8', all(r[2] > 1e-3 for r in p8) and decr and abs(far - 1.0045) < 5e-4 and abs(corner - 1.1083) < 5e-4,
    "; ".join(f"n={n}: best c {cb:.5f} (gm {g:.5f}), least dev {dvb:.3e}" for n, cb, dvb, g in p8)
    + f"; square at half-side: E(10)+E(1/10) {far:.5f}, 2E(1) {corner:.5f} (x pi L)")

open('runs/prx/prx-run1.txt', 'w').write("\n".join(out) + "\n")
