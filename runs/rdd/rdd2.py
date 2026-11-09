"""RDD run 2: the full NVSS, its power stated first (plans/rdd-plan.md, "Run 2").
Run from the repository's root:  python3 runs/rdd/rdd2.py [/tmp/rdd_data/nvss.tsv]"""
import sys, time
import numpy as np, healpy as hp
from scipy import stats
from astropy.coordinates import SkyCoord
import astropy.units as u

T0 = time.time()
PATH = sys.argv[1] if len(sys.argv) > 1 else '/tmp/rdd_data/nvss.tsv'
NSIDE = 64
BETA_CMB = 1.2336e-3
CMB = (264.02, 48.25); CW_AXIS = (234.7, 42.2)
CW_BETA, CW_ERR = 3.31e-3, 0.27e-3 * 1.7
CW_R99 = 18.4 * 1.7
ALPHA = 0.75
rng = np.random.default_rng(20261109)
say = lambda *a: print(*a, flush=True)

ras, decs, S = [], [], []
with open(PATH) as f:
    for line in f:
        if not line.strip() or line[0] in '#-' or line.startswith('RAJ') or line.startswith('"h:m:s"'):
            continue
        p = line.rstrip('\n').split('\t')
        if len(p) < 3 or not p[2].strip():
            continue
        try:
            S.append(float(p[2]))
        except ValueError:
            continue
        ras.append(p[0]); decs.append(p[1])
S = np.array(S)
c = SkyCoord(ras, decs, unit=(u.hourangle, u.deg), frame='icrs')
dec = c.dec.deg
g = c.galactic; l, b = g.l.deg, g.b.deg
say(f'rows {len(S)}')

npix = hp.nside2npix(NSIDE)
th, ph = hp.pix2ang(NSIDE, np.arange(npix))
gl, gb = np.degrees(ph), 90 - np.degrees(th)
pdec = SkyCoord(l=gl * u.deg, b=gb * u.deg, frame='galactic').icrs.dec.deg
keep = (np.abs(gb) > 16) & (pdec > -39) & (pdec < 77)
say(f'kept pixels {keep.sum()} ({keep.mean():.3f} of the sky)')
pix = hp.ang2pix(NSIDE, l, b, lonlat=True)
srcok = (np.abs(b) > 15) & (dec > -40) & (dec < 78) & keep[pix]
vec = np.array(hp.pix2vec(NSIDE, np.arange(npix)))
regions = hp.ang2pix(2, th, ph)


def sep(p, q):
    return SkyCoord(l=p[0] * u.deg, b=p[1] * u.deg, frame='galactic').separation(
        SkyCoord(l=q[0] * u.deg, b=q[1] * u.deg, frame='galactic')).deg


def measure(sel):
    m = np.bincount(pix[sel], minlength=npix).astype(float)
    mono, dip = hp.fit_dipole(np.where(keep, m, hp.UNSEEN))
    a = np.linalg.norm(dip) / mono
    lon, lat = hp.vec2ang(dip / np.linalg.norm(dip), lonlat=True)
    model = mono + dip @ vec
    bs_a, bs_v = [], []
    for _ in range(400):
        mo, di = hp.fit_dipole(np.where(keep, rng.poisson(np.clip(model, 0, None)), hp.UNSEEN).astype(float))
        bs_a.append(np.linalg.norm(di) / mo); bs_v.append(di / np.linalg.norm(di))
    eb = np.std(bs_a)
    angs = np.degrees(np.arccos(np.clip(np.array(bs_v) @ (dip / np.linalg.norm(dip)), -1, 1)))
    jk = []
    for r in np.unique(regions[keep]):
        mo, di = hp.fit_dipole(np.where(keep & (regions != r), m, hp.UNSEEN))
        jk.append(np.linalg.norm(di) / mo)
    n = len(jk); ej = np.sqrt((n - 1) / n * np.sum((np.array(jk) - np.mean(jk)) ** 2))
    e = max(eb, ej)
    return dict(N=int(sel.sum()), D=a, axis=(float(lon[0]) % 360, float(lat[0])), eb=eb, ej=ej, e=e,
                r99=np.percentile(angs, 99) * e / eb)


