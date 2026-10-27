"""MOD: each system its own unit (plans/mod-plan.md). Exact (sympy, mpmath 50 digits).
Data: Wikipedia wikitext files in the directory given as argv[1] (not committed; sha256 in the plan)."""
import sys, re, os, math, itertools
import sympy as sp
import mpmath as mp
mp.mp.dps = 50
D = sys.argv[1]
ok = {}
def rd(n): return open(os.path.join(D, n + '.txt'), encoding='utf-8').read()

# ---------------- paper ----------------
t = rd('Paper_size')
pairs = [tuple(map(int, m)) for m in re.findall(r'(\d+) × (\d+)(?:&nbsp;| )\|\|', t.split('ISO paper sizes in portrait view')[1].split('|}')[0])]
listed = {}
for n in range(11):
    for k, s in enumerate('ABC'):
        listed[f'{s}{n}'] = pairs[3 * n + k]
r = sp.symbols('r', positive=True)
a_ok = sp.solve(sp.Eq(r, 2 / r), r) == [sp.sqrt(2)]
def exact(series, n):
    # short, long in mm
    A0s = 1000 * mp.mpf(2) ** mp.mpf(-0.25)
    base = {'A': A0s, 'B': mp.mpf(1000), 'C': mp.sqrt(A0s * 1000)}[series]
    s = base * mp.mpf(2) ** (-mp.mpf(n) / 2)
    return s, s * mp.sqrt(2)
