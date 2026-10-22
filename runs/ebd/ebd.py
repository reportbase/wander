"""EBD run 1: the Ellis-Baldwin dipole as addresses and payload (plans/ebd-plan.md).

Part A is exact (mpmath, 50 digits): P1, P2.
Part B is the CatWISE2020 quasars of Secrest et al. 2021 (Zenodo 8303800): P3-P8.
Run from the repository's root:  python3 runs/ebd/ebd.py [/tmp/ebd_data]
Needs numpy, scipy, mpmath, astropy, healpy. The data stay in /tmp/ebd_data.
"""
import sys, time
import numpy as np
import mpmath as mp

mp.mp.dps = 50
T0 = time.time()
DATA = sys.argv[1] if len(sys.argv) > 1 else '/tmp/ebd_data'
BETA_CMB = mp.mpf('1.2336e-3')
L_CMB, B_CMB = 264.02, 48.25


def say(*a):
    print(*a, flush=True)


def verdict(name, killed, why):
    say(f'  -> {name}: {"KILLED" if killed else "not killed"} ({why})')


# ---------------------------------------------------------------- Part A: exact
say('=== Part A: exact (mpmath, 50 digits) ===')

# P1: the 2 is the addresses'
say('\nP1. No flux limit: the seen density D^2/4pi; 3<cos> closed form and series')
worst = mp.mpf(0)
worst_series = mp.mpf(0)
for b in ['1e-3', '1.2336e-3', '0.1', '0.6', '0.99']:
    be = mp.mpf(b)
    closed = 3 / be - 3 * (1 - be**2) / (2 * be**2) * mp.log((1 + be) / (1 - be))
    # (i) over sources uniform in their own frame: cos th' = (c + b)/(1 + b c)
    qa = 3 * mp.quad(lambda c: (c + be) / (1 + be * c), [-1, 0, 1]) / 2
    # (ii) over the seen sky with density D^2/(4 pi), azimuth integrated: (1/2) D^2 dmu'
    D2 = lambda mu: (1 - be**2) / (1 - be * mu)**2
    norm = mp.quad(lambda mu: D2(mu) / 2, [-1, 0, 1])
    qb = 3 * mp.quad(lambda mu: mu * D2(mu) / 2, [-1, 0, 1])
    e = max(abs(qa - closed), abs(qb - closed), abs(norm - 1))
    worst = max(worst, e)
    line = f'  beta={b:>10}: 3<cos> = {mp.nstr(closed, 20)}  (2beta = {mp.nstr(2*be, 12)}); quadrature miss {mp.nstr(e, 3)}; norm-1 {mp.nstr(norm-1, 3)}'
    if b in ('1e-3', '1.2336e-3'):
        ser = mp.fsum(6 * be**(2*m + 1) / ((2*m + 1) * (2*m + 3)) for m in range(40))
        three = 2*be + mp.mpf(2)/5*be**3 + mp.mpf(6)/35*be**5
        es = abs(ser - closed)
        worst_series = max(worst_series, es)
        line += f'; 40-term series miss {mp.nstr(es, 3)}; first three terms miss {mp.nstr(abs(three-closed), 3)}'
    say(line)
verdict('P1', worst > mp.mpf('1e-40') or worst_series > mp.mpf('1e-40'),
        f'worst quadrature miss {mp.nstr(worst, 3)}, series {mp.nstr(worst_series, 3)}')
say('  P1 series clause as first written (three terms to 1e-40): killed by my set-up, as recorded before the run.')

# P2: the flux limit is the payload's
say('\nP2. Flux limit: density D^(2+x(1+a)), built independently from the aberration Jacobian and I_nu/nu^3 invariance')


def jac(be, mu):
    """d(mu_rest)/d(mu_seen) of the aberration map, numerically: the solid-angle ratio dOmega/dOmega'."""
    return mp.diff(lambda m: (m - be) / (1 - be * m), mu)


