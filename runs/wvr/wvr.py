"""WVR run 1: the wave results revisited, sorted by address and central reading (plans/wvr-plan.md).
Exact (mpmath, 50 digits) plus seeded samples (numpy). Real slice of a qubit: states (cos t, sin t), A = sigma_z.
Run from the repository's root: python3 runs/wvr/wvr.py | tee runs/wvr/wvr-run1.txt
"""
from mpmath import mp, mpf, matrix, cos, sin, tan, atan, pi, sqrt, quad, log, findroot, fabs, diff, tanh, atanh
import numpy as np
mp.dps = 50
SZ = matrix([[1, 0], [0, -1]])
def ket(t): return matrix([cos(t), sin(t)])
def rho_of(nx, nz): return matrix([[(1 + nz)/2, nx/2], [nx/2, (1 - nz)/2]])
def Aw_pure(ti, tf):
    i, f = ket(ti), ket(tf)
    return (f.T*SZ*i)[0] / (f.T*i)[0]
def Aw_mixed(nx, nz, tf):
    f = ket(tf); R = rho_of(nx, nz)
    return (f.T*SZ*R*f)[0] / (f.T*R*f)[0]
def nstr(x, n=12): return mp.nstr(x, n)
verdict = {}
def mark(name, ok): verdict[name] = verdict.get(name, True) and bool(ok)

def share_above(g, c, P=pi, N=4000, off=mpf('0.000123456789')):
    """Measure of {a in [0,P): g(a) > c}/P, every crossing (root or pole) located on a grid of N and refined by bisection."""
    g0 = g
    def g(x):
        try: return g0(x)
        except ZeroDivisionError: return mpf(10)**60     # landed exactly on a pole: any huge value marks the boundary
    xs = [off + P*k/N for k in range(N + 1)]
    vals = [g(x) - c for x in xs]
    pts = [xs[0]]; signs = []
    for k in range(N):
        a, b, fa, fb = xs[k], xs[k+1], vals[k], vals[k+1]
        if (fa > 0) != (fb > 0):
            for _ in range(180):
                m = (a + b)/2; fm = g(m) - c
                if (fm > 0) == (fa > 0): a, fa = m, fm
                else: b, fb = m, fm
            pts.append((a + b)/2)
    pts.append(xs[-1])
    tot = mpf(0)
    for k in range(len(pts) - 1):
        mid = (pts[k] + pts[k+1])/2
        if g(mid) - c > 0: tot += pts[k+1] - pts[k]
    return tot/P

rng = np.random.default_rng(20261022)
TH8 = [mpf(x) for x in ('0.1', '0.3', '0.5', '0.7', '0.785398163397448309615660845819875721049292349843776', '0.9', '1.2', '1.45')]

print("== P1: the weak value is a relative address; its Cauchy's point is the Bloch point ==")
worst = mpf(0)
for k in range(30):
    ti, tf = mpf(rng.uniform(0, 3.14159)), mpf(rng.uniform(0, 3.14159))
    nz, V = cos(2*ti), sin(2*ti)
    worst = max(worst, fabs(Aw_pure(ti, tf) - (nz - V*tan(tf - ti))))
print("identity A_w = n_z - V tan(tf - ti), worst over 30:", nstr(worst, 3)); mark('P1', worst < mpf(10)**-40)
wq = mpf(0); wsw = mpf(0)
for ti in TH8:
    nz, V = cos(2*ti), sin(2*ti)
    g = lambda tf: Aw_pure(ti, tf)
    row = []
    for q in (mpf('0.1'), mpf('0.25'), mpf('0.5'), mpf('0.75'), mpf('0.9')):
        xq = nz + V*tan(pi*(q - mpf(1)/2))        # Cauchy(n_z, V) quantile
        cdf = 1 - share_above(g, xq, N=600)        # share with A_w <= xq, by root-finding on A_w itself
        wq = max(wq, fabs(cdf - q)); row.append(nstr(cdf, 6))
    sw = share_above(lambda tf: g(tf)**2, 1, N=600)
    wsw = max(wsw, fabs(sw - mpf(1)/2))
    print(f"  ti={nstr(ti,4)} n_z={nstr(nz,6)} V={nstr(V,6)}  CDF at Cauchy quantiles {row}  superweak {nstr(sw,15)}")
