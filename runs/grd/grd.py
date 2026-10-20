"""GRD run 1: the ratio between grid modules, on Gardner et al. 2022 (figshare 16764508, CC0). See plans/grd-plan.md.

The method is the one fixed in the plan before the data was opened: each rat's first open-field session; rate maps of
2.5 cm bins, counts and occupancy each smoothed by a Gaussian of sigma 2.5 cm, bins under 0.1 s of smoothed occupancy
left out; the Pearson autocorrelogram over bins valid at both ends (at least 20); a cell's spacing the median distance
of the six local maxima (3 x 3, r > 0, zero lag excluded) nearest the centre; a module's spacing the median of its
cells'; modules ordered by spacing within a rat. Numpy only.
Run: python3 runs/grd/grd.py <data dir>   (the unzipped Toroidal_topology_grid_cell_data; a few minutes)
"""
import sys, os, re
import numpy as np

D = sys.argv[1]
BIN_CM, SIGMA_CM, MIN_OCC, MIN_OVERLAP = 2.5, 2.5, 0.1, 20

def sessions(txt):
    """[(name, start, end, valid windows or None)] in the file's own order"""
    out = []
    for line in open(txt):
        m = re.match(r'\s*#\d+,\s*(\w+),\s*start=(\d+),\s*end=(\d+)(?:,\s*valid_times=\[(.*)\])?', line)
        if m:
            vt = None
            if m.group(4):
                vt = [tuple(float(v) for v in w.split(',')) for w in m.group(4).split(';')]
            out.append((m.group(1), float(m.group(2)), float(m.group(3)), vt))
    return out

def gauss_smooth(a, sigma_bins):
    r = int(np.ceil(4 * sigma_bins))
    k = np.exp(-0.5 * (np.arange(-r, r + 1) / sigma_bins) ** 2); k /= k.sum()
    a = np.apply_along_axis(lambda v: np.convolve(v, k, mode='same'), 0, a)
    return np.apply_along_axis(lambda v: np.convolve(v, k, mode='same'), 1, a)

def masked_autocorr(rate, valid):
    """Pearson correlation of the map with itself at every lag, over bins valid at both; NaN where under MIN_OVERLAP."""
    X = np.where(valid, rate, 0.0); M = valid.astype(float)
    ny, nx = X.shape; sy, sx = 2 * ny - 1, 2 * nx - 1
    F = lambda a: np.fft.rfft2(a, s=(sy, sx))
    def xc(a, b):   # sum over u of a(u) b(u + lag), all lags, centred
        c = np.fft.irfft2(np.conj(F(a)) * F(b), s=(sy, sx))
        return np.fft.fftshift(c)
    N = np.rint(xc(M, M))
    S1, S2 = xc(X, M), xc(M, X)
    S11, S22, S12 = xc(X * X, M), xc(M, X * X), xc(X, X)
    with np.errstate(invalid='ignore', divide='ignore'):
        num = N * S12 - S1 * S2
        den = np.sqrt((N * S11 - S1 ** 2) * (N * S22 - S2 ** 2))
        r = num / den
    r[N < MIN_OVERLAP] = np.nan
    return r

def spacing_of(r, bin_size):
    cy, cx = (r.shape[0] - 1) // 2, (r.shape[1] - 1) // 2
    pad = np.pad(r, 1, constant_values=np.nan)
    peaks = []
    for y in range(r.shape[0]):
        for x in range(r.shape[1]):
            v = r[y, x]
            if not np.isfinite(v) or v <= 0 or (y == cy and x == cx): continue
            nb = pad[y:y + 3, x:x + 3].copy(); nb[1, 1] = -np.inf
            if np.all(~np.isfinite(nb) | (nb < v)):
                peaks.append(np.hypot(y - cy, x - cx) * bin_size)
    if len(peaks) < 6: return None
    return float(np.median(sorted(peaks)[:6]))

