"""RDD run 1, post hoc (not a verdict): the same whole-sample fit with the one-sided mask (|b| > 16, dec > -39,
no antipode), the cut most NVSS dipole papers use, to see how much power the symmetric mask fixed in the plan gave up."""
import runpy, sys, numpy as np, healpy as hp
sys.argv = ['rdd.py'] + sys.argv[1:]
src = open('runs/rdd/rdd.py').read()
src = src.split("say('\\nWhole sample')")[0]
g = {}
exec(compile(src, 'rdd.py', 'exec'), g)
keep1 = g['ok1']
g['keep'][:] = keep1
srcok = (np.abs(g['b']) > 15) & (g['dec'] > -40) & (g['sc'] != 'U')
for S in (0.02, 0.04):
    base = srcok & (g['fn'] >= S - 1e-9) & keep1[g['pix']]
    M = g['measure'](base)
    x = g['xslope'](S, base); a = np.nanmean(g['alpha'][base]); ex = 2 + x * (1 + a)
    g['say'](f"one-sided mask, >= {S} Jy: N {M['N']} D {M['D']:.4f} (bootstrap {M['eb']:.4f}, jackknife {M['ej']:.4f}) "
             f"axis ({M['axis'][0]:.0f}, {M['axis'][1]:.0f}), {g['sep'](M['axis'], g['CMB']):.0f} from CMB, "
             f"{g['sep'](M['axis'], g['CW_AXIS']):.0f} from CatWISE; beta/CMB {M['D']/ex/g['BETA_CMB']:.2f}")
