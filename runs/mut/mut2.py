# MUT run 2 (run 1's M2 line fixed: e**x**0 raised e to the first power): two readers reading and writing each other. Predictions in plans/mut-plan.md.
from fractions import Fraction as F
import mpmath as mp

mp.mp.dps = 60
out = []


def rep(code, ok, msg):
    line = f"{code}: {'not killed' if ok else 'KILLED'}  {msg}"
    print(line)
    out.append(line)


def sim(x, a, b, al, be):
    return x + al * (a - x) + be * (b - x)


a, b = F(0), F(3)            # d_A = 1, d_B = e^3, in levels
starts = [F(-5), F(0), F(3, 2), F(10)]

# ---------- M1 ----------
ok = True
worst = 0
for al in (F(1, 8), F(1, 4), F(1, 2), F(3, 4)):
    xs = (a + b) / 2
    for x0 in starts:
        x = x0
        for n in range(1, 41):
            x = sim(x, a, b, al, al)
            if abs(x - xs) != abs(1 - 2 * al) ** n * abs(x0 - xs):
                ok = False
rep('M1', ok, "simultaneous, alpha = beta in 1/8, 1/4, 1/2, 3/4, four starts, 40 rounds: |x_n - (a+b)/2| = |1-2alpha|^n |x_0 - x*| exactly every round"
    + " (alpha = 1/2 lands in one round)")

# ---------- M2 ----------
xs = (a + b) / 2
sA = mp.e ** (mp.mpf((a - xs).numerator) / (a - xs).denominator)
sB = mp.e ** (mp.mpf((b - xs).numerator) / (b - xs).denominator)
rep('M2b', a + b - 2 * xs == 0 and abs(sA - mp.sqrt(mp.e ** int(a - b))) < mp.mpf(10) ** -55,
    f"at x* the levels a - x* = {a - xs}, b - x* = {b - xs}, their sum 0 exactly, so s_A s_B = 1; s_A = {mp.nstr(sA, 12)} = sqrt(d_A/d_B)")

# ---------- M3 ----------
ok = True
for lnk in (F(-7), F(5, 3), F(40)):
    for al, be in ((F(1, 4), F(1, 4)), (F(1, 5), F(1, 2))):
        x, y = F(-5), F(-5) + lnk
        for n in range(30):
            x, y = sim(x, a, b, al, be), sim(y, a + lnk, b + lnk, al, be)
            if y - x != lnk or (a - x) != (a + lnk - y) or (b - x) != (b + lnk - y):
                ok = False
rep('M3', ok, "the world scaled by e^-7, e^(5/3), e^40: x_n moved by ln k every round, a - x_n and b - x_n (the readings' levels) unmoved, exactly")

# ---------- M4 ----------
ok = True
rows = []
for al, be in ((F(1, 5), F(1, 2)), (F(1, 10), F(9, 10)), (F(3, 4), F(1, 4)), (F(1, 3), F(1, 3))):
    xs = (al * a + be * b) / (al + be)
    for x0 in starts:
        x = x0
        for n in range(1, 31):
            x = sim(x, a, b, al, be)
            if abs(x - xs) != abs(1 - al - be) ** n * abs(x0 - xs):
                ok = False
    rows.append((al, be, xs, a + b - 2 * xs))
ok = ok and all((r[3] == 0) == (r[0] == r[1]) for r in rows)
rep('M4', ok, "; ".join(f"alpha {r[0]}, beta {r[1]}: x* {r[2]}, ln(s_A s_B) {r[3]}" for r in rows)
    + "; factor |1 - alpha - beta| a round exactly")

# ---------- M5 ----------
def chain(N, seed):
    # rational breadths and thumbs from a fixed rule
    H = [F(2 + (7 * i + seed) % 5, 1 + (3 * i + seed) % 4) for i in range(N)]
    t = [F(1, 10 + (5 * i + 2 * seed) % 7) for i in range(N)]
    R = [H[i + 1] / t[i] for i in range(N - 1)]          # thing i's right gap wanted
    L = [H[i - 1] / t[i] for i in range(1, N)]            # thing i's left gap wanted (i = 1..N-1)
    return H, t, R, L


def pos_update(g, R, L):
    N = len(g) + 1
    dp = []
    for i in range(N):
        v = 0
        if i < N - 1:
            v += (g[i] - R[i]) / 2
        if i > 0:
            v -= (g[i - 1] - L[i - 1]) / 2
        dp.append(v)
    return dp


def gap_update(g, R, L):
    dp = pos_update(g, R, L)
    return [dp[i + 1] - dp[i] for i in range(len(g))]