worst2 = mp.mpf(0)
worst_col = mp.mpf(0)
mus = [mp.mpf(k) / 10 for k in range(-9, 10, 3)]
for b in ['1.2336e-3', '0.1']:
    be = mp.mpf(b)
    for x in ['1', '1.5', '1.7', '2.5']:
        for a in ['0', '0.75', '1.26']:
            x_, a_ = mp.mpf(x), mp.mpf(a)
            for mu in mus:
                J = jac(be, mu)                       # dOmega_rest/dOmega_seen
                Dd = mp.sqrt(1 - be**2) / (1 - be * mu)
                nu = mp.mpf('8.9e13')
                S_rest = lambda f: f**(-a_)           # S_nu in the source frame, A = 1
                # point source: I_nu/nu^3 invariant, solid angle of the source scaled by dOmega'/dOmega = 1/J
                S_seen = lambda f: Dd**3 * S_rest(f / Dd) / J
                ratio = S_seen(nu) / S_rest(nu)       # = D^(1+a) if all is right
                dens = J * ratio**x_                  # seen count above a fixed S_cut per seen solid angle
                e = abs(dens / Dd**(2 + x_ * (1 + a_)) - 1)
                worst2 = max(worst2, e)
                c0 = S_rest(nu) / S_rest(nu * mp.mpf('1.3729'))
                c1 = S_seen(nu) / S_seen(nu * mp.mpf('1.3729'))
                worst_col = max(worst_col, abs(c1 / c0 - 1))
say(f'  worst miss of the density against D^(2+x(1+a)): {mp.nstr(worst2, 3)}; colour moved by {mp.nstr(worst_col, 3)}')


def dip(be, rho):
    n = mp.quad(lambda mu: rho(mu), [-1, 0, 1])
    return 3 * mp.quad(lambda mu: mu * rho(mu), [-1, 0, 1]) / n


worst_rel = mp.mpf(0)
for b in ['1.2336e-3', '0.1']:
    be = mp.mpf(b)
    Df = lambda mu: mp.sqrt(1 - be**2) / (1 - be * mu)
    x0, k, a = mp.mpf('1.7'), mp.mpf('0.5'), mp.mpf('1.26')
    p = 2 + x0 * (1 + a)
    pure = dip(be, lambda mu: Df(mu)**p)
    def curved(mu):
        w = (1 + a) * mp.log(Df(mu))
        return Df(mu)**2 * mp.exp(x0 * w - k * w**2 / 2)
    cd = dip(be, curved)
    rp = abs(pure - p * be) / (p * be)
    rc = abs(cd - p * be) / (p * be)
    worst_rel = max(worst_rel, rc / be**2)
    say(f'  beta={b}: p = {mp.nstr(p, 6)}; first order {mp.nstr(p*be, 10)}; pure power law {mp.nstr(pure, 10)} '
        f'(rel {mp.nstr(rp, 3)} = {mp.nstr(rp/be**2, 4)} beta^2); curved {mp.nstr(cd, 10)} (rel {mp.nstr(rc, 3)} = {mp.nstr(rc/be**2, 4)} beta^2)')
    # the 2 at different cuts: aberration alone, no flux limit
    say(f'    no flux limit at this beta: {mp.nstr(dip(be, lambda mu: Df(mu)**2), 10)} (2beta = {mp.nstr(2*be, 10)})')
verdict('P2', worst2 > mp.mpf('1e-40') or worst_col > mp.mpf('1e-40') or worst_rel > 10,
        f'density {mp.nstr(worst2, 3)}, colour {mp.nstr(worst_col, 3)}, curved count worst {mp.nstr(worst_rel, 4)} beta^2 (limit 10)')
say(f'  [part A {time.time()-T0:.1f} s]')

# ---------------------------------------------------------------- Part B: data
say('\n=== Part B: CatWISE2020 quasars (Secrest et al. 2021, Zenodo 8303800) ===')
import healpy as hp
from astropy.io import fits
from scipy import stats

NSIDE = 64
NPIX = hp.nside2npix(NSIDE)
rng = np.random.default_rng(22)

