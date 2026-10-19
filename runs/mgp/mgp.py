"""MGP: the marginalization paradox and the reader's size. See plans/mgp-plan.md (P1-P4).

B1 integrates the nuisance (a scale) out of the full likelihood under the prior eta^(-k); B2 uses the law of the
scale-free data alone, computed as the classical integral over the scale group (Wijsman's representation),
b(zeta, u) = integral of lambda^(n-1) f(lambda u | zeta, eta = 1) d lambda. Some prior for B2 reproduces B1 for every
datum exactly when a/b factors as (function of zeta) x (function of the datum). Both by quadrature (mpmath, 50 digits).
Run: python3 runs/mgp/mgp.py   (several minutes)
"""
import random
import mpmath as mp
mp.mp.dps = 50
M = mp.mpf
rng = random.Random(1972)
def verdict(ok): return "not killed" if ok else "KILLED"
KS = [M(0), M('0.5'), M(1), M('1.5'), M(2)]
INF = mp.inf

def judge(ratio, zetas, data):
    """ratio(zeta, datum) = a/b. Returns (spread of a/b over the data at each zeta, relative; worst factorization gap,
    against the first zeta and the first datum as reference: a/b factors exactly when R(t,d)R(t0,d0) = R(t,d0)R(t0,d))."""
    R = [[ratio(t, d) for d in data] for t in zetas]
    spread = max(max(abs(r / row[0] - 1) for r in row) for row in R)
    gap = max(abs(R[i][p] * R[0][0] / (R[i][0] * R[0][p]) - 1) for i in range(len(zetas)) for p in range(len(data)))
    return spread, gap

def run(name, ratio_k, zetas, data):
    out = {}
    for k in KS:
        out[k] = judge(lambda t, d: ratio_k(k, t, d), zetas, data)
    ok = out[M(1)][0] < M('1e-30') and all(out[k][1] > M('1e-6') for k in KS if k != 1)
    msg = "; ".join(f"k = {mp.nstr(k, 2)}: a/b spread {mp.nstr(out[k][0], 3)}, factorization gap {mp.nstr(out[k][1], 3)}" for k in KS)
    return ok, msg

results = {}

# ---------------------------------------------------------------- P1: Stone and Dawid's exponentials
# X ~ Exp(theta phi), Y ~ Exp(phi); datum (x, y) = (1, z), so z = y/x
def p1_ratio(k, th, z):
    x, y = M(1), z
    a = mp.quad(lambda ph: th * ph * mp.exp(-th * ph * x) * ph * mp.exp(-ph * y) * ph ** (-k), [0, 1, INF])
    u = (x, y)
    b = mp.quad(lambda lam: lam * (th * mp.exp(-th * lam * u[0])) * mp.exp(-lam * u[1]), [0, 1, INF])   # n = 2
    return a / b
zs1 = [M(10) ** M(rng.uniform(-2, 2)) for _ in range(50)]
th1 = [M(10) ** M(rng.uniform(-1.5, 1.5)) for _ in range(20)]
results['P1'] = run('P1', p1_ratio, th1, zs1)

# ---------------------------------------------------------------- P2: DSZ's change point (Jaynes's Example 1)
n2, c2 = 6, M(2)
def lik_cp(zeta, eta, xs):
    s = sum(xs[:zeta]) + c2 * sum(xs[zeta:])
    return eta ** n2 * c2 ** (n2 - zeta) * mp.exp(-eta * s)
def p2_ratio(k, zeta, zv):
    xs = [M(1)] + list(zv)                       # y = x1 = 1, x_i = z_i
    a = mp.quad(lambda e: lik_cp(zeta, e, xs) * e ** (-k), [0, 1, INF])
    b = mp.quad(lambda lam: lam ** (n2 - 1) * lik_cp(zeta, M(1), [lam * x for x in xs]), [0, 1, INF])
    return a / b
zs2 = [tuple(M(rng.uniform(0.1, 3)) for _ in range(n2 - 1)) for _ in range(50)]
results['P2'] = run('P2', p2_ratio, [1, 2, 3, 4, 5], zs2)

# ---------------------------------------------------------------- P3: DSZ's normal, interest mu/sigma
n3 = 4
def lik_norm(zeta, sig, xs):
    return sig ** (-n3) * mp.exp(-sum((x - zeta * sig) ** 2 for x in xs) / (2 * sig ** 2))
def p3_ratio(k, zeta, xs):
    a = mp.quad(lambda s: lik_norm(zeta, s, xs) * s ** (-k), [0, 1, INF])          # prior sigma^(-k) at fixed zeta
    b = mp.quad(lambda lam: lam ** (n3 - 1) * lik_norm(zeta, M(1), [lam * x for x in xs]), [0, 1, INF])
    return a / b
xs3 = [tuple(M(rng.uniform(-1, 3)) for _ in range(n3)) for _ in range(50)]
zt3 = [M(rng.uniform(-1, 2)) for _ in range(20)]
results['P3'] = run('P3', p3_ratio, zt3, xs3)

# ---------------------------------------------------------------- P4: a general scale nuisance, Gamma shape of interest
n4 = 4
def lik_gamma(zeta, kap, ls):
    out = M(1)
    for l in ls:
        w = l / kap
        out *= w ** (zeta - 1) * mp.exp(-w) / mp.gamma(zeta) / kap
    return out
def p4_ratio(k, zeta, ls):
    a = mp.quad(lambda kp: lik_gamma(zeta, kp, ls) * kp ** (-k), [0, 1, INF])
    b = mp.quad(lambda lam: lam ** (n4 - 1) * lik_gamma(zeta, M(1), [lam * l for l in ls]), [0, 1, INF])
    return a / b
ls4 = [tuple([M(1)] + [M(rng.uniform(0.2, 4)) for _ in range(n4 - 1)]) for _ in range(50)]
zt4 = [M(rng.uniform(0.5, 4)) for _ in range(20)]
results['P4'] = run('P4', p4_ratio, zt4, ls4)

for k, (ok, msg) in results.items():
    print(f"{k}: {verdict(ok)}. {msg}")
