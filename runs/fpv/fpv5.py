"""FPV run 5: when to move the focus (plans/fpv-plan.md, run 5). Seeded.
Run from the repository's root: python3 runs/fpv/fpv5.py"""
import math
import numpy as np

ok = True


def say(code, good, note):
    global ok
    ok = ok and good
    print(f"  {'ok  ' if good else 'FAIL'} {code}: {note}")


rng = np.random.default_rng(20261025)
N, p, sig, span = 200_000, 0.05, 0.1, 8.0

# the gaze trace, in levels: a target held a geometric number of looks, then a jump; jitter on every look
jump = rng.random(N) < p
jump[0] = True
tgt = np.empty(N)
cur = 0.0
draws = rng.random(N) * span
for t in range(N):
    if jump[t]:
        cur = draws[t]
    tgt[t] = cur
x = tgt + rng.normal(0, sig, N)


def run(policy):
    c = x[0]; moves = 0; slid = 0.0; g = 0.0; hist = []
    for t in range(N):
        xt = x[t]
        new = policy(c, xt, hist, t)
        if new != c:
            moves += 1; slid += abs(new - c)
        c = new
        g += math.cosh(xt - c)
    return g / N, moves / N, slid / N


def follow(c, xt, hist, t): return xt
def hold(L): return lambda c, xt, hist, t: xt if abs(xt - c) > L else c
def ease(a): return lambda c, xt, hist, t: c + a * (xt - c)
def median(m):
    def f(c, xt, hist, t):
        hist.append(xt)
        if len(hist) > m: hist.pop(0)
        return float(np.median(hist))
    return f


print(f"trace: {N} looks, {int(jump.sum())} jumps, jitter sd {sig}, targets on [0, {span}] nats")
G0, R0, S0 = run(follow)
say("F1", abs(G0 - 1) < 1e-12 and R0 == 1 and abs(S0 - np.mean(np.abs(np.diff(x)))) < 1e-9 * (1 + S0),
    f"follow: G = {G0:.15f}, R = {R0}, S = {S0:.4f} levels a look (the trace's mean step)")

Gh, Rh, Sh = run(hold(0.4))
say("F2", 0.04 <= Rh <= 0.06, f"hold 0.4: R = {Rh:.4f} ({1 / Rh:.1f} times fewer re-lays than follow)")
say("F2", 1.005 <= Gh <= 1.02, f"hold 0.4: G = {Gh:.5f} (e^(sigma^2) = {math.exp(sig ** 2):.5f}); S = {Sh:.4f}")

Ge, Re, Se = run(ease(0.5))
say("F3", Re == 1 and 1.05 <= Ge <= 1.2 and Ge > Gh and Re > Rh, f"ease 0.5: G = {Ge:.4f}, R = {Re}, S = {Se:.4f}; "
    "worse than hold 0.4 on both")

Gm, Rm, Sm = run(median(5))
say("F4", Gm > 2, f"median 5: G = {Gm:.2f}, R = {Rm:.4f}, S = {Sm:.4f}")

print("\n  the frontier (not predicted): hold L for several L")
for L in (0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.0, 1.5):
    G, R, S = run(hold(L))
    print(f"      L = {L:<4}: G = {G:.5f}  R = {R:.4f}  S = {S:.4f}")
for a in (0.25, 0.75):
    G, R, S = run(ease(a))
    print(f"      ease {a}: G = {G:.4f}  R = {R:.4f}")
for m in (3, 9):
    G, R, S = run(median(m))
    print(f"      median {m}: G = {G:.2f}  R = {R:.4f}")

print("\nF5, the one-or-two-corners switch")
one = lambda D: math.cosh(D / 2)                                   # in units of pi/K
two = lambda D: (4 / math.pi) * math.atan(math.exp(D / 2))
lo, hi = 1.0, 3.0
for _ in range(200):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if one(mid) < two(mid) else (lo, mid)
Ds = (lo + hi) / 2
s = math.sinh(Ds / 2) / 2 - (2 / math.pi) * math.exp(Ds / 2) / (1 + math.exp(Ds))
b = 0.25
worst = max(abs(one(D) - two(D)) for D in np.linspace(Ds - b, Ds + b, 2001))
say("F5", abs(worst / (s * b) - 1) < 0.05, f"D* = {Ds:.6f}, s = {s:.4f}; worst in-band loss {worst:.5f} against "
    f"s b = {s * b:.5f} ({100 * (worst / (s * b) - 1):+.2f}%)")
D = np.empty(N); d = Ds
steps = rng.normal(0, 0.05, N)
for t in range(N):
    d += steps[t]
    if d < 1: d = 2 - d
    if d > 3: d = 6 - d
    D[t] = d


def switches(band):
    two_on = D[0] > Ds; n = 0; loss = 0.0
    for d in D:
        if not two_on and d > Ds + band: two_on, n = True, n + 1
        elif two_on and d < Ds - band: two_on, n = False, n + 1
        have = two(d) if two_on else one(d)
        loss += have - min(one(d), two(d))
    return n, loss / N


n0, l0 = switches(0.0)
nb, lb = switches(b)
say("F5", nb * 10 <= n0, f"switches: {n0} with no band, {nb} with b = {b} ({n0 / max(nb, 1):.1f} times fewer); "
    f"mean extra grain {l0:.5f} and {lb:.5f} pi/K")

print("\n" + ("nothing killed" if ok else "KILLED"))
