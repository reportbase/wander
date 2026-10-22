"""GDR run 1: GRD revisited. See plans/gdr-plan.md (predictions written first).

P2-P5 are exact (mpmath, 50 digits). P1 re-runs GRD run 1's method (runs/grd/grd.py, copied with the lengths made
parameters) on Gardner et al. 2022 (figshare 16764508 v6, CC0), with every tracked position scaled by k.
Run from the repository root:  python3 runs/gdr/gdr.py <unzipped Toroidal_topology_grid_cell_data dir>
"""
import sys, os, re, hashlib
import numpy as np
import mpmath as mp

mp.mp.dps = 50
out = []
def say(s=""):
    print(s); out.append(s)

# ---------------------------------------------------------------- P2: the turn's K addresses along scale
say("== P2: the turn's K addresses, boundaries H*tan(k*pi/2K), adjacent ratios ==")
SQ2 = mp.sqrt(2)
def turn_ratios(K):
    b = [mp.tan(k * mp.pi / (2 * K)) for k in range(1, K)]
    return [b[i + 1] / b[i] for i in range(len(b) - 1)]
def central(K):
    r = turn_ratios(K)
    m = len(r) // 2
    # the ratio at the corner: for even K the two either side of tan(pi/4)=1 (equal); for odd K the middle one
    return r[m] if len(r) % 2 == 1 else r[m - 1]
cands = sorted(range(6, 41), key=lambda K: abs(central(K) - SQ2))
say("K nearest sqrt2 at the corner: " + ", ".join(f"K={K} central {mp.nstr(central(K), 6)} (off {mp.nstr(central(K)-SQ2, 3)})" for K in cands[:4]))
p2 = set(cands[:2]) == {9, 10}
for K in (8, 9, 10, 11):
    r = turn_ratios(K)
    inb = [abs(x - SQ2) < mp.mpf('0.07') for x in r]
    run = best = 0
    for f in inb:
        run = run + 1 if f else 0; best = max(best, run)
    say(f"K={K}: ratios " + ", ".join(mp.nstr(x, 5) for x in r) + f"; longest run within 0.07 of sqrt2: {best}; outermost {mp.nstr(r[-1], 5)}")
    if K in (9, 10):
        p2 = p2 and best <= 4 and r[-1] > 2
# log-steps grow as cosh: at K=9, xi = ln tan(theta) at boundary, step/central
K = 9; b = [mp.tan(k * mp.pi / (2 * K)) for k in range(1, K)]
steps = [mp.log(b[i + 1] / b[i]) for i in range(len(b) - 1)]
say("K=9 log-steps over the central log-step: " + ", ".join(mp.nstr(s / min(steps), 4) for s in steps))
say(f"P2: {'not killed' if p2 else 'KILLED'}")

# ---------------------------------------------------------------- P3: counts across 0.3-10 m
say("\n== P3: modules to span 0.3-10 m (range 100/3), ends included ==")
R = mp.mpf(100) / 3
named = {'sqrt2': SQ2, '3/2': mp.mpf(3) / 2, 'sqrt e': mp.sqrt(mp.e), '1.7': mp.mpf('1.7'), '2': mp.mpf(2)}
want = {'sqrt2': 11, '3/2': 9, 'sqrt e': 8, '1.7': 7, '2': 6}
p3 = True
for n, r in named.items():
    steps = mp.log(R) / mp.log(r); N = 1 + int(mp.floor(steps))
    say(f"r={n} ({mp.nstr(r, 6)}): {mp.nstr(steps, 6)} steps, {N} modules (predicted {want[n]})")
    p3 = p3 and N == want[n]
