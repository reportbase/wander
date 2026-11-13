"""CXB run 1: where the sweep reading of chaos ends. See plans/cxb-plan.md (method and predictions fixed there first).
Run: python3 -I runs/cxb/cxb.py"""
import numpy as np
from mpmath import mp, mpf, sin, pi as mpi
out = []
def say(s): print(s); out.append(s)
rng = np.random.default_rng(928)
LN2, LN3 = np.log(2), np.log(3)

def logi(r):
    return (lambda y: r * y * (1 - y)), (lambda y: np.log(np.abs(r * (1 - 2 * y))))
T3 = (lambda x: np.clip(4 * x ** 3 - 3 * x, -1, 1)), (lambda x: np.log(np.abs(12 * x * x - 3)))

def lyap(fd, lo, hi):
    f, d = fd; x = rng.uniform(lo, hi, 200)
    for _ in range(10_000): x = f(x)
    acc = np.zeros(200)
    for _ in range(100_000):
        acc += d(x); x = f(x)
    per = acc / 100_000
    return per.mean(), per.std(ddof=1) / np.sqrt(200)

def htop_logistic(r):
    ys = np.array([0.5]); N = [1]
    while ys.size < 2e7:
        ys = ys[ys <= r / 4]; s = np.sqrt(1 - 4 * ys / r)
        ys = np.concatenate([(1 - s) / 2, (1 + s) / 2]); N.append(ys.size)
    return fit(N)
def htop_T3():
    xs = np.array([-0.5, 0.5]); N = [2]
    while xs.size < 2e7:
        a = np.arccos(np.clip(xs, -1, 1))
        xs = np.concatenate([np.cos((a + 2 * np.pi * j) / 3) for j in range(3)]); N.append(xs.size)
    return fit(N)
def fit(N):
    k = np.arange(len(N))[-8:]; L = np.log(np.array(N, float))[-8:]
    return np.polyfit(k, L, 1)[0], N

# chart identity at r = 4
mp.dps = 60
def tent(w): return 2 * w if w <= mpf(1) / 2 else 2 - 2 * w
worst = mpf(0)
for w in rng.uniform(0, 1, 1000):
    w = mpf(float(w)); y = sin(mpi * w / 2) ** 2
    worst = max(worst, abs(4 * y * (1 - y) - sin(mpi * tent(w) / 2) ** 2))
say(f"chart identity at r = 4: worst |f4(sin²(πw/2)) − sin²(πT(w)/2)| over 1000 w = {float(worst):.2e}")

res = {}
for name, fd, lo, hi, ht in [('r=4', logi(4.0), 0, 1, lambda: htop_logistic(4.0)), ('T3', T3, -1, 1, htop_T3),
                             ('r=3.7', logi(3.7), 0, 1, lambda: htop_logistic(3.7)),
                             ('r=3.8', logi(3.8), 0, 1, lambda: htop_logistic(3.8)),
                             ('r=3.9', logi(3.9), 0, 1, lambda: htop_logistic(3.9))]:
    lam, se = lyap(fd, lo, hi); h, N = ht()
    res[name] = (lam, se, h)
    say(f"{name}: λ = {lam:.5f} ± {se:.5f}   h_top = {h:.5f} (N_k to k={len(N)-1}, last {N[-1]})   h_top − λ = {h - lam:+.5f}")

x1 = (worst < mpf(10) ** -50 and abs(res['r=4'][0] - LN2) < 3 * res['r=4'][1] and abs(res['r=4'][2] - LN2) < 0.01
      and abs(res['T3'][0] - LN3) < 3 * res['T3'][1] and abs(res['T3'][2] - LN3) < 0.01)
say(f"X1: {'not killed' if x1 else 'KILLED'} (ln 2 = {LN2:.5f}, ln 3 = {LN3:.5f})")
gaps = {r: res[r][2] - res[r][0] for r in ['r=3.7', 'r=3.8', 'r=3.9']}
x2 = all(res[r][0] > 0 and res[r][0] < res[r][2] < LN2 and gaps[r] >= 0.02 for r in gaps)
fault = any(g < -0.01 for g in gaps.values())
say(f"X2: {'not killed' if x2 else 'KILLED'}; gaps {', '.join(f'{r} {g:+.4f}' for r, g in gaps.items())}; code fault (gap < −0.01): {fault}")

# digits per step
def part(r, p, y0):
    mp.prec = p; a = mpf(y0); mp.prec = p + 400; b = mpf(y0); R = mpf(r)
    for n in range(1, 6 * p):
        mp.prec = p; a = R * a * (1 - a)
        mp.prec = p + 400; b = R * b * (1 - b)
        if abs(a - b) > mpf('0.1'): return n
    return None
bad = 0
for r in ['r=4', 'r=3.7', 'r=3.8', 'r=3.9']:
    rv = float(r[2:]); lam = res[r][0]
    for p in (53, 100, 200):
        steps = [part(rv, p, float(rng.uniform(0.05, 0.95))) for _ in range(50)]
        steps = [s for s in steps if s]
        m = np.mean(steps); pred = p * LN2 / lam; off = m / pred - 1
        if abs(off) > 0.2: bad += 1
        say(f"  {r} p={p}: mean parting step {m:.1f} (sd {np.std(steps):.1f}, n {len(steps)}), predicted p·ln2/λ = {pred:.1f}, off {off:+.1%}")
say(f"X3: {'KILLED' if bad > 2 else 'not killed'}; points off by more than 20%: {bad} of 12")
open('runs/cxb/run1.txt', 'w').write('\n'.join(out) + '\n')
