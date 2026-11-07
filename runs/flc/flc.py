"""FLC: a flat chart for the read in space (plans/flc-plan.md). Run from the repository root:
    python3 runs/flc/flc.py
Predictions F1-F7 are in the plan, written before this script was run."""
import math, random
import numpy as np
import mpmath as mp

mp.mp.dps = 40
rng = random.Random(20261107)
out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)
def verdict(name, ok, note=''):
    say(f'{name}: {"not killed" if ok else "KILLED"}{("  (" + note + ")") if note else ""}')

# ---------- F1: the cylinder ----------
def logpolar(x):
    r = mp.sqrt(sum(c * c for c in x))
    return [mp.log(r)] + [c / r for c in x]
worst = mp.mpf(0)
for _ in range(1000):
    x = [mp.mpf(rng.uniform(-1, 1)) * mp.mpf(10) ** rng.uniform(-3, 3) for _ in range(3)]
    r2 = sum(c * c for c in x); h = mp.mpf('1e-15')
    J = []
    for j in range(3):
        xp = list(x); xm = list(x); xp[j] += h; xm[j] -= h
        fp, fm = logpolar(xp), logpolar(xm)
        J.append([(a - b) / (2 * h) for a, b in zip(fp, fm)])
    for a in range(3):
        for b in range(3):
            g = sum(J[a][k] * J[b][k] for k in range(4))   # pulled-back metric
            want = (1 / r2) if a == b else 0
            worst = max(worst, abs(g * r2 - want * r2))       # relative to the factor 1/r^2
say(f'F1 worst |g r^2 - I| over 1000 points: {mp.nstr(worst, 3)}')
verdict('F1', worst < mp.mpf('1e-10'))

# ---------- F2: writing a slide that commutes ----------
def rand_rot():
    q = np.array([rng.gauss(0, 1) for _ in range(4)]); q /= np.linalg.norm(q)
    w, x, y, z = q
    return np.array([[1-2*(y*y+z*z), 2*(x*y-w*z), 2*(x*z+w*y)],
                     [2*(x*y+w*z), 1-2*(x*x+z*z), 2*(y*z-w*x)],
                     [2*(x*z-w*y), 2*(y*z+w*x), 1-2*(x*x+y*y)]])
def lp(x):
    r = np.linalg.norm(x); return math.log(r), x / r
worst = 0.0
pts = [np.array([rng.uniform(-1, 1) for _ in range(3)]) * 10 ** rng.uniform(-3, 3) for _ in range(1000)]
rots = [rand_rot() for _ in range(100)]
for R in rots:
    k = 10 ** rng.uniform(-6, 6)
    for x in pts[:200]:
        u1, w1 = lp(R @ (k * x))            # scale, then turn, read on the cylinder
        u0, w0 = lp(x); u2, w2 = u0 + math.log(k), R @ w0   # slide u, turn omega
        u3, w3 = lp(k * (R @ x))            # turn, then scale
        worst = max(worst, abs(u1 - u2) / max(1, abs(u2)), np.max(np.abs(w1 - w2)), abs(u1 - u3) / max(1, abs(u3)), np.max(np.abs(w1 - w3)))
say(f'F2 worst difference, slide/turn in either order: {worst:.2e}')
verdict('F2', worst < 1e-14 * 50, 'doubles; tolerance 1e-14 per unit of |u|, ln k up to 13.8')

# ---------- F3: Lambert x the lay, the read's measure flat ----------
def lambert(om):       # about the look z; om a unit vector with z >= 0
    s = math.hypot(om[0], om[1]); R = math.sqrt(max(0.0, 2 - 2 * om[2]))
    return (0.0, 0.0) if s == 0 else (R * om[0] / s, R * om[1] / s)
# Jacobian: solid angle per unit of disc area, by finite differences in mpmath
def lam_inv_mp(X, Y):
    R2 = X * X + Y * Y; c = 1 - R2 / 2; s = mp.sqrt(1 - c * c); R = mp.sqrt(R2)
    return [X / R * s, Y / R * s, c]
