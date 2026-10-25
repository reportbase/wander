"""ONL run 1: online decisions read as the reader's geometry (plans/onl-plan.md).

Exact arithmetic (fractions) throughout but for the galloping search's logarithms and the randomized ski rental's
quadrature (mpmath, 40 digits). Seeded. Run from the repository's root: python3 runs/onl/onl.py
"""
from fractions import Fraction as F
import math, random
import mpmath as mp

mp.mp.dps = 40
out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)
verdict = {}

# ---------------------------------------------------------------- O1: ski rental at the corner
say('O1  ski rental')
def ski_worst(s, grid=4000, top=20):
    """buy after paying s (in units of the price) in rent; the adversary stops at T; worst of online/offline,
    scanned over T on a grid of 1/200 that contains s, and at s itself"""
    worst = F(0)
    Ts = {F(k, 200) for k in range(1, top * 200)} | {s}
    for T in Ts:
        on = T if T < s else s + 1
        off = min(T, F(1))
        worst = max(worst, on / off)
    return worst
ss = [F(1, 5), F(1, 4), F(1, 2), F(2, 3), F(1), F(3, 2), F(2), F(4), F(5)]
ok1 = True
for s in ss:
    w = ski_worst(s); form = 1 + max(s, 1 / s)
    sym = ski_worst(1 / s)
    say(f'    s = {s}: worst {w}  1 + max(s, 1/s) = {form}  at 1/s {sym}')
    ok1 &= (w == form == sym)
ok1 &= min(ss, key=ski_worst) == 1
# whole days: price B, rent 1 a day, buy on day k
def ski_days(B, k, top):
    worst = F(0)
    for T in range(1, top):
        on = T if T < k else (k - 1) + B
        worst = max(worst, F(on, min(T, B)))
    return worst
bad = []
for B in range(1, 51):
    r = {k: ski_days(B, k, 4 * B + 5) for k in range(1, 3 * B + 2)}
    best = min(r.values())
    if r[B] != 2 - F(1, B) or best < r[B]: bad.append(B)
say(f'    whole days: day B gives 2 − 1/B and nothing better, for B = 1 … 50: {"yes" if not bad else "no at " + str(bad)}')
ok1 &= not bad
verdict['O1'] = ok1

# ---------------------------------------------------------------- O2, O3: the cow path, walked
say('O2  the cow path, walked')
def walk(b, d0, x, side, legs=400):
    """legs alternate sides 0, 1, 0, …, leg i out to d0·b^i and back unless the target is met"""
    cost = F(0)
    for i in range(legs):
        reach = d0 * b ** i
        if i % 2 == side and reach >= x:
            return cost + x
        cost += 2 * reach
    raise RuntimeError('not found')
def cow_sup(b, d0=F(1), K=36):
    eps = F(1, 10 ** 15)
    best = F(0)
    for k in range(K):
        t = d0 * b ** k
        x = t * (1 + eps)                  # just past a turn point, on its own side
        best = max(best, walk(b, d0, x, k % 2) / x)
    return best
ok2 = True
for b in [F(3, 2), F(2), F(3), F(4)]:
    r = 1 / (b - 1)
    form = 1 + 2 * b * b / (b - 1); form_r = 5 + 2 * (r + 1 / r)
    sup = cow_sup(b, K=60 if b == F(3, 2) else 40)
    say(f'    b = {b}: walked sup {float(sup):.9f}  1 + 2b²/(b − 1) = {form} = 5 + 2(r + 1/r) = {form_r} (r = {r}); '
        f'below it: {sup < form}; gap {float(form - sup):.1e}')
    ok2 &= form == form_r and sup < form and form - sup < F(1, 10 ** 5)
ok2 &= min([F(3, 2), F(2), F(3), F(4)], key=lambda b: 1 + 2 * b * b / (b - 1)) == 2
verdict['O2'] = ok2

