"""CAL: observation costs calories. See plans/cal-plan.md (prediction and kill written before this).

    python3 plans/cal/cal.py
"""
import math

import numpy as np

SIG, KMAX, TRIALS = 0.2, 60, 20000
RS = (0.3, 0.5, 0.7)
VCS = [10.0 ** e for e in range(1, 7)]


def net(V, c, r, K):
    return V * (1 - r ** K) - c * K


def oracle(V, c, r):
    return max(range(KMAX + 1), key=lambda K: net(V, c, r, K))


def adaptive(V, c, r, rng):
    o_prev, k = None, 0
    o = math.exp(rng.normal(0, SIG))          # the first look: level 0, a0 = 1, free
    while k < KMAX:
        rh = 0.5 if o_prev is None else min(max(o / o_prev, 1e-6), 0.999)
        if V * o * (1 - rh) <= c:
            break
        k += 1
        o_prev, o = o, r ** k * math.exp(rng.normal(0, SIG))
    return k


def run(seed=91):
    rng = np.random.default_rng(seed)
    rows = []
    for r in RS:
        for vc in VCS:
            V, c = vc, 1.0
            ks = np.array([adaptive(V, c, r, rng) for _ in range(TRIALS)])
            n_ad = float(np.mean(V * (1 - r ** ks) - c * ks))
            K = oracle(V, c, r)
            rows.append((r, vc, ks.mean(), n_ad, net(V, c, r, K), K, net(V, c, r, 30), 0.0))
    return rows


if __name__ == '__main__':
    rows = run()
    for r in RS:
        sub = [x for x in rows if x[0] == r]
        slope = np.polyfit([math.log2(x[1]) for x in sub], [x[2] for x in sub], 1)[0]
        print(f'r = {r}: depth slope per doubling of V/c {slope:.3f} (predicted {1 / math.log2(1 / r):.3f})')
        for _, vc, d, na, no, K, ne, nn in sub:
            print(f'   V/c {vc:>9.0f}: adaptive depth {d:5.2f} net {na:10.2f} | oracle K*={K:2d} net {no:10.2f} '
                  f'(adaptive/oracle {na / no:.3f}) | everywhere {ne:10.2f} | never {nn:.0f}')
