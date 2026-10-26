"""GRS run 2: Gr(k, 2k) for k = 3, 4, the π/4 proof checked, and Gr(3, 7) (plans/grs-plan.md, run 2's predictions).

Exact parts in sympy; the Monte Carlo (seeded, N = 10^6) is a referee, its tolerance 4 standard errors.
Run from the repository's root: python3 runs/grs/grs2.py
"""
import itertools
import math
import random
import time

import numpy as np
import sympy as sp
from scipy import stats

rng_r = random.Random(20261027)
rng = np.random.default_rng(20261027)
N = 10**6
verdict = {}
T0 = time.time()


def say(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- Q0: the π/4, symbolically
x, y = sp.symbols("x y", real=True)
half = sp.pi / 2
# |cos x − cos y| over [0, π/2]²: twice the region x < y, where cos x > cos y
I_abs = sp.simplify(2 * sp.integrate(sp.integrate(sp.cos(x) - sp.cos(y), (x, 0, y)), (y, 0, half)))
E_abs = sp.simplify(I_abs / half**2)
straddle_formula = sp.simplify((sp.Rational(1, 2) * 4 / sp.pi) / (sp.Rational(1, 2) * 4 / sp.pi + sp.Rational(1, 2) * E_abs))
say(f"Q0  ∫∫|cos x − cos y| over [0, π/2]² = {I_abs};  E|a1 − a2| = {E_abs};  P(straddle) = {straddle_formula}")


# ---------------------------------------------------------------- exact counts of angles inside the corner
def counts(k):
    """P(j of k angles inside the corner), j = 0..k, from the ordered φ's (φ = 2θ uniform), weight ∏(cos φi − cos φj)."""
    ph = sp.symbols(f"p0:{k}", real=True)
    w = sp.expand(sp.prod([sp.cos(ph[i]) - sp.cos(ph[j]) for i in range(k) for j in range(i + 1, k)]))
    out = []
    for jin in range(k + 1):
        # φ0 < … < φ(jin−1) in [0, π/2], φ(jin) < … < φ(k−1) in [π/2, π]; integrate innermost (largest index) first
        f = w
        for i in reversed(range(k)):
            lo_bound = 0 if i < jin else half
            hi_bound = half if i < jin else sp.pi
            lo = ph[i - 1] if (i > 0 and (i - 1 < jin) == (i < jin)) else lo_bound
            f = sp.integrate(f, (ph[i], lo, hi_bound))
            f = sp.expand(sp.simplify(f))
        out.append(sp.nsimplify(sp.simplify(f)))
    Z = sp.simplify(sum(out))
    return [sp.simplify(o / Z) for o in out]


exact = {}
for k in (1, 2, 3, 4):
    t = time.time()
    exact[k] = counts(k)
    say(f"    k = {k}: P(j inside), j = 0..{k}: " + ", ".join(f"{sp.nsimplify(p)} ≈ {float(p):.6f}" for p in exact[k])
        + f"   ({time.time() - t:.1f} s)")

q0 = sp.simplify(I_abs - (4 - sp.pi)) == 0 and sp.simplify(straddle_formula - sp.pi / 4) == 0 \
    and sp.simplify(exact[2][1] - sp.pi / 4) == 0
verdict["Q0"] = q0
q3 = all(sp.simplify(exact[k][j] - exact[k][k - j]) == 0 for k in exact for j in range(k + 1))
verdict["Q3"] = q3
pin = {k: float(exact[k][k]) for k in exact}
q4 = abs(pin[1] - 0.5) < 1e-15 and abs(pin[2] - (1 - math.pi / 4) / 2) < 1e-15 and pin[3] < 0.054 and pin[4] < pin[3] / 2
verdict["Q4"] = q4
say(f"Q3  counts symmetric about k/2: {q3}")
say(f"Q4  P_in: k=1 {pin[1]:.6f}, k=2 {pin[2]:.6f}, k=3 {pin[3]:.6f}, k=4 {pin[4]:.6f}")


# ---------------------------------------------------------------- Q1: invariance, by the linear-map Jacobian
def cayley(n):
    S = sp.zeros(n, n)
    for i, j in itertools.combinations(range(n), 2):
        v = sp.Rational(rng_r.randint(-5, 5), rng_r.randint(1, 4))
        S[i, j], S[j, i] = v, -v
    I = sp.eye(n)
    return (I - S) * (I + S).inv()


def q1(k, n):
    m = n - k
    ok = True
    for _ in range(5):
        R = cayley(n)
        assert R.T * R == sp.eye(n)
        A, B, C, D = R[:k, :k], R[:k, k:], R[k:, :k], R[k:, k:]
        for _ in range(5):
            X = sp.Matrix(m, k, lambda i, j: sp.Rational(rng_r.randint(-7, 7), rng_r.randint(1, 5)))
            top = A + B * X
            if top.det() == 0:
                continue
            Nn = top.inv()
            Xp = (C + D * X) * Nn
            J = (D - Xp * B).det() ** k * Nn.det() ** m
            lhs = (sp.eye(k) + Xp.T * Xp).det() ** (-n) * J**2
            rhs = (sp.eye(k) + X.T * X).det() ** (-n)
            ok &= lhs == rhs
    return ok


q1ok = True
for k, n in [(2, 4), (3, 6), (4, 8), (3, 7)]:
    r = q1(k, n)
    q1ok &= r
    say(f"Q1  (k, n) = ({k}, {n}): {'exact' if r else 'FAILS'}")
verdict["Q1"] = q1ok


# ---------------------------------------------------------------- Monte Carlo
def sample(k, n):
    A = rng.standard_normal((N, k, k))
    B = rng.standard_normal((N, n - k, k))
    Xt = np.linalg.solve(np.transpose(A, (0, 2, 1)), np.transpose(B, (0, 2, 1)))
    return np.transpose(Xt, (0, 2, 1))


q2, q5, q6 = True, True, True
var_ln = {}
var_se = {}
for k, n in [(1, 2), (2, 4), (3, 6), (4, 8), (3, 7)]:
    X = sample(k, n)
    t = np.linalg.svd(X, compute_uv=False)
    inside = (t <= 1).sum(axis=1)
    prod = np.prod(t, axis=1)
    if n == 2 * k:
        for j in range(k + 1):
            p = float(exact[k][j])
            mc = np.mean(inside == j)
            z = (mc - p) / math.sqrt(p * (1 - p) / N)
            q2 &= abs(z) < 4
            say(f"Q2  ({k},{n}) j = {j} inside: exact {p:.6f}, MC {mc:.6f}, z {z:+.2f}")
        mc5 = np.mean(prod <= 1)
        z5 = (mc5 - 0.5) / math.sqrt(0.25 / N)
        q5 &= abs(z5) < 4
        L = np.log(prod)
        var_ln[k] = L.var()
        var_se[k] = math.sqrt((np.mean((L - L.mean()) ** 4) - L.var() ** 2) / N)
        say(f"Q5  ({k},{n}) P(∏t ≤ 1) {mc5:.5f} (z {z5:+.2f}); ln|det X| mean {L.mean():+.4f}, "
            f"variance {var_ln[k]:.4f} ± {var_se[k]:.4f}")
        if k == 3:
            d = np.linalg.det(X)
            p_c = stats.kstest(d, "cauchy").pvalue
            say(f"Q7  (3,6) det X against the Cauchy: KS p {p_c:.2e}")
            verdict["_q7_kscauchy"] = p_c <= 1e-6
    else:
        mc8 = np.mean(prod <= 1)
        z8 = (mc8 - 0.5) / math.sqrt(0.25 / N)
        verdict["Q8"] = z8 < -4
        say(f"Q8  ({k},{n}) P(∏t ≤ 1) {mc8:.5f} (z against ½ {z8:+.1f}); median ∏t {np.median(prod):.4f}")
    if k >= 3:
        for (i, j) in [(0, 0), (0, k - 1), (n - k - 1, 0), (n - k - 1, k - 1)]:
            p = stats.kstest(X[:, i, j], "cauchy").pvalue
            q6 &= p >= 0.001
            say(f"Q6  ({k},{n}) x{i}{j}: KS p {p:.3f}")
verdict["Q2"], verdict["Q5"], verdict["Q6"] = q2, q5, q6
q7 = (abs(var_ln[1] - math.pi**2 / 4) < 4 * var_se[1] and abs(var_ln[2] - math.pi**2 / 3) < 4 * var_se[2]
      and var_ln[3] > var_ln[2] + 4 * var_se[3] and var_ln[4] > var_ln[3] + 4 * var_se[4] and verdict.pop("_q7_kscauchy"))
verdict["Q7"] = q7
say(f"Q7  Var ln|det X|: k=1 {var_ln[1]:.4f} (π²/4 {math.pi**2/4:.4f}), k=2 {var_ln[2]:.4f} (π²/3 {math.pi**2/3:.4f}), "
    f"k=3 {var_ln[3]:.4f}, k=4 {var_ln[4]:.4f}")

say("")
for kk in ["Q0", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8"]:
    say(f"{kk}: {'not killed' if verdict[kk] else 'KILLED'}")
say(f"({time.time() - T0:.0f} s)")