say('O3  near and far on the cow path')
ok3 = True
for d0 in [F(1), F(2)]:
    for b in [F(2), F(3)]:
        behind = [walk(b, d0, x, 1) - x for x in [d0 / 2, d0 / 10, d0 / 1000, d0 / 10 ** 9]]
        ahead = [walk(b, d0, x, 0) - x for x in [d0 / 2, d0 / 10, d0 / 1000]]
        ratio_small = walk(b, d0, d0 / 10 ** 9, 1) / (d0 / 10 ** 9)
        c = 1 + 2 * b * b / (b - 1)
        far = max((walk(b, d0, x, s) - x) / x for x in [d0 * F(k, 7) for k in range(7, 400)] for s in (0, 1))
        say(f'    d0 = {d0}, b = {b}: excess behind the start {sorted(set(behind))}, ahead {sorted(set(ahead))}; '
            f'ratio at x = d0·1e-9 {float(ratio_small):.3e}; far excess/x at most {float(far):.4f} < c − 1 = {c - 1}')
        ok3 &= set(behind) == {2 * d0} and set(ahead) == {0} and ratio_small > 10 ** 9 and far < c - 1
sup1, sup2 = cow_sup(F(2), F(1)), cow_sup(F(2), F(2))
say(f'    doubling d0 leaves the far constant: {sup1 == sup2}')
ok3 &= sup1 == sup2
verdict['O3'] = ok3

# ---------------------------------------------------------------- the dynamic array
class Arr:
    def __init__(s, g, C0, shrink_at=None):
        s.g, s.C0, s.C, s.N, s.copies, s.ops = g, F(C0), F(C0), 0, 0, 0
        s.shrink_at = shrink_at if shrink_at is not None else 1 / (g * g)
        s.landed = []; s.reallocs = 0
    def push(s):
        s.ops += 1
        if s.N == s.C or s.N + 1 > s.C:
            s.copies += s.N; s.C *= s.g; s.reallocs += 1; s.landed.append(('grow', F(s.N) / s.C))
        s.N += 1
    def pop(s):
        if s.N == 0: return
        s.ops += 1; s.N -= 1
        if s.shrink_at and s.C / s.g >= s.C0 and F(s.N) / s.C <= s.shrink_at:
            s.copies += s.N; s.C /= s.g; s.reallocs += 1; s.landed.append(('shrink', F(s.N) / s.C))

say('O4  the dynamic array\'s band')
ok4 = True
for g in [F(3, 2), F(2), F(3), F(4)]:
    lo = 1 / (g * g)
    grow_lands = F(1) / g                    # full at C, then capacity gC
    shrink_lands = lo * g                    # at load 1/g² of C, then capacity C/g
    mid = F(math.isqrt((1 * lo).numerator), math.isqrt((1 * lo).denominator))
    say(f'    g = {g}: grow lands {grow_lands}, shrink at the threshold lands {shrink_lands}, √(1/g² · 1) = {mid}')
    ok4 &= grow_lands == shrink_lands == mid == 1 / g
# exact landings in a real run at g = 2 with capacities powers of 2 (the thresholds hit exactly)
a = Arr(F(2), 1); [a.push() for _ in range(4096)]; [a.pop() for _ in range(4000)]
lands = {l for k, l in a.landed}
say(f'    g = 2, 4096 pushes then 4000 pops: every resize landed at {sorted(lands)}')
ok4 &= lands == {F(1, 2)}
# thrashing when shrinking at 1/g
thr = []
for e in range(4, 17):
    N = 2 ** e
    t = Arr(F(2), 1, shrink_at=F(1, 2)); [t.push() for _ in range(N)]
    c0 = t.copies; t.push(); t.pop(); per_pair = t.copies - c0
    thr.append((N, per_pair))
