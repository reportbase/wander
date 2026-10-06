"""Checks behind plans/wavelets.md: SPN's octaves against filters, wavelets and hearing scales.

    python3 plans/wavelets/checks.py
"""
import math

import numpy as np

P = math.pi
deg = math.degrees


def theta_octaves(s, r=2.0):
    """SPN Proposition 3.12's reading: each octave (c/r to rc) one quarter turn, read projectively."""
    s = np.asarray(s, float)
    n = np.floor(np.log(s * r) / np.log(r * r))
    x = s / (r * r) ** n
    with np.errstate(divide='ignore'):
        return (P / 2) * (n + (2 / P) * np.arctan((r * x - 1) / (r - x)))


print('1. One first-order filter, H = 1/(1 + i·ω/ωc). Its phase lag is atan(s), s = ω/ωc: one bounded sweep.')
print(f'   at the corner frequency: lag {deg(math.atan(1)):.1f}°, power passed {1 / 2:.2f} (the half-power point)')
print('   turn each octave out from the corner gets (×4 per octave):',
      [round(deg(math.atan(2 * 4**n) - math.atan(0.5 * 4**n)), 2) for n in range(6)], '(Proposition 3.11\'s counterexample)')

print('\n2. A ladder of first-order sections, corners geometrically spaced at qⁿ (one per octave): phase Φ(ω) = Σ atan(ω/qⁿ).')
for q in (4.0, 2.0):
    N = 60
    corners = q ** np.arange(-N, N + 1)
    phase = lambda w: np.sum(np.arctan(np.outer(np.atleast_1d(w), 1 / corners)), axis=1)
    W = q ** np.linspace(-6, 6, 4801)
    F = phase(W)
    step = phase(W * q) - F
    k = (P / 2) / math.log(q)                       # radians per neper, if each octave turns a quarter
    fit = np.polyfit(np.log(W), F, 1)
    ripple = F - np.polyval(fit, np.log(W))
    print(f'   q = {q:g}: one octave adds {deg(step.mean()):.4f}° (spread {deg(step.max() - step.min()):.1e}°); '
          f'phase against ln ω has slope {fit[0]:.4f} (a quarter turn per octave: {k:.4f}); '
          f'ripple about the straight line ±{deg(np.max(np.abs(ripple))):.4f}°')
for r in (2.0, math.sqrt(2)):
    S = (r * r) ** np.linspace(-4, 4, 8001)
    T = theta_octaves(S, r)
    fit = np.polyfit(np.log(S), T, 1)
    print(f'   SPN 3.12, octave ×{r*r:g}: slope {fit[0]:.4f}, ripple ±{deg(np.max(np.abs(T - np.polyval(fit, np.log(S))))):.2f}° '
          f'(the projective octave wobbles more than the ladder)')

print('\n3. Tilings of the frequency axis: how many analysis bins fall in each octave.')
octs = [(2.0**j, 2.0**(j + 1)) for j in range(0, 8)]
stft = [int(round((b - a) / 1.0)) for a, b in octs]      # uniform: bins 1 Hz wide
wav = [12 for _ in octs]                                 # constant-Q: 12 bins per octave
print('   uniform (short-time Fourier, bins 1 apart), octaves 1-2, 2-4, …:', stft, '(doubles each octave)')
print('   constant-Q / wavelet (12 a octave):', wav, '(the same every octave: (R))')
print('   one bounded sweep (bins even in atan s), share per octave out from the corner:',
      [round(float(math.atan(2.0**(j + 1)) - math.atan(2.0**j)) / (P / 2) * 96, 1) for j in range(0, 8)], '(of 96)')

print('\n4. Hearing scales: proportion below a corner, a logarithm above it.')
for name, fc, A in (('mel (O\'Shaughnessy 1987)', 700.0, 2595.0), ('ERB-number (Glasberg and Moore 1990)', 1 / 0.00437, 21.4)):
    f = lambda x: A * math.log10(1 + x / fc)
    lin = lambda x: A * (x / fc) / math.log(10)              # the front side: the slope at 0
    print(f'   {name}: corner fc = {fc:.0f} Hz; slope at fc is {1/(1+1):.2f} of the slope at 0; '
          f'at fc/10 proportion holds to {abs(f(fc/10)/lin(fc/10) - 1):.1%}, '
          f'at 10·fc the logarithm (no +1) to {abs(A*math.log10(10) / f(10*fc) - 1):.1%}')
print('   log(1 + s) is not fair to the facings: it runs on without bound past the corner; read past the corner')
print('   as a count it is SPN\'s R176 lay (proportion to the corner, octaves past it), a float\'s subnormals then normals.')
