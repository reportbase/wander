"""QSO run 1 (plans/qso-plan.md): three readings of known quantum results in the situated framing.
F: twirls (no shared frame); W: weak values as addresses; G: Gaussian widths and the corner.
Exact where possible (mpmath, 40 digits); twirls by exact designs; samples seeded (numpy).
Run: python3 runs/qso/qso.py   (run 3: F4″, the distance |Δ(n₁·n₂)|/4; about a minute)
"""
import random
import numpy as np
from mpmath import mp, mpf, mpc, matrix, cos, sin, sqrt, exp, pi, fabs, quad, atan, tan, log, cosh, sech, factorial, inf, eye
mp.dps = 40
TOL = mpf(10)**-30
I = mpc(0, 1)
sx = matrix([[0, 1], [1, 0]]); sy = matrix([[0, -I], [I, 0]]); sz = matrix([[1, 0], [0, -1]]); one = eye(2)
ok = {}

def kron(a, b):
    m = matrix(a.rows * b.rows, a.cols * b.cols)
    for i in range(a.rows):
        for j in range(a.cols):
            for k in range(b.rows):
                for l in range(b.cols):
                    m[i * b.rows + k, j * b.cols + l] = a[i, j] * b[k, l]
    return m
def tr(m): return sum(m[i, i] for i in range(m.rows))
def dag(m): return m.H
def ket(th, al=0): return matrix([cos(th), exp(I * al) * sin(th)])
def proj(psi): return psi * psi.H
def bloch(rho): return [tr(rho * s).real for s in (sx, sy, sz)]
def mx(a): return max(abs(x) for x in a) if not isinstance(a, matrix) else max(abs(a[i, j]) for i in range(a.rows) for j in range(a.cols))
def rand_state(rng):
    z = rng.uniform(-1, 1); al = rng.uniform(0, 2 * float(pi))
    return ket(mp.acos(mpf(z)) / 2, mpf(al))

# the single-qubit Clifford group mod phase (24 elements), a unitary 2-design
Hd = matrix([[1, 1], [1, -1]]) / sqrt(2); Sg = matrix([[1, 0], [0, I]])
def canon(u):
    for i in range(2):
        for j in range(2):
            if abs(u[i, j]) > mpf('1e-20'):
                ph = u[i, j] / abs(u[i, j]); return u / ph
cliff = [one]; frontier = [one]
while frontier:
    new = []
    for u in frontier:
        for g in (Hd, Sg):
            w = canon(g * u)
            if all(mx(w - c) > mpf('1e-20') for c in cliff):
                cliff.append(w); new.append(w)
    frontier = new
assert len(cliff) == 24, len(cliff)
def twirl1(rho): return sum((u * rho * dag(u) for u in cliff), matrix(2, 2)) / 24
def twirl2(rho):
    acc = matrix(4, 4)
    for u in cliff:
        uu = kron(u, u); acc += uu * rho * dag(uu)
    return acc / 24
def phase_twirl(rho, N=4, two=False):
    acc = matrix(rho.rows, rho.cols)
    for k in range(N):
        a = 2 * pi * k / N
        u = matrix([[exp(-I * a / 2), 0], [0, exp(I * a / 2)]])
        if two: u = kron(u, u)
        acc += u * rho * dag(u)
    return acc / N

rng = random.Random(5)
# F1, F2
e1 = e2 = mpf(0)
for _ in range(20):
    psi = rand_state(rng); rho = proj(psi); n = bloch(rho)
    m = bloch(phase_twirl(rho))
    e1 = max(e1, fabs(m[0]), fabs(m[1]), fabs(m[2] - n[2]))
    e2 = max(e2, mx(twirl1(rho) - one / 2))
ok['F1'] = e1 <= TOL; ok['F2'] = e2 <= TOL
print(f"F1 phase twirl: n → (0, 0, n_z), visibility lost, predictability kept: worst {mp.nstr(e1, 3)}")
print(f"F2 SU(2) twirl of one qubit → I/2: worst {mp.nstr(e2, 3)}")
# F3, F4
singlet = matrix([0, 1, -1, 0]) / sqrt(2); Ps = proj(singlet); Pt = eye(4) - Ps
swap = matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
def tdist(a, b):
    d = a - b
    ev = mp.eighe(d)[0]
    return sum(fabs(x) for x in ev) / 2
