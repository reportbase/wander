"""EPI run 1: epicycles (Fourier circles) against aimed Cauchy terms (Takenaka–Malmquist, adaptive Fourier
decomposition), on a dent, two dents, a broad shape and a one-pole shape. Plan: plans/epi-plan.md.

python3 runs/epi/epi.py > runs/epi/epi-run1.txt
python3 runs/epi/epi.py 2 > runs/epi/epi-run2.txt   (run 2: each part takes a = 0 first, as Qian's first step)
"""
import sys
import numpy as np
from scipy.optimize import minimize

RUN = int(sys.argv[1]) if len(sys.argv) > 1 else 1
M = 4096
TH = 2 * np.pi * np.arange(M) / M
ZETA = np.exp(1j * TH)
KMAX = M // 2
RHO_MAX = 1 - 0.006


def coeffs(vals):
    return np.fft.fft(vals) / M


def wrapgauss(theta, t0, w):
    return sum(np.exp(-((theta - t0 + 2 * np.pi * m) / w) ** 2 / 2) for m in range(-3, 4))


def shape(name):
    if name == 'S1':
        f = -0.25 * wrapgauss(TH, 1.0, 0.05)
        return np.exp(f) * ZETA
    if name == 'S2':
        f = -0.25 * (wrapgauss(TH, 1.0, 0.05) + wrapgauss(TH, 3.5, 0.05))
        return np.exp(f) * ZETA
    if name == 'S3':
        f = 0.10 * np.cos(2 * TH) + 0.05 * np.sin(3 * TH)
        return np.exp(f) * ZETA
    if name == 'S4':
        a = 0.8 * np.exp(1j)
        return ZETA + 0.3 / (1 - np.conj(a) * ZETA)
    raise ValueError(name)


# ---------------------------------------------------------------- E1: the Cauchy shrinks each circle by r^|k|
def e1():
    z = shape('S1')
    c = coeffs(z)
    k = np.fft.fftfreq(M, 1 / M)
    out = []
    worst = 0.0
    for g in (0.05, 0.2, 1.0):
        r = np.exp(-g)
        # direct sum over the samples, the Poisson kernel (the wrapped Cauchy), no FFT
        P = (1 - r * r) / (1 - 2 * r * np.cos(TH) + r * r)   # 2π × density
        conv = np.array([np.dot(z, np.roll(P[::-1], j + 1)) / M for j in range(M)])
        scaled = np.fft.ifft(c * r ** np.abs(k)) * M
        rel = np.max(np.abs(conv - scaled)) / np.max(np.abs(scaled))
        worst = max(worst, rel)
        cauchy_ratio = [r ** (kk + 1) / r ** kk for kk in range(1, 21)]
        sig2 = 2 * g                      # the wrapped Gaussian whose first shrink is also e^{-γ}
        gauss = np.exp(-sig2 * np.arange(1, 22) ** 2 / 2)
        gr = gauss[1:] / gauss[:-1]
        out.append((g, rel, max(abs(np.array(cauchy_ratio) - r)), gr.max() / gr.min()))
    return out, worst