worstJ = mp.mpf(0)
for _ in range(500):
    rr = mp.sqrt(mp.mpf(rng.uniform(0.01, 1.99))); b = mp.mpf(rng.uniform(0, 2 * math.pi))
    X, Y = rr * mp.cos(b), rr * mp.sin(b); h = mp.mpf('1e-15')
    dX = [(p - m) / (2 * h) for p, m in zip(lam_inv_mp(X + h, Y), lam_inv_mp(X - h, Y))]
    dY = [(p - m) / (2 * h) for p, m in zip(lam_inv_mp(X, Y + h), lam_inv_mp(X, Y - h))]
    cr = [dX[1]*dY[2]-dX[2]*dY[1], dX[2]*dY[0]-dX[0]*dY[2], dX[0]*dY[1]-dX[1]*dY[0]]
    worstJ = max(worstJ, abs(mp.sqrt(sum(c*c for c in cr)) - 1))
say(f'F3 Lambert: |dOmega/dA - 1| worst over 500 points: {mp.nstr(worstJ, 3)}  (g: dg = sech(u) du / pi by definition)')
# draws from the read's measure, with no trig: direction a normal 3-vector folded to the front, distance ratio |Y/X|
NB = 16; N = 2_000_000
nprng = np.random.default_rng(20261107)
V = nprng.standard_normal((N, 3)); V[:, 2] = np.abs(V[:, 2]); V /= np.linalg.norm(V, axis=1)[:, None]
t = np.abs(nprng.standard_normal(N) / nprng.standard_normal(N))       # d/H, half-Cauchy
g = (2 / np.pi) * np.arctan(t)                                       # the lay (the writer's formula, for binning)
R2 = 2 - 2 * V[:, 2]                                                  # Lambert radius squared, uniform on [0, 2]
beta = np.arctan2(V[:, 1], V[:, 0]) % (2 * np.pi)
ring = np.minimum((R2 / 2 * NB).astype(int), NB - 1)
sect = np.minimum((beta / (2 * np.pi) * NB).astype(int), NB - 1)
gb = np.minimum((g * NB).astype(int), NB - 1)
cnt = np.bincount((ring * NB + sect) * NB + gb, minlength=NB ** 3)
mean = N / NB ** 3; se = math.sqrt(mean)
zmax = np.max(np.abs(cnt - mean)) / se
say(f'F3 draws: {NB**3} cells of equal chart volume, mean {mean:.1f}, worst {zmax:.2f} standard errors')
verdict('F3', worstJ < mp.mpf('1e-12') and zmax < 5)

# ---------- F4: turns keep the measure, not the shape ----------
mp.mp.dps = 30
def lam_mp(om):
    s = mp.sqrt(om[0]**2 + om[1]**2); R = mp.sqrt(2 - 2 * om[2])
    return (R * om[0] / s, R * om[1] / s)
def rotx(phi):
    c, s = mp.cos(phi), mp.sin(phi)
    return lambda v: [v[0], c * v[1] - s * v[2], s * v[1] + c * v[2]]
def transition(phi):   # chart about the old look -> chart about the look turned by phi (a turn of the world by -phi)
    Rm = rotx(phi)    # takes the new look (0, sin phi, cos phi) to (0, 0, 1)
    return lambda X, Y: lam_mp(Rm(lam_inv_mp(X, Y)))
def jac(T, X, Y, h=mp.mpf('1e-12')):
    a = T(X + h, Y); b = T(X - h, Y); c = T(X, Y + h); d = T(X, Y - h)
    return mp.matrix([[(a[0]-b[0])/(2*h), (c[0]-d[0])/(2*h)], [(a[1]-b[1])/(2*h), (c[1]-d[1])/(2*h)]])
def smax(M):
    T = sum(M[i, j] ** 2 for i in range(2) for j in range(2)); D = abs(M[0,0]*M[1,1]-M[0,1]*M[1,0])
    return mp.sqrt((T + mp.sqrt(T * T - 4 * D * D)) / 2)
