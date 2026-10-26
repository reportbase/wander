"""GRS run 1: the reader's addresses on the Grassmannian, k = 2 (plans/grs-plan.md).

Exact checks in sympy (rational rotations from the Cayley transform) and mpmath; a seeded Monte Carlo (N = 10^6) as a
referee for the laws, its tolerance 4 standard errors. Run from the repository's root: python3 runs/grs/grs.py
"""
import itertools
import random

import mpmath as mp
import numpy as np
import sympy as sp
from scipy import stats

mp.mp.dps = 40
rng_r = random.Random(20261026)
verdict = {}


def say(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- G1: the chart density is rotation invariant
def cayley(n):
    """A rational rotation (I - S)(I + S)^-1 from a random rational skew-symmetric S."""
    S = sp.zeros(n, n)
    for i, j in itertools.combinations(range(n), 2):
        v = sp.Rational(rng_r.randint(-5, 5), rng_r.randint(1, 4))
        S[i, j], S[j, i] = v, -v
    I = sp.eye(n)
    R = (I - S) * (I + S).inv()
    assert sp.simplify(R.T * R - I) == sp.zeros(n, n)
    return R


def g1(k, n, rots=5, pts=5):
    m = n - k
    xs = sp.symbols(f"x0:{m * k}")
    X = sp.Matrix(m, k, xs)
    ok = True
    for _ in range(rots):
        R = cayley(n)
        top = R[:k, :k] + R[:k, k:] * X
        bot = R[k:, :k] + R[k:, k:] * X
        Xp = bot * top.inv()
        J = sp.Matrix(list(Xp)).jacobian(xs)
        for _ in range(pts):
            pt = {x: sp.Rational(rng_r.randint(-7, 7), rng_r.randint(1, 5)) for x in xs}
            X0 = X.subs(pt)
            top0 = top.subs(pt)
            if top0.det() == 0:
                continue
            Xp0 = Xp.subs(pt)
            J0 = J.subs(pt).det()
            lhs = (sp.eye(k) + Xp0.T * Xp0).det() ** (-n) * J0 ** 2  # f(gX)^2 |J|^2, f = det(...)^(-n/2)
            rhs = (sp.eye(k) + X0.T * X0).det() ** (-n)
            ok &= sp.simplify(lhs - rhs) == 0
    return ok


say("G1  chart density det(I + X^T X)^(-n/2) unchanged by rational rotations")
g1ok = True
for k, n in [(1, 2), (1, 3), (2, 3), (2, 4), (2, 5)]:
    r = g1(k, n)
    g1ok &= r
    say(f"    (k, n) = ({k}, {n}): {'exact' if r else 'FAILS'}")
verdict["G1"] = g1ok

# ---------------------------------------------------------------- G2: k = 2, n = 3 is the wedge
a, b = sp.symbols("a b", real=True)
X = sp.Matrix([[a, b]])
dens = sp.simplify((sp.eye(2) + X.T * X).det())
normal = sp.Matrix([1, 0, a]).cross(sp.Matrix([0, 1, b]))
cosang = normal[2] / sp.sqrt(normal.dot(normal))
sv = sp.sqrt((X * X.T)[0, 0])
g2 = sp.simplify(dens - (1 + a**2 + b**2)) == 0 and sp.simplify(cosang - 1 / sp.sqrt(1 + sv**2)) == 0
say(f"G2  Gr(2,3): det(I + X^T X) = {dens}; the normal's angle from the third axis is the plane's principal angle: {g2}")
verdict["G2"] = g2

# ---------------------------------------------------------------- G3: Gr(2,4) exchange and the principal angles' law
xs = sp.symbols("p q r s")
X = sp.Matrix(2, 2, xs)
Xi = X.inv()
Ji = sp.factor(sp.Matrix(list(Xi)).jacobian(xs).det())
fX = (sp.eye(2) + X.T * X).det()
fXi = sp.factor((sp.eye(2) + Xi.T * Xi).det())
exch = sp.simplify(Ji**2 - X.det() ** (-8)) == 0 and sp.simplify(fXi - fX / X.det() ** 2) == 0
# f(X^-1)|J| = (fX/detX^2)^-2 |detX|^-4 = fX^-2 = f(X)
say(f"G3  X -> X^-1: |J| = |det X|^-4 and det(I + X^-T X^-1) = det(I + X^T X)/det(X)^2, so the law is kept: {exch}")


def gdens(t1, t2, w=lambda t: 1):
    return abs(mp.cos(t1) ** 2 - mp.cos(t2) ** 2) * w(t1) * w(t2)


def integ(f, lo1, hi1, lo2, hi2):
    """Integrate over the box, splitting at the diagonal where |cos^2 - cos^2| has its kink."""
    def inner(t1):
        l2, h2 = lo2(t1), hi2(t1)
        if h2 <= l2:
            return mp.mpf(0)
        pts = [l2] + ([t1] if l2 < t1 < h2 else []) + [h2]
        return mp.quad(lambda t2: f(t1, t2), pts)
    return mp.quad(inner, [lo1, hi1])


P2 = mp.pi / 2
c = lambda x: (lambda t: x)
Z4 = integ(gdens, 0, P2, c(0), c(P2))
E_cc = integ(lambda u, v: gdens(u, v) * mp.cos(u) ** 2 * mp.cos(v) ** 2, 0, P2, c(0), c(P2)) / Z4
E_abs = integ(lambda u, v: gdens(u, v) * abs(mp.cos(u) ** 2 - mp.cos(v) ** 2), 0, P2, c(0), c(P2)) / Z4
sym = integ(lambda u, v: gdens(u, v) - gdens(P2 - u, P2 - v), 0, P2, c(0), c(P2))

N = 10**6
rng = np.random.default_rng(20261026)


def sample(k, n):
    A = rng.standard_normal((N, k, k))
    B = rng.standard_normal((N, n - k, k))
    # X = B A^-1  ->  X^T = A^-T B^T
    Xt = np.linalg.solve(np.transpose(A, (0, 2, 1)), np.transpose(B, (0, 2, 1)))
    return np.transpose(Xt, (0, 2, 1))


X4 = sample(2, 4)
t = np.linalg.svd(X4, compute_uv=False)  # descending
t2_, t1_ = t[:, 0], t[:, 1]
th1, th2 = np.arctan(t1_), np.arctan(t2_)
cc = np.cos(th1) ** 2 * np.cos(th2) ** 2
ab = np.abs(np.cos(th1) ** 2 - np.cos(th2) ** 2)
z_cc = (cc.mean() - float(E_cc)) / (cc.std() / np.sqrt(N))
z_ab = (ab.mean() - float(E_abs)) / (ab.std() / np.sqrt(N))
g3 = exch and abs(sym) < mp.mpf(10) ** -30 and abs(z_cc) < 4 and abs(z_ab) < 4
say(f"    density ∝ |cos²θ1 − cos²θ2|: unchanged by θ -> π/2 − θ (difference {mp.nstr(sym, 3)});")
say(f"    E[cos²θ1 cos²θ2] {mp.nstr(E_cc, 10)} (MC {cc.mean():.6f}, z {z_cc:+.2f}); "
    f"E|cos²θ1 − cos²θ2| {mp.nstr(E_abs, 10)} (MC {ab.mean():.6f}, z {z_ab:+.2f})")
verdict["G3"] = g3

# ---------------------------------------------------------------- G4: the near field's share
Q = mp.pi / 4
p_near = integ(gdens, 0, Q, c(0), c(Q)) / Z4
p_far = integ(gdens, Q, P2, c(Q), c(P2)) / Z4
p_str = 1 - p_near - p_far
mc_near = np.mean(t2_ <= 1)
mc_far = np.mean(t1_ >= 1)
se = np.sqrt(float(p_near) * (1 - float(p_near)) / N)
z_n, z_f = (mc_near - float(p_near)) / se, (mc_far - float(p_far)) / se
g4 = p_near < mp.mpf(1) / 4 and p_str > mp.mpf(1) / 2 and abs(p_near - p_far) < mp.mpf(10) ** -20 and abs(z_n) < 4 and abs(z_f) < 4
say(f"G4  P(both t ≤ 1) {mp.nstr(p_near, 15)}, P(both ≥ 1) {mp.nstr(p_far, 15)}, straddling {mp.nstr(p_str, 15)}")
say(f"    (1/2 − 1/π = {mp.nstr(mp.mpf(1)/2 - 1/mp.pi, 15)}); MC {mc_near:.5f}, {mc_far:.5f} (z {z_n:+.2f}, {z_f:+.2f})")
verdict["G4"] = g4

# ---------------------------------------------------------------- G5: medians
F_min = lambda a_: 1 - integ(gdens, a_, P2, c(a_), c(P2)) / Z4  # P(θmin ≤ a)
F_max = lambda a_: integ(gdens, 0, a_, c(0), c(a_)) / Z4  # P(θmax ≤ a)
a1 = mp.findroot(lambda a_: F_min(a_) - mp.mpf(1) / 2, 0.5)
a2 = mp.findroot(lambda a_: F_max(a_) - mp.mpf(1) / 2, 1.0)
prod_med = mp.tan(a1) * mp.tan(a2)
p_prod = integ(gdens, 0, P2, c(0), lambda u: P2 - u) / Z4  # P(θ1 + θ2 ≤ π/2) = P(t1 t2 ≤ 1)
mc_prod = np.median(t1_ * t2_)
se_med = 1 / (2 * np.sqrt(N) * 0.25)  # density of t1 t2 at 1 is 1/4 (G7's law: ½(1 + 1)^-2)
g5 = abs(prod_med - 1) < mp.mpf(10) ** -20 and abs(p_prod - mp.mpf(1) / 2) < mp.mpf(10) ** -20 and abs(mc_prod - 1) < 4 * se_med
say(f"G5  median t1 {mp.nstr(mp.tan(a1), 12)}, median t2 {mp.nstr(mp.tan(a2), 12)}, product {mp.nstr(prod_med, 25)}")
say(f"    P(t1 t2 ≤ 1) {mp.nstr(p_prod, 25)}; MC median(t1 t2) {mc_prod:.5f}")
verdict["G5"] = g5

# ---------------------------------------------------------------- G6: every entry a standard Cauchy
g6 = True
se_q = np.sqrt(3 / 16 / N) * 2 * np.pi
for i, j in itertools.product(range(2), range(2)):
    e = X4[:, i, j]
    p = stats.kstest(e, "cauchy").pvalue
    q1, q3 = np.quantile(e, [0.25, 0.75])
    okij = p >= 0.001 and abs(q1 + 1) < 4 * se_q and abs(q3 - 1) < 4 * se_q
    g6 &= okij
    say(f"G6  x{i}{j}: KS p {p:.3f}, quartiles {q1:+.4f} {q3:+.4f}")
verdict["G6"] = g6

# ---------------------------------------------------------------- G7: det X, the diamond's law
d = np.linalg.det(X4)
Fd = lambda r: np.where(r <= 0, 0.5 / (1 - r), 1 - 0.5 / (1 + r))
p_dia = stats.kstest(d, Fd).pvalue
p_cau = stats.kstest(d, "cauchy").pvalue
g7 = p_dia >= 0.001 and p_cau <= 1e-6
say(f"G7  det X: KS p against ½(1 + |r|)^-2 {p_dia:.3f}, against the Cauchy {p_cau:.2e}; "
    f"median |det X| {np.median(np.abs(d)):.5f}; P(|det X| ≤ 1/3) {np.mean(np.abs(d) <= 1/3):.4f} (diamond 0.25, Cauchy {2/np.pi*np.arctan(1/3):.4f})")
verdict["G7"] = g7

# ---------------------------------------------------------------- G8: Gr(2,5), no exchange
w5 = lambda tt: mp.sin(tt)
g5d = lambda u, v: gdens(u, v, w5)
Z5 = integ(g5d, 0, P2, c(0), c(P2))
p5 = integ(g5d, 0, P2, c(0), lambda u: P2 - u) / Z5
X5 = sample(2, 5)
t5 = np.linalg.svd(X5, compute_uv=False)
prod5 = t5[:, 0] * t5[:, 1]
mc5 = np.mean(prod5 <= 1)
z5 = (mc5 - float(p5)) / np.sqrt(float(p5) * (1 - float(p5)) / N)
g8 = p5 < mp.mpf(1) / 2 and abs(z5) < 4
say(f"G8  Gr(2,5): P(t1 t2 ≤ 1) {mp.nstr(p5, 12)} (MC {mc5:.5f}, z {z5:+.2f}); median(t1 t2) {np.median(prod5):.4f}")
verdict["G8"] = g8

say("")
for kk, v in verdict.items():
    say(f"{kk}: {'not killed' if v else 'KILLED'}")
