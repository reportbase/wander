# KPL run 2: S2's measured orbit about Sgr A* (Gillessen et al. 2017, VizieR J/ApJ/837/30 table5).
# Usage: python3 -I runs/kpl/kpl2.py <table5.tsv> [table3.tsv]
# Step 1 untimed: a conic through the places, e from the focus, the Thiele-Innes constants, the elements.
# Step 2 the clock from place: M/2pi.  Step 3 the period in the observer's years.  Step 4 a in mas only.
import sys, numpy as np
from scipy.optimize import least_squares

def read_tsv(fn):
    rows = [l.rstrip('\n').split('\t') for l in open(fn) if l.strip() and not l.startswith('#')]
    head = rows[0]; body = [r for r in rows[3:] if len(r) == len(head)]   # name row, unit row, dashes row
    return head, body

head, body = read_tsv(sys.argv[1])
ix = {h.strip(): k for k, h in enumerate(head)}
t, x, y, sx, sy = [], [], [], [], []
for r in body:
    if r[ix['Flag']].strip() != 'a': continue
    vals = [r[ix[c]].strip() for c in ('oRA-S2', 'oDE-S2', 'e_oRA-S2', 'e_oDE-S2')]
    if '' in vals: continue
    t.append(float(r[ix['Date']])); y.append(float(vals[0])); x.append(float(vals[1]))   # x north (Dec), y east (RA)
    sy.append(float(vals[2])); sx.append(float(vals[3]))
t, x, y, sx, sy = map(np.array, (t, x, y, sx, sy))
o = np.argsort(t); t, x, y, sx, sy = t[o], x[o], y[o], sx[o], sy[o]
print('S2 astrometric looks: %d, dates %.3f to %.3f' % (len(t), t.min(), t.max()))

# ---- step 1: the conic, dates dropped (the order of the looks is not used here)
def conic_fit(x, y, w):
    Mx = np.c_[x*x, x*y, y*y, x, y]*w[:, None]
    return np.linalg.lstsq(Mx, w, rcond=None)[0]
s = np.hypot(sx, sy)/np.sqrt(2)
c = conic_fit(x, y, 1/s)
for _ in range(5):   # reweight by the gradient: algebraic residual over (gradient times sigma), the geometric distance
    A2, B2, C2, D2, E2 = c
    g = np.hypot(2*A2*x + B2*y + D2, B2*x + 2*C2*y + E2)
    c = conic_fit(x, y, 1/(g*s))
A2, B2, C2, D2, E2 = c
Mq = np.array([[A2, B2/2], [B2/2, C2]])
ctr = np.linalg.solve(2*Mq, -np.array([D2, E2]))
Q = lambda p: p @ Mq @ p + np.array([D2, E2]) @ p - 1
def chord(u):   # the s > 0 with ctr + s u on the conic
    a = u @ Mq @ u; b = 2*ctr @ Mq @ u + np.array([D2, E2]) @ u; cc = Q(ctr)
    return (-b + np.sqrt(b*b - 4*a*cc))/(2*a)
u = -ctr/np.linalg.norm(ctr)                         # from the centre toward the focus (the origin)
half = chord(u); e = np.linalg.norm(ctr)/half
AB = -ctr/e                                          # (A, B): centre = -e (A, B)
v = np.array([-(Mq @ u)[1], (Mq @ u)[0]]); v /= np.linalg.norm(v)   # the conjugate direction: u' M v = 0
FG = chord(v)*v/np.sqrt(1 - e*e)
print('STEP 1 (untimed): apparent centre (%.2f, %.2f) mas, e = %.4f' % (ctr[0], ctr[1], e))

def ti(el):
    a, i, W, w = el
    cw, sw, cW, sW, ci = np.cos(w), np.sin(w), np.cos(W), np.sin(W), np.cos(i)
    return a*np.array([cw*cW - sw*sW*ci, cw*sW + sw*cW*ci, -sw*cW - cw*sW*ci, -sw*sW + cw*cW*ci])
