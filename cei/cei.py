"""CEI: more points, less seen. Brute force against R(N) = (N/pi) arccos(eps N / 2pi). See plans/cei-plan.md."""
import numpy as np

def brute(N, eps):
    k = np.arange(N)
    th = 2*np.pi*k/N
    th = (th + np.pi) % (2*np.pi) - np.pi          # angle from the middle of the view, in (-pi, pi]
    vis = np.abs(th) <= np.pi/2
    idx = np.where(vis)[0]
    order = idx[np.argsort(th[idx])]
    x = np.sin(th[order])                           # projection, in units of the radius
    gaps = np.diff(x)
    left = np.r_[np.inf, gaps]; right = np.r_[gaps, np.inf]
    return int(np.sum((left >= eps) & (right >= eps)))

def formula(N, eps):
    x = eps*N/(2*np.pi)
    return 0.0 if x >= 1 else (N/np.pi)*np.arccos(x)

res = {}
for eps in (1e-3, 1e-4):
    Ns = np.unique(np.linspace(0.05/eps, 0.99*2*np.pi/eps, 400).astype(int))
    worst = 0; worst_rel_ok = True
    best = (0, 0)
    for N in Ns:
        b = brute(N, eps); f = formula(N, eps)
        d = abs(b - f)
        worst = max(worst, d)
        if d > 2 + 0.002*f: worst_rel_ok = False
        if b > best[0]: best = (b, N)
    # fine search near the peak
    for N in range(int(3.9/eps), int(4.3/eps), max(1, int(0.001/eps))):
        b = brute(N, eps)
        if b > best[0]: best = (b, N)
    Nc = int(np.ceil(2*np.pi/eps))
    ceil0 = all(brute(N, eps) == 0 for N in (Nc, Nc+7, int(1.1*Nc)))
    res[eps] = dict(worst=worst, p1=worst_rel_ok, best=best, ceil0=ceil0)
    print(f"eps={eps:g}: worst |brute-formula| {worst:.2f}; P1 {'not killed' if worst_rel_ok else 'KILLED'}")
    print(f"   peak {best[0]} at N={best[1]}; 1.1222/eps={1.1222/eps:.1f} ({100*(best[0]*eps/1.1222-1):+.3f}%), "
          f"N*=4.098/eps={4.098/eps:.0f} ({100*(best[1]*eps/4.098-1):+.2f}%)")
    print(f"   ceiling: count 0 at and past N={Nc}: {ceil0}")
p2 = all(abs(r['best'][0]*e/1.1222-1) <= 0.005 and abs(r['best'][1]*e/4.098-1) <= 0.02 for e, r in res.items())
p3 = all(r['ceil0'] for r in res.values())
# P4: share at same eps*N
shares = []
for eN in (0.5, 1, 2, 4, 6):
    a = brute(int(eN/1e-3), 1e-3)/int(eN/1e-3); b = brute(int(eN/1e-4), 1e-4)/int(eN/1e-4)
    shares.append((eN, a, b)); 
p4 = all(abs(a-b) <= 0.002 for _, a, b in shares)
for eN, a, b in shares: print(f"   eps*N={eN}: share {a:.4f} (1e-3) {b:.4f} (1e-4)")
x = 0.6522; 
from scipy.optimize import minimize_scalar
o = minimize_scalar(lambda x: -x*np.arccos(x), bounds=(0.1, 0.99), method='bounded')
print(f"exact peak: x*={o.x:.6f}, 2 x* arccos x* = {-2*o.fun:.6f}")
print("P2", "not killed" if p2 else "KILLED", "| P3", "not killed" if p3 else "KILLED", "| P4", "not killed" if p4 else "KILLED")
