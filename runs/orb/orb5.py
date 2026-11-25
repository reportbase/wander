# ORB run 5: Q1' in plans/orb-plan.md, beta as the half-slope of the angular eccentricity, in rational form.
import sympy as sp
t = sp.symbols('t', positive=True)
s = 2*t/(1 + t**2); c = (1 - t**2)/(1 + t**2)
res = sp.simplify((1 - c)/s - t)
print("Q1' beta - t =", res); print("Q1'", 'not killed' if res == 0 else 'KILLED')
open('runs/orb/orb-run5.txt', 'w').write(f"Q1' beta - t = {res}\nQ1' {'not killed' if res == 0 else 'KILLED'}\n")
