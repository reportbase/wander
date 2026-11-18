# EHO part 3: the observer's own motion on a small source, exact (mpmath, 60 digits).
# A boost of rapidity eta along +z acts on the sky as the Mobius map w -> e^{-eta} w on the stereographic
# coordinate w = tan(theta/2) e^{i phi}, theta from the direction of motion (aberration: tan(theta'/2) = e^{-eta} tan(theta/2)).
# Local scale on the sphere: |dw'/dw| (1+|w|^2)/(1+|w'|^2); local rotation: arg(dw'/dw) in frames along the meridian.
from mpmath import mp, mpf, tan, atan, cos, sin, acos, sqrt, atanh, exp, pi, log10, fabs, arg, mpc, findroot
mp.dps = 60
def boost(beta):
    return atanh(beta)
def scale_rot(beta, chi):
    eta = boost(beta)
    w = tan(chi/2); k = exp(-eta)
    wp = k*w
    s = k*(1+w*w)/(1+wp*wp)
    rot = arg(mpc(k,0))          # derivative k is real and positive: no rotation
    return s, rot
def doppler(beta, chi):
    g = 1/sqrt(1-beta*beta)
    # direction seen by the moving observer: chi' with tan(chi'/2)=e^{-eta}tan(chi/2); angular sizes scale by
    # D(chi') = 1/(g(1 - beta cos chi')) in the moving frame's direction
    chip = 2*atan(exp(-boost(beta))*tan(chi/2))
    return 1/(g*(1-beta*cos(chip))), chip
def sph(theta, phi):
    return [sin(theta)*cos(phi), sin(theta)*sin(phi), cos(theta)]
def ang(a, b):
    d = sum(x*y for x,y in zip(a,b)); return acos(max(min(d,1),-1))
def ring_image(beta, chi, alpha, n=360):
    # a small circle of angular radius alpha about (chi, 0); map each point; fit the image circle's radius
    eta = boost(beta); k = exp(-eta)
    c = sph(chi, 0)
    # orthonormal frame at c
    e1 = [cos(chi), 0, -sin(chi)]; e2 = [0, 1, 0]
    pts = []
    for j in range(n):
        t = 2*pi*j/n
        p = [cos(alpha)*c[i] + sin(alpha)*(cos(t)*e1[i] + sin(t)*e2[i]) for i in range(3)]
        th = acos(p[2]); ph = mp.atan2(p[1], p[0])
        thp = 2*atan(k*tan(th/2))
        pts.append(sph(thp, ph))
    # image of a circle is a circle on the sphere: its centre is the normalized mean of an equally spaced set? use
    # plane through three points
    import itertools
    A, B, C = pts[0], pts[n//3], pts[2*n//3]
    u = [B[i]-A[i] for i in range(3)]; v = [C[i]-A[i] for i in range(3)]
    nrm = [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]]
    L = sqrt(sum(x*x for x in nrm)); nrm = [x/L for x in nrm]
    if sum(nrm[i]*pts[0][i] for i in range(3)) < 0: nrm = [-x for x in nrm]
    radii = [ang(nrm, p) for p in pts]
    off = max(fabs(sum(nrm[i]*p[i] for i in range(3)) - sum(nrm[i]*pts[0][i] for i in range(3))) for p in pts)
    return radii, off
print("Q6: local scale against the Doppler factor, local rotation")
worst_s = mpf(0); worst_r = mpf(0)
for beta in [mpf('1e-4'), mpf('1e-3'), mpf('5e-3')]:
    for chid in [0, 30, 90, 150]:
        chi = mpf(chid)*pi/180 if chid else mpf('1e-40')
        s, rot = scale_rot(beta, chi)
        D, chip = doppler(beta, chi)
        rel = fabs(s*D - 1)   # angular size seen = alpha * (dtheta'/dtheta) = alpha * s ; and s should equal 1/D(chi')?? report both
        worst_s = max(worst_s, min(fabs(s-D), fabs(s-1/D))); worst_r = max(worst_r, fabs(rot))
        print(f"  beta={float(beta):.0e} chi={chid:3d}  scale={mp.nstr(s,20)}  D(chi')={mp.nstr(D,20)}  1/D={mp.nstr(1/D,20)}  rot={mp.nstr(rot,5)}")
print("  worst |scale - D or 1/D| =", mp.nstr(worst_s,3), " worst rotation =", mp.nstr(worst_r,3))
print("Q6 finite ring, alpha = 42 uas / 2 (radius), beta = 5e-3, chi = 90")
alpha = mpf(21)*pi/(180*3600*10**6)
radii, off = ring_image(mpf('5e-3'), pi/2, alpha)
r0 = sum(radii)/len(radii)
print("  image a circle: max |radius - mean|/mean =", mp.nstr(max(fabs(r-r0) for r in radii)/r0, 3), " plane offset", mp.nstr(off,3))
print("  image radius / alpha =", mp.nstr(r0/alpha, 15))
print("Q7: change of the ring's diameter (42 uas) for the observer's motions, worst over direction")
for name, beta in [("Earth's spin", mpf('1.55e-6')), ("Earth's orbit", mpf('9.94e-5')), ("Sun vs CMB", mpf('1.23e-3'))]:
    worst = max(fabs(scale_rot(beta, mpf(c)*pi/180 if c else mpf('1e-40'))[0]-1) for c in range(0,181,5))
    print(f"  {name:14s} beta={float(beta):.3e}  max fractional {mp.nstr(worst,4)}  -> {mp.nstr(worst*42,4)} uas")
