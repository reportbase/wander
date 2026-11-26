"""CRC run 1: a Cauchy reading a Cauchy (plans/crc-plan.md). mpmath quadrature, G = 1."""
import mpmath as mp
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s)

def rel(x, y):
    return abs(x - y) / max(abs(y), mp.mpf(10)**-60)

# ---------- C1: one Cauchy from two ----------
mp.mp.dps = 35
PL = lambda a, x: a / (mp.pi * (a*a + x*x))                 # line kernel
PP = lambda a, r: a / (2*mp.pi * (a*a + r*r)**mp.mpf(1.5))   # plane kernel
C1 = True
for a, h in ((1, 1), (mp.mpf('0.3'), mp.mpf('2.5')), (4, mp.mpf('0.25'))):
    a, h = mp.mpf(a), mp.mpf(h)
    for x in (0, mp.mpf('0.7'), 3):
        x = mp.mpf(x)
        lhs = mp.quad(lambda t: PL(a, x - t) * PL(h, t), [-mp.inf, 0, x, mp.inf])
        e = rel(lhs, PL(a + h, x)); C1 &= e < mp.mpf(10)**-20
        say(f"C1 line a={mp.nstr(a,3)} h={mp.nstr(h,3)} x={mp.nstr(x,3)}: rel err {mp.nstr(e,3)}")
mp.mp.dps = 30
def plane_read(f, X, Y, a):
    # (1/2pi) int int f(X + a tan u cos p, Y + a tan u sin p) sin u du dp : the heat P_a dA in u = atan(rho/a)
    g = lambda u, p: f(X + a*mp.tan(u)*mp.cos(p), Y + a*mp.tan(u)*mp.sin(p)) * mp.sin(u)
    return mp.quad(g, [0, mp.pi/4, mp.pi/2], [0, mp.pi/2, mp.pi, 3*mp.pi/2, 2*mp.pi]) / (2*mp.pi)
for a, h in ((1, 1), (mp.mpf('0.3'), mp.mpf('2.5'))):
    a, h = mp.mpf(a), mp.mpf(h)
    for r0 in (0, mp.mpf('1.3')):
        r0 = mp.mpf(r0)
        lhs = plane_read(lambda x, y: PP(h, mp.sqrt(x*x + y*y)), r0, 0, a)
        e = rel(lhs, PP(a + h, r0)); C1 &= e < mp.mpf(10)**-20
        say(f"C1 plane a={mp.nstr(a,3)} h={mp.nstr(h,3)} r0={mp.nstr(r0,3)}: rel err {mp.nstr(e,3)}")
say("C1", "not killed" if C1 else "KILLED")

# ---------- C2: the reader gets the pull at its own place (3D) ----------
mp.mp.dps = 25
def pull(masses, p):
    gx = gy = gz = mp.mpf(0)
    for m, q in masses:
        dx, dy, dz = q[0]-p[0], q[1]-p[1], q[2]-p[2]
        r3 = (dx*dx + dy*dy + dz*dz)**mp.mpf(1.5)
        gx += m*dx/r3; gy += m*dy/r3; gz += m*dz/r3
    return gx, gy, gz
def reading(masses, X, Y, h, a):
    return tuple(plane_read(lambda x, y, i=i: pull(masses, (x, y, h))[i], X, Y, a) for i in range(3))
def compare(masses, X, Y, h, a):
    R = reading(masses, X, Y, h, a); g = pull(masses, (X, Y, h + a))
    gn = mp.sqrt(sum(c*c for c in g))
    return max(abs(R[i] - g[i]) for i in range(3)) / gn, R, g
cases = [
    ("on axis", [(1, (0, 0, -1))], 0, 0, mp.mpf(1), mp.mpf(1)),
    ("off axis", [(1, (mp.mpf('0.8'), mp.mpf('-0.5'), mp.mpf('-0.6')))], mp.mpf('0.2'), mp.mpf('0.3'), mp.mpf('0.7'), mp.mpf('1.5')),
    ("a pair", [(1, (mp.mpf('-1'), 0, mp.mpf('-0.4'))), (mp.mpf('2.5'), (mp.mpf('1.2'), mp.mpf('0.9'), mp.mpf('-2')))], mp.mpf('0.4'), mp.mpf('-0.2'), mp.mpf('1.1'), mp.mpf('0.6')),
]
C2 = True
for name, ms, X, Y, h, a in cases:
    e, R, g = compare(ms, X, Y, h, a); C2 &= e < mp.mpf(10)**-12
    say(f"C2 {name}: reading {[mp.nstr(c,12) for c in R]}, pull at the eye {[mp.nstr(c,12) for c in g]}, rel err {mp.nstr(e,3)}")
say("C2", "not killed" if C2 else "KILLED")

# ---------- C3: standpoints add (2D gravity on the line) ----------
mp.mp.dps = 35
def pull2(m2, c, x, y):
    dx, dy = m2 - x, -c - y; r2 = dx*dx + dy*dy
    return 2*dx/r2, 2*dy/r2