e3 = mpf(0); e4 = mpf(0); sep = True; pairs = []
for _ in range(20):
    a, b = rand_state(rng), rand_state(rng)
    na, nb = bloch(proj(a)), bloch(proj(b)); dot = sum(x * y for x, y in zip(na, nb))
    rho = proj(kron(a, b)); tw = twirl2(rho)
    p = (1 - dot) / 4
    e3 = max(e3, mx(tw - (p * Ps + (1 - p) / 3 * Pt)), fabs(abs((a.H * b)[0])**2 - (1 + dot) / 2), fabs((1 - 2 * p) - (1 + dot) / 2))
    e4 = max(e4, fabs(tr(swap * tw) - tr(swap * rho)))
    # a rotated copy: a Clifford element is a rotation; also an arbitrary rotation exp(-i σ·u t/2)
    u = cos(mpf('0.7')) * one - I * sin(mpf('0.7')) * (sx * mpf('0.6') + sz * mpf('0.8'))
    tw_r = twirl2(proj(kron(u * a, u * b)))
    e4 = max(e4, mx(tw_r - tw))
    pairs.append((dot, tw))
for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        dd = fabs(pairs[i][0] - pairs[j][0])
        if dd > mpf('1e-3'):
            # F4″ (run 3): trace distance between the Werner states is |Δp| = |Δ(n₁·n₂)|/4 (run 2's /3 killed)
            td = tdist(pairs[i][1], pairs[j][1])
            if td < mpf('1e-3') or fabs(td - dd / 4) > TOL: sep = False
ok['F3'] = e3 <= TOL; ok['F4'] = e4 <= TOL and sep
print(f"F3 U⊗U twirl = p·singlet + (1−p)/3·triplet, p = (1 − n₁·n₂)/4, overlap read back: worst {mp.nstr(e3, 3)}")
print(f"F4 rotated pair, same twirled state; swap kept: worst {mp.nstr(e4, 3)}; different n₁·n₂ told apart: {sep}")
# F5
e5 = mpf(0)
sp = matrix([[0, 1], [0, 0]]); sm = matrix([[0, 0], [1, 0]])
for _ in range(20):
    t1, t2 = mpf(rng.uniform(0, 1.5)), mpf(rng.uniform(0, 1.5)); a1, a2 = mpf(rng.uniform(0, 6.28)), mpf(rng.uniform(0, 6.28))
    rho = proj(kron(ket(t1, a1), ket(t2, a2))); tw = phase_twirl(rho, N=4, two=True)
    A = tr(tw * kron(sx, one)); B = tr(tw * kron(one, sy))
    c = tr(tw * kron(sp, sm)); target = sin(2 * t1) * sin(2 * t2) / 4 * exp(I * (a1 - a2))
    e5 = max(e5, abs(A), abs(B), min(abs(c - target), abs(c - target.conjugate())), abs(c - tr(rho * kron(sp, sm))))
ok['F5'] = e5 <= TOL
print(f"F5 common phase twirl: each qubit's transverse part 0, ⟨σ₊⊗σ₋⟩ = (sin2θ₁ sin2θ₂/4)·e^(i(α₁−α₂)) kept: worst {mp.nstr(e5, 3)}")

# W1
def weak(i, f): return (f.H * sz * i)[0] / (f.H * i)[0]
e6 = mpf(0)
for _ in range(30):
    i, f = rand_state(rng), rand_state(rng)
    n, m = bloch(proj(i)), bloch(proj(f))
    cross_z = (m[0] * 0 - 0) ; mxz = [m[1] * 1 - m[2] * 0, m[2] * 0 - m[0] * 1, 0]   # m × ẑ
    im = sum(x * y for x, y in zip(mxz, n)); dot = sum(x * y for x, y in zip(m, n))
    w = weak(i, f); pred = mpc(n[2] + m[2], im) / (1 + dot); pred2 = mpc(n[2] + m[2], -im) / (1 + dot)
    e6 = max(e6, min(abs(w - pred), abs(w - pred2)))
ok['W1'] = e6 <= TOL
print(f"W1 A_w = (n_z + m_z ± i (m×ẑ)·n)/(1 + m·n): worst {mp.nstr(e6, 3)}")
# W2: foot-weighted mean of Re A_w over m uniform = n_z; Re A_w (1+m·n)/2 = (n_z+m_z)/2
e7 = mpf(0)
for _ in range(5):
    i = rand_state(rng); n = bloch(proj(i))
    def integrand(a, b):   # m in spherical coordinates about z
        m = [sin(a) * cos(b), sin(a) * sin(b), cos(a)]
        dot = sum(x * y for x, y in zip(m, n))
        return ((n[2] + m[2]) / (1 + dot)) * (1 + dot) / 2 * sin(a)
    num = quad(integrand, [0, pi], [0, 2 * pi])
    den = quad(lambda a, b: (1 + sum(x * y for x, y in zip([sin(a) * cos(b), sin(a) * sin(b), cos(a)], n))) / 2 * sin(a), [0, pi], [0, 2 * pi])
    e7 = max(e7, fabs(num / den - n[2]))
