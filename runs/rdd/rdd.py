"""RDD run 1: the radio dipole sorted by the second test (plans/rdd-plan.md).

de Gasperin, Intema and Frail 2018's TGSS x NVSS spectral-index catalogue (VizieR J/MNRAS/474/5008/spidxcat).
Run from the repository's root:  python3 runs/rdd/rdd.py [/tmp/rdd_data/spidx.tsv]
Needs numpy, scipy, astropy, healpy. The data stay in /tmp/rdd_data.
"""
import sys, time
import numpy as np, healpy as hp
from scipy import stats
from astropy.coordinates import SkyCoord
import astropy.units as u

T0 = time.time()
PATH = sys.argv[1] if len(sys.argv) > 1 else '/tmp/rdd_data/spidx.tsv'
NSIDE = 64
BETA_CMB = 1.2336e-3
CMB = (264.02, 48.25)
CW_AXIS = (234.7, 42.2)
CW_BETA, CW_ERR = 3.31e-3, 0.27e-3 * 1.7
CW_R99 = 18.4 * 1.7
rng = np.random.default_rng(20261109)
say = lambda *a: print(*a, flush=True)

# ---- read
ra, dec, fn, si, sc = [], [], [], [], []
with open(PATH) as f:
    for line in f:
        if not line or line[0] in '#-' or line.startswith('RAJ') or line.startswith('deg'):
            continue
        p = line.rstrip('\n').split('\t')
        if len(p) < 5:
            continue
        try:
            r, d = float(p[0]), float(p[1])
        except ValueError:
            continue
        ra.append(r); dec.append(d)
        fn.append(float(p[2]) if p[2].strip() else np.nan)
        si.append(float(p[3]) if p[3].strip() else np.nan)
        sc.append(p[4].strip())
ra, dec, fn, si, sc = map(np.array, (ra, dec, fn, si, sc))
say(f'rows read {len(ra)}; codes', {c: int((sc == c).sum()) for c in 'SMCILU'})
alpha = -si
g = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame='icrs').galactic
l, b = g.l.deg, g.b.deg

# ---- mask: pixel centre and antipode both |b|>16, dec>-39
npix = hp.nside2npix(NSIDE)
th, ph = hp.pix2ang(NSIDE, np.arange(npix))
gl, gb = np.degrees(ph), 90 - np.degrees(th)
pc = SkyCoord(l=gl * u.deg, b=gb * u.deg, frame='galactic').icrs
pdec = pc.dec.deg
ok1 = (np.abs(gb) > 16) & (pdec > -39)
anti = hp.ang2pix(NSIDE, np.pi - th, ph + np.pi)
keep = ok1 & ok1[anti]
say(f'kept pixels {keep.sum()} of {npix} ({keep.mean():.3f} of the sky)')
srcok = (np.abs(b) > 15) & (np.abs(dec) < 40) & (sc != 'U')
pix = hp.ang2pix(NSIDE, l, b, lonlat=True)


def fit(sel):
    m = np.bincount(pix[sel], minlength=npix).astype(float)
    mm = np.where(keep, m, hp.UNSEEN)
    mono, dip = hp.fit_dipole(mm)
    return m, mono, dip


def amp_axis(mono, dip):
    a = np.linalg.norm(dip) / mono
    lon, lat = hp.vec2ang(dip / np.linalg.norm(dip), lonlat=True)
    return a, (float(lon[0]) % 360, float(lat[0]))


def sep(p, q):
    return SkyCoord(l=p[0] * u.deg, b=p[1] * u.deg, frame='galactic').separation(
        SkyCoord(l=q[0] * u.deg, b=q[1] * u.deg, frame='galactic')).deg


vec = np.array(hp.pix2vec(NSIDE, np.arange(npix)))
regions = hp.ang2pix(2, th, ph)


def measure(sel):
    m, mono, dip = fit(sel)
    a, ax = amp_axis(mono, dip)
    model = mono + dip @ vec
    # Poisson bootstrap
    bs_a, bs_v = [], []
    for _ in range(400):
        mb = np.where(keep, rng.poisson(np.clip(model, 0, None)), hp.UNSEEN).astype(float)
        mo, di = hp.fit_dipole(mb)
        bs_a.append(np.linalg.norm(di) / mo); bs_v.append(di / np.linalg.norm(di))
    eb = np.std(bs_a)
    v0 = dip / np.linalg.norm(dip)
    angs = np.degrees(np.arccos(np.clip(np.array(bs_v) @ v0, -1, 1)))
    # jackknife over nside-2 regions holding kept pixels
    regs = np.unique(regions[keep])
    jk = []
    for r in regs:
        k2 = keep & (regions != r)
        mm = np.where(k2, m, hp.UNSEEN)
        mo, di = hp.fit_dipole(mm)
        jk.append(np.linalg.norm(di) / mo)
    n = len(jk)
    ej = np.sqrt((n - 1) / n * np.sum((np.array(jk) - np.mean(jk)) ** 2))
    e = max(eb, ej)
    r99 = np.percentile(angs, 99) * (e / eb)
    return dict(N=int(sel.sum()), D=a, axis=ax, eb=eb, ej=ej, e=e, r99=r99)


grid = np.round(np.arange(0.01, 5.0, 0.01), 2)


def xslope(S, sel):
    f = fn[sel]
    s = grid[(grid >= S / 1.5 - 1e-9) & (grid <= 1.5 * S + 1e-9)]
    N = np.array([(f >= x - 1e-9).sum() for x in s])
    return -np.polyfit(np.log(s), np.log(N), 1)[0]


