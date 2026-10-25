"""FOV run 1: fidelity at the focus, only enough in the fields (plans/fov-plan.md). Exact where it can be."""
from fractions import Fraction as Fr
from mpmath import mp, log, tan, pi, ceil
from mpmath import mpf as _mpf
mp.dps = 40
def mpf(x):
    return _mpf(x.numerator) / x.denominator if isinstance(x, Fr) else _mpf(x)
out = []
def say(s): print(s); out.append(s)

def reach(a, F, d, r):
    # the farthest end of a cell starting at a: width <= d while the cell touches the focus, ratio <= r past it
    return r * a if a >= F else a + d

def greedy(F, X, d, r):
    a, cells = Fr(0), []
    while a < X:
        b = min(reach(a, F, d, r), X); cells.append((a, b)); a = b
    return cells

def dp(F, X, d, r, g):
    n = int(X / g); INF = 10**9; best = [INF] * (n + 1); best[0] = 0
    for i in range(n):
        if best[i] == INF: continue
        a = i * g; jmax = min(n, int(reach(a, F, d, r) / g))
        for j in range(i + 1, jmax + 1):
            if best[i] + 1 < best[j]: best[j] = best[i] + 1
    return best[n]

def formula(F, X, d, r):
    return int(ceil(mpf(F / d))) + int(ceil(log(mpf(X) / mpf(F)) / log(mpf(r)) - mpf(10)**-30))

say("F1  the fewest cells: greedy against a grid DP and the formula")
ok1 = True
for X in (Fr(16), Fr(90)):
    for d in (Fr(1, 8), Fr(1, 16)):
        for r in (Fr(2), Fr(3, 2)):
            F = Fr(1); gr = len(greedy(F, X, d, r)); fo = formula(F, X, d, r)
            g = d / 4 if X == 16 else d / 2
            dpn = dp(F, X, d, r, g)
            beat = dpn < gr; ok1 &= (not beat) and gr == fo
            say(f"    X={X} δ={d} ρ={r}: greedy {gr}, formula {fo}, grid DP (step {g}) {dpn}{'  <-- DP beats greedy' if beat else ''}")

say("F2  K fixed: the best δ, the switch, the field's count (ρ = 2)")
ok2 = True
for XF in (64, 90):
    for K in (64, 256):
        field = int(ceil(log(mpf(XF)) / log(mpf(2)) - mpf(10)**-30))
        d = Fr(1, K - field)                       # F = 1
        cells = greedy(Fr(1), Fr(XF), d, Fr(2))
        focus = [c for c in cells if c[1] <= 1]; rest = [c for c in cells if c[0] >= 1]
        switch = rest[0][0]; total = len(cells)
        ok2 &= (total == K and switch == 1 and len(rest) == field)
        say(f"    X/F={XF} K={K}: field {len(rest)} cells (predicted {field}), focus {len(focus)} cells of δ = F/{K - field}, "
            f"switch at {switch}·F, total {total}")
    # a smaller δ needs more than K
d58 = Fr(1, 59); say(f"    one address fewer in the field is impossible: δ = F/59 at X/F = 64 needs {len(greedy(Fr(1), Fr(64), d58, Fr(2)))} > 64")

say("F3  grain matched at the corner (ρ = 1 + δ/F): the reader's lay")
ok3 = True
for n in (8, 32, 128):
    for XF in (16, 64, 90):
        fieldc = int(ceil(log(mpf(XF)) / log(1 + mpf(1) / n) - mpf(10)**-30))
        target = n * log(mpf(XF)); bound = log(mpf(XF)) / 2 + 1
        dev = fieldc - target; ok3 &= abs(dev) <= bound
        say(f"    n={n} X/F={XF}: field {fieldc} cells, n·ln(X/F) = {float(target):.2f}, off {float(dev):+.2f} (bound {float(bound):.2f})")

say("F4  the turn with its corner at F, K = 64, X/F = 64")
K = 64; bnd = [tan(k * pi / (2 * K)) for k in range(K)] + [mp.inf]
focus_widths = [bnd[k + 1] - bnd[k] for k in range(K) if bnd[k + 1] <= 1 + mpf(10)**-30]
wid = max(focus_widths); dopt = mpf(1) / (K - 6); ratio = wid / dopt
viol = [k for k in range(K - 1) if bnd[k] >= 1 and bnd[k + 1] / bnd[k] > 2 and bnd[k] < 64]
first = viol[0] if viol else None
ok4 = (mpf('2.7') <= ratio <= mpf('3.0')) and first is not None
say(f"    widest focus cell {float(wid):.5f} F against the optimum δ = F/58 = {float(dopt):.5f} F: ratio {float(ratio):.3f} "
    f"(π(K−6)/K = {float(pi * (K - 6) / K):.3f}); at the centre {float((bnd[1]-bnd[0])/dopt):.3f}")
if first is not None:
    say(f"    factor 2 first broken at the cell from s = {float(bnd[first]):.2f} to {float(bnd[first+1]):.2f} "
        f"(predicted near 2K/π = {float(2*K/pi):.1f}); {len(viol)} cells below s = 64 break it")
say("")
for name, ok in (("F1", ok1), ("F2", ok2), ("F3", ok3), ("F4", ok4)):
    say(f"{name}: {'not killed' if ok else 'KILLED'}")
open('runs/fov/fov.txt', 'w').write('\n'.join(out) + '\n')
