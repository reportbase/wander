"""SKT run 1: the reader's data structure, measured (plans/skt-plan.md).

Seeded streams of 10^6 positive values; K = 256 cells for every structure. Run from the repository's root:
python3 runs/skt/skt.py
"""
import math
import numpy as np

out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)
V = {}
K = 256
PI = math.pi

# ---------------------------------------------------------------- the structures
def turn_idx(x, H):  # (2/π)·arctan, the horizon kept in the last cell
    return np.minimum(K - 1, np.floor(K * (2 / PI) * np.arctan2(x, H) + 1e-9)).astype(np.int64)
def turn_cell(k, H):
    lo = H * np.tan(k * PI / (2 * K)); hi = np.where(k + 1 >= K, np.inf, H * np.tan(np.minimum(k + 1, K - 1e-9) * PI / (2 * K)))
    rep = H * np.tan((k + 0.5) * PI / (2 * K)); return lo, hi, rep

N_NEAR = 32
M_LVL = (K - N_NEAR) / math.log(2 ** 16)          # cells a neper past H
def lay_F(s):
    return np.where(s <= 1, N_NEAR * s, N_NEAR + M_LVL * np.log(np.maximum(s, 1))) / K
def lay_idx(x, H):
    return np.minimum(K - 1, np.floor(K * lay_F(x / H) + 1e-9)).astype(np.int64)
def lay_cell(k, H):
    k = np.asarray(k, float)
    lo = np.where(k < N_NEAR, k * H / N_NEAR, H * np.exp((k - N_NEAR) / M_LVL))
    hi = np.where(k < N_NEAR, (k + 1) * H / N_NEAR, np.where(k >= K - 1, np.inf, H * np.exp((k + 1 - N_NEAR) / M_LVL)))
    rep = np.where(k < N_NEAR, (k + 0.5) * H / N_NEAR, H * np.exp((k + 0.5 - N_NEAR) / M_LVL))
    return lo, hi, rep

def writer_idx(x, X):
    return np.minimum(K - 1, np.floor(K * x / X)).astype(np.int64)
def writer_cell(k, X):
    k = np.asarray(k, float); return k * X / K, np.where(k >= K - 1, np.inf, (k + 1) * X / K), (k + 0.5) * X / K

class DD:  # DDSketch with K buckets, collapsing the lowest
    def __init__(s, gamma): s.g = gamma; s.lg = math.log(gamma)
    def idx(s, x): return np.ceil(np.log(x) / s.lg - 1e-12).astype(np.int64)
    def build(s, x):
        i = s.idx(x); u, c = np.unique(i, return_counts=True)
        if len(u) > K:
            cut = u[-K]; c = np.concatenate([[c[u <= cut].sum()], c[u > cut]]); u = np.concatenate([[cut], u[u > cut]])
            s.collapsed = True
        else: s.collapsed = False
        s.u, s.c = u, c; return s
    def quantile(s, q, n):
        r = math.ceil(q * n); cs = np.cumsum(s.c); j = int(np.searchsorted(cs, r)); i = s.u[j]
        lo, hi = s.g ** (i - 1), s.g ** i; return 2 * s.g ** i / (s.g + 1), lo, hi

def quant_from(idx_vals, cellf, q, n):
    cnt = np.bincount(idx_vals, minlength=K); cs = np.cumsum(cnt); r = math.ceil(q * n)
    k = int(np.searchsorted(cs, r)); lo, hi, rep = cellf(np.array(k)); return float(rep), float(lo), float(hi)

