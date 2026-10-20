"""HTP: parallax from turning the head. See plans/htp-plan.md (predictions written before this script).

The head's axis at the origin, facing +y at the start; the eye at E(D) = r*(sin D, cos D) after a turn D, facing the
turned direction. A point is read as a bearing in the head's frame. Two looks, at 0 and D1, the turn known; the rays
crossed. mpmath at 50 digits.
Run: python3 -I runs/htp/htp.py [1|2]   (run 1 as first run; run 2 wraps pair angles, P1')
"""
from mpmath import mp, mpf, pi, sin, cos, atan2, sqrt, findroot, asin, fabs, inf

mp.dps = 50
import sys
RUN = int(sys.argv[1]) if len(sys.argv) > 1 else 2   # run 1 compared pair angles without wrapping them
TOL = mpf(10) ** -40
deg = lambda x: mpf(x) * pi / 180

def eye(r, D):
    return (r * sin(D), r * cos(D))

def bearing(P, r, D):
    """Angle of P - E(D) from the facing direction (the facing is +y turned clockwise by D), counter-clockwise positive."""
    ex, ey = eye(r, D)
    world = atan2(P[1] - ey, P[0] - ex)          # angle from +x
    facing = pi / 2 - D                           # +y turned clockwise by D
    a = world - facing
    while a > pi: a -= 2 * pi
    while a <= -pi: a += 2 * pi
    return a

def triangulate(b0, b1, r, D1):
    """Rays from E(0) at bearing b0 and from E(D1) at bearing b1, both turned back to the start frame; their crossing,
    or None if the two rays are one (no baseline)."""
    p0, p1 = eye(r, 0), eye(r, D1)
    a0, a1 = pi / 2 + b0, pi / 2 - D1 + b1
    u0, u1 = (cos(a0), sin(a0)), (cos(a1), sin(a1))
    den = u0[0] * u1[1] - u0[1] * u1[0]
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    if fabs(den) < TOL and fabs(dx * u1[1] - dy * u1[0]) < TOL:
        return None                               # the same ray: nothing placed
    if fabs(den) < TOL:
        return None
    t = (dx * u1[1] - dy * u1[0]) / den
    return (p0[0] + t * u0[0], p0[1] + t * u0[1])

out = []
def rec(name, ok, detail):
    out.append((name, ok)); print(f"{'not killed' if ok else 'KILLED':10s} {name}: {detail}")

# a field of points: distances 0.5 r .. 1e6 r, directions within 60 degrees of the start facing (seen in both looks
# for turns up to 30 degrees; for wider turns only those still within view are used)
def field(r):
    pts = []
    for e in [mpf('0.5'), 1, 2, 5, 10, 100, 10**3, 10**4, 10**6]:
        for a in [-50, -20, 0, 15, 40]:
            d = e * r + 2 * r                     # from the axis, beyond the eye
            th = deg(90 - a)
            pts.append((d * cos(th), d * sin(th)))
    return pts

def seen(P, r, D):
    return fabs(bearing(P, r, D)) < deg(80)

# P1: r = 0
r0 = mpf(0)
worst, placed = mpf(0), 0
pts = field(mpf(1))
for D1 in [deg(5), deg(30), deg(90), deg(150)]:
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            a0 = bearing(pts[i], r0, 0) - bearing(pts[j], r0, 0)
            a1 = bearing(pts[i], r0, D1) - bearing(pts[j], r0, D1)
            dd = a0 - a1
            if RUN >= 2:                          # run 2: a pair angle is only defined up to a whole turn
                while dd > pi: dd -= 2 * pi
                while dd <= -pi: dd += 2 * pi
            worst = max(worst, fabs(dd))
    for P in pts:
        if seen(P, r0, D1) and triangulate(bearing(P, r0, 0), bearing(P, r0, D1), r0, D1) is not None:
            placed += 1
rec('P1 a pure turn gives no parallax', worst < TOL and placed == 0, f'largest change in a pair angle {mp.nstr(worst, 3)}, points placed {placed}')

# P2: r > 0, recovery exact
r = mpf('0.1')
worst, n, chord_err = mpf(0), 0, mpf(0)
for D1 in [deg(5), deg(30), deg(90), deg(150)]:
    e0, e1 = eye(r, 0), eye(r, D1)
    chord_err = max(chord_err, fabs(sqrt((e1[0] - e0[0])**2 + (e1[1] - e0[1])**2) - 2 * r * sin(D1 / 2)))
    for P in field(r):
        if not (seen(P, r, 0) and seen(P, r, D1)): continue
        Q = triangulate(bearing(P, r, 0), bearing(P, r, D1), r, D1)
        dist = sqrt(P[0]**2 + P[1]**2)
        worst = max(worst, sqrt((Q[0] - P[0])**2 + (Q[1] - P[1])**2) / dist); n += 1
