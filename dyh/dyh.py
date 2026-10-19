"""DYH run 1: the floor's depth as the half-plane (plans/dyh-plan.md). Exact (mpmath, integers)."""
from collections import deque
import mpmath as mp
mp.mp.dps = 60

def cell(j, k):
    w = mp.mpf(2) ** (-j)
    return (k + mp.mpf(1) / 2) * w, w / 2, w

def cdf(x, m, g):
    return mp.mpf(1) / 2 + mp.atan((x - m) / g) / mp.pi

def dist(z1, z2):
    (m1, g1), (m2, g2) = z1, z2
    return mp.acosh(1 + ((m1 - m2) ** 2 + (g1 - g2) ** 2) / (2 * g1 * g2))

ok = {}
# D1
want = [mp.mpf(1) / 2, mp.mpf(1) / 4, (mp.atan(1) - mp.atan(mp.mpf(1) / 2)) / mp.pi]
worst = 0
for j in (0, 1, 5, 20, 52):
    for k in (0, (2 ** j) // 3, 2 ** j - 1):
        m, g, w = cell(j, k)
        a, b = k * w, (k + 1) * w
        own = cdf(b, m, g) - cdf(a, m, g)
        half = cdf(m, m, g) - cdf(a, m, g)
        outer = cdf(a + w / 4, m, g) - cdf(a, m, g)
        worst = max(worst, abs(own - want[0]), abs(half - want[1]), abs(outer - want[2]))
ok['D1'] = worst < mp.mpf(10) ** -40
print('D1 shares own 1/2, half 1/4, outer quarter %s; worst %s' % (mp.nstr(want[2], 12), mp.nstr(worst, 3)), ok['D1'])

# D2
ref = {'parent-child': mp.acosh(mp.mpf(3) / 2), 'siblings': mp.acosh(3)}
worst = 0
for j in (1, 5, 20, 52):
    for k in (0, 2 ** (j - 1) - 1, 2 ** j - 1):
        m, g, w = cell(j, k)
        pm, pg, _ = cell(j - 1, k // 2)
        worst = max(worst, abs(dist((m, g), (pm, pg)) - ref['parent-child']))
        sib = k ^ 1
        sm, sg, _ = cell(j, sib)
        worst = max(worst, abs(dist((m, g), (sm, sg)) - ref['siblings']))
        for n in (1, 2, 3, 7):
            if k + n < 2 ** j:
                nm, ng, _ = cell(j, k + n)
                worst = max(worst, abs(dist((m, g), (nm, ng)) - mp.acosh(1 + 2 * n * n)))
        # z -> 2z is an isometry carrying cell k of level j onto cell k of level j - 1 (on [0, 2))
        z2 = 2 * mp.mpc(m, g)
        m2, g2, _ = cell(j - 1, k)
        worst = max(worst, abs(z2 - mp.mpc(m2, g2)))
ok['D2'] = worst < mp.mpf(10) ** -40
print('D2 parent-child %s, siblings %s; worst %s' % (mp.nstr(ref['parent-child'], 12), mp.nstr(ref['siblings'], 12), mp.nstr(worst, 3)), ok['D2'])

# D3
worst = 0
for j in (0, 3, 20, 52):
    for k in (0, 2 ** j - 1):
        _, _, w = cell(j, k)
        closed = w * (1 / (w / 2) - 1 / w)
        quad = mp.quad(lambda y: w / y ** 2, [w / 2, w])
        worst = max(worst, abs(closed - 1), abs(quad - 1))
ok['D3'] = worst < mp.mpf(10) ** -30
print('D3 tile area 1; worst %s' % mp.nstr(worst, 3), ok['D3'])

# D4 (a)
worst = 0
for j in range(2, 31):
    a, b = 2 ** (j - 1) - 1, 2 ** j // 2
    ma, ga, _ = cell(j, a); mb, gb, _ = cell(j, b)
    worst = max(worst, abs(dist((ma, ga), (mb, gb)) - mp.acosh(3)))
    # tree distance: up to the common ancestor
    t, x, y = 0, a, b
    while x != y:
        x //= 2; y //= 2; t += 1
    assert 2 * t == 2 * j, (j, t)
ok['D4a'] = worst < mp.mpf(10) ** -40
print('D4a across the middle: tree 2j, d arcosh 3 (worst %s)' % mp.nstr(worst, 3), ok['D4a'])

# D4 (b): BFS on the binary tiling graph, levels 0..10
J = 10
nodes = [(j, k) for j in range(J + 1) for k in range(2 ** j)]
def nbrs(j, k):
    if j > 0: yield (j - 1, k // 2)
    if j < J: yield (j + 1, 2 * k); yield (j + 1, 2 * k + 1)
    if k > 0: yield (j, k - 1)
    if k < 2 ** j - 1: yield (j, k + 1)
def formula(k1, k2):
    return min(2 * s + abs((k2 >> s) - (k1 >> s)) for s in range(J + 1))
import math
LN2 = math.log(2)
worst_dev, pairs, fdiff = 0.0, 0, 0
for k1 in range(2 ** J):
    seen = {(J, k1): 0}; q = deque([(J, k1)])
    while q:
        u = q.popleft()
        for v in nbrs(*u):
            if v not in seen:
                seen[v] = seen[u] + 1; q.append(v)
    for k2 in range(k1 + 1, 2 ** J):
        g = seen[(J, k2)]; n = k2 - k1
        d = math.acosh(1 + 2 * n * n)
        worst_dev = max(worst_dev, abs(d - g * LN2)); pairs += 1
        if g != formula(k1, k2): fdiff += 1
ok['D4b'] = worst_dev <= 3
print('D4b %d pairs, max |d - g ln2| = %.4f; up-across-down formula differs from BFS in %d' % (pairs, worst_dev, fdiff), ok['D4b'])

# D4 (c)
rows = []
for t in range(10, 41):
    n = 2 ** t
    g = min(2 * s + (n >> s) for s in range(t + 2))  # up-across-down; equals the BFS at level 10 (D4b)
    d = mp.acosh(1 + 2 * mp.mpf(n) ** 2)
    rows.append((t, g, d / g))
ok['D4c'] = abs(rows[-1][2] - mp.log(2)) < 0.05
print('D4c d/g at t=10: %s (g %d), t=40: %s (g %d), ln 2 %s' % (mp.nstr(rows[0][2], 6), rows[0][1], mp.nstr(rows[-1][2], 6), rows[-1][1], mp.nstr(mp.log(2), 6)), ok['D4c'])

# D5: Poisson fade against the cell average, w = 1
import numpy as np
n = np.arange(0, 20001) * 1e-3
sinc = np.abs(np.sinc(n))  # numpy sinc is sin(pi x)/(pi x)
best = (9, None)
for i in range(1, 2001):
    g = i * 1e-3
    m = np.max(np.abs(np.exp(-2 * np.pi * n * g) - sinc))
    if m < best[0]: best = (m, g)
ok['D5'] = best[0] >= 0.1
hp_sinc = n[np.argmax(sinc < 2 ** -0.5)]
print('D5 least max difference %.4f at gamma %.3f (w = 1); half power: sinc at n = %.3f, Poisson at n*gamma = %.4f, so the best-matching gamma by half power is %.4f'
      % (best[0], best[1], hp_sinc, math.log(2) / (4 * math.pi), math.log(2) / (4 * math.pi) / hp_sinc), ok['D5'])
print('D6', all(ok.values()))
