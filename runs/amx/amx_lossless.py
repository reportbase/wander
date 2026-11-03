"""AMX run 5: a lossless source (the Sintel score), binary leaves near-transparent, lossless TVF, FLAC and Opus.

    python3 runs/amx/amx_lossless.py <dir with 1-Snow_Fight.flac and 7-I_Move_On-Sintels_Song.flac> > runs/amx/amx-run6.txt
"""
import sys, os, subprocess, tempfile
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import amx
from amx_bin import frame_numbers, leaves_N, rebuild, rice_bits
M, SR = amx.M, 44100


def pcm(path, start=0.0, dur=None):
    cmd = ['ffmpeg', '-v', 'error', '-i', path, '-ss', str(start)] + (['-t', str(dur)] if dur else []) + \
          ['-ac', '1', '-c:a', 'pcm_s16le', '-f', 's16le', '-']
    return np.frombuffer(subprocess.run(cmd, check=True, capture_output=True).stdout, dtype='<i2').astype(np.int16)


def encode(x16, args, ext):
    with tempfile.TemporaryDirectory() as d:
        p, q, r = (os.path.join(d, n) for n in ('a.raw', 'a.' + ext, 'b.raw'))
        x16.tofile(p)
        subprocess.run(['ffmpeg', '-v', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '1', '-i', p] + args + [q],
                       check=True)
        subprocess.run(['ffmpeg', '-v', 'error', '-i', q, '-ac', '1', '-ar', str(SR), '-c:a', 'pcm_s16le', '-f', 's16le',
                        r], check=True)
        size = amx.flac_audio_bytes(q) if ext == 'flac' else os.path.getsize(q)
        return size, np.fromfile(r, dtype='<i2').astype(float)


