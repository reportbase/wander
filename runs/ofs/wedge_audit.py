"""Audit of OFS Proposition 5(e), "More parties" and Proposition 3(f)/(d).

Exact closed forms checked against mpmath quadrature (30 digits; tolerance 1e-12 unless stated).
n = number of OTHER parties (as in "More parties"); the system has n + 1 unit relations
(h, v_1, ..., v_n); the relation lies on the unit sphere S^n in R^(n+1); the readings
s = (v_1/h, ..., v_n/h) live in [0, inf)^n.  Uniform = uniform by area on the positive orthant of S^n.

Key device (independent of any symmetry argument): Gamma-function splitting
  (1 + |s|^2)^(-p) = (1/Gamma(p)) * int_0^inf t^(p-1) e^(-t) e^(-t|s|^2) dt,
which factorises any integral of the density over a product of intervals into 1D Gaussian pieces.
Run from the repository root:  python3 runs/ofs/wedge_audit.py
"""
from mpmath import mp, mpf, gamma, pi, sqrt, quad, erf, erfc, exp, atan, inf, binomial, matrix, det, diff, cos, sin, asin
import random

mp.dps = 30
TOL = mpf('1e-12')
fails = []

def check(name, got, want, tol=TOL):
    err = abs(got - want)
    ok = err <= tol * max(1, abs(want))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}: got {mp.nstr(got, 15)}  want {mp.nstr(want, 15)}  |err| {mp.nstr(err, 3)}")
    if not ok:
        fails.append(name)

def Z(n):  # the paper's constant
    return 2**n * gamma(mpf(n + 1) / 2) / pi**(mpf(n + 1) / 2)

def orthant_area_Sn(n):  # area of the positive orthant of S^n (in R^(n+1))
    return 2 * pi**(mpf(n + 1) / 2) / gamma(mpf(n + 1) / 2) / 2**(n + 1)

def gamma_split(n, pieces):
    """Z_n * int over a product of 1D sets of (1+|s|^2)^(-(n+1)/2) ds, where pieces is a list of n functions
    t -> int_{set_i} e^(-t s^2) ds."""
    p = mpf(n + 1) / 2
    def f(t):
        v = t**(p - 1) * exp(-t)
        for g in pieces:
            v *= g(t)
        return v
    return Z(n) / gamma(p) * quad(f, [0, 1, 10, inf])

half_line = lambda t: sqrt(pi) / (2 * sqrt(t))                 # int_0^inf e^(-t s^2) ds
unit_int  = lambda t: sqrt(pi) * erf(sqrt(t)) / (2 * sqrt(t))   # int_0^1
past_int  = lambda t: sqrt(pi) * erfc(sqrt(t)) / (2 * sqrt(t))  # int_1^inf
point     = lambda s: (lambda t: exp(-t * s * s))               # a fixed coordinate (density, not integral)

print("1. Indexing.")
print("  Prop 3(d): 'n freedoms ... 2^n orthants: 4 quadrants for the circle, 8 octants for the sphere'"
      " -> there n counts unit relations (circle n=2).")
print("  'More parties': n other parties, n+1 unit relations, sphere S^n in R^(n+1), 2^(n+1) orthants.")
for n in range(1, 6):
    print(f"   n={n} other parties: {n+1} unit relations, sphere S^{n} (dim {n}) in R^{n+1}, readings in R^{n},"
          f" orthants 2^{n+1}={2**(n+1)}; Prop 3(d) with n={n} would give {2**n}")
check("Z_1 = sweep's 2/pi (Prop 5(b))", Z(1), 2 / pi)
check("Z_2 = 2/pi, the constant of 5(e)", Z(2), 2 / pi)

print("2. Area element of the gnomonic map s -> (1,s)/r is r^-(n+1) (Gram determinant, numerical derivatives).")
random.seed(1)
for n in range(1, 6):
    s0 = [mpf(random.uniform(0.05, 3)) for _ in range(n)]
    def emb(*s):
        r = sqrt(1 + sum(x * x for x in s))
        return [1 / r] + [x / r for x in s]
    J = matrix(n + 1, n)
    for j in range(n):
        for i in range(n + 1):
            J[i, j] = diff(lambda x: emb(*[x if k == j else s0[k] for k in range(n)])[i], s0[j])
    G = J.T * J
    r = sqrt(1 + sum(x * x for x in s0))
    check(f"n={n} sqrt(det Gram) * r^(n+1)", sqrt(det(G)) * r**(n + 1), 1, mpf('1e-10'))