C3 = True
for X, a, h, m2, c in ((0, 1, 1, mp.mpf('0.5'), 1), (mp.mpf('1.7'), mp.mpf('0.4'), mp.mpf('2'), mp.mpf('-0.3'), mp.mpf('0.2')),
                       (mp.mpf('-2'), mp.mpf('3'), mp.mpf('0.5'), mp.mpf('1'), mp.mpf('1.5')), (mp.mpf('0.1'), mp.mpf('0.05'), mp.mpf('0.1'), mp.mpf('4'), mp.mpf('0.3'))):
    X, a, h = mp.mpf(X), mp.mpf(a), mp.mpf(h)
    Rx = mp.quad(lambda x: PL(a, x - X) * pull2(m2, c, x, h)[0], [-mp.inf, X, m2, mp.inf])
    Ry = mp.quad(lambda x: PL(a, x - X) * pull2(m2, c, x, h)[1], [-mp.inf, X, m2, mp.inf])
    gx, gy = pull2(m2, c, X, h + a)
    H = a + h + c; cauchy = -2*mp.pi*PL(H, X - m2)             # g_y = -2 pi P_(a+h+c)(X - m2)
    e = max(rel(Rx, gx), rel(Ry, gy), rel(gy, cauchy)); C3 &= e < mp.mpf(10)**-20
    say(f"C3 X={mp.nstr(X,3)} a={mp.nstr(a,3)} h={mp.nstr(h,3)} m2={mp.nstr(m2,3)} c={mp.nstr(c,3)}: point {mp.nstr(X-m2,4)} + {mp.nstr(H,4)}i, rel err {mp.nstr(e,3)}")
say("C3", "not killed" if C3 else "KILLED")

# ---------- C4: where it stops ----------
mp.mp.dps = 20
below = [(1, (mp.mpf('0.8'), mp.mpf('-0.5'), mp.mpf('-0.6')))]
X, Y, h, a = mp.mpf('0.2'), mp.mpf('0.3'), mp.mpf('0.7'), mp.mpf('1.5')
# (a) heat-weighted median of |g_z| on the plane, by a midpoint grid in (u, phi) (weights sin u du dphi / 2pi)
import math
N = 900
vals = []
for i in range(N):
    u = (i + 0.5) * (math.pi/2) / N
    for j in range(N):
        p = (j + 0.5) * 2*math.pi / N
        x = float(X) + float(a)*math.tan(u)*math.cos(p); y = float(Y) + float(a)*math.tan(u)*math.sin(p)
        gz = float(pull(below, (x, y, h))[2])
        vals.append((abs(gz), math.sin(u)))
vals.sort(); tot = sum(w for _, w in vals); acc = 0
for v, w in vals:
    acc += w
    if acc >= tot/2: med = v; break
gz_eye = abs(pull(below, (X, Y, h + a))[2])
mean_grid = sum(v*w for v, w in vals) / tot
ea = abs(med - float(gz_eye)) / float(gz_eye)
say(f"C4a: heat-weighted median |g_z| {med:.6g}, mean on the grid {mean_grid:.6g}, |g_z| at the eye {mp.nstr(gz_eye,8)}: median off by {ea*100:.2f}%")
mid = [(1, (mp.mpf('0.9'), mp.mpf('0.1'), h + a/2))]
e4b, Rb, gb = compare(below + mid, X, Y, h, a)
say(f"C4b: a mass between, reading {[mp.nstr(c,8) for c in Rb]}, pull at the eye {[mp.nstr(c,8) for c in gb]}, off by {mp.nstr(e4b*100,4)}%")
top = [(1, (mp.mpf('0.9'), mp.mpf('0.1'), h + 2*a))]
e4c, Rc, gc = compare(below + top, X, Y, h, a)
say(f"C4c: a mass above the reader, reading {[mp.nstr(c,8) for c in Rc]}, pull at the eye {[mp.nstr(c,8) for c in gc]}, off by {mp.nstr(e4c*100,4)}%")
C4 = ea > 0.01 and e4b > mp.mpf('0.01') and e4c > mp.mpf('0.01')
say("C4", "not killed" if C4 else "KILLED")

# ---------- C5: scale ----------
mp.mp.dps = 25
C5 = True
R0 = reading(below, X, Y, h, a); g0 = pull(below, (X, Y, h + a))
for k in (mp.mpf(3), mp.mpf(1)/7):
    msk = [(m, tuple(k*c for c in q)) for m, q in below]
    Rk = reading(msk, k*X, k*Y, k*h, k*a); gk = pull(msk, (k*X, k*Y, k*(h + a)))
    e1 = max(abs(Rk[i]/gk[i] - 1) for i in range(3)); e2 = max(abs(gk[i]*k*k/g0[i] - 1) for i in range(3))
    C5 &= e1 < mp.mpf(10)**-12 and e2 < mp.mpf(10)**-12
    say(f"C5 k={mp.nstr(k,4)}: reading/pull - 1 {mp.nstr(e1,3)}; pull x k^2 / pull - 1 {mp.nstr(e2,3)}")
say("C5", "not killed" if C5 else "KILLED")
open('runs/crc/crc-run1.txt', 'w').write("\n".join(out) + "\n")