t = fits.open(f'{DATA}/catwise_agns_masked_final_w1lt16p5_alpha.fits', memmap=True)[1].data
l = np.asarray(t['l'], float); b = np.asarray(t['b'], float)
w1 = np.asarray(t['w1'], float); w2 = np.asarray(t['w2'], float)
alpha = -np.asarray(t['alpha_W1'], float)
say(f'rows {len(l):,}; |b| min {np.abs(b).min():.3f}; W1 {w1.min():.2f}..{w1.max():.2f}; W1-W2 min {(w1-w2).min():.3f}; '
    f'mean alpha (all rows) {alpha.mean():.4f}')
# alpha from the colour, as a cross-check of their column
F1, F2, L1, L2 = 309.540, 171.787, 3.3526, 4.6028
alpha_col = np.log((F2 * 10**(-0.4 * w2)) / (F1 * 10**(-0.4 * w1))) / np.log(L2 / L1)
say(f'alpha from W1-W2 with Vega zero points: mean {alpha_col.mean():.4f}; median |difference from their column| '
    f'{np.median(np.abs(alpha_col-alpha)):.4f}')

pix_src = hp.ang2pix(NSIDE, l, b, lonlat=True)
vx, vy, vz = hp.pix2vec(NSIDE, np.arange(NPIX))
V = np.vstack([vx, vy, vz]).T
pl, pb = hp.pix2ang(NSIDE, np.arange(NPIX), lonlat=True)

# ecliptic latitude of pixel centres (galactic -> ecliptic)
rot_ge = hp.Rotator(coord=['G', 'E'])
el_th, el_ph = rot_ge(*hp.pix2ang(NSIDE, np.arange(NPIX)))
pelat = 90.0 - np.degrees(el_th)

# masks
mk = fits.open(f'{DATA}/MASKS_exclude_master_final.fits')[1].data
rot_cg = hp.Rotator(coord=['C', 'G'])
th_c, ph_c = rot_cg(np.radians(90 - np.asarray(mk['dec'], float)), np.radians(np.asarray(mk['ra'], float)))
cvec = hp.ang2vec(th_c, ph_c)
crad = np.radians(np.asarray(mk['radius'], float))
say(f'mask circles {len(crad)}; radius {np.degrees(crad).min():.3f}..{np.degrees(crad).max():.3f} deg; '
    f'ba < 1 for {(np.asarray(mk["ba"]) < 1).sum()}')
cosang = V @ cvec.T                          # pixels x circles
in_circ = (cosang > np.cos(crad)).any(1)
in_anti = (-cosang > np.cos(crad)).any(1)
gal = np.abs(pb) > 30.0
mask_sym = gal & ~in_circ & ~in_anti
mask_one = gal & ~in_circ
# sources inside circles (is the catalogue already masked at source level?)
svec = hp.ang2vec(l, b, lonlat=True)
inside = np.zeros(len(l), bool)
for i in range(len(crad)):
    inside |= (svec @ cvec[i]) > np.cos(crad[i])
say(f'sources inside a mask circle: {inside.sum():,}; pixels kept: symmetric {mask_sym.sum():,} '
    f'({mask_sym.mean():.4f} of the sky), one-sided {mask_one.sum():,}')


def fit(counts, m, ecl=True):
    """Least squares N_p = A + (A d).n_p [+ e(|elat_p| - mean)] over pixels in m. Returns d (3-vector), A."""
    cols = [np.ones(m.sum()), V[m, 0], V[m, 1], V[m, 2]]
    if ecl:
        ae = np.abs(pelat[m]); cols.append(ae - ae.mean())
    X = np.vstack(cols).T
    coef, *_ = np.linalg.lstsq(X, counts[m], rcond=None)
    return coef[1:4] / coef[0], coef[0], X, coef


def lb(vec):
    th, ph = hp.vec2ang(vec / np.linalg.norm(vec))
    return np.degrees(ph[0]) % 360, 90 - np.degrees(th[0])


CMB = hp.ang2vec(L_CMB, B_CMB, lonlat=True)


def angle(u, v):
    return np.degrees(np.arccos(np.clip(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v), -1, 1)))