print("worst quantile miss", nstr(wq, 3), " worst superweak miss from 1/2", nstr(wsw, 3))
mark('P1', wq < mpf(10)**-30 and wsw < mpf(10)**-30)
N = 10**6
for ti in (0.3, 0.9):
    tf = rng.uniform(0, np.pi, N)
    a = (np.cos(tf)*np.cos(ti) - np.sin(tf)*np.sin(ti))/(np.cos(tf)*np.cos(ti) + np.sin(tf)*np.sin(ti))
    nz, V = np.cos(2*ti), np.sin(2*ti)
    for q in (0.25, 0.5, 0.75):
        xq = nz + V*np.tan(np.pi*(q - 0.5)); dens = V/(np.pi*(V**2 + (xq - nz)**2))
        se = np.sqrt(q*(1 - q)/N)/dens; got = np.quantile(a, q); z = (got - xq)/se
        print(f"  sample ti={ti} q={q}: {got:.6f} vs {xq:.6f}  ({z:+.2f} se)"); mark('P1', abs(z) < 3)
    print(f"  sample superweak share {np.mean(np.abs(a) > 1):.5f} (se {np.sqrt(0.25/N):.5f})")
print("P1", "not killed" if verdict['P1'] else "KILLED")

print("\n== P2: Born's weight makes the address a payload; V^2 + P^2 = 1 as its second moment ==")
w2 = mpf(0)
for ti in TH8:
    nz, V = cos(2*ti), sin(2*ti); i = ket(ti)
    def born(tf): return 2*((ket(tf).T*i)[0])**2/pi           # normalised over tf in [0, pi)
    def num1(tf): f = ket(tf); return 2*(f.T*SZ*i)[0]*(f.T*i)[0]/pi        # A_w x weight, smooth
    def num2(tf): f = ket(tf); return 2*((f.T*SZ*i)[0])**2/pi               # A_w^2 x weight, smooth
    tot = quad(born, [0, pi/2, pi]); m1 = quad(num1, [0, pi/2, pi]); m2 = quad(num2, [0, pi/2, pi])
    var = m2 - m1**2
    errs = [fabs(tot - 1), fabs(m1 - nz), fabs(var - V**2), fabs(m2 - 1)]
    dmiss = mpf(0)
    for t0 in (mpf(-3), mpf('-0.5'), mpf(0), mpf('0.7'), mpf(4)):
        tfun = lambda tf: (nz - Aw_pure(ti, tf))/V
        root = findroot(lambda tf: tfun(tf) - t0, ti + atan(t0))
        dens = born(root)/fabs(diff(tfun, root))
        dmiss = max(dmiss, fabs(dens - 2/(pi*(1 + t0**2)**2)))
    errs.append(dmiss); w2 = max(w2, max(errs))
    print(f"  ti={nstr(ti,4)}: Born mean {nstr(m1,12)} (n_z {nstr(nz,12)}), var {nstr(var,12)} (V^2 {nstr(V**2,12)}), <A_w^2> {nstr(m2,15)}, density miss {nstr(dmiss,3)}")
print("worst", nstr(w2, 3)); mark('P2', w2 < mpf(10)**-30)
print("P2", "not killed" if verdict['P2'] else "KILLED")