# ---------------------------------------------------------------- the streams
rng = np.random.default_rng(20261025)
NS = 1_000_000
def streams(seed=20261025):
    r = np.random.default_rng(seed)
    two = np.concatenate([np.exp(r.normal(math.log(1e3), 0.1, NS // 2)), np.exp(r.normal(math.log(1e-3), 0.1, NS // 2))])
    return {
        'loguniform': 10 ** r.uniform(-6, 6, NS),
        'lognormal3': np.exp(r.normal(0, 3, NS)),
        'pareto1': 1 / r.uniform(0, 1, NS),          # x ≥ 1, P(X > x) = 1/x, no mean
        'twoclusters': r.permutation(two),
        'lognormal03': np.exp(r.normal(0, 0.3, NS)),
    }
S = streams()
QS = [0.001, 0.01, 0.25, 0.5, 0.75, 0.99, 0.999]
exactq = lambda x, q: float(np.sort(x)[math.ceil(q * len(x)) - 1])
SORTED = {k: np.sort(v) for k, v in S.items()}
exq = lambda name, q: float(SORTED[name][math.ceil(q * NS) - 1])

# ---------------------------------------------------------------- K1: one form
say('K1  every index rule one form ⌊K·F(x/H)⌋ + c')
# HdrHistogram's integer algorithm (sub-bucket count 32, half 16, unit 1) against the float lay with H = 32 units
SUBH = 4; SUBC = 2 ** (SUBH + 1); HALF = SUBC // 2      # 32 sub-buckets, half 16
def hdr_index(v):
    v = int(v); mask = SUBC - 1
    pow2ceil = (v | mask).bit_length(); b = pow2ceil - (SUBH + 1); sub = v >> b
    return ((b + 1) << SUBH) + (sub - HALF)
def hdr_F_index(v):  # the float lay in base 2, H = SUBC units: linear below, 16 a doubling with linear steps past
    if v < SUBC: return v
    e = math.floor(math.log2(v)); f = v / 2 ** e - 1
    if 2 ** e > v: e -= 1; f = v / 2 ** e - 1
    return SUBC + HALF * (e - (SUBH + 1)) + math.floor(HALF * f + 1e-12)
vals = list(range(0, 4096)) + [int(x) for x in np.unique(np.floor(10 ** rng.uniform(0, 6, 200000)))]
bad_hdr = [v for v in vals if hdr_index(v) != hdr_F_index(v)]
say(f'    HdrHistogram, {len(vals)} integer values 0 … 10⁶: its bucket/sub-bucket index equals the float lay\'s '
    f'⌊·⌋ form at every one: {not bad_hdr}' + (f' (first misses {bad_hdr[:5]})' if bad_hdr else ''))
# DDSketch: ⌈log_γ x⌉ is ⌈K·F(x)⌉ with F = ln x/(K ln γ); the turn and the lay are their own F by construction
xs = S['loguniform'][:200000]; dd = DD(math.exp(12 * math.log(10) / K))
dd_ok = np.array_equal(dd.idx(xs), np.ceil(K * (np.log(xs) / (K * dd.lg)) - 1e-12).astype(np.int64))
say(f'    DDSketch ⌈log_γ x⌉ = ⌈K·ln(x)/(K ln γ)⌉ on 200,000 values: {dd_ok}; the turn and the lay are ⌊K·F⌋ by construction')
V['K1'] = not bad_hdr and dd_ok

# ---------------------------------------------------------------- K2: HdrHistogram within 0.0861 of a doubling
say('K2  HdrHistogram\'s continuous position against the smooth base-2 lay')
v = np.exp(np.linspace(math.log(SUBC), math.log(SUBC * 2 ** 14), 2_000_001))
e = np.floor(np.log2(v)); f = v / 2 ** e - 1
pos_hdr = e + f                                   # linear inside each doubling, in doublings
pos_smooth = np.log2(v)
dev = np.abs(pos_smooth - pos_hdr); mx = dev.max(); at = f[dev.argmax()]
say(f'    the largest gap {mx:.7f} of a doubling at f = {at:.5f} (bound 0.0860713 at f = {1 / math.log(2) - 1:.5f})')
V['K2'] = mx <= 0.0860713320559342 + 1e-12 and abs(mx - 0.0860713320559342) < 1e-6

# ---------------------------------------------------------------- K3: the turn's cell
say('K3  the turn\'s quantile errors inside its cells')
k3 = True; rows = []
for name in S:
    H = exq(name, 0.5)
    ti = turn_idx(S[name], H)
    for q in QS:
        x = exq(name, q); rep, lo, hi = quant_from(ti, lambda k: turn_cell(k, H), q, NS)
        err = abs(rep - x) / x; width = (hi - lo) / x; s = x / H; form = (PI / (2 * K)) * (s + 1 / s)
        k3 &= lo <= x <= hi and err <= width
        rows.append((name, q, err, width, form))
for name in S:
    r = [x for x in rows if x[0] == name]
    say(f'    {name}: errors ' + ', '.join(f'{e:.2g}' for _, _, e, _, _ in r) + '; cell widths ' + ', '.join(f'{w:.2g}' for *_, w, _ in r))
w = np.array([(np.tan((k + 1) * PI / (2 * K)) - np.tan(k * PI / (2 * K))) for k in range(K - 1)])
mids = np.tan((np.arange(K - 1) + 0.5) * PI / (2 * K))
rw = w / mids; sym = max(abs(rw[k] - rw[K - 2 - k]) / rw[k] for k in range(1, K - 2))
say(f'    the cells\' relative widths about their middles mirror about the corner (k ↔ K − 2 − k): largest mismatch {sym:.1e}')
H2 = exq('twoclusters', 0.5); ti = turn_idx(S['twoclusters'], H2)
e25 = quant_from(ti, lambda k: turn_cell(k, H2), 0.25, NS); e75 = quant_from(ti, lambda k: turn_cell(k, H2), 0.75, NS)
x25, x75 = exq('twoclusters', 0.25), exq('twoclusters', 0.75)
r25, r75 = abs(e25[0] - x25) / x25, abs(e75[0] - x75) / x75; cw = (e75[2] - e75[1]) / x75
say(f'    two clusters at H·10⁻³ and H·10³ (H = {H2:.3g}): errors {r25:.3g} and {r75:.3g}, cell {cw:.3g}: within one cell {abs(r25 - r75) <= cw}')
k3 &= abs(r25 - r75) <= cw
V['K3'] = bool(k3)

# ---------------------------------------------------------------- K4: where each wins
say('K4  where each wins (H at the median)')
dd_g = math.exp(12 * math.log(10) / K)
def all_errors(name, H=None, ddg=dd_g, sc=1.0):
    x = S[name] * sc; H = exq(name, 0.5) * sc if H is None else H
    ti, li = turn_idx(x, H), lay_idx(x, H); d = DD(ddg).build(x); res = {}
    for q in QS:
        ex = exq(name, q) * sc
        res[q] = dict(turn=abs(quant_from(ti, lambda k: turn_cell(k, H), q, NS)[0] - ex) / ex,
                      lay=abs(quant_from(li, lambda k: lay_cell(k, H), q, NS)[0] - ex) / ex,
                      dd=abs(d.quantile(q, NS)[0] - ex) / ex)
    return res, d.collapsed
nar, _ = all_errors('lognormal03')
ratios = [nar[q]['dd'] / max(nar[q]['turn'], 1e-300) for q in (0.25, 0.5, 0.75)]
say('    narrow lognormal, q = 0.25, 0.5, 0.75: turn ' + ', '.join(f"{nar[q]['turn']:.2e}" for q in (0.25, 0.5, 0.75))
    + '; DDSketch ' + ', '.join(f"{nar[q]['dd']:.2e}" for q in (0.25, 0.5, 0.75)) + '; ratio ' + ', '.join(f'{r:.1f}' for r in ratios))
lu, coll = all_errors('loguniform')
say('    log-uniform over 12 decades: ' + '; '.join(f"q {q}: turn {lu[q]['turn']:.3g}, DD {lu[q]['dd']:.3g}, lay {lu[q]['lay']:.3g}" for q in QS)
    + f'; DDSketch collapsed: {coll}')
dd_beats = all(lu[q]['dd'] < lu[q]['turn'] for q in QS if q != 0.5)
quart_over1 = lu[0.25]['turn'] > 1 and lu[0.75]['turn'] > 1
# the lay: relative error per level (a dense set of quantiles), past H the same on every level to 10%
H = exq('loguniform', 0.5); li = lay_idx(S['loguniform'], H); cnt = np.bincount(li, minlength=K); cs = np.cumsum(cnt)
qd = np.linspace(0.0005, 0.9995, 4000); lvl_err = {}; inside = []
for q in qd:
    r = math.ceil(q * NS); k = int(np.searchsorted(cs, r)); lo, hi, rep = lay_cell(np.array(k), H)
    ex = float(SORTED['loguniform'][r - 1]); s = ex / H; err = abs(float(rep) - ex) / ex
    if s > 1 and k < K - 1: lvl_err.setdefault(int(math.floor(math.log(s) / math.log(2))), []).append(err)
    elif s <= 1: inside.append((s, err))
lv = {j: max(v) for j, v in lvl_err.items() if len(v) > 20}
lv_spread = (max(lv.values()) - min(lv.values())) / max(lv.values())
say(f'    the lay past H, largest error per doubling: ' + ', '.join(f'{lv[j]:.4f}' for j in sorted(lv)) + f' (spread {lv_spread:.1%})')
ins = sorted(inside); bins = [b for b in ([e for s, e in ins if lo_ <= s < lo_ * 2] for lo_ in (1 / 64, 1 / 16, 1 / 4)) if b]
grow = [max(b) for b in bins]
say(f'    inside H, largest error at s ≈ 1/64, 1/16, 1/4: ' + ', '.join(f'{g:.3f}' for g in grow) + ' (growing as 1/s: ×4 a step)')
k4 = all(r >= 5 for r in ratios) and dd_beats and quart_over1 and lv_spread <= 0.10 and len(grow) == 3 and grow[0] > grow[1] > grow[2]
say(f'    turn ≥ 5× DDSketch on the narrow stream: {all(r >= 5 for r in ratios)}; DDSketch better at every quantile but the median '
    f'on 12 decades: {dd_beats}; the turn over 1 at the quartiles: {quart_over1}; the lay level to 10%: {lv_spread <= 0.10}')
V['K4'] = bool(k4)

# ---------------------------------------------------------------- K5: scaling the world
say('K5  scaling the world')
k5 = True
for name in ('loguniform', 'lognormal3'):
    base, _ = all_errors(name, H=1.0)
    for kk in (1e-3, 1e3):
        fixed, _ = all_errors(name, H=1.0, sc=kk); moved, _ = all_errors(name, H=kk, sc=kk)
        dd_move = max(abs(fixed[q]['dd'] - base[q]['dd']) for q in QS)
        turn_move = max(abs(fixed[q]['turn'] - base[q]['turn']) for q in QS)
        lay_move = max(abs(fixed[q]['lay'] - base[q]['lay']) for q in QS)
        with_H = max(max(abs(moved[q][s] - base[q][s]) for q in QS) for s in ('turn', 'lay', 'dd'))
        say(f'    {name}, k = {kk:g}: H fixed: DDSketch moves {dd_move:.3g} (a bucket {2 * (dd_g - 1) / (dd_g + 1):.3g}), turn {turn_move:.3g}, lay {lay_move:.3g}; '
            f'H moved with the world: at most {with_H:.3g}')
        k5 &= dd_move <= 2 * (dd_g - 1) / (dd_g + 1) and with_H <= 2 * (dd_g - 1) / (dd_g + 1) and (turn_move > 1e-3 or lay_move > 1e-3)
# the writer's array
x = S['loguniform']; Xt = float(x.max())
for name_, X in (('X exact', Xt), ('X ×10', 10 * Xt), ('X ×0.1', 0.1 * Xt)):
    wi = writer_idx(x, X); rep, lo, hi = quant_from(wi, lambda k: writer_cell(k, X), 0.5, NS); ex = exq('loguniform', 0.5)
    over = int((x >= X).sum())
    say(f'    the writer, {name_}: median error {abs(rep - ex) / ex:.3g}, values past the extent {over}')
    if name_ != 'X exact': k5 &= abs(rep - ex) / ex > 0.5 or over > 0
wi1 = writer_idx(x, Xt); wik = writer_idx(x * 1e3, Xt * 1e3)
say(f'    the writer with X moved with the world (×10³): the same cells {np.array_equal(wi1, wik)}')
k5 &= np.array_equal(wi1, wik)
V['K5'] = bool(k5)

# ---------------------------------------------------------------- K6: the best H
say('K6  the best H for the turn')
k6 = True
for name in ('pareto1', 'lognormal3', 'loguniform'):
    for qset in ((0.25, 0.5, 0.75), (0.01, 0.25, 0.5, 0.75, 0.99)):
        xs_ = S[name]; exs = [exq(name, q) for q in qset]
        Hs = np.exp(np.linspace(math.log(exs[0]) - 2, math.log(exs[-1]) + 2, 401))
        worst = []
        for H in Hs:
            ti = turn_idx(xs_, H); cnt = np.bincount(ti, minlength=K); cs = np.cumsum(cnt); m = 0
            for q, ex in zip(qset, exs):
                k = int(np.searchsorted(cs, math.ceil(q * NS))); m = max(m, abs(float(turn_cell(np.array(k), H)[2]) - ex) / ex)
            worst.append(m)
        Hb = float(Hs[int(np.argmin(worst))]); gm = math.sqrt(exs[0] * exs[-1]); ratio = max(Hb / gm, gm / Hb)
        say(f'    {name}, q {qset[0]}–{qset[-1]}: best H {Hb:.4g} against √(q_lo·q_hi) = {gm:.4g} (median {exq(name, 0.5):.4g}): off by ×{ratio:.2f}')
        k6 &= ratio <= 1.5
V['K6'] = bool(k6)

# ---------------------------------------------------------------- K7: order per cell, not sums
say('K7  the Pareto stream: medians within a cell, the midpoint mean')
x = S['pareto1']; H = exq('pareto1', 0.5); ex = exq('pareto1', 0.5); k7 = True
for nm, idxf, cellf in (('turn', lambda v: turn_idx(v, H), lambda k: turn_cell(k, H)),
                        ('lay', lambda v: lay_idx(v, H), lambda k: lay_cell(k, H))):
    rep, lo, hi = quant_from(idxf(x), cellf, 0.5, NS); k7 &= lo <= ex <= hi
    means = []
    for n in (100_000, 200_000, 500_000, 1_000_000):
        cnt = np.bincount(idxf(x[:n]), minlength=K); reps = np.array(cellf(np.arange(K))[2], float)
        means.append(float((cnt * reps).sum() / n))
    settle = abs(means[-1] - means[-2]) / means[-1]
    say(f'    {nm}: median in its cell {lo <= ex <= hi}; midpoint mean at N = 10⁵, 2·10⁵, 5·10⁵, 10⁶: ' + ', '.join(f'{m:.4g}' for m in means)
        + f' (last step {settle:.2%})')
    if settle < 0.01: k7 = False
d = DD(dd_g).build(x); rep, lo, hi = d.quantile(0.5, NS); k7 &= lo <= ex <= hi
dm = []
for n in (100_000, 200_000, 500_000, 1_000_000):
    dn = DD(dd_g).build(x[:n]); dm.append(float((dn.c * (2 * dn.g ** dn.u / (dn.g + 1))).sum() / n))
say(f'    DDSketch: median in its cell {lo <= ex <= hi}; midpoint mean ' + ', '.join(f'{m:.4g}' for m in dm)
    + f' (last step {abs(dm[-1] - dm[-2]) / dm[-1]:.2%}); the exact mean of the sample ' + ', '.join(f'{x[:n].mean():.4g}' for n in (100_000, 200_000, 500_000, 1_000_000)))
if abs(dm[-1] - dm[-2]) / dm[-1] < 0.01: k7 = False
V['K7'] = bool(k7)

say('')
for k_, v_ in V.items(): say(f'{k_}: {"not killed" if v_ else "KILLED"}')
open('runs/skt/skt.txt', 'w').write('\n'.join(out) + '\n')
