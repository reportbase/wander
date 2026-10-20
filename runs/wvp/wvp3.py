"""WVP run 3, real data (plans/wvp-plan.md): single photons building a double-slit pattern, Aspden, Padgett and
Spalding 2016 (doi:10.5525/gla.researchdata.281, CC BY 4.0). Q1 the fringe period against f·λ/d, Q2 the pattern built
at √N, Q3 the phase found by count with the spread the pattern sets, Q4 the contrast at most the pair's facing 2hv.
Run: python3 -I runs/wvp/wvp3.py <folder holding the inner zips of Video_data.zip>   (numpy, scipy; about ten minutes)
"""
import sys, os, zipfile
import numpy as np
from math import pi, sqrt
from scipy.optimize import minimize

SRC = sys.argv[1]
SETS = {'D_SM': 'Heralded Diffraction SM.zip', 'D_MM': 'Heraded DIffraction MM.zip', 'I_SM': 'Heralded Imaing SM .zip',
        'G_SM': 'Ghost Diffraction SM.zip', 'GI_SM': 'Ghost Imaging SM.zip'}

def arrivals(name):
    """Every frame's new arrivals as (frame, row, col), a gain of k counted k times; cached beside the data."""
    cache = os.path.join(SRC, name + '.npz')
    if os.path.exists(cache):
        return np.load(cache)['a']
    z = zipfile.ZipFile(os.path.join(SRC, SETS[name])); out = []
    names = sorted(n for n in z.namelist() if n.lower().endswith('.asc'))
    prev = np.zeros((512, 512), dtype=np.int32)
    for f, n in enumerate(names):
        img = np.array(z.read(n).split(), dtype=np.int32).reshape(512, 512)
        new = img - prev; prev = img       # the frames are cumulative: a frame's arrivals are its gain on the last
        assert new.min() >= 0, (name, n)
        r, c = np.nonzero(new)
        k = new[r, c]
        out.append(np.column_stack([np.full(k.sum(), f), np.repeat(r, k), np.repeat(c, k)]))
    a = np.concatenate(out); np.savez_compressed(cache, a=a); return a

def order(a):
    """By frame, within a frame shuffled (seed 0)."""
    rng = np.random.default_rng(0)
    return a[np.lexsort((rng.random(len(a)), a[:, 0]))]

def axis_of(a):
    """The axis (1 rows, 2 columns) whose summed profile has more power at periods 30–90 px."""
    best = None
    for ax in (1, 2):
        p = np.bincount(a[:, ax], minlength=512).astype(float); p -= p.mean()
        F = np.abs(np.fft.rfft(p))**2; fr = np.fft.rfftfreq(512)
        band = (fr >= 1/90) & (fr <= 1/30)
        pw = F[band].max()
        if best is None or pw > best[1]:
            best = (ax, pw, 1 / fr[band][F[band].argmax()])
    return best[0], best[2]

X = np.arange(512.)

def model(q):
    B, A, x0, W, C, P, d = q
    return B + A * np.sinc((X - x0) / W)**2 * (1 + C * np.cos(2*pi*(X - x0)/P + d))

def fit(prof, P0, q0=None):
    """Poisson maximum likelihood of the seven parameters."""
    if q0 is None:
        x0 = (prof * X).sum() / prof.sum()
        q0 = [max(prof.min(), 0.1), prof.max() / 1.5, x0, 5 * P0, 0.5, P0, 0.0]
        best = None
        for d0 in np.linspace(-pi, pi, 8, endpoint=False):   # start the phase at eight places, keep the best
            q0[6] = d0; r = fit(prof, P0, list(q0))
            if best is None or r[1] < best[1]:
                best = r
        return best
    def nll(q):
        m = model(q)
        if np.any(m <= 0) or q[4] < 0 or q[4] > 1.5 or q[3] <= 0:
            return 1e30
        return (m - prof * np.log(m)).sum()
    r = minimize(nll, q0, method='Nelder-Mead', options={'maxiter': 40000, 'maxfev': 40000, 'xatol': 1e-7, 'fatol': 1e-9})
    r = minimize(nll, r.x, method='Nelder-Mead', options={'maxiter': 40000, 'maxfev': 40000, 'xatol': 1e-8, 'fatol': 1e-10})
    q = r.x.copy(); q[6] = (q[6] + pi) % (2*pi) - pi
    return q, r.fun

def boot(a, ax, f, nb=200, seed=1):
    """f(profile) over resamples of frames."""
    rng = np.random.default_rng(seed); fr = a[:, 0]; nf = fr.max() + 1
    per = np.zeros((nf, 512)); np.add.at(per, (fr, a[:, ax]), 1)
    return np.array([f(per[rng.integers(0, nf, nf)].sum(0)) for _ in range(nb)])

def ks(block, rest):
    cb = np.cumsum(np.bincount(block, minlength=512)) / len(block)
    cr = np.cumsum(np.bincount(rest, minlength=512)) / len(rest)
    return np.abs(cb - cr).max()

