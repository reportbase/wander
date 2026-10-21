"""depends.py: what depends on the weighting (OFS §11.2, "What depends on what"; SPN R416).

ChatGPT, via Tom, 21 Oct 2026: state which conclusions survive a change of the reader's attitude-weighting and which need
reciprocal symmetry, a weight above zero at the horizon, full permutation symmetry, or the uniform turn itself; "every
row should tell the reader not only what survives, but exactly what premise makes it survive."

A weight w(θ) on the quarter turn [0, π/2], the reading x = tan θ (= v/h). Examples, each built to have one condition
and lack another:
  L  lopsided, w ∝ 1 + 2θ/π: not reciprocal-symmetric, above zero at the horizon
  S  sin² 2θ:               reciprocal-symmetric, zero at the horizon
  U  uniform turn:           both
And in three unit relations, P: half the weight on the chamber v₂ > h > v and half on v > h > v₂ (uniform within each),
which has every pair's median at its corner and is not symmetric under all six permutations.

Predictions, written before running (Claude):
  E1  Any weight, the payload changed (each reading's reach ℓ(θ) drawn at random): every reading the same, exactly; the
      readings' ranks unchanged by an increasing map (x ↦ x³ + x). Holds for L, S and U alike.
  E2  The median at the corner (x = 1) for S and U, not for L (L's median above 1).
  E3  The mean: finite for S (4/π exactly), divergent for L and U (the mean of readings below s grows without bound,
      by a fixed amount each tenfold far out: (2/π)·w̃(π/2)·ln 10 with w̃ the normalized weight).
  E4  P: P(v/h ≤ 1) = P(v₂/h ≤ 1) = P(v₂/v ≤ 1) = ½, and P(h largest) = 0; the uniform area: ½, ½, ½ and ⅓.
So the median needs symmetry and not the horizon (S), the missing mean needs the horizon and not symmetry (L), and
1/(n + 1) needs the full permutation group, not the pairs (P).

Run 1 (21 Oct, output depends-run1.out): E1, E2, E4 not killed; E3 killed by my set-up. The divergence is as predicted
(L and U climb, S's mean is 4/π to 30 digits), but between 10³ and 10⁶ L's climb per tenfold is 1.9544048 against the
far-out 1.9544949, off 9·10⁻⁵ against my tolerance of 10⁻⁵: the asymptote has a 1/s correction not yet gone.
Run 2, prediction written before it ran: E3′, the climb per tenfold between 10⁶ and 10⁹ is within 10⁻⁶ of
(2/π)·w̃(π/2)·ln 10 for L and U, and S's mean below 10⁹ within 10⁻⁸ of 4/π.
"""
import random
import mpmath as mp

mp.mp.dps = 40
Q = mp.pi / 2
WEIGHTS = {
    'L (lopsided)': lambda t: 1 + t / Q,
    'S (sin² 2θ)':  lambda t: mp.sin(2 * t) ** 2,
    'U (uniform)':  lambda t: mp.mpf(1),
}

def normed(w):
    Z = mp.quad(w, [0, Q])
    return lambda t: w(t) / Z

print('E1  payload changed, readings and ranks')
rnd = random.Random(7)
thetas = [mp.mpf(rnd.random()) * Q for _ in range(200)]
worst = 0
for t in thetas:
    h, v = mp.cos(t), mp.sin(t)
    for _ in range(3):
        ell = mp.mpf(10) ** rnd.uniform(-12, 12)                   # any reach, any unit
        worst = max(worst, abs((ell * v) / (ell * h) - v / h))
xs = [mp.tan(t) for t in thetas]
f = lambda x: x ** 3 + x
ranks_same = sorted(range(200), key=lambda i: xs[i]) == sorted(range(200), key=lambda i: f(xs[i]))
print(f'    largest change of a reading under a new payload {mp.nstr(worst, 3)}; ranks kept by x³ + x: {ranks_same}')
E1 = worst < mp.mpf(10) ** -30 and ranks_same

