"""HOL run 2 (plans/hol-plan.md, H8-H10): Leek et al. 2007 (arXiv:0711.0218), Fig. 3A read from the figure.

The points were found by template matching on the figure's raster (fig3.jpg inside fig3.eps, sha256
757794301c182c63904824477ddd693e6bde2b7557f5c8a224396e0542d5ed1c): pixel centres in leek2007-fig3a-points.json
('open' and 'fill' markers). Axes from the figure's own ticks: phase 0, pi, -2pi at rows 513, 364, 810 (a line fitted through them); solid angle
0 and 3pi/4 at columns 170 and 846 (pi/4 at 395). Label areas are dropped; so are points with Theta < 0.3, where the
five series meet and cannot be told apart by marker and sign alone. Series by marker (filled n = 1, open n = 1.5) and
sign; open points within +-0.45 rad of zero are C++. Compared: phi against Omega = 2 n Theta signed by direction
(the text's reading, fixed in the plan before the figure was looked at); C++ against 0.
Errors: the plan's rule, half the smallest tick (pi/2 in phi, pi/8 in Theta), counted; and, reported, not counted,
the paper's own r.m.s. scatter of 0.14 rad."""
import json, os
import numpy as np
from scipy import stats

here = os.path.dirname(__file__)
P = json.load(open(os.path.join(here, 'leek2007-fig3a-points.json')))
labels = [(195, 225, 145, 185), (625, 725, 150, 190), (450, 485, 295, 325), (800, 835, 345, 375),
          (535, 605, 480, 505), (800, 835, 650, 680), (425, 460, 715, 750), (625, 725, 830, 865)]
inlab = lambda x, y: any(a <= x <= b and c <= y <= d for a, b, c, d in labels)
_k, _c = np.polyfit([364, 513, 810], [np.pi, 0, -2 * np.pi], 1)  # a line through the three ticks (np.interp would clamp)
phi_of = lambda y: float(_k * y + _c)
th_of = lambda x: (x - 170) / ((846 - 170) / 3) * np.pi / 4
series = {}
for kind in ('open', 'fill'):
    for x, y, _ in P[kind]:
        if inlab(x, y):
            continue
        t, f = th_of(x), phi_of(y)
        if t < 0.3:
            continue
        if kind == 'fill':
            n, s = 1.0, (1 if f > 0 else -1)
        else:
            n, s = 1.5, (1 if f > 0.45 else -1 if f < -0.45 else 0)
        key = ('C++' if s == 0 else f'n={n:g} ' + ('C-+' if s > 0 else 'C+-'))
        series.setdefault(key, []).append((s * 2 * n * t, f, 2 * n * t))


def wfit(x, y, sy):
    w = 1 / sy ** 2
    A = np.vstack([x, np.ones_like(x)]).T
    cov = np.linalg.inv(A.T @ (A * w[:, None]))
    b, a = cov @ (A.T @ (w * y))
    return b, a, np.sqrt(cov[0, 0]), np.sqrt(cov[1, 1])


SY, STH = np.pi / 2, np.pi / 8
print('H8 per series, phi = slope * Omega + intercept')
chi_rule = chi_emp = 0.0
N = 0
for key in sorted(series):
    arr = np.array(series[key])
    Om, ph, absOm = arr[:, 0], arr[:, 1], arr[:, 2]
    N += len(arr)
    if key == 'C++':
        m, se = ph.mean(), ph.std(ddof=1) / np.sqrt(len(ph))
        print(f'  {key:10s} {len(arr)} points, Omega = 0: mean phi {m:+.3f} (sd {ph.std(ddof=1):.3f}, se {se:.3f}); '
              f'rule error {SY / np.sqrt(len(ph)):.3f}: {abs(m) / (SY / np.sqrt(len(ph))):.2f} sigma; '
              f'by its own scatter {abs(m) / se:.1f} se')
        chi_rule += np.sum((ph / SY) ** 2)
        chi_emp += np.sum((ph / 0.14) ** 2)
        continue
    sy_rule = np.sqrt(SY ** 2 + (2 * (1.5 if '1.5' in key else 1.0) * STH) ** 2)
    b, a, eb, ea = wfit(Om, ph, np.full_like(ph, sy_rule))
    b2, a2, eb2, ea2 = wfit(Om, ph, np.full_like(ph, 0.14))
    print(f'  {key:10s} {len(arr)} points, Omega to {np.abs(Om).max():.2f}: slope {b:.4f} +- {eb:.4f} '
          f'({(b - 1) / eb:+.2f} sigma), intercept {a:+.4f} +- {ea:.4f} ({a / ea:+.2f} sigma) [rule]; '
          f'with 0.14 rad: slope {(b2 - 1) / eb2:+.1f} sigma, intercept {a2 / ea2:+.1f} sigma')
    chi_rule += np.sum(((ph - Om) / sy_rule) ** 2)
    chi_emp += np.sum(((ph - Om) / 0.14) ** 2)
print(f'H9 all {N} points: chi2 {chi_rule:.1f} on {N} (rule errors), p = {stats.chi2.sf(chi_rule, N):.3g}')
print(f'   reported: with the paper\'s 0.14 rad, chi2 {chi_emp:.1f} on {N}, p = {stats.chi2.sf(chi_emp, N):.3g}; '
      f'r.m.s. of phi - Omega {np.sqrt(chi_emp / N) * 0.14:.3f} rad')
allp = np.concatenate([np.array(v) for v in series.values()])
b, a, eb, ea = wfit(allp[:, 0], allp[:, 1], np.full(len(allp), 0.14))
print(f'   one line through all points: slope {b:.4f} +- {eb:.4f}, intercept {a:+.4f} +- {ea:.4f}')
