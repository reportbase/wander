"""squeeze.py: three ways to squeeze the reader's line into K addresses (OFS §8, "Two readers, one K"; SPN R413).

Tom, 21 Oct 2026: "how does this other method achieve the same thing?", then "Yes, add the three-path table. do these other
methods also support being recombined and swept. the cauchy is unique because once a cauchy always a cauchy, and that
means it can be swept, without visual distortion. does the other methods also have this cauchy property?"

The three paths of OFS §11.2 question 2, each swept uniformly along its own length, give a law for the signed reading
s = v/h on the whole line (the four quadrants alike):
  circle  (the turn)          f_C(s) = 1/(π(1 + s²))                        the Cauchy
  line    |h| + |v| = 1       f_L(s) = ½·(1 + |s|)^(−2)                     the share s/(1 + s) on each side
  square  max(|h|, |v|) = 1   f_Q(s) = ¼ for |s| ≤ 1, 1/(4s²) past it       the in-place lay 2 − 1/s, halved
With H the zoom (s = d/H) and K addresses at equal shares of the sweep on s ≥ 0.

Predictions, written before running (Claude):
  S1  Reach: the last address starts at cot(π/2K)·H (circle), (K − 1)·H (line), (K/2)·H (square); the share past s is
      c/s far out with c = 2/π, 1, ½, so each reach is about c·K·H. Exact.
  S2  Each is unchanged by s → 1/s on s > 0 (F(1/s) = 1 − F(s), median at s = 1, K/2 addresses either side of H). Exact.
  S3  Swept again from a new zero (a turn α, s → tan(θ + α)): the Cauchy's law is unchanged (0 to the working
      precision); the line's and the square's leave their own location-scale family. Kolmogorov distance to the
      family's nearest member at α = 30°: above 10⁻³ for both.
  S4  Recombined (the sum of two independent readings): the Cauchy's sum is the Cauchy at scale 2, exactly; the line's
      and the square's sums are not in their own family: the characteristic function φ(t)² differs from every φ(γt) by
      more than 10⁻³ somewhere.
  S5  Recombined many times, (S₁ + … + Sₙ)/n tends to a Cauchy for all three (each tail is c/|s|, Lévy's domain of
      index 1), of scale γ = πc/2·(each side's share) …: circle 1, line π/2, square π/4; the characteristic function's
      gap at n = 10⁶ under 10⁻⁴.

Run 1 (21 Oct): S1–S4 not killed; S5 killed by my set-up. The test asked every gap to shrink from n = 10² to 10⁶, but
the circle is a Cauchy already, so its gap is rounding (10⁻³⁰ to 10⁻²⁶ at 30 digits) and cannot shrink. The line's and
the square's gaps shrink, to 2.7·10⁻⁶ and 1.2·10⁻⁷ at n = 10⁶, both under 10⁻⁴, at scales π/2 and π/4. Output in squeeze.out.
"""
import mpmath as mp
import numpy as np
from scipy.optimize import minimize
from scipy.integrate import quad

mp.mp.dps = 30
PI = np.pi


# the three laws on the whole line
def f_C(s): return 1 / (PI * (1 + s * s))
def f_L(s): return 0.5 / (1 + abs(s)) ** 2
def f_Q(s): return 0.25 if abs(s) <= 1 else 0.25 / (s * s)
def F_C(s): return 0.5 + np.arctan(s) / PI
def F_L(s): return 0.5 + 0.5 * np.sign(s) * (abs(s) / (1 + abs(s)))
def F_Q(s):
    a = abs(s); half = 0.25 * a if a <= 1 else 0.5 - 0.25 / a
    return 0.5 + np.sign(s) * half
LAWS = {'circle': (f_C, F_C), 'line': (f_L, F_L), 'square': (f_Q, F_Q)}

print('S1  reach of K addresses on s ≥ 0, and the tail constant c (share past s → c/s; on s ≥ 0 alone, 2·(1 − F))')
def reach(name, K):
    if name == 'circle': return mp.cot(mp.pi / (2 * K))
    if name == 'line': return mp.mpf(K - 1)                      # s/(1 + s) = 1 − 1/K
    return mp.mpf(K) / 2                                         # 1 − 1/(2s) = 1 − 1/K
for name in LAWS:
    F = LAWS[name][1]
    c = 2 * (1 - F(1e9)) * 1e9
    print(f'    {name:7s} c = {c:.6f}', ' '.join(f'K={K}: {float(reach(name, K)):.4f} H ({float(reach(name, K)) / K:.4f}·K·H)' for K in (32, 512, 2048)))
    for K in (32, 512, 2048):                                     # the last boundary holds exactly 1/K past it (on s ≥ 0)
        r = float(reach(name, K)); assert abs(2 * (1 - F(r)) - 1 / K) < 1e-12, (name, K)
S1 = True
print('    each last address holds exactly 1/K of the sweep: yes')

print('S2  reciprocal symmetry F(1/s) = 1 − F(s) on s > 0 (here F on s ≥ 0, G = 2F − 1)')
dev = {}
for name in LAWS:
    F = LAWS[name][1]; G = lambda s: 2 * F(s) - 1
    dev[name] = max(abs(G(1 / s) - (1 - G(s))) for s in np.geomspace(1e-6, 1e6, 2001))
    print(f'    {name:7s} max |G(1/s) − (1 − G(s))| = {dev[name]:.1e}, median {[s for s in (0.999999, 1, 1.000001) if True] and "at 1" if abs(G(1) - 0.5) < 1e-15 else G(1)}')
S2 = all(d < 1e-12 for d in dev.values())


