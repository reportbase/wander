# FCL run 9: the corner two masses own, from ratios of pulls alone.
# Predictions in plans/fcl-plan.md, committed before this ran.  python3 runs/fcl/fcl9.py   (doubles; needs numpy, scipy)
import numpy as np
from scipy.optimize import least_squares
ok = lambda b: 'ok' if b else 'KILLED'

def pull(x, p1, p2, M1, M2):
    a, b = p1 - x, p2 - x
    return M1*a/np.linalg.norm(a)**3 + M2*b/np.linalg.norm(b)**3
unit = lambda v: v/np.linalg.norm(v)

def scene(seed):
    R = np.random.default_rng(seed)
    while True:
        p1, p2 = R.uniform(-1, 1, 3), R.uniform(-1, 1, 3)
        if np.linalg.norm(p1 - p2) > 0.6: break
    mu = float(np.exp(R.uniform(np.log(0.2), np.log(5))))
    X = []
    while len(X) < 4:
        x = R.uniform(-2, 2, 3)
        if min(np.linalg.norm(x - p1), np.linalg.norm(x - p2)) > 0.4 and all(np.linalg.norm(x - y) > 0.5 for y in X): X.append(x)
    return p1, p2, mu, np.array(X)

print('R1  both masses scaled alike: no direction and no ratio of strengths moves')
R1 = True; worst = 0
for seed in range(5):
    p1, p2, mu, X = scene(seed)
    g0 = [pull(x, p1, p2, mu, 1.0) for x in X]
    for lam in (1e-3, 7.0, 1e6):
        g = [pull(x, p1, p2, mu*lam, lam) for x in X]
        d = max(np.abs(unit(a) - unit(b)).max() for a, b in zip(g0, g))
        r = max(abs(np.linalg.norm(g[i])/np.linalg.norm(g[0])/(np.linalg.norm(g0[i])/np.linalg.norm(g0[0])) - 1) for i in range(4))
        worst = max(worst, d, r)
R1 = worst < 1e-12
print('  worst change over 5 scenes, 3 scalings: %.2e  %s' % (worst, ok(R1)))

print('\nR2  on the line, halving on the sign of the pull alone meets the meeting place; (d1/d2)^2 there is mu')
R2 = True
for M1, M2 in [(1, 1), (3, 1), (10, 1), (2, 5)]:
    D = 1.0; p2 = np.zeros(3); p1 = np.array([D, 0, 0.0])
    lo, hi = 1e-6, D - 1e-6      # s from mass 2 toward mass 1
    for _ in range(200):
        mid = (lo + hi)/2
        if pull(np.array([mid, 0, 0.0]), p1, p2, M1, M2)[0] > 0: hi = mid      # pulled toward mass 1: we are past the meeting place
        else: lo = mid
    s = (lo + hi)/2; exact = D*np.sqrt(M2)/(np.sqrt(M1) + np.sqrt(M2))
    mu_read = ((D - s)/s)**2
    good = abs(s - exact) < 1e-10 and abs(mu_read/(M1/M2) - 1) < 1e-9; R2 &= good
    print('  M1/M2 %-4g: met at s = %.12f (exact %.12f), (d1/d2)^2 = %.10f against mu %.10g  %s' % (M1/M2, s, exact, mu_read, M1/M2, ok(good)))
print('R2', ok(R2))

def solve(X, dirs, ratios, seed, n=40):
    """Every solution found from n random starts: (residual norm, p1, p2, mu)."""
    R = np.random.default_rng(1000 + seed); out = []
    def res(q):
        p1, p2, mu = q[:3], q[3:6], np.exp(q[6])
        g = [pull(x, p1, p2, mu, 1.0) for x in X]
        r = [unit(gi) - di for gi, di in zip(g, dirs)]
        if ratios is not None:
            r.append(np.array([np.log(np.linalg.norm(g[i])/np.linalg.norm(g[0])) - ratios[i - 1] for i in range(1, len(X))]))
        return np.concatenate(r)
    for _ in range(n):
        q0 = np.concatenate([R.uniform(-3, 3, 6), R.uniform(-2, 2, 1)])
        try: s = least_squares(res, q0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=3000)
        except Exception: continue
        out.append((np.linalg.norm(s.fun), s.x[:3], s.x[3:6], float(np.exp(s.x[6]))))
    return out

def off(sol, p1, p2, mu):
    _, a, b, m = sol
    d1 = max(np.linalg.norm(a - p1), np.linalg.norm(b - p2), abs(np.log(m/mu)))
    d2 = max(np.linalg.norm(a - p2), np.linalg.norm(b - p1), abs(np.log(m*mu)))
    return min(d1, d2)

def trial(nplaces, use_ratios, label):
    hit = other = 0; rows = []
    for seed in range(20):
        p1, p2, mu, X = scene(seed); X = X[:nplaces]
        g = [pull(x, p1, p2, mu, 1.0) for x in X]
        dirs = [unit(v) for v in g]
        ratios = [np.log(np.linalg.norm(g[i])/np.linalg.norm(g[0])) for i in range(1, nplaces)] if use_ratios else None
        sols = [s for s in solve(X, dirs, ratios, seed) if s[0] < 1e-10]
        if not sols: rows.append((seed, 'no solution found')); continue
        best = min(sols, key=lambda s: s[0]); o = off(best, p1, p2, mu)
        far = max(off(s, p1, p2, mu) for s in sols)
        hit += o < 1e-6; other += far > 1e-2
        rows.append((seed, 'best %.1e from the truth; %d of 40 starts solved; farthest solved %.2e' % (o, len(sols), far)))
    print('  %s: the truth found in %d of 20; a solved start more than 0.01 from the truth in %d of 20' % (label, hit, other))
    for seed, t in rows[:4]: print('     scene %d: %s' % (seed, t))
    return hit, other

print('\nR3  directions alone')
h4, o4 = trial(4, False, 'four places, directions (8 numbers, 7 unknowns)')
h3, o3 = trial(3, False, 'three places, directions (6 numbers)')
R3 = h4 >= 18 and o3 >= 15
print('R3', ok(R3), '(four places: also %d of 20 with another solution)' % o4)

print('\nR4  directions and ratios of strengths, three places (8 numbers)')
h, o = trial(3, True, 'three places, directions and strength ratios')
R4 = h >= 18
print('R4', ok(R4), '(%d of 20 with another solution)' % o)

print('\nR5  one strength in a unit, with G carried in, gives both masses')
G = 6.6743e-11; R5 = True
for seed in range(3):
    p1, p2, mu, X = scene(seed); M2 = 5.0e24*(seed + 1); M1 = mu*M2
    g_meas = G*np.linalg.norm(pull(X[0], p1, p2, M1, M2))            # one strength, in a unit
    g_unit = np.linalg.norm(pull(X[0], p1, p2, mu, 1.0))             # from the solved scene: places and mu only
    GM2 = g_meas/g_unit; m2 = GM2/G; m1 = mu*m2
    good = abs(m2/M2 - 1) < 1e-8 and abs(m1/M1 - 1) < 1e-8; R5 &= good
    print('  scene %d: G M2 = %.6e (all that is had without G); with G, M2 = %.6e (true %.6e), M1 = %.6e (true %.6e)  %s' % (seed, GM2, m2, M2, m1, M1, ok(good)))
print('R5', ok(R5))
