"""PXC: parallax from the corner. See plans/pxc-plan.md.

Amounts: a baseline B, a target's distance d from its middle, an angular step eps (radians). The pair is
(half-baseline, distance), its reading k = (B/2)/d; on the bisector tan(gamma/2) = k. P1-P3 in mpmath at 50 digits
(the derivative by complex step through gamma, never from the closed form); P4 a Monte Carlo triangulation in floats.
Needs mpmath (PyPI, BSD) and numpy.
"""
import mpmath as mp
import numpy as np
mp.mp.dps = 50
def verdict(ok): return "not killed" if ok else "KILLED"
B = mp.mpf(2)                                                     # the half-baseline is 1, so k = 1/d

def dlnd_dgamma(gamma, h=mp.mpf('1e-40')):
    """d ln d / d gamma by complex step, from d(gamma) = (B/2)/tan(gamma/2) alone"""
    f = lambda g: mp.log((B / 2) / mp.tan(g / 2))
    return mp.im(f(mp.mpc(gamma, h))) / h

# ---------------------------------------------------------------- P1, P2: the bell, and the flip
worst1 = worst_s = worst2 = mp.mpf(0)
for j in range(-300, 301):
    k = mp.mpf(2) ** (mp.mpf(j) / 10)                             # 2^-30 .. 2^30, ten points a level
    g = 2 * mp.atan(k)
    rel = abs(dlnd_dgamma(g))
    worst1 = max(worst1, abs(rel / mp.cosh(mp.log(k)) - 1))
    worst_s = max(worst_s, abs(mp.sin(g) / mp.sech(mp.log(k)) - 1))
    gf = 2 * mp.atan(1 / k)
    worst2 = max(worst2, abs(abs(dlnd_dgamma(gf)) / rel - 1))
ok1 = worst1 <= mp.mpf('1e-12') and worst_s <= mp.mpf('1e-12')
ok2 = worst2 <= mp.mpf('1e-12')
print(f"P1 |d ln d/d gamma| against cosh(ln k): worst {mp.nstr(worst1, 3)}; sin gamma against sech(ln k): worst"
      f" {mp.nstr(worst_s, 3)} (k from 2^-30 to 2^30) ->", verdict(ok1))
print(f"P2 the relative error at k against 1/k: worst {mp.nstr(worst2, 3)} ->", verdict(ok2))
for k in (mp.mpf(1) / 64, mp.mpf(1) / 4, 1, 4, 64):
    g = 2 * mp.atan(k)
    print(f"   k = {mp.nstr(k, 4):>8}: gamma {mp.nstr(mp.degrees(g), 8):>12} deg, relative error per unit angle {mp.nstr(abs(dlnd_dgamma(g)), 8)}")

# ---------------------------------------------------------------- P3: the band
def far_edge(eps):
    """the far k at which eps*cosh(ln k) = 1, and the distance there"""
    x = mp.acosh(1 / eps)                                          # |ln k| at the edge
    k = mp.e ** (-x)
    return k, (B / 2) / k
e6 = mp.mpf('1e-6'); k6, d6 = far_edge(e6)
e3 = mp.mpf('1e-3'); x3 = mp.acosh(1 / e3); half3 = x3 / mp.log(2)
# the half-width found by bisection on the error itself, not from the formula
lo, hi = mp.mpf(0), mp.mpf(100)
for _ in range(200):
    mid = (lo + hi) / 2
    (lo, hi) = (mid, hi) if e3 * mp.cosh(mid * mp.log(2)) <= 1 else (lo, mid)
ok3 = abs(d6 * e6 / B - 1) <= mp.mpf('1e-6') and abs(lo - half3) <= mp.mpf('1e-9')
print(f"P3 far edge at eps = 1e-6: d*eps/B = {mp.nstr(d6 * e6 / B, 12)}; band at eps = 1e-3: {mp.nstr(lo, 12)} levels each"
      f" side (acosh(1/eps)/ln 2 = {mp.nstr(half3, 12)}; log2(2/eps) = {mp.nstr(mp.log(2 / e3, 2), 12)}) ->", verdict(ok3))

# ---------------------------------------------------------------- P4: triangulation with noisy directions
rng = np.random.default_rng(13)
eps, N, worst4, rows = 1e-6, 20000, 0.0, []
for j in range(-8, 9):
    k = 2.0 ** j; d = 1.0 / k                                      # half-baseline 1
    A, Bp = np.array([-1.0, 0.0]), np.array([1.0, 0.0]); X = np.array([0.0, d])
    ta = np.arctan2(X[1] - A[1], X[0] - A[0]) + rng.normal(0, eps / np.sqrt(2), N)
    tb = np.arctan2(X[1] - Bp[1], X[0] - Bp[0]) + rng.normal(0, eps / np.sqrt(2), N)
    # intersect the two rays: A + s(cos ta, sin ta) = Bp + t(cos tb, sin tb)
    ca, sa, cb, sb = np.cos(ta), np.sin(ta), np.cos(tb), np.sin(tb)
    det = ca * (-sb) - sa * (-cb)
    s = ((Bp[0] - A[0]) * (-sb) - (Bp[1] - A[1]) * (-cb)) / det
    px, py = A[0] + s * ca, A[1] + s * sa
    dist = np.hypot(px, py)
    rel = np.sqrt(np.mean((dist / d - 1) ** 2)) / (eps * np.cosh(np.log(k)))
    rows.append((j, rel)); worst4 = max(worst4, abs(rel - 1))
ok4 = worst4 <= 0.03
print(f"P4 rms relative distance error over eps*cosh(ln k), k = 2^-8..2^8: worst |ratio - 1| = {worst4:.4f} ->", verdict(ok4))
print("   " + ", ".join(f"2^{j}: {r:.3f}" for j, r in rows))
