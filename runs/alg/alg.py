"""ALG run 1 (plans/alg-plan.md): classical algorithms from one standpoint and from none.
Run from the repository's root: python3 runs/alg/alg.py"""
import math, random, sys
sys.set_int_max_str_digits(0)
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp
import sympy as sp

mp.mp.dps = 60
rng = random.Random(20261116)
V = {}

def oplus(s, a):  # tangent addition
    return (s + a) / (1 - s * a)

print("== C. CORDIC ==")
ok1 = True
for _ in range(200):
    n = 24
    x0 = Fr(rng.randint(1, 1000)); y0 = Fr(rng.randint(-1000, 1000))
    sig = [rng.choice((-1, 1)) for _ in range(n)]
    x, y, s = x0, y0, y0 / x0
    good = True
    for i, g in enumerate(sig):
        t = Fr(g, 2 ** i)
        x, y = x - y * t, y + x * t
        if 1 - s * t == 0:
            good = False; break
        s = oplus(s, t)
    if good and x != 0:
        ok1 &= (y / x == s)
print("C1 final y/x equals the composed slope, exactly, in 200 cases:", ok1)
V["C1"] = ok1
ratio_ok = True
for _ in range(50):
    x0, y0 = Fr(rng.randint(1, 99)), Fr(rng.randint(-99, 99)); x, y = x0, y0
    for i in range(24):
        g = rng.choice((-1, 1)); t = Fr(g, 2 ** i); x, y = x - y * t, y + x * t
    prod = 1
    for i in range(24):
        prod *= (1 + Fr(1, 4 ** i))
    ratio_ok &= ((x * x + y * y) / (x0 * x0 + y0 * y0) == prod)
K30 = mp.mpf(1)
for i in range(30):
    K30 /= mp.sqrt(1 + mp.mpf(4) ** (-i))
Kinf = mp.mpf(1)
for i in range(200):
    Kinf /= mp.sqrt(1 + mp.mpf(4) ** (-i))
print("C2 length^2 grows by prod(1 + 4^-i) exactly:", ratio_ok, "  K_30 =", mp.nstr(K30, 12), " K_inf =", mp.nstr(Kinf, 15))
V["C2"] = ratio_ok and abs(K30 - mp.mpf("0.6072529350")) < 1e-10

# C3: rotation mode, sigma by the sign of the angle left (table) against the sign of the slope left (no table)
table = [mp.atan(mp.mpf(2) ** (-i)) for i in range(32)]
same = 0; diffs = []
for trial in range(1000):
    th = mp.mpf(rng.uniform(-1.74, 1.74))
    # angle mode
    z = th; sa = []
    for i in range(32):
        g = 1 if z >= 0 else -1; sa.append(g); z -= g * table[i]
    # slope mode, the letter of the prediction: sign of (T (-) s), T = tan(theta) the target slope
    T = Fr(mp.nstr(mp.tan(th), 50))
    x, y = Fr(1), Fr(0); ss = []
    for i in range(32):
        s = y / x if x != 0 else None
        if s is None or 1 + T * s == 0:
            left = None
        else:
            left = (T - s) / (1 + T * s)
        g = 1 if (left is not None and left >= 0) else -1; ss.append(g)
        t = Fr(g, 2 ** i); x, y = x - y * t, y + x * t
    if ss == sa:
        same += 1
    else:
        diffs.append(float(th))
print(f"C3 (letter: sign of the slope left) sequences equal in {same} of 1000; differing targets |theta| min {min(map(abs, diffs)) if diffs else None}")
V["C3"] = (same == 1000)

# post hoc, not a prediction: the same slope subtraction kept as a pair (dot, cross), as atan2 keeps it
samep = 0
rng2 = random.Random(20261116)
for trial in range(1000):
    th = mp.mpf(rng2.uniform(-1.74, 1.74))
    z = th; sa = []
    for i in range(32):
        g = 1 if z >= 0 else -1; sa.append(g); z -= g * table[i]
    a, b = Fr(mp.nstr(mp.cos(th), 50)), Fr(mp.nstr(mp.sin(th), 50))
    x, y = Fr(1), Fr(0); sp_ = []
    for i in range(32):
        cross = x * b - y * a
        g = 1 if cross >= 0 else -1; sp_.append(g)
        t = Fr(g, 2 ** i); x, y = x - y * t, y + x * t
    samep += (sp_ == sa)
