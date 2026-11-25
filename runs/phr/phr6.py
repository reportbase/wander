# PHR run 6: run 5b's analysis after removing a delay e^(-2 pi i f tau), tau read off the line alone (the outer 20%
# of each side's unwrapped phase, one straight line in f). Usage: python3 runs/phr/phr6.py <carter dir> <fano Data dir>
import sys, os, glob, numpy as np, multiprocessing as mp
src = open(os.path.join(os.path.dirname(__file__), 'phr5.py')).read().split("if __name__ == '__main__':")[0]
exec(src)  # phr3's analysis, run 5b's budget, qualifies, one, judge

def tau_off_line(f, z):
    n = len(f); k = max(3, int(0.2*n)); idx = np.r_[0:k, n-k:n]
    ph = np.unwrap(np.angle(z))
    a = np.polyfit(f[idx] - f.mean(), ph[idx], 1)[0]
    return -a/(2*np.pi)

def one6(job):
    tag, f, z, seed = job
    o = np.argsort(f); f, z = f[o], z[o]
    tau = tau_off_line(f, z)
    zc = z*np.exp(2j*np.pi*(f - f.mean())*tau)
    r = one((tag, f, zc, seed))
    if r[1] == 'ok':
        r[2]['tau'] = tau
        print('   %s tau %.3f ns' % (tag, tau*1e9), flush=True)
    return r + (tau,) if r[1] != 'ok' else r

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
        d = np.load(fn)  # allow_pickle stays False
        f = d['frequency']; A = d['amplitude']; P = d['phase']
        for j in range(A.shape[0]):
            fj.append(('%s p%d' % (os.path.basename(fn), j), f, A[j]*np.exp(1j*P[j]), 5000 + len(fj)))
    with mp.Pool(os.cpu_count()) as pool:
        rc = pool.map(one6, cj, chunksize=1)
        rf = pool.map(one6, fj, chunksize=1)
    from collections import Counter
    passed = sum(1 for x in rc if x[1] != 'noise')
    a = judge('CARTER (200 seeded of 972), delay removed', rc)
    okc = [x[2] for x in rc if x[1] == 'ok']
    if okc:
        rel = np.array([r['rel'] for r in okc]); turn = np.array([r['turn'] for r in okc]); tau = np.array([r['tau'] for r in okc])
        print('  R9 median |rel| %.4f ->' % np.median(np.abs(rel)), 'not killed' if np.median(np.abs(rel)) < 0.03 else 'KILLED')
        print('  R10 median turn %.1f ->' % np.median(turn), 'not killed' if abs(np.median(turn) - 90) <= 5 else 'KILLED')
        m = np.median(tau); within = np.all(np.abs(tau - m) <= 0.1*abs(m)) and m > 0
        print('  R11 tau median %.3f ns, range %.3f..%.3f ns ->' % (m*1e9, tau.min()*1e9, tau.max()*1e9), 'not killed' if within else 'KILLED')
        by = Counter(t.split('_')[0] for t in [x[0] for x in rc if x[1] == 'ok']); print('  fitted by resonator:', dict(by))
    print('  R12 Carter passing the line test: %d (run 5b 63) ->' % passed, 'not killed' if passed > 63 else 'KILLED')
    alltau = np.array([x[-1] for x in rc if x[1] != 'ok'] + [x[2]['tau'] for x in rc if x[1] == 'ok'])
    print('  Carter tau over all 200: median %.3f ns, quartiles %.3f %.3f' % (np.median(alltau)*1e9, *np.percentile(alltau, [25, 75])*1e9))
    b = judge('FANO (all power sweeps), delay removed', rf)
    okf = [x[2] for x in rf if x[1] == 'ok']
    if okf:
        rel = np.array([r['rel'] for r in okf]); turn = np.array([r['turn'] for r in okf])
        d_rel = np.median(rel) - 0.0040; d_turn = np.median(turn) - 91.0
        print('  R13 median rel moved %+.4f, median turn moved %+.1f deg ->' % (d_rel, d_turn),
              'not killed' if abs(d_rel) < 0.01 and abs(d_turn) < 2 else 'KILLED')
        print('  Fano tau median %.4f ns' % (np.median([r['tau'] for r in okf])*1e9))
