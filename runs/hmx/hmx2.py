"""HMX run 2, P1' (plans/hmx-plan.md): the circle of radius 1.2. Run: python3 runs/hmx/hmx2.py"""
from mpmath import mp, mpf, exp, sqrt, pi, cos, sin, gamma
mp.dps = 30
laws = {'normal': lambda x: exp(-x * x / 2) / sqrt(2 * pi), 'Laplace': lambda x: exp(-abs(x)) / 2,
        'uniform': lambda x: mpf(1) / 2 if abs(x) <= 1 else mpf(0),
        't3': lambda x: gamma(2) / (sqrt(3 * pi) * gamma(mpf(3) / 2)) * (1 + x * x / 3) ** -2}
R = mpf('1.2'); sp = {}
for k, f in laws.items():
    vals = [f(R * cos(pi * j / 16)) * f(R * sin(pi * j / 16)) for j in range(9)]
    sp[k] = max(vals) - min(vals); print(f"P1' {k}: variation on the circle of radius 1.2 {mp.nstr(sp[k], 6)}")
ok = sp['normal'] <= mpf(10) ** -25 and sp['uniform'] >= mpf('0.2') and sp['Laplace'] > mpf(10) ** -3 and sp['t3'] > mpf(10) ** -3
print("P1'", 'not killed' if ok else 'KILLED')
