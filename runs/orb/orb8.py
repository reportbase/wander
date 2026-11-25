# ORB run 8: R3'' (plans/orb-plan.md), committed first.  python3 runs/orb/orb8.py
import mpmath as mp
mp.mp.dps = 50
g = {h: abs(mp.sqrt((mp.coth(h) + 1)/(mp.coth(h) - 1)) - mp.exp(h))/mp.exp(h) for h in map(mp.mpf, ['0.01', '0.5', '2', '10'])}
w = max(g.values())
lines = ['R3\'\' relative gaps: ' + ', '.join(f'eta {mp.nstr(h, 3)}: {mp.nstr(v, 3)}' for h, v in g.items()),
         f"verdict: R3'' {'not killed' if w < mp.mpf('1e-40') else 'KILLED'}"]
print('\n'.join(lines)); open('runs/orb/orb-run8.txt', 'w').write('\n'.join(lines) + '\n')
