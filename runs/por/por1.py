# POR run 1, P4–P5 (plans/por-plan.md), and the corner identities of "Known beforehand" (arithmetic, not tests).
# Usage: python3 runs/por/por1.py   (from the repository root). Seeded; exact up to floating point and erf.
import math, numpy as np, mpmath as mp
out = []
def say(s): out.append(s); print(s, flush=True)
rng = np.random.default_rng(20261022)
SIG, M, H, W = 1/8, 12, 1.0, 1/12           # pulse width, cells a level, H, the reader's first cell
SQ = math.sqrt(2*math.pi)

# ── the corner identities (exact, 40 digits) ──
mp.mp.dps = 40
for e in (mp.mpf(1), mp.mpf('0.96'), mp.mpf('0.8')):
    q = lambda r: (1+e)*r**3/(1+r**3); T = lambda r: (1+e)**2*r**3/(1+r**3)**2
    s1 = max(abs(q(r)+q(1/r)-(1+e)) for r in (mp.mpf('0.3'), mp.mpf(2), mp.mpf(7)))
    dq = mp.diff(lambda L: q(mp.e**L), 0); dT = mp.diff(lambda L: T(mp.e**L), 0); d2T = mp.diff(lambda L: T(mp.e**L), 0, 2)
    say(f"identity e={float(e)}: q(r)+q(1/r)-(1+e) {mp.nstr(s1,3)}; dq/dlnr at 1 {mp.nstr(dq,12)} (3(1+e)/4 = {mp.nstr(3*(1+e)/4,12)}); "
        f"T at 1 {mp.nstr(T(1),12)}, dT/dlnr {mp.nstr(dT,3)}, d2T {mp.nstr(d2T,12)} (-(9/8)(1+e)^2 = {mp.nstr(-mp.mpf(9)/8*(1+e)**2,12)}); T(r)=T(1/r) {mp.nstr(abs(T(mp.mpf(3))-T(mp.mpf(1)/3)),3)}")

# ── one dimension ──
def addr_edges(top):                        # the reader's address cells: m to [0, H], m to each doubling
    e = list(np.linspace(0, H, M+1)); j = 1
    while e[-1] < top:
        a = H*2**(j-1); e += list(a + np.arange(1, M+1)*a/M); j += 1
    return np.array(e)
def G(x, c): return 0.5*(1+np.vectorize(math.erf)((np.asarray(x)-c)/(SIG*math.sqrt(2))))   # Gaussian CDF (area 1)
def fold(edges, c):                          # cell averages of the unit-height pulse centred at c
    Cg = SIG*SQ*G(edges, c); return np.diff(Cg)/np.diff(edges)
def truth_read(c=None):                      # the truth's reading: the pulse's largest average over [0, W]
    c = W/2 if c is None else c
    return SIG*SQ*(G(W, c)-G(0, c))/W
def window_max(edges, u):                    # largest average over a window [x, x+W] of a piecewise-constant field, any x
    C = np.concatenate([[0], np.cumsum(u*np.diff(edges))])
    xs = np.concatenate([edges, edges-W]); vals = (np.interp(xs+W, edges, C)-np.interp(xs, edges, C))/W
    return vals.max()
NEG = -np.arange(1, 25)[::-1]*W              # cells past the reader, x < 0, each W wide

def stepped(edges, u, D0, finex=None, fine_dx=None):
    """hold the field on the cells, move it exactly toward 0 by s, re-total onto the cells; read [0, W] each step"""
    e = np.concatenate([NEG, edges]); u = np.concatenate([np.zeros(len(NEG)), u]); wd = np.diff(e)
    xc, best, t = D0, 0.0, 0
    while xc > -4*SIG:
        k = np.searchsorted(e, xc) - 1; k = min(max(k, 0), len(wd)-1)
        s = fine_dx if (finex is not None and xc < finex + 8*SIG) else max(0.5*wd[k], W/2)
        nz = np.nonzero(u > 1e-30*u.max())[0]; lo, hi = max(nz[0]-3, 0), min(nz[-1]+4, len(u))
        hi2 = len(u); 
        ee = e[lo:hi+1]; C = np.concatenate([[0], np.cumsum(u[lo:hi]*np.diff(ee))])
        lo2 = max(np.searchsorted(e, e[lo]-s)-2, 0)
        tgt = e[lo2:hi+1]
        Cn = np.interp(tgt+s, ee, C, left=0.0, right=C[-1])
        un = np.zeros_like(u); un[lo2:hi] = np.diff(Cn)/np.diff(tgt)
        u = un; xc -= s; t += 1
        C0 = np.concatenate([[0], np.cumsum(u*wd)]); r = (np.interp(W, e, C0)-np.interp(0, e, C0))/W
        best = max(best, r)
    return best, t

say("\nP4 (one dimension; sigma = 1/8, m = 12, H = 1; readings over the truth's largest average over [0, 1/12])")
tr = truth_read()
rows = []
for p in range(6, 13):
    D = 2**p*(1+rng.random(32)/8)
    for D0 in D:
        edges = addr_edges(D0+1)
        u = fold(edges, D0)
        rows.append((p, D0, window_max(edges, u)/tr))
P = np.array([r[0] for r in rows]); D = np.array([r[1] for r in rows]); R = np.array([r[2] for r in rows])
slope_a = np.polyfit(np.log2(D), np.log2(R), 1)[0]
a_ok = -1.03 <= slope_a <= -0.97
say(f"(a) folded at birth: slope {slope_a:.4f} (band [-1.03, -0.97])")
med_ok = True
for p in range(6, 13):
    med = np.median(R[P == p]); pred = SQ*SIG*M/2**(p-1); also = SQ*SIG*M/2**p
    ratio = med/pred; ok = abs(ratio-1) <= 0.03; med_ok &= ok
    say(f"    p = {p}: median {med:.5e}; plan's sqrt(2pi)sigma m/2^(p-1) {pred:.5e} (ratio {ratio:.4f}); over the birth cell's actual breadth 2^p/m: {also:.5e} (ratio {med/also:.4f})")