def xslope(Sc, sel):
    f = np.sort(S[sel])
    s = np.exp(np.linspace(np.log(Sc / 1.25), np.log(Sc * 1.25), 21))
    N = len(f) - np.searchsorted(f, s, side='left')
    return -np.polyfit(np.log(s), np.log(N), 1)[0]


def xeff(S1, S2, sel):
    x1 = xslope(S1, sel)
    if S2 is None:
        return x1
    x2 = xslope(S2, sel)
    N1, N2 = (S[sel] >= S1).sum(), (S[sel] >= S2).sum()
    return (x1 * N1 - x2 * N2) / (N1 - N2)


base = srcok & (S >= 20)
say(f'sample >= 20 mJy in the mask: {base.sum()}')
W = measure(base)
x = xslope(20, base)
ex = {a: 2 + x * (1 + a) for a in (0.6, 0.75, 0.9)}
bw, ebw = W['D'] / ex[ALPHA], W['e'] / ex[ALPHA]
say(f"\nWhole sample: N {W['N']}  D {W['D']:.4f} +- {W['e']:.4f} (bootstrap {W['eb']:.4f}, jackknife {W['ej']:.4f})"
    f"  axis ({W['axis'][0]:.1f}, {W['axis'][1]:.1f})  99% radius {W['r99']:.1f}")
say(f"  x {x:.3f}; 2 + x(1+a) = {ex[0.6]:.3f}, {ex[0.75]:.3f}, {ex[0.9]:.3f} at a = 0.6, 0.75, 0.9")
say(f"  beta-hat {bw:.3e} +- {ebw:.3e} ({bw/BETA_CMB:.2f} x CMB; at a = 0.6 / 0.9: {W['D']/ex[0.6]/BETA_CMB:.2f} / {W['D']/ex[0.9]/BETA_CMB:.2f})")
say(f"  axis {sep(W['axis'], CMB):.1f} deg from CMB, {sep(W['axis'], CW_AXIS):.1f} from CatWISE")
powered = ebw < 1.0e-3
say(f"\nR6 (power): error {ebw:.2e} against 1.0e-3 -> {'powered' if powered else 'UNPOWERED: R1-R4 reported, not counted'}")

say('\nR1: flux slices')
bs, es = [], []
for S1, S2 in [(20, 40), (40, 80), (80, 160), (160, None)]:
    sel = base & (S >= S1) & ((S < S2) if S2 else True)
    M = measure(sel); xe = xeff(S1, S2, base); e_ = 2 + xe * (1 + ALPHA)
    bs.append(M['D'] / e_); es.append(M['e'] / e_)
    say(f"  {S1}-{S2 or 'up'} mJy: N {M['N']} x_eff {xe:.3f} D {M['D']:.4f} +- {M['e']:.4f} "
        f"(boot {M['eb']:.4f}, jk {M['ej']:.4f}) beta/CMB {bs[-1]/BETA_CMB:.2f} +- {es[-1]/BETA_CMB:.2f} "
        f"axis ({M['axis'][0]:.0f}, {M['axis'][1]:.0f}) {sep(M['axis'], CMB):.0f} from CMB")
w = 1 / np.array(es) ** 2; mb = np.sum(w * bs) / w.sum(); ch = np.sum(w * (np.array(bs) - mb) ** 2); p = stats.chi2.sf(ch, 3)
say(f"  one beta {mb:.3e} +- {1/np.sqrt(w.sum()):.3e}; chi2 {ch:.2f} on 3, p = {p:.3g} -> R1': {'KILLED' if p <= 0.01 else 'not killed'}")

z = abs(bw - CW_BETA) / np.hypot(ebw, CW_ERR)
say(f"\nR3': radio {bw:.3e} +- {ebw:.3e} vs CatWISE {CW_BETA:.3e} +- {CW_ERR:.3e}: {z:.2f} sigma -> {'KILLED' if z > 2.58 else 'not killed'}")
z0 = abs(bw - BETA_CMB) / ebw
say(f"  (reported, not scored) radio vs the CMB's beta: {z0:.2f} sigma")
s4 = sep(W['axis'], CW_AXIS); r4 = np.hypot(W['r99'], CW_R99)
say(f"R4': axis {s4:.1f} deg from CatWISE, combined 99% radius {r4:.1f} -> {'KILLED' if s4 > r4 else 'not killed'}")
say(f'\n{time.time()-T0:.0f} s')