say(f'    shrinking at 1/g (g = 2): copies per push–pop pair at the boundary {[p for _, p in thr[:3]]} … {thr[-1]}')
ok4 &= all(p >= N for N, p in thr)
# random runs
def run(g, C0, mix, n=100_000, seed=1):
    rnd = random.Random(seed); a = Arr(g, C0); worst = F(0)
    for i in range(n):
        if mix == 'runs':
            push = (i // 5000) % 2 == 0
        else:
            push = rnd.random() < mix
        a.push() if push else a.pop()
        if a.ops: worst = max(worst, F(a.copies, a.ops))
    return worst, a
mixes = [0.5, 0.55, 0.6, 0.45, 'runs']
say('    g = 2, copies per operation at its worst over every prefix:')
for C0 in [1, 16]:
    w = [run(F(2), C0, m)[0] for m in mixes]
    say(f'      C0 = {C0}: {[round(float(x), 4) for x in w]}')
    ok4 &= all(x <= 2 for x in w)
say('    other g, the worst copies per operation over pushes to N then the mixes:')
for g in [F(3, 2), F(3), F(4)]:
    per = []
    for e in [8, 12, 16]:
        N = 2 ** e; a = Arr(g, 1); rnd = random.Random(e); worst = F(0)
        for _ in range(N): a.push(); worst = max(worst, F(a.copies, a.ops))
        for i in range(4 * N):
            a.push() if rnd.random() < 0.5 else a.pop(); worst = max(worst, F(a.copies, a.ops))
        per.append(worst)
    say(f'      g = {g}: N = 2^8, 2^12, 2^16 → {[round(float(x), 4) for x in per]}')
    ok4 &= per[-1] <= F(11, 10) * per[1]
verdict['O4'] = ok4

say('O5  the array\'s near and far')
ok5 = True
for g in [F(3, 2), F(2), F(3)]:
    for C0 in [8, 16]:
        a = Arr(g, C0, shrink_at=0); waste_near = 0; bad = []; maxratio = F(0)
        for N in range(1, 20_000):
            a.push()
            if N <= C0:
                if a.copies or a.C - N > C0: bad.append(('near', N))
            else:
                k = 0
                while F(C0) * g ** k < N: k += 1     # ⌈log_g(N/C0)⌉, exactly
                if a.reallocs != k: bad.append(('reallocs', N, a.reallocs, k))
                maxratio = max(maxratio, a.C / N)
        say(f'    g = {g}, C0 = {C0}: near field no copying and waste ≤ C0: {not [b for b in bad if b[0] == "near"]}; '
            f'reallocations ⌈log_g(N/C0)⌉ exactly: {not [b for b in bad if b[0] == "reallocs"]}; '
            f'worst C/N past C0 {float(maxratio):.4f} < g')
        ok5 &= not bad and maxratio < g
# with shrinking: the load past C0 never below 1/g² (waste factor at most g²)
for g in [F(3, 2), F(2), F(3)]:
    rnd = random.Random(7); a = Arr(g, 8); low = F(1)
    for i in range(100_000):
        a.push() if rnd.random() < 0.5 + 0.1 * math.sin(i / 3000) else a.pop()
        if a.C > a.C0 and a.N: low = min(low, F(a.N) / a.C)
    say(f'    g = {g}, with shrinking: least load past C0 {float(low):.4f} > 1/g² = {float(1 / g ** 2):.4f}')
    ok5 &= low > 1 / g ** 2
# doubling C0 at g = 2 shifts the reallocations by one level
def reallocs_after(N, C0):
    a = Arr(F(2), C0, shrink_at=0)
    for _ in range(N): a.push()
    return a.reallocs
sh = all(reallocs_after(N, 8) == reallocs_after(N, 16) + 1 for N in [17, 100, 1000, 5000])
say(f'    doubling C0 (8 → 16) at g = 2: one reallocation fewer at N = 17, 100, 1000, 5000: {sh}')
ok5 &= sh
verdict['O5'] = ok5

# ---------------------------------------------------------------- O6: which problems reduce
say('O6  which problems reduce to a reciprocal-symmetric f(r)')
ok6 = True
# the predicted reducers
red_ski = all(ski_worst(s) == ski_worst(1 / s) for s in ss)
red_cow = all(5 + 2 * (r + 1 / r) == 5 + 2 * (1 / r + r) for r in [F(1, 2), F(2), F(1, 3), F(3)])
# the dynamic array, time alone: worst copies per element over pushes, as a function of r = 1/(g − 1)
def copies_per_elem(g, n=200_000):
    a = Arr(g, 1, shrink_at=0); worst = F(0)
    for N in range(1, n):
        a.push(); worst = max(worst, F(a.copies, N))
    return worst
cpe = {}
for g in [F(3, 2), F(2), F(3)]:
    cpe[g] = copies_per_elem(g)
    say(f'    array, copying alone: g = {g} (r = {1 / (g - 1)}): worst copies per element {float(cpe[g]):.4f} '
        f'against 1 + r = {float(1 + 1 / (g - 1)):.4f}')
arr_sym = abs(float(cpe[F(3, 2)]) - float(cpe[F(3)])) < 0.05     # r = 2 against r = 1/2
say(f'    ski rental symmetric: {red_ski}; cow path symmetric in r: {red_cow}; '
    f'the array\'s copying alone the same at r = 2 and r = 1/2: {arr_sym}')
ok6 &= red_ski and red_cow and arr_sym
# randomized ski rental: the optimal mixture's density on the buy time s, ∝ e^s on [0, 1]; its ratio e/(e − 1) at every
# T, all its weight inside the corner
def rand_ratio(T):
    T = mp.mpf(T); Z = mp.e - 1
    dens = lambda s: mp.e ** s / Z
    on = mp.quad(lambda s: dens(s) * (s + 1), [0, min(T, 1)]) + (T * mp.quad(dens, [T, 1]) if T < 1 else 0)
    return on / min(T, 1)
rr = [rand_ratio(T) for T in ['0.1', '0.5', '0.9', '1', '2', '10']]
target = mp.e / (mp.e - 1)
say(f'    randomized ski rental: ratio at T = 0.1 … 10 within {float(max(abs(x - target) for x in rr)):.1e} of '
    f'e/(e − 1) = {float(target):.6f}, every buy time inside the corner (s ≤ 1): not at the corner, does not reduce')
ok6 &= max(abs(x - target) for x in rr) < mp.mpf(10) ** -30
# galloping search: probe b^j until ≥ i, then binary search the last gap; worst comparisons / log2 i for large i
def gallop_worst(b, top=40):
    worst = 0.0
    for e in range(20, top):
        for i in [2 ** e + 1, 2 ** e + 2 ** (e - 1), 2 ** (e + 1) - 1]:
            j = 0
            while b ** j < i: j += 1
            gap = b ** j - (b ** (j - 1) if j else 0)
            cost = j + 1 + math.ceil(math.log2(gap))
            worst = max(worst, cost / math.log2(i))
    return worst
gw = {b: gallop_worst(b) for b in [2, 3, 4, 8, 16, 256]}
say(f'    galloping search, worst comparisons over log2 i (i 2^20 … 2^40): {dict((b, round(v, 4)) for b, v in gw.items())}')
gal_no_corner = all(gw[x] >= gw[y] for x, y in zip([2, 3, 4, 8, 16], [3, 4, 8, 16, 256]))
say(f'    galloping falls as b grows, no interior corner: {gal_no_corner}')
ok6 &= gal_no_corner
say('    paging (LRU k) and online bin packing (First Fit 1.7): not computed; no sunk-against-committed ratio enters '
    'their bounds, by their definitions')
verdict['O6'] = ok6

# ---------------------------------------------------------------- O7: the time-times-space reason for 2
say('O7  the time-times-space product')
ok7 = True
prod = {}
for g in [F(3, 2), F(2), F(3), F(4)]:
    a = Arr(g, 1, shrink_at=0); wc = F(0); ws = F(0)
    for N in range(1, 200_000):
        a.push(); wc = max(wc, F(a.copies, N))
        if N > 4: ws = max(ws, a.C / N)
    r = 1 / (g - 1); form = 2 + r + 1 / r
    prod[g] = wc * ws
    say(f'    g = {g}: copies per element × waste factor {float(prod[g]):.4f}, (1 + r)(1 + 1/r) = 2 + r + 1/r '
        f'= {float(form):.4f}')
    ok7 &= abs(prod[g] - form) < F(1, 100)
ok7 &= min(prod, key=prod.get) == 2
verdict['O7'] = ok7

say('')
for k, v in verdict.items():
    say(f'{k}: {"not killed" if v else "KILLED"}')
open('runs/onl/onl.txt', 'w').write('\n'.join(out) + '\n')
