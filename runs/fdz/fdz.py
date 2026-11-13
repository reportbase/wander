"""FDZ Part A: depth stored as a renderer stores it. See plans/fdz-plan.md (predictions fixed there first).
r(d) = width of the stored cell containing d, as Δd/d, exact (mpmath 50 digits; binary32 neighbours by IEEE next-after;
float64 -> float32 rounding is correct since 53 >= 2*24 + 2). Run: python3 -I runs/fdz/fdz.py
"""
import numpy as np
from mpmath import mp, mpf, tan, atan, exp, log, pi, sinh, asinh, acosh, cosh
mp.dps = 50
f = mpf(1); n32 = mpf('1e-6'); n16 = mpf('1e-3'); far16 = mpf('1e3')

def f32cell(v):  # stored value and its cell [lo, hi] in value space
    s = np.float32(float(v)); a = np.nextafter(s, np.float32(-np.inf)); b = np.nextafter(s, np.float32(np.inf))
    return (mpf(float(a)) + mpf(float(s))) / 2, (mpf(float(s)) + mpf(float(b))) / 2

SCH32 = {  # name: (forward x -> value, inverse value -> x)
 'RZ32': (lambda x: n32 / (x * f), lambda w: n32 / w),
 'T32': (lambda x: 2 / pi * atan(x), lambda g: tan(pi * g / 2)),
 'C32': (lambda x: (x - 1) / (x + 1), lambda q: (1 + q) / (1 - q)),
 'S32': (lambda x: 1 / x - 1, lambda z: 1 / (z + 1)),
}
def r32(name, x):
    F, Fi = SCH32[name]; lo, hi = f32cell(F(x)); a, b = sorted([Fi(lo), Fi(hi)]); return (b - a) / x

def r16(name, x):
    d = x * f; K = 2 ** 16
    if name == 'Z16':
        F = lambda d: (1 / n16 - 1 / d) / (1 / n16 - 1 / far16); Fi = lambda w: 1 / (1 / n16 - w * (1 / n16 - 1 / far16))
    elif name == 'L16':
        F = lambda d: log(d / n16) / log(far16 / n16); Fi = lambda w: n16 * exp(w * log(far16 / n16))
    else:
        F = lambda d: 2 / pi * atan(d / f); Fi = lambda g: f * tan(pi * g / 2)
    k = mp.floor(F(d) * K); a, b = sorted([Fi(k / K), Fi((k + 1) / K)]); return (b - a) / d

U = [mpf(u) / 8 for u in range(-120, 121)]   # u from -15 to 15 in eighths
xs = [exp(u) for u in U]
lo24, hi23 = mpf(2) ** -24, mpf(2) ** -23
out = []
def say(s): print(s); out.append(s)

# F1
xs1 = [exp(mpf(u) / 4) for u in range(int(-11.5 * 4), int(13.8 * 4) + 1)]
bad = [x for x in xs1 if not (lo24 * 0.99 <= r32('RZ32', x) <= hi23 * 1.01)]
rr = [r32('RZ32', x) for x in xs1]
say(f"F1 RZ32: r from {float(min(rr)):.3e} to {float(max(rr)):.3e} over d/f 1e-5..1e6; outside (2^-24, 2^-23]: {len(bad)} -> {'KILLED' if bad else 'not killed'}")
# F2
rf = r32('T32', mpf(1)); fine24 = [x for x in xs if r32('T32', x) < lo24 * 0.99]; fine23 = [x for x in xs if x >= 1 and r32('T32', x) < hi23 * 0.99]
ok2 = abs(rf / (pi * lo24) - 1) < 0.01 and not fine24 and not fine23
say(f"F2 T32: r at focus {float(rf):.4e} (pred {float(pi*lo24):.4e}); finer than 2^-24 anywhere: {len(fine24)}; finer than 2^-23 at d>=f: {len(fine23)} -> {'not killed' if ok2 else 'KILLED'}")
for x in [mpf('1e-3'), mpf('0.1'), mpf(1), mpf(10), mpf(1000)]:
    say(f"    T32 at d/f {float(x):g}: r {float(r32('T32', x)):.3e}   RZ32 {float(r32('RZ32', x)):.3e}")
# F3
viol3 = []
for u, x in zip(U, xs):
    if abs(u) < mpf('1e-3'): continue
    r = r32('C32', x); lo = sinh(abs(u)) * lo24 * mpf('0.99'); hi = sinh(abs(u)) * hi23 * mpf('1.01')
    if not (lo <= r <= hi): viol3.append((float(u), float(r / (sinh(abs(u)) * lo24))))
