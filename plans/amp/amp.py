"""AMP (plans/amp-plan.md): does error add, multiply or vanish across the levels?
Fill levels only: g on [0, 1], each level's own x on [0, 1], values as fill levels. Seeded; python3 plans/amp/amp.py"""
import numpy as np

K, N, M, DELTA = 8, 16, 4000, 1e-3
rng = np.random.default_rng(20261009)
home = lambda k: 1 - 2.0 ** -k              # level k's home in g (the geometry)
width = lambda k: 2.0 ** -k                 # level k's support, home to the far wall
xs = (np.arange(M) + 0.5) / M               # sample points in a level's own x
basis = np.cos(np.pi * np.outer(xs, np.arange(N)))   # M x N
coef = [2.0 ** -k * rng.standard_normal(N) / (1 + np.arange(N)) for k in range(K)]  # T_k, amplitude 2^-k

# sample g: each region k is g in [home(k), home(k+1)); the last region is level K-1's whole support
def region_pts(k):
    lo, hi = home(k), (home(k + 1) if k < K - 1 else 1.0)
    return lo + (hi - lo) * xs

def level_val(a, k, g):
    """level k's held series at g (0 off its support)"""
    x = (g - home(k)) / width(k)
    on = (x >= 0) & (x <= 1)
    out = np.zeros_like(g)
    out[on] = np.cos(np.pi * np.outer(x[on], np.arange(N))) @ a
    return out

def target(g):
    return sum(level_val(coef[k], k, g) for k in range(K))

def inject(shape, k, g):
    x = (g - home(k)) / width(k)
    on = (x >= 0) & (x <= 1)
    return np.where(on, DELTA * (1.0 if shape == 'flat' else 1) * (np.ones_like(g) if shape == 'flat' else x), 0.0)

# ---- nesting 1: fixed frames, own band (P1)
def recon_p1(js, shape):
    return lambda g: target(g) + sum(inject(shape, j, g) for j in js)

# ---- nesting 3: the child re-reads the parent's leftover (P3); least squares on each level's own samples
def build_p3(js, shape):
    held = []          # (k, coefficients, extra injected function or None)
    def recon(g, upto):
        r = np.zeros_like(g)
        for k, a, inj in held[:upto]:
            r += level_val(a, k, g)
            if inj: r += inject(shape, k, g)
        return r
    leftovers = {}
    for k in range(K):
        g = home(k) + width(k) * xs
        resid = target(g) - recon(g, k)
        a, *_ = np.linalg.lstsq(basis, resid, rcond=None)
        leftovers[k] = resid - basis @ a       # what level k could not hold, on its own support
        held.append((k, a, k in js))
    return (lambda g: recon(g, K)), leftovers

def region_err(R, k):
    g = region_pts(k)
    return np.max(np.abs(R(g) - target(g)))

out = []
P = lambda *a: (print(*a), out.append(' '.join(str(x) for x in a)))
base1 = [region_err(recon_p1([], 'flat'), k) for k in range(K)]
R3_0, left0 = build_p3([], 'flat')
base3 = [region_err(R3_0, k) for k in range(K)]
P('baseline error, P1 nesting:', f'{max(base1):.1e}', ' P3 nesting:', f'{max(base3):.1e}')

# P1
p1_ok = True
P('\nP1 (fixed frames, own band): A(j -> k)')
for shape in ('flat', 'sloped'):
    for j in range(K - 1):
        R = recon_p1([j], shape)
        A = [(region_err(R, k) - base1[k]) / DELTA for k in range(K)]
        for k in range(K):
            if k < j:
                ok = A[k] < 1e-9
            elif shape == 'flat':
                ok = 0.99 <= A[k] <= 1.01
            else:
                want = 1.0 if k == K - 1 else 1 - 2.0 ** -(k - j + 1)
                ok = abs(A[k] - want) <= 0.01 * want
            p1_ok &= ok
        P(f'  {shape:6s} j={j}:', ' '.join(f'{a:.4f}' for a in A))
R = recon_p1([1, 3, 5], 'flat')
s7 = (region_err(R, 7) - base1[7]) / DELTA
p1_ok &= 2.97 <= s7 <= 3.03
P(f'  flat at j = 1, 3, 5 together, region 7: {s7:.4f} delta')
P('P1', 'NOT KILLED' if p1_ok else 'KILLED')

# P2: frame shifts in each level's own x
P('\nP2 (frames from the parent\'s reading): frame shift of level k in its own x, per delta at level j')
for model in ('a', 'b'):
    ok_all = True
    for j in range(K - 2):
        h = [home(k) for k in range(K)]
        w = [width(k) for k in range(K)]
        for k in range(j, K - 1):
            read_corner = h[k] + w[k] * (0.5 + (DELTA if k == j else 0.0))
            h[k + 1] = read_corner
            w[k + 1] = (1.0 - h[k + 1]) if model == 'a' else width(k + 1)
        shift = [abs(h[k] - home(k)) / width(k) / DELTA for k in range(K)]
        growth = [shift[k + 1] / shift[k] for k in range(j + 1, K - 1)]
        ok = all(1.8 <= x <= 2.2 for x in growth)
        ok_all &= ok
        P(f'  model {model} j={j}: shifts', ' '.join(f'{shift[k]:.3f}' for k in range(j + 1, K)),
          ' growth/level', ' '.join(f'{x:.3f}' for x in growth))
    P(f'P2 model {model}', 'NOT KILLED' if ok_all else 'KILLED')

# P3
p3_ok = True
P('\nP3 (the child re-reads the leftover): A(j -> k), and the sloped leftover beside each child\'s walls')
for shape in ('flat', 'sloped'):
    for j in range(K - 1):
        R, left = build_p3([j], shape)
        A = [(region_err(R, k) - base3[k]) / DELTA for k in range(K)]
        below = [abs(A[k]) for k in range(j + 1, K)]
        if shape == 'flat':
            ok = max(below) < 1e-6
            P(f'  flat   j={j}: A below j max {max(below):.2e};', ' A(j->j)', f'{A[j]:.4f}')
        else:
            fr = []
            for k in range(j + 1, K):
                d = np.abs(left[k] - left0[k])
                fr.append(d[(xs < 0.1) | (xs > 0.9)].sum() / d.sum() if d.sum() > 0 else 1.0)
            ok = max(below) < 0.1 and min(fr) >= 0.8
            P(f'  sloped j={j}: A below j max {max(below):.4f}; beside walls min {min(fr):.3f};', ' A(j->j)', f'{A[j]:.4f}')
        p3_ok &= ok
P('P3', 'NOT KILLED' if p3_ok else 'KILLED')
open('plans/amp/amp-run1.txt', 'w').write('\n'.join(out) + '\n')
