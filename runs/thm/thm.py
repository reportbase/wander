# THM run 1: three thumbs meeting at the corner (plans/thm-plan.md). Exact (sympy) and 50-digit (mpmath).
import sympy as sp, mpmath as mp
mp.mp.dps = 50
ok = lambda c: 'not killed' if c else 'KILLED'

# T1: flat screen at unit distance along a look; a screen point at radius r is at angle a, tan a = r.
# solid angle per screen area = cos^3 a; the uniform measure's density on the sphere is 1/(4π); so (1/4π)cos^3 a per area
# for the whole sphere, (1/2π)(1+r^2)^(-3/2) for the hemisphere in front. Check the hemisphere integrates to 1.
r = sp.symbols('r', positive=True)
dens = (1/(2*sp.pi))*(1 + r**2)**sp.Rational(-3, 2)
tot = sp.integrate(dens*2*sp.pi*r, (r, 0, sp.oo))
print('T1 hemisphere total', tot, '; density peak at r=0 (decreasing):', sp.simplify(sp.diff(dens, r)) < 0 if False else 'd/dr =', sp.simplify(sp.diff(dens, r)))
T1 = (tot == 1)
print('T1', ok(T1))

# T2: corner planes n.e1 = n.e2, n.e2 = n.e3 (n.e1 = n.e3 follows); their common line
x, y, z = sp.symbols('x y z', real=True)
sol = sp.solve([sp.Eq(x, y), sp.Eq(y, z)], [x, y, z], dict=True)
print('T2 common line of the three corner planes:', sol)
# rank check: the three plane normals (1,-1,0),(0,1,-1),(1,0,-1) span 2 dims -> a line
M = sp.Matrix([[1, -1, 0], [0, 1, -1], [1, 0, -1]])
T2 = (M.rank() == 2) and sol == [{x: z, y: z}]
print('T2 rank', M.rank(), ok(T2))

# T3: look along depth e3: crosshair n = e3, readings n.e1/n.e3 = 0, n.e2/n.e3 = 0 (home of pairs (1,3),(2,3)); pair (1,2)
# undefined (0/0). Corner of pair (1,3) at 45 deg off. Look down the diagonal: all three ratios 1.
n_depth = sp.Matrix([0, 0, 1]); n_diag = sp.Matrix([1, 1, 1])/sp.sqrt(3)
print('T3 depth look readings e1/e3, e2/e3:', n_depth[0]/n_depth[2], n_depth[1]/n_depth[2], '; diagonal look:', [sp.simplify(n_diag[i]/n_diag[j]) for i, j in ((0, 1), (1, 2), (0, 2))])
T3 = T2 and all(sp.simplify(n_diag[i]/n_diag[j]) == 1 for i, j in ((0, 1), (1, 2), (0, 2)))
print('T3', ok(T3))

# T4: corner reach one thumb on each -> point (1,1,1), length sqrt3; angle thumb-to-look
L = sp.sqrt(3); ang = sp.acos(1/sp.sqrt(3))
print('T4 distance along look', L, '; thumb off look', sp.N(ang*180/sp.pi, 8), 'deg')
T4 = abs(sp.N(ang*180/sp.pi, 30) - mp.mpf('54.735610317245345684622999669981')) < 1e-20
print('T4', ok(T4))

# T5: nearest edge of the wedge from the diagonal: angle between diagonal and plane x=0: asin(1/sqrt3)
edge = sp.asin(1/sp.sqrt(3))
print('T5 edge off look', sp.N(edge*180/sp.pi, 8), 'deg')
# shares on the octant under the uniform measure: P(v<=h) = 1/2 by symmetry; P(h largest) = 1/3; octant 1/8
# check P(h largest) numerically by integrating over the octant in spherical coordinates
f = lambda th, ph: mp.sin(th)  # area element, theta polar from z(=h?), use axes: h=z
def share(cond):
    num = mp.quad(lambda th: mp.quad(lambda ph: mp.sin(th) if cond(mp.cos(th), mp.sin(th)*mp.cos(ph), mp.sin(th)*mp.sin(ph)) else 0, [0, mp.pi/4, mp.pi/2]), [0, mp.atan(mp.sqrt(2)), mp.pi/2])
    return num/(mp.pi/2)
