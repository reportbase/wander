"""AMX run 1: aimed terms mixed into even leaves, on real audio. Plan: plans/amx-plan.md (predictions written first).

    python3 runs/amx/amx.py <dir with the two .ogg files> > runs/amx/amx-run1.txt

Each 1024-sample frame, its end-to-end line taken off, is read by: even leaves (the band-limited projection, N leaf
values), and the mixed reader (N leaves, then aimed Takenaka–Malmquist terms by Qian's greedy on what is left, 4 reals a
term), the cheapest (N, n) meeting the target kept. Bytes are the numbers as decimal text with d significant digits, a
frame a line, gzipped. FLAC on the same 16-bit PCM for reference.
"""
import sys, os, gzip, subprocess, tempfile
import numpy as np
from scipy.optimize import minimize
from multiprocessing import Pool

M = 1024
KH = M // 2 + 1                     # analytic part: frequencies 0 … M/2
TH = 2 * np.pi * np.arange(M) / M
Z = np.exp(1j * TH)
RHO_MAX = 1 - 1e-3
NSTEP, NMAX_TERMS = 8, 64
KK = np.arange(KH)


def pcm(path, start=0.0, dur=None):
    cmd = ['ffmpeg', '-v', 'error', '-i', path, '-ss', str(start)] + (['-t', str(dur)] if dur else []) + \
          ['-ac', '1', '-ar', '22050', '-c:a', 'pcm_s16le', '-f', 's16le', '-']
    raw = subprocess.run(cmd, check=True, capture_output=True).stdout
    return np.frombuffer(raw, dtype='<i2').astype(np.int16)


def flac_bytes(x16):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, 'a.raw')
        x16.tofile(p)
        q = os.path.join(d, 'a.flac')
        subprocess.run(['ffmpeg', '-v', 'error', '-f', 's16le', '-ar', '22050', '-ac', '1', '-i', p,
                        '-c:a', 'flac', '-compression_level', '12', q], check=True)
        return os.path.getsize(q)


# ── the aimed terms on an analytic remainder ────────────────────────────
def ea(a):
    return np.sqrt(1 - abs(a) ** 2) / (1 - np.conj(a) * Z)


def best_a(g):
    c = np.fft.fft(g) / M
    cp = c[:KH]
    best = (-1.0, 0j)
    for x in np.linspace(0, np.log10(1 / (1 - RHO_MAX)), 24):
        rho = 0.0 if x == 0 else 1 - 10 ** (-x)
        full = np.zeros(M, complex)
        full[:KH] = cp * rho ** KK
        vals = np.fft.ifft(full) * M
        obj = (1 - rho * rho) * np.abs(vals) ** 2
        m = int(np.argmax(obj))
        if obj[m] > best[0]:
            best = (obj[m], rho * np.exp(1j * TH[m]))

    def gain(a):
        p = a ** KK
        return (1 - abs(a) ** 2) * abs(np.dot(cp, p)) ** 2

    def neg(p):
        rho = RHO_MAX / (1 + np.exp(-p[0]))
        return -gain(rho * np.exp(1j * p[1]))

    r0 = min(max(abs(best[1]), 1e-4), RHO_MAX * 0.999)
    res = minimize(neg, [np.log(r0 / (RHO_MAX - r0)), np.angle(best[1])], method='Nelder-Mead',
                   options={'xatol': 1e-9, 'fatol': 1e-20, 'maxiter': 60})
    if -res.fun > best[0]:
        return RHO_MAX / (1 + np.exp(-res.x[0])) * np.exp(1j * res.x[1])
    return best[1]


def afd_steps(h, nmax, stop_err2, budget):
    """Greedy on analytic h; yields (n, approx of h) after each term, up to nmax or the budget of terms."""
    g = h.copy()
    B = np.ones(M, complex)
    ap = np.zeros(M, complex)
    terms = []
    for n in range(1, min(nmax, budget) + 1):
        a = best_a(g)
        e = ea(a)
        coef = np.vdot(e, g) / M
        ap = ap + coef * e * B
        g = (g - coef * e) * (1 - np.conj(a) * Z) / (Z - a)
        c = np.fft.fft(g)
        c[KH:] = 0
        g = np.fft.ifft(c)
        B = B * (Z - a) / (1 - np.conj(a) * Z)
        terms.append((a, coef))
        yield n, ap, list(terms)


def synth_terms(terms):
    B = np.ones(M, complex)
    ap = np.zeros(M, complex)
    for a, coef in terms:
        ap = ap + coef * ea(a) * B
        B = B * (Z - a) / (1 - np.conj(a) * Z)
    return ap


# ── one frame ──────────────────────────────────────────────────────────
def leaves_of(c, N):
    """The frame's band-limited projection with N leaves: frequencies |k| < N/2."""
    if N >= M:              # run 2: the whole frame, the top frequency included
        return c.copy()
    keep = np.zeros(M, complex)
    if N > 0:
        h = N // 2
        keep[:h] = c[:h]
        if h > 1:
            keep[M - h + 1:] = c[M - h + 1:]
    return keep