print("3. Normalisation: Z_n * int_[0,inf)^n (1+|s|^2)^(-(n+1)/2) ds = 1, and the total area = orthant of S^n.")
for n in range(1, 6):
    check(f"n={n} total (Gamma split)", gamma_split(n, [half_line] * n), 1)
    # radial: area of positive orthant of S^(n-1) times int q^(n-1)(1+q^2)^(-(n+1)/2) dq
    radial = orthant_area_Sn(n - 1) * quad(lambda q: q**(n - 1) * (1 + q * q)**(-mpf(n + 1) / 2), [0, 1, inf])
    check(f"n={n} unnormalised area (radial) = orthant of S^{n}", radial, orthant_area_Sn(n))
    check(f"n={n} Z_n = 1/area", Z(n), 1 / orthant_area_Sn(n))

print("4. One reading s_1 = v_1/h: marginal density 2/(pi(1+s^2)), CDF(1) = 1/2, reciprocal h/v_1 same law.")
for n in range(1, 6):
    for s in [mpf(1) / 8, mpf(1) / 2, 1, 3, 20]:
        got = gamma_split(n, [point(s)] + [half_line] * (n - 1))
        check(f"n={n} marginal at s={mp.nstr(s,4)}", got, 2 / (pi * (1 + s * s)))
    med = gamma_split(n, [unit_int] + [half_line] * (n - 1))
    check(f"n={n} P(v_1/h <= 1)", med, mpf(1) / 2)
    r = mpf(3)
    lo = gamma_split(n, [lambda t: sqrt(pi) * erf(r * sqrt(t)) / (2 * sqrt(t))] + [half_line] * (n - 1))
    hi = gamma_split(n, [lambda t: sqrt(pi) * erfc(sqrt(t) / r) / (2 * sqrt(t))] + [half_line] * (n - 1))
    check(f"n={n} P(s_1<=3) = P(s_1>=1/3) (reciprocal-symmetric)", lo, hi)

print("5. Pairs: 2D marginal of (s_1,s_2) is 5(e)'s law; v_1/v_2 has CDF (2/pi)atan r, median 1.")
for n in range(2, 6):
    for (a, b) in [(mpf(1) / 4, 2), (1, 1), (3, mpf(1) / 2)]:
        got = gamma_split(n, [point(a), point(b)] + [half_line] * (n - 2))
        check(f"n={n} 2D marginal at ({mp.nstr(a,3)},{b})", got, 2 / (pi * (1 + a * a + b * b)**mpf(1.5)))
f2 = lambda a, b: 2 / (pi * (1 + a * a + b * b)**mpf(1.5))
for r in [mpf(1) / 4, 1, 4]:
    got = quad(lambda b: quad(lambda a: f2(a, b), [0, r * b]), [0, 1, inf])
    check(f"P(v_1/v_2 <= {mp.nstr(r,3)}) from 5(e)'s law", got, 2 / pi * atan(r))

print("6. Near in all readings = {s_i <= 1 for all i} = {h >= every v_i} (the same event for every n): 1/(n+1);"
      " number past the corner uniform on 0..n.")
for n in range(1, 6):
    check(f"n={n} P(near in all)", gamma_split(n, [unit_int] * n), mpf(1) / (n + 1))
    for k in range(n + 1):
        pk = binomial(n, k) * gamma_split(n, [past_int] * k + [unit_int] * (n - k))
        check(f"n={n} P(exactly {k} past)", pk, mpf(1) / (n + 1))