# ---------------------------------------------------------------- the aimed terms (AFD)
class Part:
    def __init__(self, vals):
        self.g = vals.astype(complex)         # remainder on the samples, in H^2
        self.B = np.ones(M, complex)          # Blaschke product of the poles taken
        self.approx = np.zeros(M, complex)
        self.terms = []
        self.leak = 0.0

    def pos(self):
        c = coeffs(self.g)
        return c[:KMAX]

    def gain_at(self, a, cp):
        a = complex(a)
        val = np.polyval(cp[::-1], a)
        return (1 - abs(a) ** 2) * abs(val) ** 2

    def best(self):
        cp = self.pos()
        k = np.arange(KMAX)
        best = (-1, 0j)
        for x in np.linspace(0, np.log10(1 / 0.006), 60):
            rho = 0.0 if x == 0 else 1 - 10 ** (-x)
            full = np.zeros(M, complex)
            full[:KMAX] = cp * rho ** k
            vals = np.fft.ifft(full) * M          # g(rho e^{i phi_m})
            obj = (1 - rho * rho) * np.abs(vals) ** 2
            m = int(np.argmax(obj))
            if obj[m] > best[0]:
                best = (obj[m], rho * np.exp(1j * TH[m]))
        a0 = best[1]

        def neg(p):
            u, ph = p
            rho = RHO_MAX / (1 + np.exp(-u))
            return -self.gain_at(rho * np.exp(1j * ph), cp)

        r0 = min(abs(a0), RHO_MAX * 0.999)
        u0 = np.log(max(r0, 1e-6) / (RHO_MAX - max(r0, 1e-6))) if r0 > 0 else -8.0
        res = minimize(neg, [u0, np.angle(a0)], method='Nelder-Mead',
                       options={'xatol': 1e-10, 'fatol': 1e-18, 'maxiter': 2000})
        if -res.fun > best[0]:
            u, ph = res.x
            a = RHO_MAX / (1 + np.exp(-u)) * np.exp(1j * ph)
            return -res.fun, a
        return best

    def take(self, a):
        ea = np.sqrt(1 - abs(a) ** 2) / (1 - np.conj(a) * ZETA)
        coef = np.dot(self.g, np.conj(ea)) / M
        self.approx += coef * ea * self.B
        g = (self.g - coef * ea) * (1 - np.conj(a) * ZETA) / (ZETA - a)
        c = coeffs(g)
        self.leak = max(self.leak, np.sqrt(np.sum(np.abs(c[KMAX:]) ** 2) / max(np.sum(np.abs(c) ** 2), 1e-300)))
        c[KMAX:] = 0
        self.g = np.fft.ifft(c) * M
        self.B = self.B * (ZETA - a) / (1 - np.conj(a) * ZETA)
        self.terms.append((a, coef))


def afd(z, nmax, target=None):
    c = coeffs(z)
    c0 = c[0]
    plus = np.zeros(M, complex); plus[1:KMAX] = c[1:KMAX]
    minus = np.zeros(M, complex)                 # conj(z_-): coefficient of zeta^k is conj(c_{-k})
    for kk in range(1, KMAX + 1):
        minus[kk % M] = np.conj(c[-kk]) if kk < KMAX else np.conj(c[KMAX])
    minus[KMAX:] = 0
    P = Part(np.fft.ifft(plus) * M)
    Q = Part(np.fft.ifft(minus) * M)
    norm = np.sqrt(np.mean(np.abs(z - c0) ** 2))
    errs, picks = [], []
    if RUN >= 2:                                   # Qian's first step: a = 0, the constant, then divide by z
        for part, sgn in ((P, '+'), (Q, '-')):
            part.take(0j); picks.append((sgn, 0j))
            approx = c0 + P.approx + np.conj(Q.approx)
            errs.append(np.sqrt(np.mean(np.abs(z - approx) ** 2)) / norm)
    for n in range(nmax - len(picks)):
        gp, ap = P.best()
        gq, aq = Q.best()
        if gp >= gq:
            P.take(ap); picks.append(('+', ap))
        else:
            Q.take(aq); picks.append(('-', aq))
        approx = c0 + P.approx + np.conj(Q.approx)
        e = np.sqrt(np.mean(np.abs(z - approx) ** 2)) / norm
        errs.append(e)
        if target is not None and e < target:
            break
    return np.array(errs), picks, max(P.leak, Q.leak)


def fourier_errs(z, nmax):
    c = coeffs(z)
    p = np.abs(c[1:]) ** 2
    p = np.sort(p)[::-1]
    tot = p.sum()
    rem = np.maximum(tot - np.cumsum(p[:nmax]), 0)
    return np.sqrt(rem / tot)


def first_below(errs, t):
    idx = np.nonzero(errs < t)[0]
    return int(idx[0]) + 1 if len(idx) else None


def angdist(x, y):
    d = (x - y) % (2 * np.pi)
    return min(d, 2 * np.pi - d)


