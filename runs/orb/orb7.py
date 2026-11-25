# ORB run 7: R1' and R3' (plans/orb-plan.md), committed first.  python3 runs/orb/orb7.py
import sympy as sp, mpmath as mp
mp.mp.dps = 50
t, p = sp.symbols('t p', positive=True)
r1 = sp.simplify(p/(1 + (1 - t**2)/(1 + t**2))*(2*t/(1 + t**2)) - p*t)
x = sp.symbols('x', positive=True)
r3a = sp.simplify(sp.sqrt(x)*sp.sqrt(1/x) - 1)
w = max(abs(mp.sqrt((mp.coth(h) + 1)/(mp.coth(h) - 1)) - mp.exp(h)) for h in map(mp.mpf, ['0.01', '0.5', '2', '10']))
lines = [f"R1' y - p t = {r1}", f"R3' sqrt(x) sqrt(1/x) - 1 = {r3a}; K(coth eta) - e^eta worst {mp.nstr(w, 3)}",
         f"verdicts: R1' {'not killed' if r1 == 0 else 'KILLED'}, R3' {'not killed' if r3a == 0 and w < mp.mpf('1e-45') else 'KILLED'}"]
print('\n'.join(lines)); open('runs/orb/orb-run7.txt', 'w').write('\n'.join(lines) + '\n')
