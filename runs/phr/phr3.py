# PHR runs 3-4 (run 4: each channel rescaled, z/max|z| and f in sweep steps, before any fit): one-pole fit of both quadratures, then Gamma from the amplitude alone and from the phase alone.
# Usage: python3 runs/phr/phr3.py <VWireStudyData/RawScans/Wire> <online_data/Fig1c/resonance_curve.dat>
import sys, glob, os, numpy as np
from scipy.optimize import least_squares
rng = np.random.default_rng(1208)

def model(p, f, fb):
    Ar, Ai, f0, G, B0r, B0i, B1r, B1i = p
    return (Ar + 1j*Ai)/(f0 - f - 0.5j*G) + (B0r + 1j*B0i) + (B1r + 1j*B1i)*(f - fb)

def fit1(f, z, p0, fb, sx=None, sy=None):
    wx = 1/sx if sx is not None else 1.0; wy = 1/sy if sy is not None else 1.0
    r = lambda p: np.r_[(model(p, f, fb) - z).real*wx, (model(p, f, fb) - z).imag*wy]
    return least_squares(r, p0, x_scale='jac', max_nfev=4000)

def side_fits(f, zc, f0, G):
    p2 = np.abs(zc)**2
    lor = lambda q: q[0]/((f - q[1])**2 + q[2]**2/4) - p2
    a = least_squares(lor, [p2.max()*G*G/4, f0, G], x_scale='jac', max_nfev=4000).x
    Gamp = abs(a[2])
    ph = np.unwrap(np.angle(zc)); w = np.abs(zc)
    def pres(q):
        m = q[2] + np.unwrap(np.arctan2(q[1]/2, q[0] - f))
        d = np.angle(np.exp(1j*(ph - m)))
        return d*w
    # phi0 start: phase far below resonance (atan2 -> 0 there)
    phi0 = np.angle(zc[np.argmax(w)]) - np.pi/2
    s = 1 if np.mean(np.diff(ph)[np.abs(f[1:] - f0) < G]) >= 0 else -1
    best = None
    for sg in (1, -1):
        def pr(q, sg=sg):
            m = q[2] + sg*np.arctan2(q[1]/2, q[0] - f)
            return np.angle(np.exp(1j*(ph - m)))*w
        for ph0 in np.linspace(-np.pi, np.pi, 8, endpoint=False):
            r = least_squares(pr, [f0, G, ph0], x_scale='jac', max_nfev=4000)
            if best is None or r.cost < best[0].cost: best = (r, sg)
    q = best[0].x
    Gph = abs(q[1])
    # data's turn across f0 +- Gph/2 (unwrapped arg zc)
    turn = abs(np.interp(q[0] + Gph/2, f, ph) - np.interp(q[0] - Gph/2, f, ph))
    return Gamp, Gph, np.degrees(turn), q[0]

def analyse(f, z, sx=None, sy=None, nboot=200):
    o = np.argsort(f); f, z = f[o], z[o]
    # run 4: rescale so every fitted number is of order 1 (widths are compared as ratios)
    zs = np.max(np.abs(z)); df = np.median(np.diff(f)); fm = f.mean()
    f = (f - fm)/df; z = z/zs
    if sx is not None: sx, sy = sx/zs, sy/zs
    if sx is not None: sx, sy = sx[o], sy[o]
    fb = f.mean(); n = len(f); k = max(3, int(0.2*n)); idx = np.r_[0:k, n-k:n]
    cr = np.polyfit(f[idx]-fb, z.real[idx], 1); ci = np.polyfit(f[idx]-fb, z.imag[idx], 1)
    zc0 = z - (np.polyval(cr, f-fb) + 1j*np.polyval(ci, f-fb))
    p2 = np.abs(zc0)**2; i0 = p2.argmax(); above = np.where(p2 >= p2[i0]/2)[0]
    G0 = max(f[above.max()] - f[above.min()], np.median(np.diff(f)))
    A0 = zc0[i0]*(-0.5j*G0)
    p0 = [A0.real, A0.imag, f[i0], G0, cr[1], ci[1], cr[0], ci[0]]
    # run 4: several starting widths, keep the least cost (one start found a worse local minimum after rescaling)
    fit = None
    for m in (0.5, 1, 2, 4):
        q0 = list(p0); q0[3] = G0*m; q0[0], q0[1] = (A0*m).real, (A0*m).imag
        r_ = fit1(f, z, q0, fb, sx, sy)
        if fit is None or r_.cost < fit.cost: fit = r_
    p = fit.x
    chi2 = None
    if sx is not None:
        chi2 = 2*fit.cost/(2*n - len(p))
    def from_fit(pp, zz):
        zc = zz - (pp[4] + 1j*pp[5]) - (pp[6] + 1j*pp[7])*(f - fb)
        return side_fits(f, zc, pp[2], abs(pp[3]))
    Ga, Gp, turn, f0 = from_fit(p, z)
    resid = z - model(p, f, fb); fitted = model(p, f, fb)
    diffs = []
    for b in range(nboot):
        zb = fitted + resid[rng.integers(0, n, n)]
        pb = fit1(f, zb, p, fb, sx, sy).x
        try:
            a, g, _, _ = from_fit(pb, zb); diffs.append(g - a)
        except Exception: pass
    sig = np.std(diffs) if len(diffs) > 10 else np.nan
    return dict(f0=fm + f0*df, G=abs(p[3])*df, Gamp_u=Ga, G_u=abs(p[3]), Gamp=Ga*df, Gph=Gp*df, rel=Gp/Ga - 1, sig=sig*df, turn=turn, chi2=chi2,
                pts=abs(p[3]))

