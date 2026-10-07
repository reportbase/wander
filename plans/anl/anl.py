"""ANL: a number line that recurses as needed. See plans/anl-plan.md (prediction and kill written before this).

    python3 plans/anl/anl.py
"""
import math

import numpy as np

N = 1000


def sets(seed=71):
    rng = np.random.default_rng(seed)
    E = (np.arange(N) + 0.5) / N
    U = rng.uniform(0, 1, N)
    centres = rng.uniform(0, 1 - 1e-6, 50)
    C = (centres[:, None] + rng.uniform(0, 1e-6, (50, 20))).ravel()
    return {'E': np.sort(E), 'U': np.sort(U), 'C': np.sort(C)}


def everywhere(x):
    g = np.diff(np.sort(x)).min()
    b = math.ceil(math.log2(1 / g))
    return len(x) * b, b


def where_needed(x):
    """Split [lo, lo + w) in half while it holds two or more; return (digits written, split marks, max depth)."""
    digits = splits = deepest = 0
    stack = [(np.sort(x), 0.0, 1.0, 0)]
    while stack:
        pts, lo, w, d = stack.pop()
        if len(pts) <= 1:
            digits += d * len(pts)
            deepest = max(deepest, d) if len(pts) else deepest
            continue
        splits += 1
        mid = lo + w / 2
        k = np.searchsorted(pts, mid)
        stack.append((pts[:k], lo, w / 2, d + 1))
        stack.append((pts[k:], mid, w / 2, d + 1))
    return digits, splits, deepest


if __name__ == '__main__':
    for name, x in sets().items():
        cost_e, b = everywhere(x)
        dig, spl, deep = where_needed(x)
        cost_n = dig + spl
        print(f'{name}: everywhere {cost_e} digits ({b} a number); where needed {dig} digits + {spl} splits = {cost_n} '
              f'(mean depth {dig / len(x):.1f}, deepest {deep}); ratio {cost_n / cost_e:.3f}')