# S3: sweep again from a new zero, a turn α: s' = tan(θ + α) = (s + τ)/(1 − sτ)
def turned_cdf(F, tau):
    # P(S' ≤ x): S' = (S + τ)/(1 − Sτ). The map is increasing in s on each side of its pole s = 1/τ, jumping from +∞ to −∞.
    def G(x):
        s_x = (x - tau) / (1 + x * tau)                          # the preimage of x
        p_pole = F(1 / tau)                                      # P(S < 1/τ)
        # S' ≤ x  ⇔  (S < 1/τ and S ≤ s_x) or (S > 1/τ and S ≤ s_x), with s_x on the right branch when x < −1/τ … handle by cases
        if x >= -1 / tau:                                        # s_x lies below the pole: S in (−∞, s_x] on the left branch, plus all of S > 1/τ
            return F(s_x) + (1 - p_pole)
        return F(s_x) - p_pole                                   # s_x above the pole: only S in (1/τ, s_x]
    return G

def ks_to_family(Fbase, G, xs):
    Gx = np.array([G(x) for x in xs])
    def loss(p):
        m, lg = p; g = np.exp(lg)
        return max(abs(Gx[i] - Fbase((x - m) / g)) for i, x in enumerate(xs))
    best = None
    for m0 in (-1, -0.5, 0, 0.5, 1):
        for lg0 in (-0.5, 0, 0.5):
            r = minimize(loss, [m0, lg0], method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 4000})
            if best is None or r.fun < best.fun: best = r
    return best.fun, best.x[0], np.exp(best.x[1])

alpha = PI / 6; tau = np.tan(alpha)
xs = np.concatenate([-np.geomspace(1e3, 1e-3, 150), [0], np.geomspace(1e-3, 1e3, 150)])
print('S3  swept again from a new zero, a turn of 30°: the Kolmogorov distance to the nearest member of the law\'s own location-scale family')
ks3 = {}
for name, (f, F) in LAWS.items():
    G = turned_cdf(F, tau)
    d, m, g = ks_to_family(F, G, xs)
    ks3[name] = d
    print(f'    {name:7s} {d:.3e}  (nearest m = {m:+.4f}, γ = {g:.4f})')
S3 = ks3['circle'] < 1e-8 and ks3['line'] > 1e-3 and ks3['square'] > 1e-3


# S4, S5: recombined. Characteristic functions φ(t) = ∫ cos(ts) f(s) ds (all three symmetric).
def phi(name, t):
    t = mp.mpf(t)
    if t == 0: return mp.mpf(1)
    if name == 'circle': return mp.e ** (-abs(t))
    t = abs(t)
    # ∫₁^∞ cos(tu)/u² du = cos t − t(π/2 − Si t);  ∫₁^∞ sin(tu)/u² du = sin t − t·Ci t  (by parts)
    if name == 'line':   return 1 - t * (mp.cos(t) * (mp.pi / 2 - mp.si(t)) + mp.sin(t) * mp.ci(t))     # u = 1 + s
    return mp.sin(t) / (2 * t) + (mp.cos(t) - t * (mp.pi / 2 - mp.si(t))) / 2                       # ½∫₀¹ + ½∫₁^∞

# the closed forms checked against direct quadrature once
for _t in (0.3, 2.0):
    _l = mp.quadosc(lambda s: mp.cos(_t * s) / (1 + s) ** 2, [0, mp.inf], omega=_t)
    _q = mp.sin(_t) / (2 * _t) + mp.quadosc(lambda s: mp.cos(_t * s) / s ** 2, [1, mp.inf], omega=_t) / 2
    assert abs(_l - phi('line', _t)) < 1e-20 and abs(_q - phi('square', _t)) < 1e-20, (_t, _l, _q)

ts = [mp.mpf(x) for x in (0.05, 0.1, 0.2, 0.4, 0.7, 1, 1.5, 2, 3, 5)]
print('S4  the sum of two independent readings, against the law\'s own family: min over γ of max_t |φ(t)² − φ(γt)|')
gap4 = {}
for name in LAWS:
    p = {t: phi(name, t) for t in ts}
    def loss(lg):
        g = float(np.exp(lg)); return float(max(abs(p[t] ** 2 - phi(name, t * g)) for t in ts))
    best = min((minimize(lambda x: loss(x[0]), [l0], method='Nelder-Mead', options={'xatol': 1e-8, 'fatol': 1e-14}) for l0 in (0.3, 0.69, 1.0)), key=lambda r: r.fun)
    gap4[name] = best.fun
    print(f'    {name:7s} {best.fun:.3e} at γ = {np.exp(best.x[0]):.6f}')
S4 = gap4['circle'] < 1e-12 and gap4['line'] > 1e-3 and gap4['square'] > 1e-3

print('S5  recombined many times: |φ(t/n)^n − e^(−γ|t|)|, max over t, γ = πc/2 for the tail c/|s| of each side together')
gam = {'circle': mp.mpf(1), 'line': mp.pi / 2, 'square': mp.pi / 4}
gap5 = {}
for name in LAWS:
    row = []
    for n in (10 ** 2, 10 ** 4, 10 ** 6):
        row.append(max(abs(phi(name, t / n) ** n - mp.e ** (-gam[name] * t)) for t in ts))
    gap5[name] = row
    print(f'    {name:7s} γ = {float(gam[name]):.6f}: n = 10², 10⁴, 10⁶ gaps', ', '.join(f'{float(x):.2e}' for x in row))
S5 = all(r[-1] < 1e-4 and r[-1] < r[0] for r in gap5.values())

print()
for k, v in (('S1', S1), ('S2', S2), ('S3', S3), ('S4', S4), ('S5', S5)):
    print(k, 'not killed' if v else 'KILLED')
