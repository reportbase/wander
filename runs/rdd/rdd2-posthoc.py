"""RDD run 2, post hoc (not a verdict): run 2's numbers with x taken, as the plan meant, from the counts
before the 20 mJy cut (run 2 took it from the cut sample, which flattens the slope at and below 20 mJy: my code)."""
import sys, numpy as np
src = open('runs/rdd/rdd2.py').read().split("base = srcok & (S >= 20)")[0]
g = {}; sys.argv = ['rdd2.py']
exec(compile(src, 'rdd2.py', 'exec'), g)
S, srcok, measure, xslope, xeff, sep, say = (g[k] for k in ('S', 'srcok', 'measure', 'xslope', 'xeff', 'sep', 'say'))
B, CW_BETA, CW_ERR = g['BETA_CMB'], g['CW_BETA'], g['CW_ERR']
base = srcok & (S >= 20)
W = measure(base)
x = xslope(20, srcok)
for a in (0.6, 0.75, 0.9):
    e = 2 + x * (1 + a)
    say(f"whole: x {x:.3f}, a {a}: 2 + x(1+a) {e:.3f}, beta-hat {W['D']/e:.3e} +- {W['e']/e:.3e} ({W['D']/e/B:.2f} x CMB)")
e = 2 + x * 1.75; bw, ebw = W['D'] / e, W['e'] / e
say(f"power: {ebw:.2e} against 1.0e-3 -> {'powered' if ebw < 1e-3 else 'still unpowered'}")
say(f"vs CatWISE {abs(bw-CW_BETA)/np.hypot(ebw, CW_ERR):.2f} sigma; vs CMB {abs(bw-B)/ebw:.2f} sigma")
bs, es = [], []
for S1, S2 in [(20, 40), (40, 80), (80, 160), (160, None)]:
    sel = base & (S >= S1) & ((S < S2) if S2 else True)
    M = measure(sel); xe = xeff(S1, S2, srcok); e = 2 + xe * 1.75
    bs.append(M['D'] / e); es.append(M['e'] / e)
    say(f"  {S1}-{S2 or 'up'}: x_eff {xe:.3f} beta/CMB {bs[-1]/B:.2f} +- {es[-1]/B:.2f}")
from scipy import stats
w = 1 / np.array(es) ** 2; m = np.sum(w * bs) / w.sum(); ch = np.sum(w * (np.array(bs) - m) ** 2)
say(f"  one beta {m/B:.2f} x CMB; chi2 {ch:.2f} on 3, p = {stats.chi2.sf(ch, 3):.3g}")
