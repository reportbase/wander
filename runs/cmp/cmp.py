"""CMP run 1: the conformal map, CIW beyond the circle (plans/cmp-plan.md).

Run from the repository's root: python3 runs/cmp/cmp.py

C1  walk-on-spheres from w = F(z) lands, pulled back through F, as the wrapped Cauchy P_z (KS, N = 1e5, nine cases)
C2  2 dtheta_w/dphi - 1 = 2 pi P_z(phi): Moebius to 1e-30, polynomial off by > 1e-3 (expected killed: see the plan)
C2' 2 dtheta_w/dphi - dpsi/dphi = 2 pi P_z(phi), psi the image circle's own central angle: (a) Moebius to 1e-30,
    (b) polynomial with psi = arg F off by > 1e-3
C3  F = z + a z^3, z = 0.3: max residual / a the same within 2% at a = 1e-2, 1e-3, 1e-4
C4  Theodorsen's iteration from the true radii recovers arg F(e^{i phi}) to 1e-10 within 60 iterations
C5  rho -> k rho moves the recovered theta by < 1e-12
"""
import numpy as np
import mpmath as mp
from scipy.spatial import cKDTree
from scipy.stats import kstest

mp.mp.dps = 50
rng = np.random.default_rng(20261019)


# ---- the maps ------------------------------------------------------------------------------------------------
def moebius(b):
    F = lambda z: z / (1 - b * z)
    F1 = lambda z: 1 / (1 - b * z) ** 2
    F2 = lambda z: 2 * b / (1 - b * z) ** 3
    c = b / (1 - b * b)                      # the image circle's centre (radius 1/(1 - b^2))
    return dict(name=f"z/(1 - {b}z)", F=F, F1=F1, F2=F2, centre=c, b=b, kind="moebius")


def poly(a, n):
    F = lambda z: z + a * z ** n
    F1 = lambda z: 1 + n * a * z ** (n - 1)
    F2 = lambda z: n * (n - 1) * a * z ** (n - 2)
    return dict(name=f"z + {a}z^{n}", F=F, F1=F1, F2=F2, centre=0, a=a, n=n, kind="poly")


def wrapped_cdf(phi, z):
    """CDF of the Poisson kernel P_z, measured from arg z - pi."""
    r, al = abs(z), np.angle(z)
    t = np.mod(phi - al + np.pi, 2 * np.pi) - np.pi
    if r == 0:
        return (t + np.pi) / (2 * np.pi)
    return 0.5 + np.arctan((1 + r) / (1 - r) * np.tan(t / 2)) / np.pi


# ---- C1: walk-on-spheres -------------------------------------------------------------------------------------
def wos(m, z, N, eps=1e-6, M=1 << 16):
    F, F1, F2 = m["F"], m["F1"], m["F2"]
    ph = 2 * np.pi * np.arange(M) / M
    bd = F(np.exp(1j * ph))
    tree = cKDTree(np.c_[bd.real, bd.imag])
    w = np.full(N, complex(F(z)))
    out = np.full(N, np.nan)
    act = np.arange(N)
    steps = 0
    while act.size:
        steps += 1
        x = w[act]
        _, j = tree.query(np.c_[x.real, x.imag])
        p = ph[j]
        for _ in range(4):                    # Newton on d/dphi |F(e^{i phi}) - x|^2 = 0
            s = np.exp(1j * p)
            e = F(s) - x
            T = 1j * s * F1(s)
            dT = -s * s * F2(s) - s * F1(s)
            g = np.real(np.conj(e) * T)
            h = np.abs(T) ** 2 + np.real(np.conj(e) * dT)
            p = p - g / h
        d = np.abs(F(np.exp(1j * p)) - x)
        done = d < eps
        out[act[done]] = np.mod(p[done], 2 * np.pi)
        keep = ~done
        act, x, d = act[keep], x[keep], d[keep]
        w[act] = x + d * np.exp(2j * np.pi * rng.random(act.size))
        if steps > 10000:
            raise RuntimeError("walk did not finish")
    return out, steps


print("C1: walk-on-spheres, N = 1e5, KS threshold 1.63/sqrt(N) =", round(1.63 / np.sqrt(1e5), 5))
N1 = 100_000
c1_ok = True
for m in (moebius(0.4), poly(0.3, 2), poly(0.2, 3)):
    for z in (0.0, 0.4, 0.6 * np.exp(1j)):
        phis, steps = wos(m, z, N1)
        D = kstest(wrapped_cdf(phis, z), "uniform").statistic
        ok = D < 1.63 / np.sqrt(N1)
        c1_ok &= ok
        print(f"  {m['name']:14s} z = {complex(z):.3f}  steps {steps:4d}  KS {D:.5f}  {'ok' if ok else 'FAIL'}")
print("C1", "not killed" if c1_ok else "KILLED")


# ---- C2, C2': the straight-ray combination, at 50 digits ---------------------------------------------------
def mpmap(m):
    if m["kind"] == "moebius":
        b = mp.mpf(m["b"])
        return (lambda z: z / (1 - b * z)), (lambda z: 1 / (1 - b * z) ** 2), b / (1 - b * b)
    a, n = mp.mpf(m["a"]), m["n"]
    return (lambda z: z + a * z ** n), (lambda z: 1 + n * a * z ** (n - 1)), mp.mpf(0)


