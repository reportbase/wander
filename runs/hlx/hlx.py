"""HLX run 1: the holonomy laws in the leftover's half-slope, computed from the loops themselves (plans/hlx-plan.md).
Exact rational arithmetic. Run from the repository root."""
from fractions import Fraction as F

AX = [(F(3, 5), F(4, 5), F(0)), (F(0), F(3, 5), F(4, 5)), (F(1), F(0), F(0)), (F(2, 3), F(1, 3), F(2, 3)),
      (F(2, 7), F(3, 7), F(6, 7)), (F(6, 7), F(-2, 7), F(3, 7))]
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
cross = lambda a, b: (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
for v in AX:
    assert dot(v, v) == 1


# ---- 89: two turns about two axes, the loop a b a^-1 b^-1 ----
def qmul(p, q):
    a, u = p[0], p[1:]
    b, v = q[0], q[1:]
    s = a * b - dot(u, v)
    w = tuple(a * v[i] + b * u[i] + cross(u, v)[i] for i in range(3))
    return (s,) + w


def qbar(p):
    return (p[0], -p[1], -p[2], -p[3])


cases89 = [(F(1, 2), F(1, 3), 0, 1), (F(2), F(3, 4), 2, 3), (F(1, 7), F(5, 2), 1, 4), (F(3), F(1, 9), 0, 5),
           (F(4, 5), F(6, 5), 3, 5)]
ok89 = []
for ta, tb, i, j in cases89:
    na, nb = AX[i], AX[j]
    pa = (F(1),) + tuple(ta * x for x in na)
    pb = (F(1),) + tuple(tb * x for x in nb)
    P = qmul(qmul(qmul(pa, pb), qbar(pa)), qbar(pb))
    norm = (1 + ta * ta) * (1 + tb * tb)
    cos_half = P[0] / norm
    tau2 = sum(x * x for x in P[1:]) / (P[0] * P[0])
    law_cos = 1 - 2 * (ta * ta / (1 + ta * ta)) * (tb * tb / (1 + tb * tb)) * (1 - dot(na, nb) ** 2)
    law_tau2 = 1 / law_cos ** 2 - 1
    good = cos_half == law_cos and tau2 == law_tau2 and isinstance(tau2, F)
    ok89.append(good)
    print(f'89  t_a={ta} t_b={tb} n_a.n_b={dot(na, nb)}: cos(Θ/2)={cos_half}, τ²={tau2}  law {"=" if good else "≠"}')


# ---- 90: a turn and an unequal stretch, L = S^-1 R(-α) S R(α) ----
def mm(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def rot2(t):
    d = 1 + t * t
    return [[(1 - t * t) / d, -2 * t / d], [2 * t / d, (1 - t * t) / d]]


cases90 = [(F(1, 3), F(3, 2)), (F(2), F(5, 4)), (F(1, 5), F(7)), (F(3, 4), F(2, 9)), (F(5), F(4, 3))]
ok90 = []
for t, q in cases90:
    c = q * q
    S, Si = [[q, F(0)], [F(0), 1 / q]], [[1 / q, F(0)], [F(0), q]]
    L = mm(mm(mm(Si, rot2(-t)), S), rot2(t))
    cosh = (L[0][0] + L[1][1]) / 2
    u2 = (cosh - 1) / (cosh + 1)
    sin2 = (2 * t / (1 + t * t)) ** 2
    law = 1 + 2 * sin2 * ((c - 2 + 1 / c) / 4)
    good = cosh == law and isinstance(u2, F)
    ok90.append(good)
    print(f'90  t={t} c={c}: cosh ζ={cosh}, u²={u2}  law {"=" if good else "≠"}')


# ---- 92: Thomas-Wigner, two boosts with rational half-rapidities along rational directions ----
def boost(g, w):  # g = gamma, w = gamma*beta*n, a 4x4 Lorentz boost
    M = [[g] + list(w)]
    for i in range(3):
        M.append([w[i]] + [(1 if i == j else 0) + w[i] * w[j] / (g + 1) for j in range(3)])
    return M


def boost_of(a, n):
    beta = 2 * a / (1 + a * a)
    g = (1 + a * a) / (1 - a * a)
    return boost(g, tuple(g * beta * x for x in n))


cases92 = [(F(1, 3), F(1, 2), 0, 1), (F(1, 5), F(2, 3), 2, 3), (F(1, 2), F(1, 4), 1, 4), (F(3, 5), F(1, 7), 0, 5),
           (F(2, 5), F(3, 7), 3, 5)]
ok92 = []
for a, b, i, j in cases92:
    n1, n2 = AX[i], AX[j]
    B1, B2 = boost_of(a, n1), boost_of(b, n2)
    M = mm(B2, B1)
    g = M[0][0]
    w = tuple(M[i][0] for i in range(1, 4))
    Bi = boost(g, tuple(-x for x in w))
    R = mm(Bi, M)
    assert R[0][0] == 1 and all(R[0][k] == 0 and R[k][0] == 0 for k in range(1, 4))
    cosT = (R[1][1] + R[2][2] + R[3][3] - 1) / 2
    tau2 = (1 - cosT) / (1 + cosT)
    cphi = dot(n1, n2)
    sphi2 = 1 - cphi * cphi
    law_tau2 = (a * b) ** 2 * sphi2 / (1 + a * b * cphi) ** 2
    good = tau2 == law_tau2 and isinstance(tau2, F)
    ok92.append(good)
    print(f'92  a={a} b={b} cos φ={cphi}: τ²={tau2}  law {"=" if good else "≠"}')

print(f'\nH1 (89): {sum(ok89)}/5;  H2 (90): {sum(ok90)}/5;  H3 (92): {sum(ok92)}/5')
print('H4 (102): (θ₁θ₂/2)·sin(φ/2)/(φ/2) is a leading-order term with φ/2 bare; not tested by arithmetic.')