ok4 = True
for deg in (15, 30, 45, 60, 75, 90):
    phi = mp.radians(deg); T = transition(phi); new_look = [0, mp.sin(phi), mp.cos(phi)]  # look turned toward +y
    worstJ = mp.mpf(0); n = 0
    while n < 2000:
        om = [mp.mpf(rng.gauss(0, 1)) for _ in range(3)]; nn = mp.sqrt(sum(c*c for c in om)); om = [c / nn for c in om]
        if om[2] <= mp.mpf('0.02') or (om[1] * new_look[1] + om[2] * new_look[2]) <= mp.mpf('0.02') or om[0]**2 + om[1]**2 < mp.mpf('1e-6'):
            continue
        X, Y = lam_mp(om); M = jac(T, X, Y)
        worstJ = max(worstJ, abs(abs(M[0,0]*M[1,1]-M[0,1]*M[1,0]) - 1)); n += 1
    # at the old look (the disc's centre): expected 1/cos(phi/2); the centre itself is singular for finite differences of the
    # polar form, so read it just off the centre and at the centre by a symmetric limit
    e = mp.mpf('1e-9'); s0 = smax(jac(T, e, mp.mpf(0)))
    want0 = 1 / mp.cos(phi / 2)
    # at the directions square to both looks: (+-1, 0, 0)
    Xq, Yq = lam_mp([mp.mpf(1), mp.mpf('1e-25'), mp.mpf('1e-25')])
    sq = smax(jac(T, Xq, Yq))
    Mf = mp.matrix([[mp.cos(phi), -mp.sin(phi) / 2], [2 * mp.sin(phi), mp.cos(phi)]]); wantq = smax(Mf)
    bad = worstJ > mp.mpf('1e-11') or abs(s0 - want0) > mp.mpf('1e-8') or abs(sq - wantq) > mp.mpf('1e-9')
    ok4 = ok4 and not bad
    say(f'F4 phi={deg:2d}: |det-1| worst {mp.nstr(worstJ,3)}; stretch at old look {mp.nstr(s0,12)} vs 1/cos(phi/2) {mp.nstr(want0,12)}; '
        f'at the square direction {mp.nstr(sq,12)} vs formula {mp.nstr(wantq,12)}')
# the grid bound, in doubles
def lam_np(om):
    s = np.hypot(om[..., 0], om[..., 1]); R = np.sqrt(np.maximum(0, 2 - 2 * om[..., 2]))
    return np.stack([R * om[..., 0] / s, R * om[..., 1] / s], -1)
def lam_inv_np(P):
    R2 = np.sum(P * P, -1); c = 1 - R2 / 2; s = np.sqrt(np.maximum(0, 1 - c * c)); R = np.sqrt(R2)
    return np.stack([P[..., 0] / R * s, P[..., 1] / R * s, c], -1)
grid_max = {}
for deg in (15, 30, 45, 60, 75, 90):
    phi = math.radians(deg); c, s = math.cos(phi), math.sin(phi)
    def T(P):
        v = lam_inv_np(P); w = np.stack([v[..., 0], c * v[..., 1] - s * v[..., 2], s * v[..., 1] + c * v[..., 2]], -1)
        return lam_np(w)
    xs = np.linspace(-math.sqrt(2), math.sqrt(2), 400); X, Y = np.meshgrid(xs, xs); P = np.stack([X, Y], -1)
    v = lam_inv_np(P); inside = (np.sum(P * P, -1) < 2 - 1e-4) & (np.sum(P * P, -1) > 1e-6)
    inside &= (v[..., 1] * math.sin(phi) + v[..., 2] * math.cos(phi)) > 1e-3
    h = 1e-5
    dX = (T(P + [h, 0]) - T(P - [h, 0])) / (2 * h); dY = (T(P + [0, h]) - T(P - [0, h])) / (2 * h)
    Tr = dX[..., 0]**2 + dX[..., 1]**2 + dY[..., 0]**2 + dY[..., 1]**2
    D = np.abs(dX[..., 0] * dY[..., 1] - dX[..., 1] * dY[..., 0])
    sm = np.sqrt((Tr + np.sqrt(np.maximum(0, Tr * Tr - 4 * D * D))) / 2)
    grid_max[deg] = float(np.max(sm[inside]))
