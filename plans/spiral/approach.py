"""The two situated measures of a sweep against the line (SPN §2.1, 6 October): outside counts the turn (arc ÷ line,
θ/sin θ), inside projects it (line ÷ arc, sin θ/θ). Reciprocal at every turn; both tend to 1, the line, and never reach it.

    python3 plans/spiral/approach.py
"""
import math

print(f'{"turned through":>14} {"outside θ/sinθ":>15} {"inside sinθ/θ":>14} {"product":>8}')
for d in (1e-6, 15, 45, 75, 90):
    t = math.radians(d)
    a, b = t / math.sin(t), math.sin(t) / t
    print(f'{d:13g}° {a:15.4f} {b:14.4f} {a * b:8.4f}')
print(f'ends: outside π/2 = {math.pi / 2:.4f}, inside 2/π = {2 / math.pi:.4f}; 1 only with no turn (the line)')

print('\nRecursion as the approach: halve the sweep, and each piece turns less (gap from 1 shrinks ×4 per level)')
prev = None
for k in range(7):
    n = 2 ** k
    t = (math.pi / 2) / n
    g = t / math.sin(t) - 1
    print(f'  {n:3d} pieces of {math.degrees(t):7.3f}°: outside {t / math.sin(t):.6f}, inside {math.sin(t) / t:.6f}'
          + ('' if prev is None else f', gap ÷ {prev / g:.2f}'))
    prev = g
print('Archimedes, sides doubling: n·sin(π/n) < π < n·tan(π/n)')
for n in (6, 12, 24, 48, 96):
    print(f'  n = {n:2d}: {n * math.sin(math.pi / n):.6f} < π < {n * math.tan(math.pi / n):.6f}')
