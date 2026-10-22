"""RFR run 2: P4'(b) and P5' (plans/rfr-plan.md, predictions written before this script). python3 runs/rfr/rfr2.py"""
import mpmath as mp
mp.mp.dps = 40
pi, R = mp.pi, mp.mpf(1)
out = []
def say(s): print(s); out.append(s)
worst = mp.mpf(0)
for dR in ['1.5', '3', '10']:
    d = mp.mpf(dR)
    P = lambda ph: (d * d - R * R) / (2 * pi * (d * d - 2 * d * R * mp.cos(ph) + R * R))
    for n in range(1, 9):
        cn = mp.quad(lambda ph: P(ph) * mp.cos(n * ph), mp.linspace(0, 2 * pi, 9))
        worst = max(worst, abs(cn - (R / d) ** n))
say(f"P4'(b): {'not killed' if worst < mp.mpf('1e-20') else 'KILLED'}. worst |coefficient - (R/d)^n| {mp.nstr(worst, 3)}")
wa, wb, rows = mp.mpf(0), mp.mpf(0), []
for dR in ['1.01', str(mp.sqrt(2)), '2', '10', '1000']:
    d = mp.mpf(dR); ell = mp.sqrt(d * d - R * R)
    for hR in ['1e-5', '1e-4']:
        h = mp.mpf(hR); da = mp.asin((R + h) / d) - mp.asin(R / d)
        rs = []
        for k in range(3, 10):
            rho = h * 2 ** (k + 1) / (pi * R)
            for K in [64, 512, 4096]:
                eps = pi / (2 * K)
                held_d_ell = pi * R / (2 ** (k + 1) * eps)        # the tangent distance at which octave k is first held
                # the reader stands where l = 2^(k+1) is first held: its shift is measured with its own ell
                rs.append((da * ell / h))
        r0 = rs[0]; wa = max(wa, max(abs(x - r0) for x in rs))
        q = (r0 - 1) / (h * R / (2 * ell ** 2)); wb = max(wb, abs(q - 1))
        rows.append(f"d/R {mp.nstr(d,6)} h/R {hR}: shift/rho - 1 = {mp.nstr(r0 - 1, 5)}, over hR/(2 ell^2) {mp.nstr(q, 6)}")
for r in rows: say("  " + r)
say(f"P5': {'not killed' if wa < mp.mpf('1e-30') and wb < mp.mpf('0.01') else 'KILLED'}. (a) spread over k and K {mp.nstr(wa,3)}; "
    f"(b) worst |ratio to hR/(2 ell^2) - 1| {mp.nstr(wb,3)}")
open('runs/rfr/rfr-run2.txt', 'w').write('\n'.join(out) + '\n')
