# OFS review 35, G3: two sweeps that each return to their start, each in its own inner product,
# can compose to a map that grows without bound; together bounded only if they share one.
import numpy as np
def R(a, i, j):
    M = np.eye(3); c, s = np.cos(a), np.sin(a)
    M[i, i] = c; M[j, j] = c; M[i, j] = -s; M[j, i] = s
    return M
rng = np.random.default_rng(1); best = (0,)
for _ in range(3000):
    U = np.eye(3) + 0.6 * rng.standard_normal((3, 3))
    if abs(np.linalg.det(U)) < 0.2: continue
    a, b = rng.uniform(0, np.pi, 2)
    P = R(a, 0, 1) @ U @ R(b, 0, 2) @ np.linalg.inv(U)   # a turn h->v, then a turn h->v2 in a sheared measure
    m = max(abs(np.linalg.eigvals(P)))
    if m > best[0]: best = (m, a, b, U)
m, a, b, U = best
P = R(a, 0, 1) @ U @ R(b, 0, 2) @ np.linalg.inv(U)
print("each factor returns: R(2pi) = I and U R(2pi) U^-1 = I")
print("largest |eigenvalue| of the composed step: %.4f" % m)
print("norm of the step repeated 10 times: %.3e" % np.linalg.norm(np.linalg.matrix_power(P, 10)))
# with a shared inner product (U = I) the composition stays a rotation
Q = R(a, 0, 1) @ R(b, 0, 2)
print("shared inner product: |eigenvalues| =", np.round(abs(np.linalg.eigvals(Q)), 12))
