# PHR runs 5 and 5b (5b: a budget per sweep): run 4's analysis on finer sweeps (Carter et al. 2016, Zenodo 61575; Rieger, Guenzler et al. 2023,
# Zenodo 7767046). Usage: python3 runs/phr/phr5.py <carter 08222016Res dir> <fano Data dir>
import sys, os, glob, numpy as np, multiprocessing as mp
src = open(os.path.join(os.path.dirname(__file__), 'phr3.py')).read().split("root, set2 = sys.argv")[0]
exec(src)  # model, fit1, side_fits, analyse (run 4's)
# run 5b's budget: each fit capped at 500 evaluations, 20 bootstrap resamples, 5 minutes a sweep
import signal
_ls = least_squares
def least_squares(*a, **k):
    k['max_nfev'] = min(k.get('max_nfev', 500), 500); return _ls(*a, **k)
class _Timeout(Exception): pass
def _alarm(*a): raise _Timeout()

def qualifies(f, z):
    n = len(f); k = max(3, int(0.2*n)); idx = np.r_[0:k, n-k:n]
    cr = np.polyfit(f[idx], z.real[idx], 1); ci = np.polyfit(f[idx], z.imag[idx], 1)
    p = np.abs(z - (np.polyval(cr, f) + 1j*np.polyval(ci, f)))**2
    return p.max() >= 20*np.sqrt(np.mean(p[idx]**2))

def one(job):
    global rng
    tag, f, z, seed = job
    rng = np.random.default_rng(seed)
    if not qualifies(f, z): return (tag, 'noise')
    signal.signal(signal.SIGALRM, _alarm); signal.alarm(300)
    try: r = analyse(f, z, nboot=20)
    except _Timeout: return (tag, 'timed out')
    except Exception: return (tag, 'fail')
    finally: signal.alarm(0)
    if f.min() > r['f0'] - 2*r['G'] or f.max() < r['f0'] + 2*r['G']: return (tag, 'narrow')
    if r['pts'] < 20: return (tag, 'coarse')
    print('%s rel %+.4f sig/G %.4f turn %.1f pts %.0f' % (tag, r['rel'], r['sig']/r['Gamp'], r['turn'], r['pts']), flush=True)
    return (tag, 'ok', r)

def judge(name, res):
    from collections import Counter
    ok = [x[2] for x in res if x[1] == 'ok']
    print('%s: %s' % (name, dict(Counter(x[1] for x in res))))
    if not ok: print('  nothing qualified'); return None
    bad = sum(1 for r in ok if abs(r['Gph'] - r['Gamp']) > 3*r['sig'] + 0.02*r['Gamp'])
    rel = np.array([r['rel'] for r in ok]); turn = np.array([r['turn'] for r in ok])
    R5 = bad <= 0.10*len(ok); R6 = np.median(np.abs(rel)) < 0.03; R7 = abs(np.median(turn) - 90) <= 5
    print('  R5 beyond 3 sigma + 2%%: %d of %d (%.1f%%) -> %s' % (bad, len(ok), 100*bad/len(ok), 'not killed' if R5 else 'KILLED'))
    print('  R6 median |rel| %.4f (rel median %+.4f, quartiles %+.4f %+.4f) -> %s' % (np.median(np.abs(rel)), np.median(rel),
          *np.percentile(rel, [25, 75]), 'not killed' if R6 else 'KILLED'))
    print('  R7 median turn %.1f deg (quartiles %.1f, %.1f) -> %s' % (np.median(turn), *np.percentile(turn, [25, 75]),
          'not killed' if R7 else 'KILLED'))
    print('  points per Gamma: median %.0f' % np.median([r['pts'] for r in ok]))
    return R5, R6, R7

if __name__ == '__main__':
    cdir, fdir = sys.argv[1], sys.argv[2]
    files = sorted(glob.glob(os.path.join(cdir, '*.S2P')))
    pick = sorted(np.random.default_rng(1209).choice(len(files), 200, replace=False))
    cj = []
    for i in pick:
        d = np.loadtxt(files[i], skiprows=1)
        cj.append((os.path.basename(files[i]), d[:, 0], d[:, 1] + 1j*d[:, 2], 2000 + int(i)))
    fj = []
    for fn in sorted(glob.glob(os.path.join(fdir, '*', '*powersweep*.npz'))):
        d = np.load(fn)  # allow_pickle stays False: settings.npy is never read
        f = d['frequency']; A = d['amplitude']; P = d['phase']
        for j in range(A.shape[0]):
            fj.append(('%s p%d' % (os.path.basename(fn), j), f, A[j]*np.exp(1j*P[j]), 5000 + len(fj)))
    with mp.Pool(os.cpu_count()) as pool:
        rc = pool.map(one, cj, chunksize=1)
        rf = pool.map(one, fj, chunksize=1)
    a = judge('CARTER (200 seeded of 972)', rc)
    b = judge('FANO (all power sweeps)', rf)
    if a and b:
        print('R8 ->', 'KILLED' if ((not b[0] or not b[1]) and a[0] and a[1]) else 'not killed')
