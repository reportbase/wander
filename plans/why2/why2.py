"""WHY2: does the cheapest dial step by 2? See plans/why2-plan.md (prediction and kill written before this).

    python3 plans/why2/why2.py
"""
import math

import numpy as np

RHOS = [1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.5, 4, 5, 6, 8]
S0 = np.exp(np.linspace(math.log(2 ** -20), math.log(2 ** -2), 200))
TRIALS = 2000


def simulate(rho, s0, rng):
    """Mean cost ratio over TRIALS: look i costs rho**i, shows 'two' with probability min(s0*rho**i, 1)."""
    cost = np.zeros(TRIALS)
    alive = np.ones(TRIALS, bool)
    i = 0
    while alive.any():
        cost[alive] += rho ** i
        p = min(s0 * rho ** i, 1.0)
        alive &= rng.random(TRIALS) >= p
        i += 1
    return float(np.mean(cost * s0))


def exact(rho, s0):
    total, reach, i = 0.0, 1.0, 0
    while reach > 0:
        total += reach * rho ** i
        p = min(s0 * rho ** i, 1.0)
        reach *= 1 - p
        i += 1
    return total * s0


def run(seed=101):
    rng = np.random.default_rng(seed)
    out = []
    for rho in RHOS:
        sim = np.array([simulate(rho, s, rng) for s in S0])
        ex = np.array([exact(rho, s) for s in S0])
        out.append((rho, sim.mean(), sim.max(), ex.mean(), ex.max()))
    return out


if __name__ == '__main__':
    rows = run()
    print(f'{"rho":>5} {"mean ratio":>11} {"worst ratio":>12} {"(exact mean":>12} {"exact worst)":>13}')
    for r in rows:
        print(f'{r[0]:5.2f} {r[1]:11.3f} {r[2]:12.3f} {r[3]:12.3f} {r[4]:13.3f}')
    print('best rho, mean ratio:', min(rows, key=lambda r: r[1])[0], '| worst ratio:', min(rows, key=lambda r: r[2])[0])


def exact_confirm(rho, s0, k=3, luck=True):
    """Run 2: at grain i a look costs rho**i; a 'two' is confirmed by k-1 more looks there. Exact mean cost ratio."""
    total, reach, i = 0.0, 1.0, 0
    while reach > 1e-15:
        s = s0 * rho ** i
        p = min(s, 1.0) if luck else (1.0 if s >= 1 else 0.0)
        # first look always; each further confirming look only while all so far showed two
        looks = sum(p ** j for j in range(k))
        total += reach * looks * rho ** i
        reach *= 1 - p ** k
        i += 1
    return total * s0


def simulate_confirm(rho, s0, rng, k=3):
    cost = np.zeros(TRIALS)
    alive = np.ones(TRIALS, bool)
    i = 0
    while alive.any():
        p = min(s0 * rho ** i, 1.0)
        ok = alive.copy()
        for _ in range(k):
            cost[ok] += rho ** i
            ok &= rng.random(TRIALS) < p
        alive &= ~ok
        i += 1
    return float(np.mean(cost * s0))


def run2(seed=102):
    rng = np.random.default_rng(seed)
    out = []
    for rho in RHOS:
        sim = np.array([simulate_confirm(rho, s, rng) for s in S0])
        ex = np.array([exact_confirm(rho, s) for s in S0])
        nl = np.array([exact_confirm(rho, s, luck=False) for s in S0])
        out.append((rho, sim.mean(), sim.max(), ex.mean(), ex.max(), nl.mean(), nl.max()))
    return out