def boot(counts, m, ecl=True, n=400):
    d, A, X, coef = fit(counts, m, ecl)
    model = X @ coef
    model = np.clip(model, 0, None)
    out = []
    full = np.zeros(NPIX)
    for _ in range(n):
        full[m] = rng.poisson(model)
        out.append(fit(full, m, ecl)[0])
    return d, np.array(out)


def jack(counts, m, ecl=True):
    base = hp.ring2nest(NSIDE, np.arange(NPIX)) // (NSIDE * NSIDE)   # 12 base pixels
    ds = []
    for r in range(12):
        mm = m & (base != r)
        ds.append(fit(counts, mm, ecl)[0])
    ds = np.array(ds)
    amps = np.linalg.norm(ds, axis=1)
    return np.sqrt(11 / 12 * ((amps - amps.mean())**2).sum())


def xslope(mag_sel, cut, half=0.1):
    """x = dlog10 N(<m)/(0.4 dm) at m = cut, from N(<cut-half) and N(<cut+half)."""
    n_lo = (mag_sel < cut - half).sum(); n_hi = (mag_sel < cut + half).sum()
    return np.log10(n_hi / n_lo) / (0.4 * 2 * half), n_lo, n_hi


keep_pix = mask_sym[pix_src]
base_sel = keep_pix & (w1 > 9) & (w1 < 16.4)
counts = np.bincount(pix_src[base_sel], minlength=NPIX).astype(float)
N = base_sel.sum()
say(f'\nsample 9 < W1 < 16.4 in the symmetric mask: N = {N:,}')

say('\nThe full-sample dipole, four ways (amplitude, direction, angle from the CMB):')
res = {}
for name, m, ecl in [('symmetric + ecliptic', mask_sym, True), ('symmetric, no ecliptic', mask_sym, False),
                     ('one-sided + ecliptic', mask_one, True), ('one-sided, no ecliptic', mask_one, False)]:
    sel = m[pix_src] & (w1 > 9) & (w1 < 16.4)
    c = np.bincount(pix_src[sel], minlength=NPIX).astype(float)
    d, bs = boot(c, m, ecl)
    amp = np.linalg.norm(d); sd = np.std(np.linalg.norm(bs, axis=1))
    angs = np.array([angle(x_, d) for x_ in bs])
    r99 = np.percentile(angs, 99)
    jk = jack(c, m, ecl)
    L_, B_ = lb(d)
    res[name] = (d, amp, sd, r99, jk, sel.sum())
    say(f'  {name:24s} N={sel.sum():,}  D = {amp:.5f} +- {sd:.5f} (boot), +- {jk:.5f} (jackknife); '
        f'(l, b) = ({L_:.1f}, {B_:.1f}); {angle(d, CMB):.1f} deg from the CMB; 99% boot radius {r99:.1f} deg; '
        f'68% {np.percentile(angs, 68):.1f} deg')

d0, amp0, sd0, r990, jk0, _ = res['symmetric + ecliptic']
ang0 = angle(d0, CMB)
say('\nP3. The direction against the CMB dipole')
verdict('P3', ang0 > r990, f'{ang0:.1f} deg from the CMB against a 99% bootstrap radius of {r990:.1f} deg')

# x and alpha at the cut
alpha_s = alpha[base_sel]
x0, nlo, nhi = xslope(w1[keep_pix & (w1 > 9)], 16.4)
abar = alpha_s.mean()
p0 = 2 + x0 * (1 + abar)
xa_src = np.mean(x0 * (1 + alpha_s))
Dkin = p0 * float(BETA_CMB)
say(f'\nx at W1 = 16.4: {x0:.4f} (N(<16.3) = {nlo:,}, N(<16.5) = {nhi:,}); mean alpha {abar:.4f} '
    f'(median {np.median(alpha_s):.4f}); mean x(1+alpha) per source {xa_src:.4f}')
