"""RDD run 4's power forecast (plans/rdd-plan.md, "Run 4"), from NVSS counts alone; no RACS data read.
The joined sky's error on beta-hat, forecast as: the Poisson scatter of the fit on the joined mask (simulated),
times the jackknife-over-bootstrap ratio runs 2-3 measured on NVSS (1.45), over 2 + x(1 + alpha).
Run from the repository's root:  python3 runs/rdd/rdd4-forecast.py [/tmp/rdd_data/nvss.tsv]"""
import sys, numpy as np, healpy as hp
from astropy.coordinates import SkyCoord
import astropy.units as u
path = sys.argv[1] if len(sys.argv) > 1 else '/tmp/rdd_data/nvss.tsv'
ras, decs, S = [], [], []
for line in open(path):
    if not line.strip() or line[0] in '#-' or line.startswith('RAJ') or line.startswith('"h:m:s"'):
        continue
    f = line.rstrip('\n').split('\t')
    if len(f) < 3 or not f[2].strip():
        continue
    try:
        S.append(float(f[2]))
    except ValueError:
        continue
    ras.append(f[0]); decs.append(f[1])
S = np.array(S)
cc0 = SkyCoord(ras, decs, unit=(u.hourangle, u.deg), frame='icrs')
dec = cc0.dec.deg
NSIDE = 64; npix = hp.nside2npix(NSIDE)
th, ph = hp.pix2ang(NSIDE, np.arange(npix))
gl, gb = np.degrees(ph), 90 - np.degrees(th)
pdec = SkyCoord(l=gl * u.deg, b=gb * u.deg, frame='galactic').icrs.dec.deg
b = cc0.galactic.b.deg
nv = (np.abs(gb) > 16) & (pdec > -39) & (pdec < 77)          # runs 2-3's NVSS mask
area = nv.sum() * hp.nside2pixarea(NSIDE, degrees=True)
ok = (np.abs(b) > 16) & (dec > -39) & (dec < 77)
RATIO = 1.45            # runs 2-3: jackknife over bootstrap, NVSS (0.0058 / 0.0040)
ALPHA = 0.75
joined = (np.abs(gb) > 16) & (pdec < 77)                      # run 4's sky: NVSS north of -10, RACS-mid south
south = (pdec < -10).astype(float)
K = np.where(joined)[0]
vec = np.array(hp.pix2vec(NSIDE, np.arange(npix)))
X = np.column_stack([np.ones(len(K)), south[K], vec[0, K], vec[1, K], vec[2, K]])
rng = np.random.default_rng(4)
print(f'NVSS kept area {area:.0f} deg2; joined sky {joined.mean():.3f} of the sky')
for cut in (10, 15, 20):
    n = (ok & (S >= cut)).sum(); dens = n / area
    x = np.log(n / (ok & (S >= cut * 1.5)).sum()) / np.log(1.5)
    lam = dens * hp.nside2pixarea(NSIDE, degrees=True)
    Ntot = lam * len(K)
    amps = []
    for _ in range(300):
        m = rng.poisson(lam, len(K)).astype(float)
        cc, *_ = np.linalg.lstsq(X, m, rcond=None)
        amps.append(cc[2:] / cc[0])
    sig = np.sqrt(np.mean(np.var(np.array(amps), axis=0)))   # per component
    sD = sig
    sb = RATIO * sD / (2 + x * (1 + ALPHA))
    print(f'cut {cut} mJy: NVSS density {dens:.2f}/deg2, x {x:.3f}, joined N ~ {Ntot:,.0f}, '
          f'Poisson sigma(D) {sD:.4f}, forecast sigma(beta) {sb:.2e} '
          f'({"under" if sb < 1e-3 else "over"} 1.0e-3)')
