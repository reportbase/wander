"""RDD run 3: NVSS with its configurations modelled (plans/rdd-plan.md, "Run 3").
Run from the repository's root:  python3 runs/rdd/rdd3.py [/tmp/rdd_data/nvss.tsv]"""
import sys, numpy as np, healpy as hp
from scipy import stats
src = open('runs/rdd/rdd2.py').read().split("base = srcok & (S >= 20)")[0]
g = {}
exec(compile(src, 'rdd2.py', 'exec'), g)
S, srcok, keep, pix, npix, vec, regions, sep, say, rng = (g[k] for k in
    ('S', 'srcok', 'keep', 'pix', 'npix', 'vec', 'regions', 'sep', 'say', 'rng'))
xslope, xeff = g['xslope'], g['xeff']
B, CW_BETA, CW_ERR, CW_AXIS, CW_R99, CMB = (g[k] for k in ('BETA_CMB', 'CW_BETA', 'CW_ERR', 'CW_AXIS', 'CW_R99', 'CMB'))
import healpy as hp
from astropy.coordinates import SkyCoord
import astropy.units as u
th, ph = hp.pix2ang(64, np.arange(npix))
pdec = SkyCoord(l=np.degrees(ph) * u.deg, b=(90 - np.degrees(th)) * u.deg, frame='galactic').icrs.dec.deg
south = (pdec < -10).astype(float)
K = np.where(keep)[0]
X = np.column_stack([np.ones(len(K)), south[K], vec[0, K], vec[1, K], vec[2, K]])
say(f'kept pixels {len(K)}, of them below dec -10: {int(south[K].sum())}')


def lsq(m, idx=None):
    rows = np.arange(len(K)) if idx is None else idx
    c, *_ = np.linalg.lstsq(X[rows], m[K][rows], rcond=None)
    return c


def amp(c):
    d = c[2:]
    lon, lat = hp.vec2ang(d / np.linalg.norm(d), lonlat=True)
    return np.linalg.norm(d) / c[0], (float(lon[0]) % 360, float(lat[0])), d / np.linalg.norm(d)


def measure(sel):
    m = np.bincount(pix[sel], minlength=npix).astype(float)
    c = lsq(m); a, ax, v0 = amp(c)
    model = np.zeros(npix); model[K] = X @ c
    bs_a, angs = [], []
    for _ in range(400):
        mb = np.zeros(npix); mb[K] = rng.poisson(np.clip(model[K], 0, None))
        ab, _, vb = amp(lsq(mb)); bs_a.append(ab); angs.append(np.degrees(np.arccos(np.clip(vb @ v0, -1, 1))))
    eb = np.std(bs_a)
    reg = regions[K]; jk = []
    for r in np.unique(reg):
        jk.append(amp(lsq(m, np.where(reg != r)[0]))[0])
    n = len(jk); ej = np.sqrt((n - 1) / n * np.sum((np.array(jk) - np.mean(jk)) ** 2))
    e = max(eb, ej)
    return dict(N=int(sel.sum()), D=a, axis=ax, eb=eb, ej=ej, e=e, r99=np.percentile(angs, 99) * e / eb, step=c[1] / c[0])


base = srcok & (S >= 20)
W = measure(base)
x = xslope(20, srcok); ex = 2 + x * 1.75
bw, ebw = W['D'] / ex, W['e'] / ex
say(f"\nWhole: N {W['N']} D {W['D']:.4f} +- {W['e']:.4f} (boot {W['eb']:.4f}, jk {W['ej']:.4f}) axis ({W['axis'][0]:.1f}, {W['axis'][1]:.1f})"
    f" 99% {W['r99']:.1f}; step below -10: {W['step']:+.4f} of the monopole")
say(f"  x {x:.3f}, 2 + x(1.75) {ex:.3f}, beta-hat {bw:.3e} +- {ebw:.3e} ({bw/B:.2f} x CMB); axis {sep(W['axis'], CMB):.1f} from CMB, {sep(W['axis'], CW_AXIS):.1f} from CatWISE")
say(f"R6'': {ebw:.2e} vs 1.0e-3 -> {'powered' if ebw < 1e-3 else 'UNPOWERED: the rest reported, not counted'}")
bs, es = [], []
for S1, S2 in [(20, 40), (40, 80), (80, 160), (160, None)]:
    sel = base & (S >= S1) & ((S < S2) if S2 else True)
    M = measure(sel); xe = xeff(S1, S2, srcok); e = 2 + xe * 1.75
    bs.append(M['D'] / e); es.append(M['e'] / e)
    say(f"  {S1}-{S2 or 'up'}: N {M['N']} x_eff {xe:.3f} D {M['D']:.4f} +- {M['e']:.4f} beta/CMB {bs[-1]/B:.2f} +- {es[-1]/B:.2f} axis ({M['axis'][0]:.0f}, {M['axis'][1]:.0f})")
w = 1 / np.array(es) ** 2; mb = np.sum(w * bs) / w.sum(); ch = np.sum(w * (np.array(bs) - mb) ** 2); p = stats.chi2.sf(ch, 3)
say(f"R1'': one beta {mb/B:.2f} x CMB, chi2 {ch:.2f} on 3, p = {p:.3g} -> {'KILLED' if p <= 0.01 else 'not killed'}")
z = abs(bw - CW_BETA) / np.hypot(ebw, CW_ERR)
say(f"R3'': {z:.2f} sigma from CatWISE -> {'KILLED' if z > 2.58 else 'not killed'}; (reported) {abs(bw-B)/ebw:.2f} sigma from the CMB's")
s4 = sep(W['axis'], CW_AXIS); r4 = np.hypot(W['r99'], CW_R99)
say(f"R4'': {s4:.1f} deg from CatWISE, radius {r4:.1f} -> {'KILLED' if s4 > r4 else 'not killed'}")