def attack(x16):
    x = x16.astype(float) / 32768
    r = np.array([np.sqrt(np.mean(x[i * M:(i + 1) * M] ** 2)) for i in range(len(x) // M)])
    ok = (r[:-1] > 1e-3) & (r[1:] > 1e-3)
    return float(np.max((r[1:] / np.maximum(r[:-1], 1e-12))[ok])) if ok.any() else 0.0, float(np.sqrt(np.mean(x ** 2)))


def pick(path, largest):
    full = pcm(path)
    n = int(2 * SR)
    best = None
    for s in range(0, len(full) - n, SR // 2):
        a, rms = attack(full[s:s + n])
        if not largest and rms < 0.02:
            continue
        if best is None or (a > best[0] if largest else a < best[0]):
            best = (a, s / SR, rms)
    return best


def run(name, x16):
    x = x16.astype(float) / 32768
    nf = len(x) // M
    x16 = x16[:nf * M]
    x = x[:nf * M]
    rms = np.sqrt(np.mean(x ** 2))
    floor = 2 ** -15 / np.sqrt(12)
    flac, _ = encode(x16, ['-c:a', 'flac', '-compression_level', '12'], 'flac')
    frames = [frame_numbers(x[f * M:(f + 1) * M]) for f in range(nf)]
    print(f'## {name}: {nf} frames, clip RMS {rms:.4g}; FLAC {flac:,} bytes')
    out = {'flac': flac}
    lossless = []
    for tname, eps in (('40 dB', 1e-2 * rms), ('60 dB', 1e-3 * rms), ('16-bit floor', floor)):
        Ns = [leaves_N(c, (0.9 * eps) ** 2 * M) for _, _, c in frames]
        q = 2.0 ** -1
        while True:
            recs, ok = [], True
            for (y, line, c), N in zip(frames, Ns):
                lq = np.round(np.array([line[0], line[-1]]) / q) * q
                lineq = lq[0] + (lq[1] - lq[0]) * np.arange(M) / (M - 1)
                rec = rebuild(c, N, q, lq) + lineq
                if np.sqrt(np.mean((y + line - rec) ** 2)) > eps:
                    ok = False
                    break
                recs.append(rec)
            if ok:
                break
            q /= 2
        bits = 0
        for (y, line, c), N in zip(frames, Ns):
            seq = [line[0], line[-1]] + ([] if N == 0 else list(amx.leaf_values(c, N)))
            if N >= M:
                seq.append((c[M // 2] / M).real)
            bits += 7 + 2 + 5 + rice_bits(np.round(np.array(seq) / q).astype(np.int64))
        b = (bits + 7) // 8
        # lossless: the integer remainder against the rounded rebuild
        rb = 0
        for f, rec in enumerate(recs):
            pred = np.clip(np.round(rec * 32768), -32768, 32767).astype(np.int64)
            rb += 2 + 5 + rice_bits(x16[f * M:(f + 1) * M].astype(np.int64) - pred)
        lossless.append((tname, b + (rb + 7) // 8))
        out[tname] = b
        print(f'   {tname}: binary leaves {b:,} bytes = {b / flac:.3f} × FLAC (step 2^{int(np.log2(q))}); '
              f'with the integer remainder, lossless {lossless[-1][1]:,} = {lossless[-1][1] / flac:.3f} × FLAC')
    rb = 0
    for f in range(nf):
        rb += 2 + 5 + rice_bits(x16[f * M:(f + 1) * M].astype(np.int64))
    lossless.append(('no leaves', (rb + 7) // 8))
    print(f'   no leaves, the PCM alone by the same fixed predictor and Rice code: {lossless[-1][1]:,} = '
          f'{lossless[-1][1] / flac:.3f} × FLAC')
    bestl = min(lossless, key=lambda t: t[1])
    out['lossless'] = bestl[1]
    print(f'   lossless TVF, best ({bestl[0]}): {bestl[1]:,} bytes = {bestl[1] / flac:.3f} × FLAC')
    out['opus'] = {}
    for kb in (64, 128, 256):
        size, dec = encode(x16, ['-ar', '48000', '-c:a', 'libopus', '-b:a', f'{kb}k'], 'opus')
        ref = x16.astype(float)
        n = min(len(dec), len(ref))
        lags = range(-2000, 2001)
        best = max(lags, key=lambda L: np.dot(ref[max(0, L):n + min(0, L)], dec[max(0, -L):n - max(0, L)])
                   if abs(L) < n else -1e300)
        a = ref[max(0, best):n + min(0, best)]
        bdec = dec[max(0, -best):n - max(0, best)]
        g = np.dot(a, bdec) / np.dot(bdec, bdec)
        snr = 10 * np.log10(np.sum(a ** 2) / np.sum((a - g * bdec) ** 2))
        out['opus'][kb] = snr
        print(f'   Opus {kb} kb/s: {size:,} bytes = {size / flac:.3f} × FLAC, SNR {snr:.1f} dB (lag {best}, gain {g:.3f})')
    return out


if __name__ == '__main__':
    d = sys.argv[1]
    print('AMX run 6 (plans/amx-plan.md): the Sintel score, lossless source.\n')
    fight, song = os.path.join(d, '1-Snow_Fight.flac'), os.path.join(d, '7-I_Move_On-Sintels_Song.flac')
    pa, pb = pick(fight, True), pick(song, False)
    print(f'percussive window: Snow Fight from {pa[1]:.1f} s (attack {pa[0]:.2f}, RMS {pa[2]:.4f})')
    print(f'tonal window: Sintel\'s Song from {pb[1]:.1f} s (attack {pb[0]:.2f}, RMS {pb[2]:.4f})\n')
    ra = run('Snow Fight, percussive', pcm(fight, pa[1], 2))
    print()
    rb = run('Sintel\'s Song, tonal', pcm(song, pb[1], 2))
    print()
    r = [(n, o['16-bit floor'] / o['flac']) for n, o in (('percussive', ra), ('tonal', rb))]
    print(f'E1 binary leaves at the floor / FLAC: {", ".join(f"{n} {v:.3f}" for n, v in r)} (≥ 1.0): '
          f'{"not killed" if all(v >= 1.0 for _, v in r) else "KILLED"}')
    r = [(n, o['lossless'] / o['flac']) for n, o in (('percussive', ra), ('tonal', rb))]
    print(f'E2 lossless TVF / FLAC: {", ".join(f"{n} {v:.3f}" for n, v in r)} (1.0–1.3): '
          f'{"not killed" if all(1.0 <= v <= 1.3 for _, v in r) else "KILLED"}')
    r = [(n, o['60 dB'] / o['flac']) for n, o in (('percussive', ra), ('tonal', rb))]
    print(f'E3 binary leaves at 60 dB / FLAC: {", ".join(f"{n} {v:.3f}" for n, v in r)} (< 1.0): '
          f'{"not killed" if all(v < 1.0 for _, v in r) else "KILLED"}')
    r = [(n, o['opus'][128]) for n, o in (('percussive', ra), ('tonal', rb))]
    print(f'E4 Opus 128 kb/s SNR: {", ".join(f"{n} {v:.1f} dB" for n, v in r)} (< 30 dB): '
          f'{"not killed" if all(v < 30 for _, v in r) else "KILLED"}')
