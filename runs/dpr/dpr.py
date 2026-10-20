"""DPR run 1: depth precision of the papers' lays against the standard depth buffers (plans/dpr-plan.md).
Run from the repository's root: python3 runs/dpr/dpr.py"""
import numpy as np
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 50
n, f = mp.mpf(1), mp.mpf(10) ** 7
STEP = mp.mpf(2) ** -24
DS = [mp.mpf(10) ** k for k in range(8)]
A = f / (f - n)


def fixed(w, winv, d):
    """Relative separation: the depth one 24-bit step farther, over d."""
    return (winv(w(d) + STEP) - d) / d


def Lr(s): return s if s <= 1 else 1 + mp.log(s)
def Lr_inv(u): return u if u <= 1 else mp.e ** (u - 1)
def Li(s): return s if s <= 1 else 2 - 1 / s
def Li_inv(u): return u if u <= 1 else 1 / (2 - u)


def lay(L, Linv, H):
    a, span = L(n / H), L(f / H) - L(n / H)
    return (lambda d: (L(d / H) - a) / span), (lambda w: H * Linv(a + w * span)), span


def rz32(d):
    w0 = np.float32(float(n / d)); w1 = np.nextafter(w0, np.float32(0))
    d0, d1 = n / mp.mpf(Fraction(float(w0))), n / mp.mpf(Fraction(float(w1)))
    return (d1 - d0) / d0


z24 = (lambda d: A * (1 - n / d), lambda w: n / (1 - w / A))
log24 = (lambda d: mp.log(d / n) / mp.log(f / n), lambda w: n * mp.e ** (w * mp.log(f / n)))
Hc = mp.sqrt(n * f)
rlc_w, rlc_inv, span_c = lay(Lr, Lr_inv, Hc)
rln_w, rln_inv, _ = lay(Lr, Lr_inv, n)
ipn_w, ipn_inv, _ = lay(Li, Li_inv, n)

rows = []
print("d (m)      Z24          IP24(n)      RZ32         LOG24        RL24(sqrt nf)  RL24(n)")
for d in DS:
    r = dict(z=fixed(*z24, d), ip=fixed(ipn_w, ipn_inv, d), rz=rz32(d), lg=fixed(*log24, d),
             rc=fixed(rlc_w, rlc_inv, d), rn=fixed(rln_w, rln_inv, d))
    rows.append((d, r))
    print(f"1e{int(mp.log10(d))}       " + "  ".join(mp.nstr(r[k], 5).ljust(11) for k in ('z', 'ip', 'rz', 'lg', 'rc', 'rn')))

near = lambda a, b: abs(a / b - 1) <= mp.mpf('0.01')
d1z = all(near(r['z'], (d / n) * (1 - n / f) * STEP) for d, r in rows)
d1i = all(near(r['ip'], r['z']) for d, r in rows)
worst = max(abs(r['z'] / ((d / n) * (1 - n / f) * STEP) - 1) for d, r in rows)
print(f"\nD1: Z24 against (d/n)(1 - n/f)2^-24, worst {mp.nstr(worst, 4)};  IP24(n) equals Z24 within 1%: {d1i}")
print("D1", "not killed" if (d1z and d1i) else "KILLED")
d2 = all(2 ** -24 < r['rz'] <= 2 ** -23 for d, r in rows)
print("D2 RZ32 in (2^-24, 2^-23] at every d:", "not killed" if d2 else "KILLED")
lg0 = mp.log(f / n) * STEP
d3 = all(near(r['lg'], lg0) for d, r in rows)
print(f"D3 LOG24 = ln(f/n)2^-24 = {mp.nstr(lg0, 4)} within 1%:", "not killed" if d3 else "KILLED")
abs_in = Hc * span_c * STEP; rel_out = span_c * STEP
d4 = all(near(r['rc'] * d, abs_in) if d <= Hc else near(r['rc'], rel_out) for d, r in rows)
print(f"D4 RL24(sqrt nf): span {mp.nstr(span_c, 5)}, inside |dd| = {mp.nstr(abs_in, 4)} m, past r = {mp.nstr(rel_out, 4)};",
      "not killed" if d4 else "KILLED")
d5 = all(near(r['rn'], r['lg']) for d, r in rows)
print("D5 RL24(n) equals LOG24 within 1%:", "not killed" if d5 else "KILLED")

# D6: every exponent of binary32, its first and last mantissa
bad = 0; checked = 0
for e in range(0, 255):
    for m in (0, 1, (1 << 23) - 2, (1 << 23) - 1):
        bits = (e << 23) | m
        if bits == 0: continue
        x = np.array([bits], dtype=np.uint32).view(np.float32)[0]
        y = np.nextafter(x, np.float32(np.inf))
        if not np.isfinite(y): continue
        X, Y = Fraction(float(x)), Fraction(float(y)); sp = Y - X; checked += 1
        if X < Fraction(2) ** -126: ok = sp == Fraction(2) ** -149
        else: ok = Fraction(2) ** -24 < sp / X <= Fraction(2) ** -23
        bad += not ok
print(f"D6 binary32 values checked {checked}, breaking a clause {bad}:", "not killed" if bad == 0 else "KILLED")
print("D7", "not killed" if all((d1z and d1i, d2, d3, d4, d5, bad == 0)) else "KILLED")
