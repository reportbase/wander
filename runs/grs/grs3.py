"""GRS run 3: the general formula for the number of principal angles inside the corner in Gr(k, 2k)
(plans/grs-plan.md, run 3's predictions). De Bruijn's Pfaffian; symbolic for k ≤ 8, 80 digits for k ≤ 24.

Run from the repository's root: python3 runs/grs/grs3.py
"""
import functools
import math
import time

import mpmath as mp
import numpy as np
import sympy as sp

T0 = time.time()
z = sp.symbols("z")
P2 = sp.pi / 2
verdict = {}


def say(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- entries, exact
ph, ps = sp.symbols("phi psi", real=True)


@functools.lru_cache(None)
def S(r, s, a, b):
    """∫_a^b ∫_a^b sign(ψ − φ) cos rφ cos sψ dφ dψ (a, b in {0, π/2, π}, given as 0, 1, 2 halves of π)."""
    A, B = a * P2, b * P2
    inner = sp.integrate(sp.cos(r * ph), (ph, A, ps)) - sp.integrate(sp.cos(r * ph), (ph, ps, B))
    return sp.simplify(sp.integrate(sp.expand(sp.cos(s * ps) * inner), (ps, A, B)))


@functools.lru_cache(None)
def M(r, a, b):
    return sp.simplify(sp.integrate(sp.cos(r * ph), (ph, a * P2, b * P2)))


def entry(r, s):
    """A(z)_rs with w = z on [0, π/2), 1 on [π/2, π]."""
    return sp.expand(z**2 * S(r, s, 0, 1) + S(r, s, 1, 2) + z * M(r, 0, 1) * M(s, 1, 2) - z * M(r, 1, 2) * M(s, 0, 1))


def border(r):
    return sp.expand(z * M(r, 0, 1) + M(r, 1, 2))


def pfaff(Mx):
    """Pfaffian by expansion along the first row (small matrices only)."""
    n = Mx.shape[0]
    if n == 0:
        return sp.Integer(1)
    out = 0
    for j in range(1, n):
        if Mx[0, j] == 0:
            continue
        keep = [i for i in range(n) if i not in (0, j)]
        out += (-1) ** (j + 1) * Mx[0, j] * pfaff(Mx.extract(keep, keep))
    return sp.expand(out)


def amat(k):
    A = sp.Matrix(k, k, lambda r, s: entry(r, s))
    if k % 2:
        b = sp.Matrix([border(r) for r in range(k)])
        A = A.row_join(b).col_join((-b.T).row_join(sp.zeros(1, 1)))
    return A


G = {}
for k in range(1, 9):
    t = time.time()
    Pf = pfaff(amat(k))
    g = sp.expand(sp.simplify(Pf / Pf.subs(z, 1)))
    G[k] = sp.Poly(g, z)
    coeffs = [sp.nsimplify(sp.simplify(G[k].coeff_monomial(z**j))) for j in range(k + 1)]
    say(f"k = {k} ({time.time() - t:.1f} s): " + ", ".join(f"{c}" for c in coeffs))
    say("        ≈ " + ", ".join(f"{float(c):.8f}" for c in coeffs))

# ---------------------------------------------------------------- R1: against run 2
run2 = {
    1: [sp.Rational(1, 2), sp.Rational(1, 2)],
    2: [sp.Rational(1, 2) - sp.pi / 8, sp.pi / 4, sp.Rational(1, 2) - sp.pi / 8],
    3: [(sp.pi - 3) / (4 * sp.pi), (sp.pi + 3) / (4 * sp.pi), (sp.pi + 3) / (4 * sp.pi), (sp.pi - 3) / (4 * sp.pi)],
    4: [sp.Rational(19, 256) - 3 * sp.pi / 128, 3 * sp.pi / 64, sp.Rational(109, 128) - 3 * sp.pi / 64, 3 * sp.pi / 64,
        sp.Rational(19, 256) - 3 * sp.pi / 128],
}
# run 2 counted j inside from the low-φ end; G's z marks φ < π/2, the same thing
r1 = all(sp.simplify(G[k].coeff_monomial(z**j) - run2[k][k - j]) == 0 for k in run2 for j in range(k + 1))
verdict["R1"] = r1
say(f"R1  G_k matches run 2 for k = 1 … 4: {r1}")

# ---------------------------------------------------------------- R2: normalised and exchange-symmetric
r2 = True
for k, g in G.items():
    e = g.as_expr()
    r2 &= sp.simplify(e.subs(z, 1) - 1) == 0
    r2 &= sp.simplify(sp.expand(z**k * e.subs(z, 1 / z)) - e) == 0
verdict["R2"] = r2
say(f"R2  G_k(1) = 1 and z^k G_k(1/z) = G_k(z), k ≤ 8: {r2}")

# ---------------------------------------------------------------- R3: the form of P_in(k)
r3 = True
for k, g in G.items():
    p = sp.expand(sp.simplify(g.coeff_monomial(z**k)))
    if k % 2 == 0:
        q = sp.Poly(p, sp.pi)
        ok = q.degree() <= 1 and all(c.is_rational for c in q.all_coeffs())
    else:
        q = sp.Poly(sp.expand(p * sp.pi), sp.pi)
        ok = q.degree() <= 1 and all(c.is_rational for c in q.all_coeffs())
    r3 &= ok
    say(f"R3  P_in({k}) = {p}   ({'ok' if ok else 'OTHER FORM'})")
verdict["R3"] = r3

# ---------------------------------------------------------------- R4: brute force at k = 5, 6
rng = np.random.default_rng(20261028)
N = 10**6
r4 = True
for k in (5, 6):
    A = rng.standard_normal((N, k, k))
    B = rng.standard_normal((N, k, k))
    X = np.linalg.solve(np.transpose(A, (0, 2, 1)), np.transpose(B, (0, 2, 1)))
    t = np.linalg.svd(X, compute_uv=False)
    inside = (t <= 1).sum(axis=1)
    for j in range(k + 1):
        p = float(G[k].coeff_monomial(z**j))
        mc = np.mean(inside == j)
        se = math.sqrt(max(p * (1 - p), 1e-12) / N)
        zz = (mc - p) / se
        r4 &= abs(zz) < 4
        say(f"R4  k = {k}, j = {j}: formula {p:.6f}, MC {mc:.6f}, z {zz:+.2f}")
verdict["R4"] = r4

# ---------------------------------------------------------------- R5: the asymptotic, 80 digits
mp.mp.dps = 80


def Snum(r, s, a, b):
    """The same entry numerically from its exact sympy form (cached)."""
    return mp.mpf(sp.N(S(r, s, a, b), 90))


def Mnum(r, a, b):
    return mp.mpf(sp.N(M(r, a, b), 90))


def pin(k):
    def mat(a, b):
        Am = mp.matrix(k + (k % 2), k + (k % 2))
        for r in range(k):
            for s in range(k):
                Am[r, s] = Snum(r, s, a, b)
            if k % 2:
                Am[r, k] = Mnum(r, a, b)
                Am[k, r] = -Mnum(r, a, b)
        return Am
    return mp.sqrt(abs(mp.det(mat(0, 1)) / mp.det(mat(0, 2))))


ks = list(range(10, 25))
L = []
for k in ks:
    v = pin(k)
    L.append(-mp.log(v))
    say(f"    k = {k}: P_in = {mp.nstr(v, 12)},  −ln P_in = {mp.nstr(L[-1], 12)},  /k² = {mp.nstr(L[-1] / k**2, 8)}")
# check the 80-digit route against the symbolic values at k = 5..8
chk = max(abs(pin(k) - mp.mpf(sp.N(G[k].coeff_monomial(z**k), 90))) for k in (5, 6, 7, 8))
say(f"    80-digit route against the symbolic P_in(5 … 8): largest difference {mp.nstr(chk, 3)}")
Amat = mp.matrix([[k * k, k, 1] for k in ks])
sol = mp.lu_solve(Amat.T * Amat, Amat.T * mp.matrix(L))
a_fit, b_fit, c_fit = sol
r5 = abs(a_fit - mp.log(2) / 2) < 0.02 and chk < mp.mpf(10) ** -40
verdict["R5"] = r5
say(f"R5  fit −ln P_in ≈ a k² + b k + c over k = 10 … 24: a = {mp.nstr(a_fit, 8)} (ln2/2 = {mp.nstr(mp.log(2)/2, 8)}), "
    f"b = {mp.nstr(b_fit, 6)}, c = {mp.nstr(c_fit, 6)}")

say("")
for kk in ["R1", "R2", "R3", "R4", "R5"]:
    say(f"{kk}: {'not killed' if verdict[kk] else 'KILLED'}")
say(f"({time.time() - T0:.0f} s)")
