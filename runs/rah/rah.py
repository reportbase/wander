"""RAH run 1 (plans/rah-plan.md). Run from the repository's root: python3 runs/rah/rah.py"""
import itertools, math
import numpy as np
import sympy as sp

src = open('runs/tbh/tbh.py').read()
cut = src.index('# ---------------------------------------------------------------- P1')
g = {'__name__': 'rah'}
exec(compile(src[:cut], 'runs/tbh/tbh.py', 'exec'), g)
exec(compile(open('runs/tbh/tbh2.py').read().split('g = {')[0], 'x', 'exec'), {})   # nothing: keep tbh2's compose below


def compose(s, sk):            # run 2's composition, with the horizon given its address
    s = np.broadcast_to(s, np.broadcast(s, sk).shape).astype(float)
    sk = np.broadcast_to(sk, s.shape).astype(float)
    with np.errstate(divide='ignore', invalid='ignore'):
        u = (s - sk) / (1.0 + s * sk)
    den = 1.0 + s * sk
    u = np.where(den == 0.0, np.inf, u)
    with np.errstate(divide='ignore'):
        u = np.where(~np.isfinite(s), 1.0 / sk, u)
        u = np.where(~np.isfinite(sk), -1.0 / s, u)
    return u
g['compose'] = compose

MONO = [(a, b, c) for a in range(7) for b in range(7) for c in range(7) if a + b + c <= 6]
assert len(MONO) == 84


def mono_slopes(abc):
    a, b, c = abc
    def f(s1, s2):
        h = 1.0 / np.sqrt(1.0 + s1 * s1 + s2 * s2)
        return h ** a * (s1 * h) ** b * (s2 * h) ** c
    return f


def bridge(f, Nb, Na, S1, S2):
    sigj = g['beta_halfslopes'](Nb); tak = g['alpha_slopes'](Na)
    L1, L2 = g['leaf_screen'](sigj, tak)
    F = f(L1, L2)
    sig, ta = g['query_slopes'](S1, S2)
    Kb = g['kernel_u'](Nb, compose(sig[:, None], sigj[None, :]))
    Ka = g['kernel_u'](Na, compose(ta[:, None], tak[None, :]))
    return ((Kb @ F) * Ka).sum(1)


def bridge_dhv(abc, N, S1, S2):
    a, b, c = abc
    jb = (np.arange(N) + 0.5) * 2 * np.pi / N
    ka = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    B, A = np.meshgrid(jb, ka, indexing='ij')
    F = np.cos(A) ** a * (np.sin(A) * np.cos(B)) ** b * (np.sin(A) * np.sin(B)) ** c
    al = np.arctan(np.sqrt(S1 * S1 + S2 * S2)); be = np.arctan2(S2, S1)
    Kb = g['ktil'](N, (be[:, None] - jb[None, :]) / 2)
    Ka = g['ktil'](N, (al[:, None] - ka[None, :]) / 2)
    return ((Kb @ F) * Ka).sum(1)


S1, S2 = g['S1'], g['S2']
out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

even = [m for m in MONO if sum(m) % 2 == 0]
odd_h = [m for m in MONO if sum(m) % 2 == 1 and m[0] >= 1]
odd_0 = [m for m in MONO if sum(m) % 2 == 1 and m[0] == 0]
say(f'monomials: {len(even)} even degree, {len(odd_h)} odd with h, {len(odd_0)} odd without h')

errs = {}
for N in (16, 32, 64):
    for m in MONO:
        f = mono_slopes(m)
        errs[(m, N)] = float(np.abs(bridge(f, N, N, S1, S2) - f(S1, S2)).max())

r1 = max(errs[(m, N)] for m in even for N in (16, 32, 64))
say(f'R1: even degree, largest sup error over N = 16, 32, 64: {r1:.2e}')
say('R1', 'not killed' if r1 <= 1e-11 else 'KILLED')

ok2, worst_fall, least64 = True, 99.0, 1.0
for m in odd_h:
    e = [errs[(m, N)] for N in (16, 32, 64)]
    least64 = min(least64, e[2]); worst_fall = min(worst_fall, e[0] / e[1], e[1] / e[2])
    ok2 &= e[2] >= 1e-6 and e[0] / e[1] >= 1.6 and e[1] / e[2] >= 1.6
say(f'R2: odd with h: least error at N = 64 {least64:.2e}; least fall per doubling {worst_fall:.2f}')
for m in odd_h[:6]:
    say('   ', m, ['%.2e' % errs[(m, N)] for N in (16, 32, 64)])
say('R2', 'not killed' if ok2 else 'KILLED')

least3 = min(errs[(m, N)] for m in odd_0 for N in (16, 32, 64))
say(f'R3: odd without h, least sup error over N = 16, 32, 64: {least3:.3f}')
for m in odd_0[:6]:
    say('   ', m, ['%.3f' % errs[(m, N)] for N in (16, 32, 64)])
say('R3', 'not killed' if least3 >= 0.05 else 'KILLED')

r4 = 0.0
for m in MONO:
    a, b, c = m
    h = 1.0 / np.sqrt(1 + S1 * S1 + S2 * S2)
    truth = h ** a * (S1 * h) ** b * (S2 * h) ** c
    r4 = max(r4, float(np.abs(bridge_dhv(m, 16, S1, S2) - truth).max()))
say(f'R4: the DHV form at N = 16, largest sup error over all 84: {r4:.2e}')
say('R4', 'not killed' if r4 <= 1e-11 else 'KILLED')

s1, s2 = sp.symbols('s1 s2', real=True)
hs = 1 / sp.sqrt(1 + s1 ** 2 + s2 ** 2)
rational = {}
for m in MONO:
    a, b, c = m
    e = sp.simplify(hs ** a * (s1 * hs) ** b * (s2 * hs) ** c)
    rational[m] = not e.has(sp.sqrt) and not any(isinstance(p, sp.Pow) and not p.exp.is_integer for p in e.atoms(sp.Pow))
r5 = all(rational[m] == (sum(m) % 2 == 0) for m in MONO)
say(f'R5: rational in the slopes: {sum(rational.values())} of 84; the same set as even degree: {r5}')
say('R5', 'not killed' if r5 else 'KILLED')

calls_max = 0
for m in even:
    g['TRIG']['n'] = 0; g['counting'](True)
    bridge(mono_slopes(m), 16, 16, S1, S2)
    calls_max = max(calls_max, g['TRIG']['n']); g['counting'](False)
say(f'R6: trig calls on the read-alone path, most over the even monomials: {calls_max}')
say('R6', 'not killed' if calls_max == 0 else 'KILLED')
open('runs/rah/rah-run1.txt', 'w').write('\n'.join(out) + '\n')
