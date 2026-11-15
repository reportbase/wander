# CPX run 1: when composing reads forces i. Exact rationals, seeded. See plans/cpx-plan.md.
from fractions import Fraction as F
import random
random.seed(20261115)

def mul(A, B):
    a,b,c,d = A; e,f,g,h = B
    return (a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h)
def add(A, B): return tuple(x+y for x,y in zip(A,B))
def sc(k, A): return tuple(k*x for x in A)
I = (F(1),F(0),F(0),F(1))
def tr(A): return A[0]+A[3]
def det(A): return A[0]*A[3]-A[1]*A[2]
def disc(A): return tr(A)**2-4*det(A)
def is_scalar(A): return A[1]==0 and A[2]==0 and A[0]==A[3]

def nullity(rows, n):
    M = [list(r) for r in rows]; r = 0
    for col in range(n):
        piv = next((i for i in range(r, len(M)) if M[i][col] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and M[i][col] != 0:
                k = M[i][col]/M[r][col]
                M[i] = [x-k*y for x,y in zip(M[i], M[r])]
        r += 1
    return n - r, M

def commutant_dim(A):
    # unknown C=(x,y,z,w); rows of CA-AC=0
    rows = []
    for k in range(4):
        basis = [F(0)]*4; basis[k] = F(1)
        pass
    cols = []
    for k in range(4):
        E = [F(0)]*4; E[k] = F(1); E = tuple(E)
        D = add(mul(E, A), sc(-1, mul(A, E)))
        cols.append(D)
    rows = [[cols[k][i] for k in range(4)] for i in range(4)]
    return nullity(rows, 4)[0]

def form_dim(A):
    # symmetric Q=(q1,q2,q3): A^T Q A - det(A) Q = 0
    At = (A[0],A[2],A[1],A[3]); dA = det(A)
    cols = []
    for (q1,q2,q3) in [(1,0,0),(0,1,0),(0,0,1)]:
        Q = (F(q1),F(q2),F(q2),F(q3))
        D = add(mul(mul(At,Q),A), sc(-dA,Q))
        cols.append((D[0],D[1],D[3]))
    rows = [[cols[k][i] for k in range(3)] for i in range(3)]
    n, M = nullity(rows, 3)
    return n, M

def rnd(): return F(random.randint(-6,6), random.randint(1,4))
def sample(kind):
    while True:
        if kind == 'para':
            a = rnd(); x = rnd(); y = rnd()
            if y == 0: continue
            N = (x, y, -x*x/y, -x)
            A = add(sc(a,I), N)
        else:
            A = (rnd(),rnd(),rnd(),rnd())
        if is_scalar(A) or det(A) == 0: continue
        dd = disc(A)
        if kind=='ell' and dd < 0: return A
        if kind=='hyp' and dd > 0: return A
        if kind=='para' and dd == 0: return A

S = [sample('ell') for _ in range(800)] + [sample('hyp') for _ in range(800)] + [sample('para') for _ in range(400)]
fails = {k: [] for k in ['J1','J2','J3','J4','J5','J6']}

for A in S:
    a = tr(A)/2; B = add(A, sc(-a, I)); dd = disc(A)
    if mul(B,B) != sc(dd/4, I): fails['J1'].append(A)
    if commutant_dim(A) != 2: fails['J2'].append(A)
    for _ in range(3):
        p1,q1,p2,q2 = rnd(),rnd(),rnd(),rnd()
        lhs = mul(add(sc(p1,I),sc(q1,B)), add(sc(p2,I),sc(q2,B)))
        rhs = add(sc(p1*p2+q1*q2*dd/4, I), sc(p1*q2+p2*q1, B))
        if lhs != rhs: fails['J3'].append(A)
    # J4: fixed directions; for dd==0 the eigenspace of a (rank of B) must be 1-dim
    if dd == 0:
        if not (B != (0,0,0,0) and det(B) == 0): fails['J4'].append(A)

ret = {'ell':0,'hyp':0,'para':0}; ret_bad = []
for A in S:
    P = A
    for n in range(1, 65):
        if is_scalar(P):
            k = 'ell' if disc(A)<0 else ('hyp' if disc(A)>0 else 'para')
            ret[k] += 1
            if disc(A) >= 0: ret_bad.append((A, n))
            break
        P = mul(P, A)
cons = {'[[0,-1],[1,0]]':(0,-1,1,0), '[[1,-1],[1,1]]':(1,-1,1,1), '[[-1,-1],[1,0]]':(-1,-1,1,0), '[[1,-1],[1,0]]':(1,-1,1,0)}
cons_n = {}
for name, t in cons.items():
    A = tuple(F(x) for x in t); P = A; cons_n[name] = None
    for n in range(1, 65):
        if is_scalar(P): cons_n[name] = n; break
        P = mul(P, A)
if ret_bad: fails['J5'] = ret_bad
if [cons_n[k] for k in cons] != [2,4,3,6]: fails['J5'].append(('constructed', cons_n))

J0 = (F(0),F(-1),F(1),F(0))
j6 = []
for c2 in [F(1,4),F(1,2),F(1),F(2),F(4),F(9)]:
    K = (F(0),-c2,F(1),F(0))
    commute = mul(K,J0) == mul(J0,K)
    n, M = form_dim(K)
    j6.append((c2, commute, n))
    if commute != (c2 == 1) or n != 1: fails['J6'].append(c2)
fdims = [form_dim(A)[0] for A in S[:800]]
if any(d != 1 for d in fdims): fails['J6'].append('ell form dim')
# the form of K_c: solve with q1 = 1
forms = []
for c2 in [F(1,4),F(2),F(9)]:
    K = (F(0),-c2,F(1),F(0))
    # K^T Q K = c2 Q with Q=diag(1, t): check t = 1/c2
    t = 1/c2; Q = (F(1),F(0),F(0),t); Kt = (K[0],K[2],K[1],K[3])
    forms.append((c2, mul(mul(Kt,Q),K) == sc(c2,Q)))
if not all(ok for _,ok in forms): fails['J6'].append('form h^2+v^2/c^2')

print("samples: elliptic 800, hyperbolic 800, parabolic 400 (rational entries, seed 20261115)")
print("returns (A^n scalar, n<=64):", ret)
for A, n in ret_bad[:5]:
    print("  returned with disc>=0:", [str(x) for x in A], "n =", n, "tr", tr(A), "det", det(A))
print("constructed returns:", cons_n)
print("J6 K_c commutes with J0 / form dim:", [(str(c), cm, n) for c, cm, n in j6])
print("J6 form h^2 + v^2/c^2 kept by K_c:", [(str(c), ok) for c, ok in forms])
for k, v in fails.items():
    print(k, "killed" if v else "not killed", f"({len(v)} failures)" if v else "")
