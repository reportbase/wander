"""HOL run 1 (plans/hol-plan.md): the exact predictions H1-H4. Run from the repository's root: python3 runs/hol/hol.py
Parallel transport is integrated as an ODE (mpmath's Taylor-series odefun), never taken from the holonomy formula,
and compared with the area computed separately (signed spherical excess; hyperbolic angle defect)."""
import random, time
from multiprocessing import Pool
from mpmath import mp, mpf, matrix, odefun, sqrt, cos, sin, acos, atan2, pi, cosh, sinh, fabs, asin, tan, atan
mp.dps = 50
TOL = mpf(10) ** -20
TOL40 = mpf(10) ** -40
rnd = random.Random(20261109)
t0 = time.time()

def dot(a, b): return sum(x * y for x, y in zip(a, b))
def cross(a, b): return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def scale(a, s): return [x * s for x in a]
def add(a, b): return [x + y for x, y in zip(a, b)]
def norm(a): return sqrt(dot(a, a))
def unit(a): n = norm(a); return [x / n for x in a]
def wrap(x):
    x = (x + pi) % (2 * pi) - pi
    return x

# ---------- the sphere: transport along a curve gamma(t), t in [0, 1], radius R ----------
def transport(curve, dcurve, v0, R=1):
    # state: v (3); v' = -(v . gamma') gamma / R^2
    f = lambda t, v: [-(dot(v, dcurve(t))) * g / R**2 for g in curve(t)]
    sol = odefun(f, 0, v0)
    return sol(1)

def geodesic(a, b):
    # great circle from a to b on the sphere of a's radius, angle w
    R = norm(a); au, bu = unit(a), unit(b)
    w = acos(dot(au, bu)); n = unit(cross(au, bu)); p = cross(n, au)
    c = lambda t: scale(add(scale(au, cos(w*t)), scale(p, sin(w*t))), R)
    dc = lambda t: scale(add(scale(au, -w*sin(w*t)), scale(p, w*cos(w*t))), R)
    return c, dc

def turn_of(p0, v0, v1):
    n = unit(p0)
    return atan2(dot(cross(v0, v1), n), dot(v0, v1))

def tangent_at(p):
    a = [mpf(1), mpf(0), mpf(0)] if fabs(p[0]) < mpf('0.9')*norm(p) else [mpf(0), mpf(1), mpf(0)]
    return unit(cross(cross(unit(p), a), unit(p)))  # any unit tangent

def polygon_turn(pts, R=1):
    v0 = tangent_at(pts[0]); v = v0
    for i in range(len(pts)):
        c, dc = geodesic(pts[i], pts[(i + 1) % len(pts)])
        v = transport(c, dc, v, R)
    return turn_of(pts[0], v0, v)

def tri_area(a, b, c):  # signed solid angle, Van Oosterom & Strackee
    a, b, c = unit(a), unit(b), unit(c)
    return 2 * atan2(dot(a, cross(b, c)), 1 + dot(a, b) + dot(b, c) + dot(c, a))

def rand_pt():
    while True:
        p = [mpf(rnd.gauss(0, 1)) for _ in range(3)]
        if norm(p) > 0.1: return unit(p)

out = []
say = lambda s: (print(s, flush=True), out.append(s))

# H1a latitude circles: closed curve, counterclockwise about +z
worst = 0
for k in range(12):
    lat = -pi/2 + pi*(k + mpf(1)/2)/12
    c = lambda t, lat=lat: [cos(lat)*cos(2*pi*t), cos(lat)*sin(2*pi*t), sin(lat)]
    dc = lambda t, lat=lat: [-2*pi*cos(lat)*sin(2*pi*t), 2*pi*cos(lat)*cos(2*pi*t), mpf(0)]
    p0 = c(0); v0 = [mpf(0), mpf(0), mpf(1)]; v0 = unit(add(v0, scale(p0, -dot(v0, p0))))
    v1 = transport(c, dc, v0)
    area = 2*pi*(1 - sin(lat))          # the cap the loop goes round counterclockwise
    d = fabs(wrap(turn_of(p0, v0, v1) - area)); worst = max(worst, d)
say(f'H1a latitude circles (12): worst |turn - cap area| = {mp.nstr(worst, 3)}')
w1a = worst

# H1b random geodesic triangles and quadrilaterals (the points drawn first, in order, then transported in parallel)
tris = [(rand_pt(), rand_pt(), rand_pt()) for i in range(100)]
quads = [(rand_pt(), rand_pt(), rand_pt(), rand_pt()) for i in range(100)]
with Pool(4) as pool:
    tt = pool.map(polygon_turn, [list(t) for t in tris])
    tq = pool.map(polygon_turn, [list(q) for q in quads])
worst = 0; n = 0
for (a, b, c), t in zip(tris, tt):
    worst = max(worst, fabs(wrap(t - tri_area(a, b, c)))); n += 1
for (a, b, c, e), t in zip(quads, tq):
    worst = max(worst, fabs(wrap(t - tri_area(a, b, c) - tri_area(a, c, e)))); n += 1
say(f'H1b random geodesic triangles and quadrilaterals ({n}): worst |turn - signed area| = {mp.nstr(worst, 3)}')
w1b = worst
say(f'H1: {"KILLED" if max(w1a, w1b) > TOL else "not killed"} (tolerance 1e-20)   [{time.time()-t0:.0f} s]')

