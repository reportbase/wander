# EHO part 2: ring fits to the EHT 2017 M87 public visibilities (2019-D01-01, HOPS netcal, Stokes I csv).
# Model: m-ring of order 1 (Johnson et al. 2020's family): I(phi) on a thin ring of diameter d with
# brightness 1 + 2|b| cos(phi - psi), blurred by a circular Gaussian of FWHM w.
# V(u) = F e^{-(pi w rho)^2/(4 ln 2)} [ J0(pi d rho) - 2 i |b| J1(pi d rho) cos(phi_u - psi) ]   (phi measured E of N)
# Fitted to visibility amplitudes (10% systematic added) and closure phases (triangles at one timestamp).
# Reported: d, the first null u0 = 2.405/(pi d) of the J0 term, and psi, the bright side's position angle (E of N).
import sys, glob, itertools, warnings, numpy as np
warnings.filterwarnings("ignore")
from scipy.special import j0, j1
from scipy.optimize import least_squares
PATS = sys.argv[1:]
UAS = np.pi/180/3600/1e6
def load(f):
    rows = []
    for line in open(f):
        if line.startswith('#'): continue
        t,a,b,u,v,amp,ph,sig = line.strip().split(',')
        rows.append((float(t),a,b,float(u),float(v),float(amp),float(ph),float(sig)))
    return rows
def model(p, u, v):
    F, d, w, b, psi = p
    rho = np.hypot(u, v); phu = np.arctan2(u, v)          # position angle of the baseline, E of N
    x = np.pi*d*UAS*rho
    env = np.exp(-(np.pi*w*UAS*rho)**2/(4*np.log(2)))
    return F*env*(j0(x) - 2j*b*j1(x)*np.cos(phu - psi))
def prep(rows):
    rows = [r for r in rows if np.hypot(r[3], r[4]) > 0.1e9]       # drop intra-site baselines (ALMA-APEX, SMA-JCMT)
    amp = np.array([(r[3], r[4], r[5], np.hypot(r[7], 0.1*r[5])) for r in rows])
    by_t = {}
    for r in rows: by_t.setdefault(round(r[0],6), []).append(r)
    cps = []
    for t, rs in by_t.items():
        vis = {}
        for r in rs: vis[(r[1],r[2])] = r
        st = sorted({s for r in rs for s in (r[1],r[2])})
        for a,b,c in itertools.combinations(st, 3):
            legs = []
            for p,q in ((a,b),(b,c),(c,a)):
                if (p,q) in vis: r = vis[(p,q)]; legs.append((r[3],r[4],np.deg2rad(r[6]),r[7]/r[5],1))
                elif (q,p) in vis: r = vis[(q,p)]; legs.append((-r[3],-r[4],-np.deg2rad(r[6]),r[7]/r[5],1))
                else: break
            else:
                cp = sum(l[2] for l in legs); s = np.sqrt(sum(l[3]**2 for l in legs))
                cps.append([l[0] for l in legs]+[l[1] for l in legs]+[cp, max(s, np.deg2rad(2))])
    return amp, np.array(cps)
def resid(p, amp, cps):
    ra = (np.abs(model(p, amp[:,0], amp[:,1])) - amp[:,2])/amp[:,3]
    m = model(p, cps[:,0:3].ravel(), cps[:,3:6].ravel()).reshape(-1,3)
    cpm = np.angle(m.prod(axis=1))
    rc = np.angle(np.exp(1j*(cpm - cps[:,6])))/cps[:,7]
    return np.concatenate([ra, rc])
def fit(f):
    amp, cps = prep(load(f))
    best = None
    for d0 in (35, 40, 45, 50):
        for psi0 in np.deg2rad([0, 90, 180, 270]):
            r = least_squares(resid, [0.6, d0, 15, 0.3, psi0], args=(amp, cps),
                              bounds=([0.1, 20, 0, 0, -10], [2, 70, 40, 0.5, 10]))
            if best is None or r.cost < best.cost: best = r
    F, d, w, b, psi = best.x
    J = best.jac; cov = np.linalg.pinv(J.T @ J) * (2*best.cost/max(1, len(best.fun)-5))
    e = np.sqrt(np.diag(cov))
    return dict(F=F, d=d, ed=e[1], w=w, b=b, psi=np.rad2deg(psi) % 360, epsi=np.rad2deg(e[4]),
                u0=2.405/(np.pi*d*UAS)/1e9, chi2=2*best.cost/len(best.fun), n=len(amp), ncp=len(cps))
res = {}
files = sorted(f for p in PATS for f in glob.glob(p))
for f in files:
    parts = f.split('/')[-1].split('_')
    key = parts[2] + '-' + parts[3] + ' ' + parts[4]
    r = fit(f); res[key] = r
    print(f"{key}: d={r['d']:.2f}±{r['ed']:.2f} uas  u0={r['u0']:.3f} Glambda  w={r['w']:.1f}  b={r['b']:.2f}  "
          f"PA={r['psi']:.1f}±{r['epsi']:.1f} deg  F={r['F']:.2f} Jy  chi2/n={r['chi2']:.2f}  (amps {r['n']}, closure phases {r['ncp']})")
def grp(pre): return {k:v for k,v in res.items() if k.startswith(pre)}
def circmean(a): return np.rad2deg(np.angle(np.mean(np.exp(1j*np.deg2rad(a))))) % 360
def dang(a, b): return (a - b + 180) % 360 - 180
y17 = grp('2017'); u17 = np.array([r['u0'] for r in y17.values()]); d17 = np.array([r['d'] for r in y17.values()])
p17 = np.array([r['psi'] for r in y17.values()])
print(f"Q2 (2017, 4 days x 2 bands): u0 spread (max-min)/mean = {(u17.max()-u17.min())/u17.mean():.4f}  (kill > 0.05)")
print(f"Q3 (2017): mean d = {d17.mean():.2f} uas, off 42 by {abs(d17.mean()-42)/42:.3f}  (kill > 0.15)")
print(f"Q5 (2017): PA spread about the mean = {np.ptp(dang(p17, circmean(p17))):.1f} deg  (predicted < 20, recorded)")
for day in ('2018-111', '2018-112', '2018-115'):
    g = grp(day); u = np.array([r['u0'] for r in g.values()]); pa = np.array([r['psi'] for r in g.values()])
    print(f"Q4 {day}: mean u0 {u.mean():.3f} vs 2017 {u17.mean():.3f}: off {abs(u.mean()-u17.mean())/u17.mean():.3f} (kill > 0.05);"
          f" PA {circmean(pa):.1f} vs 2017 {circmean(p17):.1f}: shift {dang(circmean(pa), circmean(p17)):.1f} deg (kill < 15);"
          f" band spread of u0 {np.ptp(u)/u.mean():.3f}; median chi2/n {np.median([r['chi2'] for r in g.values()]):.2f}")