def merge_u(sign):
    a, b = mpf(10), mpf(25)
    for _ in range(200):
        m = (a + b) / 2; q = (exp(sign * m) - 1) / (exp(sign * m) + 1)
        if abs(float(np.float32(float(q)))) == 1.0: b = m
        else: a = m
    return a
mf, mn = merge_u(1), merge_u(-1)
small = [mpf(10) ** -k for k in (3, 6, 10, 20, 30)]
apart = all(np.float32(float((1 + e - 1) / (1 + e + 1))) != np.float32(float((1 - e - 1) / (1 - e + 1))) for e in small)
ok3 = not viol3 and abs(mf - 26 * log(2)) < 0.1 and abs(mn - 26 * log(2)) < 0.1 and apart
say(f"F3 C32: points outside (sinh|u|·2^-24, sinh|u|·2^-23] by >1%: {len(viol3)} {viol3[:6]}; merge far at u={float(mf):.3f}, near at u={-float(mn):.3f} (pred ±18.022); pair f(1±ε) apart down to ε=1e-30: {apart} -> {'not killed' if ok3 else 'KILLED'}")
for u in [mpf('0.01'), mpf('0.1'), mpf('0.3'), mpf('0.48'), mpf('1'), mpf('1.44'), mpf(3), mpf(5), mpf(10)]:
    x = exp(u); say(f"    C32 at u {float(u):+.2f} (d/f {float(x):.3g}): r {float(r32('C32', x)):.3e}; u {-float(u):+.2f}: {float(r32('C32', 1/x)):.3e};   RZ32 {float(r32('RZ32', x)):.3e}")
# F4
viol4 = []
for u, x in zip(U, xs):
    if abs(u) < mpf('1e-3'): continue
    r = r32('S32', x); lo = abs(1 - x) * lo24 * mpf('0.99'); hi = abs(1 - x) * hi23 * mpf('1.01')
    if not (lo <= r <= hi): viol4.append((float(u), float(r / (abs(1 - x) * lo24))))
say(f"F4 S32: points outside (|1-x|·2^-24, |1-x|·2^-23] by >1%: {len(viol4)} {viol4[:6]} -> {'KILLED' if viol4 else 'not killed'}")
for x in [mpf('1e-4'), mpf('0.5'), mpf('0.9'), mpf('1.1'), mpf('1.5'), mpf(3), mpf(100)]:
    say(f"    S32 at d/f {float(x):g}: r {float(r32('S32', x)):.3e}   RZ32 {float(r32('RZ32', x)):.3e}")
# F5
t, l, z = r16('T16', mpf(1)), r16('L16', mpf(1)), r16('Z16', mpf(1))
pt, pl, pz = pi * mpf(2) ** -16, log(mpf(10) ** 6) * mpf(2) ** -16, mpf('1.5258773803710938e-2')
a, b = mpf(0), mpf(5)   # band edge on the far side, where T16 = L16
g = lambda u: r16('T16', exp(u)) - r16('L16', exp(u))
for _ in range(60):
    m = (a + b) / 2
    if g(m) < 0: a = m
    else: b = m
edge = a; pe = acosh(log(mpf(10) ** 6) / pi)
ok5 = all(abs(v / p - 1) < 0.02 for v, p in [(t, pt), (l, pl), (z, pz)]) and abs(edge - pe) < 0.05
say(f"F5 16-bit at focus: T16 {float(t):.4e} (pred {float(pt):.4e}), L16 {float(l):.4e} (pred {float(pl):.4e}), Z16 {float(z):.4e} (pred {float(pz):.4e}); L16/T16 {float(l/t):.2f}, Z16/T16 {float(z/t):.0f}; band edge u={float(edge):.3f} (pred {float(pe):.3f}) -> {'not killed' if ok5 else 'KILLED'}")
for x in [mpf('0.01'), mpf('0.1'), mpf(1), mpf(10), mpf(100)]:
    say(f"    d/f {float(x):g}: Z16 {float(r16('Z16', x)):.3e}  L16 {float(r16('L16', x)):.3e}  T16 {float(r16('T16', x)):.3e}")
open('runs/fdz/run1.txt', 'w').write('\n'.join(out) + '\n')