say(f'expected D_kin = [2 + x(1+alpha)] beta = [2 + {x0*(1+abar):.4f}] x {float(BETA_CMB):.4e} = {Dkin:.5f}; '
    f'aberration part 2beta = {2*float(BETA_CMB):.5f} ({2/p0:.3f} of it), payload part {x0*(1+abar)*float(BETA_CMB):.5f}')
say(f'measured / expected = {amp0/Dkin:.3f}; excess over the kinematic expectation {(amp0-Dkin)/sd0:.2f} bootstrap sigma '
    f'(amplitude only)')

say('\nP4. My set-up against Secrest et al. 2021 (a check of my set-up, not of the framing)')
Ls, Bs = lb(d0)
sec = hp.ang2vec(238.2, 28.8, lonlat=True)
checks = [('amplitude within 15% of 0.01554', abs(amp0 / 0.01554 - 1) <= 0.15, f'{amp0:.5f}'),
          ('axis within 10 deg of (238.2, 28.8)', angle(d0, sec) <= 10, f'{angle(d0, sec):.1f} deg'),
          ('x within 0.1 of 1.7', abs(x0 - 1.7) <= 0.1, f'{x0:.3f}'),
          ('mean alpha within 0.05 of 1.26', abs(abar - 1.26) <= 0.05, f'{abar:.3f}'),
          ('expectation within 5% of 0.0072', abs(Dkin / 0.0072 - 1) <= 0.05, f'{Dkin:.5f}')]
for c_, ok, v in checks:
    say(f'  {c_}: {v} {"ok" if ok else "MISSED"}')
verdict('P4', not all(ok for _, ok, _ in checks), 'all five' if all(ok for _, ok, _ in checks) else 'see the misses')

say('\nP5. Every flux and the cut times one factor (W1, W2 and the cut all -0.37 mag)')
sh = 0.37
keep2 = keep_pix & (w1 - sh > 9 - sh) & (w1 - sh < 16.4 - sh)
x0b, _, _ = xslope((w1 - sh)[keep_pix & (w1 - sh > 9 - sh)], 16.4 - sh)
ac2 = np.log((F2 * 10**(-0.4 * (w2 - sh))) / (F1 * 10**(-0.4 * (w1 - sh)))) / np.log(L2 / L1)
dx = abs(x0b - x0); dsel = (keep2 != base_sel).sum(); da = abs(ac2[keep2].mean() - alpha_col[base_sel].mean())
verdict('P5', dx > 1e-12 or dsel > 0 or da > 1e-12,
        f'x moved {dx:.2e}, sample moved by {dsel} sources, colour-alpha mean moved {da:.2e}')


def slice_beta(sel, xeff, ab, ecl=True):
    c = np.bincount(pix_src[sel], minlength=NPIX).astype(float)
    d, bs = boot(c, mask_sym, ecl, n=300)
    amp = np.linalg.norm(d); sd = np.std(np.linalg.norm(bs, axis=1))
    p = 2 + xeff * (1 + ab)
    proj = np.dot(d, d0 / amp0)
    sdp = np.std(bs @ (d0 / amp0))
    return d, amp, sd, p, proj, sdp


def chi2p(vals, sds):
    w = 1 / sds**2
    mu = (w * vals).sum() / w.sum()
    chi = (w * (vals - mu)**2).sum()
    return mu, np.sqrt(1 / w.sum()), chi, stats.chi2.sf(chi, len(vals) - 1)


