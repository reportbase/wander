"""WDG: the wedge, made with the Cauchy. See plans/wdg-plan.md.

Unit relations h, v, v2 in [0, 1]; readings a = v/h, b = v2/h. With V = V2 = H the attitudes are the unit sphere and one
facing of each is the octant (the wedge); sweeping it evenly is uniform by area. P1-P4 and P6 in mpmath at 30 digits
(quadrature and derivatives, never the closed forms being tested); P5 identities in floats (numpy).
Needs mpmath (PyPI, BSD) and numpy.
"""
import mpmath as mp
import numpy as np
mp.mp.dps = 30
def verdict(ok): return "not killed" if ok else "KILLED"
rel = lambda x, y: abs(x / y - 1)
f = lambda a, b: 2 / (mp.pi * (1 + a * a + b * b) ** mp.mpf(1.5))      # P1's density, used once P1 stands
inf = mp.inf
grid = [mp.mpf(2) ** j for j in range(-8, 9, 2)]

# ---------------------------------------------------------------- P1: the octant's area element in the readings
def F(a, b):
    n = mp.sqrt(1 + a * a + b * b); return (1 / n, a / n, b / n)
def area_element(a, b):
    Fa = [mp.diff(lambda s: F(s, b)[i], a) for i in range(3)]
    Fb = [mp.diff(lambda s: F(a, s)[i], b) for i in range(3)]
    cr = (Fa[1] * Fb[2] - Fa[2] * Fb[1], Fa[2] * Fb[0] - Fa[0] * Fb[2], Fa[0] * Fb[1] - Fa[1] * Fb[0])
    return mp.sqrt(sum(c * c for c in cr))
w1 = max(rel(area_element(a, b), (1 + a * a + b * b) ** mp.mpf(-1.5)) for a in grid for b in grid)
tot = mp.quad(lambda a, b: (1 + a * a + b * b) ** mp.mpf(-1.5), [0, 1, inf], [0, 1, inf])
ok1 = w1 <= mp.mpf('1e-20') and abs(tot - mp.pi / 2) <= mp.mpf('1e-15')
print(f"P1 area element vs (1+a^2+b^2)^-1.5 on 2^-8..2^8: worst {mp.nstr(w1, 3)}; total {mp.nstr(tot, 20)}"
      f" (pi/2 = {mp.nstr(mp.pi / 2, 20)}) ->", verdict(ok1))

# ---------------------------------------------------------------- P2: every pair keeps its corner
w2a = max(rel(mp.quad(lambda b: f(a, b), [0, 1, inf]), 2 / (mp.pi * (1 + a * a))) for a in grid)
def p_ratio(r):   # P(a/b <= r) = P(a <= r b)
    return mp.quad(lambda b: mp.quad(lambda a: f(a, b), [0, r * b]), [0, 1, inf])
w2b = max(abs(p_ratio(mp.mpf(r)) - 2 / mp.pi * mp.atan(r)) for r in ('0.25', '0.5', '1', '2', '4'))
med_a = mp.quad(lambda a: mp.quad(lambda b: f(a, b), [0, 1, inf]), [0, 1])
ok2 = w2a <= mp.mpf('1e-15') and w2b <= mp.mpf('1e-15')
print(f"P2 marginal of v/h vs 2/(pi(1+a^2)): worst {mp.nstr(w2a, 3)}; P(v/v2 <= r) vs (2/pi)atan r: worst {mp.nstr(w2b, 3)};"
      f" P(v/h <= 1) = {mp.nstr(med_a, 20)} ->", verdict(ok2))

# ---------------------------------------------------------------- P3: six chambers, the near field a third
ch = {
  'h > v > v2': mp.quad(lambda a: mp.quad(lambda b: f(a, b), [0, a]), [0, 1]),
  'h > v2 > v': mp.quad(lambda b: mp.quad(lambda a: f(a, b), [0, b]), [0, 1]),
  'v > h > v2': mp.quad(lambda a: mp.quad(lambda b: f(a, b), [0, 1]), [1, inf]),
  'v2 > h > v': mp.quad(lambda b: mp.quad(lambda a: f(a, b), [0, 1]), [1, inf]),
  'v > v2 > h': mp.quad(lambda a: mp.quad(lambda b: f(a, b), [1, a]), [1, 2, inf]),
  'v2 > v > h': mp.quad(lambda b: mp.quad(lambda a: f(a, b), [1, b]), [1, 2, inf]),
}
near = mp.quad(lambda a, b: f(a, b), [0, 1], [0, 1])
far = mp.quad(lambda a, b: f(a, b), [1, 2, inf], [1, 2, inf])
one = 1 - near - far
w3 = max([abs(x - mp.mpf(1) / 6) for x in ch.values()] + [abs(near - mp.mpf(1) / 3), abs(far - mp.mpf(1) / 3), abs(one - mp.mpf(1) / 3)])
ok3 = w3 <= mp.mpf('1e-15')
print(f"P3 chambers {', '.join(mp.nstr(x, 12) for x in ch.values())}; near in both {mp.nstr(near, 20)}, past in one"
      f" {mp.nstr(one, 20)}, past in both {mp.nstr(far, 20)}; worst {mp.nstr(w3, 3)} ->", verdict(ok3))