def xeff(S1, S2, sel):
    f = fn[sel]
    x1 = xslope(S1, sel)
    if S2 is None:
        return x1
    x2 = xslope(S2, sel)
    N1, N2 = (f >= S1 - 1e-9).sum(), (f >= S2 - 1e-9).sum()
    return (x1 * N1 - x2 * N2) / (N1 - N2)


def chi2_one(betas, errs):
    w = 1 / np.array(errs) ** 2
    m = np.sum(w * betas) / np.sum(w)
    c = np.sum(w * (np.array(betas) - m) ** 2)
    return m, np.sqrt(1 / np.sum(w)), c, stats.chi2.sf(c, len(betas) - 1)


base = srcok & (fn >= 0.02 - 1e-9) & keep[pix]
say(f'\nsample >= 0.02 Jy in the mask: {base.sum()}; alpha mean {np.nanmean(alpha[base]):.3f}; '
    f'TGSS limits (L) {np.sum(base & (sc == "L"))}')

say('\nWhole sample')
W = measure(base)
xw = xslope(0.02, base); aw = np.nanmean(alpha[base])
expw = 2 + xw * (1 + aw)
say(f"  N {W['N']}  D {W['D']:.4f} +- {W['e']:.4f} (bootstrap {W['eb']:.4f}, jackknife {W['ej']:.4f})  axis "
    f"({W['axis'][0]:.1f}, {W['axis'][1]:.1f})  99% radius {W['r99']:.1f} deg")
say(f"  x {xw:.3f}  alpha {aw:.3f}  2 + x(1+alpha) {expw:.3f}  expectation at CMB beta {expw*BETA_CMB:.4f}  "
    f"beta/beta_CMB {W['D']/expw/BETA_CMB:.2f}")
say(f"  axis from CMB {sep(W['axis'], CMB):.1f} deg, from CatWISE {sep(W['axis'], CW_AXIS):.1f} deg")

say('\nR1: flux slices')
edges = [(0.02, 0.04), (0.04, 0.08), (0.08, 0.16), (0.16, None)]
bs, es = [], []
say('  | S (Jy) | N | x_eff | alpha | 2 + x(1+a) | D | beta/beta_CMB | axis | from CMB |')
for S1, S2 in edges:
    sel = base & (fn >= S1 - 1e-9) & ((fn < S2 - 1e-9) if S2 else True)
    M = measure(sel); xe = xeff(S1, S2, base); am = np.nanmean(alpha[sel]); ex = 2 + xe * (1 + am)
    bh, eh = M['D'] / ex, M['e'] / ex
    bs.append(bh); es.append(eh)
    say(f"  | {S1}-{S2 or 'up'} | {M['N']} | {xe:.3f} | {am:.3f} | {ex:.3f} | {M['D']:.4f} +- {M['e']:.4f} | "
        f"{bh/BETA_CMB:.2f} +- {eh/BETA_CMB:.2f} | ({M['axis'][0]:.0f}, {M['axis'][1]:.0f}) | {sep(M['axis'], CMB):.0f} |")
m1, e1, c1, p1 = chi2_one(bs, es)
say(f'  one beta {m1:.3e} +- {e1:.3e} ({m1/BETA_CMB:.2f} x CMB); chi2 {c1:.2f} on {len(bs)-1}, p = {p1:.3g}')
say(f'  -> R1: {"KILLED" if p1 <= 0.01 else "not killed"}')

say('\nR2: colour terciles (alpha = -SpIndex), >= 0.02 Jy')
q = np.nanpercentile(alpha[base], [100 / 3, 200 / 3])
cb, ce = [], []
for lo, hi, name in [(-np.inf, q[0], 'flattest'), (q[0], q[1], 'middle'), (q[1], np.inf, 'steepest')]:
    sel = base & (alpha >= lo) & (alpha < hi)
    M = measure(sel); xe = xslope(0.02, sel); am = np.nanmean(alpha[sel]); ex = 2 + xe * (1 + am)
    bh, eh = M['D'] / ex, M['e'] / ex
    cb.append(bh); ce.append(eh)
    say(f"  {name}: alpha in [{lo:.3f}, {hi:.3f}) N {M['N']}  mean alpha {am:.3f}  x {xe:.3f}  D {M['D']:.4f} +- {M['e']:.4f}"
        f"  beta/CMB {bh/BETA_CMB:.2f} +- {eh/BETA_CMB:.2f}  axis ({M['axis'][0]:.0f}, {M['axis'][1]:.0f}), {sep(M['axis'], CMB):.0f} from CMB")
m2, e2, c2, p2 = chi2_one(cb, ce)
say(f'  chi2 {c2:.2f} on 2, p = {p2:.3g}  -> R2: {"KILLED" if p2 <= 0.01 else "not killed"}')

say('\nR3: one motion, two wavelengths')
z = abs(m1 - CW_BETA) / np.hypot(e1, CW_ERR)
say(f'  radio {m1:.3e} +- {e1:.3e}, CatWISE {CW_BETA:.3e} +- {CW_ERR:.3e}: {z:.2f} sigma  -> R3: {"KILLED" if z > 2.58 else "not killed"}')

say('\nR4: one axis')
s4 = sep(W['axis'], CW_AXIS); r4 = np.hypot(W['r99'], CW_R99)
say(f'  radio axis {s4:.1f} deg from CatWISE; combined 99% radius {r4:.1f}  -> R4: {"KILLED" if s4 > r4 else "not killed"}')

say(f'\nR5 (reported): whole sample beta/beta_CMB {W["D"]/expw/BETA_CMB:.2f}; axis {sep(W["axis"], CMB):.1f} deg from CMB')
say(f'\n{time.time()-T0:.0f} s')
