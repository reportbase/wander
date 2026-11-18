# EHO run 3: an m-ring of order 3 with a disc floor, fitted to closure phases and log closure amplitudes only (station gains cancel).
# Same baselines and errors as eho2.py; the flux is fixed at 1 (closures carry no overall scale).
import sys, glob, itertools, warnings, numpy as np
warnings.filterwarnings("ignore")
from scipy.special import j0, j1, jv
from scipy.optimize import least_squares
UAS = np.pi/180/3600/1e6
def load(f):
    rows = []
    for line in open(f):
        if line.startswith('#'): continue
        t,a,b,u,v,amp,ph,sig = line.strip().split(',')
        rows.append((float(t),a,b,float(u),float(v),float(amp),float(ph),float(sig)))
    return rows
def model(p, u, v):
    # m-ring of order 3 + a filled disc of share f, both blurred by a Gaussian of FWHM w
    d, w, f = p[0], p[1], p[2]
    beta = [p[3] + 1j*p[4], p[5] + 1j*p[6], p[7] + 1j*p[8]]
    rho = np.hypot(u, v); phu = np.arctan2(u, v)
    x = np.pi*d*UAS*rho + 1e-12
    env = np.exp(-(np.pi*w*UAS*rho)**2/(4*np.log(2)))
    ring = jv(0, x).astype(complex)
    for k, bk in enumerate(beta, start=1):
        e = np.exp(1j*k*(phu - np.pi/2))
        ring = ring + bk*jv(k, x)*e + np.conj(bk)*((-1)**k)*jv(k, x)*np.conj(e)
    disc = 2*j1(x)/x
    return env*((1 - f)*ring + f*disc)
def prep(rows):
    rows = [r for r in rows if np.hypot(r[3], r[4]) > 0.1e9]
    by_t = {}
    for r in rows: by_t.setdefault(round(r[0],6), []).append(r)
    cps, cas = [], []
    def leg(vis, p, q):
        if (p,q) in vis: r = vis[(p,q)]; return (r[3], r[4], np.deg2rad(r[6]), r[5], np.hypot(r[7], 0.1*r[5]))
        if (q,p) in vis: r = vis[(q,p)]; return (-r[3], -r[4], -np.deg2rad(r[6]), r[5], np.hypot(r[7], 0.1*r[5]))
        return None
    for t, rs in by_t.items():
        vis = {(r[1],r[2]): r for r in rs}
        st = sorted({s for r in rs for s in (r[1],r[2])})
        for a,b,c in itertools.combinations(st, 3):
            L = [leg(vis,a,b), leg(vis,b,c), leg(vis,c,a)]
            if None in L: continue
            cp = sum(l[2] for l in L); s = np.sqrt(sum((l[4]/l[3])**2 for l in L))
            cps.append([l[0] for l in L]+[l[1] for l in L]+[cp, max(s, np.deg2rad(2))])
        # one independent-ish closure amplitude per quadrangle (a,b,c,d): |ab||cd|/(|ac||bd|)
        for a,b,c,d in itertools.combinations(st, 4):
            L = [leg(vis,a,b), leg(vis,c,d), leg(vis,a,c), leg(vis,b,d)]
            if None in L: continue
            lca = np.log(L[0][3]) + np.log(L[1][3]) - np.log(L[2][3]) - np.log(L[3][3])
            s = np.sqrt(sum((l[4]/l[3])**2 for l in L))
            cas.append([l[0] for l in L]+[l[1] for l in L]+[lca, s])
    return np.array(cps), np.array(cas)
def resid(p, cps, cas):
    m = model(p, cps[:,0:3].ravel(), cps[:,3:6].ravel()).reshape(-1,3)
    rc = np.angle(np.exp(1j*(np.angle(m.prod(axis=1)) - cps[:,6])))/cps[:,7]
    if len(cas) == 0: return rc
    a = np.abs(model(p, cas[:,0:4].ravel(), cas[:,4:8].ravel())).reshape(-1,4) + 1e-12
    ra = (np.log(a[:,0]) + np.log(a[:,1]) - np.log(a[:,2]) - np.log(a[:,3]) - cas[:,8])/cas[:,9]
    return np.concatenate([rc, ra])
def fit(f):
    cps, cas = prep(load(f))
    best = None
    rng = np.random.default_rng(7)
    for d0 in (38, 43, 48):
        for s in range(3):
            b0 = rng.uniform(-0.2, 0.2, 6)
            x0 = np.concatenate([[d0, 10, 0.1], b0])
            r = least_squares(resid, x0, args=(cps, cas),
                              bounds=([20, 0, 0] + [-0.5]*6, [70, 40, 0.9] + [0.5]*6))
            if best is None or r.cost < best.cost: best = r
    p = best.x
    J = best.jac; cov = np.linalg.pinv(J.T @ J) * (2*best.cost/max(1, len(best.fun)-9))
    b1 = p[3] + 1j*p[4]
    return dict(d=p[0], ed=np.sqrt(abs(cov[0,0])), w=p[1], f=p[2], b=abs(b1), psi=np.rad2deg(-np.angle(b1)) % 360,
                b2=abs(p[5]+1j*p[6]), b3=abs(p[7]+1j*p[8]), chi2=2*best.cost/len(best.fun), ncp=len(cps), nca=len(cas))
if __name__ == "__main__":
    import multiprocessing as mp
    files = sorted(f for p in sys.argv[1:] for f in glob.glob(p))
    keys = []
    for f in files:
        parts = f.split('/')[-1].split('_'); keys.append(parts[2] + '-' + parts[3] + ' ' + parts[4])
    with mp.Pool(min(len(files), mp.cpu_count())) as pool:
        outs = pool.map(fit, files)
    res = dict(zip(keys, outs))
    for key, r in res.items():
        print(f"{key}: d={r['d']:.2f}±{r['ed']:.2f} uas  w={r['w']:.1f}  f={r['f']:.2f}  |b1|={r['b']:.2f} |b2|={r['b2']:.2f} |b3|={r['b3']:.2f}  "
              f"chi2/n={r['chi2']:.2f}  (closure phases {r['ncp']}, closure amplitudes {r['nca']})", flush=True)
    d17 = np.array([v['d'] for k,v in res.items() if k.startswith('2017')])
    d18 = np.array([v['d'] for k,v in res.items() if k[:8] in ('2018-111','2018-115') and k.endswith(('b3','b4'))])
    c17 = [v["chi2"] for k,v in res.items() if k.startswith("2017")]
    c18 = [v["chi2"] for k,v in res.items() if k[:8] in ("2018-111","2018-115") and k.endswith(("b3","b4"))]
    print(f"Q13: median chi2/n 2017 {np.median(c17):.3f}, 2018 b3/b4 {np.median(c18):.3f}")
    print(f"Q11 (2017): spread (max-min)/mean = {np.ptp(d17)/d17.mean():.4f}  (kill > 0.05); mean {d17.mean():.2f} uas")
    print(f"Q12 (2018 days 111, 115; b3, b4): mean {d18.mean():.2f} uas against 2017's {d17.mean():.2f}: off {abs(d18.mean()-d17.mean())/d17.mean():.4f}  (kill > 0.05)")
    print("(2018 day 112, recorded):", ", ".join(f"{k}: {v['d']:.1f}" for k,v in res.items() if k.startswith('2018-112')))
