"""CNT run 3 (plans/cnt-plan.md): K0 giants counted inside their complete distance, set by the data (under 2% fainter than V 7.3)."""
import math, runpy, sys
ns = runpy.run_path('plans/cnt/cnt2.py', run_name='lib')   # loads the stars and helpers (and prints run 2's lines again)
stars, giant, slope_cum, K = ns['stars'], ns['giant'], ns['slope_cum'], ns['K']
k = sorted((s for s in stars if giant(s[2])), key=lambda s: s[0])
dc, faint = None, 0
for i, s in enumerate(k):
    if s[1] > 7.3: faint += 1
    if faint / (i + 1) < 0.02 and i >= 20: dc = s[0]
print('--- run 3 ---')
inside = [s for s in k if s[0] <= dc]
print(f'complete distance of K0 giants: {dc:.1f} pc ({len(inside)} giants within it, {sum(1 for s in inside if s[1] > 7.3)} fainter than V 7.3)')
lo = dc / 4
s9 = slope_cum([math.log2(s[0]) for s in inside], math.log2(lo), math.log2(dc), 0.05)
n9 = sum(1 for s in inside if s[0] >= lo)
print(f'P9: {"not killed" if 2.6 <= s9 <= 3.4 and n9 >= 100 else "KILLED"}. K0 giants, {lo:.1f}-{dc:.1f} pc: {s9:.3f} levels of number per level of distance ({n9} stars in the range)')
mags = sorted(s[1] for s in inside if s[1] <= 7.3); xs, ys = [], []; v = math.floor(mags[0] * 10) / 10
while v <= mags[-1] + 1e-9:
    n = sum(1 for m in mags if m <= v)
    if n: xs.append(-K * v); ys.append(math.log2(n))
    v += 0.1
mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
s10 = -sum((a - mx) * (c - my) for a, c in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)
print(f'P10: {"not killed" if 1.2 <= s10 <= 1.8 else "KILLED"}. by light inside it, V {mags[0]:.2f}-{mags[-1]:.2f}: {s10:.3f} levels of number per level of light')
