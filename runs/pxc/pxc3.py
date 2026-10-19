"""PXC run 3: which error is least where, and where the error is round. See plans/pxc-plan.md.

Half-baseline b = 1, standpoints A = (-1, 0) and B = (1, 0). Each reads the direction to a place, turned by delta_1 and
delta_2 (independent, spread 1). The triangulation map (delta_1, delta_2) -> (x, y) is the exact intersection of the two
turned lines; its Jacobian J is taken by complex step in mpmath at 50 digits, never from the closed forms, and the
error's covariance is J J^T. Needs mpmath (PyPI, BSD).
"""
import mpmath as mp
mp.mp.dps = 50
def verdict(ok): return "not killed" if ok else "KILLED"
A, Bp = (mp.mpf(-1), mp.mpf(0)), (mp.mpf(1), mp.mpf(0))
H = mp.mpf('1e-40')

def meet(ta, tb):
    """the meeting point of the line from A at angle ta and the line from B at angle tb (complex-safe)"""
    ca, sa, cb, sb = mp.cos(ta), mp.sin(ta), mp.cos(tb), mp.sin(tb)
    det = ca * (-sb) - sa * (-cb)
    s = ((Bp[0] - A[0]) * (-sb) - (Bp[1] - A[1]) * (-cb)) / det
    return A[0] + s * ca, A[1] + s * sa

def cov(x, y):
    """the covariance J J^T of the meeting point at (x, y), J by complex step in each direction's turn"""
    ta, tb = mp.atan2(y - A[1], x - A[0]), mp.atan2(y - Bp[1], x - Bp[0])
    c1 = [mp.im(v) / H for v in meet(mp.mpc(ta, H), tb)]
    c2 = [mp.im(v) / H for v in meet(ta, mp.mpc(tb, H))]
    J = mp.matrix([[c1[0], c2[0]], [c1[1], c2[1]]])
    return J * J.T

rel = lambda a, b: abs(a / b - 1)

# ---------------------------------------------------------------- P8: on the bisector, which error is least where
w_depth = w_across = w_total = mp.mpf(0)
for j in range(-100, 101):
    k = mp.mpf(2) ** (mp.mpf(j) / 10); d = 1 / k
    C = cov(mp.mpf(0), d)
    depth, across = mp.sqrt(C[1, 1]) / d, mp.sqrt(C[0, 0]) / d
    total = mp.sqrt(C[0, 0] + C[1, 1]) / d
    w_depth = max(w_depth, rel(depth, mp.sqrt(2) * mp.cosh(mp.log(k))))
    w_across = max(w_across, rel(across, mp.sqrt(2) * (1 + k ** 2) / 2))
    w_total = max(w_total, rel(total, mp.sqrt(2) * (1 + k ** 2) ** mp.mpf(1.5) / (2 * k)))
def total_at(k):
    C = cov(mp.mpf(0), 1 / k); return mp.sqrt(C[0, 0] + C[1, 1]) * k
lo, hi = mp.mpf('0.2'), mp.mpf('2')                               # golden section on the exact total
g = (mp.sqrt(5) - 1) / 2
for _ in range(160):
    a, b = hi - g * (hi - lo), lo + g * (hi - lo)
    (lo, hi) = (lo, b) if total_at(a) < total_at(b) else (a, hi)
kmin = (lo + hi) / 2
ok8 = max(w_depth, w_across, w_total) <= mp.mpf('1e-12') and abs(kmin - 1 / mp.sqrt(2)) <= mp.mpf('1e-9')
print(f"P8 depth/d vs sqrt2*cosh(ln k): {mp.nstr(w_depth, 3)}; across/d vs sqrt2*(1+k^2)/2: {mp.nstr(w_across, 3)};"
      f" total/d vs sqrt2*(1+k^2)^1.5/(2k): {mp.nstr(w_total, 3)}")
print(f"   the total least at k = {mp.nstr(kmin, 15)} (1/sqrt2 = {mp.nstr(1 / mp.sqrt(2), 15)}), d = {mp.nstr(1 / kmin, 12)} half-baselines;"
      f" there {mp.nstr(total_at(kmin) / mp.sqrt(2), 10)}*sqrt2, at the corner {mp.nstr(total_at(mp.mpf(1)) / mp.sqrt(2), 10)}*sqrt2 ->", verdict(ok8))