Hm = mp.sqrt(mp.mpf('0.3') * 10)
bd = [Hm * mp.tan(k * mp.pi / 18) for k in range(1, 9)]
inside = sum(1 for x in bd if mp.mpf('0.3') <= x <= 10)
say(f"turn K=9, H = sqrt(0.3*10) = {mp.nstr(Hm, 6)} m: boundaries " + ", ".join(mp.nstr(x, 4) for x in bd) + f"; inside {inside} of 8")
say(f"   span of K=9's interior boundaries tan(80)/tan(10) = {mp.nstr(mp.tan(80*mp.pi/180)/mp.tan(10*mp.pi/180), 6)} against 100/3")
p3 = p3 and inside == 8
say(f"P3: {'not killed' if p3 else 'KILLED'}")

# ---------------------------------------------------------------- P4: steps needed to tell sqrt2 from the others
say("\n== P4: independent first steps n for 1.96*sigma/sqrt(n) < half the log2 distance from sqrt2 (sigma 0.045) ==")
sig = mp.mpf('0.045'); want4 = {'3/2': 5, 'sqrt e': 1, '1.7': 1, '2': 1}
p4 = True
for n_, r in named.items():
    if n_ == 'sqrt2': continue
    D = abs(mp.log(r, 2) - mp.mpf('0.5'))
    nmin = int(mp.floor((2 * mp.mpf('1.96') * sig / D) ** 2)) + 1
    say(f"{n_}: log2 distance {mp.nstr(D, 5)}, n >= {nmin} (predicted {want4[n_]})")
    p4 = p4 and nmin == want4[n_]
# for information: the turn layout vs constant sqrt2 at the step beyond the central four (K=9 boundary ratio 1.586)
D_turn = mp.log(turn_ratios(9)[-2], 2) - mp.mpf('0.5')
say(f"for information: K=9's step past the central three ({mp.nstr(turn_ratios(9)[-2], 5)}) sits {mp.nstr(D_turn, 4)} in log2 off sqrt2, n >= "
    f"{int(mp.floor((2*mp.mpf('1.96')*sig/D_turn)**2))+1} steps of that rank")
say(f"P4: {'not killed' if p4 else 'KILLED'}")

# ---------------------------------------------------------------- P5: area count vs the reader's lay
say("\n== P5: which count gives sqrt2 ==")
p5 = True
for d in (mp.mpf('0.5'), 1, 3, 100):
    # proportional plane: count within d is c*d^2; doubling ratio
    r = mp.sqrt(2 * d ** 2) / d
    say(f"(a) proportional plane, d={mp.nstr(d,3)}: doubling ratio {mp.nstr(r, 20)}"); p5 = p5 and abs(r - SQ2) < mp.mpf('1e-40')
rs = []
for s in (1, 2, 10, 100):
    s = mp.mpf(s)
    s2 = mp.e * s ** 2       # 1 + ln s' = 2(1 + ln s)
    rs.append(s2 / s)
    one_level = mp.exp(mp.log(s) + mp.log(2))   # count + n ln 2  <=> ln s' = ln s + ln 2
    say(f"(b) reader's lay, s={mp.nstr(s,4)}: count doubles at s'={mp.nstr(s2, 8)}, ratio {mp.nstr(s2/s, 8)}; one level more at ratio {mp.nstr(one_level/s, 20)}")
    p5 = p5 and abs(one_level / s - 2) < mp.mpf('1e-40')
p5 = p5 and len(set(mp.nstr(x, 10) for x in rs)) > 1
say("(c) equal addresses per level: the lay is along distance alone (1 + ln s per ray, any number of directions), so a level is ln s += ln 2: ratio 2 in the plane and the wedge alike")
say(f"P5: {'not killed' if p5 else 'KILLED'}")

# ---------------------------------------------------------------- P1: the data
say("\n== P1: GRD run 1's method with positions scaled by k ==")
if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
    say("P1: untested (no data directory given)")
