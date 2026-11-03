"""AMX run 4: run 3's leaves packed as binary (quantized, fixed polynomial prediction, Rice coding), against FLAC.

    python3 runs/amx/amx_bin.py <dir with the two .ogg files> > runs/amx/amx-run4.txt
"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import amx
M = amx.M


def frame_numbers(seg):
    t = np.arange(M) / (M - 1)
    line = seg[0] + (seg[-1] - seg[0]) * t
    y = seg - line
    return y, line, np.fft.fft(y)


def leaves_N(c, tol2):
    pw = np.abs(c) ** 2 / M
    for N in range(0, M + 1, 8):
        if pw.sum() - (np.abs(amx.leaves_of(c, N)) ** 2 / M).sum() <= tol2:
            return N
    return M


def rebuild(c, N, q, line_q):
    """The frame from its numbers rounded to the step q."""
    vals = [] if N == 0 else list(np.round(amx.leaf_values(c, N) / q) * q)
    part = np.zeros(M)
    if N:
        lv = np.array(vals)
        L = np.fft.fft(lv) / N
        Lc = L * np.exp(-1j * np.pi * np.fft.fftfreq(N, 1 / N) / N)
        full = np.zeros(M, complex)
        h = N // 2
        full[:h] = Lc[:h]
        if h > 1:
            full[M - h + 1:] = Lc[N - h + 1:]
        part = np.real(np.fft.ifft(full) * M)
    if N >= M:
        nyq = np.round((c[M // 2] / M).real / q) * q
        part = part + nyq * np.cos(np.pi * np.arange(M))
    return part


def rice_bits(ints):
    """Best fixed predictor (order 0–3) and Rice parameter; bits for the residuals."""
    best = None
    x = np.asarray(ints, dtype=np.int64)
    for order in range(4):
        if len(x) <= order:
            continue
        r = x.copy()
        for _ in range(order):
            r = np.diff(r)
        u = np.where(r >= 0, 2 * r, -2 * r - 1)
        for k in range(0, 24):
            bits = int(np.sum((u >> k) + 1 + k)) + order * 24   # warm-up values sent raw
            if best is None or bits < best:
                best = bits
    return best if best is not None else 0


def run(name, x16):
    x = x16.astype(float) / 32768
    nf = len(x) // M
    x = x[:nf * M]
    rms = np.sqrt(np.mean(x ** 2))
    floor = 2 ** -15 / np.sqrt(12)
    flac = amx.flac_bytes(x16[:nf * M])
    frames = [frame_numbers(x[f * M:(f + 1) * M]) for f in range(nf)]
    print(f'## {name}: FLAC {flac:,} bytes')
    out = {}
    for tname, eps in (('40 dB', 1e-2 * rms), ('60 dB', 1e-3 * rms), ('16-bit floor', floor)):
        Ns = [leaves_N(c, (0.9 * eps) ** 2 * M) for _, _, c in frames]
        q = 2.0 ** -1
        while True:
            ok = True
            for (y, line, c), N in zip(frames, Ns):
                lq = np.round(np.array([line[0], line[-1]]) / q) * q
                lineq = lq[0] + (lq[1] - lq[0]) * np.arange(M) / (M - 1)
                err = np.sqrt(np.mean((y + line - rebuild(c, N, q, lq) - lineq) ** 2))
                if err > eps:
                    ok = False
                    break
            if ok:
                break
            q /= 2
        bits = 0
        for (y, line, c), N in zip(frames, Ns):
            seq = [line[0], line[-1]] + ([] if N == 0 else list(amx.leaf_values(c, N)))
            if N >= M:
                seq.append((c[M // 2] / M).real)
            ints = np.round(np.array(seq) / q).astype(np.int64)
            bits += 7 + 2 + 5 + rice_bits(ints)
        b = (bits + 7) // 8
        out[tname] = b
        print(f'   {tname}: {sum(2 + N + (N >= M) for N in Ns):,} numbers, step 2^{int(np.log2(q))}, '
              f'{b:,} bytes = {b / flac:.3f} × FLAC')
    return out, flac


if __name__ == '__main__':
    d = sys.argv[1]
    print('AMX run 4 (plans/amx-plan.md): run 3\'s leaves as binary (quantized, fixed prediction, Rice).\n')
    s, fs = run('snare (first 2 s)', amx.pcm(os.path.join(d, 'snare-accelerate.ogg'), 0, 2))
    t, ft = run('trumpet (first 2 s)', amx.pcm(os.path.join(d, 'sorohanro_-_solo-trumpet-06.ogg'), 0, 2))
    text = {'snare': {'40 dB': 18924, '60 dB': 26897, '16-bit floor': 38925},
            'trumpet': {'40 dB': 45794, '60 dB': 102660, '16-bit floor': 152281}}
    d1 = s['16-bit floor'] / fs < 1.0 and t['16-bit floor'] / ft < 1.3
    print(f'\nD1 at the 16-bit floor binary/FLAC snare {s["16-bit floor"] / fs:.3f} (< 1.0), trumpet '
          f'{t["16-bit floor"] / ft:.3f} (< 1.3): {"not killed" if d1 else "KILLED"}')
    rat = [r[k] / text[n][k] for n, r in (('snare', s), ('trumpet', t)) for k in r]
    print(f'D2 binary/text: {", ".join(f"{v:.3f}" for v in rat)} (all ≤ 0.5): '
          f'{"not killed" if all(v <= 0.5 for v in rat) else "KILLED"}')
