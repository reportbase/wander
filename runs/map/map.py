"""MAP run 1: what it takes to map, the two readers made into a mapper (plans/map-plan.md).
Run from the repository's root: python3 runs/map/map.py

A room 5 x 4 x 2.5 m; 80 features (50 on walls, floor and ceiling, 30 on four things), 6 far features at 1e6 m; each a
16-number payload. Standpoints A, B (a unit step from A), C (a unit step from B), each turned by a seeded rotation.
Each reads every feature's direction in its own frame. Places are written in A's frame, in |AB|. Occlusion is ignored
(every feature is read from every standpoint): this tests the division of labour, not visibility.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 50
EXACT = mp.mpf('1e-40')
PLACE = mp.mpf('1e-30')
APART = mp.mpf('1e-6')
THINGS = [((1.0, 2.0, 0.0), (1.2, 0.8, 0.75)), ((3.4, 0.9, 0.0), (0.5, 0.5, 0.5)), ((1.4, 2.2, 0.75), (0.24, 0.24, 0.24)),
          ((4.2, 3.0, 0.0), (0.6, 0.5, 1.8))]        # (corner, size): table, cube, ball on the table, cabinet


def mvec(x): return mp.matrix([mp.mpf(float(v)) for v in x])
def norm(v): return mp.sqrt(sum(c * c for c in v))
def unit(v): n = norm(v); return v / n
def dot(a, b): return sum(a[i] * b[i] for i in range(3))
def cross(a, b): return mp.matrix([a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]])


def rotation(rng):
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    w, x, y, z = [mp.mpf(float(c)) for c in q]
    n = mp.sqrt(w * w + x * x + y * y + z * z); w, x, y, z = w / n, x / n, y / n, z / n
    return mp.matrix([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                      [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                      [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])


def room(seed):
    rng = np.random.default_rng(seed)
    pts = []
    for _ in range(50):                                     # walls, floor, ceiling
        face = rng.integers(6); p = rng.uniform([0, 0, 0], [5, 4, 2.5])
        p[face // 2] = [0, 5, 0, 4, 0, 2.5][face]
        pts.append(p)
    for i in range(30):                                     # on the things' surfaces
        c, s = THINGS[i % 4]; p = np.array(c) + rng.uniform(0, 1, 3) * s
        f = rng.integers(3); p[f] = c[f] + s[f] * rng.integers(2)
        pts.append(p)
    P = [mvec(p) for p in pts]
    for _ in range(6):                                      # far, through a window in the x = 5 wall
        d = np.array([1.0, rng.uniform(-0.3, 0.3), rng.uniform(-0.1, 0.3)]); d /= np.linalg.norm(d)
        P.append(mvec([2.5, 2.0, 1.25]) + mvec(d) * mp.mpf(10) ** 6)
    A = mvec([rng.uniform(2.0, 2.6), rng.uniform(1.0, 1.4), rng.uniform(1.4, 1.8)])
    def step(X):
        while True:
            a = rng.uniform(0, 2 * np.pi); e = rng.uniform(-0.3, 0.3)
            d = mvec([np.cos(a) * np.cos(e), np.sin(a) * np.cos(e), np.sin(e)]); d = unit(d)
            Y = X + d
            if 0.6 < Y[0] < 4.4 and 0.6 < Y[1] < 3.4 and 0.4 < Y[2] < 2.1: return Y
    B = step(A); C = step(B)
    R = {k: rotation(rng) for k in 'ABC'}
    pay = rng.normal(size=(len(P), 16))
    return dict(P=P, X={'A': A, 'B': B, 'C': C}, R=R, pay=pay, rng=rng)


def read(W, k, eps=0.0, rng=None):
    """Directions in standpoint k's own frame, perturbed by an angle of sd eps."""
    X, R = W['X'][k], W['R'][k]
    out = []
    for p in W['P']:
        d = unit(R.T * (p - X))
        if eps:
            n = mvec(rng.normal(size=3)); n = n - d * dot(n, d); n = unit(n)
            ang = mp.mpf(float(rng.normal())) * eps
            d = unit(d * mp.cos(ang) + n * mp.sin(ang))
        out.append(d)
    return out


def in_A(W, k):
    """Standpoint k's centre (in |AB|) and its rotation, in A's frame."""
    A, s = W['X']['A'], norm(W['X']['B'] - W['X']['A'])
    return W['R']['A'].T * (W['X'][k] - A) / s, W['R']['A'].T * W['R'][k]