def elements(A, B, F, G):
    sols = []
    for s0 in np.linspace(0, 2*np.pi, 12, endpoint=False):
        for s1 in np.linspace(0, 2*np.pi, 6, endpoint=False):
            r = least_squares(lambda q: ti(q) - [A, B, F, G], [np.hypot(A, B), 1.0 + s1/3, s0, s1], max_nfev=2000)
            if r.cost < 1e-12*(A*A + B*B):
                a, i, W, w = r.x; i = np.mod(i, 2*np.pi)
                if i > np.pi: i = 2*np.pi - i; W += np.pi; w += np.pi
                k = (round(abs(a), 6), round(np.degrees(i), 3), round(np.degrees(np.mod(W, 2*np.pi)), 3) % 360, round(np.degrees(np.mod(w, 2*np.pi)), 3) % 360)
                if a > 0 and k not in sols: sols.append(k)
    return sols
untimed = []
for sg in (1, -1):    # the sense of motion is not in untimed places
    untimed += [(sg,) + k for k in elements(AB[0], AB[1], sg*FG[0], sg*FG[1])]
print('STEP 1 elements consistent with the untimed places (sense, a mas, i, Omega, omega deg):')
for k in untimed: print('   ', k)

# ---- steps 2-3: the clock from place, then the dates
def mean_anom(A, B, F, G, e):
    T = np.array([[A, F], [B, G]]); XY = np.linalg.solve(T, np.vstack([x, y]))
    E = np.arctan2(XY[1]/np.sqrt(1 - e*e), XY[0] + e)
    return E - e*np.sin(E)
best = None
for sg in (1, -1):
    M = np.unwrap(mean_anom(AB[0], AB[1], sg*FG[0], sg*FG[1], e))/(2*np.pi)
    p = np.polyfit(t, M, 1)
    res = M - np.polyval(p, t)
    if p[0] > 0 and (best is None or np.median(np.abs(res)) < best[2]): best = (sg, p, np.median(np.abs(res)), res)
sg, p, medres, res = best
P = 1/p[0]; Tp = -p[1]/p[0]
Tp = Tp + P*np.ceil((t.min() - Tp)/P)
print('STEP 2-3: sense %+d; M/2pi against the date: slope %.5f /yr, median |residual| %.4f period, max %.4f' % (sg, p[0], medres, np.abs(res).max()))
print('          period %.3f yr (the observer\'s years), a pericentre at %.3f' % (P, Tp))
el = [k for k in untimed if k[0] == sg]
a_mas = el[0][1] if el else np.nan
print('STEP 4: a = %.2f mas (no a in au, GM or seconds from any step)' % a_mas)

print('\nPREDICTIONS')
print('V1 e %.4f vs 0.884 ->' % e, 'not killed' if abs(e - 0.884) <= 0.02 else 'KILLED')
near = [k for k in untimed if abs(k[2] - 134) <= 3 and min(abs(k[3] - 227), 360 - abs(k[3] - 227)) <= 3 and min(abs(k[4] - 66), 360 - abs(k[4] - 66)) <= 3]
print('V2 among %d untimed solutions, within 3 deg of (134, 227, 66): %s ->' % (len(untimed), near), 'determined' if len(untimed) == 1 and near else ('in the set, not determined' if near else 'KILLED'))
print('V3 median |residual| %.4f period ->' % medres, 'not killed' if medres < 0.01 else 'KILLED')
print('V4 P %.3f yr vs 16.0 ->' % P, 'not killed' if abs(P/16.0 - 1) <= 0.01 else 'KILLED')
print('V5 a %.2f mas vs 125 ->' % a_mas, 'not killed' if abs(a_mas/125 - 1) <= 0.03 else 'KILLED')
R0 = 8300.0   # pc, carried in
a_au = a_mas/1000*R0
print('   with R0 = 8.3 kpc carried in: a = %.0f au, M = a^3/P^2 = %.3g suns' % (a_au, a_au**3/P**2))
if len(sys.argv) > 2:
    h3, b3 = read_tsv(sys.argv[2]); j = {hh.strip(): k for k, hh in enumerate(h3)}
    for r in b3:
        if r[j['Star']].strip() == 'S2':
            print('   the paper (table3): a %s", e %s, i %s, Omega %s, omega %s, Tp %s, P %s' % tuple(r[j[c]].strip() for c in ('a', 'e', 'i', 'Omega', 'w', 'Tp', 'Per')))