say('\nP6. Four disjoint W1 bins: beta = D / [2 + x_eff(1 + alpha)]')
edges = [9.0, 15.0, 15.5, 16.0, 16.4]
mags = w1[keep_pix & (w1 > 9)]
bet, bsd, bproj, bprojsd = [], [], [], []
for lo, hi in zip(edges[:-1], edges[1:]):
    sel = keep_pix & (w1 > lo) & (w1 < hi)
    xf, _, _ = xslope(mags, hi); Nf = (mags < hi).sum()
    xb, _, _ = xslope(mags, lo) if lo > 9.05 else (0.0, 0, 0)
    Nb = (mags < lo).sum()
    xeff = (xf * Nf - xb * Nb) / (Nf - Nb)
    ab = alpha[sel].mean()
    d, amp, sd, p, proj, sdp = slice_beta(sel, xeff, ab)
    L_, B_ = lb(d)
    bet.append(amp / p); bsd.append(sd / p); bproj.append(proj / p); bprojsd.append(sdp / p)
    say(f'  {lo:4.1f}-{hi:4.1f}: N={sel.sum():,}  x_f={xf:.3f} x_b={xb:.3f} x_eff={xeff:.3f}  alpha={ab:.3f}  '
        f'p={p:.3f} (2 of it the addresses\', {p-2:.3f} the payload\'s)  D={amp:.5f}+-{sd:.5f} at ({L_:.0f}, {B_:.0f}), '
        f'{angle(d, CMB):.0f} deg from CMB  -> beta={amp/p:.3e}+-{sd/p:.1e} ({amp/p/float(BETA_CMB):.2f} x CMB); '
        f'along the full axis {proj/p:.3e}+-{sdp/p:.1e}; expected D_kin {p*float(BETA_CMB):.5f}')
mu, se, chi, pv = chi2p(np.array(bet), np.array(bsd))
say(f'  amplitudes: weighted beta {mu:.3e} +- {se:.1e} ({mu/float(BETA_CMB):.2f} x CMB); chi2 {chi:.2f} on 3 dof, p = {pv:.3g}')
mu2, se2, chi2, pv2 = chi2p(np.array(bproj), np.array(bprojsd))
say(f'  along the full-sample axis (a check, not the verdict): beta {mu2:.3e} +- {se2:.1e}; chi2 {chi2:.2f}, p = {pv2:.3g}')
verdict('P6', pv <= 0.01, f'p = {pv:.3g}')

say('\nP7. Three alpha terciles at 9 < W1 < 16.4: beta = D / [2 + x(1 + alpha)]')
qs = np.quantile(alpha[base_sel], [1/3, 2/3])
bet, bsd, bproj, bprojsd = [], [], [], []
for k_, (lo, hi) in enumerate([(-np.inf, qs[0]), (qs[0], qs[1]), (qs[1], np.inf)]):
    inter = (alpha > lo) & (alpha <= hi)
    sel = base_sel & inter
    xk, _, _ = xslope(w1[keep_pix & (w1 > 9) & inter], 16.4)
    ab = alpha[sel].mean()
    d, amp, sd, p, proj, sdp = slice_beta(sel, xk, ab)
    L_, B_ = lb(d)
    bet.append(amp / p); bsd.append(sd / p); bproj.append(proj / p); bprojsd.append(sdp / p)
    say(f'  tercile {k_+1}: alpha {lo:.2f}..{hi:.2f}, mean {ab:.3f}, x {xk:.3f}, N={sel.sum():,}, p={p:.3f}; '
        f'D={amp:.5f}+-{sd:.5f} at ({L_:.0f}, {B_:.0f}) -> beta={amp/p:.3e}+-{sd/p:.1e} ({amp/p/float(BETA_CMB):.2f} x CMB); '
        f'along the full axis {proj/p:.3e}+-{sdp/p:.1e}')
mu, se, chi, pv = chi2p(np.array(bet), np.array(bsd))
say(f'  amplitudes: weighted beta {mu:.3e} +- {se:.1e}; chi2 {chi:.2f} on 2 dof, p = {pv:.3g}')
mu2, se2, chi2, pv2 = chi2p(np.array(bproj), np.array(bprojsd))
say(f'  along the full-sample axis (a check): beta {mu2:.3e} +- {se2:.1e}; chi2 {chi2:.2f}, p = {pv2:.3g}')
verdict('P7', pv <= 0.01, f'p = {pv:.3g}')

say('\nP8. The size (no prediction)')
say(f'  beta read from the full sample: {amp0/p0:.3e} +- {sd0/p0:.1e} = {amp0/p0/float(BETA_CMB):.2f} x the CMB\'s '
    f'(direction {angle(d0, CMB):.1f} deg off). Reported, not scored.')
say(f'\n[total {time.time()-T0:.0f} s]')