def approach(o1, u1, o2, u2):
    """Closest approach of two rays (parameters clamped at 0): the distance and the midpoint."""
    w = o1 - o2; a, b, c = dot(u1, u1), dot(u1, u2), dot(u2, u2); d, e = dot(u1, w), dot(u2, w)
    den = a * c - b * b
    t = (b * e - c * d) / den if den > 0 else mp.mpf(0)
    s = (a * e - b * d) / den if den > 0 else e / c
    t, s = max(t, mp.mpf(0)), max(s, mp.mpf(0))
    p1, p2 = o1 + u1 * t, o2 + u2 * s
    return norm(p1 - p2), (p1 + p2) / 2, t


def truth_in_A(W, i):
    A, s = W['X']['A'], norm(W['X']['B'] - W['X']['A'])
    return W['R']['A'].T * (W['P'][i] - A) / s


SEEDS = [11, 12, 13, 14, 15]
N = 86

# ---- M1 -----------------------------------------------------------------------------------------------------------
print("M1: addresses alone, turn and step direction known")
worst_true, least_wrong = mp.mpf(0), mp.mpf(10)
amb = {}
for seed in SEEDS:
    W = room(seed); a, b = read(W, 'A'), read(W, 'B'); oB, RB = in_A(W, 'B'); o = mvec([0, 0, 0])
    for i in range(80):                                      # the plan's 80 x 79 wrong pairs: the room's features
        for j in range(80):
            dist = approach(o, a[i], oB, RB * b[j])[0]
            if i == j: worst_true = max(worst_true, dist)
            else: least_wrong = min(least_wrong, dist)
for eps in (1e-3, 1e-2):
    shares = []
    for seed in SEEDS:
        W = room(seed); rng = np.random.default_rng(seed + 1000)
        a, b = read(W, 'A', eps, rng), read(W, 'B', eps, rng); oB, RB = in_A(W, 'B'); o = mvec([0, 0, 0])
        n_amb = 0
        for i in range(80):                                  # the room's features (far ones are rays at any eps)
            within = 0
            for j in range(N):
                dist, _, t = approach(o, a[i], oB, RB * b[j])
                if dist <= 3 * eps * t: within += 1
            n_amb += within > 1
        shares.append(n_amb / 80)
    amb[eps] = float(np.mean(shares))
m1 = worst_true < EXACT and least_wrong >= APART and 0 < amb[1e-3] < amb[1e-2]
print(f"  exact: true pairs meet to {mp.nstr(worst_true, 3)}; nearest wrong pair {mp.nstr(least_wrong, 4)} |AB|")
print(f"  ambiguous share of A rays: eps 1e-3 {amb[1e-3]:.4f}, eps 1e-2 {amb[1e-2]:.4f}")
print("M1", "not killed" if m1 else "KILLED")


# ---- M2, M3 -------------------------------------------------------------------------------------------------------
def match(pa, pb):
    d = ((pa[:, None, :] - pb[None, :, :]) ** 2).sum(-1)
    return d.argmin(1)


def place_all(W, a, b, m, k='B'):
    oB, RB = in_A(W, k); o = mvec([0, 0, 0])
    return [approach(o, a[i], oB, RB * b[m[i]])[1] for i in range(N)]


print("\nM2: payload matching (sd 0.1), then the rays crossed")
m2, worst_place = True, mp.mpf(0)
for seed in SEEDS:
    W = room(seed); rng = np.random.default_rng(seed + 2000)
    pa = W['pay'] + 0.1 * rng.normal(size=W['pay'].shape); pb = W['pay'] + 0.1 * rng.normal(size=W['pay'].shape)
    m = match(pa, pb); right = int((m == np.arange(N)).sum())
    a, b = read(W, 'A'), read(W, 'B')
    q = place_all(W, a, b, m)
    err = max(norm(q[i] - truth_in_A(W, i)) / max(mp.mpf(1), norm(truth_in_A(W, i))) for i in range(80))
    worst_place = max(worst_place, err); m2 &= right == N and err < PLACE
    print(f"  room {seed}: {right}/{N} matched right; worst place {mp.nstr(err, 3)} (relative past |AB|)")
print("M2", "not killed" if m2 else "KILLED")

print("\nM3: scale the world (the step included)")
W = room(SEEDS[0]); a0, b0 = read(W, 'A'), read(W, 'B'); q0 = place_all(W, a0, b0, np.arange(N))
m3 = True
for k in ('1e-3', '7', '1e3'):
    K = mp.mpf(k)
    Wk = dict(W); Wk['P'] = [p * K for p in W['P']]; Wk['X'] = {s: x * K for s, x in W['X'].items()}
    a, b = read(Wk, 'A'), read(Wk, 'B'); q = place_all(Wk, a, b, np.arange(N))
    da = max(norm(a[i] - a0[i]) for i in range(N)); dq = max(norm(q[i] - q0[i]) / max(1, norm(q0[i])) for i in range(N))
    stride = norm(Wk['X']['B'] - Wk['X']['A'])               # one counted stride, carried in
    met = max(norm(q[i] * stride - Wk['R']['A'].T * (Wk['P'][i] - Wk['X']['A'])) / stride / max(1, norm(q0[i]))
              for i in range(N))
    m3 &= da < EXACT and dq < PLACE and met < PLACE
    print(f"  k = {k}: addresses moved {mp.nstr(da, 3)}; places in |AB| moved {mp.nstr(dq, 3)}; metres off {mp.nstr(met, 3)}")
