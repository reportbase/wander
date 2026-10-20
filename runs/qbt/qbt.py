"""QBT run 1 (plans/qbt-plan.md): the qubit's state (a direction at θ) and its Bloch point (at 2θ, the state squared)
as the two sweeps of OFS §4. Exact, mpmath at 40 digits.
Run: python3 runs/qbt/qbt.py
"""
import random
from mpmath import mp, mpf, mpc, matrix, cos, sin, sqrt, exp, pi, fabs
mp.dps = 40
TOL = mpf(10)**-30
I = mpc(0, 1)
sx = matrix([[0, 1], [1, 0]]); sy = matrix([[0, -I], [I, 0]]); sz = matrix([[1, 0], [0, -1]])
def ket(th, al=0): return matrix([cos(th), exp(I * al) * sin(th)])
def ev(op, psi):
    return (psi.H * op * psi)[0].real
def bloch(psi): return [ev(sx, psi), ev(sy, psi), ev(sz, psi)]
def norm(v): return sqrt(sum(x * x for x in v))
def inner(a, b): return (a.H * b)[0]
ok = {}
random.seed(3)
pairs = [(mpf(random.random()) * pi / 2, mpf(random.random()) * 2 * pi) for _ in range(30)]
# Q1, Q2
e1 = e2 = mpf(0)
for th, al in pairs:
    n = bloch(ket(th, al))
    e1 = max(e1, fabs(n[0] - sin(2 * th) * cos(al)), fabs(n[1] - sin(2 * th) * sin(al)), fabs(n[2] - cos(2 * th)))
    h, v = cos(th), sin(th)
    n0 = bloch(ket(th, 0))
    e1 = max(e1, fabs(n0[0] - 2 * h * v), fabs(n0[1]), fabs(n0[2] - (h * h - v * v)))
    p0 = abs(inner(matrix([1, 0]), ket(th, al)))**2
    e2 = max(e2, fabs(p0 - h * h), fabs(p0 - (1 + n[2]) / 2))
ok['Q1'] = e1 <= TOL; ok['Q2'] = e2 <= TOL
print(f"Q1 Bloch point = (sin2θ cosα, sin2θ sinα, cos2θ), real slice (2hv, 0, h²−v²): worst {mp.nstr(e1, 3)}")
print(f"Q2 Born's rule P(0) = h² = (1 + n_z)/2: worst {mp.nstr(e2, 3)}")
# Q3
e3 = mpf(0)
for th, al in pairs:
    a, b = ket(th, al), ket(th + pi / 2, al)
    na, nb = bloch(a), bloch(b)
    e3 = max(e3, abs(inner(a, b)), max(fabs(x + y) for x, y in zip(na, nb)))
for k in range(30):
    a = ket(*pairs[k]); b = ket(*pairs[(k + 7) % 30])
    na, nb = bloch(a), bloch(b)
    e3 = max(e3, fabs(abs(inner(a, b))**2 - (1 + sum(x * y for x, y in zip(na, nb))) / 2))
ok['Q3'] = e3 <= TOL
print(f"Q3 orthogonal states antipodal; |⟨ψ₁|ψ₂⟩|² = (1 + n₁·n₂)/2: worst {mp.nstr(e3, 3)}")
# Q4
def turn(beta):  # exp(−iσ_y β) = cos β − iσ_y sin β, a real rotation of the amplitudes
    return matrix([[cos(beta), -sin(beta)], [sin(beta), cos(beta)]])
e4 = mpf(0)
for th, _ in pairs[:10]:
    psi = ket(th)
    for beta in (mpf('0.3'), mpf(1), pi / 3):
        n0, n1 = bloch(psi), bloch(turn(beta) * psi)
        rot = [n0[0] * cos(2 * beta) + n0[2] * sin(2 * beta), n0[1], -n0[0] * sin(2 * beta) + n0[2] * cos(2 * beta)]
        e4 = max(e4, max(fabs(x - y) for x, y in zip(n1, rot)))
    m = turn(pi) * psi; e4 = max(e4, max(abs(x + y) for x, y in zip(m, psi)), max(fabs(x - y) for x, y in zip(bloch(m), bloch(psi))))
    m2 = turn(2 * pi) * psi; e4 = max(e4, max(abs(x - y) for x, y in zip(m2, psi)))
ok['Q4'] = e4 <= TOL
print(f"Q4 a state turn β turns n by 2β; β = π gives −ψ with the same n, 2π gives ψ: worst {mp.nstr(e4, 3)}")
# Q5
e5 = mpf(0)
for th, al in pairs:
    if th < mpf('0.01'): continue
    psi = ket(th, al); n = bloch(psi)
    zeta = psi[1] / psi[0]
    e5 = max(e5, abs(zeta - exp(I * al) * sin(th) / cos(th)), abs(zeta - mpc(n[0], n[1]) / (1 + n[2])))
    z0 = ket(th)[1] / ket(th)[0]
    e5 = max(e5, abs(z0 - sin(th) / cos(th)))
ok['Q5'] = e5 <= TOL
print(f"Q5 ζ = ψ₁/ψ₀ = e^(iα)·tanθ = (n_x + i n_y)/(1 + n_z); real slice ζ = v/h: worst {mp.nstr(e5, 3)}")
# Q6
e6 = mpf(0); inside = True
plus = matrix([1, 1]) / sqrt(2); zero = matrix([1, 0])
def bl(rho): return [(rho * s)[0, 0].real + (rho * s)[1, 1].real for s in (sx, sy, sz)]
for a in (mpf('0.05'), mpf('0.24'), mpf('0.5'), mpf('0.9')):
    psi = matrix([1, sqrt(a)]) / sqrt(1 + a)
    n = bloch(psi)
    e6 = max(e6, fabs(sqrt(n[0]**2 + n[1]**2) - 2 * sqrt(a) / (1 + a)), fabs(fabs(n[2]) - (1 - a) / (1 + a)), fabs(norm(n) - 1))
    rho = (2 * a * (plus * plus.H) + (1 - a) * (zero * zero.H)) / (1 + a)
    m = bl(rho)
    e6 = max(e6, fabs(sqrt(m[0]**2 + m[1]**2) - 2 * a / (1 + a)), fabs(m[2] - (1 - a) / (1 + a)))
    inside &= norm(m) < 1 - mpf('1e-3')
    print(f"   a = {a}: foil V {mp.nstr(sqrt(n[0]**2 + n[1]**2), 10)}, P {mp.nstr(n[2], 10)}, |n| {mp.nstr(norm(n), 10)};"
          f" chopper V {mp.nstr(sqrt(m[0]**2 + m[1]**2), 10)}, P {mp.nstr(m[2], 10)}, |n| {mp.nstr(norm(m), 10)}")
ok['Q6'] = e6 <= TOL and inside
print(f"Q6 foil on the sphere, chopper inside the ball: worst {mp.nstr(e6, 3)}, mixtures inside: {inside}")
for k in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6'):
    print(k, 'not killed' if ok[k] else 'KILLED')