print(f"   post hoc, the slope left kept as a pair (sign of the cross term): equal in {samep} of 1000")

print("== B. Bresenham ==")
rngb = random.Random(7)
segs = []
for _ in range(1000):
    dx = int(round(10 ** rngb.uniform(0.3, 6)))
    dx = max(dx, 2); dy = rngb.randint(0, dx); segs.append((dx, dy))
mis_b = 0; mis_f = 0; checked = 0
for dx, dy in segs:
    xs = set(range(dx + 1)) if dx <= 2000 else set(rngb.sample(range(dx + 1), 2000))
    y = 0; D = 2 * dy - dx
    for x in range(dx + 1):
        if x in xs:
            exact = -((-(2 * dy * x - dx)) // (2 * dx))   # ceil((2 dy x - dx) / (2 dx)) = round half down
            fl = math.ceil((dy / dx) * x - 0.5)
            mis_b += (y != exact); mis_f += (fl != exact); checked += 1
        if D > 0:
            y += 1; D -= 2 * dx
        D += 2 * dy
print(f"B1 Bresenham against the exact line: {mis_b} mismatches in {checked} points; B2 float DDA: {mis_f} mismatches")
V["B1"] = mis_b == 0; V["B2"] = mis_f > 0

print("== T. atan2 against atan ==")
rngt = np.random.default_rng(3)
ang = rngt.uniform(-math.pi, math.pi, 10000)
X, Y = np.cos(ang), np.sin(ang)
t1 = np.all(np.arctan(Y / X) == np.arctan((-Y) / (-X)))
t1b = np.allclose(np.abs(np.arctan2(Y, X) - np.arctan2(-Y, -X)), math.pi)
try:
    1.0 / 0.0; t2a = False
except ZeroDivisionError:
    t2a = True
try:
    Fr(1) / Fr(0); t2b = False
except ZeroDivisionError:
    t2b = True
t2c = math.atan2(1.0, 0.0) == math.pi / 2 and math.atan2(-1.0, 0.0) == -math.pi / 2
print(f"T1 atan gives d and -d the same value: {bool(t1)}; atan2 keeps them pi apart: {bool(t1b)}")
print(f"T2 y/x at x = 0 raises (float {t2a}, exact {t2b}); atan2 gives +-pi/2: {t2c}")
V["T1"] = bool(t1 and t1b); V["T2"] = t2a and t2b and t2c

print("== R. Rotation drift ==")
c, s = Fr(63, 65), Fr(16, 65)
r_ok = True
for n in (10, 100, 1000, 4000):
    x, y = Fr(1), Fr(0)
    for _ in range(n):
        x, y = x * c - y * s, x * s + y * c
    dig = len(str(max(x.denominator, y.denominator)))
    for _ in range(n):
        x, y = x * c + y * s, -x * s + y * c
    err = abs(x - 1) + abs(y)
    pred = n * math.log10(65)
    print(f"   rational n={n}: return error {err}, denominator digits {dig} (n*log10 65 = {pred:.1f})")
    r_ok &= (err == 0) and abs(dig - pred) <= 0.01 * pred + 1
V["R1"] = r_ok
th = 2 * math.atan(1 / 8); cf, sf = math.cos(th), math.sin(th)
errs = {}
for n in (10 ** 3, 10 ** 4, 10 ** 5):
    x, y = 1.0, 0.0
    for _ in range(n):
        x, y = x * cf - y * sf, x * sf + y * cf
    for _ in range(n):
        x, y = x * cf + y * sf, -x * sf + y * cf
    errs[n] = math.hypot(x - 1, y)
print("R2 float return error:", {k: f"{v:.3e}" for k, v in errs.items()})
V["R2"] = all(v > 0 for v in errs.values()) and errs[10 ** 5] > errs[10 ** 3]

print("== M. Median and mean under increasing maps ==")
rngm = np.random.default_rng(11)
Xm = rngm.standard_normal(1001)
maps = {"x^3": lambda v: v ** 3, "e^x": np.exp, "ln(x+10)": lambda v: np.log(v + 10)}
m1 = True; m2 = True
for k, f in maps.items():
    a = np.median(f(Xm)); b = f(np.median(Xm))
    mu1 = np.mean(f(Xm)); mu2 = f(np.mean(Xm))
    rel = abs(mu1 - mu2) / abs(mu1)
    print(f"   {k}: median(f) == f(median) {a == b}; mean(f) vs f(mean) relative gap {rel:.3e}")
    m1 &= bool(a == b); m2 &= rel > 1e-6
V["M1"] = m1; V["M2"] = m2

print("== I. Inverse depth ==")
import warnings; warnings.filterwarnings("ignore")
u = np.array([0.36, 0.48, 0.8])  # a unit direction, exactly representable ratios 9:12:20 over 25
B = np.array([1.0, 0.0, 0.0])
i1 = True; i2 = True
for label, d, rho in (("1e300", 1e300, Fr(1, 10 ** 300)), ("1e310", float("1e310"), Fr(1, 10 ** 310)), ("inf", math.inf, Fr(0))):
    P = d * u
    nrm = P / np.linalg.norm(P)
    xyz_nan = bool(np.any(np.isnan(nrm)))
    uf = [Fr(9, 25), Fr(12, 25), Fr(20, 25)]
    bear = [uf[0] - rho, uf[1], uf[2]]            # u - rho*B, B along x
    bear_f = np.array([float(b) for b in bear]); bear_f /= np.linalg.norm(bear_f)
    Pb = P - B; nb = Pb / np.linalg.norm(Pb); xyz2_nan = bool(np.any(np.isnan(nb)))
    print(f"   d={label}: xyz direction NaN {xyz_nan}; second camera xyz NaN {xyz2_nan}; inverse-depth bearing {np.round(bear_f, 6)}, rho = {float(rho)}")
    if label != "1e300":
        i1 &= xyz_nan and (rho == 0 or rho > 0)
        i2 &= xyz2_nan and np.allclose(bear_f, u, atol=1e-15)
V["I1"] = i1; V["I2"] = i2

print("== F. Median and mean filters on Cauchy noise ==")
rngf = np.random.default_rng(5)
Z = rngf.standard_cauchy(200000)
W = Z.reshape(-1, 25)
iqr = lambda a: np.subtract(*np.percentile(a, [75, 25]))
raw = iqr(Z); mean_r = iqr(W.mean(1)) / raw; med_r = iqr(np.median(W, 1)) / raw
print(f"F1 mean filter IQR / raw = {mean_r:.3f} (predicted within 10% of 1); F2 median filter = {med_r:.3f} (predicted 0.212 within 15%)")
V["F1"] = abs(mean_r - 1) <= 0.10; V["F2"] = abs(med_r - 0.212) <= 0.15 * 0.212

print("== N. Roots of unity ==")
cos_rat, both_rat = [], []
for N in range(1, 65):
    c = sp.cos(2 * sp.pi / N); s_ = sp.sin(2 * sp.pi / N)
    x = sp.Symbol("x")
    dc = sp.degree(sp.minimal_polynomial(c, x), x); ds = sp.degree(sp.minimal_polynomial(s_, x), x)
    if dc == 1: cos_rat.append(N)
    if dc == 1 and ds == 1: both_rat.append(N)
print("N1 cos(2pi/N) rational for N =", cos_rat, "; cos and sin both rational for N =", both_rat)
V["N1"] = cos_rat == [1, 2, 3, 4, 6] and both_rat == [1, 2, 4]

print("== verdicts ==")
for k, v in V.items():
    print(f"  {k}: {'not killed' if v else 'KILLED'}")
