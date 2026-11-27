"""CDW run 3: a chain of reads, a telescope and a pixel layer (SPN R1271; plans/cdw-plan.md, run 3).
Run from the repository's root: python3 runs/cdw/cdw3.py
Each layer is a wrapped Cauchy applied by the trapezoid sum on its period (the direct quadrature; the FFT only
evaluates that same circular sum quickly). The pixel layer and the eye over the pixels are summed directly."""
import numpy as np

LS = 16                                       # the sky's period, writes at the whole numbers
rng = np.random.default_rng(1271)
amps = 0.5 + rng.random(LS)

def K(t, h, L):                               # the wrapped Cauchy of height h on period L, total 1
    a = 2 * np.pi * h / L
    return np.sinh(a) / (L * (np.cosh(a) - np.cos(2 * np.pi * t / L)))

def sky(x, h, a):                             # writes with amplitudes a, read from height h, on the sky
    return sum(a[n] * K(x - n, h, LS) for n in range(LS))

def chain(h1, M, h2, h3, a, per=512):
    L = LS * M; N = LS * M * per; y = np.arange(N) * L / N; dy = L / N
    J = sky(y / M, h1, a) / M                 # the objective's image, magnified
    for h in (h2, h3):
        if h > 0:
            k = K(y, h, L) * dy
            J = np.real(np.fft.ifft(np.fft.fft(J) * np.fft.fft(k)))
    return y, J

out = []
def say(s): print(s); out.append(s)

# T1
worst = 0
for M in (1, 2, 10):
    h1, h2, h3 = 0.3, 0.3, 0.3
    y, J = chain(h1, M, h2, h3, amps)
    u = h1 + (h2 + h3) / M
    pred = sky(y / M, u, amps) / M
    e = np.max(np.abs(J - pred)) / np.max(pred); worst = max(worst, e)
    say(f"T1 M = {M:>2}: one read at u = {u:.3f}, worst gap {e:.2e} of the peak")
imgs = [chain(*hs, amps)[1] for hs in [(0.1, 1, 0.2, 0.3), (0.3, 1, 0.2, 0.1), (0.6, 1, 0, 0)]]
e_order = max(np.max(np.abs(i - imgs[0])) for i in imgs) / np.max(imgs[0])
say(f"T1 M = 1, splits (0.1,0.2,0.3), (0.3,0.2,0.1), (0.6,0,0): worst gap {e_order:.2e}")
T1 = worst < 1e-10 and e_order < 1e-10

# T2
ones = np.ones(LS); rip = {}; worst2 = 0
for M in (1, 2, 10):
    y, J = chain(0.3, M, 0.3, 0.3, ones)
    d = M * J; u = 0.3 + 0.6 / M
    r = d.max() - d.min(); p = 2 / np.sinh(2 * np.pi * u); rip[M] = r
    worst2 = max(worst2, abs(r - p) / p)
    say(f"T2 M = {M:>2}: u = {u:.3f}, ripple {r:.6e} against 2/sinh(2 pi u) = {p:.6e}")
say(f"T2 ripple at M = 10 over M = 1: {rip[10] / rip[1]:.1f}; worst relative gap {worst2:.2e}")
T2 = worst2 < 1e-9 and rip[10] / rip[1] > 20

# T3
M, p, h1, h3 = 8, 1.0, 0.3, 0.5
L = LS * M; npix = int(L / p); gx, gw = np.polynomial.legendre.leggauss(40)
def pixels(Jfun):
    v = np.empty(npix)
    for j in range(npix):
        yy = j * p + (gx + 1) * p / 2
        v[j] = np.sum(gw * Jfun(yy)) * p / 2
    return v
G = 64; N = npix * G; y = np.arange(N) * L / N
def eye(v):
    c = (np.arange(npix) + 0.5) * p
    return sum(v[j] * K(y - c[j], h3, L) for j in range(npix))
Fu = eye(pixels(lambda yy: np.full_like(yy, 1 / M)))
ra = (Fu.max() - Fu.min()) / Fu.mean(); pa = 2 / np.sinh(2 * np.pi * h3 / p)
say(f"T3a uniform sky: ripple at the pixel spacing {ra:.9e} of the mean, 2/sinh(2 pi h3/p) = {pa:.9e}")
Fs = eye(pixels(lambda yy: sky(yy / M, h1, ones) / M))
c = np.fft.fft(Fs) / N
kst = int(L / M); kpx = int(L / p)
star = 2 * abs(c[kst]) / abs(c[0])
pst = 2 * np.exp(-2 * np.pi * h1) * (np.sin(np.pi * p / M) / (np.pi * p / M)) * np.exp(-2 * np.pi * h3 / M)
pix = 2 * abs(c[kpx]) / abs(c[0]); ppx = 2 * np.exp(-2 * np.pi * h3 / p)
say(f"T3b the stars' frequency: {star:.9e} against {pst:.9e}, relative gap {abs(star - pst) / pst:.2e}")
say(f"T3c the pixel frequency: {pix:.6e} against 2e^(-2 pi h3/p) = {ppx:.6e}, relative gap {abs(pix - ppx) / ppx:.2e}")
T3 = abs(ra - pa) / pa < 1e-9 and abs(star - pst) / pst < 1e-5 and abs(pix - ppx) / ppx < 1e-2
say(f"verdicts: T1 {'not killed' if T1 else 'KILLED'}, T2 {'not killed' if T2 else 'KILLED'}, T3 {'not killed' if T3 else 'KILLED'}")
open('runs/cdw/cdw3-out.txt', 'w').write('\n'.join(out) + '\n')