# ---------------------------------------------------------------- P4: the wedge requires V = V2 = H
def drawn(c1, c2):
    """even by direction in the drawing (1, c1 a, c2 b): the law of (a, b) is c1 c2 f(c1 a, c2 b)"""
    g = lambda a, b: c1 * c2 * f(c1 * a, c2 * b)
    cdf_a = lambda m: mp.quad(lambda a: mp.quad(lambda b: g(a, b), [0, 1, inf]), [0, m])
    cdf_b = lambda m: mp.quad(lambda b: mp.quad(lambda a: g(a, b), [0, 1, inf]), [0, m])
    cdf_r = lambda m: mp.quad(lambda b: mp.quad(lambda a: g(a, b), [0, m * b]), [0, 1, inf])
    med = lambda cdf, x0: mp.findroot(lambda m: cdf(m) - mp.mpf(1) / 2, x0)
    nearsh = mp.quad(lambda a, b: g(a, b), [0, 1], [0, 1])
    return med(cdf_a, 1 / mp.mpf(c1)), med(cdf_b, 1 / mp.mpf(c2)), med(cdf_r, mp.mpf(c2) / c1), nearsh
mp.mp.dps = 20
w4, flags, rows4 = mp.mpf(0), [], []
for c1, c2 in ((1, 1), (2, 1), (1, 2), (2, 2), (mp.mpf('0.5'), 3)):
    ma, mb, mr, ns = drawn(mp.mpf(c1), mp.mpf(c2))
    w4 = max(w4, rel(ma, 1 / mp.mpf(c1)), rel(mb, 1 / mp.mpf(c2)), rel(mr, mp.mpf(c2) / c1))
    if (c1, c2) != (1, 1): flags.append(abs(ns - mp.mpf(1) / 3) <= mp.mpf('1e-6'))
    rows4.append((c1, c2, ma, mb, mr, ns))
ok4 = w4 <= mp.mpf('1e-12') and not any(flags)
mp.mp.dps = 30
print(f"P4 medians vs 1/c1, 1/c2, c2/c1: worst {mp.nstr(w4, 3)}; near-in-both 1/3 only at (1, 1) ->", verdict(ok4))
for c1, c2, ma, mb, mr, ns in rows4:
    print(f"   V = {mp.nstr(c1, 2)}H, V2 = {mp.nstr(c2, 2)}H: medians v/h {mp.nstr(ma, 8)}, v2/h {mp.nstr(mb, 8)}, v/v2 {mp.nstr(mr, 8)};"
          f" near in both {mp.nstr(ns, 10)}")

# ---------------------------------------------------------------- P5: a rotatable sphere in a cube of known extent
rng = np.random.default_rng(20)
def turn():
    q, r = np.linalg.qr(rng.normal(size=(3, 3))); return q * np.sign(np.diag(r))
def to_address(x, e, R):
    t = np.max(np.abs(x), axis=1) / e
    w = x / np.linalg.norm(x, axis=1, keepdims=True)
    return w @ R, t                                                   # u = R^T w, row-wise
def to_point(u, t, e, R):
    d = u @ R.T                                                       # R u
    return t[:, None] * e * d / np.max(np.abs(d), axis=1, keepdims=True)
worst_rt = worst_addr = 0.0; faces_ok = True
for trial in range(5):
    R = turn()
    x1 = rng.uniform(-1, 1, size=(100000, 3))
    surf = rng.uniform(-1, 1, size=(20000, 3)); k = rng.integers(0, 3, 20000); surf[np.arange(20000), k] = np.sign(rng.uniform(-1, 1, 20000))
    x1 = np.vstack([x1, surf])                                        # inside and on the surface
    addr = {}
    for e in (1e-6, 1.0, 1e6):
        x = x1 * e; u, t = to_address(x, e, R); back = to_point(u, t, e, R)
        worst_rt = max(worst_rt, np.max(np.linalg.norm(back - x, axis=1) / np.linalg.norm(x, axis=1)))
        addr[e] = (u, t)
        d = u @ R.T
        faces_ok &= bool(np.all(np.argmax(np.abs(d), axis=1) == np.argmax(np.abs(x), axis=1)))
    for e in (1e-6, 1e6):
        worst_addr = max(worst_addr, np.max(np.abs(addr[e][0] - addr[1.0][0])), np.max(np.abs(addr[e][1] / addr[1.0][1] - 1)))
ok5 = worst_rt <= 1e-12 and worst_addr <= 1e-12 and faces_ok
print(f"P5 round trip x -> (u, t) -> x: worst {worst_rt:.2e}; address across e = 1e-6, 1, 1e6: worst {worst_addr:.2e};"
      f" the face reached is the largest component's: {faces_ok} ->", verdict(ok5))

# ---------------------------------------------------------------- P6: the even sphere on a face of the cube
dens = lambda a, b: 1 / (4 * mp.pi * (1 + a * a + b * b) ** mp.mpf(1.5))   # share of the whole sphere per unit face area
face = mp.quad(dens, [-1, 0, 1], [-1, 0, 1])
mid = mp.quad(dens, [-0.5, 0, 0.5], [-0.5, 0, 0.5]) / face
pred = 4 * mp.atan(1 / (4 * mp.sqrt(mp.mpf(1.5)))) / (2 * mp.pi / 3)
ok6 = abs(face - mp.mpf(1) / 6) <= mp.mpf('1e-15') and abs(mid - pred) <= mp.mpf('1e-15')
print(f"P6 a face holds {mp.nstr(face, 20)} of the sphere; its middle quarter by area takes {mp.nstr(mid, 15)} of the face"
      f" (predicted {mp.nstr(pred, 15)}); centre over corner density {mp.nstr(3 ** mp.mpf(1.5), 8)} ->", verdict(ok6))
