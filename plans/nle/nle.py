"""NLE: number-line estimation against the corner. See plans/nle-plan.md (prediction and kill written before any data).

Input: a CSV of trials, one row per estimate, with columns (names set by flags, defaults shown):
    participant   who made the estimate
    target        the number shown
    estimate      where it was placed, in the line's own numbers (0 to the line's end)
    age           optional: age or grade, for P2
    count_range   optional: how far the child counts, for P3
and the line's end, --max (e.g. 100 or 1000). Estimates given as a share of the line can be scaled with --scale.

Four models, fitted to each participant by least squares and compared by BIC:
    LIN   p = a·n + c
    LOG   p = a·ln n + c
    PWR1  p = N·n^b / (n^b + (N − n)^b)          (one-cycle power: proportion judgment)
    CNR   p = c + a·min(n, h) + a·h·ln(max(n, h)/h)   (proportion up to the corner h, a count of doublings past it)

    python3 plans/nle/nle.py data.csv --max 100
    python3 plans/nle/nle.py --selftest            # model recovery on made-up children; a calibration, not a result
"""
import argparse
import csv
import math
import sys
from collections import defaultdict

import numpy as np


def ols(X, y):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ beta
    return beta, float(r @ r)


def bic(rss, m, k):
    return k * math.log(m) + m * math.log(max(rss, 1e-12) / m)


def fit_lin(n, p, N):
    beta, rss = ols(np.column_stack([n, np.ones_like(n)]), p)
    return rss, 2, {'a': beta[0], 'c': beta[1]}


def fit_log(n, p, N):
    beta, rss = ols(np.column_stack([np.log(np.maximum(n, 1)), np.ones_like(n)]), p)
    return rss, 2, {'a': beta[0], 'c': beta[1]}


def pwr1(n, b, N):
    x = np.clip(n, 1e-9, N - 1e-9)
    return N * x ** b / (x ** b + (N - x) ** b)


def fit_pwr1(n, p, N):
    best = None
    for b in np.exp(np.linspace(math.log(0.05), math.log(5), 400)):
        r = p - pwr1(n, b, N)
        rss = float(r @ r)
        if best is None or rss < best[0]:
            best = (rss, b)
    return best[0], 1, {'b': best[1]}


def cnr_basis(n, h):
    return np.minimum(n, h) + h * np.log(np.maximum(n, h) / h)


def fit_cnr(n, p, N):
    best = None
    for h in np.exp(np.linspace(0, math.log(N), 300)):
        beta, rss = ols(np.column_stack([cnr_basis(n, h), np.ones_like(n)]), p)
        if best is None or rss < best[0]:
            best = (rss, h, beta)
    return best[0], 3, {'h': best[1], 'a': best[2][0], 'c': best[2][1]}


MODELS = {'LIN': fit_lin, 'LOG': fit_log, 'PWR1': fit_pwr1, 'CNR': fit_cnr}


def fit_person(n, p, N):
    out = {}
    for name, f in MODELS.items():
        rss, k, par = f(n, p, N)
        out[name] = {'bic': bic(rss, len(n), k), 'par': par}
    return out


def departs(f, N):
    """Departs from a straight line, by any model's account: LOG beats LIN; or PWR1 beats LIN with its exponent away
    from 1 (outside 0.8 to 1.25; at 1 it is a straight line); or CNR beats LIN with its corner inside the line (h < 0.8 N).
    Fair to both rivals: the self-test checks that made-up straight placers are left out and the others kept in."""
    lin = f['LIN']['bic']
    b = f['PWR1']['par']['b']
    return (f['LOG']['bic'] < lin
            or (f['PWR1']['bic'] < lin and not 0.8 <= b <= 1.25)
            or (f['CNR']['bic'] < lin and f['CNR']['par']['h'] < 0.8 * N))


def spearman(a, b):
    ra = np.argsort(np.argsort(a))
    rb = np.argsort(np.argsort(b))
    return float(np.corrcoef(ra, rb)[0, 1])


