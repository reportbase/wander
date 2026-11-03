"""AMX run 7: TVF binary leaves against Opus by perceptual measures (Zimtohrli, ViSQOL), on run 6's Sintel windows.

    python3 runs/amx/amx_percept.py <dir with the Sintel FLACs> > runs/amx/amx-run7.txt
"""
import sys, os, subprocess, tempfile
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import amx
from amx_bin import frame_numbers, leaves_N, rebuild, rice_bits
from amx_lossless import pcm, pick
import zimtohrli
from visqol.api import VisqolApi

M, SR = amx.M, 44100
TARGETS_DB = [20, 25, 30, 35, 40, 50, 60]
OPUS_KB = [24, 32, 48, 64, 96, 128, 192]
ZIM = zimtohrli.Pyohrli()
VQ = VisqolApi()
VQ.create(mode='audio')


def to48(x, sr):
    with tempfile.TemporaryDirectory() as d:
        p, q = os.path.join(d, 'a.f32'), os.path.join(d, 'b.f32')
        x.astype('<f4').tofile(p)
        subprocess.run(['ffmpeg', '-v', 'error', '-f', 'f32le', '-ar', str(sr), '-ac', '1', '-i', p, '-ar', '48000',
                        '-f', 'f32le', q], check=True)
        return np.fromfile(q, dtype='<f4').astype(float)


def scores(ref48, deg48):
    n = min(len(ref48), len(deg48))
    a, b = ref48[:n], deg48[:n]
    z = ZIM.distance(a, b)
    v = VQ.measure_from_arrays(a, b, 48000).moslqo
    return zimtohrli.mos_from_zimtohrli(z), float(v)


def snr(ref, deg):
    n = min(len(ref), len(deg))
    return 10 * np.log10(np.sum(ref[:n] ** 2) / np.sum((ref[:n] - deg[:n]) ** 2))


def leaves_at(x, eps):
    """Run 6's binary leaves at the target eps: (bytes, reconstruction)."""
    nf = len(x) // M
    frames = [frame_numbers(x[f * M:(f + 1) * M]) for f in range(nf)]
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
    return (bits + 7) // 8, np.concatenate(recs)


def opus_at(x16, kb):
    with tempfile.TemporaryDirectory() as d:
        p, q, r = (os.path.join(d, n) for n in ('a.raw', 'a.opus', 'b.raw'))
        x16.tofile(p)
        subprocess.run(['ffmpeg', '-v', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '1', '-i', p, '-ar', '48000',
                        '-c:a', 'libopus', '-b:a', f'{kb}k', q], check=True)
        sizes = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'a', '-show_entries', 'packet=size',
                                '-of', 'csv=p=0', q], check=True, capture_output=True, text=True).stdout.split()
        subprocess.run(['ffmpeg', '-v', 'error', '-i', q, '-ac', '1', '-ar', '48000', '-f', 'f32le', r], check=True)
        return sum(int(s.strip(',')) for s in sizes if s.strip(',')), np.fromfile(r, dtype='<f4').astype(float)


def align(ref, deg):
    n = min(len(ref), len(deg))
    c = np.fft.irfft(np.fft.rfft(ref[:n], 2 * n) * np.conj(np.fft.rfft(deg[:n], 2 * n)))
    lag = int(np.argmax(np.concatenate([c[-2000:], c[:2001]]))) - 2000
    if lag > 0:
        deg = np.concatenate([np.zeros(lag), deg])
    elif lag < 0:
        deg = deg[-lag:]
    return deg[:len(ref)] if len(deg) >= len(ref) else np.concatenate([deg, np.zeros(len(ref) - len(deg))]), lag


def interp(xs, ys, x):
    """Linear in log size; None outside the curve."""
    lx = np.log(np.asarray(xs, float))
    o = np.argsort(lx)
    lx, ys = lx[o], np.asarray(ys, float)[o]
    if np.log(x) < lx[0] or np.log(x) > lx[-1]:
        return None
    return float(np.interp(np.log(x), lx, ys))