def rat_spacings(npz, sess_txt):
    z = np.load(npz, allow_pickle=True)
    x, y, t = z['x'].astype(float), z['y'].astype(float), z['t'].astype(float)
    of = [s for s in sessions(sess_txt) if s[0].startswith('open_field')][0]
    windows = of[3] if of[3] else [(of[1], of[2])]
    keep = np.zeros(t.shape, bool)
    for a, b in windows: keep |= (t >= a) & (t <= b)
    xs, ys, ts = x[keep], y[keep], t[keep]
    ok = np.isfinite(xs) & np.isfinite(ys); xs, ys, ts = xs[ok], ys[ok], ts[ok]
    unit = 100.0 if (np.nanmax(xs) - np.nanmin(xs)) < 10 else 1.0     # metres if the range is under 10
    xs, ys = xs * unit, ys * unit
    dt = np.median(np.diff(ts))
    ex = np.arange(np.min(xs), np.max(xs) + BIN_CM, BIN_CM); ey = np.arange(np.min(ys), np.max(ys) + BIN_CM, BIN_CM)
    occ = np.histogram2d(ys, xs, bins=[ey, ex])[0] * dt
    occ_s = gauss_smooth(occ, SIGMA_CM / BIN_CM)
    valid = occ_s >= MIN_OCC
    out = {}
    mods = sorted(k for k in z.keys() if k.startswith('spikes_mod'))
    for mk in mods:
        cells = z[mk].item()
        sp = []
        for cid, st in cells.items():
            st = np.asarray(st, float)
            inw = np.zeros(st.shape, bool)
            for a, b in windows: inw |= (st >= a) & (st <= b)
            st = st[inw]
            if st.size == 0: continue
            sx, sy = np.interp(st, ts, xs), np.interp(st, ts, ys)
            cnt = np.histogram2d(sy, sx, bins=[ey, ex])[0]
            cnt_s = gauss_smooth(cnt, SIGMA_CM / BIN_CM)
            with np.errstate(invalid='ignore', divide='ignore'):
                rate = cnt_s / occ_s
            sg = spacing_of(masked_autocorr(rate, valid), BIN_CM)
            if sg is not None: sp.append(sg)
        out[mk] = (len(cells), len(sp), float(np.median(sp)) if sp else None)
    return out, unit, of[0], windows

rats = [('Q', 'rat_q_grid_modules_1_2.npz', 'rat_q_sessions.txt'),
        ('R', 'rat_r_day1_grid_modules_1_2_3.npz', 'rat_r_day1_sessions.txt'),
        ('S', 'rat_s_grid_modules_1.npz', 'rat_s_sessions.txt')]
modules = {}
for name, f, s in rats:
    res, unit, sess, win = rat_spacings(os.path.join(D, f), os.path.join(D, s))
    sp = sorted(v[2] for v in res.values() if v[2] is not None)
    modules[name] = sp
    print(f"rat {name}: {sess} {win}, positions x{unit:g} to cm; " +
          "; ".join(f"{k}: {v[1]} of {v[0]} cells, spacing {v[2]:.1f} cm" if v[2] else f"{k}: {v[1]} of {v[0]} cells"
                    for k, v in res.items()))
ratios = {n: [b / a for a, b in zip(sp, sp[1:])] for n, sp in modules.items()}
allr = [r for rs in ratios.values() for r in rs]
print("adjacent ratios:", {n: [round(r, 3) for r in rs] for n, rs in ratios.items()})
gm = 2 ** np.mean(np.log2(allr))
rng = np.random.default_rng(1)
animals = [n for n in ratios if ratios[n]]
boot = []
for _ in range(10000):
    pick = rng.choice(animals, size=len(animals), replace=True)
    rs = [r for n in pick for r in ratios[n]]
    boot.append(2 ** np.mean(np.log2(rs)))
lo, hi = np.percentile(boot, [2.5, 97.5])
p1 = (abs(gm - 2 ** 0.5) <= 0.07) or (abs(gm - 2) <= 0.07)
print(f"P1: {'not killed' if p1 else 'KILLED'}. pooled geometric-mean ratio {gm:.3f} over {len(allr)} ratios from "
      f"{len(animals)} animals (bootstrap over animals 95%: {lo:.3f}-{hi:.3f}); bands 1.344-1.484 and 1.93-2.07")
three = [n for n, sp in modules.items() if len(sp) >= 3]
d12 = [np.log2(modules[n][1] / modules[n][0]) - np.log2(modules[n][2] / modules[n][1]) for n in three]
print(f"P2: {'KILLED' if len(three) < 3 else ('not killed' if abs(np.mean(d12)) < 0.1 else 'KILLED')}. animals with three "
      f"modules: {len(three)} (needs 3); for information, log2 step difference {[round(v, 3) for v in d12]}")
two = [n for n, sp in modules.items() if len(sp) >= 2]
info3 = ""
if len(two) >= 2:
    info3 = (f"; for information, sd log2 lambda1 {np.std([np.log2(modules[n][0]) for n in two]):.3f}, "
             f"sd log2 ratio {np.std([np.log2(modules[n][1] / modules[n][0]) for n in two]):.3f}")
print(f"P3: {'KILLED' if len(two) < 5 else '(computed)'}. animals with two modules: {len(two)} (needs 5){info3}")
small = [r for r in allr if r < 1.2]
print(f"P4: {'not killed' if len(small) <= 0.05 * len(allr) else 'KILLED'}. adjacent pairs under 1.2: {len(small)} of {len(allr)}")