ok['W2'] = e7 <= mpf(10)**-25
print(f"W2 foot-weighted mean of Re A_w = n_z: worst {mp.nstr(e7, 3)}")
# W3: n = x̂. P(|Re A_w| > x) for m uniform: (1/2π)∫db (1/(1+t²)) with t = x/|sin b|, i.e. P(s > t) = 1/(1+t²)
mp.dps = 35
def P_unw(x): return quad(lambda b: 1 / (1 + (x / fabs(sin(b)))**2), [0, pi / 2]) * 4 / (2 * pi)
def P_w(x):   # foot-weighted: weight (1+cos a)/2 normalised by 1/2: P(s > t) = 1/(1+t²)²
    return quad(lambda b: 1 / (1 + (x / fabs(sin(b)))**2)**2, [0, pi / 2]) * 4 / (2 * pi)
e8 = mpf(0)
for x in (mpf('0.5'), mpf(1), mpf(3), mpf(30)):
    e8 = max(e8, fabs(P_unw(x) - (1 - x / sqrt(1 + x * x))))
    # (3/4)(1+x²)^(-5/2): tail 1 − x(2x²+3)/(2(1+x²)^(3/2))
    e8 = max(e8, fabs(P_w(x) - (1 - x * (2 * x * x + 3) / (2 * (1 + x * x)**mpf(1.5)))))
sw_u, sw_w = P_unw(mpf(1)), P_w(mpf(1))
var_w = quad(lambda a, b: (tan(a / 2) * sin(b))**2 * (1 + cos(a)) / 2 * sin(a), [0, pi], [0, 2 * pi]) / (2 * pi)
e8 = max(e8, fabs(sw_u - (1 - 1 / sqrt(2))), fabs(sw_w - (1 - 5 / (4 * sqrt(2)))), fabs(var_w - mpf(1) / 2))
# check the reduction Re A_w = tan(a/2) sin b against the matrices at random m, n = x̂
ix = matrix([1, 1]) / sqrt(2)
for _ in range(20):
    a, b = mpf(rng.uniform(0.1, 3.0)), mpf(rng.uniform(0, 6.28))
    # m = cos a x̂ + sin a (cos b ŷ' + sin b ẑ) with ŷ' = ŷ: a state with Bloch vector m
    m = [cos(a), sin(a) * cos(b), sin(a) * sin(b)]
    th = mp.acos(m[2]) / 2; al = mp.atan2(m[1], m[0])
    e8 = max(e8, fabs(weak(ix, ket(th, al)).real - tan(a / 2) * sin(b)))
ok['W3q'] = e8 <= mpf(10)**-28
mp.dps = 40
print(f"W3 n = x̂: P(|Re A_w|>1) = {mp.nstr(sw_u, 12)} (1 − 1/√2 = {mp.nstr(1 - 1 / sqrt(2), 12)}), foot-weighted {mp.nstr(sw_w, 12)}"
      f" (1 − 5/(4√2) = {mp.nstr(1 - 5 / (4 * sqrt(2)), 12)}), weighted variance {mp.nstr(var_w, 12)}; worst {mp.nstr(e8, 3)}")
# samples
g = np.random.default_rng(16)
N = 10**6
def unif(N):
    v = g.normal(size=(N, 3)); return v / np.linalg.norm(v, axis=1)[:, None]
M = unif(N); nx = np.array([1.0, 0, 0])
re = (nx[2] + M[:, 2]) / (1 + M @ nx)
w = (1 + M @ nx) / 2
p_u = np.mean(np.abs(re) > 1); se_u = np.sqrt(p_u * (1 - p_u) / N)
p_w = np.sum(w * (np.abs(re) > 1)) / np.sum(w)
# weighted se: by resampling-free delta method
z = w * ((np.abs(re) > 1) - p_w); se_w = np.sqrt(np.sum(z**2)) / np.sum(w)
tail = [np.mean(np.abs(re) > x) for x in (100, 1000)]
ok['W3s'] = abs(p_u - (1 - 2**-0.5)) <= 3 * se_u and abs(p_w - (1 - 5 / (4 * 2**0.5))) <= 3 * se_w
print(f"   samples: unweighted {p_u:.5f} ± {se_u:.5f}, weighted {p_w:.5f} ± {se_w:.5f}; P(|Re|>100), P(>1000) = {tail[0]:.2e}, {tail[1]:.2e}"
      f" (1/(2x²): {0.5e-4:.2e}, {0.5e-6:.2e})")