if __name__ == '__main__':
    print(f'EPI run {RUN} (plans/epi-plan.md). M = 4096 samples; errors relative L2 to ||z - c0||.\n')
    rows, worst = e1()
    print('E1: the wrapped Cauchy (Poisson kernel) by direct sum against each circle scaled by r^|k|, on S1')
    gmax = 0
    for g, rel, cr, gspread in rows:
        print(f'  gamma {g:<5} max rel diff {rel:.2e}   Cauchy shrink ratio off e^-gamma by {cr:.1e}   '
              f'wrapped Gaussian ratio max/min over k=1..20: {gspread:.3g}')
        gmax = max(gmax, cr)
    e1ok = worst < 1e-12 and gmax < 1e-12 and all(r[3] > 1.1 for r in rows)
    print(f'  E1 {"not killed" if e1ok else "KILLED"} (worst {worst:.2e})\n')

    res = {}
    for name, nmax in (('S4', 12), ('S1', 60), ('S3', 40), ('S2', 80)):
        z = shape(name)
        fe = fourier_errs(z, 600)
        ae, picks, leak = afd(z, nmax, target=1e-6)
        res[name] = (fe, ae, picks)
        print(f'{name}: negative-frequency leak in the remainders at most {leak:.1e}')
        for t in (1e-2, 1e-3, 1e-4, 1e-6):
            nf, na = first_below(fe, t), first_below(ae, t)
            print(f'  to {t:.0e}: Fourier best-n {nf} terms ({None if nf is None else 2*nf} reals); '
                  f'aimed {na} terms ({None if na is None else 4*na} reals)')
        print('  aimed terms: ' + ', '.join(f'{s}|a|={abs(a):.3f} arg={np.angle(a):+.3f}' for s, a in picks[:20]))
        print()

    fe, ae, picks = res['S4']
    nf, na = first_below(fe, 1e-4), first_below(ae, 1e-4)
    ok = na is not None and na <= 6 and nf is not None and nf >= 38
    print(f'E2 one pole: aimed {na} terms, Fourier {nf} to 1e-4: {"not killed" if ok else "KILLED"}')

    fe, ae, picks = res['S1']
    nf, na = first_below(fe, 1e-3), first_below(ae, 1e-3)
    ok = na is not None and nf is not None and na <= nf / 2
    print(f'E3 one dent: aimed {na} terms, Fourier {nf} to 1e-3: {"not killed" if ok else "KILLED"}')

    fe3, ae3, _ = res['S3']
    nf3, na3 = first_below(fe3, 1e-3), first_below(ae3, 1e-3)
    ok = na3 is not None and nf3 is not None and na3 >= nf3 - 1
    print(f'E4 broad: aimed {na3} terms, Fourier {nf3} to 1e-3: {"not killed" if ok else "KILLED"}')

    big = [(i, a) for i, (s, a) in enumerate(picks) if abs(a) > 0.5][:10]
    near = sum(1 for i, a in big if angdist(np.angle(a), 1.0) < 0.3)
    one = [1 - abs(a) for s, a in picks]
    m25 = float(np.median(one[1:5])) if len(one) >= 5 else None
    m610 = float(np.median(one[5:10])) if len(one) >= 10 else None
    ok = len(big) == 10 and near >= 8 and m25 is not None and m610 is not None and m610 < m25
    print(f'E5 aimed at the dent: {near} of the first {len(big)} with |a| > 0.5 within 0.3 of theta0; '
          f'median 1-|a| terms 2-5 {m25}, terms 6-10 {m610}: {"not killed" if ok else "KILLED"}')

    fe, ae, picks = res['S2']
    big = [a for s, a in picks[:20] if abs(a) > 0.5]
    n1 = sum(1 for a in big if angdist(np.angle(a), 1.0) < 0.3)
    n2 = sum(1 for a in big if angdist(np.angle(a), 3.5) < 0.3)
    ok = len(big) > 0 and n1 >= 0.3 * len(big) and n2 >= 0.3 * len(big)
    print(f'E6 two dents: of {len(big)} with |a| > 0.5 in the first 20, {n1} at the first, {n2} at the second: '
          f'{"not killed" if ok else "KILLED"}')
