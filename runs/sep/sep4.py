"""SEP run 4: channels laid by the turn (SPN R1279; plans/sep-plan.md). Run from the root: python3 runs/sep/sep4.py"""
import mpmath as mp
mp.mp.dps = 30
out = []
def say(s): print(s, flush=True); out.append(s)
def pair(d, r):                                     # run 2's pairs: distance d, width ratio r, the same as sep2.py
    g1, g2 = 1 / mp.sqrt(r), mp.sqrt(r)
    dm = mp.sqrt(max(2 * (mp.cosh(d) - 1) - (g1 - g2) ** 2, 0))
    return [mp.mpc(-dm / 2, g1), mp.mpc(dm / 2, g2)]
def C(x, z): m, g = z.real, z.imag; return g / (mp.pi * ((x - m) ** 2 + g ** 2))
def grads(x, z, a):                                  # d/dm, d/dlog g, d/da of a·C
    m, g = z.real, z.imag; D = (x - m) ** 2 + g ** 2
    return [a * 2 * g * (x - m) / (mp.pi * D ** 2), a * (g / (mp.pi * D) - 2 * g ** 3 / (mp.pi * D ** 2)), C(x, z)]
def bound(zs, weight):
    a = [mp.mpf('0.5'), mp.mpf('0.5')]
    def vec(x): return grads(x, zs[0], a[0]) + grads(x, zs[1], a[1])
    def f(x): return a[0] * C(x, zs[0]) + a[1] * C(x, zs[1])
    def w(x): return 1 / f(x) if weight == 'count' else (1 if weight == 'freq' else mp.pi * (1 + x * x))
    I = mp.matrix(6, 6)
    for i in range(6):
        for j in range(i, 6):
            h = lambda t: (lambda x, v: v[i] * v[j] * w(x))(mp.tan(t), vec(mp.tan(t))) / mp.cos(t) ** 2
            I[i, j] = I[j, i] = mp.quad(h, mp.linspace(-mp.pi / 2, mp.pi / 2, 13))
    g = mp.matrix([0, 0, a[1] / (a[0] + a[1]) ** 2, 0, 0, -a[0] / (a[0] + a[1]) ** 2])
    return mp.sqrt((g.T * (I ** -1) * g)[0])
def turn(z, p):  return (mp.cos(p) * z + mp.sin(p)) / (-mp.sin(p) * z + mp.cos(p))
# T1
rho = lambda x: 1 / (mp.pi * (1 + x * x))
xs = [mp.mpf(k) / 3 for k in range(-12, 13)]
worst_turn = 0
for p in (mp.mpf('0.3'), mp.mpf(1), mp.mpf(2)):
    for x in xs:
        if abs(-mp.sin(p) * x + mp.cos(p)) < mp.mpf('1e-3'): continue
        gx = (mp.cos(p) * x + mp.sin(p)) / (-mp.sin(p) * x + mp.cos(p)); gp = 1 / (-mp.sin(p) * x + mp.cos(p)) ** 2
        worst_turn = max(worst_turn, abs(gp * rho(gx) - rho(x)) / rho(x))
worst_other = []
for name, gx, gp in [("translation by 1", lambda x: x + 1, lambda x: 1), ("dilation by 2", lambda x: 2 * x, lambda x: 2)]:
    worst_other.append((name, max(abs(gp(x) * rho(gx(x)) - rho(x)) / rho(x) for x in xs)))
say(f"T1: turns about i, worst relative departure {mp.nstr(worst_turn, 3)}; " + "; ".join(f"{n} {mp.nstr(v, 3)}" for n, v in worst_other))
T1 = worst_turn < 1e-25 and all(v > 1e-3 for _, v in worst_other)
cases = [(d, r) for d in (1.5, 2.0, 3.0) for r in (1, 2, 4)] + [(3.0, 16)]
draws = {1.5: mp.mpf('3.9206025055'), 2.0: mp.mpf('1.90607019581'), 3.0: mp.mpf('0.876654356749')}
B = {}
for wname in ('count', 'freq', 'turn'):
    for d, r in cases:
        B[(wname, d, r)] = bound(pair(mp.mpf(d), mp.mpf(r)), wname)
        say(f"{wname:5s} d = {d}, r = {r:>2}: bound on the split {mp.nstr(B[(wname, d, r)], 15)}")
def spread(wname, d):
    v = [B[(wname, dd, r)] for dd, r in cases if dd == d]; return (max(v) - min(v)) / min(v)
T2 = True
for d in (1.5, 2.0, 3.0):
    s = spread('count', d); dev = abs(B[('count', d, 1)] - draws[d]) / draws[d]
    say(f"counts d = {d}: spread across r {mp.nstr(s, 3)}; against run 2's draws {mp.nstr(dev, 3)}")
    T2 &= s < 1e-20 and dev < 1e-10   # run 2's draws bounds are quoted to 12 digits
for w in ('freq', 'turn'):
    for d in (1.5, 2.0, 3.0): say(f"{w} d = {d}: spread across r {mp.nstr(spread(w, d), 4)}")
T3 = spread('freq', 1.5) > 0.05; T4 = spread('turn', 1.5) > 0.05
base = pair(mp.mpf('1.5'), mp.mpf(1)); T5 = True
bt0, bf0 = bound(base, 'turn'), bound(base, 'freq'); fdev = 0
for p in ('0.3', '1.0', '2.0'):
    zs = [turn(z, mp.mpf(p)) for z in base]
    bt, bf = bound(zs, 'turn'), bound(zs, 'freq')
    dd = mp.acosh(1 + abs(zs[0] - zs[1]) ** 2 / (2 * zs[0].imag * zs[1].imag))
    say(f"turned by {p}: d {mp.nstr(dd, 12)}; turn-laid bound {mp.nstr(bt, 15)} (off {mp.nstr(abs(bt - bt0) / bt0, 3)}); even in frequency {mp.nstr(bf, 8)} (off {mp.nstr(abs(bf - bf0) / bf0, 3)})")
    T5 &= abs(bt - bt0) / bt0 < 1e-20; fdev = max(fdev, abs(bf - bf0) / bf0)
T5 &= fdev > 0.01
for n, v in [("T1", T1), ("T2", T2), ("T3", T3), ("T4", T4), ("T5", T5)]: say(f"{n}: {'not killed' if v else 'KILLED'}")
open('runs/sep/sep4-out.txt', 'w').write('\n'.join(out) + '\n')
