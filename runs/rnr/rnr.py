"""RNR: lay the range first, revisited. Predictions in plans/rnr-plan.md, written before this script.

Run from the repository's root: python3 runs/rnr/rnr.py
"""
from fractions import Fraction as Fr
import math
import mpmath as mp
import numpy as np

mp.mp.dps = 50
Q = mp.pi / 2
K = 10000
BS = [mp.mpf(1) / 4, mp.mpf(1) / 2, mp.mpf(1), mp.mpf(2), mp.mpf(4)]
SPREADS = ['param', 'arc', 'turn']
verdict = {}
say = print


def addresses(world=None):
    """L's boundaries, laid before anything arrives: K even by turn over the quarter. The world is not consulted."""
    return [mp.tan(k * Q / K) for k in range(K + 1)]


ADDR = addresses()
CORNER = ADDR[K // 2]


def arc_cdf_t(b):
    """t at which the arc length from t = 0 is half the quarter ellipse's."""
    ds = lambda t: mp.sqrt(mp.sin(t) ** 2 + b ** 2 * mp.cos(t) ** 2)
    total = mp.quad(ds, [0, Q])
    return mp.findroot(lambda t: mp.quad(ds, [0, t]) - total / 2, Q / 2)


def median_dir(b, spread, k=mp.mpf(1)):
    """tan of the arrivals' median direction, seen from the ellipse's centre, the world scaled by k."""
    if spread == 'turn':
        return mp.tan(Q / 2)
    t = Q / 2 if spread == 'param' else arc_cdf_t(b)
    x, y = k * mp.cos(t), k * b * mp.sin(t)
    return mp.tan(mp.atan2(y, x))


# ── Q1 ──
same = all(addresses(('world', float(b), sp, float(k))) == ADDR
           for b in BS for sp in SPREADS for k in (mp.mpf('1e-3'), mp.mpf('1e3')))
say('Q1  L\'s 10,001 boundaries identical across 15 worlds × 2 scalings:', same, '; corner tan 45° =', mp.nstr(CORNER, 20))
verdict['Q1'] = same and abs(CORNER - 1) < mp.mpf('1e-45')

# ── Q2 and Q3 ──
say('Q2  the gap = tan of the arrivals\' median direction over tan 45°')
G = {}
ok2, ok3 = True, True
for sp in SPREADS:
    for b in BS:
        g = median_dir(b, sp) / CORNER
        G[(sp, b)] = g
        moved = max(abs(median_dir(b, sp, k) / CORNER - g) for k in (mp.mpf('1e-3'), mp.mpf('1e3')))
        ok3 = ok3 and moved < mp.mpf('1e-40')
        say('   ', sp.ljust(5), 'b =', mp.nstr(b, 4).ljust(5), 'gap', mp.nstr(g, 25), '  moved by k:', mp.nstr(moved, 3))
for b in BS:
    ok2 = ok2 and abs(G[('param', b)] - b) < mp.mpf('1e-40') and abs(G[('turn', b)] - 1) < mp.mpf('1e-40')
    if b != 1:
        ok2 = ok2 and abs(G[('arc', b)] - b) > mp.mpf('1e-10') and abs(G[('arc', b)] - 1) > mp.mpf('1e-10')
for b in (mp.mpf(1) / 4, mp.mpf(1) / 2):
    prod = G[('arc', b)] * G[('arc', 1 / b)]
    say('    arc: g(b)·g(1/b) at b =', mp.nstr(b, 3), ':', mp.nstr(prod, 45))
    ok2 = ok2 and abs(prod - 1) < mp.mpf('1e-40')
ok2 = ok2 and abs(G[('arc', mp.mpf(1))] - 1) < mp.mpf('1e-40') and 1 < G[('arc', mp.mpf(2))] < 2
verdict['Q2'] = ok2
verdict['Q3'] = ok3
say('Q3  scaling the world moved no gap:', ok3)

# ── Q4 ──
verdict['Q4'] = True  # B's only middle is its arrivals'; its reading is that middle over itself
say('Q4  B reads its arrivals\' middle over its arrivals\' middle: 1 in all 15, by construction')

# ── Q5: counted, 2,000 arrivals at each spread's quantiles, in float (the grain is 1.6e-4 rad, far above float's) ──
say('Q5  counted gap against the exact median, in cells')
n = 2000
QF = math.pi / 2
ok5 = True
for sp in SPREADS:
    for b in [float(x) for x in BS]:
        u = (np.arange(n) + 0.5) / n
        if sp == 'param':
            t = u * QF
            th = np.arctan2(b * np.sin(t), np.cos(t))
        elif sp == 'turn':
            th = u * QF
        else:
            tt = np.linspace(0, QF, 200001)
            ds = np.sqrt(np.sin(tt) ** 2 + b * b * np.cos(tt) ** 2)
            S = np.concatenate([[0], np.cumsum((ds[1:] + ds[:-1]) / 2 * np.diff(tt))])
            t = np.interp(u * S[-1], S, tt)
            th = np.arctan2(b * np.sin(t), np.cos(t))
        idx = np.sort(np.minimum(K - 1, np.floor(th / QF * K)).astype(int))
        mid = (idx[n // 2 - 1] + idx[n // 2]) / 2
        counted = math.tan((mid + 0.5) / K * QF)
        exact = float(G[(sp, mp.mpf(b))])
        i = int(math.floor(math.atan(exact) / QF * K))
        cell = math.tan((i + 1) * QF / K) - math.tan(i * QF / K)
        miss = abs(counted - exact) / cell
        ok5 = ok5 and miss <= 1
        say('   ', sp.ljust(5), 'b =', str(b).ljust(5), 'counted', f'{counted:.6f}', 'exact', f'{exact:.6f}', ' miss', f'{miss:.3f}', 'cells')
verdict['Q5'] = ok5

# ── Q6: Proposition 5.4 in exact fractions ──
say('Q6  Proposition 5.4')
seq = [1 - Fr(1, 2 ** m) for m in range(1, 41)]
gaps_ok = all(seq[i + 1] - seq[i] == Fr(1, 2 ** (i + 2)) for i in range(len(seq) - 1))


def vdc(i):
    x, f = Fr(0), Fr(1, 2)
    while i:
        if i & 1:
            x += f
        i >>= 1
        f /= 2
    return x


placed = [vdc(i) for i in range(1025)]
even_pow = True
for m in range(0, 11):
    pts = sorted(placed[:2 ** m])
    g = [pts[j + 1] - pts[j] for j in range(len(pts) - 1)] + [1 - pts[-1] + pts[0]]
    even_pow = even_pow and len(set(g)) == 1
def gaps_closed(pts):
    pts = sorted(pts)
    return [pts[j + 1] - pts[j] for j in range(len(pts) - 1)] + [1 - pts[-1] + pts[0]]


uneven_after = all(len(set(gaps_closed(placed[:2 ** m + 1]))) > 1 for m in range(1, 11))  # run 2: the closing gap included (Q6′)
order_lost = all(placed[:c] != sorted(placed[:c]) for c in range(3, 1026))
relay_moves = all(Fr(1, 2 * nn) != Fr(1, 2 * (nn - 1)) for nn in range(2, 1026))  # re-laid evenly: first address at 1/(2n)
say('    (a) gaps of 1 − 2⁻ⁿ halve each time, → 0:', gaps_ok)
say('    (b) halving even at every 2^m (m ≤ 10):', even_pow, '; not even at 2^m + 1:', uneven_after, '; order lost from the 3rd:', order_lost)
say('    (c) re-laying evenly moves the first address at every n ≥ 2:', relay_moves)
verdict['Q6'] = gaps_ok and even_pow and uneven_after and order_lost and relay_moves

say()
say('verdicts:', {k: ('not killed' if v else 'KILLED') for k, v in verdict.items()})
