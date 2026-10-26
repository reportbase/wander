"""GRS run 1, post hoc: closed forms suggested by run 1's numbers (not predicted). Ordered integrals, smooth integrands."""
import mpmath as mp
mp.mp.dps = 50
P2, Q = mp.pi / 2, mp.pi / 4
# ordered region θ1 < θ2, where cos²θ1 − cos²θ2 > 0
f4 = lambda u, v: mp.cos(u)**2 - mp.cos(v)**2
f5 = lambda u, v: (mp.cos(u)**2 - mp.cos(v)**2) * mp.sin(u) * mp.sin(v)
def I(f, a, b, lo, hi):
    return mp.quad(lambda u: mp.quad(lambda v: f(u, v), [lo(u), hi(u)]) if hi(u) > lo(u) else 0, [a, b])
Z4 = I(f4, 0, P2, lambda u: u, lambda u: P2)
near = I(f4, 0, Q, lambda u: u, lambda u: Q) / Z4
print("Gr(2,4) normaliser (ordered)  ", mp.nstr(Z4, 30), " π/8 =", mp.nstr(mp.pi/8, 30))
print("near field                    ", mp.nstr(near, 30), " (1 − π/4)/2 =", mp.nstr((1 - mp.pi/4)/2, 30))
Z5 = I(f5, 0, P2, lambda u: u, lambda u: P2)
p5 = I(f5, 0, Q, lambda u: u, lambda u: P2 - u) / Z5
print("Gr(2,5) P(t1 t2 ≤ 1)          ", mp.nstr(p5, 30))