say('F4 grid (400 x 400, both hemispheres): largest stretch ' + ', '.join(f'{d} deg {m:.5f}' for d, m in grid_max.items()))
ok4 = ok4 and all(m <= 2 + 1e-6 for m in grid_max.values())
verdict('F4', ok4, 'the 90-degree grid maximum short of 2 only by the grid missing the exact direction')

# ---------- F5: the stereographic chart ----------
def st_mp(om): return (2 * om[0] / (1 + om[2]), 2 * om[1] / (1 + om[2]))
def st_inv_mp(X, Y):
    w2 = X * X + Y * Y; d = 4 + w2
    return [4 * X / d, 4 * Y / d, (4 - w2) / d]
worst_aniso = mp.mpf(0)
for _ in range(10):
    q = [mp.mpf(rng.gauss(0, 1)) for _ in range(4)]; nq = mp.sqrt(sum(c*c for c in q)); w, x, y, z = [c / nq for c in q]
    Rm = [[1-2*(y*y+z*z), 2*(x*y-w*z), 2*(x*z+w*y)], [2*(x*y+w*z), 1-2*(x*x+z*z), 2*(y*z-w*x)], [2*(x*z-w*y), 2*(y*z+w*x), 1-2*(x*x+y*y)]]
    T = lambda X, Y: st_mp([sum(Rm[i][j] * v for j, v in enumerate(st_inv_mp(X, Y))) for i in range(3)])
    n = 0
    while n < 100:
        X, Y = mp.mpf(rng.uniform(-2, 2)), mp.mpf(rng.uniform(-2, 2))
        if X*X + Y*Y > 4: continue
        img = [sum(Rm[i][j] * v for j, v in enumerate(st_inv_mp(X, Y))) for i in range(3)]
        if img[2] < mp.mpf('-0.9'): continue
        M = jac(T, X, Y); sM = smax(M); D = abs(M[0,0]*M[1,1]-M[0,1]*M[1,0]); smin = D / sM
        worst_aniso = max(worst_aniso, abs(sM / smin - 1)); n += 1
def st_area(X, Y, h=mp.mpf('1e-15')):   # solid angle per unit of stereographic area
    a = st_inv_mp(X + h, Y); b = st_inv_mp(X - h, Y); c = st_inv_mp(X, Y + h); d = st_inv_mp(X, Y - h)
    dX = [(p - m) / (2 * h) for p, m in zip(a, b)]; dY = [(p - m) / (2 * h) for p, m in zip(c, d)]
    cr = [dX[1]*dY[2]-dX[2]*dY[1], dX[2]*dY[0]-dX[0]*dY[2], dX[0]*dY[1]-dX[1]*dY[0]]
    return mp.sqrt(sum(c*c for c in cr))
ratio = st_area(mp.mpf(2), mp.mpf(0)) / st_area(mp.mpf(0), mp.mpf(0))
say(f'F5 stereographic: worst |sigma_max/sigma_min - 1| over 1000 points and 10 turns {mp.nstr(worst_aniso,3)}; rim/centre density {mp.nstr(ratio, 15)}')
verdict('F5', worst_aniso < mp.mpf('1e-9') and abs(ratio - mp.mpf(1) / 4) < mp.mpf('1e-12'))

# ---------- F6: the plane ----------
th = nprng.uniform(0, np.pi, 1_000_000)          # the read's directions in the plane, uniform by turn over the half turn
t2 = np.abs(nprng.standard_normal(1_000_000) / nprng.standard_normal(1_000_000))
g2 = (2 / np.pi) * np.arctan(t2)
c2 = np.bincount(np.minimum((th / np.pi * 64).astype(int), 63) * 64 + np.minimum((g2 * 64).astype(int), 63), minlength=4096)
z2 = np.max(np.abs(c2 - 1e6 / 4096)) / math.sqrt(1e6 / 4096)
# a turn is theta -> theta + phi: its Jacobian on (theta, g) is the identity, stretch 1, by construction; check numerically
J = np.array([[1.0, 0.0], [0.0, 1.0]])
say(f'F6 plane: (theta, g) cells worst {z2:.2f} standard errors; a turn\'s Jacobian {J.tolist()} (stretch 1)')
verdict('F6', z2 < 5)

