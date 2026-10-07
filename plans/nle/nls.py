"""NLS: the number-line split, on synthetic readers. See plans/nls-plan.md (prediction and kill written before this).

Three kinds of reader, each placing the same 24 targets on a bounded line (0 to 100 marked) and an open one (0 and 10
marked, no end), scored with NLE's instrument (plans/nle/nle.py): the model with the lowest BIC on each line.

    python3 plans/nle/nls.py            # noise sd 8 (the run), then sd 4 and 12 (reported only)
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from nle import bic, cnr_basis, fit_cnr, fit_lin, fit_log, fit_pwr1, pwr1  # noqa: E402

N = 100.0
TARGETS = np.array([2, 3, 4, 6, 8, 12, 17, 21, 25, 29, 33, 39, 43, 48, 52, 57, 61, 64, 72, 79, 81, 84, 90, 96], float)
BOUNDED = {'LIN': fit_lin, 'LOG': fit_log, 'PWR1': fit_pwr1, 'CNR': fit_cnr}
OPEN = {'LIN': fit_lin, 'LOG': fit_log, 'CNR': fit_cnr}
EXPECT = {'S': ('CNR', 'CNR'), 'W': ('PWR1', 'LIN'), 'C': ('PWR1', 'CNR')}


def corner(h):
    """A corner reader with unit h, scaled so that 96 lands near 96, as NLE's self-test does."""
    a = 92.0 / cnr_basis(np.array([96.0]), h)[0]
    return 4.0 + a * cnr_basis(TARGETS, h)


def best(models, p):
    scores = {}
    for name, f in models.items():
        rss, k, par = f(TARGETS, p, N)
        scores[name] = (bic(rss, len(TARGETS), k), par)
    name = min(scores, key=lambda k: scores[k][0])
    return name, scores


def run(sd, seed=11, per=200):
    rng = np.random.default_rng(seed)
    out = {}
    for kind in 'SWC':
        hits = 0
        pairs = {}
        h_ok = h_n = 0
        for _ in range(per):
            h = float(np.exp(rng.normal(math.log(12), 0.45)))
            b = float(rng.uniform(0.5, 0.75))
            if kind == 'S':
                pb, po = corner(h), corner(h)
            elif kind == 'W':
                pb, po = pwr1(TARGETS, b, N), TARGETS * rng.uniform(0.95, 1.05)
            else:
                pb, po = pwr1(TARGETS, b, N), corner(h)
            pb = pb + rng.normal(0, sd, len(TARGETS))
            po = po + rng.normal(0, sd, len(TARGETS))
            wb, _ = best(BOUNDED, pb)
            wo, so = best(OPEN, po)
            pairs[(wb, wo)] = pairs.get((wb, wo), 0) + 1
            hits += (wb, wo) == EXPECT[kind]
            if kind in 'SC':
                h_n += 1
                hf = so['CNR'][1]['h']
                h_ok += 0.5 <= hf / h <= 2
        out[kind] = (hits, per, pairs, h_ok, h_n)
    return out


def report(sd, out, label):
    print(f'\nnoise sd {sd} ({label})')
    for kind, (hits, per, pairs, h_ok, h_n) in out.items():
        top = sorted(pairs.items(), key=lambda kv: -kv[1])[:4]
        tops = ', '.join(f'{a}/{b} {c}' for (a, b), c in top)
        hline = f'; open h within ×2: {h_ok}/{h_n}' if h_n else ''
        print(f'  {kind}: expected {EXPECT[kind][0]}/{EXPECT[kind][1]} recovered {hits}/{per} '
              f'({100 * hits / per:.0f}%){hline}   [most common: {tops}]')


if __name__ == '__main__':
    report(8, run(8), 'the run')
    for sd in (4, 12):
        report(sd, run(sd), 'reported only')