def solve(Amat, rhs):
    n = len(rhs)
    M = [row[:] + [rhs[i]] for i, row in enumerate(Amat)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [M[r][j] - f * M[c][j] for j in range(n + 1)]
    return [M[i][n] / M[i][i] for i in range(n)]


ok = True
rows = []
for N, seed in ((5, 1), (8, 2), (12, 3)):
    H, t, R, L = chain(N, seed)
    n = N - 1
    zero = [F(0)] * n
    c0 = gap_update(zero, R, L)
    A = [[gap_update([F(int(i == j)) for i in range(n)], R, L)[r] - c0[r] for j in range(n)] for r in range(n)]
    gs = solve(A, [-x for x in c0])                       # gap fixed point, solved once
    lam = mp.eig(mp.matrix([[mp.mpf(A[r][j].numerator) / A[r][j].denominator for j in range(n)] for r in range(n)]))[0]
    lam_re = [mp.re(l) for l in lam]
    lmax = max(-l for l in lam_re)
    crit = 2 / lmax
    allneg = all(l < 0 for l in lam_re) and all(abs(mp.im(l)) < mp.mpf(10) ** -40 for l in lam)
    res = {}
    for frac, label in ((mp.mpf('0.9'), 'below'), (mp.mpf('1.1'), 'above')):
        al = frac * crit
        g = [mp.mpf(1)] * n
        for it in range(6000):
            dg = gap_update(g, [mp.mpf(r.numerator) / r.denominator for r in R], [mp.mpf(l.numerator) / l.denominator for l in L])
            g = [g[i] + al * dg[i] for i in range(n)]
            if max(abs(x) for x in g) > mp.mpf(10) ** 30:
                break
        res[label] = max(abs(g[i] - (mp.mpf(gs[i].numerator) / gs[i].denominator)) for i in range(n))
    # scaling the world by k
    k = F(7, 3)
    Hk = [h * k for h in H]
    Rk = [Hk[i + 1] / t[i] for i in range(N - 1)]
    Lk = [Hk[i - 1] / t[i] for i in range(1, N)]
    c0k = gap_update(zero, Rk, Lk)
    gsk = solve(A, [-x for x in c0k])
    scal = all(gsk[i] == k * gs[i] for i in range(n))
    drift = sum(pos_update(gs, R, L)) / N
    rows.append((N, crit, res['below'], res['above'], scal, allneg, drift))
    ok = ok and res['below'] < mp.mpf(10) ** -50 and res['above'] > 1 and scal and allneg
rep('M5', ok, "; ".join(f"N={r[0]}: 2/lambda_max {mp.nstr(r[1], 8)}, at 0.9 of it off the solve by {mp.nstr(r[2], 3)}, at 1.1 by "
                         f"{mp.nstr(r[3], 3)}, solution x k = k x solution {r[4]}, eigenvalues real negative {r[5]}, "
                         f"positions drift {mp.nstr(mp.mpf(r[6].numerator) / r[6].denominator, 6)} alpha a round at the gaps' fixed point"
                         for r in rows))

# ---------- M6 ----------
ok = True
xs = (a + b) / 2
x = F(-5)
for n in range(20):
    x2 = sim(x, a, b, F(1), F(1))
    if x2 - xs != -(x - xs):
        ok = False
    x = x2
cyc = x != xs
x = F(-5)
for n in range(1, 21):
    x = sim(x, a, b, F(5, 4), F(5, 4))
    if abs(x - xs) != F(3, 2) ** n * abs(F(-5) - xs):
        ok = False
rep('M6', ok and cyc, "alpha + beta = 2: x' - x* = -(x - x*) every round, a two-cycle; alpha = beta = 5/4: |x_n - x*| = (3/2)^n |x_0 - x*| exactly, diverging")

# ---------- M7 ----------
ok = True
rows = []
for al, be in ((F(1, 2), F(1, 2)), (F(1, 5), F(1, 2)), (F(3, 4), F(1, 10))):
    xB = ((1 - be) * al * a + be * b) / (1 - (1 - al) * (1 - be))
    xA = xB + al * (a - xB)
    x = F(-5)
    e0 = None
    for n in range(1, 31):
        xa = x + al * (a - x)
        x = xa + be * (b - xa)
        if e0 is None:
            e0 = abs(F(-5) - xB)
        if abs(x - xB) != ((1 - al) * (1 - be)) ** n * e0:
            ok = False
    # the cycle itself
    if xB + al * (a - xB) != xA or xA + be * (b - xA) != xB:
        ok = False
    rows.append((al, be, xA, xB, (xA + xB) / 2))
ok = ok and rows[0][2] == (2 * a + b) / 3 and rows[0][3] == (a + 2 * b) / 3 and rows[0][4] == (a + b) / 2
rep('M7', ok, "; ".join(f"alpha {r[0]}, beta {r[1]}: after A {r[2]}, after B {r[3]}, midpoint {r[4]}" for r in rows)
    + "; factor (1-alpha)(1-beta) a round exactly")

open('runs/mut/mut-run2.txt', 'w').write("\n".join(out) + "\n")
