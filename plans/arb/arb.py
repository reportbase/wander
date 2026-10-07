"""ARB: an arithmetic baseline. See plans/arb-plan.md (prediction and kill written before this).

    python3 plans/arb/arb.py
"""
import math
from fractions import Fraction as F
from math import isqrt

import numpy as np


def measure(x, d):
    """x measured to d decimals, rounded to nearest: the measured value and its half-width."""
    m = F(round(F(x) * 10 ** d), 10 ** d)
    return m, F(1, 2 * 10 ** d)


def column(rng, depths):
    true = rng.uniform(0, 10, len(depths))
    ms = [measure(x, int(d)) for x, d in zip(true, depths)]
    truth = sum(F(x) for x in true)
    return true, ms, truth


def task1(seed=81, cols=200, n=1000):
    rng = np.random.default_rng(seed)
    inside = dishonest = 0
    ratios = []
    fixed_err_claim = []
    for _ in range(cols):
        depths = rng.choice([1, 2, 6], n, p=[0.70, 0.25, 0.05])
        _, ms, truth = column(rng, depths)
        lo = sum(m - w for m, w in ms)
        hi = sum(m + w for m, w in ms)
        inside += lo <= truth <= hi
        fl = 0.0
        for m, _ in ms:
            fl += float(m)
        dishonest += abs(F(fl) - truth) > F(math.ulp(fl)) / 2
        rec = sum(1 + int(d) + 1 for d in depths)
        fix = n * (1 + int(depths.max()))
        ratios.append(rec / fix)
        fixed_err_claim.append(float(abs(sum(m for m, _ in ms) - truth)) / 0.5e-6)
    return inside, dishonest, cols, float(np.mean(ratios)), float(np.median(fixed_err_claim))


def task2():
    fl = (1e16 + 1) - 1e16
    exact = (F(10) ** 16 + 1) - F(10) ** 16
    return fl, exact


def task3(seed=82, n=1000):
    rng = np.random.default_rng(seed)
    depths = np.full(n, 3)
    _, ms, truth = column(rng, depths)
    rec = sum(1 + 3 + 1 for _ in depths)
    fix = n * (1 + 3)
    lo, hi = sum(m - w for m, w in ms), sum(m + w for m, w in ms)
    return rec / fix, lo <= truth <= hi


def task4():
    a_float = (0.1 + 0.2) == 0.3
    a_exact = F(1, 10) + F(2, 10) == F(3, 10)
    b_float = math.sqrt(2) * math.sqrt(2) == 2
    verdicts = []
    for k in range(1, 51):
        lo = F(isqrt(2 * 10 ** (2 * k)), 10 ** k)
        hi = lo + F(1, 10 ** k)
        sq_lo, sq_hi = lo * lo, hi * hi
        verdicts.append('undecided' if sq_lo < 2 < sq_hi else ('true' if sq_lo == sq_hi == 2 else 'false'))
    return a_float, a_exact, b_float, math.sqrt(2) * math.sqrt(2), sorted(set(verdicts))


if __name__ == '__main__':
    inside, dish, cols, ratio, fixmed = task1()
    print(f'task 1: recursing interval holds the truth in {inside}/{cols}; float error beyond its half-ulp in {dish}/{cols};'
          f' storage recursing/fixed {ratio:.3f}; fixed line error / its claimed 0.5e-6, median {fixmed:.0f}x')
    fl, ex = task2()
    print(f'task 2: float {fl}, exact {ex}')
    r3, ok3 = task3()
    print(f'task 3 (control): storage recursing/fixed {r3:.3f}; recursing interval holds the truth: {ok3}')
    af, ae, bf, bv, verd = task4()
    print(f'task 4: 0.1+0.2==0.3 float {af}, exact {ae}; sqrt2*sqrt2==2 float {bf} ({bv!r}); recursing at depths 1..50: {verd}')
