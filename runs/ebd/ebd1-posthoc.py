"""EBD run 1, post hoc (after the verdicts): why P4 missed, and how robust the P3 and P7 kills are.

Secrest et al.'s own recipe, read from their notebook (Resultscode.tar.gz, CatWISE_Dipole_Results.ipynb):
the mask at nside 1024 (|b| > 30 deg and the circles, one-sided), degraded to nside 64 keeping only pixels wholly
unmasked; the ecliptic trend fitted first (density against |ecliptic latitude|) and subtracted; then healpy's
remove_dipole (an unweighted linear fit of monopole and dipole). Nothing here changes a verdict.
Run:  python3 -I runs/ebd/ebd1-posthoc.py /tmp/ebd_data
"""
import sys
import numpy as np
import healpy as hp
from astropy.io import fits

DATA = sys.argv[1] if len(sys.argv) > 1 else '/tmp/ebd_data'
rng = np.random.default_rng(23)
t = fits.open(f'{DATA}/catwise_agns_masked_final_w1lt16p5_alpha.fits', memmap=True)[1].data
l = np.asarray(t['l'], float); b = np.asarray(t['b'], float); w1 = np.asarray(t['w1'], float)
alpha = -np.asarray(t['alpha_W1'], float)
mk = fits.open(f'{DATA}/MASKS_exclude_master_final.fits')[1].data
CMB = hp.ang2vec(264.02, 48.25, lonlat=True)
SEC = hp.ang2vec(238.2, 28.8, lonlat=True)


def ang(u, v):
    return np.degrees(np.arccos(np.clip(u @ v / np.linalg.norm(u) / np.linalg.norm(v), -1, 1)))


def lb(v):
    lo, la = hp.vec2ang(v / np.linalg.norm(v), lonlat=True)
    return lo[0] % 360, la[0]


def hires_mask(nside, symmetric):
    m = np.ones(hp.nside2npix(nside))
    _, pb = hp.pix2ang(nside, np.arange(len(m)), lonlat=True)
    m[np.abs(pb) < 30] = 0
    rot = hp.Rotator(coord=['C', 'G'])
    th, ph = rot(np.radians(90 - np.asarray(mk['dec'], float)), np.radians(np.asarray(mk['ra'], float)))
    for i in range(len(th)):
        v = hp.ang2vec(th[i], ph[i])
        m[hp.query_disc(nside, v, np.radians(mk['radius'][i]))] = 0
        if symmetric:
            m[hp.query_disc(nside, -v, np.radians(mk['radius'][i]))] = 0
    return m


NS = 64
pix = np.arange(hp.nside2npix(NS))
eth, _eph = hp.Rotator(coord=['G', 'E'])(*hp.pix2ang(NS, pix))
pelat = 90 - np.degrees(eth)
masks = {}
for sym in (False, True):
    lo = hp.ud_grade(hires_mask(1024, sym), nside_out=NS)
    masks[sym] = lo == 1
psrc = hp.ang2pix(NS, l, b, lonlat=True)


def run(sel, m, ecl='subtract', nboot=200):
    c = np.bincount(psrc[sel], minlength=len(pix)).astype(float)

    def one(c):
        y = c.copy()
        if ecl == 'subtract':
            k = np.polyfit(np.abs(pelat[m]), y[m], 1)[0]
            y = y - k * np.abs(pelat)
        mm = y.copy(); mm[~m] = hp.UNSEEN
        mono, dip = hp.fit_dipole(mm)
        return dip / mono

    d = one(c)
    bs = []
    lam = np.clip(c, 0, None)
    for _ in range(nboot):
        cc = c.copy(); cc[m] = rng.poisson(lam[m])
        bs.append(one(cc))
    bs = np.array(bs)
    return d, np.std(np.linalg.norm(bs, axis=1)), np.percentile([ang(x, d) for x in bs], 99)


base = (w1 > 9) & (w1 < 16.4)
print("Secrest's recipe (one-sided, wholly unmasked nside-64 pixels, ecliptic trend subtracted, fit_dipole):")
for sym in (False, True):
    m = masks[sym]
    sel = base & m[psrc]
    for ecl in ('subtract', 'none'):
        d, sd, r99 = run(sel, m, ecl)
        L, B = lb(d)
        print(f'  {"symmetric" if sym else "one-sided"}, ecliptic {ecl:8s}: N={sel.sum():,} pixels {m.sum():,} '
              f'D={np.linalg.norm(d):.5f}+-{sd:.5f} at ({L:.1f}, {B:.1f}); {ang(d, SEC):.1f} deg from Secrest\'s, '
              f'{ang(d, CMB):.1f} from the CMB, 99% radius {r99:.1f}')

print('\nP7 again on this recipe (one-sided, ecliptic subtracted): alpha terciles')
m = masks[False]
sel0 = base & m[psrc]
qs = np.quantile(alpha[sel0], [1/3, 2/3])
for lo_, hi_ in [(-np.inf, qs[0]), (qs[0], qs[1]), (qs[1], np.inf)]:
    s = sel0 & (alpha > lo_) & (alpha <= hi_)
    d, sd, _ = run(s, m, 'subtract', 150)
    L, B = lb(d)
    print(f'  alpha {lo_:.2f}..{hi_:.2f}: N={s.sum():,} D={np.linalg.norm(d):.5f}+-{sd:.5f} at ({L:.0f}, {B:.0f}), '
          f'{ang(d, CMB):.0f} deg from the CMB')

print('\nP7: the reddest tercile split by W1 (is it the faint end?)')
s3 = sel0 & (alpha > qs[1])
for lo_, hi_ in [(9, 15.5), (15.5, 16.0), (16.0, 16.4)]:
    s = s3 & (w1 > lo_) & (w1 < hi_)
    d, sd, _ = run(s, m, 'subtract', 100)
    L, B = lb(d)
    print(f'  W1 {lo_}-{hi_}: N={s.sum():,} D={np.linalg.norm(d):.5f}+-{sd:.5f} at ({L:.0f}, {B:.0f})')
