# ACC run 1: a source at rest at t = 0 but accelerating (z = a t^2/2 along y); the look, a charge's pull and the
# linearized pull of gravity at a place at rest, from the exact retarded fields (mpmath, 40 digits), c = 1.
# Usage: python3 -I runs/acc/acc.py
import mpmath as mp
mp.mp.dps = 40

def traj(a):
    z = lambda t: mp.matrix([0, a*t*t/2, 0]); v = lambda t: mp.matrix([0, a*t, 0]); ac = lambda t: mp.matrix([0, a, 0])
    return z, v, ac
def norm(u): return mp.sqrt(sum(c*c for c in u))
def dot(u, w): return sum(u[i]*w[i] for i in range(3))
def cross(u, w): return mp.matrix([u[1]*w[2]-u[2]*w[1], u[2]*w[0]-u[0]*w[2], u[0]*w[1]-u[1]*w[0]])
def tret(t, x, z):
    return mp.findroot(lambda tr: t - tr - norm(x - z(tr)), t - norm(x - z(t)))
def angle(u, w):
    return mp.atan2(norm(cross(u, w)), dot(u, w))
def side(u, w, a):                 # +1 if u is turned from w toward the acceleration's direction
    return 1 if dot(cross(w, u), cross(w, a)) > 0 else -1

def look(x, a):
    z, v, ac = traj(a); tr = tret(0, x, z)
    return z(tr) - x                                      # from the place toward where the light left
def efield(t, x, a):
    z, v, ac = traj(a); tr = tret(t, x, z); Rv = x - z(tr); R = norm(Rv); n = Rv/R; b = v(tr); bd = ac(tr)
    k = 1 - dot(n, b)
    return (n - b)*(1 - dot(b, b))/(k**3*R*R) + cross(n, cross(n - b, bd))/(k**3*R)
def hfield(t, x, a):               # h_00 and h_0i (lowered) of a point mass M = 1, linearized, Lienard-Wiechert form
    z, v, ac = traj(a); tr = tret(t, x, z); Rv = x - z(tr); R = norm(Rv); b = v(tr)
    g = 1/mp.sqrt(1 - dot(b, b)); rho = g*(R - dot(b, Rv))
    u = [g, g*b[0], g*b[1], g*b[2]]
    hb = [[4*u[m]*u[nu]/rho for nu in range(4)] for m in range(4)]       # upper indices
    trace = -hb[0][0] + hb[1][1] + hb[2][2] + hb[3][3]
    h00 = hb[0][0] + trace/2
    h0 = [-hb[0][i+1] for i in range(3)]
    return h00, h0
def pull(x, a):
    acc = []
    for i in range(3):
        def f(s, i=i):
            xx = x.copy(); xx[i] += s; return hfield(0, xx, a)[0]
        d00 = mp.diff(f, 0)
        d0i = mp.diff(lambda t: hfield(t, x, a)[1][i], 0)
        acc.append(d00/2 - d0i)
    return mp.matrix(acc)

aY = mp.matrix([0, 1, 0])
print('first-order coefficients: departure from the present place over eps = a r, toward +a, over sin(psi)')
for psi in (30, 60, 90):
    p = mp.radians(psi); n = mp.matrix([mp.sin(p), mp.cos(p), 0])      # angle psi between a (along y) and n
    for eps in ('1e-3', '1e-4', '1e-5'):
        r = mp.mpf(10); a = mp.mpf(eps)/r; x = n*r
        toward = -x                                                     # the present place, from x
        L = look(x, a); F = -efield(0, x, a); G = pull(x, a)
        cs = []
        for vec in (L, F, G):
            cs.append(side(vec, toward, aY)*angle(vec, toward)/(mp.mpf(eps)*mp.sin(p)))
        print('psi %2d eps %s: look %s  charge %s  gravity %s' % (psi, eps, mp.nstr(cs[0], 10), mp.nstr(cs[1], 10), mp.nstr(cs[2], 10)))
p = 0; n = mp.matrix([0, 1, 0]); r = mp.mpf(10); a = mp.mpf('1e-4')/r; x = n*r
print('psi 0 (a along n): angles look %s charge %s gravity %s' % tuple(mp.nstr(angle(v, -x), 3) for v in (look(x, a), -efield(0, x, a), pull(x, a))))

print('scale test: lengths and times by k, accelerations by 1/k (psi 60, eps 1e-3)')
p = mp.radians(60); n = mp.matrix([mp.sin(p), mp.cos(p), 0])
base = None
for k in (1, 5, 100):
    r = 10*mp.mpf(k); a = mp.mpf('1e-3')/r; x = n*r
    vecs = (look(x, a), -efield(0, x, a), pull(x, a)); ang = [angle(v, -x) for v in vecs]
    mags = [norm(v) for v in vecs[1:]]
    if base is None: base = (ang, mags)
    print('k %3d: angle changes %s; strengths over k=1 times k^2: %s' % (k,
          [mp.nstr(ang[j] - base[0][j], 3) for j in range(3)], [mp.nstr(mags[j]/base[1][j]*k*k, 12) for j in range(2)]))
