"""Which classical near/far laws are fair to the facings? Checks behind plans/near-far-classification.md.

Each law is written as a reading f(s) on [0, 1], s the thing's own size over the distance (or the ratio the law turns
on), increasing from 0 far away. Fair to the facings: f(s) + f(1/s) = 1 for every s (Proposition 3.2(b)'s condition).

    python3 plans/audit/near_far.py
"""
import math

import numpy as np

S = np.exp(np.linspace(math.log(1e-3), math.log(1e3), 20001))

LAWS = [
    # name, f(s), what s is
    ('glowing disc, on-axis light (share of most)', lambda s: s**2 / (1 + s**2), 'disc radius / distance'),
    ('dipole, magnetic field: near term\'s share of intensity', lambda s: s**2 / (1 + s**2), 'λ/2π / distance'),
    ('first-order filter, power passed above the corner (high-pass)', lambda s: s**2 / (1 + s**2), 'frequency / corner frequency'),
    ('Michaelis–Menten rate, v / Vmax', lambda s: s / (1 + s), 'concentration / K'),
    ('two-state occupancy (Boltzmann)', lambda s: s / (1 + s), 'Boltzmann factor ratio'),
    ('voltage divider, share across R1', lambda s: s / (1 + s), 'R1 / R2'),
    ('Hill equation, n = 4', lambda s: s**4 / (1 + s**4), 'concentration / K'),
    ('angle a segment subtends, share of the half turn', lambda s: (2 / math.pi) * np.arctan(s), 'half-length / distance'),
    ('circular coil, on-axis field', lambda s: s**3 / (1 + s**2) ** 1.5, 'coil radius / distance'),
    ('first-order filter, amplitude passed (high-pass)', lambda s: s / np.sqrt(1 + s**2), 'frequency / corner frequency'),
    ('ring (or Plummer-softened point), potential on axis', lambda s: s / np.sqrt(1 + s**2), 'radius (softening) / distance'),
    ('uniform disc, field on axis; solid angle of a disc / 2π', lambda s: 1 - 1 / np.sqrt(1 + s**2), 'disc radius / distance'),
]


def middle(f):
    lo, hi = 1e-6, 1e6
    for _ in range(200):
        m = math.sqrt(lo * hi)
        lo, hi = (m, hi) if f(m) < 0.5 else (lo, m)
    return m


def main():
    print('A. The criterion: f is fair iff f(eˣ) − ½ is odd in x. Checked on each law below as max |f(s) + f(1/s) − 1|.\n')
    print(f'{"law":62} {"max |f(s)+f(1/s)−1|":>20} {"f(1)":>7} {"f = ½ at s":>11}  kind')
    for name, f, _ in LAWS:
        v = f(S)
        dev = float(np.max(np.abs(v + f(1 / S) - 1)))
        m = middle(lambda s: float(f(np.array([s]))[0]))
        kind = 'fair' if dev < 1e-9 else 'favours ' + ('the near facing' if m < 1 else 'the far facing')
        print(f'{name:62} {dev:20.2e} {float(f(np.array([1.0]))[0]):7.4f} {m:11.4f}  {kind}')

    print('\nB. Powers of s/√(1 + s²) (the coil is n = 3, the disc n = 2): f(s) + f(1/s) at the corner, and where f = ½')
    for n in (1, 2, 3, 4, 6):
        f = lambda s, n=n: s**n / (1 + s * s) ** (n / 2)
        print(f'  n = {n}: f(1) + f(1) = {2 * f(1.0):.4f}; f = ½ at s = {middle(f):.4f}')

    print('\nC. Not of the form at all:')
    peak = lambda s: np.where(s <= 1, s, 1 / s**2)
    print(f'  gravity inside and outside a ball, g/g_surface (s = r/R): peaks at the corner; s for s ≤ 1, s⁻² past it; '
          f'symmetric under the flip? {bool(np.allclose(peak(S), peak(1 / S)))} (exponents 1 and −2)')
    print(f'  a dipole\'s electric intensity s²(s⁴ − s² + 1): bracket palindromic, s⁴P(1/s) = P(s): '
          f'{bool(np.allclose(S**4 * (S**-4 - S**-2 + 1), S**4 - S**2 + 1))}; not a share')
    a = np.linspace(0, 1, 6)
    print(f'  a ball\'s share of the view, (1 − √(1 − s²))/2 for s ≤ 1: ends at contact, s = 1: {np.round((1 - np.sqrt(1 - a**2)) / 2, 4)}')
    print('  the round opening, 4 sin²(πs²/2): oscillates, its last maximum at s = 1 (§3.2)')

    print('\nD. Power against amplitude, first-order filter at the corner frequency:')
    print(f'  power share {0.5:.4f} (the half-power point, fair), amplitude share {1 / math.sqrt(2):.4f} (favours a facing)')


if __name__ == '__main__':
    main()