print("\n== P3: a mixture loses the address's horizon, not its median ==")
worst = {'max': True, 'med': mpf(0), 'sw': mpf(0), 'mean': mpf(0)}; below1 = True
for k in range(12):
    r = mpf(rng.uniform(0.1, 0.95)); ang = mpf(rng.uniform(0.05, 3.09))    # n = r(sin ang, cos ang), n_x > 0
    nx, nz = r*sin(ang), r*cos(ang)
    g = lambda tf: Aw_mixed(nx, nz, tf)
    grid = [pi*j/4000 for j in range(4000)]; vals = [fabs(g(x)) for x in grid]
    j = max(range(4000), key=lambda q: vals[q]); a, b = grid[j] - pi/4000, grid[j] + pi/4000
    for _ in range(200):                                      # ternary search for the largest |A_w|
        m1, m2 = a + (b - a)/3, b - (b - a)/3
        if fabs(g(m1)) < fabs(g(m2)): a = m1
        else: b = m2
    mx = fabs(g((a + b)/2)); bound = (1 + fabs(nz))/(1 - r)
    med = 1 - share_above(g, nz)                              # share at or below n_z
    sw = share_above(lambda tf: g(tf)**2, 1); swp = atan(2*nx/(1 - r**2))/pi
    def p(tf): f = ket(tf); return (f.T*rho_of(nx, nz)*f)[0]
    def n1(tf): f = ket(tf); return (f.T*SZ*rho_of(nx, nz)*f)[0]
    Z = quad(p, [0, pi/2, pi]); bm = quad(n1, [0, pi/2, pi])/Z
    b2 = quad(lambda tf: n1(tf)**2/p(tf), [0, pi/4, pi/2, 3*pi/4, pi])/Z
    worst['max'] &= (mx <= bound); worst['med'] = max(worst['med'], fabs(med - mpf(1)/2))
    worst['sw'] = max(worst['sw'], fabs(sw - swp)); worst['mean'] = max(worst['mean'], fabs(bm - nz)); below1 &= (b2 < 1)
    print(f"  |n|={nstr(r,5)} n_x={nstr(nx,5)} n_z={nstr(nz,5)}: max|A_w| {nstr(mx,8)} (bound {nstr(bound,6)}), share<=n_z {nstr(med,15)}, "
          f"superweak {nstr(sw,12)} vs {nstr(swp,12)}, Born mean-n_z {nstr(bm-nz,3)}, Born <A_w^2> {nstr(b2,10)}")
print("worst:", {k: (v if isinstance(v, bool) else nstr(v, 3)) for k, v in worst.items()}, "all Born <A_w^2> < 1:", below1)
tol = mpf(10)**-25
mark('P3', worst['max'] and worst['med'] < tol and worst['sw'] < tol and worst['mean'] < tol and below1)
for r in (mpf('0.5'), mpf('0.9'), mpf('0.99'), mpf('0.999')):
    sw = share_above(lambda tf: Aw_mixed(r, 0, tf)**2, 1)
    print(f"  equator |n|={r}: superweak {nstr(sw,12)}, (2/pi)atan|n| {nstr(2*atan(r)/pi,12)}")
print("P3", "not killed" if verdict['P3'] else "KILLED")

print("\n== P4: without a phase reference the weak value adds levels ==")
worst = mpf(0)
for k in range(30):
    nz = mpf(rng.uniform(-0.95, 0.95)); tf = mpf(rng.uniform(0, 3.14159)); mz = cos(2*tf)
    worst = max(worst, fabs(Aw_mixed(0, nz, tf) - tanh(atanh(mz) + atanh(nz))))
print("identity to tanh(artanh m_z + artanh n_z), worst:", nstr(worst, 3)); mark('P4', worst < mpf(10)**-40)
for nz in (mpf('-0.8'), mpf('-0.3'), mpf(0), mpf('0.5'), mpf('0.9')):
    g = lambda tf: Aw_mixed(0, nz, tf)
    sw = share_above(lambda tf: g(tf)**2, 1); med = 1 - share_above(g, nz)
    print(f"  n_z={nz}: superweak share {nstr(sw,5)}, share <= n_z {nstr(med,15)}")
    mark('P4', sw == 0 and fabs(med - mpf(1)/2) < mpf(10)**-25)
print("P4", "not killed" if verdict['P4'] else "KILLED")

