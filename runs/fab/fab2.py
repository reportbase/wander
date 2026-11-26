"""FAB run 2 (plans/fab-plan.md): F1' and F2'. Run from the repository's root."""
import math
import numpy as np
from scipy.optimize import minimize

out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)
rng = np.random.default_rng(20261127)
TWO_PI = 2 * np.pi
gx, gw = np.polynomial.legendre.leggauss(64)


def toy_product(roots):
    r = np.sort(np.mod(roots, TWO_PI))
    a = r; b = np.concatenate([r[1:], [r[0] + TWO_PI]])          # pieces between consecutive roots
    mid, half = (a + b) / 2, (b - a) / 2
    x = mid[:, None] + half[:, None] * gx[None, :]                 # pieces x nodes
    P = np.prod(np.sin((x[..., None] - r[None, None, :]) / 2), axis=-1)
    intP = float((np.abs(P) * gw[None, :]).sum(1) @ half)
    s = np.sin((r[:, None] - r[None, :]) / 2); np.fill_diagonal(s, 1.0)
    dP = 0.5 * np.prod(s, axis=1)
    return intP * float(np.sum(1.0 / np.abs(dP)))


say("F1': the toy floor, integral piece by piece")
f1 = True
for n in (2, 4, 8, 16):
    v = toy_product(np.arange(2 * n) * np.pi / n + 0.3)
    say(f'  n={n}: equally spaced {v:.15f}')
    f1 &= abs(v - 8) <= 1e-12
for n in (4, 8):
    obj = lambda p: toy_product(np.concatenate([[0.0], p]))
    ends = []
    for s in range(20):
        p0 = np.sort(rng.uniform(0, TWO_PI, 2 * n - 1))
        res = minimize(obj, p0, method='Nelder-Mead', options={'maxiter': 60000, 'xatol': 1e-12, 'fatol': 1e-14})
        ends.append(obj(res.x))
    say(f'  n={n}: 20 minimizations end at least {min(ends):.12f}, most {max(ends):.6f}')
    f1 &= min(ends) >= 8 - 1e-9
say("F1'", 'not killed' if f1 else 'KILLED')

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

say("F2': the sinusoid's factors with no angle")
f2 = True
for n in (2, 4, 8, 16):
    TRIG['n'] = 0; counting(True)
    intP = 2 * n * (2.0 * (0.0 - (-1.0 / np.sqrt(1.0 + 0.0))) / n)
    step = 1.0                                              # tan(pi/4)
    for _ in range(int(round(math.log2(n))) - 1):
        step = step / (1.0 + np.sqrt(1.0 + step * step))    # tan(pi/(2n))
    sumrecip, t = 0.0, 0.0                                  # t = tan(x_k / 2), x_k = k pi / n
    for k in range(2 * n):
        c = -1.0 if not np.isfinite(t) else (1 - t * t) / (1 + t * t)
        for _ in range(int(round(math.log2(n)))):
            c = 2 * c * c - 1                               # cos(n x_k) by doubling
        sumrecip += 1.0 / abs(n * c)
        if not np.isfinite(t):
            t = -1.0 / step                                 # past the horizon: tan(pi/2 + a) = -1/tan a
        else:
            den = 1 - t * step
            t = np.inf if abs(den) < 1e-12 else (t + step) / den
    calls = TRIG['n']; counting(False)
    say(f'  n={n}: integral {intP:.15f}  sum 1/|P\'| {sumrecip:.15f}  product {intP * sumrecip:.15f}  trig calls {calls}')
    f2 &= abs(intP - 4) <= 1e-12 and abs(sumrecip - 2) <= 1e-12 and calls == 0
say("F2'", 'not killed' if f2 else 'KILLED')
open('runs/fab/fab-run2.txt', 'w').write('\n'.join(out) + '\n')
