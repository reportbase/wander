"""FAB run 1 (plans/fab-plan.md). Run from the repository's root: python3 runs/fab/fab.py"""
import math
import numpy as np
from scipy.optimize import minimize

out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

rng = np.random.default_rng(20261126)
TWO_PI = 2 * np.pi


# ---------------------------------------------------------------- the toy: P = prod sin((x - x_k)/2)
def toy_product(roots, M):
    x = (np.arange(M) + 0.5) * TWO_PI / M
    d = (x[:, None] - roots[None, :]) / 2
    P = np.prod(np.sin(d), axis=1)
    intP = np.abs(P).sum() * TWO_PI / M
    dd = (roots[:, None] - roots[None, :]) / 2
    s = np.sin(dd)
    np.fill_diagonal(s, 1.0)
    dP = 0.5 * np.prod(s, axis=1)
    return intP * np.sum(1.0 / np.abs(dP))


say('F1: the toy floor')
f1 = True
for n in (2, 4, 8, 16):
    eq = np.arange(2 * n) * np.pi / n + 0.3
    v = toy_product(eq, 400000)
    say(f'  n={n}: equally spaced {v:.12f}')
    f1 &= abs(v - 8) <= 1e-9
for n in (4, 8):
    vals = np.array([toy_product(np.sort(rng.uniform(0, TWO_PI, 2 * n)), 20000) for _ in range(10000)])
    say(f'  n={n}: 10,000 random root sets, least {vals.min():.6f}, median {np.median(vals):.3f}')
    f1 &= vals.min() >= 8 - 1e-6

    def obj(p, n=n):
        r = np.concatenate([[0.0], np.mod(p, TWO_PI)])
        return toy_product(np.sort(r), 20000)
    ends = []
    for s in range(20):
        p0 = np.sort(rng.uniform(0, TWO_PI, 2 * n - 1))
        res = minimize(obj, p0, method='Nelder-Mead', options={'maxiter': 20000, 'xatol': 1e-10, 'fatol': 1e-12})
        r = np.sort(np.concatenate([[0.0], np.mod(res.x, TWO_PI)]))
        ends.append(toy_product(r, 400000))
    say(f'  n={n}: 20 minimizations end at least {min(ends):.9f}, most {max(ends):.6f}')
    f1 &= min(ends) >= 8 - 1e-6
say('F1', 'not killed' if f1 else 'KILLED')


# ---------------------------------------------------------------- F2: the sinusoid's two factors, no trig
TRIG = {'n': 0}
_names = ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'arctan2']
_orig = {k: getattr(np, k) for k in _names}
def counting(on):
    for k in _names:
        f = _orig[k]
        if on:
            def w(*a, _f=f, **kw):
                TRIG['n'] += 1; return _f(*a, **kw)
            setattr(np, k, w)
        else:
            setattr(np, k, f)

say('F2: the sinusoid sin(nx), its factors with no angle')
f2 = True
for n in (2, 4, 8, 16):
    TRIG['n'] = 0
    counting(True)
    # integral of |sin(nx)| over [0, 2 pi): 2n arches, each (1/n) * 2 * [-1/sqrt(1+s^2)]_0^inf
    arch = 2.0 * (0.0 - (-1.0 / np.sqrt(1.0 + 0.0))) / n
    intP = 2 * n * arch
    # roots x_k = k pi / n; P'(x_k) = n cos(n x_k); cos x from the half-angle slope, cos(n x) by doubling
    step = 1.0
    for _ in range(int(round(math.log2(n))) + 1):
        step = step / (1.0 + np.sqrt(1.0 + step * step))     # tan(pi/(2n)) from tan(pi/4)
    sumrecip = 0.0
    t = 0.0
    for k in range(2 * n):
        if np.isfinite(t):
            c = (1 - t * t) / (1 + t * t)
        else:
            c = -1.0
        for _ in range(int(round(math.log2(n)))):
            c = 2 * c * c - 1
        sumrecip += 1.0 / abs(n * c)
        # next half-angle slope by tangent addition, with the horizon given its address
        if not np.isfinite(t):
            t = -1.0 / step
        else:
            den = 1 - t * step
            t = np.inf if abs(den) < 1e-15 else (t + step) / den
    calls = TRIG['n']
    counting(False)
    say(f'  n={n}: integral {intP:.15f}  sum 1/|P\'| {sumrecip:.15f}  product {intP * sumrecip:.15f}  trig calls {calls}')
    f2 &= abs(intP - 4) < 1e-12 and abs(sumrecip - 2) < 1e-12 and calls == 0