print("\n== P5: a fringe's arrivals read as addresses split by the visibility ==")
for V in (mpf(0), mpf('0.3'), mpf('0.7'), mpf(1)):
    def ft(t): return (1 + V*cos(2*atan(t)))/(2*pi) * 2/(1 + t**2)       # pushed forward from phi
    pred = lambda t: V*(2/pi)/(1 + t**2)**2 + (1 - V)/(pi*(1 + t**2))
    dm = max(fabs(ft(t) - pred(t)) for t in (mpf(-5), mpf(-1), mpf('0.2'), mpf(2), mpf(30)))
    med = quad(lambda ph: (1 + V*cos(ph))/(2*pi), [-pi, 0])               # share with t <= 0
    def M(T):
        edges = [mpf(0)] + [mpf(10)**e for e in range(0, int(mp.log10(T)) + 1)]
        return 2*sum(quad(lambda t: t*pred(t), [edges[j], edges[j+1]]) for j in range(len(edges) - 1))
    climb = M(mpf(10)**9) - M(mpf(10)**8); want = (1 - V)*(2/pi)*log(10)
    print(f"  V={V}: density miss {nstr(dm,3)}, share t<=0 {nstr(med,15)}, climb 1e8->1e9 {nstr(climb,12)} vs {nstr(want,12)} (off {nstr(climb-want,3)})")
    mark('P5', dm < mpf(10)**-30 and fabs(med - mpf(1)/2) < mpf(10)**-30 and fabs(climb - want) < mpf(10)**-6)
print("P5", "not killed" if verdict['P5'] else "KILLED")

print("\n== P6: the re-sort's bookkeeping ==")
med = quad(lambda t: 2/pi, [0, pi/4])
cl = (quad(lambda t: tan(t)*2/pi, [0, atan(mpf(10)**9)]) - quad(lambda t: tan(t)*2/pi, [0, atan(mpf(10)**8)]))
mV = quad(lambda t: sin(2*t)*2/pi, [0, pi/2]); mP = quad(lambda t: fabs(cos(2*t))*2/pi, [0, pi/4, pi/2])
qV = quad(lambda t: sin(2*t)**2*2/pi, [0, pi/2]); qP = quad(lambda t: cos(2*t)**2*2/pi, [0, pi/2])
print(f"  s: share <= 1 {nstr(med,15)}, climb {nstr(cl,12)} vs (2/pi)ln10 {nstr(2*log(10)/pi,12)}")
print(f"  V mean {nstr(mV,15)}, P mean {nstr(mP,15)} (2/pi {nstr(2/pi,15)}); mean squares {nstr(qV,15)}, {nstr(qP,15)}")
mark('P6', fabs(med - mpf(1)/2) < mpf(10)**-30 and fabs(cl - 2*log(10)/pi) < mpf(10)**-6 and
     max(fabs(mV - 2/pi), fabs(mP - 2/pi), fabs(qV - mpf(1)/2), fabs(qP - mpf(1)/2)) < mpf(10)**-30)
wt = mpf(0)
for k in range(5):
    th, al = mpf(rng.uniform(0.05, 1.5)), mpf(rng.uniform(0, 6.28))
    V, nz = sin(2*th), cos(2*th)
    for Nph in range(2, 8):
        pts = [(V*cos(al + 2*pi*j/Nph), V*sin(al + 2*pi*j/Nph)) for j in range(Nph)]
        each = max(fabs(sqrt(x*x + y*y) - V) for x, y in pts)
        avg = sqrt(sum(x for x, _ in pts)**2 + sum(y for _, y in pts)**2)/Nph
        wt = max(wt, each, avg)
print("  twirl: every member's |n_perp| = V and the average n_perp = 0, worst", nstr(wt, 3))
mark('P6', wt < mpf(10)**-30)
print("P6", "not killed" if verdict['P6'] else "KILLED")
print("\nverdicts:", {k: ('not killed' if v else 'KILLED') for k, v in verdict.items()})
