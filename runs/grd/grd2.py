"""GRD run 2: the ratio between grid modules, on Waaga, Agmon, Normand et al. 2022 (Zenodo 6200517, CC BY 4.0).
See plans/grd-plan.md, "Run 2, plan". Run 1's rate map, autocorrelogram and spacing, copied unchanged from grd.py.
Reads the dataset's MATLAB files with scipy.io.loadmat (the .npy files would need unpickling).
Run: python3 -I runs/grd/grd2.py <dir with the matlab_format .mat files>
"""
import sys, os, re, glob
import numpy as np
from scipy.io import loadmat
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

def spacings(path, task):
    d = loadmat(path, simplify_cells=True)['dataset']
    T = d['task'][task]; tr = T['tracking']
    u = str(T.get('tracking_units', '')).lower().strip()
    x, y, t = (np.asarray(tr[k], float).ravel() for k in ('x', 'y', 'timestamp'))
    ok = np.isfinite(x) & np.isfinite(y) & np.isfinite(t); x, y, t = x[ok], y[ok], t[ok]
    if u in ('cm', 'centimeter', 'centimeters', 'centimetre', 'centimetres'): f = 1.0
    elif u in ('m', 'meter', 'meters', 'metre', 'metres'): f = 100.0
    else: f = 100.0 if (x.max() - x.min()) < 10 else 1.0
    x, y = x * f, y * f
    dt = np.median(np.diff(t))
    ex = np.arange(x.min(), x.max() + BIN_CM, BIN_CM); ey = np.arange(y.min(), y.max() + BIN_CM, BIN_CM)
    occ_s = gauss_smooth(np.histogram2d(y, x, bins=[ey, ex])[0] * dt, SIGMA_CM / BIN_CM)
    valid = occ_s >= MIN_OCC
    side = min(x.max() - x.min(), y.max() - y.min())
    st_all = np.asarray(T['spike_timestamp'], float).ravel(); cid = np.asarray(T['spike_cluster_id']).ravel()
    uid = np.asarray(d['unit_id']).ravel(); mid = np.asarray(d['module_id']).ravel()
    mods = {}
    for c, m in zip(uid, mid):
        st = st_all[cid == c]; st = st[(st >= t[0]) & (st <= t[-1])]
        mods.setdefault(int(m), [0, []]); mods[int(m)][0] += 1
        if st.size == 0: continue
        cnt = gauss_smooth(np.histogram2d(np.interp(st, t, y), np.interp(st, t, x), bins=[ey, ex])[0], SIGMA_CM / BIN_CM)
        with np.errstate(invalid='ignore', divide='ignore'): rate = cnt / occ_s
        s = spacing_of(masked_autocorr(rate, valid), BIN_CM)
        if s is not None: mods[int(m)][1].append(s)
    res = sorted((float(np.median(v[1])), k, v[0], len(v[1])) for k, v in mods.items() if v[1])
    return res, side, u, T.get('name', task), f

def run(task, which):
    out = {}
    for rat, p in which.items():
        res, side, u, tn, f = spacings(p, task)
        kept = [r[0] for r in res if r[0] <= 0.6 * side]
        print(f"rat {rat} {os.path.basename(p)}: task '{tn}', units '{u}' (x{f:g} to cm), side {side:.0f} cm; " +
              "; ".join(f"module {k}: {n} of {N} cells, {s:.1f} cm" + ("" if s <= 0.6 * side else " (over 0.6 side, left out)")
                        for s, k, N, n in res))
        out[rat] = kept
    return out
def ratios(mods): return {n: [b / a for a, b in zip(sp, sp[1:])] for n, sp in mods.items()}
def pooled(rs):
    allr = [r for v in rs.values() for r in v]; animals = [n for n in rs if rs[n]]
    gm = 2 ** np.mean(np.log2(allr)); rng = np.random.default_rng(1); boot = []
    for _ in range(10000):
        pick = rng.choice(animals, size=len(animals), replace=True)
        boot.append(2 ** np.mean(np.log2([r for n in pick for r in rs[n]])))
    return gm, np.percentile(boot, [2.5, 97.5]), allr, animals

files = sorted(glob.glob(os.path.join(D, '*.mat')))
first = {}
for p in files: first.setdefault(re.search(r'waaga_(\d+)_', p).group(1), p)
print("== light, scored ==")
L = run(1, first); R = ratios(L)
print("adjacent ratios:", {n: [round(r, 3) for r in v] for n, v in R.items()})
gm, (lo, hi), allr, an = pooled(R)
p1 = abs(gm - 2 ** .5) <= .07 or abs(gm - 2) <= .07
print(f"P1b: {'not killed' if p1 else 'KILLED'}. pooled {gm:.3f} over {len(allr)} ratios, {len(an)} rats (bootstrap 95% {lo:.3f}-{hi:.3f}); bands 1.344-1.484, 1.93-2.07")
three = [n for n, s in L.items() if len(s) >= 3]
d = [np.log2(L[n][1] / L[n][0]) - np.log2(L[n][2] / L[n][1]) for n in three]
p2 = len(three) >= 3 and abs(np.mean(d)) < 0.1
print(f"P2b: {'not killed' if p2 else 'KILLED'}. rats with three kept modules: {len(three)} (needs 3); step differences {[round(float(v), 3) for v in d]}"
      + (f", mean {np.mean(d):.3f}" if d else ""))
G = {'Q': [68.0, 95.0], 'R': [56.2, 83.6]}   # run 1's kept modules (R's third, 118 of a 147 cm side, left out by the 0.6 rule)
two = {n: s for n, s in L.items() if len(s) >= 2}
def p3(m): return (np.std([np.log2(s[0]) for s in m.values()]), np.std([np.log2(s[1] / s[0]) for s in m.values()]))
both = {**two, **G}; a, b = p3(both)
print(f"P3b: {'KILLED' if len(both) < 5 or a <= b else 'not killed'}. {len(both)} animals (needs 5); sd log2 lambda1 {a:.3f}, sd log2 ratio {b:.3f}"
      + (f"; Waaga alone ({len(two)}): {p3(two)[0]:.3f}, {p3(two)[1]:.3f}" if len(two) >= 2 else ""))
small = [r for r in allr if r < 1.2]
print(f"P4b: {'not killed' if len(small) <= .05 * len(allr) else 'KILLED'}. adjacent ratios under 1.2: {len(small)} of {len(allr)}")
gm2, (lo2, hi2), a2, an2 = pooled({**R, 'Q': [95.0 / 68.0], 'R': [83.6 / 56.2]})
print(f"reported: both datasets {gm2:.3f} over {len(a2)} ratios, {len(an2)} rats (bootstrap 95% {lo2:.3f}-{hi2:.3f})")
print("== dark, reported ==")
print({n: [round(r, 3) for r in v] for n, v in ratios(run(0, first)).items()})
rest = {re.search(r'waaga_(\d+_\d{4}-\d\d-\d\d)', p).group(1): p for p in files if p not in first.values()}
print("== other sessions, light, reported ==")
print({n: [round(r, 3) for r in v] for n, v in ratios(run(1, rest)).items()})