p_half = share(lambda h, a, b: a <= h)
print('T5 P(v<=h) on the octant', mp.nstr(p_half, 12), '(quadrature over a discontinuity; exact 1/2 by the swap symmetry)')
T5 = abs(p_half - mp.mpf(1)/2) < 1e-6
print('T5', ok(T5), '(numeric; the 1/3 and 1/6 are WDG run 1 exact)')

# T6: share of a 42 x 53 deg (half-angles) flat view looking down the diagonal that lies in the wedge
u = n_diag
# screen basis: w up = projection of e2? use symmetric frame: w = (2*e2 - e1 - e3)/sqrt6, rgt = (e3 - e1)/sqrt2  (any rotation about u)
w = sp.Matrix([-1, 2, -1])/sp.sqrt(6); rg = sp.Matrix([-1, 0, 1])/sp.sqrt(2)
uu = [float(c) for c in u]; ww = [float(c) for c in w]; rr = [float(c) for c in rg]
X = mp.tan(53*mp.pi/180); Y = mp.tan(42*mp.pi/180)
def inw(sx, sy):
    d = [uu[i] + sx*rr[i] + sy*ww[i] for i in range(3)]
    return 1 if min(d) >= 0 else 0
N = 600; cnt = 0
for i in range(N):
    for j in range(N):
        cnt += inw(float(-X + (2*X)*(i + 0.5)/N), float(-Y + (2*Y)*(j + 0.5)/N))
frac = cnt/(N*N)
print('T6 share of the view (screen area) in the wedge', round(frac, 4), '(grid 600x600; depends on the turn about the look:')
# the turn about the look matters: try the page's frame (vertical thumb straight up on the screen)
for rot in (0, 15, 30, 45, 60, 90):
    c, s_ = mp.cos(rot*mp.pi/180), mp.sin(rot*mp.pi/180)
    r2 = [float(c*rr[i] + s_*ww[i]) for i in range(3)]; w2 = [float(-s_*rr[i] + c*ww[i]) for i in range(3)]
    cc = 0
    for i in range(200):
        for j in range(200):
            sx = float(-X + 2*X*(i + .5)/200); sy = float(-Y + 2*Y*(j + .5)/200)
            d = [uu[k] + sx*r2[k] + sy*w2[k] for k in range(3)]
            cc += min(d) >= 0
    print('   turned', rot, 'deg:', round(cc/40000, 4))
T6 = frac < 0.5
print('T6', ok(T6))

# T7: scaling
k = sp.symbols('k', positive=True); p = sp.Matrix(sp.symbols('p1 p2 p3', real=True)); H = sp.symbols('H', positive=True)
T7 = all(sp.simplify((k*p[i])/(k*H) - p[i]/H) == 0 for i in range(3))
print('T7', ok(T7))

# T8: cos^3 at the wedge edge and at the thumbs
c_edge = sp.cos(sp.pi/2 - sp.acos(1/sp.sqrt(3)))  # angle off look = asin(1/sqrt3) -> cos = sqrt(2/3)
v_edge = sp.simplify(sp.cos(sp.asin(1/sp.sqrt(3)))**3); v_thumb = sp.simplify(sp.cos(sp.acos(1/sp.sqrt(3)))**3)
print('T8 cos^3 at the edge', v_edge, sp.N(v_edge, 6), '; at the thumbs', v_thumb, sp.N(v_thumb, 6))
T8 = abs(sp.N(v_edge, 30) - mp.mpf(2)/3*mp.sqrt(mp.mpf(2)/3)) < 1e-20 and abs(sp.N(v_thumb, 30) - 1/(3*mp.sqrt(3))) < 1e-20
print('T8', ok(T8))