def analyse(people, N):
    """people: list of dicts {id, n, p, age?, count?}. Prints the verdicts the plan asks for."""
    rows = []
    for q in people:
        f = fit_person(np.asarray(q['n'], float), np.asarray(q['p'], float), N)
        best = min(f, key=lambda k: f[k]['bic'])
        rows.append({**q, 'fit': f, 'best': best})
    m = len(rows)
    print(f'{m} participants, line 0–{N:g}')
    for name in MODELS:
        print(f'  best by BIC: {name:5} {sum(r["best"] == name for r in rows):4d}')
    nonlin = [r for r in rows if departs(r['fit'], N)]
    k = len(nonlin)
    if k:
        cnr_beats_pwr = sum(r['fit']['CNR']['bic'] < r['fit']['PWR1']['bic'] for r in nonlin)
        cnr_beats_log = sum(r['fit']['CNR']['bic'] < r['fit']['LOG']['bic'] for r in nonlin)
        print(f'\nP1, over the {k} who depart from a straight line:')
        print(f'  CNR beats PWR1: {cnr_beats_pwr} ({cnr_beats_pwr / k:.0%}); PWR1 beats CNR: {k - cnr_beats_pwr} ({(k - cnr_beats_pwr) / k:.0%})')
        print(f'  (CNR beats LOG: {cnr_beats_log} ({cnr_beats_log / k:.0%}); reported, not part of the kill)')
        print(f'  P1: {"KILLED" if k - cnr_beats_pwr > k / 2 else "not killed"}')
    else:
        print('\nP1: no participant departs from a straight line; nothing to decide')
    hs = [r['fit']['CNR']['par']['h'] for r in rows]
    print(f'\nCNR corner h: median {np.median(hs):.1f} (IQR {np.percentile(hs, 25):.1f}–{np.percentile(hs, 75):.1f}) of a line to {N:g}')
    aged = [r for r in rows if r.get('age') is not None]
    if len(aged) >= 10:
        rho = spearman([r['age'] for r in aged], [r['fit']['CNR']['par']['h'] for r in aged])
        print(f'P2: Spearman(age, h) = {rho:+.2f} over {len(aged)}: {"KILLED" if rho < 0 else "not killed"}')
    else:
        print('P2: no age column (or fewer than 10 with one); not tested')
    counted = [r for r in rows if r.get('count') is not None and departs(r['fit'], N)]
    if len(counted) >= 10:
        within = sum(0.5 <= r['fit']['CNR']['par']['h'] / r['count'] <= 2 for r in counted)
        print(f'P3: h within a factor 2 of the counting range: {within} of {len(counted)} ({within / len(counted):.0%}): '
              f'{"not killed" if within > len(counted) / 2 else "KILLED"}')
    else:
        print('P3: no counting-range column (or fewer than 10); not tested')


def load(path, a):
    by = defaultdict(lambda: {'n': [], 'p': [], 'age': None, 'count': None})
    with open(path, newline='', encoding='utf-8-sig') as fh:
        for row in csv.DictReader(fh):
            try:
                n = float(row[a.target])
                p = float(row[a.estimate]) * a.scale
            except (KeyError, ValueError):
                continue
            q = by[row[a.participant]]
            q['n'].append(n)
            q['p'].append(p)
            for col, key in ((a.age, 'age'), (a.count, 'count')):
                if col and row.get(col) not in (None, ''):
                    try:
                        q[key] = float(row[col])
                    except ValueError:
                        pass
    return [{'id': pid, **q} for pid, q in by.items() if len(q['n']) >= 8]


def selftest():
    """Made-up children from each model, with noise; how often each is recovered. A calibration of the instrument."""
    rng = np.random.default_rng(7)
    N = 100.0
    targets = np.array([2, 3, 4, 6, 8, 12, 17, 21, 25, 29, 33, 39, 43, 48, 52, 57, 61, 64, 72, 79, 81, 84, 90, 96], float)
    gens = {
        'LIN': lambda: 0.9 * targets + 3,
        'LOG': lambda: 21 * np.log(targets) + 2,
        'PWR1': lambda: pwr1(targets, 0.6, N),
        'CNR': lambda: 4 + 2.2 * cnr_basis(targets, 12),
    }
    print('Model recovery, 200 made-up children per generating model, noise sd 8 (a calibration, not a result):')
    print(f'{"made as":>8} ' + ' '.join(f'{k:>6}' for k in MODELS) + '   (best by BIC)')
    for g, make in gens.items():
        counts = {k: 0 for k in MODELS}
        comp = [0, 0, 0]
        for _ in range(200):
            p = make() + rng.normal(0, 8, len(targets))
            f = fit_person(targets, p, N)
            counts[min(f, key=lambda k: f[k]['bic'])] += 1
            if departs(f, N):
                comp[0] += 1
                comp[1] += f['CNR']['bic'] < f['PWR1']['bic']
                comp[2] += f['PWR1']['bic'] < f['CNR']['bic']
        print(f'{g:>8} ' + ' '.join(f'{counts[k]:6d}' for k in MODELS) + f'   depart {comp[0]:3d}: CNR beats PWR1 {comp[1]:3d}, PWR1 beats CNR {comp[2]:3d}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('csv', nargs='?')
    ap.add_argument('--max', type=float)
    ap.add_argument('--participant', default='participant')
    ap.add_argument('--target', default='target')
    ap.add_argument('--estimate', default='estimate')
    ap.add_argument('--age', default='age')
    ap.add_argument('--count', default='count_range')
    ap.add_argument('--scale', type=float, default=1.0)
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.csv or not a.max:
        ap.error('give a CSV and --max (the line\'s end)')
    people = load(a.csv, a)
    if not people:
        sys.exit('no participant with 8 or more usable trials; check the column names')
    analyse(people, a.max)


if __name__ == '__main__':
    main()
