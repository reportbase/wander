"""HMX run 1 (plans/hmx-plan.md): the payload Gaussian, the address Cauchy. mpmath, 30 digits.
Run: python3 runs/hmx/hmx.py
"""
from mpmath import mp, mpf, exp, sqrt, pi, cos, sin, atan, quad, inf, log, gamma, npdf, ncdf, findroot, fabs, mpf as F
mp.dps = 30
verdict = {}
# P1
laws = {'normal': lambda x: exp(-x * x / 2) / sqrt(2 * pi), 'Laplace': lambda x: exp(-abs(x)) / 2,
        'uniform': lambda x: mpf(1) / 2 if abs(x) <= 1 else mpf(0),
        't3': lambda x: gamma(2) / (sqrt(3 * pi) * gamma(mpf(3) / 2)) * (1 + x * x / 3) ** -2}
spread = {}
for k, f in laws.items():
    vals = [f(cos(pi * j / 16 + mpf('0.1'))) * f(sin(pi * j / 16 + mpf('0.1'))) for j in range(8)]
    spread[k] = max(vals) - min(vals)
    print(f"P1 {k}: variation of f(x)f(y) on the unit circle over 8 directions {mp.nstr(spread[k], 5)}")
verdict['P1'] = spread['normal'] <= mpf(10) ** -25 and all(spread[k] >= mpf(10) ** -3 for k in ('Laplace', 'uniform', 't3'))
# P2: s = |Y|/|X|, X ~ N(0, sh), Y ~ N(0, sv)
def cdf_ratio(r, sh, sv, mh=0, mv=0):
    # P(|Y| <= r|X|) = ∫ p_X(x) P(|Y| <= r|x|) dx
    return quad(lambda x: npdf(x, mh, sh) * (ncdf(r * abs(x), mv, sv) - ncdf(-r * abs(x), mv, sv)), [-inf, mh, inf])
worst = 0
for sh, sv in ((1, 1), (1, 2), (3, 1)):
    for r in (mpf(1) / 4, mpf(1), mpf(4)):
        worst = max(worst, fabs(cdf_ratio(r, sh, sv) - 2 / pi * atan(r * sh / sv)))
    print(f"P2 σh={sh}, σv={sv}: median σv/σh = {sv/sh}; P(s ≤ σv/σh) = {mp.nstr(cdf_ratio(mpf(sv)/sh, sh, sv), 12)}")
print(f"P2 worst gap from (2/π)·arctan(r σh/σv): {mp.nstr(worst, 5)}")
verdict['P2'] = worst <= mpf(10) ** -20
# P3: joint of R and θ on the quadrant (|X|, |Y|)
def joint(a, t, sh, sv):
    # 4 × ∫_0^t ∫_0^a p(ρcosφ)p(ρsinφ) ρ dρ dφ  over the first quadrant
    return 4 * quad(lambda ph: quad(lambda rho: npdf(rho * cos(ph), 0, sh) * npdf(rho * sin(ph), 0, sv) * rho, [0, a]), [0, t])
d_eq, d_un = [], []
for a, t in ((mpf('0.5'), pi / 8), (mpf(1), pi / 4), (mpf(2), 3 * pi / 8)):
    for sh, sv, lst in ((1, 1, d_eq), (1, 2, d_un)):
        J = joint(a, t, sh, sv); PR = joint(a, pi / 2, sh, sv); PT = joint(mpf(60), t, sh, sv)
        lst.append(fabs(J - PR * PT))
    print(f"P3 (a, t) = ({a}, {mp.nstr(t, 4)}): defect equal spreads {mp.nstr(d_eq[-1], 4)}, σv = 2σh {mp.nstr(d_un[-1], 4)}; "
          f"P(θ ≤ t) = {mp.nstr(joint(mpf(60), t, 1, 1), 12)} vs 2t/π = {mp.nstr(2 * t / pi, 12)}")
verdict['P3'] = max(d_eq) <= mpf(10) ** -20 and min(d_un) >= mpf(10) ** -3
# P4: means (0, 1)
med = findroot(lambda r: cdf_ratio(r, 1, 1, 0, 1) - mpf(1) / 2, mpf(2))
gaps = [fabs(cdf_ratio(r, 1, 1, 0, 1) - 2 / pi * atan(r / med)) for r in (mpf(1) / 4, mpf(1) / 2, mpf(2), mpf(4))]
print(f"P4 means (0, 1): median of |Y|/|X| {mp.nstr(med, 10)}; gaps from the half-Cauchy of that median {[mp.nstr(g, 4) for g in gaps]}")
verdict['P4'] = med > 1 and max(gaps) > mpf(10) ** -3
# P5
EX = quad(lambda x: abs(x) * npdf(x), [-inf, 0, inf])
tm = lambda M: quad(lambda s: s * 2 / (pi * (1 + s * s)), [0, 1, M])
c6, c8 = tm(mpf(10) ** 6) - 2 / pi * log(mpf(10) ** 6), tm(mpf(10) ** 8) - 2 / pi * log(mpf(10) ** 8)
print(f"P5 E|X| {mp.nstr(EX, 20)} vs √(2/π) {mp.nstr(sqrt(2 / pi), 20)}; truncated mean − (2/π)ln M at 1e6, 1e8: {mp.nstr(c6, 6)}, {mp.nstr(c8, 6)}")
verdict['P5'] = fabs(EX - sqrt(2 / pi)) <= mpf(10) ** -25 and fabs(c6 - c8) <= mpf(10) ** -6
for k, v in verdict.items(): print(k, 'not killed' if v else 'KILLED')
