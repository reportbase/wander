"""TBH run 1: the Tangent Bridge on the read's hemisphere (plans/tbh-plan.md).

Run from the repository's root: python3 runs/tbh/tbh.py
The slope path (leaves, kernels, content, interpolant) is run with every trigonometric
entry point of numpy and math replaced by a counter; the angle-chart reference and the
measure checks use trigonometry and are said to.
"""
import math
import numpy as np

# ---------------------------------------------------------------- trig counter
TRIG = {'n': 0}
_NAMES = ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'arctan2',
          'sinh', 'cosh', 'tanh', 'exp', 'log']
_ORIG_NP = {k: getattr(np, k) for k in _NAMES}
_ORIG_M = {k: getattr(math, k) for k in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'atan2']}


def counting(on):
    for k in _NAMES:
        if k in ('exp', 'log'):
            continue          # exp is used by the content g, not by the bridge; see below
        f = _ORIG_NP[k]
        if on:
            def wrap(*a, _f=f, **kw):
                TRIG['n'] += 1
                return _f(*a, **kw)
            setattr(np, k, wrap)
        else:
            setattr(np, k, f)
    for k, f in _ORIG_M.items():
        if on:
            def wrapm(*a, _f=f):
                TRIG['n'] += 1
                return _f(*a)
            setattr(math, k, wrapm)
        else:
            setattr(math, k, f)


# ---------------------------------------------------------------- slope path (no trig)
def halve(t):
    return t / (1.0 + np.sqrt(1.0 + t * t))


def add(a, b):
    return (a + b) / (1.0 - a * b)