def leaf_values(c, N):
    """The projection's values at the N leaves, positions (k + 1/2)·M/N, exactly (c the frame's unnormalised FFT)."""
    h = N // 2
    m = np.arange(-(h - 1), h)
    cm = c[m % M] / M
    p = (np.arange(N) + 0.5) * M / N
    return np.real(np.exp(2j * np.pi * np.outer(p, m) / M) @ cm)


def frame_job(args):
    """Every target at once: the greedy's terms for a given N do not depend on the target, so one run serves all."""
    y, tol2s = args                    # y: frame with its line taken off; tol2s: per-target allowed sum of squares
    c = np.fft.fft(y)
    pw = np.abs(c) ** 2 / M            # Parseval: sum of squares in the frame
    best = []
    for tol2 in tol2s:                 # pure leaves: the least N (step 8) whose tail is within the allowance
        Nmin = M
        for N in range(0, M + 1, NSTEP):
            tail = pw.sum() - (np.abs(leaves_of(c, N)) ** 2 / M).sum()
            if tail <= tol2:
                Nmin = N
                break
        best.append({'cost': Nmin, 'N': Nmin, 'terms': [], 'leaf': Nmin})
    for N in range((max(b['leaf'] for b in best) - 1) // 64 * 64, -1, -64):
        budgets = [(b['cost'] - N - 1) // 4 for b in best]
        budget = min(NMAX_TERMS, max(budgets))
        if budget < 1:
            continue
        keep = leaves_of(c, N)
        r = np.real(np.fft.ifft(c - keep))           # the remainder, real
        rc = np.fft.fft(r) / M
        h = np.zeros(M, complex)
        h[1:M // 2] = rc[1:M // 2]
        h[M // 2] = rc[M // 2] / 2
        hz = np.fft.ifft(h) * M                      # analytic: r - rc0 = 2 Re hz
        r0 = rc[0].real
        open_ = [ti for ti in range(len(tol2s)) if budgets[ti] >= 1]
        for n, ap, terms in afd_steps(hz, NMAX_TERMS, 0, budget):
            e2 = np.sum((r - r0 - 2 * np.real(ap)) ** 2)
            for ti in list(open_):
                if n > budgets[ti]:
                    open_.remove(ti)
                elif e2 <= tol2s[ti]:
                    best[ti] = {'cost': N + 4 * n, 'N': N, 'terms': terms, 'leaf': best[ti]['leaf'], 'r': r}
                    open_.remove(ti)
            if not open_:
                break
    return best


def recon(c, sol, d):
    """The frame back from a solution with every number rounded to d significant digits."""
    def rnd(x):
        if x == 0:
            return 0.0
        return float(f'{x:.{d - 1}e}')
    keep = leaves_of(c, sol['N'])
    leaves_part = np.real(np.fft.ifft(keep))
    if sol['N'] > 0:      # the N leaf values, rounded, then the projection back (the leaves are the stored numbers)
        lv = np.array([rnd(v) for v in leaf_values(c, sol['N'])])
        # trigonometric interpolation through the rounded leaves (even N, the half-shifted lattice)
        L = np.fft.fft(lv) / sol['N']
        shift = np.exp(-1j * np.pi * np.fft.fftfreq(sol['N'], 1 / sol['N']) / sol['N'])
        Lc = L * shift
        full = np.zeros(M, complex)
        h = sol['N'] // 2
        full[:h] = Lc[:h]
        if h > 1:
            full[M - h + 1:] = Lc[sol['N'] - h + 1:]
        leaves_part = np.real(np.fft.ifft(full) * M)
    terms = [(complex(rnd(a.real), rnd(a.imag)), complex(rnd(co.real), rnd(co.imag))) for a, co in sol['terms']]
    if terms and max(abs(a) for a, _ in terms) >= 1:
        return None
    aimed = 2 * np.real(synth_terms(terms)) if terms else 0
    return leaves_part + aimed, (sol['N'], terms)


def run_clip(name, x16, pool):
    x = x16.astype(float) / 32768
    nf = len(x) // M
    x = x[:nf * M]
    rms = np.sqrt(np.mean(x ** 2))
    floor = 2 ** -15 / np.sqrt(12)
    targets = [('40 dB', 1e-2 * rms), ('60 dB', 1e-3 * rms), ('16-bit floor', floor)]
    frames, lines_ = [], []
    for f in range(nf):
        seg = x[f * M:(f + 1) * M]
        t = np.arange(M) / (M - 1)
        line = seg[0] + (seg[-1] - seg[0]) * t
        frames.append((seg, line, seg - line))
    jobs = [(fr[2], [(0.9 * e) ** 2 * M for _, e in targets]) for fr in frames]
    sols = pool.map(frame_job, jobs)
    flac = flac_bytes(x16[:nf * M])
    pcm_gz = len(gzip.compress(x16[:nf * M].tobytes(), 9))
    print(f'## {name}: {nf} frames of {M}, {nf * M / 22050:.2f} s, clip RMS {rms:.4g} of full scale')
    print(f'   FLAC (level 12) {flac:,} bytes; PCM16 gzipped {pcm_gz:,}; PCM16 raw {2 * nf * M:,}')
    res = {'flac': flac}
    for ti, (tname, eps) in enumerate(targets):
        snr = 20 * np.log10(rms / eps)
        rows = {}
        for kind in ('leaves', 'mixed'):
            chosen = []
            for fi, s in enumerate(sols):
                sol = s[ti]
                if kind == 'leaves':
                    sol = {'N': sol['leaf'], 'terms': []}
                chosen.append(sol)
            nums = sum(2 + s['N'] + 4 * len(s['terms']) for s in chosen)
            ok_d = None
            for d in range(2, 10):
                text, good = [], True
                for fi, sol in enumerate(chosen):
                    seg, line, y = frames[fi]
                    c = np.fft.fft(y)
                    out = recon(c, sol, d)
                    if out is None:
                        good = False
                        break
                    yy, (N, terms) = out
                    err = np.sqrt(np.mean((y - yy) ** 2))
                    if err > eps:
                        good = False
                        break
                    def fmt(v):
                        return f'{v:.{d - 1}e}' if v != 0 else '0'
                    vals = [line[0], line[-1]]
                    if N:
                        vals += list(leaf_values(c, N))
                    for a, co in terms:
                        vals += [a.real, a.imag, co.real, co.imag]
                    text.append(f'{N} {len(terms)} ' + ' '.join(fmt(v) for v in vals))
                if good:
                    ok_d = d
                    gz = len(gzip.compress(('\n'.join(text) + '\n').encode(), 9))
                    break
            nterm = sum(len(s['terms']) for s in chosen)
            nleaf = sum(s['N'] for s in chosen)
            rows[kind] = gz if ok_d else None
            tail = f'd = {ok_d}, gzipped {gz:,} bytes = {gz / flac:.3f} × FLAC' if ok_d else 'no d from 2 to 9 meets it'
            print(f'   {tname} (SNR {snr:.1f} dB) {kind:6s}: {nums:,} numbers ({nleaf:,} leaves, {nterm:,} aimed terms), '
                  + tail)
        res[tname] = rows
        res[tname + ' sols'] = [s[ti] for s in sols]
    return res, frames


def a4(sols, frames):
    hits = tot = 0
    for fi, sol in enumerate(sols):
        deep = [a for a, _ in sol['terms'] if abs(a) > 0.9]
        if not deep or 'r' not in sol:
            continue
        r = sol['r']
        jmax = int(np.argmax(np.abs(r)))
        for a in deep[:1]:
            j = (np.angle(a) % (2 * np.pi)) * M / (2 * np.pi)
            dist = min(abs(j - jmax), M - abs(j - jmax))
            tot += 1
            hits += dist <= 32
    return hits, tot


if __name__ == '__main__':
    d = sys.argv[1]
    snare = pcm(os.path.join(d, 'snare-accelerate.ogg'), 0, 2)
    trumpet = pcm(os.path.join(d, 'sorohanro_-_solo-trumpet-06.ogg'), 0, 2)
    print('AMX run 2 (plans/amx-plan.md). Frames of 1024, the line off each, targets per frame against the clip RMS.\n')
    with Pool(4) as pool:
        rs, fs = run_clip('snare (first 2 s)', snare, pool)
        print()
        rt, ft = run_clip('trumpet (first 2 s)', trumpet, pool)
    print()

    def ratio(r, t):
        a, b = r[t]['mixed'], r[t]['leaves']
        return a / b if a and b else float('nan')
    fl, t40 = ratio(rs, '16-bit floor'), ratio(rs, '40 dB')
    ok = fl <= 0.8 and t40 >= 0.95
    print(f'A1 snare mixed/leaves: 16-bit floor {fl:.3f} (≤ 0.8), 40 dB {t40:.3f} (≥ 0.95): {"not killed" if ok else "KILLED"}')
    tr = [ratio(rt, t) for t in ('40 dB', '60 dB', '16-bit floor')]
    ok = all(v >= 0.95 for v in tr)
    print(f'A2 trumpet mixed/leaves at 40, 60 dB, 16-bit floor: {", ".join(f"{v:.3f}" for v in tr)} (all ≥ 0.95): '
          f'{"not killed" if ok else "KILLED"}')
    q = lambda r, k: (r['16-bit floor'][k] or float('nan')) / r['flac']
    ls, lt, ms = q(rs, 'leaves'), q(rt, 'leaves'), q(rs, 'mixed')
    ok = 0.7 <= ls <= 1.5 and 0.7 <= lt <= 1.5 and ms < 1.0
    print(f'A3 at the 16-bit floor, leaves/FLAC snare {ls:.3f}, trumpet {lt:.3f} (0.7–1.5); mixed/FLAC snare {ms:.3f} '
          f'(< 1.0): {"not killed" if ok else "KILLED"}')
    h, t = a4(rs['60 dB sols'], fs)
    ok = t > 0 and h >= 0.6 * t
    print(f'A4 snare at 60 dB: the first deep standpoint within 32 samples of the largest remainder in {h} of {t} frames '
          f'(≥ 60%): {"not killed" if ok else "KILLED"}')