for j in (-4, -2, -1, 0, 1, 2, 4):
    k = mp.mpf(2) ** j; C = cov(mp.mpf(0), 1 / k); d = 1 / k
    print(f"   {j:+d} levels (d = {mp.nstr(d, 5):>7}): depth {mp.nstr(mp.sqrt(C[1, 1]) / d / mp.sqrt(2), 6):>8}, across"
          f" {mp.nstr(mp.sqrt(C[0, 0]) / d / mp.sqrt(2), 6):>8}, total {mp.nstr(mp.sqrt(C[0, 0] + C[1, 1]) / d / mp.sqrt(2), 6):>8} (times sqrt2)")

# ---------------------------------------------------------------- P9: on the circle, round only at the top
w9, rows9 = mp.mpf(0), []
for deg in range(5, 180, 5):
    phi = mp.radians(deg); x, y = mp.cos(phi), mp.sin(phi)             # on the circle of radius b = 1
    C = cov(x, y)
    ev = mp.eig(C)[0]; ev = sorted(mp.re(e) for e in ev)
    aspect = mp.sqrt(ev[1] / ev[0])
    r1, r2 = mp.hypot(x - A[0], y), mp.hypot(x - Bp[0], y)
    w9 = max(w9, rel(aspect, max(r1, r2) / min(r1, r2)))
    if deg in (15, 45, 75, 90, 135): rows9.append((deg, aspect))
ok9 = w9 <= mp.mpf('1e-12')
print(f"P9 the aspect on the circle vs max(r1,r2)/min(r1,r2), 5..175 deg: worst {mp.nstr(w9, 3)} ->", verdict(ok9))
print("   " + ", ".join(f"{d} deg: {mp.nstr(a, 6)}" for d, a in rows9))

# ---------------------------------------------------------------- P10: off the bisector, no flip
def radial(rho, phi):
    """the radial error over rho, from the exact Jacobian"""
    u = (mp.cos(phi), mp.sin(phi)); C = cov(rho * u[0], rho * u[1])
    return mp.sqrt(u[0] ** 2 * C[0, 0] + 2 * u[0] * u[1] * C[0, 1] + u[1] ** 2 * C[1, 1]) / rho
def radial_formula(rho, phi):
    c, s = mp.cos(phi), mp.sin(phi)
    r1s, r2s = rho ** 2 + 1 + 2 * rho * c, rho ** 2 + 1 - 2 * rho * c
    return mp.sqrt(r1s ** 2 * (rho - c) ** 2 + r2s ** 2 * (rho + c) ** 2) / (2 * rho ** 2 * s)
w10 = mp.mpf(0); mins = []
for deg in range(15, 91, 15):
    phi = mp.radians(deg)
    for j in range(-40, 41):
        rho = mp.mpf(2) ** (mp.mpf(j) / 10)
        w10 = max(w10, rel(radial(rho, phi), radial_formula(rho, phi)))
    lo, hi = mp.mpf('0.05'), mp.mpf('20')
    for _ in range(160):
        a, b = hi - g * (hi - lo), lo + g * (hi - lo)
        (lo, hi) = (lo, b) if radial(a, phi) < radial(b, phi) else (a, hi)
    rmin = (lo + hi) / 2
    mins.append((deg, rmin, radial(rmin, phi), radial(mp.mpf(1), phi)))
p60 = mp.radians(60); f2, fh = radial(mp.mpf(2), p60), radial(mp.mpf('0.5'), p60)
ok10 = w10 <= mp.mpf('1e-12') and rel(f2, fh) > mp.mpf('0.01')
print(f"P10 exact vs the formula on rays 15..90 deg: worst {mp.nstr(w10, 3)}; at 60 deg, rho = 2: {mp.nstr(f2, 8)},"
      f" rho = 1/2: {mp.nstr(fh, 8)} ->", verdict(ok10))
print("   least along each ray (measured, not predicted):")
for deg, rmin, fmin, f1 in mins:
    print(f"   {deg:>2} deg: least at rho = {mp.nstr(rmin, 8)} half-baselines, {mp.nstr(fmin, 6)}; on the circle {mp.nstr(f1, 6)}")
