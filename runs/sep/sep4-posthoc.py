"""SEP run 4, post hoc (SPN R1279). Run from the root: python3 runs/sep/sep4-posthoc.py"""
import mpmath as mp, importlib.util, sys
spec = importlib.util.spec_from_file_location("s4", "runs/sep/sep4.py")
src = open("runs/sep/sep4.py").read().split("# T1")[0]          # the definitions only
ns = {}; exec(src, ns); mp.mp.dps = 30
out = []
def say(s): print(s, flush=True); out.append(s)
pair, bound, C = ns['pair'], ns['bound'], ns['C']
def draws(zs):                         # run 2's draws bound, recomputed at full precision (mixture of Cauchy draws)
    w = mp.mpf('0.5')
    def sc(x):
        p1, p2 = C(x, zs[0]), C(x, zs[1]); p = w * p1 + (1 - w) * p2
        g1 = ns['grads'](x, zs[0], 1)[:2]; g2 = ns['grads'](x, zs[1], 1)[:2]
        return [w * g1[0] / p, w * g1[1] / p, (1 - w) * g2[0] / p, (1 - w) * g2[1] / p, (p1 - p2) / p], p
    F = mp.matrix(5, 5)
    for i in range(5):
        for j in range(i, 5):
            h = lambda t: (lambda s, p: s[i] * s[j] * p)(*sc(mp.tan(t))) / mp.cos(t) ** 2
            F[i, j] = F[j, i] = mp.quad(h, mp.linspace(-mp.pi / 2, mp.pi / 2, 13))
    return mp.sqrt((F ** -1)[4, 4])
for d in ('1.5', '2.0', '3.0'):
    zs = pair(mp.mpf(d), mp.mpf(1)); a, b = bound(zs, 'count'), draws(zs)
    say(f"d = {d}: counts {mp.nstr(a, 20)}, draws at full precision {mp.nstr(b, 20)}, apart {mp.nstr(abs(a - b) / b, 3)}")
# the turn-laid bound as the d = 1.5, r = 1 pair is carried away from i by a dilation (a hyperbolic step D from i)
base = pair(mp.mpf('1.5'), mp.mpf(1)); b0 = bound(base, 'count')
for D in ('0', '0.5', '1', '2', '3'):
    k = mp.e ** mp.mpf(D); zs = [z * k for z in base]
    say(f"carried {D} from i: turn-laid {mp.nstr(bound(zs, 'turn'), 10)}, even in frequency {mp.nstr(bound(zs, 'freq'), 10)}, counts {mp.nstr(bound(zs, 'count'), 10)} (the draws' {mp.nstr(b0, 10)})")
open('runs/sep/sep4-posthoc-out.txt', 'w').write('\n'.join(out) + '\n')