say('F2', 'not killed' if f2 else 'KILLED')


# ---------------------------------------------------------------- the circle's Lebesgue function
def lagrange_abs_sum(nodes, x):
    d = (x[:, None] - nodes[None, :]) / 2
    S = np.sin(d)                                  # M x N
    dd = (nodes[:, None] - nodes[None, :]) / 2
    D = np.sin(dd); np.fill_diagonal(D, 1.0)
    den = np.prod(D, axis=1)                       # N
    full = np.prod(S, axis=1)                      # M
    with np.errstate(divide='ignore', invalid='ignore'):
        L = full[:, None] / S / den[None, :]
    # at a node the ratio is 0/0: there l_k = delta
    bad = ~np.isfinite(L)
    if bad.any():
        L[bad] = 1.0
    return np.abs(L).sum(1)


def mean_lebesgue(nodes, M):
    x = (np.arange(M) + 0.5) * TWO_PI / M
    return float(lagrange_abs_sum(nodes, x).mean())


say('F3: on the circle, is equal spacing the least average?')
f3 = True
for N in (9, 17):
    eq = np.arange(N) * TWO_PI / N
    meq = mean_lebesgue(eq, 65536)

    def obj(p, N=N):
        r = np.sort(np.concatenate([[0.0], np.mod(p, TWO_PI)]))
        return mean_lebesgue(r, 4096)
    ends = []
    for s in range(20):
        p0 = np.sort(rng.uniform(0, TWO_PI, N - 1))
        res = minimize(obj, p0, method='Nelder-Mead', options={'maxiter': 40000, 'xatol': 1e-10, 'fatol': 1e-12})
        r = np.sort(np.concatenate([[0.0], np.mod(res.x, TWO_PI)]))
        ends.append(mean_lebesgue(r, 65536))
    say(f'  N={N}: equally spaced mean {meq:.9f}; 20 minimizations end at least {min(ends):.9f}, most {max(ends):.6f}')
    f3 &= min(ends) >= meq - 1e-6
say('F3', 'not killed' if f3 else 'KILLED')


say('F4: the equally spaced mean against ln N')
Ns, ms = [], []
for k in range(6, 13):
    N = 2 ** k + 1
    xk = np.arange(N) * TWO_PI / N
    x = (np.arange(4000) + 0.5) * (TWO_PI / N) / 4000        # one cell; lambda has period 2 pi / N
    d = (x[:, None] - xk[None, :]) / 2
    lam = (np.abs(np.sin(N * x / 2))[:, None] / (N * np.abs(np.sin(d)))).sum(1)
    Ns.append(N); ms.append(lam.mean())
a, b = np.polyfit(np.log(Ns), ms, 1)
say('  means', ['%.5f' % m for m in ms], f' slope {a:.5f} (4/pi^2 = {4/np.pi**2:.5f}), {100*(a/(4/np.pi**2)-1):+.2f}%')
f4 = abs(a / (4 / np.pi ** 2) - 1) <= 0.02
say('F4', 'not killed' if f4 else 'KILLED')


say('F5: the rotation, and one turned read')
f5 = True
for N in (9, 17, 33):
    nodes = np.arange(N) * TWO_PI / N
    M = 20000
    x = (np.arange(M) + 0.5) * TWO_PI / M
    lam_x = lagrange_abs_sum(nodes, x)
    # turn the places by a = -x and read at 0: the same numbers, by construction of the grid
    lam_turn = np.array([lagrange_abs_sum(np.mod(nodes - a, TWO_PI), np.array([0.0]))[0] for a in x[:2000]])
    fub = float(np.abs(lam_turn - lam_x[:2000]).max())
    share = float(np.mean(lam_x < 1.1))
    say(f'  N={N}: turned read against the average\'s integrand {fub:.1e}; share of turns with lambda(0) < 1.1: {share:.3f}')
    f5 &= fub <= 1e-10 and share >= 0.10
say('F5', 'not killed' if f5 else 'KILLED')

open('runs/fab/fab-run1.txt', 'w').write('\n'.join(out) + '\n')
