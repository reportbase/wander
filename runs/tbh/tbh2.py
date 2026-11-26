"""TBH run 2: P1 again with the horizon given its address (TB section 11.2). Run from the root."""
import sys, runpy, numpy as np
sys.argv = ['tbh']
# load run 1's definitions without running its checks: exec up to the P1 block
src = open('runs/tbh/tbh.py').read()
cut = src.index('# ---------------------------------------------------------------- P1')
g = {'__name__': 'tbh'}
exec(compile(src[:cut], 'runs/tbh/tbh.py', 'exec'), g)


def compose(s, sk):
    s = np.broadcast_to(s, np.broadcast(s, sk).shape).astype(float)
    sk = np.broadcast_to(sk, s.shape).astype(float)
    with np.errstate(divide='ignore', invalid='ignore'):
        u = (s - sk) / (1.0 + s * sk)
    den = 1.0 + s * sk
    u = np.where(den == 0.0, np.inf, u)
    with np.errstate(divide='ignore'):
        u = np.where(~np.isfinite(s), 1.0 / sk, u)        # t at the horizon: tan(pi/2 - t_k) = 1/s_k
        u = np.where(~np.isfinite(sk), -1.0 / s, u)       # the leaf at the horizon
    return u


g['compose'] = compose
out = []
ok_all = True
for N in (8, 16, 32, 64):
    g['TRIG']['n'] = 0
    g['counting'](True)
    a = g['alpha_slopes'](N); sb = g['beta_halfslopes'](N)
    node = max(np.abs(g['kernel_u'](N, compose(a[:, None], a[None, :])) - np.eye(N)).max(),
               np.abs(g['kernel_u'](N, compose(sb[:, None], sb[None, :])) - np.eye(N)).max())
    v1, Kb, Ka = g['bridge_slope']('g', N, N, g['S1'], g['S2'], return_K=True)
    pou = float(np.abs(Kb.sum(1) * Ka.sum(1) - 1).max())
    v2 = g['bridge_slope']('g', N, N, g['S1'], g['S2'], other=True)
    calls = g['TRIG']['n']
    g['counting'](False)
    inv = float(np.abs(v1 - v2).max())
    chart = float(np.abs(v1 - g['bridge_angle']('g', N, N, g['S1'], g['S2'])).max())
    ok = node <= 1e-12 and pou <= 1e-12 and inv <= 1e-12 and chart <= 1e-12 and calls == 0
    ok_all &= ok
    s = f'N={N}: node {node:.1e}  PoU {pou:.1e}  two reps {inv:.1e}  slope/angle {chart:.1e}  trig calls {calls}  {"ok" if ok else "KILLED"}'
    print(s); out.append(s)
out.append("P1' " + ('not killed' if ok_all else 'KILLED')); print(out[-1])
open('runs/tbh/tbh-run2.txt', 'w').write('\n'.join(out) + '\n')
