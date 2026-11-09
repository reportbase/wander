# BRL run 2: the two-read loop's commutator in unit quaternions (B3'). See plans/brl-plan.md.
from mpmath import mp, mpf, cos, sin, pi, fabs, matrix
exec(open('runs/brl/brl.py').read().split('# B1')[0])   # same helpers and seeded stream
mp.dps = 60
def qmul(p, q):
    a1,b1,c1,d1 = p; a2,b2,c2,d2 = q
    return (a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2, a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2)
def qc(q): return (q[0], -q[1], -q[2], -q[3])
def qof(n, a): s = sin(a/2); return (cos(a/2), s*n[0], s*n[1], s*n[2])
def qmat(q):
    w,x,y,z = q
    return matrix([[1-2*(y*y+z*z), 2*(x*y-w*z), 2*(x*z+w*y)],[2*(x*y+w*z), 1-2*(x*x+z*z), 2*(y*z-w*x)],[2*(x*z-w*y), 2*(y*z+w*x), 1-2*(x*x+y*y)]])
for _ in range(20): r(-pi,pi); r(-3,3)
for _ in range(20): unit(); r(-pi,pi); r(-3,3)
draws = [(r(1e-3,pi), r(1e-3,pi), r(1e-3,pi-mpf('1e-3'))) for _ in range(30)]
draws += [(r(1e-3,2*pi), r(1e-3,2*pi), r(1e-3,pi-mpf('1e-3'))) for _ in range(200)]
ws = 0; wm = 0; above = 0
for a,b,phi in draws:
    n1 = [mpf(1),mpf(0),mpf(0)]; n2 = [cos(phi), sin(phi), mpf(0)]
    q1, q2 = qof(n1,a), qof(n2,b)
    Q = qmul(qc(q2), qmul(qc(q1), qmul(q2, q1)))
    form = 1 - 2*sin(a/2)**2*sin(b/2)**2*sin(phi)**2
    ws = max(ws, fabs(Q[0]-form))
    if form < 0: above += 1
    # sign flips of either lift
    for s1 in (1,-1):
        for s2 in (1,-1):
            p1 = tuple(s1*x for x in q1); p2 = tuple(s2*x for x in q2)
            P = qmul(qc(p2), qmul(qc(p1), qmul(p2, p1)))
            ws = max(ws, fabs(P[0]-form))
    A, B = rot(n1,a), rot(n2,b); M = B.T*A.T*B*A
    wm = max(wm, maxabs(qmat(Q)-M))
lines = [f"B3' scalar part vs form: max diff {mp.nstr(ws,3)} over {len(draws)} draws x 4 sign choices ({above} with Omega > pi)",
         f"B3' quaternion image vs run 1's matrix M: max diff {mp.nstr(wm,3)}",
         "-> " + ("held" if max(ws,wm) < mpf('1e-50') else "KILLED")]
print('\n'.join(lines)); open('runs/brl/brl-run2.txt','w').write('\n'.join(lines)+'\n')