rec('P2 the chord is the baseline', worst < TOL and chord_err < TOL, f'{n} points recovered, largest relative error {mp.nstr(worst, 3)}; chord = 2r sin(D/2) to {mp.nstr(chord_err, 3)}')

# P3: in r, unchanged by k
def in_r(k, D1):
    rr = r * k
    res = []
    for P in field(r):
        Pk = (P[0] * k, P[1] * k)
        if not (seen(Pk, rr, 0) and seen(Pk, rr, D1)): continue
        Q = triangulate(bearing(Pk, rr, 0), bearing(Pk, rr, D1), mpf(1), D1)   # laid in r: the reader's unit is r
        res.append(Q)
    return res
worst = mpf(0)
for D1 in [deg(30), deg(90)]:
    base = in_r(mpf(1), D1)
    for k in [mpf('1e-3'), mpf(7), mpf('1e3')]:
        got = in_r(k, D1)
        for A, B in zip(base, got):
            worst = max(worst, sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2) / sqrt(A[0]**2 + A[1]**2))
rec('P3 in the reader\'s own unit', worst < TOL, f'largest change of a reading in r under k = 1e-3, 7, 1e3: {mp.nstr(worst, 3)}')

# P4: the reach. Parallax of a point straight ahead at distance d against a point at infinity straight ahead
def parallax(d, rr, D1):
    P = (mpf(0), d)
    far = (mpf(0), mpf(10) ** 30)
    return fabs((bearing(P, rr, D1) - bearing(far, rr, D1)) - (bearing(P, rr, 0) - bearing(far, rr, 0)))
eps = mpf('1e-3')
worst = mpf(0); rows = []
for Dd in [30, 90, 150]:
    D1 = deg(Dd)
    pred = r * sin(D1) / eps
    exact = findroot(lambda d: parallax(d, r, D1) - eps, pred)
    rel = fabs(exact / pred - 1); worst = max(worst, rel)
    rows.append(f'{Dd} deg: exact {mp.nstr(exact, 6)} m, r sin D/eps {mp.nstr(pred, 6)} m, off {mp.nstr(rel, 3)}')
rec('P4 the reach is the sideways step over eps', worst < mpf('0.01'), '; '.join(rows))

# P5: the numbers
arcmin = pi / (180 * 60)
head_mrad = r * sin(deg(90)) / mpf('1e-3')
head_arcmin = r * sin(deg(90)) / arcmin
eye_only = mpf('0.0076') * sin(deg(10)) / arcmin
eye_exact = findroot(lambda d: parallax(d, mpf('0.0076'), deg(10)) - arcmin, eye_only)
rec('P5 the numbers', 1 <= eye_exact <= 10,
    f'head r = 0.1 m, quarter turn: {mp.nstr(head_mrad, 5)} m at 1 mrad, {mp.nstr(head_arcmin, 5)} m at 1 arcmin; '
    f'eye alone r = 7.6 mm, 10 deg: {mp.nstr(eye_only, 4)} m first order, {mp.nstr(eye_exact, 4)} m exact')

# P6: fixating F straight ahead at d_F: the eye's own turn keeps F's bearing; a point on the line of sight shifts against
# F by (bearing change of P) - (bearing change of F)
def shift(d, dF, rr, D1):
    P, F = (mpf(0), d), (mpf(0), dF)
    return (bearing(P, rr, D1) - bearing(P, rr, 0)) - (bearing(F, rr, D1) - bearing(F, rr, 0))
dF = mpf(2)
signs = [(d, shift(mpf(d), dF, r, deg(30))) for d in ['0.5', '1', '1.5', '1.99', '2', '2.01', '3', '10', '1000']]
flip_ok = all((s < 0) == (signs[0][1] < 0) for d, s in signs if mpf(d) < dF) and all((s < 0) != (signs[0][1] < 0) for d, s in signs if mpf(d) > dF) and fabs(dict(signs)['2']) < TOL
zero_r = max(fabs(shift(mpf(d), dF, mpf(0), deg(30))) for d, _ in signs)
rec('P6 fixating', flip_ok and zero_r < TOL, ', '.join(f'{d}: {mp.nstr(s, 3)}' for d, s in signs) + f'; at r = 0 the largest shift {mp.nstr(zero_r, 3)}')

print('\nkilled:', [n for n, ok in out if not ok] or 'none')
