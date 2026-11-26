"""DBR run 1 (plans/dbr-plan.md): a Tangent Bridge behind the dial. Run from the repository's root."""
import math
import numpy as np

out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

H = 1.0
L2_ = math.log(2.0)
def f_ratio(x):                      # the paint: features the same size in ratio wherever they are
    u = np.log(x / H) / L2_
    return np.cos(2 * np.pi * u) + 0.5 * np.sin(2 * np.pi * 1.7 * u)
def g_size(x, c=0.0):                # features a fixed number of records; c lets the paint be made from the offset
    return np.cos(x / H)

# ---------------------------------------------------------------- trig counter for the bridge path
TRIG = {'n': 0}
_names = ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'arctan2', 'sinh', 'cosh', 'arcsinh', 'log', 'exp']
_orig = {k: getattr(np, k) for k in _names}
def counting(on):
    for k in _names:
        fn = _orig[k]
        if on:
            def w(*a, _f=fn, **kw):
                TRIG['n'] += 1; return _f(*a, **kw)
            setattr(np, k, w)
        else:
            setattr(np, k, fn)

# ---------------------------------------------------------------- the leaves with no angle
def halve(t): return t / (1.0 + np.sqrt(1.0 + t * t))
def add(a, b): return (a + b) / (1.0 - a * b)
def lattice(N):
    """tan((k + 1/2) pi / N), k = 0..N-1 (TB 11.1), N even."""
    if (N & (N - 1)) == 0:
        b, ang = 1.0, 4                             # b = tan(pi/ang): the corner
    elif N % 3 == 0 and ((N // 3) & (N // 3 - 1)) == 0:
        b, ang = 1.0 / np.sqrt(3.0), 6              # Gauss's seed for 3 * 2^m: tan(pi/6)
    else:
        raise ValueError('N not reachable by halving')
    while ang < 2 * N:
        b = halve(b); ang *= 2                      # tan(pi/(2N)) once ang = 2N
    s = halve(b) if False else None
    # tan(pi/N) is b doubled: tan(2a) = 2b/(1 - b^2)
    step = 2 * b / (1 - b * b)
    out_ = np.empty(N); q = N // 4; cur = b
    for k in range(max(q, 1)):
        if k < N // 2:
            out_[k] = cur; cur = add(cur, step)
    for k in range(q, N // 2):
        out_[k] = 1.0 / out_[N // 2 - 1 - k]
    for k in range(N // 2, N):
        out_[k] = -out_[N - 1 - k]
    return out_

def cheb(K):
    """Chebyshev nodes cos((k+1/2) pi / K) and barycentric weights (-1)^k sin((k+1/2) pi / K), from the lattice."""
    t = lattice(2 * K)[:K]                          # tan((k+1/2) pi / (2K)): half of each node's angle
    c = (1 - t * t) / (1 + t * t)
    s = 2 * t / (1 + t * t)
    w = s * np.where(np.arange(K) % 2 == 0, 1.0, -1.0)
    return c, w

def bary(yk, wk, fk, y):
    d = y[:, None] - yk[None, :]
    hit = d == 0
    d = np.where(hit, 1.0, d)
    q = wk[None, :] / d
    p = (q * fk[None, :]).sum(1) / q.sum(1)
    if hit.any():
        r, cidx = np.nonzero(hit); p[r] = fk[cidx]
    return p, d.shape[1]                            # value, terms per read

def lebesgue(yk, wk, y):
    d = y[:, None] - yk[None, :]
    d = np.where(d == 0, 1e-300, d)
    q = wk[None, :] / d
    return float((np.abs(q).sum(1) / np.abs(q.sum(1))).max())

# ---------------------------------------------------------------- L2: a window in ratios round c
def l2_window(c, rho, K, paint, nq=4000):
    Y = (rho - 1) / (rho + 1)
    z, w = cheb(K)
    yk = Y * z
    xk = c * (1 + yk) / (1 - yk)                    # the leaves, as records
    yq = np.linspace(-Y, Y, nq)
    xq = c * (1 + yq) / (1 - yq)
    counting(False); fk = paint(xk); fq = paint(xq); counting(True)
    p, terms = bary(yk, w, fk, yq)
    # back to y from the record, as a read would: at the leaves
    yb = (xk - c) / (xk + c)
    pb, _ = bary(yk, w, fk, yb)
    return float(np.abs(p - fq).max()), float(np.abs(pb - fk).max()), terms, len(fk)

CENTRES = [1e1, 1e3, 1e6, 1e9, 1e12]

say('D1: exact at its own leaves (K = 16, rho = 4)')
d1 = True
for c in CENTRES:
    TRIG['n'] = 0; counting(True)
    e, el, terms, nl = l2_window(c, 4.0, 16, f_ratio)
    counting(False)
    say(f'  c = {c:.0e}: at the leaves {el:.1e}')
    d1 &= el <= 1e-12
say('D1', 'not killed' if d1 else 'KILLED')

say('D2, D3, D4: ratio content, K = 24, rho = 4')
errs, ok34 = [], True
for c in CENTRES:
    TRIG['n'] = 0; counting(True)
    e, el, terms, nl = l2_window(c, 4.0, 24, f_ratio)
    calls = TRIG['n']; counting(False)
    errs.append(e)
    say(f'  c = {c:.0e}: sup error {e:.2e}  terms per read {terms}  leaf values {nl}  trig calls {calls}')
    ok34 &= terms == 24 and nl == 24 and calls == 0
d2 = max(errs) <= 1e-6 and max(errs) / min(errs) <= 2
say('D2', 'not killed' if d2 else 'KILLED', ' (largest / smallest %.2f)' % (max(errs) / min(errs)))
say('D3, D4', 'not killed' if ok34 else 'KILLED')

say('D5: the whole list on the turn (z = (x - H)/(x + H), N leaves)')
def l1_err(N, a, b, nq=4000):
    z, w = cheb(N)
    xk = H * (1 + z) / (1 - z)
    fk = f_ratio(xk)
    xq = np.exp(np.linspace(math.log(a), math.log(b), nq))
    zq = (xq - H) / (xq + H)
    p, _ = bary(z, w, fk, zq)
    return float(np.abs(p - f_ratio(xq)).max())
near, far = l1_err(256, H / 4, 4 * H), l1_err(256, 1e3 * H, 1e4 * H)
say(f'  N = 256: sup error on [H/4, 4H] {near:.2e}; on [1e3 H, 1e4 H] {far:.3f}')
def need(X):
    reach = sorted({2 ** m for m in range(3, 15)} | {3 * 2 ** m for m in range(2, 13)})   # counts halving reaches
    for N in reach:
        if l1_err(N, H / 4, X) <= 1e-3:
            return N
    return None
n16, n256 = need(16 * H), need(256 * H)
say(f'  N needed for 1e-3 on [H/4, X]: X = 16 H: {n16}; X = 256 H: {n256}')
d5 = near < 1e-3 and far > 0.3 and n16 and n256 and n256 / n16 >= 5
say('D5', 'not killed' if d5 else 'KILLED')

say('D6: size content g = cos(x/H)')
row2 = []
for c in (1e1, 1e3):
    e, *_ = l2_window(c, 4.0, 24, g_size)
    row2.append(e)
say(f'  L2 (ratios), K = 24, rho = 4: c = 10: {row2[0]:.2e}; c = 1e3: {row2[1]:.3f}')
z, w = cheb(24)
row3 = []
for c in CENTRES:
    xk = c + 4 * H * z
    xq = c + 4 * H * np.linspace(-1, 1, 4000)
    p, _ = bary(z, w, g_size(xk), np.linspace(-1, 1, 4000))
    row3.append(float(np.abs(p - g_size(xq)).max()))
say('  L3 (records), K = 24, w = 4H:', '  '.join(f'c = {c:.0e}: {e:.1e}' for c, e in zip(CENTRES, row3)))
last_ok = max([c for c, e in zip(CENTRES, row3) if e <= 1e-6], default=None)
say(f'  L3 holds 1e-6 out to c = {last_ok:.0e}' if last_ok else '  L3 holds 1e-6 nowhere')
d6 = row2[0] <= 1e-6 and row2[1] >= 0.3 and all(e <= 1e-6 for e in row3)
say('D6', 'not killed' if d6 else 'KILLED')

say('D7: the window is a whole bridge')
d7 = True
yq = np.linspace(-1, 1, 20001)
for K in (16, 32, 64):
    zk, wk = cheb(K)
    lam = lebesgue(zk, wk, yq)
    ref = (2 / np.pi) * (math.log(K) + 0.5772156649 + math.log(8 / np.pi))
    say(f'  K = {K}: Lebesgue {lam:.4f}  (2/pi)(ln K + gamma + ln(8/pi)) = {ref:.4f}  {100*(lam/ref-1):+.1f}%')
    d7 &= abs(lam / ref - 1) <= 0.10
e12 = [l2_window(c, 4.0, 12, f_ratio)[0] for c in CENTRES]
e24 = errs
say('  K = 12 errors', ['%.1e' % e for e in e12], ' ratio to K = 24:', ['%.0f' % (a / b) for a, b in zip(e12, e24)])
d7 &= all(a / b >= 100 for a, b in zip(e12, e24))
say('D7', 'not killed' if d7 else 'KILLED')
open('runs/dbr/dbr-run1.txt', 'w').write('\n'.join(out) + '\n')