print("7. Is permutation symmetry needed, or do pair corners suffice?")
# orderings of (h,v,w) with probabilities; pair medians at corner but near share 0:
P = {'w>h>v': mpf(1) / 2, 'v>h>w': mpf(1) / 2}
print("  counterexample (n=2): mass 1/2 on chamber v2>h>v, 1/2 on v>h>v2:")
print("   P(v<=h)=1/2, P(v2<=h)=1/2, P(v<=v2)=1/2 (every pair at its corner), P(h largest)=0, not 1/3.")
# uniform in both angles (altitude a, azimuth psi): two pairs move off 1/3
c = (2 / pi)**2
p_vh = c * quad(lambda p: atan(cos(p)), [0, pi / 2])
near = c * quad(lambda p: atan(cos(p)), [0, pi / 4])
p_v2h = c * quad(lambda p: pi / 2 if p <= pi / 4 else 0, [0, pi / 4, pi / 2])
print(f"  uniform in altitude and azimuth: P(v<=h)={mp.nstr(p_vh,6)} (paper 0.343), P(v2<=h)={mp.nstr(p_v2h,6)},"
      f" near={mp.nstr(near,6)} (paper 0.233)")
check("altitude-azimuth P(v<=h) vs paper 0.343", p_vh, mpf('0.343'), mpf('1.5e-3'))
check("altitude-azimuth near vs paper 0.233", near, mpf('0.233'), mpf('2.5e-3'))

print("8. Height (one coordinate) on the uniform orthant of S^n: density prop. (1-t^2)^((n-2)/2).")
for n, want in [(1, lambda t: 2 / (pi * sqrt(1 - t * t))), (2, lambda t: mpf(1)), (3, lambda t: 4 / pi * sqrt(1 - t * t))]:
    k = mpf(n - 2) / 2
    norm = quad(lambda t: (1 - t * t)**k, [0, 1])
    for t in [mpf('0.3'), mpf('0.8')]:
        check(f"S^{n} ({n+1} unit relations) height density at {t}", (1 - t * t)**k / norm, want(t))

print("9. Cosine form: Z_n (1+|s|^2)^(-(n+1)/2) = Z_n cos^(n+1) alpha, alpha the angle off h.")
for n in range(1, 6):
    s = [mpf(i + 1) / 3 for i in range(n)]
    r2 = 1 + sum(x * x for x in s)
    cosa = 1 / sqrt(r2)
    check(f"n={n}", r2**(-mpf(n + 1) / 2), cosa**(n + 1))

print("10. 5(e) last bullet: drawn at c1, c2, medians 1/c1, 1/c2, c2/c1.")
for c1, c2 in [(2, 1), (mpf(1) / 2, 3)]:
    # (X, Y) = (c1 s, c2 s2) has the uniform law, so P(s <= m) = P(X <= c1 m): evaluate at m = 1/c1, and at m = 1
    m = 1 / mpf(c1)
    m1 = gamma_split(2, [lambda t: sqrt(pi) * erf(c1 * m * sqrt(t)) / (2 * sqrt(t)), half_line])
    at1 = gamma_split(2, [lambda t: sqrt(pi) * erf(c1 * sqrt(t)) / (2 * sqrt(t)), half_line])
    print(f"   P(v/h <= 1) when drawn at c1={c1}: {mp.nstr(at1, 10)} (1/2 only at c1 = 1)")
    # (c1 s, c2 s2) has the uniform law; P(s <= 1/c1) = P(c1 s <= 1) = 1/2
    check(f"(c1,c2)=({c1},{c2}) P(v/h <= 1/c1)", m1, mpf(1) / 2)
    # v/v2 = (X/c1)/(Y/c2) = (c2/c1)(X/Y); median c2/c1 since X/Y median 1 (item 5)
    print(f"   median v/v2 = c2/c1 = {mp.nstr(mpf(c2)/c1,6)} (X/Y has median 1, item 5)")

print("11. Line 694 ('In n dimensions ... sqrt(pi)Gamma((n+1)/2)/Gamma(n/2)'): n is the ambient dimension = unit relations.")
for m, want in [(2, pi / 2), (3, mpf(2)), (4, 3 * pi / 4)]:
    check(f"m={m} unit relations", sqrt(pi) * gamma(mpf(m + 1) / 2) / gamma(mpf(m) / 2), want)

print()
print("FAILED: " + ", ".join(fails) if fails else "All checks passed.")