else:
    D = sys.argv[1]
    SIGMA_OVER_BIN, MIN_OCC, MIN_OVERLAP = 1.0, 0.1, 20

    def sessions(txt):
        res = []
        for line in open(txt):
            m = re.match(r'\s*#\d+,\s*(\w+),\s*start=(\d+),\s*end=(\d+)(?:,\s*valid_times=\[(.*)\])?', line)
            if m:
                vt = None
                if m.group(4):
                    vt = [tuple(float(v) for v in w.split(',')) for w in m.group(4).split(';')]
                res.append((m.group(1), float(m.group(2)), float(m.group(3)), vt))
        return res

    def gauss_smooth(a, sb):
        r = int(np.ceil(4 * sb))
        kk = np.exp(-0.5 * (np.arange(-r, r + 1) / sb) ** 2); kk /= kk.sum()
        a = np.apply_along_axis(lambda v: np.convolve(v, kk, mode='same'), 0, a)
        return np.apply_along_axis(lambda v: np.convolve(v, kk, mode='same'), 1, a)

    def masked_autocorr(rate, valid):
        X = np.where(valid, rate, 0.0); M = valid.astype(float)
        ny, nx = X.shape; sy, sx = 2 * ny - 1, 2 * nx - 1
        F = lambda a: np.fft.rfft2(a, s=(sy, sx))
        def xc(a, b):
            return np.fft.fftshift(np.fft.irfft2(np.conj(F(a)) * F(b), s=(sy, sx)))
        N = np.rint(xc(M, M)); S1, S2 = xc(X, M), xc(M, X)
        S11, S22, S12 = xc(X * X, M), xc(M, X * X), xc(X, X)
        with np.errstate(invalid='ignore', divide='ignore'):
            r = (N * S12 - S1 * S2) / np.sqrt((N * S11 - S1 ** 2) * (N * S22 - S2 ** 2))
        r[N < MIN_OVERLAP] = np.nan
        return r

    def spacing_of(r, bin_size):
        cy, cx = (r.shape[0] - 1) // 2, (r.shape[1] - 1) // 2
        pad = np.pad(r, 1, constant_values=np.nan); peaks = []
        for y in range(r.shape[0]):
            for x in range(r.shape[1]):
                v = r[y, x]
                if not np.isfinite(v) or v <= 0 or (y == cy and x == cx): continue
                nb = pad[y:y + 3, x:x + 3].copy(); nb[1, 1] = -np.inf
                if np.all(~np.isfinite(nb) | (nb < v)):
                    peaks.append(np.hypot(y - cy, x - cx) * bin_size)
        if len(peaks) < 6: return None
        return float(np.median(sorted(peaks)[:6]))

    def rat_spacings(npz, sess_txt, k, bin_cm):
        z = np.load(npz, allow_pickle=True)
        x, y, t = z['x'].astype(float), z['y'].astype(float), z['t'].astype(float)
        of = [s for s in sessions(sess_txt) if s[0].startswith('open_field')][0]
        windows = of[3] if of[3] else [(of[1], of[2])]
        keep = np.zeros(t.shape, bool)
        for a, b in windows: keep |= (t >= a) & (t <= b)
        xs, ys, ts = x[keep], y[keep], t[keep]
        ok = np.isfinite(xs) & np.isfinite(ys); xs, ys, ts = xs[ok], ys[ok], ts[ok]
        unit = 100.0 if (np.nanmax(xs) - np.nanmin(xs)) < 10 else 1.0   # decided on the unscaled data, as run 1
        xs, ys = xs * unit * k, ys * unit * k
        dt = np.median(np.diff(ts))
        # bin edges laid as multiples of the bin from the minimum: index-exact under a common scale
        nxb = int(np.floor((np.max(xs) - np.min(xs)) / bin_cm + 1e-9)) + 2
        nyb = int(np.floor((np.max(ys) - np.min(ys)) / bin_cm + 1e-9)) + 2
        ex = np.min(xs) + bin_cm * np.arange(nxb); ey = np.min(ys) + bin_cm * np.arange(nyb)
        occ = np.histogram2d(ys, xs, bins=[ey, ex])[0] * dt
        occ_s = gauss_smooth(occ, SIGMA_OVER_BIN); valid = occ_s >= MIN_OCC
        res = {}
        for mk in sorted(kk for kk in z.keys() if kk.startswith('spikes_mod')):
            cells = z[mk].item(); sp = []
            for cid, st in cells.items():
                st = np.asarray(st, float); inw = np.zeros(st.shape, bool)
                for a, b in windows: inw |= (st >= a) & (st <= b)
                st = st[inw]
                if st.size == 0: continue
                sx, sy = np.interp(st, ts, xs), np.interp(st, ts, ys)
                cnt_s = gauss_smooth(np.histogram2d(sy, sx, bins=[ey, ex])[0], SIGMA_OVER_BIN)
                with np.errstate(invalid='ignore', divide='ignore'):
                    rate = cnt_s / occ_s
                g = spacing_of(masked_autocorr(rate, valid), bin_cm)
                if g is not None: sp.append(g)
            res[mk] = float(np.median(sp)) if sp else None
        return sorted(v for v in res.values() if v is not None)

    rats = [('Q', 'rat_q_grid_modules_1_2.npz', 'rat_q_sessions.txt'),
            ('R', 'rat_r_day1_grid_modules_1_2_3.npz', 'rat_r_day1_sessions.txt'),
            ('S', 'rat_s_grid_modules_1.npz', 'rat_s_sessions.txt')]
    def all_rats(k, bin_cm):
        return {n: rat_spacings(os.path.join(D, f), os.path.join(D, s), k, bin_cm) for n, f, s in rats}
    def first_steps_gm(m):
        r = [m['Q'][1] / m['Q'][0], m['R'][1] / m['R'][0]]
        return float(np.exp(np.mean(np.log(r)))), r
    base = all_rats(1.0, 2.5)
    gm0, r0 = first_steps_gm(base)
    say(f"k=1, bin 2.5 cm: " + "; ".join(f"{n} " + ", ".join(f'{v:.2f}' for v in sp) for n, sp in base.items())
        + f"; first steps {r0[0]:.4f}, {r0[1]:.4f}, gm {gm0:.4f}")
    say("   (bin edges here laid from the minimum by index, not np.arange as in run 1; run 1's values were Q 68.0, 95.0; R 56.2, 83.6, 118.0; S 54.7)")
    p1a = True
    for k in (0.5, 7.0):
        m = all_rats(k, 2.5 * k)
        devs = [abs(m[n][i] / (k * base[n][i]) - 1) for n in base for i in range(len(base[n]))]
        rdev = max(abs((m[n][i + 1] / m[n][i]) / (base[n][i + 1] / base[n][i]) - 1) for n in base for i in range(len(base[n]) - 1))
        say(f"(a) k={k}, bin {2.5*k} cm: max |spacing/(k*base) - 1| = {max(devs):.2e}; max relative ratio change {rdev:.2e}")
        p1a = p1a and max(devs) < 1e-9 and rdev < 1e-9
    p1b = True
    for k in (0.5, 2.0):
        m = all_rats(k, 2.5)
        gm, r = first_steps_gm(m)
        say(f"(b) k={k}, bin 2.5 cm fixed: " + "; ".join(f"{n} " + ", ".join(f'{v:.2f}' for v in sp) for n, sp in m.items())
            + f"; first steps {r[0]:.4f}, {r[1]:.4f}, gm {gm:.4f}, moved {gm - gm0:+.4f}")
        p1b = p1b and abs(gm - gm0) < 0.03
    say(f"P1: (a) {'not killed' if p1a else 'KILLED'}; (b) {'not killed' if p1b else 'KILLED'}")

with open(os.path.join('runs', 'gdr', 'gdr-run1.txt'), 'w') as f:
    f.write("\n".join(out) + "\n")