root, set2 = sys.argv[1], sys.argv[2]
d = np.loadtxt(set2, delimiter=',', comments='#')
r2 = analyse(d[:, 0]*1e9, d[:, 2] + 1j*d[:, 3])
print('SET 2: f0 %.6f GHz, Gamma(full) %.2f kHz, Gamma_amp %.2f kHz, Gamma_phase %.2f kHz, rel %+.4f, sigma(diff) %.2f kHz, '
      '|diff|/sigma %.2f, turn over f0 +- G/2 %.1f deg, points/Gamma %.1f' % (r2['f0']/1e9, r2['G']/1e3, r2['Gamp']/1e3,
      r2['Gph']/1e3, r2['rel'], r2['sig']/1e3, abs(r2['Gph'] - r2['Gamp'])/r2['sig'], r2['turn'], r2['pts']))
R1 = abs(r2['rel']) <= 0.05 and abs(r2['Gph'] - r2['Gamp']) <= 3*r2['sig']
print('R1', 'not killed' if R1 else 'KILLED')
print('R4 set 2', 'not killed' if abs(r2['turn'] - 90) <= 10 else 'KILLED')

# set 1: the channels run 1 analysed (same selection rule)
files = sorted(glob.glob(os.path.join(root, '02_Precision', '*.txt')) + glob.glob(os.path.join(root, '03_FieldReconstr', '*.txt')))
def one(job):
    # one channel; its own seed (run 4 runs channels in parallel, so the shared generator is replaced per channel)
    global rng
    fn, ch, seed = job
    rng = np.random.default_rng(seed)
    try: D = np.genfromtxt(fn, delimiter=',', names=True)
    except Exception: return None
    if D.size < 20 or 'Frequency' not in D.dtype.names: return None
    f = D['Frequency']; o = np.argsort(f); f = f[o]
    z = (D[f'MeanX{ch}'] + 1j*D[f'MeanY{ch}'])[o]
    sx = D[f'stdX{ch}'][o]; sy = D[f'stdY{ch}'][o]
    n = len(f); k = max(3, int(0.2*n)); idx = np.r_[0:k, n-k:n]
    cr = np.polyfit(f[idx], z.real[idx], 1); ci = np.polyfit(f[idx], z.imag[idx], 1)
    zc = z - (np.polyval(cr, f) + 1j*np.polyval(ci, f)); p = np.abs(zc)**2
    if p.max() < 20*np.sqrt(np.mean(p[idx]**2)): return None
    try:
        r = analyse(f, z, np.maximum(sx, 1e-12), np.maximum(sy, 1e-12), nboot=100)
    except Exception:
        return (fn, ch, 'fail')
    if f[0] > r['f0'] - 2*r['G'] or f[-1] < r['f0'] + 2*r['G']:
        return (fn, ch, 'narrow')
    print('%s ch%d rel %+.4f sig/G %.4f turn %.1f chi2 %.2f' % (os.path.basename(fn), ch, r['rel'], r['sig']/r['Gamp'],
          r['turn'], r['chi2']), flush=True)
    return (fn, ch, 'ok', r)
import multiprocessing as mp
jobs = [(fn, ch, 1208 + 2*i + ch) for i, fn in enumerate(files) for ch in (1, 2)]
with mp.Pool(min(8, os.cpu_count())) as pool:
    rows = [x for x in pool.map(one, jobs, chunksize=1) if x is not None]
ok = [x[3] for x in rows if x[2] == 'ok']
print('SET 1: channels fitted', len(ok), 'other', [x[2] for x in rows if x[2] != 'ok'].count('narrow'), 'narrow,',
      [x[2] for x in rows if x[2] != 'ok'].count('fail'), 'failed')
bad = [r for r in ok if abs(r['Gph'] - r['Gamp']) > 3*r['sig'] + 0.02*r['Gamp']]
print('R2: beyond 3 sigma + 2%%: %d of %d (%.1f%%) ->' % (len(bad), len(ok), 100*len(bad)/len(ok)),
      'not killed' if len(bad) <= 0.10*len(ok) else 'KILLED')
good = [r for r in ok if r['chi2'] < 2]
badg = [r for r in good if abs(r['Gph'] - r['Gamp']) > 3*r['sig'] + 0.02*r['Gamp']]
print('R2 (adequate, chi2/dof<2): %d of %d (%.1f%%)' % (len(badg), len(good), 100*len(badg)/max(1,len(good))))
print('R4 (adequate): median turn %.1f deg' % np.median([r['turn'] for r in good]))
relg = np.array([r['rel'] for r in good]); print('adequate rel: median %+.4f quartiles %+.4f %+.4f' % (np.median(relg), *np.percentile(relg,[25,75])))
chis = np.array([r['chi2'] for r in ok])
print('R3: chi2/dof median %.2f (quartiles %.2f, %.2f) ->' % (np.median(chis), *np.percentile(chis, [25, 75])),
      'not killed' if np.median(chis) < 2 else 'KILLED')
turns = np.array([r['turn'] for r in ok])
print('R4 set 1: median turn %.1f deg (quartiles %.1f, %.1f) ->' % (np.median(turns), *np.percentile(turns, [25, 75])),
      'not killed' if abs(np.median(turns) - 90) <= 10 else 'KILLED')
rel = np.array([r['rel'] for r in ok])
print('set 1 Gamma_phase/Gamma_amp - 1: median %+.4f, quartiles %+.4f %+.4f' % (np.median(rel), *np.percentile(rel, [25, 75])))
print('set 1 points per Gamma: median %.1f' % np.median([r['pts'] for r in ok]))
