"""CRC post hoc (after run 1, not a prediction): the reading of matter on the reader's side of the plane is its mirror."""
import mpmath as mp, importlib.util, sys
mp.mp.dps = 20
def pull(masses, p):
    g = [mp.mpf(0)]*3
    for m, q in masses:
        d = [q[i]-p[i] for i in range(3)]; r3 = (sum(x*x for x in d))**mp.mpf(1.5)
        g = [g[i] + m*d[i]/r3 for i in range(3)]
    return g
def plane_read(f, X, Y, a):
    g = lambda u, p: f(X + a*mp.tan(u)*mp.cos(p), Y + a*mp.tan(u)*mp.sin(p)) * mp.sin(u)
    return mp.quad(g, [0, mp.pi/4, mp.pi/2], [0, mp.pi/2, mp.pi, 3*mp.pi/2, 2*mp.pi]) / (2*mp.pi)
X, Y, h, a = mp.mpf('0.2'), mp.mpf('0.3'), mp.mpf('0.7'), mp.mpf('1.5')
out = []
for name, s in (("between", h + a/2), ("above", h + 2*a)):
    m = [(1, (mp.mpf('0.9'), mp.mpf('0.1'), s))]
    R = [plane_read(lambda x, y, i=i: pull(m, (x, y, h))[i], X, Y, a) for i in range(3)]
    img = [(1, (mp.mpf('0.9'), mp.mpf('0.1'), 2*h - s))]          # mirrored in the plane
    gi = pull(img, (X, Y, h + a)); pred = [gi[0], gi[1], -gi[2]]
    e = max(abs(R[i] - pred[i]) for i in range(3)) / mp.sqrt(sum(c*c for c in pred))
    line = f"mass {name} (z = {mp.nstr(s,3)}): reading {[mp.nstr(c,10) for c in R]}, mirror's pull, vertical flipped {[mp.nstr(c,10) for c in pred]}, rel err {mp.nstr(e,3)}"
    print(line); out.append(line)
open('runs/crc/crc-posthoc.txt', 'w').write("\n".join(out) + "\n")
