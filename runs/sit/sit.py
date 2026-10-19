"""SIT: the situations with V2, organized by the relations. See plans/sit-plan.md (P1-P3).

P1: where rays from the parties at the unit points meet with every pair at a right angle, found by Gauss-Newton from
random starts (floats to converge, mpmath at 50 digits to polish), never from the predicted points.
P2: a hemisphere's two readings by numerical integration over it, not from the Gamma form.
Run: python3 runs/sit/sit.py   (under a minute; needs mpmath and numpy)
"""
import itertools, random
import numpy as np
import mpmath as mp
mp.mp.dps = 50
M = mp.mpf
def verdict(ok): return "not killed" if ok else "KILLED"
results = {}

# ---------------------------------------------------------------- P1: three rays meet square only at the reader
def residuals(P, k):
    """(P - e_i).(P - e_j) for every pair of the k unit points: |P|^2 - P_i - P_j."""
    s = sum(x * x for x in P)
    return [s - P[i] - P[j] for i, j in itertools.combinations(range(k), 2)]
def jac(P, k):
    return [[2 * P[m] - (1 if m == i else 0) - (1 if m == j else 0) for m in range(k)] for i, j in itertools.combinations(range(k), 2)]
def solve_from(start, k):
    P = np.array(start, dtype=float)
    for _ in range(200):                                          # Gauss-Newton in floats
        r = np.array(residuals(P, k)); J = np.array(jac(P, k))
        step, *_ = np.linalg.lstsq(J, -r, rcond=None)
        P = P + step
        if np.linalg.norm(step) < 1e-14: break
    Q = [M(float(x)) for x in P]                                  # polish at 50 digits
    for _ in range(12):
        r = mp.matrix(residuals(Q, k)); J = mp.matrix(jac(Q, k))
        step = mp.lu_solve(J.T * J, -(J.T * r))
        Q = [Q[m] + step[m] for m in range(k)]
    return Q, max(abs(x) for x in residuals(Q, k))
random.seed(1)
ok1, notes1 = True, []
for k in (3, 4, 5):
    preds = [[M(0)] * k, [M(2) / (k)] * k]                        # t = 0 and t = 2/(n + 1), n + 1 = k parties
    pred_res = max(max(abs(x) for x in residuals(p, k)) for p in preds)
    found, far = 0, M(0)
    for _ in range(2000):
        Q, res = solve_from([random.uniform(-2, 3) for _ in range(k)], k)
        if res < M('1e-40'):
            found += 1
            d = min(max(abs(Q[m] - p[m]) for m in range(k)) for p in preds)
            far = max(far, d)
    ok1 = ok1 and pred_res < M('1e-45') and far < M('1e-30')
    notes1.append(f"{k} parties: {found} of 2000 starts converged, all within {mp.nstr(far, 2)} of t = 0 or 2/{k}")
# two parties: the circle x² + y² = x + y through home
w_circle = M(0)
for i in range(500):
    t = 2 * mp.pi * i / 500
    P = [M(1) / 2 + mp.cos(t) / mp.sqrt(2), M(1) / 2 + mp.sin(t) / mp.sqrt(2)]
    w_circle = max(w_circle, abs(residuals(P, 2)[0]))
ok1 = ok1 and w_circle < M('1e-45')
notes1.append(f"two parties: the circle on the chord, through home, to {mp.nstr(w_circle, 2)}")
results['P1'] = (ok1, "; ".join(notes1))

# ---------------------------------------------------------------- P2: the hemisphere's two readings
ok2, notes2 = True, []
for n in (2, 3, 4):
    # polar angle theta from the pole; the sphere's element ~ sin^(n-2) theta (the common |S^(n-2)| cancels)
    area = mp.quad(lambda th: mp.sin(th) ** (n - 2), [0, mp.pi / 2])
    shadow = mp.quad(lambda r: r ** (n - 2), [0, 1])               # the base (n-1)-ball, by its own radius
    height = mp.quad(lambda th: mp.cos(th) * mp.sin(th) ** (n - 2), [0, mp.pi / 2])   # the height summed over the area
    outer, inner = area / shadow, height / area
    closed = mp.sqrt(mp.pi) * mp.gamma(M(n + 1) / 2) / mp.gamma(M(n) / 2)
    w = max(abs(outer - closed), abs(inner - 1 / closed), abs(outer * inner - 1))
    ok2 = ok2 and w < M('1e-40')
    notes2.append(f"n = {n}: at once {mp.nstr(outer, 10)}, one at a time {mp.nstr(inner, 10)} (closed form to {mp.nstr(w, 2)})")
results['P2'] = (ok2, "; ".join(notes2))

# ---------------------------------------------------------------- P3: the readings do not multiply sweep by sweep
o3 = mp.sqrt(mp.pi) * mp.gamma(2) / mp.gamma(M(3) / 2)
d_out, d_in = abs(o3 - (mp.pi / 2) ** 2), abs(1 / o3 - (2 / mp.pi) ** 2)
results['P3'] = (d_out >= M('0.1') and d_in >= M('0.1'),                 # killed if either holds to within 0.1
                 f"2 against (π/2)² = {mp.nstr((mp.pi / 2) ** 2, 6)}, off {mp.nstr(d_out, 4)}; ½ against (2/π)² = {mp.nstr((2 / mp.pi) ** 2, 6)}, off {mp.nstr(d_in, 4)}")

for k_, (ok, msg) in results.items():
    print(f"{k_}: {verdict(ok)}. {msg}")