print('E2, E3  median and mean of x = tan θ under each weight')
res = {}
for name, w in WEIGHTS.items():
    p = normed(w)
    tm = mp.findroot(lambda t: mp.quad(p, [0, t]) - mp.mpf(1) / 2, Q / 2)
    med = mp.tan(tm)
    # the mean of readings below s, for s = 10³ and 10⁶: θ up to atan s
    part = [mp.quad(lambda t: mp.tan(t) * p(t), [0, mp.atan(10 ** k)]) for k in (3, 6)]
    per_decade = (part[1] - part[0]) / 3
    full = mp.quad(lambda t: mp.tan(t) * p(t), [0, Q]) if name.startswith('S') else None
    res[name] = (med, part, per_decade, full, p(Q))
    print(f'    {name:13s} median {mp.nstr(med, 12):>14s}   mean below 10³, 10⁶: {mp.nstr(part[0], 8)}, {mp.nstr(part[1], 8)}'
          f'   per tenfold {mp.nstr(per_decade, 8)} (predicted (2/π)·w̃(π/2)·ln 10 = {mp.nstr(p(Q) * mp.ln(10), 8)})'
          + (f'   full mean {mp.nstr(full, 15)} (4/π = {mp.nstr(4 / mp.pi, 15)})' if full is not None else ''))
L, S, U = (res[k] for k in WEIGHTS)
E2 = abs(S[0] - 1) < 1e-30 and abs(U[0] - 1) < 1e-30 and L[0] > 1.01
E3 = (abs(S[3] - 4 / mp.pi) < 1e-30 and abs(S[1][1] - S[1][0]) < 1e-5
      and all(abs(r[2] - r[4] * mp.ln(10)) < 1e-5 for r in (L, U)))

print('E4  three unit relations: pairs against the whole permutation group')
# Exact by symmetry of uniform area within a chamber: in the chamber v₂ > h > v every comparison is fixed.
# P: chamber A (v₂ > h > v) and chamber B (v > h > v₂), half each.
def pair_shares(chambers):            # chambers: list of (weight, ordering tuple from largest to smallest)
    def p_le(a, b):                   # P(a ≤ b)
        return sum(w for w, order in chambers if order.index(a) >= order.index(b))
    return p_le('v', 'h'), p_le('v2', 'h'), p_le('v2', 'v'), sum(w for w, order in chambers if order[0] == 'h')
from itertools import permutations
P = [(mp.mpf(1) / 2, ('v2', 'h', 'v')), (mp.mpf(1) / 2, ('v', 'h', 'v2'))]
Uarea = [(mp.mpf(1) / 6, o) for o in permutations(('h', 'v', 'v2'))]     # uniform area: the six chambers equal (5(e))
sp, su = pair_shares(P), pair_shares(Uarea)
print('    P:            P(v ≤ h), P(v₂ ≤ h), P(v₂ ≤ v), P(h largest) =', ', '.join(mp.nstr(x, 6) for x in sp))
print('    uniform area: P(v ≤ h), P(v₂ ≤ h), P(v₂ ≤ v), P(h largest) =', ', '.join(mp.nstr(x, 6) for x in su))
E4 = sp[:3] == (0.5, 0.5, 0.5) and sp[3] == 0 and su[:3] == (0.5, 0.5, 0.5) and abs(su[3] - mp.mpf(1) / 3) < 1e-30

print()
print('E3′ (run 2) the climb per tenfold between 10⁶ and 10⁹')
E3b = True
for name, w in WEIGHTS.items():
    p = normed(w)
    part = [mp.quad(lambda t: mp.tan(t) * p(t), [0, mp.atan(mp.mpf(10) ** k)]) for k in (6, 9)]
    pd = (part[1] - part[0]) / 3
    if name.startswith('S'):
        ok = abs(part[1] - 4 / mp.pi) < 1e-8
        print(f'    {name:13s} mean below 10⁹ {mp.nstr(part[1], 15)} (4/π {mp.nstr(4 / mp.pi, 15)})')
    else:
        ok = abs(pd - p(Q) * mp.ln(10)) < 1e-6
        print(f'    {name:13s} per tenfold {mp.nstr(pd, 12)} (predicted {mp.nstr(p(Q) * mp.ln(10), 12)})')
    E3b = E3b and ok

for k, v in (('E1', E1), ('E2', E2), ('E3', E3), ('E4', E4), ('E3′', E3b)):
    print(k, 'not killed' if v else 'KILLED')
