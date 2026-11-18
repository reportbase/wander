"""RIC run 1: the Riccati equation stepped from one standpoint (plans/ric-plan.md)."""
import random
from fractions import Fraction as Q
import mpmath as mp

mp.mp.dps = 50
random.seed(1101)
out = []
def say(*a):
    s = ' '.join(str(t) for t in a); print(s); out.append(s)

def mob(M, s):  # Möbius map of a 2x2 [[a,b],[c,d]] on s, exact or mp
    (a, b), (c, d) = M
    return (a * s + b) / (c * s + d)

def mul(A, B):
    return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]

def Bmat(p, q, r): return [[Q(q, 2), Q(p)], [Q(-r), Q(-q, 2)]]
def step(B, u): return [[1 + u*B[0][0], u*B[0][1]], [u*B[1][0], 1 + u*B[1][1]]]

def fr(x): return mp.mpf(x.numerator) / x.denominator

def tau(u, D):
    if D == 0: return fr(u)
    rD = mp.sqrt(mp.mpc(fr(D)))
    return mp.re(mp.atanh(fr(u) * rD) / rD)

# Q1
B = Bmat(1, 0, 1); s = Q(0)
for _ in range(3): s = mob(step(B, Q(1, 3)), s)
err = abs(mp.mpf(s.numerator) / s.denominator - mp.tan(3 * mp.atan(mp.mpf(1) / 3)))
say('Q1 three steps of 1/3:', s, ' |s - tan(3 atan 1/3)| =', mp.nstr(err, 3))

# Q2, Q4
okA = okB = skipped = n2 = 0; growth = []
while n2 < 100:
    p, q, r = (random.randint(-4, 4) for _ in range(3))
    if r == 0: continue
    D = Q(q * q, 4) - p * r
    k = random.randint(0, 6)
    u = Q(1, k + 8)
    if D > 0 and float(u) * float(D) ** 0.5 >= 1: continue
    s0 = Q(random.randint(-5, 5), random.randint(1, 5))
    B = Bmat(p, q, r)
    # (a) composition rule for an adjacent pair u, v
    v = Q(1, random.randint(8, 14))
    if D > 0 and float(v) * float(D) ** 0.5 >= 1: v = u
    lhs = mul(step(B, u), step(B, v))
    w = (u + v) / (1 + D * u * v)
    rhs = [[(1 + D*u*v) * e for e in row] for row in step(B, w)]
    okA += lhs == rhs
    # (b) five steps against the flow
    s = s0; bad = False
    for _ in range(5):
        M = step(B, u)
        den = M[1][0] * s + M[1][1]
        if den == 0: bad = True; break
        s = mob(M, s)
    T = 5 * tau(u, D)
    E = mp.expm(T * mp.matrix([[mp.mpf(B[i][j].numerator) / B[i][j].denominator for j in range(2)] for i in range(2)]))
    # pole check along the flow: denominator of flow from s0 changes sign
    sm = mp.mpf(s0.numerator) / s0.denominator
    signs = []
    for j in range(0, 51):
        Ej = mp.expm((T * j / 50) * mp.matrix([[mp.mpf(B[i][jj].numerator) / B[i][jj].denominator for jj in range(2)] for i in range(2)]))
        signs.append(mp.sign(Ej[1, 0] * sm + Ej[1, 1]))
    if bad or len(set(signs)) > 1: skipped += 1; continue
    n2 += 1
    flow = (E[0, 0] * sm + E[0, 1]) / (E[1, 0] * sm + E[1, 1])
    okB += abs(flow - mp.mpf(s.numerator) / s.denominator) < mp.mpf(10) ** -40
    # Q4 digits growth
    t = s0; dig = {}
    for i in range(1, 41):
        t = mob(step(B, u), t)
        if i in (20, 40): dig[i] = len(str(abs(t.numerator))) + len(str(t.denominator))
    growth.append(dig[40] / dig[20])
say('Q2 (a) composition rule exact:', okA, '/ 100 tried pairs (incl. skipped-free set)')
say('Q2 (b) five steps = flow to 1e-40:', okB, '/', n2, ' skipped (pole on the way):', skipped)
say('Q4 digits(40)/digits(20): max', round(max(growth), 3), ' median', round(sorted(growth)[50], 3))

# Q3
T = 3 * mp.atan(mp.mpf(1) / 3); exact = mp.tan(T)
f = lambda y: 1 + y * y
def euler(N):
    h = T / N; y = mp.mpf(0)
    for _ in range(N): y += h * f(y)
    return y
def rk4(N):
    h = T / N; y = mp.mpf(0)
    for _ in range(N):
        k1 = f(y); k2 = f(y + h*k1/2); k3 = f(y + h*k2/2); k4 = f(y + h*k3)
        y += h * (k1 + 2*k2 + 2*k3 + k4) / 6
    return y
Ns = [100 * 2**i for i in range(8)]
for name, fn in (('Euler', euler), ('RK4', rk4)):
    errs = [abs(fn(N) - exact) for N in Ns]
    slope = (mp.log(errs[-1]) - mp.log(errs[1])) / (mp.log(Ns[-1]) - mp.log(Ns[1]))
    say('Q3', name, 'errors', [mp.nstr(e, 3) for e in errs[::3]], ' slope', mp.nstr(slope, 4))

# Q5: s' = t + s^2, linear system x' = t y? s = x/y: B(t) = [[0, t], [-1, 0]]
def flowmap(t0, t1):
    cols = []
    for init in ([1, 0], [0, 1]):
        sol = mp.odefun(lambda t, Y: [t * Y[1], -Y[0]], t0, init)
        cols.append(sol(t1))
    M = mp.matrix([[cols[0][0], cols[1][0]], [cols[0][1], cols[1][1]]])
    d = mp.det(M)
    return M / mp.sqrt(d)
mp.mp.dps = 40
M01 = flowmap(0, 1); M12 = flowmap(1, 2)
C = M01 * M12 - M12 * M01
say('Q5 (a) largest entry of [M01, M12]:', mp.nstr(max(abs(C[i, j]) for i in range(2) for j in range(2)), 5))
hits = []
for i in range(2):
    for j in range(2):
        rel = mp.pslq([M01[i, j], 1], maxcoeff=10**4, maxsteps=10**5)
        hits.append(rel)
say('Q5 (b) PSLQ relations of height <= 1e4 for M01 entries:', hits)
say('     M01 =', [[mp.nstr(M01[i, j], 12) for j in range(2)] for i in range(2)])

open('runs/ric/ric-run1.txt', 'w').write('\n'.join(out) + '\n')