def lattice(N):
    """tan((k + 1/2) pi / N), k = 0..N-1, by halving from the corner and tangent addition."""
    assert N >= 4 and (N & (N - 1)) == 0
    m = int(round(math.log2(N // 2)))          # pi/4 / 2^m = pi/(2N)
    b = 1.0
    for _ in range(m):
        b = halve(b)                            # tan(pi/(2N))
    step = 1.0
    for _ in range(m - 1):
        step = halve(step)                      # tan(pi/N)
    s = np.empty(N)
    q = N // 4                                  # leaves below pi/4: k = 0..q-1
    cur = b
    for k in range(q):
        s[k] = cur
        cur = add(cur, step)
    for k in range(q, N // 2):                  # pi/4 .. pi/2: reciprocal of the mirror
        s[k] = 1.0 / s[N // 2 - 1 - k]
    for k in range(N // 2, N):                  # pi/2 .. pi: tan(pi - x) = -tan x
        s[k] = -s[N - 1 - k]
    return s


def compose(s, sk):
    """tan(t - t_k) from s = tan t and sk = tan t_k; inf where the denominator vanishes."""
    num = s - sk
    den = 1.0 + s * sk
    with np.errstate(divide='ignore', invalid='ignore'):
        u = num / den
    u = np.where(den == 0.0, np.inf, u)
    return u


def kernel_u(N, u):
    """K~_N(t) = sin(Nt)/(N tan t) as a function of u = tan t: Im(w^N)/(N u), w = (1+iu)/|1+iu|."""
    u = np.asarray(u, dtype=float)
    out = np.empty_like(u)
    inf = ~np.isfinite(u)
    small = (np.abs(u) < 1e-300) & ~inf
    reg = ~inf & ~small
    uu = u[reg]
    n = np.sqrt(1.0 + uu * uu)
    w = (1.0 + 1j * uu) / n
    p = int(round(math.log2(N)))
    for _ in range(p):
        w = w * w
    out[reg] = w.imag / (N * uu)
    out[inf] = 0.0          # N even: sin(N pi/2) = 0
    out[small] = 1.0
    return out


def alpha_slopes(N):
    """tan of the alpha leaves (k + 1/2) pi / N - pi/2, symmetric in (-pi/2, pi/2): -1/s_k."""
    return -1.0 / lattice(N)


def beta_halfslopes(N):
    """tan(beta_j / 2), beta_j = (j + 1/2) 2 pi / N."""
    return lattice(N)


def leaf_screen(sig, ta):
    """screen slopes of the leaf (beta, alpha): tan(alpha) (cos beta, sin beta), cos and sin rational in sigma."""
    c = (1 - sig * sig) / (1 + sig * sig)
    s = 2 * sig / (1 + sig * sig)
    return ta[None, :] * c[:, None], ta[None, :] * s[:, None]


def content(name, s1, s2):
    h = 1.0 / np.sqrt(1.0 + s1 * s1 + s2 * s2)
    v, v2 = s1 * h, s2 * h
    if name == 'h': return h
    if name == 'v': return v
    if name == 'v2': return v2
    if name == 'hv': return h * v
    if name == 'h2': return h * h
    if name == 'v_2': return v * v
    if name == 'vv2': return v * v2
    if name == 'g':
        d = 0.6 * h + 0.48 * v + 0.64 * v2
        return _ORIG_NP['exp'](2.0 * d * d)
    raise ValueError(name)


def query_slopes(s1, s2, other=False):
    """(tan(beta/2), tan(alpha)) of a front direction; other=True gives the second representative."""
    r = np.sqrt(s1 * s1 + s2 * s2)
    sig = s2 / (s1 + r)
    ta = r
    if other:
        sig = -1.0 / sig
        ta = -r
    return sig, ta


def bridge_slope(name, Nb, Na, s1, s2, other=False, return_K=False):
    sigj = beta_halfslopes(Nb)
    tak = alpha_slopes(Na)
    L1, L2 = leaf_screen(sigj, tak)
    F = content(name, L1, L2)                                  # Nb x Na
    sig, ta = query_slopes(s1, s2, other)
    Kb = kernel_u(Nb, compose(sig[:, None], sigj[None, :]))  # period 2 pi in beta: half-angle
    Ka = kernel_u(Na, compose(ta[:, None], tak[None, :]))    # period pi in alpha
    val = ((Kb @ F) * Ka).sum(1)
    if return_K:
        return val, Kb, Ka
    return val


# ---------------------------------------------------------------- angle chart (trig used)
def ktil(N, t):
    t = np.asarray(t, float)
    out = np.ones_like(t)
    nz = np.abs(np.sin(t)) > 1e-15
    out[nz] = np.sin(N * t[nz]) * np.cos(t[nz]) / (N * np.sin(t[nz]))
    return out


def bridge_angle(name, Nb, Na, s1, s2, period_alpha=np.pi):
    jb = (np.arange(Nb) + 0.5) * 2 * np.pi / Nb
    if period_alpha == np.pi:
        ka = (np.arange(Na) + 0.5) * np.pi / Na - np.pi / 2
    else:
        ka = (np.arange(Na) + 0.5) * 2 * np.pi / Na - np.pi
    B, A = np.meshgrid(jb, ka, indexing='ij')
    h, v, v2 = np.cos(A), np.sin(A) * np.cos(B), np.sin(A) * np.sin(B)
    if period_alpha == np.pi:
        F = content(name, v / h, v2 / h)
    else:
        F = content_dir(name, h, v, v2)
    al = np.arctan(np.sqrt(s1 * s1 + s2 * s2))
    be = np.arctan2(s2, s1)
    Kb = ktil(Nb, (be[:, None] - jb[None, :]) / 2)
    if period_alpha == np.pi:
        Ka = ktil(Na, al[:, None] - ka[None, :])
    else:
        Ka = ktil(Na, (al[:, None] - ka[None, :]) / 2)
    return ((Kb @ F) * Ka).sum(1)


def content_dir(name, h, v, v2):
    """the DHV's extension: the content's own formula on the whole sphere."""
    if name == 'h': return h
    if name == 'v': return v
    if name == 'v2': return v2
    raise ValueError(name)


# ---------------------------------------------------------------- queries
rng = np.random.default_rng(20261126)
X = rng.normal(size=(20000, 3))
X[:, 0] = np.abs(X[:, 0])
X = X[X[:, 0] > 1e-9]
QS1, QS2 = X[:, 1] / X[:, 0], X[:, 2] / X[:, 0]
# the line at beta = 0 out to the horizon (screen s2 = 0, s1 = tan alpha)
la = np.linspace(0, np.pi / 2 - 1e-6, 4001)[1:]
LS1, LS2 = np.tan(la), np.zeros_like(la)
S1 = np.concatenate([QS1, LS1])
S2 = np.concatenate([QS2, LS2])
R = np.sqrt(S1 * S1 + S2 * S2)
CORE = R <= math.sqrt(3) + 1e-12


def err(name, val, mask=None):
    e = np.abs(val - content(name, S1, S2))
    return float(e.max() if mask is None else e[mask].max())


def fit(Ns, es):
    return float(np.polyfit(np.log(Ns), np.log(es), 1)[0])


out = []
def say(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    out.append(s)


# ---------------------------------------------------------------- P1
say('P1: exactness, invariance, charts, trig calls')
p1 = True
for N in (8, 16, 32, 64):
    TRIG['n'] = 0
    counting(True)
    a = alpha_slopes(N)
    Ka_nodes = kernel_u(N, compose(a[:, None], a[None, :]))
    sb = beta_halfslopes(N)
    Kb_nodes = kernel_u(N, compose(sb[:, None], sb[None, :]))
    node = max(np.abs(Ka_nodes - np.eye(N)).max(), np.abs(Kb_nodes - np.eye(N)).max())
    v1, Kb, Ka = bridge_slope('g', N, N, S1, S2, return_K=True)
    pou = float(np.abs(Kb.sum(1) * Ka.sum(1) - 1).max())
    v2_ = bridge_slope('g', N, N, S1, S2, other=True)
    calls = TRIG['n']
    counting(False)
    inv = float(np.abs(v1 - v2_).max())
    va = bridge_angle('g', N, N, S1, S2)
    chart = float(np.abs(v1 - va).max())
    ok = node <= 1e-12 and pou <= 1e-12 and inv <= 1e-12 and chart <= 1e-12 and calls == 0
    p1 &= ok
    say(f'  N={N}: node {node:.1e}  PoU {pou:.1e}  two reps {inv:.1e}  slope/angle {chart:.1e}  trig calls {calls}  {"ok" if ok else "KILLED"}')
say('P1', 'not killed' if p1 else 'KILLED')

# ---------------------------------------------------------------- P2
say('P2: quadratic even content held exactly')
p2 = True
for (Nb, Na) in ((8, 4), (8, 8), (16, 16), (32, 32), (64, 64)):
    row = []
    for name in ('hv', 'h2', 'v_2', 'vv2'):
        e = err(name, bridge_slope(name, Nb, Na, S1, S2))
        row.append(f'{name} {e:.1e}')
        p2 &= e <= 1e-12
    say(f'  Nb={Nb} Na={Na}: ' + '  '.join(row))
say('P2', 'not killed' if p2 else 'KILLED')

# ---------------------------------------------------------------- P3
say('P3: smooth even content g')
eg = [err('g', bridge_slope('g', N, N, S1, S2)) for N in (8, 16, 32, 64)]
say('  sup err', ['%.2e' % x for x in eg])
p3 = all((eg[i] / eg[i + 1] >= 10) or eg[i + 1] <= 1e-11 for i in range(3)) and eg[-1] <= 1e-11
say('P3', 'not killed' if p3 else 'KILLED')

# ---------------------------------------------------------------- P4
say('P4: odd content, the horizon glued')
p4 = True
for name in ('v', 'v2'):
    alls, cores = [], []
    for N in (8, 16, 32, 64):
        val = bridge_slope(name, N, N, S1, S2)
        alls.append(err(name, val)); cores.append(err(name, val, CORE))
    say(f'  {name}: sup all', ['%.3f' % x for x in alls], ' core', ['%.2e' % x for x in cores])
    p4 &= min(alls) >= 0.05 and cores[-1] < 1e-2 and all(cores[i] / cores[i + 1] >= 1.6 for i in (1, 2))
say('P4', 'not killed' if p4 else 'KILLED')

# ---------------------------------------------------------------- P5
say('P5: h, kinked at the rim')
Ns = [8, 16, 32, 64]
eh = [err('h', bridge_slope('h', N, N, S1, S2)) for N in Ns]
sh = fit(Ns, eh)
say('  sup err', ['%.2e' % x for x in eh], ' exponent %.3f' % sh)
p5 = -1.2 <= sh <= -0.6 and eh[-1] < eh[0]
say('P5', 'not killed' if p5 else 'KILLED')

# ---------------------------------------------------------------- P6
say('P6: front and back (period 2 pi in alpha), angle chart')
p6 = True
for N in (8, 16, 32):
    row = []
    for name in ('h', 'v', 'v2'):
        e = err(name, bridge_angle(name, N, N, S1, S2, period_alpha=2 * np.pi))
        row.append(f'{name} {e:.1e}')
        p6 &= e <= 1e-12
    say(f'  N={N}: ' + '  '.join(row))
say('P6', 'not killed' if p6 else 'KILLED')

# ---------------------------------------------------------------- P7
say('P7: the meridian grid against the read\'s heat (angle chart)')
p7 = True
for N in (8, 16, 32, 64, 128):
    ka = (np.arange(N) + 0.5) * np.pi / N - np.pi / 2
    in1 = np.mean(np.abs(ka) <= np.pi / 4 + 1e-12)
    in3 = np.mean(np.abs(ka) <= np.pi / 3 + 1e-12)
    ring = 2.0 / N / (1 - np.cos(np.pi / N))     # leaf share over heat share in the ring nearest the look
    say(f'  N={N}: r<=1 {in1:.4f} (heat 0.29289)  r<=sqrt3 {in3:.4f} (heat 0.5)  leaves/heat at the look {ring:.1f}')
    p7 &= abs(in1 - 0.5) < 1e-12 and abs(in3 - 2 / 3) < 1e-12
rings = [2.0 / N / (1 - np.cos(np.pi / N)) for N in (8, 16, 32, 64, 128)]
p7 &= all(rings[i + 1] / rings[i] >= 1.8 for i in range(4))
say('P7', 'not killed' if p7 else 'KILLED')

# ---------------------------------------------------------------- P8
say('P8: the bridge moved onto the read\'s measure')
tt = np.linspace(-np.pi / 2, np.pi / 2, 20001)


def lebesgue_uniform(N):
    tk = (np.arange(N) + 0.5) * np.pi / N - np.pi / 2
    return float(np.abs(ktil(N, tt[:, None] - tk[None, :])).sum(1).max())


def equal_area_alpha(N):
    phk = (np.arange(N) + 0.5) * np.pi / N - np.pi / 2
    return np.sign(phk) * np.arccos(1 - 2 * np.abs(phk) / np.pi), phk


def lebesgue_substituted(N):
    tk = (np.arange(N) + 0.5) * np.pi / N - np.pi / 2
    ak, _ = equal_area_alpha(N)
    A = ktil(N, ak[:, None] - tk[None, :])
    Lag = ktil(N, tt[:, None] - tk[None, :]) @ np.linalg.inv(A)
    return float(np.abs(Lag).sum(1).max())


def phi_of(al):
    return (np.pi / 2) * np.sign(al) * (1 - np.cos(al))


def lebesgue_conjugated(N):
    _, phk = equal_area_alpha(N)
    ph = phi_of(tt)
    return float(np.abs(ktil(N, ph[:, None] - phk[None, :])).sum(1).max())


for N in (8, 16, 32):
    say(f'  N={N}: Lambda uniform {lebesgue_uniform(N):.4f}  substituted {lebesgue_substituted(N):.3e}  conjugated {lebesgue_conjugated(N):.4f}')
p8a = lebesgue_substituted(32) >= 1e3
dconj = max(abs(lebesgue_conjugated(N) - lebesgue_uniform(N)) for N in (8, 16, 32))
say('  conjugated minus uniform, largest: %.1e' % dconj)
p8b1 = dconj <= 1e-10


def bridge_conjugated(name, N):
    jb = (np.arange(N) + 0.5) * 2 * np.pi / N
    ak, phk = equal_area_alpha(N)
    B, A = np.meshgrid(jb, ak, indexing='ij')
    F = content(name, np.tan(A) * np.cos(B), np.tan(A) * np.sin(B))
    al = np.arctan(np.sqrt(S1 * S1 + S2 * S2))
    be = np.arctan2(S2, S1)
    Kb = ktil(N, (be[:, None] - jb[None, :]) / 2)
    Ka = ktil(N, phi_of(al)[:, None] - phk[None, :])
    return ((Kb @ F) * Ka).sum(1)


Ns8 = [8, 16, 32, 64, 128]
ehv = [err('hv', bridge_conjugated('hv', N)) for N in Ns8]
eh2 = [err('h2', bridge_conjugated('h2', N)) for N in Ns8]
shv, sh2 = fit(Ns8, ehv), fit(Ns8, eh2)
say('  conjugated hv sup err', ['%.2e' % x for x in ehv], ' exponent %.3f' % shv)
say('  conjugated h2 sup err', ['%.2e' % x for x in eh2], ' exponent %.3f' % sh2)
p8b2 = ehv[3] >= 1e-3 and -0.8 <= shv <= -0.2 and -1.4 <= sh2 <= -0.6
say('P8 (a)', 'not killed' if p8a else 'KILLED', ' (b) Lambda', 'not killed' if p8b1 else 'KILLED',
    ' (b) content', 'not killed' if p8b2 else 'KILLED')

open('runs/tbh/tbh-run1.txt', 'w').write('\n'.join(out) + '\n')