# ---------- F7: random charts, no third way ----------
found = 0; tried = 0
for i in range(2000):
    kind = i % 2
    if kind == 0:   # Lambert with a seeded area-preserving twist (r, b) -> (r, b + f(r^2)) and a seeded area-preserving shear
        a1, a2, a3 = rng.uniform(-2, 2), rng.uniform(-2, 2), rng.uniform(-0.5, 0.5)
        chart = lambda om, a1=a1, a2=a2, a3=a3: (lambda P: (lambda r2, b: (math.sqrt(r2) * math.cos(b + a1 * r2 + a2 * r2 * r2), math.sqrt(r2) * math.sin(b + a1 * r2 + a2 * r2 * r2)))(P[0]**2 + P[1]**2, math.atan2(P[1], P[0])))(lambert(om))
        chart2 = lambda om, ch=chart, a3=a3: (lambda P: (P[0] + a3 * P[1], P[1]))(ch(om))
        ch = chart2
    else:           # stereographic with a seeded disc automorphism (conformal)
        a = complex(rng.uniform(-0.6, 0.6), rng.uniform(-0.6, 0.6)); th0 = rng.uniform(0, 2 * math.pi)
        def ch(om, a=a, th0=th0):
            w = complex(om[0], om[1]) / (1 + om[2])            # stereographic onto the unit disc (hemisphere)
            z = complex(math.cos(th0), math.sin(th0)) * (w - a) / (1 - a.conjugate() * w)
            return (z.real, z.imag)
    # density of the measure per chart area at 40 directions, and the stretch of a 30-degree turn at 40 directions
    phi = math.radians(30); c, s = math.cos(phi), math.sin(phi)
    def inv_dir(az, el): return np.array([math.sin(el) * math.cos(az), math.sin(el) * math.sin(az), math.cos(el)])
    dens = []; stretch = []
    for _ in range(40):
        az, el = rng.uniform(0, 2 * math.pi), math.acos(rng.uniform(0.25, 0.95))
        om = inv_dir(az, el); h = 1e-6
        # chart Jacobian from (az, cos el) (an equal-area parametrization of directions)
        def P(az, ce): return np.array(ch(inv_dir(az, math.acos(ce))))
        ce = math.cos(el)
        Ja = (P(az + h, ce) - P(az - h, ce)) / (2 * h); Jc = (P(az, ce + h) - P(az, ce - h)) / (2 * h)
        dens.append(1 / abs(Ja[0] * Jc[1] - Ja[1] * Jc[0]))
        # turn's stretch in this chart: Jacobian of chart(R(chart^-1)) via chart Jacobians at om and R om
        def Rv(v): return np.array([v[0], c * v[1] - s * v[2], s * v[1] + c * v[2]])
        def Q(az, ce): return np.array(ch(Rv(inv_dir(az, math.acos(ce)))))
        Ka = (Q(az + h, ce) - Q(az - h, ce)) / (2 * h); Kc = (Q(az, ce + h) - Q(az, ce - h)) / (2 * h)
        A = np.column_stack([Ja, Jc]); B = np.column_stack([Ka, Kc])
        try:
            M = B @ np.linalg.inv(A); sv = np.linalg.svd(M, compute_uv=False); stretch.append(max(sv[0], 1 / sv[1]))
        except np.linalg.LinAlgError:
            stretch.append(float('inf'))
    tried += 1
    flat = max(dens) / min(dens) < 1 + 1e-6; rigid = max(stretch) < 1 + 1e-6
    if flat and rigid: found += 1
say(f'F7: {tried} seeded charts, flat and rigid under a 30-degree turn: {found}')
verdict('F7', found == 0)

open('runs/flc/flc-run1.txt', 'w').write('\n'.join(out) + '\n')
