# EHO run 2: the m-ring fitted to closure phases and log closure amplitudes only (station gains cancel).
# Same model, baselines and errors as eho2.py; the flux is fixed at 1 (closures carry no overall scale).
import sys, glob, itertools, warnings, numpy as np
warnings.filterwarnings("ignore")
from scipy.special import j0, j1
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
    d, w, b, psi = p
    rho = np.hypot(u, v); phu = np.arctan2(u, v)
    x = np.pi*d*UAS*rho
    env = np.exp(-(np.pi*w*UAS*rho)**2/(4*np.log(2)))
    return env*(j0(x) - 2j*b*j1(x)*np.cos(phu - psi))
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
    for d0 in (35, 40, 45, 50):
        for psi0 in np.deg2rad([0, 90, 180, 270]):
            r = least_squares(resid, [d0, 15, 0.3, psi0], args=(cps, cas), bounds=([20, 0, 0, -10], [70, 40, 0.5, 10]))
            if best is None or r.cost < best.cost: best = r
    d, w, b, psi = best.x
    J = best.jac; cov = np.linalg.pinv(J.T @ J) * (2*best.cost/max(1, len(best.fun)-4))
    return dict(d=d, ed=np.sqrt(abs(cov[0,0])), w=w, b=b, psi=np.rad2deg(psi) % 360, chi2=2*best.cost/len(best.fun),
                ncp=len(cps), nca=len(cas))
res = {}
for f in sorted(f for p in sys.argv[1:] for f in glob.glob(p)):
    parts = f.split('/')[-1].split('_'); key = parts[2] + '-' + parts[3] + ' ' + parts[4]
    r = fit(f); res[key] = r
    print(f"{key}: d={r['d']:.2f}±{r['ed']:.2f} uas  w={r['w']:.1f}  b={r['b']:.2f}  PA={r['psi']:.1f}  "
          f"chi2/n={r['chi2']:.2f}  (closure phases {r['ncp']}, closure amplitudes {r['nca']})", flush=True)
d17 = np.array([v['d'] for k,v in res.items() if k.startswith('2017')])
d18 = np.array([v['d'] for k,v in res.items() if k[:8] in ('2018-111','2018-115') and k.endswith(('b3','b4'))])
print(f"Q8 (2017): spread (max-min)/mean = {np.ptp(d17)/d17.mean():.4f}  (kill > 0.05); mean {d17.mean():.2f} uas")
print(f"Q9 (2018 days 111, 115; b3, b4): mean {d18.mean():.2f} uas against 2017's {d17.mean():.2f}: off {abs(d18.mean()-d17.mean())/d17.mean():.4f}  (kill > 0.05)")
print("Q10 (2018 day 112, recorded):", ", ".join(f"{k}: {v['d']:.1f}" for k,v in res.items() if k.startswith('2018-112')))
