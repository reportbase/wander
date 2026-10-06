"""Numerical checks behind plans/part-one-audit.md (SPN Part I). Every line prints a claim and what it comes to.

    python3 plans/audit/part_one_checks.py
"""
import math

import numpy as np

at, P = math.atan, math.pi


def bisect(f, lo, hi, target):
    for _ in range(200):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if f(m) < target else (lo, m)
    return m


print('§3.2 the disc and the coil against Proposition 3.2(b), f(s) + f(1/s) = 1:')
disc = lambda s: s * s / (1 + s * s)
coil = lambda s: s ** 3 / (1 + s * s) ** 1.5
for s in (0.5, 1, 2, 3):
    print(f'  s = {s}: disc {disc(s) + disc(1 / s):.4f}   coil {coil(s) + coil(1 / s):.4f}')
print(f'  the coil reaches half its most at s = {bisect(coil, 0.1, 10, 0.5):.4f}, not at the corner')
print(f'  disc against s² at s = 0.1: {1 - disc(0.1) / 0.01:.4%} (the photometrist\'s 1%)')
print(f'  Leibniz, 1000 terms, short by {P / 4 - sum((-1) ** k / (2 * k + 1) for k in range(1000)):.6f}')

print('\n§3.2 the dipole and the round opening:')
for s in (0.1, 0.5, 1, 2, 10):
    print(f'  dipole near share s²/(1+s²) at s = {s}: {disc(s):.4f}')
E = lambda s: abs(complex(s ** 3 - s, -s * s)) ** 2
print(f'  |E|² = s²(s⁴ − s² + 1) at s = 1.7: {E(1.7):.6f} vs {1.7 ** 2 * (1.7 ** 4 - 1.7 ** 2 + 1):.6f}')
F = 1 / 8
print(f'  L > 2D²/λ is F = 1/8, s = {math.sqrt(F):.3f}; 4 sin²(πF/2) against (πF)²: {1 - 4 * math.sin(P * F / 2) ** 2 / (P * F) ** 2:.2%} off')

print('\n§3.3 shares of an evenly spread world, and the octave as a sweep:')
print('  past 1, 2, 4 … 32:', [round(1 - 2 * at(x) / P, 4) for x in (1, 2, 4, 8, 16, 32)])
print('  doublings k = 0 … 4:', [round(2 * (at(2 ** (k + 1)) - at(2 ** k)) / P, 4) for k in range(5)])
print('  ×4 octaves n = 0, 1, 2:', [round(2 * (at(2 * 4 ** n) - at(0.5 * 4 ** n)) / P, 4) for n in (0, 1, 2)])
rho = lambda s: 2 * (s - .5) / (2 - s)
g = lambda s: (2 / P) * at(rho(s))
S = np.exp(np.linspace(math.log(.5) + 1e-9, math.log(2) - 1e-9, 200001))
G = np.array([g(s) for s in S])
d = np.abs(G - (np.log(S) / np.log(4) + .5))
print(f'  max |g − (log₄ s + ½)| = {d.max():.4f} at s = {S[d.argmax()]:.3f} (and 1/s by the flip)')
place = np.where(S <= 1, S - .5, 1 - (1 / S - .5))
d = np.abs(G - place)
print(f'  max |g − the share\'s place| = {d.max():.4f} at s = {S[d.argmax()]:.3f}')


def address(s, levels=5):
    out = []
    for _ in range(levels):
        n = math.floor(math.log(s / 0.5, 4))
        out.append(n)
        s = rho(s / 4 ** n)
    return out


print('  address of 1.37h:', address(1.37))

print('\nThe central hypothesis: does the corner sit mid-octave only for a ratio of 2? (octave c/r to rc, two facings)')
for r in (2, 3, (1 + 5 ** 0.5) / 2, 10):
    rr = lambda s, r=r: (r * s - 1) / (r - s)          # the projective map: 1/r, 1, r to 0, 1, ∞
    gg = lambda s, rr=rr: (2 / P) * at(rr(s))
    fair = max(abs(rr(1 / s) * rr(s) - 1) for s in np.linspace(1 / r + 1e-6, r - 1e-6, 997))
    print(f'  r = {r:.3f}: g at the corner = {gg(1.0):.4f}; flip fair to {fair:.1e}')

print('\nProposition 3.8(b) under R175 (corners at 4ⁿ, edges at 2·4ⁿ and ½·4ⁿ): does a reader at 2ᵐh share the edges?')
low_edges = {2 * k + 1 for k in range(-5, 5)}          # log₂ of the lower reader's edges: odd powers of 2
for m in range(1, 5):
    up_edges = {e + m for e in low_edges}
    print(f'  m = {m}: same edges {up_edges == {e for e in up_edges if e % 2 != 0}}')

print('\n§3.8 the reach of N addresses laid evenly in turn (doublings past the corner with at least 8 addresses):')
for N in (100, 1000, 10000, 100000):
    s = np.tan((np.arange(N) + 0.5) * (P / 2) / N)
    k = 0
    while np.sum((s >= 2 ** k) & (s < 2 ** (k + 1))) >= 8:
        k += 1
    print(f'  N = {N}: {k} octaves, last address {s[-1]:.0f} (4N/π = {4 * N / P:.0f})')