ok['W3'] = ok['W3q'] and ok['W3s']
# W4: both uniform
mp.dps = 25
def p_beta(beta):
    cb, sb = cos(beta), sin(beta)
    def f(b):
        c = cos(b)
        if fabs(c) < mpf(10)**-30 or sb < mpf(10)**-30: return mpf(0)
        s1 = (1 + cb) / (c * sb) if c > 0 else (1 - cb) / (-c * sb)
        return 1 / (1 + s1 * s1)
    return quad(f, [0, pi / 2, pi, 3 * pi / 2, 2 * pi]) / (2 * pi)
P4 = quad(lambda be: p_beta(be) * sin(be) / 2, [0, pi / 2, pi])
mp.dps = 40
N2 = N
Nv = unif(N2); M2 = unif(N2)
re2 = (Nv[:, 2] + M2[:, 2]) / (1 + np.sum(Nv * M2, axis=1))
p4 = np.mean(np.abs(re2) > 1); se4 = np.sqrt(p4 * (1 - p4) / N2)
ok['W4'] = fabs(P4 - mpf(1) / 3) <= mpf(10)**-20 and abs(p4 - 1 / 3) <= 3 * se4
print(f"W4 both uniform: P(|Re A_w|>1) = {mp.nstr(P4, 22)} by quadrature, {p4:.5f} ± {se4:.5f} by samples (1/3)")

# G1, G2, G4
def g_ov(s1, s2):
    f = lambda x: (2 * pi * s1 * s1)**mpf(-0.25) * (2 * pi * s2 * s2)**mpf(-0.25) * exp(-x * x / (4 * s1 * s1) - x * x / (4 * s2 * s2))
    return quad(f, [-inf, 0, inf])**2
e9 = mpf(0); e10 = mpf(0)
for k in (mpf('0.01'), mpf('0.1'), mpf('0.3'), mpf('0.5'), mpf('0.8'), mpf(1), mpf('1.25'), mpf(2), mpf('3.3'), mpf(10), mpf(100), mpf('7.7')):
    F = g_ov(k, mpf(1))
    e9 = max(e9, fabs(F - 2 * k / (1 + k * k)), fabs(F - sech(log(k))), fabs(F - g_ov(1 / k, mpf(1))))
    h, v = k / sqrt(1 + k * k), 1 / sqrt(1 + k * k)
    e9 = max(e9, fabs(F - 2 * h * v), fabs(2 * h * v - sech(log(v / h))))
    for c in (mpf('1e-3'), mpf(7), mpf('1e4')):
        e10 = max(e10, fabs(g_ov(c * k, c) - F))
ok['G1'] = ok['G2'] = e9 <= TOL; ok['G4'] = e10 <= TOL
print(f"G1–G2 |⟨g_σ₁|g_σ₂⟩|² = 2k/(1+k²) = sech ln k = 2hv: worst {mp.nstr(e9, 3)}")
print(f"G4 both widths times c (another H): unchanged, worst {mp.nstr(e10, 3)}")
# G3
e11 = mpf(0)
for r in (mpf('0.3'), mpf(1), mpf(2)):
    coef = lambda n: cosh(r)**mpf(-0.5) * (-mp.tanh(r))**n * sqrt(factorial(2 * n)) / (2**n * factorial(n))
    norm = mp.nsum(lambda n: coef(int(n))**2, [0, inf])
    e11 = max(e11, fabs(norm - 1), fabs(coef(0)**2 - sech(r)), fabs(coef(0)**2 - g_ov(exp(r), mpf(1))))
ok['G3'] = e11 <= TOL
print(f"G3 squeezed vacuum: Fock series normalised, |⟨0|S(r)|0⟩|² = sech r = G1 at k = e^r: worst {mp.nstr(e11, 3)}")
for k in ('F1', 'F2', 'F3', 'F4', 'F5', 'W1', 'W2', 'W3', 'W4', 'G1', 'G2', 'G3', 'G4'):
    print(k, 'not killed' if ok[k] else 'KILLED')
