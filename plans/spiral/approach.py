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