rule = {}
for s in 'ABC':
    sh, lo = exact(s, 0)
    cur = (int(mp.nint(sh)), int(mp.nint(lo)))
    rule[f'{s}0'] = cur
    for n in range(1, 11):
        cur = (cur[1] // 2, cur[0])
        rule[f'{s}{n}'] = cur
b_bad = [k for k in listed if listed[k] != rule[k]]
c_worst = max(max(abs(listed[k][0] - exact(k[0], int(k[1:]))[0]), abs(listed[k][1] - exact(k[0], int(k[1:]))[1])) for k in listed)
d_ok = all(mp.almosteq(exact('C', n)[0] / exact('A', n)[0], mp.mpf(2) ** 0.125, 1e-45) and
           mp.almosteq(exact('B', n)[0] / exact('A', n)[0], mp.mpf(2) ** 0.25, 1e-45) and
           mp.almosteq(exact('A', n - 1)[0] / exact('A', n)[0], mp.sqrt(2), 1e-45) for n in range(1, 11))
areas = [exact(s, 0)[0] * exact(s, 0)[1] / 10**6 for s in 'ACB']
print('M1 (a) r = 2/r only at sqrt2:', a_ok)
print('   (b) 66 listed values from the halving rule; mismatches:', b_bad)
print('   (c) worst |listed - exact| mm:', mp.nstr(c_worst, 6))
print('   (d) A:C:B:A(n-1) = 1 : 2^(1/8) : 2^(1/4) : 2^(1/2):', d_ok, '; A0, C0, B0 areas m^2:', [mp.nstr(x, 8) for x in areas])
ok['M1'] = a_ok and not b_bad and c_worst < 1 and d_ok

# ---------------- halving as an exchange ----------------
w, h = sp.symbols('w h', positive=True)  # long side h, short w, aspect h/w
halved_aspect = sp.simplify(w / (h / 2))
m2a = sp.simplify(halved_aspect - 2 / (h / w)) == 0
x = sp.symbols('x', positive=True)
recip = sp.simplify((2 / (sp.sqrt(2) * x)) / sp.sqrt(2) - 1 / x) == 0
let = [sp.Rational(11, 1) / sp.Rational(17, 2)]
for _ in range(3): let.append(2 / let[-1])
gm = sp.sqrt(let[0] * let[1])
print('M2 halving r -> 2/r:', m2a, '; in units of sqrt2 the reciprocal:', recip,
      '; Letter', [sp.N(v, 5) for v in let], 'geometric mean', gm)
ok['M2'] = m2a and recip and gm == sp.sqrt(2) and let[2] == let[0] and abs(sp.N(let[0]) - 1.2941) < 5e-5 and abs(sp.N(let[1]) - 1.5455) < 5e-5

# ---------------- preferred numbers ----------------
t = rd('Renard_series')
tab = t.split('Least rounded')[1].split('|}')[0]
cols = {'#e2e2e2': 5, '#ffe2e2': 10, '#ffffe2': 20, '#e2ffe2': 40}
R = {v: [] for v in cols.values()}
for m in re.finditer(r'background-color: (#[0-9a-f]+);" \| ([0-9.]+)', tab):
    c = cols.get(m.group(1))
    if c: R[c].append(sp.Rational(m.group(2)))
for n in R: R[n] = R[n][:n]   # one decade, 1 … below 10
nested = set(R[5]) <= set(R[10]) <= set(R[20]) <= set(R[40])
dev = {}
for n in R:
    dev[n] = max((abs(mp.mpf(str(v)) / mp.mpf(10) ** (mp.mpf(k) / n) - 1), str(v)) for k, v in enumerate(R[n]))
print('M3 (a) nested:', nested, [len(R[n]) for n in R])
for n in R: print(f'   (b) R{n}: largest deviation {mp.nstr(100*dev[n][0], 4)}% at {dev[n][1]}')
delta = dev[10][0]
def into(v):
    v = mp.mpf(v)
    while v >= 10: v /= 10
    while v < 1: v *= 10
    return v
r10 = [mp.mpf(str(v)) for v in R[10]] + [mp.mpf(10)]
worst = 0
for a_, b_ in itertools.product(R[10], R[10]):
    for v in (into(mp.mpf(str(a_)) * mp.mpf(str(b_))), into(mp.mpf(str(a_)) / mp.mpf(str(b_)))):
        worst = max(worst, min(abs(v / q - 1) for q in r10))
print(f'   (c) products and quotients: worst {mp.nstr(100*worst, 4)}% against 3*delta {mp.nstr(300*delta, 4)}%')
def pow2x10(v):
    v = sp.Rational(v)
    for j in range(-2, 3):
        q = v / sp.Integer(10) ** j
        if q > 0 and (q.p & (q.p - 1)) == 0 and (q.q & (q.q - 1)) == 0: return True
    return False
twos = [str(v) for v in R[10] if pow2x10(v)]
print('   (d) R10 values of the form 2^i*10^j:', len(twos), twos, '; 2^10/10^3 =', sp.Rational(1024, 1000))
ok['M3'] = nested and all(dev[n][0] < 0.013 for n in R) and dev[10][1] == '8/5' and abs(dev[10][0] - mp.mpf('0.0095')) < 5e-5 \
    and worst <= 3 * delta and len(twos) == 8 and set(map(str, R[10])) - set(twos) == {str(sp.Rational('3.15')), str(sp.Rational('6.30'))}

# ---------------- music ----------------
cents = lambda q: 1200 * mp.log(q, 2)
n_ = sp.symbols('n', positive=True, integer=True)
m4a = True  # modes n*f1: interval between modes p and q is p/q whatever f1 (= c/2L)
f1 = sp.symbols('f1', positive=True)
m4a = all(sp.simplify((p * f1) / (q * f1) - sp.Rational(p, q)) == 0 for p, q in [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (5, 3)])
no_close = all(3 ** k != 2 ** m for k in range(1, 200) for m in range(1, 400))
comma = sp.Rational(3 ** 12, 2 ** 19)
c_comma = cents(mp.mpf(3) ** 12 / mp.mpf(2) ** 19)
et5 = cents(mp.mpf(2) ** (mp.mpf(7) / 12)) - cents(mp.mpf(3) / 2)
et3 = cents(mp.mpf(2) ** (mp.mpf(4) / 12)) - cents(mp.mpf(5) / 4)
etm3 = cents(mp.mpf(2) ** (mp.mpf(3) / 12)) - cents(mp.mpf(6) / 5)
cf = mp.identify  # not used
# convergents of log2(3/2)
y = mp.log(mp.mpf(3) / 2, 2)
a = []; z = y
for _ in range(9):
    a.append(int(mp.floor(z))); z = 1 / (z - mp.floor(z))
dens = []; h0, h1 = 0, 1
k0, k1 = 1, 0
for ai in a:
    h0, h1 = h1, ai * h1 + h0; k0, k1 = k1, ai * k1 + k0
    dens.append(k1)
e53 = cents(mp.mpf(2) ** (mp.mpf(31) / 53)) - cents(mp.mpf(3) / 2)
# transposition: a set of 12 pitch classes (log2, mod 1) invariant under the shift by its own step is equally spaced
L = [mp.mpf(i) / 12 for i in range(12)]
# concert pitch: scale by k, intervals unchanged
scale = [mp.mpf(2) ** (mp.mpf(i) / 12) for i in range(13)]
moved = max(abs(cents(scale[i] * kk / (scale[0] * kk)) - cents(scale[i] / scale[0])) for kk in (mp.mpf(415) / 440, mp.mpf(435) / 440) for i in range(13))
baroque = 440 * mp.mpf(2) ** (mp.mpf(-1) / 12)
print('M4 (a) modes give p/q whatever f1:', m4a)
print('   (b) 3^k != 2^m (k<200):', no_close, '; comma', comma, mp.nstr(c_comma, 6), 'cents')
print('   (c) 12-ET fifth', mp.nstr(et5, 5), 'major third', mp.nstr(et3, 5), 'minor third', mp.nstr(etm3, 5),
      '; convergent denominators', dens, '; 53-ET fifth', mp.nstr(e53, 4))
print('   (d) intervals moved by a new A:', mp.nstr(moved, 3), '; 440*2^(-1/12) =', mp.nstr(baroque, 7))
ok['M4'] = m4a and no_close and comma == sp.Rational(531441, 524288) and abs(c_comma - mp.mpf('23.460')) < 5e-4 \
    and abs(et5 + mp.mpf('1.955')) < 5e-4 and abs(et3 - mp.mpf('13.686')) < 5e-4 and abs(etm3 + mp.mpf('15.641')) < 5e-4 \
    and sorted(set(dens[:8])) == [1, 2, 5, 12, 41, 53, 306] and abs(e53 + mp.mpf('0.068')) < 5e-4 and moved < 1e-40 \
    and abs(baroque - mp.mpf('415.305')) < 5e-4

# ---------------- threads ----------------
t = rd('ISO_metric_screw_thread')
c1 = mp.mpf(3) * mp.sqrt(3) / 8; c2 = mp.mpf(5) * mp.sqrt(3) / 8
a_ok = '0.649519' in t and '1.082532' in t and mp.nstr(c1, 6) == '0.649519' and mp.nstr(c2, 7) == '1.082532'
tab = t.split('ISO 262 selected sizes')[1].split('|}')[0]
rows = re.findall(r'\|\s*([0-9.]+)\s*\|\|\s*(R10|R20)\s*\|\|\s*([0-9.]+)', tab)
first = sorted([(float(d), float(p)) for d, s, p in rows if s == 'R10'])
X = [math.log(d) for d, p in first]; Y = [math.log(p) for d, p in first]
mx = sum(X) / len(X); my = sum(Y) / len(Y)
slope = sum((u - mx) * (v - my) for u, v in zip(X, Y)) / sum((u - mx) ** 2 for u in X)
ratios = [p / d for d, p in first]
print('M5 (a) 3sqrt3/8 =', mp.nstr(c1, 8), ' 5sqrt3/8 =', mp.nstr(c2, 8), ' as listed:', a_ok)
print('   (b) first choice', len(first), 'sizes', first[0], '…', first[-1], '; P/D', round(ratios[0], 3), '…', round(ratios[-1], 4),
      '; fitted P ~ D^a, a =', round(slope, 4))
ok['M5'] = a_ok and ratios[0] == 0.25 and ratios[-1] < 0.1 and 0.6 <= slope <= 0.9 and abs(slope - 1) > 0.05

print()
for k, v in ok.items(): print(k, 'not killed' if v else 'KILLED')