def run(name, x16):
    nf = len(x16) // M
    x16 = x16[:nf * M]
    x = x16.astype(float) / 32768
    rms = np.sqrt(np.mean(x ** 2))
    ref48 = to48(x, SR)
    print(f'## {name}: {nf} frames, clip RMS {rms:.4g}')
    L, O = [], []
    for db in TARGETS_DB:
        b, rec = leaves_at(x, rms * 10 ** (-db / 20))
        r48 = to48(rec, SR)
        zm, vm = scores(ref48, r48)
        L.append((b, zm, vm, snr(ref48, r48)))
        print(f'   leaves {db} dB: {b:,} bytes, Zimtohrli MOS {zm:.3f}, ViSQOL {vm:.3f}, SNR at 48 kHz {L[-1][3]:.1f} dB')
    for kb in OPUS_KB:
        b, dec = opus_at(x16, kb)
        dec, lag = align(ref48, dec)
        g = np.dot(ref48, dec) / np.dot(dec, dec)
        zm, vm = scores(ref48, dec)
        O.append((b, zm, vm, snr(ref48, g * dec)))
        print(f'   Opus {kb} kb/s: {b:,} bytes (packets), Zimtohrli MOS {zm:.3f}, ViSQOL {vm:.3f}, '
              f'SNR {O[-1][3]:.1f} dB (lag {lag}, gain {g:.3f})')
    return L, O


def compare(L, O):
    lo, hi = max(min(l[0] for l in L), min(o[0] for o in O)), min(max(l[0] for l in L), max(o[0] for o in O))
    rows = []
    for s in np.geomspace(lo, hi, 9) if hi > lo else []:
        r = {'size': s}
        for k, i in (('zim', 1), ('vq', 2), ('snr', 3)):
            r[k] = (interp([l[0] for l in L], [l[i] for l in L], s), interp([o[0] for o in O], [o[i] for o in O], s))
        rows.append(r)
    return rows


if __name__ == '__main__':
    d = sys.argv[1]
    fight, song = os.path.join(d, '1-Snow_Fight.flac'), os.path.join(d, '7-I_Move_On-Sintels_Song.flac')
    pa, pb = pick(fight, True), pick(song, False)
    print(f'AMX run 7 (plans/amx-plan.md). Windows: Snow Fight from {pa[1]:.1f} s, Sintel\'s Song from {pb[1]:.1f} s.\n')
    res = {}
    for name, path, start in (('percussive', fight, pa[1]), ('tonal', song, pb[1])):
        res[name] = run(name, pcm(path, start, 2))
        print()
    g1, g3, agree, tot = True, True, 0, 0
    for name, (L, O) in res.items():
        rows = compare(L, O)
        print(f'{name}: at equal size (interpolated in log size; leaves | Opus)')
        for r in rows:
            z, v, s = r['zim'], r['vq'], r['snr']
            print(f'   {r["size"]:9,.0f} bytes  Zimtohrli {z[0]:.3f} | {z[1]:.3f}   ViSQOL {v[0]:.3f} | {v[1]:.3f}   '
                  f'SNR {s[0]:.1f} | {s[1]:.1f} dB')
            g1 &= z[1] > z[0]
            g3 &= s[0] > s[1]
            tot += 1
            agree += (z[1] > z[0]) == (v[1] > v[0])
        if not rows:
            print('   no common sizes')
    L, O = res['tonal']
    target = [o for o, kb in zip(O, OPUS_KB) if kb == 128][0]
    ok = [l for l in sorted(L) if l[1] >= target[1]]
    need = ok[0][0] / target[0] if ok else None
    print(f'\nG1 Opus above the leaves by Zimtohrli at every common size: {"not killed" if g1 else "KILLED"}')
    print(f'G2 tonal: Opus 128 kb/s Zimtohrli MOS {target[1]:.3f} at {target[0]:,} bytes; the leaves reach it at '
          f'{"never (within 60 dB)" if need is None else f"{need:.2f}× those bytes"} (≥ 2× or never): '
          f'{"not killed" if need is None or need >= 2 else "KILLED"}')
    print(f'G3 the leaves above Opus by SNR at every common size: {"not killed" if g3 else "KILLED"}')
    print(f'G4 ViSQOL agrees with Zimtohrli on the winner in {agree} of {tot} (≥ 75%): '
          f'{"not killed" if tot and agree >= 0.75 * tot else "KILLED"}')