say(f"(a) {'not killed' if a_ok and med_ok else 'KILLED'} (slope in band: {a_ok}; medians within 3%: {med_ok})")

# (b), (c), (d) for p = 6 … 9
b_ok = c_ok = d_ok = True; bR = []; bD = []
for p in range(6, 10):
    for D0 in 2**p*(1+rng.random(6)/8):
        edges = addr_edges(D0+1); u = fold(edges, D0); ra = window_max(edges, u)/tr
        rb, nb = stepped(edges, u, D0); rb /= tr; bR.append(rb); bD.append(D0)
        if rb > ra*(1+1e-12): b_ok = False
        # (c) half way: cells of 1/24 inside x < D0/2, the address cells beyond
        X = D0/2; dx = 1/24
        fe = np.arange(0, int(X/dx)+1)*dx; ae = addr_edges(D0+1); ae = ae[ae > fe[-1]+1e-12]
        e2 = np.concatenate([fe, ae]); u2 = fold(e2, D0)
        rc, _ = stepped(e2, u2, D0, finex=fe[-1], fine_dx=dx); rc /= tr
        if rc > ra*(1+1e-12): c_ok = False
        # (c) from birth: cells of 1/96 to past the pulse, moved one cell a step (exact), against the truth at the same moments
        dx = 1/96; n = int((D0+8*SIG)/dx)+2; fe = np.arange(0, n+1)*dx
        uf = fold(fe, D0); best = 0.0; tbest = 0.0; xc = D0; shift = 0
        lo = max(int((D0-8*SIG)/dx), 0); seg = uf.copy()
        # rigid move by whole cells: after j steps the field is uf shifted j cells; read cells [0, 8) of the shifted field
        j0 = max(int((D0-1)/dx)-2, 0)
        for j in range(j0, int((D0+6*SIG)/dx)+1):
            idx = np.arange(8)+j
            r = uf[idx].mean() if idx[-1] < len(uf) else 0.0
            best = max(best, r); tbest = max(tbest, truth_read(D0-j*dx))
        relc = abs(best/tbest-1)
        if relc > 1e-9: c_ok = False
        # (d) the kind carried in: totals and centroids of the birth cells, a Gaussian of known sigma rebuilt
        Cg = SIG*SQ*G(edges, D0); Mi = np.diff(Cg)
        phi = np.exp(-(edges-D0)**2/(2*SIG**2))
        Xi = D0*Mi - SIG**2*np.diff(phi)          # integral of x times the pulse over each cell
        Mt = Mi.sum(); mu = Xi.sum()/Mt; amp = Mt/(SIG*SQ)
        rd = amp*truth_read(W/2)                  # the rebuilt pulse's largest average over [0, W]
        reld = abs(rd/tr-1) + abs(mu-D0)/D0
        if reld > 1e-9: d_ok = False
        say(f"    p = {p}, D0 = {D0:9.3f}: (a) {ra:.5e}  (b) {rb:.5e} in {nb} steps  (c, from D0/2) {rc:.5e}  (c, from birth) off {relc:.1e}  (d) off {reld:.1e}")
slope_b = np.polyfit(np.log2(bD), np.log2(bR), 1)[0]
say(f"(b) {'not killed' if b_ok and -1.3 <= slope_b <= -0.7 else 'KILLED'}: never above (a): {b_ok}; slope {slope_b:.4f} (band [-1.3, -0.7])")
say(f"(c) {'not killed' if c_ok else 'KILLED'}; (d) {'not killed' if d_ok else 'KILLED'}")

# ── P5, two dimensions: polar address cells, 96 angles round the turn ──
say("\nP5 (two dimensions; polar cells, radially as P4, 96 angles)")
NA = 96; h2 = SIG/20; g = np.arange(-6*SIG, 6*SIG+h2/2, h2); GX, GY = np.meshgrid(g, g)
wgt = np.exp(-(GX**2+GY**2)/(2*SIG**2))*h2*h2         # height 1, its total 2 pi sigma^2
rows2 = []
for p in range(6, 13):
    for _ in range(16):
        D0 = 2**p*(1+rng.random()/8); ph = rng.random()*2*np.pi
        X = D0*np.cos(ph)+GX; Y = D0*np.sin(ph)+GY; r = np.hypot(X, Y); a = np.mod(np.arctan2(Y, X), 2*np.pi)
        edges = addr_edges(D0+2); ri = np.searchsorted(edges, r)-1; ai = np.floor(a/(2*np.pi/NA)).astype(int)
        key = ri*NA+ai; mass = np.bincount(key.ravel(), weights=wgt.ravel())
        ks = np.nonzero(mass)[0]; rr = ks//NA
        area = 0.5*(2*np.pi/NA)*(edges[rr+1]**2-edges[rr]**2)
        rows2.append((p, D0, (mass[ks]/area).max()))
D2 = np.array([r[1] for r in rows2]); R2 = np.array([r[2] for r in rows2])
slope2 = np.polyfit(np.log2(D2), np.log2(R2), 1)[0]
for p in range(6, 13):
    sel = np.array([r[0] for r in rows2]) == p
    say(f"    p = {p}: median largest cell average over the blob's height {np.median(R2[sel]):.5e}")
say(f"P5: {'not killed' if -2.06 <= slope2 <= -1.94 else 'KILLED'}. slope {slope2:.4f} (band [-2.06, -1.94])")
open('runs/por/por-run1-fold.txt', 'w').write('\n'.join(out)+'\n')