def residuals(m, z, phi):
    F, F1, c = mpmap(m)
    s = mp.expj(phi)
    w = F(z)
    thw = mp.re(s * F1(s) / (F(s) - w))      # d/dphi arg(F(e^{i phi}) - w)
    psi = mp.re(s * F1(s) / (F(s) - c))      # d/dphi arg(F(e^{i phi}) - c)
    P2 = (1 - abs(z) ** 2) / abs(s - z) ** 2   # 2 pi P_z(phi)
    return abs(2 * thw - 1 - P2), abs(2 * thw - psi - P2)


samples = []
for _ in range(1000):
    r = 0.9 * np.sqrt(rng.random())
    samples.append((mp.mpf(r) * mp.expj(mp.mpf(2 * np.pi * rng.random())), mp.mpf(2 * np.pi * rng.random())))

print("\nC2 and C2': max over 1,000 seeded (z, phi), |z| < 0.9, 50 digits")
c2_ok, c2p_ok = True, True
for m in (moebius(0.2), moebius(0.4), poly(0.05, 2), poly(0.1, 2), poly(0.05, 3), poly(0.1, 3),
          poly(0.05, 5), poly(0.1, 5)):
    r1 = r2 = mp.mpf(0)
    for z, phi in samples:
        a, b = residuals(m, z, phi)
        r1, r2 = max(r1, a), max(r2, b)
    if m["kind"] == "moebius":
        c2_ok &= r1 < mp.mpf("1e-30")
        c2p_ok &= r2 < mp.mpf("1e-30")
    else:
        c2_ok &= r1 > mp.mpf("1e-3")
        c2p_ok &= r2 > mp.mpf("1e-3")
    print(f"  {m['name']:14s}  C2 {mp.nstr(r1, 4):>10s}   C2' {mp.nstr(r2, 4):>10s}")
print("C2", "not killed" if c2_ok else "KILLED", "  C2'", "not killed" if c2p_ok else "KILLED")


# ---- C3: first order in the departure ------------------------------------------------------------------------
print("\nC3: F = z + a z^3, z = 0.3, max over phi of the C2 residual, over a")
z3 = mp.mpf("0.3")
vals = []
for a in ("1e-2", "1e-3", "1e-4"):
    A = mp.mpf(a)
    F, F1 = (lambda q: q + A * q ** 3), (lambda q: 1 + 3 * A * q ** 2)
    def sr(p):                               # the C2 residual, signed
        s = mp.expj(p)
        return 2 * mp.re(s * F1(s) / (F(s) - F(z3))) - 1 - (1 - z3 ** 2) / abs(s - z3) ** 2
    grid = [2 * mp.pi * k / 4096 for k in range(4096)]
    p0 = max(grid, key=lambda p: abs(sr(p)))
    best = mp.findroot(lambda p: mp.diff(sr, p), p0)
    mx = max(abs(sr(best)), abs(sr(p0)))
    vals.append(mx / A)
    print(f"  a = {a:5s}  max {mp.nstr(mx, 8)}  max/a {mp.nstr(mx / A, 8)}  at phi {mp.nstr(best, 6)}")
spread = max(vals) / min(vals) - 1
c3_ok = spread < 0.02
print(f"C3 spread {mp.nstr(spread, 4)}", "not killed" if c3_ok else "KILLED")


# ---- C4, C5: Theodorsen --------------------------------------------------------------------------------------
def theta_true(phi, a, n):
    return phi + np.angle(1 + a * np.exp(1j * (n - 1) * phi))


def rho_of_theta(th, a, n):
    """The true radius of the shape along the geometric direction th (Newton on theta_true(phi) = th)."""
    p = th.copy()
    for _ in range(40):
        s = np.exp(1j * p)
        F = s + a * s ** n
        d = np.real(s * (1 + n * a * s ** (n - 1)) / F)
        p = p - (theta_true(p, a, n) - th) / d
    return np.abs(np.exp(1j * p) + a * np.exp(1j * n * p))


def conj(u):
    c = np.fft.fft(u)
    m = np.fft.fftfreq(u.size, 1 / u.size)
    c = -1j * np.sign(m) * c
    c[u.size // 2] = 0
    return np.real(np.fft.ifft(c))


def theodorsen(a, n, k=1.0, N=1024, iters=60):
    phi = 2 * np.pi * np.arange(N) / N
    th = phi.copy()
    hist = []
    for it in range(iters):
        th = phi + conj(np.log(k * rho_of_theta(th, a, n)))
        hist.append(np.max(np.abs(th - theta_true(phi, a, n))))
    return th, hist


print("\nC4: Theodorsen, N = 1,024, 60 iterations, max |theta - arg F(e^{i phi})|")
c4_ok, c5_ok = True, True
for n in (2, 3, 5):
    for a in (0.02, 0.1):
        th, hist = theodorsen(a, n)
        first = next((i + 1 for i, e in enumerate(hist) if e < 1e-10), None)
        ok = first is not None
        c4_ok &= ok
        moves = []
        for k in (1e-3, 7.0, 1e3):
            thk, _ = theodorsen(a, n, k)
            moves.append(np.max(np.abs(thk - th)))
        c5_ok &= max(moves) < 1e-12
        print(f"  n = {n} a = {a:4}  error {hist[-1]:.2e}  below 1e-10 at iteration {first}  "
              f"C5 moves {', '.join(f'{x:.1e}' for x in moves)}")
print("C4", "not killed" if c4_ok else "KILLED", "  C5", "not killed" if c5_ok else "KILLED")

print("\nC6", "not killed" if (c1_ok and c2p_ok and c4_ok) else "KILLED",
      "(C2' for C2, by the note written before the run)")
