# BRL: does a breath close? Exact (mpmath, 60 digits). See plans/brl-plan.md.
# Loops in time order A, B, A^-1, B^-1; product M = B^-1 A^-1 B A on column vectors.
import random
from mpmath import mp, mpf, mpc, matrix, cos, sin, exp, acos, asin, pi, sqrt, eye, fabs, log
mp.dps = 60
rng = random.Random(20261109)
def r(a, b): return mpf(a) + (mpf(b) - mpf(a)) * mpf(rng.random())
def unit():
    while True:
        v = [r(-1, 1) for _ in range(3)]
        n = sqrt(sum(x*x for x in v))
        if n > mpf('0.1'): return [x/n for x in v]
def rot(n, a):
    x, y, z = n; c, s = cos(a), sin(a); C = 1 - c
    return matrix([[c+x*x*C, x*y*C-z*s, x*z*C+y*s],
                   [y*x*C+z*s, c+y*y*C, y*z*C-x*s],
                   [z*x*C-y*s, z*y*C+x*s, c+z*z*C]])
def maxabs(M): return max(fabs(M[i, j]) for i in range(M.rows) for j in range(M.cols))
def angle_axis(R):
    tr = R[0,0]+R[1,1]+R[2,2]
    c = (tr-1)/2
    c = min(max(c, mpf(-1)), mpf(1))
    Om = acos(c)
    ax = [R[2,1]-R[1,2], R[0,2]-R[2,0], R[1,0]-R[0,1]]
    n = sqrt(sum(a*a for a in ax))
    return Om, ([a/n for a in ax] if n > 0 else [0,0,0])
I = eye(3); out = []
def say(s): print(s); out.append(s)

# B1
worst = 0
for _ in range(20):
    a, lam = r(-pi, pi), r(-3, 3)
    A, B = exp(mpc(0, a)), exp(lam)
    M = (1/B)*(1/A)*B*A
    worst = max(worst, abs(M-1))
say(f"B1 plane breath: max |M-1| = {mp.nstr(worst, 3)}  -> {'held' if worst < mpf('1e-58') else 'KILLED'}")
# B2
worst = 0
for _ in range(20):
    n, a, lam = unit(), r(-pi, pi), r(-3, 3)
    A, B = rot(n, a), exp(lam)*I
    M = (B**-1)*(A**-1)*B*A
    worst = max(worst, maxabs(M-I))
say(f"B2 space breath: max |M-I| = {mp.nstr(worst, 3)}  -> {'held' if worst < mpf('1e-50') else 'KILLED'}")
# B3 (+ B6)
worst = 0; worst_orth = 0; worst6 = 0
for k in range(30):
    a, b, phi = r(1e-3, pi), r(1e-3, pi), r(1e-3, pi - mpf('1e-3'))
    n1 = [mpf(1), mpf(0), mpf(0)]; n2 = [cos(phi), sin(phi), mpf(0)]
    A, B = rot(n1, a), rot(n2, b)
    M = B.T*A.T*B*A
    worst_orth = max(worst_orth, maxabs(M.T*M - I), fabs(mp.det(M)-1))
    Om, _ = angle_axis(M)
    pred = 2*acos(1 - 2*sin(a/2)**2*sin(b/2)**2*sin(phi)**2)
    worst = max(worst, fabs(Om - pred))
    e = a; pe = 2*acos(1-2*sin(e/2)**4*sin(phi)**2); w7 = 4*asin(sin(e/2)**2*fabs(sin(phi)))
    worst6 = max(worst6, fabs(pe - w7))
say(f"B3 two reads: residual a turn (orth/det err {mp.nstr(worst_orth,3)}); max |Omega - form| = {mp.nstr(worst,3)}  -> {'held' if worst < mpf('1e-50') else 'KILLED'}")
say(f"B6 equal angles = W7: max diff {mp.nstr(worst6,3)}  -> {'held' if worst6 < mpf('1e-50') else 'KILLED'}")
# B4
say("B4 small loop, first about x, then y (phi = 90 deg), alpha = beta = eps:")
ok4 = True
for p in range(1, 7):
    e = mpf(10)**-p
    A, B = rot([1,0,0], e), rot([0,1,0], e)
    M = B.T*A.T*B*A
    Om, ax = angle_axis(M)
    say(f"   eps=1e-{p}: Omega/(eps^2) = {mp.nstr(Om/e**2, 15)}, axis = ({mp.nstr(ax[0],3)}, {mp.nstr(ax[1],3)}, {mp.nstr(ax[2],8)})")
    if ax[2] > 0: ok4 = False
say(f"   -> {'held (axis -z)' if ok4 else 'KILLED (axis +z)'}")
# also unequal angles, phi = 60 deg
phi = pi/3; e = mpf('1e-5')
A, B = rot([1,0,0], 2*e), rot([cos(phi), sin(phi), 0], 3*e)
M = B.T*A.T*B*A; Om, ax = angle_axis(M)
say(f"   alpha=2e-5, beta=3e-5, phi=60: Omega/(alpha beta sin phi) = {mp.nstr(Om/(6*e*e*sin(phi)), 15)}, axis z {mp.nstr(ax[2],8)}")
# B5
worst = 0; worst_u = 0
for _ in range(20):
    a, b, phi, lam = r(0.1, pi), r(0.1, pi), r(0.1, 3), r(-3, 3)
    A, B = rot([1,0,0], a), rot([cos(phi), sin(phi), 0], b)
    K = exp(lam)*I
    base = B.T*A.T*B*A
    acts = [A, B, A.T, B.T]
    pos_in = rng.randrange(0, 5); pos_out = rng.randrange(pos_in, 5)
    seq = acts[:]
    seq.insert(pos_out, K**-1); seq.insert(pos_in, K)
    M = I
    for X in seq: M = X*M
    worst = max(worst, maxabs(M - base))
    seq2 = acts[:]; seq2.insert(rng.randrange(0, 5), K)
    M2 = I
    for X in seq2: M2 = X*M2
    worst_u = max(worst_u, maxabs(M2 - exp(lam)*base))
say(f"B5 a write inserted: matched max |M - two-read M| = {mp.nstr(worst,3)}; unmatched max |M - k*M| = {mp.nstr(worst_u,3)}  -> {'held' if max(worst, worst_u) < mpf('1e-50') else 'KILLED'}")
open('runs/brl/brl-run1.txt', 'w').write('\n'.join(out) + '\n')