print("M3", "not killed" if m3 else "KILLED")

# ---- M4 -----------------------------------------------------------------------------------------------------------
print("\nM4: a swapped payload in B's view")
W = room(SEEDS[1]); rng = np.random.default_rng(4000)
a, b, c = read(W, 'A'), read(W, 'B'), read(W, 'C'); oB, RB = in_A(W, 'B'); oC, RC = in_A(W, 'C'); o = mvec([0, 0, 0])
m4 = True; wrong_least, right_worst, swap_least, keep_worst = mp.mpf(10), mp.mpf(0), mp.mpf(10), mp.mpf(0)
for _ in range(10):
    i, j = rng.choice(N, 2, replace=False)
    m = np.arange(N); m[i], m[j] = j, i                     # the payload match after the swap
    for f in range(N):
        dist, qAB, _ = approach(o, a[f], oB, RB * b[m[f]])
        _, qAC, _ = approach(o, a[f], oC, RC * c[f])
        gap = norm(qAB - qAC) / max(1, norm(qAC))
        if f in (i, j): wrong_least = min(wrong_least, dist); swap_least = min(swap_least, gap)
        else: right_worst = max(right_worst, dist); keep_worst = max(keep_worst, gap)
m4 = wrong_least >= APART and right_worst < EXACT and swap_least >= APART and keep_worst < PLACE
print(f"  rays of wrong matches pass {mp.nstr(wrong_least, 4)} apart at least; right matches meet to {mp.nstr(right_worst, 3)}")
print(f"  (A, B) against (A, C): swapped features differ by {mp.nstr(swap_least, 4)} at least; the rest agree to "
      f"{mp.nstr(keep_worst, 3)}")
print("M4", "not killed" if m4 else "KILLED")

# ---- M5 -----------------------------------------------------------------------------------------------------------
print("\nM5: a ranging payload in an unread unit, from A alone")
W = room(SEEDS[2]); a = read(W, 'A'); rng = np.random.default_rng(5000)
true = [W['R']['A'].T * (p - W['X']['A']) for p in W['P']][:80]
quads = [rng.choice(80, 4, replace=False) for _ in range(500)]
m5 = True
for u in ('0.73', '1', '1.27'):
    U = mp.mpf(u)
    P = [a[i] * U * norm(true[i]) for i in range(80)]
    rat = max(abs(norm(P[i] - P[j]) / norm(P[k] - P[l]) - norm(true[i] - true[j]) / norm(true[k] - true[l]))
              for i, j, k, l in quads)
    off = max(abs(norm(P[i]) / norm(true[i]) - U) for i in range(80))
    m5 &= rat < PLACE and off < PLACE
    print(f"  u = {u}: distance ratios off {mp.nstr(rat, 3)}; every place off by u to {mp.nstr(off, 3)}")
print("M5", "not killed" if m5 else "KILLED")

# ---- M6 -----------------------------------------------------------------------------------------------------------
print("\nM6: the turn from six far features")
m6 = True
for seed in SEEDS:
    W = room(seed); a, b = read(W, 'A'), read(W, 'B')
    Ad = np.array([[float(x) for x in a[i]] for i in range(80, N)]); Bd = np.array([[float(x) for x in b[i]] for i in range(80, N)])
    U_, S_, Vt = np.linalg.svd(Bd.T @ Ad)                     # Kabsch: R_hat maps B's directions onto A's
    D = np.diag([1, 1, np.sign(np.linalg.det(U_ @ Vt))]); Rh = (U_ @ D @ Vt).T
    _, RB = in_A(W, 'B'); RBf = np.array([[float(RB[r, s]) for s in range(3)] for r in range(3)])
    ang = np.arccos(min(1.0, (np.trace(Rh.T @ RBf) - 1) / 2))
    oB, _ = in_A(W, 'B'); o = mvec([0, 0, 0]); Rm = mp.matrix(Rh.tolist())
    err = max(float(norm(approach(o, a[i], oB, Rm * b[i])[1] - truth_in_A(W, i))) for i in range(80))
    m6 &= ang <= 1e-5 and err <= 1e-4
    print(f"  room {seed}: rotation off {ang:.2e} rad; places off {err:.2e} |AB| at most")
print("M6", "not killed" if m6 else "KILLED")
print("\nM7", "not killed" if (m1 and m2 and m4 and m6) else "KILLED")
