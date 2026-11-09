# UWR run 1: BRL's unequal write as a passive polarizer stack (U1-U4). See plans/uwr-plan.md.
import random
from mpmath import mp, mpf, matrix, cos, sin, exp, sqrt, tanh, acosh, log, pi, fabs, eye, svd_r
mp.dps = 60
rng = random.Random(20261111)
def r(a, b): return mpf(a) + (mpf(b)-mpf(a))*mpf(rng.random())
def R(a): return matrix([[cos(a), -sin(a)], [sin(a), cos(a)]])
def S(c): return matrix([[c, 0], [0, 1]])
def mx(A): return max(fabs(A[i,j]) for i in range(A.rows) for j in range(A.cols))
def frob2(A): return sum(A[i,j]**2 for i in range(2) for j in range(2))
def Dof(A):  # diattenuation from singular values
    s = svd_r(A, compute_uv=False); s1, s2 = max(s), min(s); return (s1**2 - s2**2)/(s1**2 + s2**2)
out = []
def say(x): print(x); out.append(x)
draws = [(r(-pi, pi), exp(r(0.05, 2.5))) for _ in range(40)]
w1 = wa = 0; w2 = 0; ok3 = True; zero = 0
for a, c in draws:
    w1 = max(w1, mx(R(pi/2)*S(c)*R(-pi/2) - matrix([[1,0],[0,c]])))
    M = S(c)**-1 * R(-a) * S(c) * R(a)
    t = 1/c
    Px, Py = matrix([[1,0],[0,t]]), matrix([[t,0],[0,1]])
    J = Py * R(-a) * Px * R(a)                      # rotator a, polarizer x, rotator -a, polarizer y
    # J = (1/c)S(c)^{-1}... compare up to the scalar: J / (J's det)^(1/2) vs M
    k = sqrt(mp.det(J)); Jn = J / k
    wa = max(wa, min(mx(Jn - M), mx(Jn + M)))
    F = frob2(M); D2 = sqrt(F**2 - 4)/F
    w2 = max(w2, fabs(D2 - Dof(J)))
    zeta = acosh((M[0,0]+M[1,1])/2)
    if D2 < tanh(2*zeta) - mpf('1e-50'): ok3 = False
say(f"U1 diag(1,c) = R(90)S(c)R(-90): {mp.nstr(w1,3)}; stack (det-normalised) = M up to sign: {mp.nstr(wa,3)} -> {'held' if max(w1,wa) < 1e-50 else 'KILLED'}")
say(f"U2 D = sqrt(F^2-4)/F against the stack's own singular values: {mp.nstr(w2,3)} -> {'held' if w2 < 1e-50 else 'KILLED'}")
a0, c0 = pi*40/180, mpf(2)
M0 = S(c0)**-1 * R(-a0) * S(c0) * R(a0); F0 = frob2(M0); z0 = acosh((M0[0,0]+M0[1,1])/2)
say(f"   at 40 deg, c = 2: D = {mp.nstr(sqrt(F0**2-4)/F0, 10)}, zeta = {mp.nstr(z0, 10)}, tanh 2zeta = {mp.nstr(tanh(2*z0), 10)}")
zc = max(Dof(Py) for Py in [matrix([[1,0],[0,1]])])  # trivial
dz1 = max(fabs(sqrt(frob2(S(1)**-1*R(-a)*S(1)*R(a))**2-4)) for a, _ in draws)
dz2 = max(fabs(sqrt(frob2(S(c)**-1*R(-pi)*S(c)*R(pi))**2-4)) for _, c in draws)
say(f"   D at c = 1: {mp.nstr(dz1,3)}; at alpha = pi: {mp.nstr(dz2,3)}")
say(f"U3 D >= tanh 2zeta at every draw: {ok3} -> {'held' if ok3 else 'KILLED'}")
ok4 = True
for a, c in draws[:3]:
    M = S(c)**-1 * R(-a) * S(c) * R(a); z = acosh((M[0,0]+M[1,1])/2)
    ys = []
    for n in range(1, 9):
        Mn = M**n; F = frob2(Mn); D = sqrt(F**2-4)/F; ys.append(log(1 - D))
    slope = ys[7] - ys[6]
    say(f"U4 draw a={mp.nstr(a*180/pi,4)} deg c={mp.nstr(c,4)}: slope of ln(1-D_n) at n=8 {mp.nstr(slope,8)} vs -4 zeta {mp.nstr(-4*z,8)}")
    if fabs(slope/(-4*z) - 1) > 0.02: ok4 = False
say("   -> " + ("held" if ok4 else "KILLED"))
open('runs/uwr/uwr-run1.txt','w').write('\n'.join(out)+'\n')
