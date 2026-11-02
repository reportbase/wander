"""PXS run 1: parallax as a sum of reads. Predictions in plans/pxs-plan.md, written first.
Run from the repository root: python3 runs/pxs/pxs.py"""
import numpy as np, mpmath as mp
N = 10**6
rng = np.random.default_rng(20261102)

def ccdf(x, m, g): return 0.5 + np.arctan((x - m) / g) / np.pi
def ks(sample, cdf):
    x = np.sort(sample); n = len(x); F = cdf(x)
    return max(np.max(np.arange(1, n+1)/n - F), np.max(F - np.arange(n)/n))
def hiqr(x): q1, q3 = np.quantile(x, [0.25, 0.75]); return (q3 - q1) / 2
def w(c, g): return (c + 1j*g) / (1 - 1j*g*c)
def reads(x, d, g, n):
    aA = np.arctan2(d, x + 1); aB = np.arctan2(d, 1 - x)   # interior angles
    dA = np.arctan(g * np.tan(np.pi*(rng.random(n) - 0.5)))
    dB = np.arctan(g * np.tan(np.pi*(rng.random(n) - 0.5)))
    return 1/np.tan(aA + dA), 1/np.tan(aB + dB)
def Dof(x, d, g):
    cA, cB = (x + 1)/d, (1 - x)/d
    return 2/np.conj(w(cA, g) + w(cB, g))

out = []; P = lambda *a: (print(*a), out.append(' '.join(map(str, a))))
killed = {}

P("X1: depth exactly Cauchy(D)")
ok = True
for g in [1e-3, 0.1, 0.3]:
    for (x, d) in [(0, 1/8), (0, .5), (0, 1), (0, 2), (0, 8), (.6, 1.5), (-2, 3)]:
        cA, cB = reads(x, d, g, N); dh = 2/(cA + cB); D = Dof(x, d, g)
        k = ks(dh, lambda t: ccdf(t, D.real, D.imag))
        pneg = np.mean(dh < 0); ppred = 0.5 - np.arctan(D.real/D.imag)/np.pi
        se = np.sqrt(ppred*(1-ppred)/N); z = (pneg - ppred)/se if se > 0 else 0
        good = k < 0.002 and abs(z) < 3; ok &= good
        P(f"  g={g} x={x} d={d}: D={D.real:.6f}+{D.imag:.6f}i KS={k:.5f} neg={pneg:.5f} pred={ppred:.5f} z={z:+.2f} {'ok' if good else 'FAIL'}")
killed['X1'] = not ok

P("X2: first-order law at gamma 0.3 vs 1e-3")
ok = True
for g in [0.3, 1e-3]:
    for d in [1, 8]:
        cA, cB = reads(0, d, g, N); dh = 2/(cA + cB)
        s = 2*g*np.cosh(np.log(d)); k = ks((dh - d)/d, lambda t: ccdf(t, 0, s))
        good = (k > 0.01) if g == 0.3 else (k < 0.002); ok &= good
        P(f"  g={g} k={d}: KS to first order={k:.5f} {'ok' if good else 'FAIL'}")
killed['X2'] = not ok

P("X3: |D| = d at the corner only (50 digits)")
mp.mp.dps = 50; ok = True
def Dmp(x, d, g):
    W = lambda c: (c + 1j*g)/(1 - 1j*g*c)
    return 2/mp.conj(W(mp.mpf(x + 1)/d) + W(mp.mpf(1 - x)/d))
for g in [mp.mpf('1e-3'), mp.mpf('0.1'), mp.mpf('0.3'), 1, 3]:
    D = Dmp(0, mp.mpf(1), g)
    e1 = abs(abs(D) - 1); e2 = abs(mp.arg(D) - 2*mp.atan(g)); good = e1 < 1e-40 and e2 < 1e-40; ok &= good
    P(f"  k=1 g={mp.nstr(g,3)}: ||D|-d|={mp.nstr(e1,3)} |argD-2atan g|={mp.nstr(e2,3)} {'ok' if good else 'FAIL'}")
for k in [mp.mpf(1)/8, mp.mpf(1)/2, 2, 8]:
    D = Dmp(0, k, mp.mpf('0.3')); r = abs(abs(D)/k - 1); good = r > 1e-3; ok &= good
    P(f"  k={mp.nstr(k,3)} g=0.3: |D|/d-1={mp.nstr(r,6)} {'ok' if good else 'FAIL'}")
killed['X3'] = not ok

P("X4: mean of reciprocal depths vs median of depths, g=0.1, k=1")
g = 0.1; M = 10**5; W1 = (w(1, g) + w(1, g))/2; ok = True; med1 = None
for n in [1, 10, 100]:
    cA, cB = reads(0, 1, g, M*n); dh = (2/(cA + cB)).reshape(M, n)
    mrec = (1/dh).mean(axis=1); med = np.median(dh, axis=1)
    h1 = hiqr(mrec); hm = hiqr(med)
    if n == 1: med1 = hm
    r = abs(h1/W1.imag - 1); good = r < 0.01; ok &= good
    P(f"  n={n}: HIQR mean 1/d = {h1:.5f} (law {W1.imag:.5f}, rel {r:.4f}) HIQR median d = {hm:.5f}")
good = med1/hm > 5 if hm else False; ok &= good
P(f"  median narrows n=1 -> 100 by {med1/hm:.2f}x {'ok' if good else 'FAIL'}")
killed['X4'] = not ok

P("X5: two uniform half turns")
aA = np.pi*rng.random(N); aB = np.pi*rng.random(N); dh = 2/(1/np.tan(aA) + 1/np.tan(aB))
ahead = dh > 0; p = ahead.mean(); z = (p - .5)/np.sqrt(.25/N); med = np.median(dh[ahead]); k = ks(dh, lambda t: ccdf(t, 0, 1))
ok = abs(z) < 3 and abs(med - 1) < 0.005 and k < 0.002
P(f"  ahead={p:.5f} z={z:+.2f} median ahead={med:.5f} KS to C(i)={k:.5f} {'ok' if ok else 'FAIL'}")
killed['X5'] = not ok

P("X6: two quarter turns")
aA = np.pi/2*rng.random(N); aB = np.pi/2*rng.random(N); dh = 2/(1/np.tan(aA) + 1/np.tan(aB))
med = np.median(dh); k = ks(dh, lambda t: 2/np.pi*np.arctan(t/med))
P(f"  all ahead={np.all(dh>0)} median={med:.5f} KS to half-Cauchy same median={k:.5f} {'ok' if k > 0.01 else 'FAIL'}")
killed['X6'] = not (k > 0.01)

P("X7: the place, k=1")
ok = True
for g in [1e-3, 0.3]:
    cA, cB = reads(0, 1, g, N); xh = (cA - cB)/(cA + cB)
    m = np.median(xh); s = hiqr(xh); k = ks(xh, lambda t: ccdf(t, m, s))
    good = (k < 0.002) if g == 1e-3 else (k > 0.005); ok &= good
    P(f"  g={g}: fitted m={m:.5f} s={s:.5f} KS={k:.5f} {'ok' if good else 'FAIL'}")
killed['X7'] = not ok

killed['X8'] = killed['X1']
P("VERDICTS: " + ', '.join(f"{k} {'KILLED' if v else 'not killed'}" for k, v in killed.items()))
open('runs/pxs/pxs-run1.txt', 'w').write('\n'.join(out) + '\n')
