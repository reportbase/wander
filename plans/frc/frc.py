"""FRC: which ratios between levels can be precomputed? See plans/frc-plan.md (prediction and kill written before this).

A level is [0, 1]. Its named points start as {0, 1} and grow by the operations allowed. A nested level is the part between
two adjacent named points, rescaled to [0, 1], named by the same rules. Ratios are parent length over nested length.

    python3 plans/frc/frc.py
"""
import math

KEY = 12          # points are kept rounded to this many decimals
CAP = 400         # most named points kept on one level (arithmetic grows fast)


def k(x):
    return round(x, KEY)


def name_level(ops, sym):
    """The named points of one level, by the allowed operations, closed over a few rounds."""
    pts = {0.0, 1.0}
    if sym == 'fair':
        pts.add(0.5)                       # the flip's one fixed point: the corner
    # sym == 'nofair': maps f/(f + c(1 - f)) fix only 0 and 1, so nothing is added
    if 'free' in ops:
        pts.add(0.37)
    if 'pi' in ops:
        pts.add(2 / math.pi)
    for _ in range(3):
        new = set(pts)
        if sym == 'fair':
            new |= {k(1 - p) for p in pts}         # the flip
        if 'root' in ops:
            new |= {k(math.sqrt(p)) for p in pts}
        if 'arith' in ops:
            ps = sorted(pts)
            for a in ps:
                for b in ps:
                    for v in (a + b, a - b, a * b, a / b if b else 2):
                        if 0 < v < 1:
                            new.add(k(v))
        new = {k(p) for p in new}
        if len(new) > CAP:
            new = set(sorted(new)[:CAP])
        if new == pts:
            break
        pts = new
    return sorted(pts)


def ratios(ops, sym, depth):
    """Ratios of every level to each level nested directly in it, and to every descendant, to the given depth."""
    pts = name_level(ops, sym)            # every level is named the same way: the levels are precomputed alike
    parts = [b - a for a, b in zip(pts[:-1], pts[1:]) if b - a > 1e-12]
    adjacent = {k(1 / p) for p in parts}
    total = set(adjacent)
    frontier = list(parts)
    for _ in range(depth - 1):
        nxt = []
        for L in frontier:
            for p in parts:
                nxt.append(L * p)
        nxt = sorted(set(k(x) for x in nxt))[:5000]
        total |= {k(1 / x) for x in nxt if x > 0}
        frontier = nxt
    return pts, adjacent, total


def is_pow2(r):
    e = math.log2(r)
    return abs(e - round(e)) < 1e-9


def run():
    cases = [('base', set(), 'fair', 6),
             ('a free number', {'free'}, 'fair', 3),
             ('a root', {'root'}, 'fair', 3),
             ('arithmetic', {'arith'}, 'fair', 2),
             ("the sweep's constant", {'pi'}, 'fair', 3),
             ('no fairness', set(), 'nofair', 6)]
    out = []
    for name, ops, sym, depth in cases:
        pts, adj, tot = ratios(ops, sym, depth)
        nond = sorted(r for r in tot if not is_pow2(r))
        out.append((name, len(pts) - 2, sorted(adj), len(tot), nond))
    return out


if __name__ == '__main__':
    for name, interior, adj, ntot, nond in run():
        a = ', '.join(f'{r:.6g}' for r in adj[:8]) + (' …' if len(adj) > 8 else '')
        print(f'{name}: {interior} interior named points; adjacent ratios [{a}]; {ntot} ratios in all; '
              f'{len(nond)} not a power of 2' + (f', e.g. {", ".join(f"{r:.6g}" for r in nond[:6])}' if nond else ''))
    print('no symmetry at all: every point is fixed, so every point is named and every ratio is available (by definition)')


# ---- run 2: exact fractions, no cap; arithmetic two rounds, denominators to 64 ----
from fractions import Fraction as F

MAXDEN = 64


def name_exact(arith):
    pts = {F(0), F(1), F(1, 2)}
    pts |= {1 - p for p in pts}
    if arith:
        for _ in range(2):
            ps = sorted(pts)
            new = set(pts)
            for a in ps:
                for b in ps:
                    for v in (a + b, a - b, a * b) + ((a / b,) if b else ()):
                        if 0 < v < 1 and v.denominator <= MAXDEN:
                            new.add(v)
            new |= {1 - p for p in new}            # the flip, still
            pts = new
    return sorted(pts)


def ratios_exact(arith, depth):
    pts = name_exact(arith)
    parts = [b - a for a, b in zip(pts[:-1], pts[1:])]
    adjacent = {1 / p for p in parts}
    total, frontier = set(adjacent), list(parts)
    for _ in range(depth - 1):
        frontier = sorted({L * p for L in frontier for p in parts})[:20000]
        total |= {1 / x for x in frontier}
    return pts, adjacent, total


def primes_of(n):
    out, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            out.add(d)
            n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def run2():
    res = {}
    for name, arith, depth in (('base', False, 6), ('arithmetic', True, 2)):
        pts, adj, tot = ratios_exact(arith, depth)
        primes = set()
        for r in tot:
            primes |= primes_of(r.numerator) | primes_of(r.denominator)
        nond = [r for r in tot if not (r.denominator == 1 and r.numerator & (r.numerator - 1) == 0)]
        res[name] = {'interior': len(pts) - 2, 'adjacent': sorted(adj)[:10], 'n': len(tot), 'nondyadic': len(nond),
                     'primes': sorted(primes), 'has3': any(3 in primes_of(r.numerator) | primes_of(r.denominator) for r in tot),
                     'exact3': F(3) in tot}
    # the root row, in floating point: which forms of sqrt(2) appear among the ratios
    _, _, tot = ratios({'root'}, 'fair', 3)
    s2 = math.sqrt(2)
    forms = {'sqrt2': s2, '2+sqrt2': 2 + s2, '2+2sqrt2': 2 + 2 * s2, '2sqrt2': 2 * s2, '4+2sqrt2': 4 + 2 * s2,
             '4+4sqrt2': 4 + 4 * s2, '1+sqrt2': 1 + s2}
    res['root forms'] = sorted(k_ for k_, v in forms.items() if any(abs(r - v) < 1e-6 for r in tot))
    return res
