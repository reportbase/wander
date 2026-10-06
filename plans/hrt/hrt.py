"""HRT: the 2 of the central hypothesis, with h taken from the parent's record.

See plans/hrt-plan.md for the set-up, the prediction and the kill (written before this ran).

A reader stands on a landscape with its eye h above it, lays N rays evenly in direction over the lower half (both
facings) and records, for each, how many of its own h's along the ground the first meeting falls. Where neighbouring
rays jump outward by more than J, the first grazed a crest and the next landed beyond it: the stretch between is one
the reader could not see. A child stands on that crest with h = c * (the stretch's length). The reading is the ratio
h(parent) / h(child) for every hand-off past the first.

    python3 plans/hrt/hrt.py         run 1: chains of readers, the parent-to-child ratio
    python3 plans/hrt/hrt.py run2    run 2: single readers, the longest hidden stretch over h, across A and h
"""
import sys
import math
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
P, A = 64.0, 8.0
SIGNALS = [('2', 2.0, 7), ('3', 3.0, 5), ('phi', PHI, 10)]
SEEDS = [1, 2, 3]
N, J, HORIZON = 1440, 1.5, 64.0
MAX_LEVEL, PER_PARENT, MAX_READERS = 6, 3, 300
ROOT_X = [0.0, 101.3, -217.9, 333.1, -449.7]
ROOT_H = [P / 2, P / 3, P / 5]
CS = [1.0, 0.5, 2.0]


def landscape(r, K, seed, A=A):
    finest = P / r ** (K - 1)
    dx = finest / 16
    span = HORIZON * 4 * P + 600
    x = np.arange(-span, span, dx)
    phases = np.random.default_rng(seed).uniform(0, 2 * math.pi, K)
    y = sum(A * r ** -k * np.cos(2 * math.pi * r ** k * x / P + phases[k]) for k in range(K))
    return x, y, dx, finest


def read(x, y, dx, i0, h):
    """The reader's record: for each facing, rays from near-vertical out to near-horizontal, and where each first
    meets the ground, in the reader's own h's (nan past the horizon). Also the ground index of each meeting."""
    eye = y[i0] + h
    alphas = math.pi / 2 * (np.arange(N // 2) + 0.5) / (N // 2)       # depression below horizontal, even in direction
    alphas = alphas[::-1]                                              # near-vertical first, out toward the horizon
    out = []
    n = int(HORIZON * h / dx) + 1
    for step in (1, -1):
        idx = i0 + step * np.arange(1, n)
        idx = idx[(idx >= 0) & (idx < len(x))]
        dist = np.abs(x[idx] - x[i0])
        beta = np.arctan2(eye - y[idx], dist)       # depression of each ground point seen from the eye
        m = np.minimum.accumulate(beta)             # a ray at depression a meets the first point with beta <= a
        k = np.searchsorted(-m, -alphas, side='left')
        hit = k < len(idx)
        d = np.full(len(alphas), np.nan)
        gi = np.full(len(alphas), -1)
        d[hit] = dist[k[hit]] / h
        gi[hit] = idx[k[hit]]
        out.append((d, gi))
    return out


def hidden_stretches(record, h):
    """Hand-offs: neighbouring rays whose meetings jump outward by more than J. Returns (length, crest index)."""
    found = []
    for d, gi in record:
        for a in range(len(d) - 1):
            d0, d1 = d[a], d[a + 1]
            if np.isfinite(d0) and np.isfinite(d1) and d1 > J * d0:
                found.append(((d1 - d0) * h, gi[a]))
    found.sort(key=lambda t: -t[0])
    return found[:PER_PARENT]


def run(r, K, seed, c):
    x, y, dx, finest = landscape(r, K, seed)
    ratios = []
    for rx in ROOT_X:
        for rh in ROOT_H:
            queue = [(int(np.searchsorted(x, rx)), rh, 0)]
            readers = 0
            while queue and readers < MAX_READERS:
                i0, h, level = queue.pop(0)
                readers += 1
                if level >= MAX_LEVEL:
                    continue
                for L, crest in hidden_stretches(read(x, y, dx, i0, h), h):
                    hc = c * L
                    if hc < finest or hc > 4 * P:
                        continue
                    if level >= 1:
                        ratios.append(h / hc)
                    queue.append((int(crest), hc, level + 1))
    return ratios


def nearest_power(v, base):
    m = round(math.log(v) / math.log(base))
    return base ** m, m


def main():
    print(f'N={N} rays, J={J}, horizon {HORIZON:g} h, up to {PER_PARENT} children a parent, {MAX_LEVEL} levels')
    for c in CS:
        print(f'\nc = {c:g} (child h = c x the stretch its parent could not see)')
        print(f'{"signal":>7} {"pairs":>6} {"median":>8} {"IQR":>15}   {"nearest 2^m":>14} {"off":>6}   {"nearest r^m":>14} {"off":>6}   within 10% of 2?')
        for name, r, K in SIGNALS:
            ratios = [q for s in SEEDS for q in run(r, K, s, c)]
            if not ratios:
                print(f'{name:>7}      0')
                continue
            q = np.array(ratios)
            med = float(np.median(q))
            lo, hi = np.percentile(q, [25, 75])
            p2, m2 = nearest_power(med, 2)
            pr, mr = nearest_power(med, r)
            print(f'{name:>7} {len(q):6d} {med:8.3f} {lo:7.3f}-{hi:7.3f}   {p2:9.3f} (m={m2}) {abs(med / p2 - 1):5.1%}   '
                  f'{pr:9.3f} (m={mr}) {abs(med / pr - 1):5.1%}   {"yes" if abs(med / 2 - 1) <= 0.10 else "no"}')
            # the spread of the ratios on the signal's own scale: how many of r's levels each hand-off steps down
            steps = np.log(q) / math.log(r)
            hist = np.histogram(steps, bins=np.arange(-0.25, 4.0, 0.5))[0]
            print(f'{"":>7} ln(ratio)/ln(r) in half-level bins from 0: {" ".join(str(int(v)) for v in hist)}')


def run2():
    places = np.linspace(-1500, 1500, 20)
    hs = [P / 16 * 16 ** (i / 4) for i in range(5)]
    print('Run 2: median of L/h, L the longest stretch a reader cannot see (J = 1.5); rows A, columns h')
    for name, r, K in SIGNALS:
        print(f'\nsignal r = {name}')
        print(f'{"A":>5} ' + ' '.join(f'{"h=" + format(h, "g"):>9}' for h in hs))
        for amp in (4.0, 8.0, 16.0):
            cells = []
            for h in hs:
                vals = []
                for seed in SEEDS:
                    x, y, dx, _ = landscape(r, K, seed, amp)
                    for px in places:
                        st = hidden_stretches(read(x, y, dx, int(np.searchsorted(x, px)), h), h)
                        if st:
                            vals.append(st[0][0] / h)
                cells.append(f'{np.median(vals):6.2f}/{len(vals):<2d}' if vals else f'{"none":>9}')
            print(f'{amp:5g} ' + ' '.join(f'{c:>9}' for c in cells))
    print('\n(each cell: median L/h / readers with a hidden stretch, of 60)')


if __name__ == '__main__':
    run2() if sys.argv[1:] == ['run2'] else main()