res, verdict = {}, {}
fl = 0.5 * 710e-9 / 500e-6 / 12.70e-6
print(f"f·λ/d at 12.70 µm a pixel: {fl:.2f} px")
for name in ('D_SM', 'D_MM', 'G_SM'):
    a = order(arrivals(name)); M = len(a); ax, Pf = axis_of(a)
    prof = np.bincount(a[:, ax], minlength=512).astype(float)
    q, _ = fit(prof, Pf)
    bq = boot(a, ax, lambda p: fit(p, Pf, list(q))[0])
    se = bq.std(0, ddof=1)
    print(f"\n{name}: {M} arrivals in {a[:,0].max()+1} frames; fringe axis {'rows' if ax==1 else 'columns'}, "
          f"Fourier period {Pf:.1f} px")
    for k, s in zip('B A x0 W C P δ'.split(), range(7)):
        print(f"  {k} = {q[s]:.4f} ± {se[s]:.4f}")
    x = a[:, ax]
    # Q2
    Ns, Ds = [], []
    N = 25
    while N <= M // 16:
        nb = M // N; d = []
        for b in range(nb):
            blk = x[b*N:(b+1)*N]; rest = np.concatenate([x[:b*N], x[(b+1)*N:]])
            d.append(ks(blk, rest))
        Ns.append(N); Ds.append(np.mean(d)); N *= 2
    slope = np.polyfit(np.log(Ns), np.log(Ds), 1)[0]
    rise = (sqrt(Ns[-1]) * Ds[-1]) / (sqrt(Ns[0]) * Ds[0])
    print("  Q2: N, √N·mean D: " + ", ".join(f"{n} {sqrt(n)*dd:.3f}" for n, dd in zip(Ns, Ds)))
    print(f"  Q2: slope {slope:.4f}; √N·mean D largest/smallest {rise:.3f}")
    q2 = (-0.55 <= slope <= -0.45) and rise <= 1.2
    # Q3
    phi = 2*pi*(x - q[2]) / q[5] + q[6]
    c, s2 = np.cos(phi).mean(), (np.sin(phi)**2).mean()
    pred = sqrt(s2) / c
    q3 = True
    print(f"  Q3: ⟨cos φ⟩ {c:.4f}, ⟨sin² φ⟩ {s2:.4f}, predicted √N·sd(φ̂) {pred:.4f} (√2/C {sqrt(2)/q[4]:.4f})")
    for N in (50, 100, 200):
        nb = M // N
        e = np.exp(1j * phi[:nb*N]).reshape(nb, N).sum(1)
        ang = np.angle(e * np.exp(-1j * np.angle(e.sum())))
        got = sqrt(N) * ang.std(ddof=1); tol = 3 / sqrt(2 * (nb - 1))
        ok = abs(got / pred - 1) <= tol; q3 &= ok
        print(f"  Q3: N {N}, {nb} blocks: √N·sd {got:.4f}, ratio {got/pred:.4f}, allowed ±{tol:.4f} {'ok' if ok else 'OUT'}")
    res[name] = dict(q=q, se=se, ax=ax, q1=abs(q[5]/fl - 1) <= 0.10, q2=q2, q3=q3)
    print(f"  Q1: P {q[5]:.3f} px, ratio to f·λ/d {q[5]/fl:.4f}")

def shares(name, ax):
    a = arrivals(name)
    def two(p):
        B = np.concatenate([p[:128], p[384:]]).mean()
        sm = np.convolve(p, np.ones(5) / 5, 'same'); inner = np.arange(128, 384)
        i1 = inner[sm[inner].argmax()]
        far = inner[np.abs(inner - i1) >= 10]; i2 = far[sm[far].argmax()]
        lo, hi = sorted((i1, i2)); cut = lo + sm[lo:hi+1].argmin()
        n1 = (p[128:cut] - B).sum(); n2 = (p[cut:384] - B).sum()
        h, v = sqrt(n1 / (n1 + n2)), sqrt(n2 / (n1 + n2))
        return np.array([2*h*v, n1, n2, B, lo, hi, cut])
    prof = np.bincount(a[:, ax], minlength=512).astype(float)
    r = two(prof); b = boot(a, ax, two)
    print(f"\n{name}: {len(a)} arrivals; stripes at {r[4]:.0f} and {r[5]:.0f} px, split at {r[6]:.0f}; background "
          f"{r[3]:.3f} a pixel; n₁ {r[1]:.0f}, n₂ {r[2]:.0f}; 2hv = {r[0]:.5f} ± {b[:,0].std(ddof=1):.5f}")
    return r[0], b[:, 0].std(ddof=1)

f1, sf1 = shares('I_SM', res['D_SM']['ax'])
f2, sf2 = shares('GI_SM', res['G_SM']['ax'])
C = {k: (res[k]['q'][4], res[k]['se'][4]) for k in res}
z1 = (C['D_SM'][0] - f1) / sqrt(C['D_SM'][1]**2 + sf1**2)
z2 = (C['G_SM'][0] - f2) / sqrt(C['G_SM'][1]**2 + sf2**2)
z3 = (C['D_SM'][0] - C['D_MM'][0]) / sqrt(C['D_SM'][1]**2 + C['D_MM'][1]**2)
print(f"\nQ4: C(D_SM) {C['D_SM'][0]:.4f} against 2hv(I_SM) {f1:.4f}: (C − 2hv)/se = {z1:.2f}; |γ| ≈ {C['D_SM'][0]/f1:.4f}")
print(f"Q4: C(G_SM) {C['G_SM'][0]:.4f} against 2hv(GI_SM) {f2:.4f}: (C − 2hv)/se = {z2:.2f}; |γ| ≈ {C['G_SM'][0]/f2:.4f}")
print(f"Q4: C(D_MM) {C['D_MM'][0]:.4f}, below C(D_SM) by {z3:.2f} se")
print("\nQ1", 'not killed' if res['D_SM']['q1'] and res['G_SM']['q1'] else 'KILLED')
print("Q2", 'not killed' if all(res[k]['q2'] for k in res) else 'KILLED')
print("Q3", 'not killed' if res['D_SM']['q3'] and res['G_SM']['q3'] else 'KILLED')
print("Q4", 'not killed' if z1 <= 3 and z2 <= 3 and z3 >= 3 else 'KILLED')