# H2 the plane: the same loops laid flat by the gnomonic projection about the first vertex; transport v' = 0
# (the flat metric's Christoffels vanish), integrated the same way.
worst = 0
for i in range(50):
    a, b, c = rand_pt(), rand_pt(), rand_pt()
    v0 = [mpf(1), mpf(0)]
    v = v0
    for _ in range(3):
        sol = odefun(lambda t, v: [mpf(0), mpf(0)], 0, v); v = sol(1)
    worst = max(worst, fabs(atan2(v0[0]*v[1]-v0[1]*v[0], dot(v0, v))))
say(f'H2 the plane (50 loops): worst turn = {mp.nstr(worst, 3)} -> {"KILLED" if worst > mpf(10)**-40 else "not killed"}'
    ' (trivially: the flat transport equation is v\' = 0)')

# ---------- velocity space: Lorentz boosts round a loop of velocities ----------
ETA = [-1, 1, 1, 1]
def mink(a, b): return sum(e*x*y for e, x, y in zip(ETA, a, b))
def four(rap):   # rapidity vector -> 4-velocity
    r = norm(rap)
    if r == 0: return [mpf(1), mpf(0), mpf(0), mpf(0)]
    u = scale(rap, 1/r); return [cosh(r)] + scale(u, sinh(r))
def lab_boost(x):  # pure boost taking rest (1,0,0,0) to the 4-velocity x
    g = x[0]; p = x[1:]; M = matrix(4, 4)
    M[0, 0] = g
    for i in range(3):
        M[0, i+1] = p[i]; M[i+1, 0] = p[i]
        for j in range(3):
            M[i+1, j+1] = (1 if i == j else 0) + p[i]*p[j]/(1 + g)
    return M
def inv_boost(x): return lab_boost([x[0]] + [-y for y in x[1:]])
def boost_ab(a, b):  # the pure boost in a's rest frame taking a to b
    Ba, Bai = lab_boost(a), inv_boost(a)
    rel = Bai * matrix(b)
    return Ba * lab_boost([rel[i] for i in range(4)]) * Bai
def hyp_angle(x, y, z):  # interior angle at x of the geodesic triangle x y z on the hyperboloid
    ty = [yy + mink(x, y)*xx for xx, yy in zip(x, y)]
    tz = [zz + mink(x, z)*xx for xx, zz in zip(x, z)]
    return acos(mink(ty, tz)/sqrt(mink(ty, ty)*mink(tz, tz)))

worst = 0; worst_sign = 0
for i in range(200):
    raps = []
    for _ in range(3):
        d = rand_pt(); r = mpf(rnd.uniform(0.01, 3)); raps.append(scale(d, r))
    x, y, z = (four(r) for r in raps)
    L = boost_ab(z, x) * boost_ab(y, z) * boost_ab(x, y)
    R = inv_boost(x) * L * lab_boost(x)         # a rotation in x's rest frame
    Rs = [[R[i+1, j+1] for j in range(3)] for i in range(3)]
    tr = Rs[0][0] + Rs[1][1] + Rs[2][2]
    ang = acos(max(min((tr - 1)/2, mpf(1)), mpf(-1)))
    axis = [Rs[2][1]-Rs[1][2], Rs[0][2]-Rs[2][0], Rs[1][0]-Rs[0][1]]
    # orientation of the triangle seen from x's rest frame
    yr = inv_boost(x) * matrix(y); zr = inv_boost(x) * matrix(z)
    nrm = cross([yr[1], yr[2], yr[3]], [zr[1], zr[2], zr[3]])
    signed = ang if dot(axis, nrm) > 0 else -ang
    defect = pi - hyp_angle(x, y, z) - hyp_angle(y, z, x) - hyp_angle(z, x, y)
    worst = max(worst, fabs(signed + defect))
    worst_sign = max(worst_sign, fabs(fabs(signed) - defect))
say(f'H3 velocity space (200 triangles, rapidities 0.01-3): worst |Wigner turn + hyperbolic area| = {mp.nstr(worst, 3)};'
    f' magnitudes alone {mp.nstr(worst_sign, 3)} -> {"KILLED" if worst > TOL else "not killed"}')

# H4 scale and clock
def h4one(pts):
    a, b, c = pts
    t1 = polygon_turn([a, b, c]); w = 0
    for Rr in (mpf('1e-3'), mpf(7), mpf('1e6')):
        w = max(w, fabs(wrap(t1 - polygon_turn([scale(a, Rr), scale(b, Rr), scale(c, Rr)], Rr))))
    return w
h4pts = [(rand_pt(), rand_pt(), rand_pt()) for i in range(20)]
with Pool(4) as pool:
    worst = max(pool.map(h4one, h4pts))
w4a = worst
# a two-leg loop on the sphere, and out and back in velocity space
a, b = rand_pt(), rand_pt()
c1, d1 = geodesic(a, b); c2, d2 = geodesic(b, a)
v0 = tangent_at(a); v = transport(c2, d2, transport(c1, d1, v0))
w4b = fabs(turn_of(a, v0, v))
x, y = four(scale(rand_pt(), mpf(2))), four(scale(rand_pt(), mpf('0.7')))
L = boost_ab(y, x) * boost_ab(x, y)
w4c = max(fabs(L[i, j] - (1 if i == j else 0)) for i in range(4) for j in range(4))
say(f'H4 sphere radius 1e-3, 7, 1e6: worst turn change {mp.nstr(w4a, 3)}; two-leg loop on the sphere {mp.nstr(w4b, 3)},'
    f' out and back in velocity {mp.nstr(w4c, 3)} -> {"KILLED" if max(w4a, w4b, w4c) > TOL40 else "not killed"} (tolerance 1e-40)'
    f'   [{time.time()-t0:.0f} s]')
