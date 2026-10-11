"""TGT: closure recovers the ratio of two readers' holds. See plans/tgt-plan.md."""
import numpy as np
rng = np.random.default_rng(11)

def polygon(n):
    ang = np.sort(rng.uniform(0, 2*np.pi, n))
    r = rng.uniform(0.5, 2.0, n)
    P = np.c_[r*np.cos(ang), r*np.sin(ang)]
    E = np.roll(P, -1, axis=0) - P                 # closed: sum of edges is zero
    return E

def counts(E, k, HA, HB):
    L = np.linalg.norm(E, axis=1); U = E/L[:, None]
    a = L[:k]/HA; b = L[k:]/HB                     # each part counted in its own hold
    return a, U[:k], b, U[k:]

def recover(a, Ua, b, Ub, tol=1e-12):
    SA = (a[:, None]*Ua).sum(0); SB = (b[:, None]*Ub).sum(0)
    nA, nB = np.linalg.norm(SA), np.linalg.norm(SB)
    if nA < tol or nB < tol: return None
    return nA/nB                                    # rho = HB/HA

# P1
worst = 0
for t in range(2000):
    n = rng.integers(3, 41); E = polygon(n); k = rng.integers(1, n)
    rho = 10**rng.uniform(-2, 2); HA = 10**rng.uniform(-3, 3); HB = rho*HA
    r = recover(*counts(E, k, HA, HB))
    worst = max(worst, abs(r/rho - 1))
print(f"P1 worst relative error {worst:.2e}:", "not killed" if worst <= 1e-12 else "KILLED")
# P2
th = 2*np.pi*np.arange(4000)/4000; P = np.c_[np.cos(th), np.sin(th)]; E = np.roll(P, -1, 0) - P
out = []
for rho in (0.5, 2, 3.7):
    r = recover(*counts(E, 2000, 1.0, rho)); out.append(r)
print("P2 recovered", [f"{x:.4f}" for x in out], ":", "not killed" if all(abs(x-y) < 5e-5 for x, y in zip(out, (0.5, 2, 3.7))) else "KILLED")
# P3
E = polygon(17); c1 = counts(E, 6, 2.0, 5.0); c2 = counts(E*1.0, 6, 2.0*7.3, 5.0*7.3)
same = np.allclose(c1[0], c2[0]*7.3) and np.allclose(c1[2], c2[2]*7.3)
# counts change only if the figure is held fixed; scaling holds AND figure together leaves counts fixed:
c3 = counts(E*7.3, 6, 2.0*7.3, 5.0*7.3)
fixed = np.allclose(c1[0], c3[0]) and np.allclose(c1[2], c3[2])
print("P3 figure and both holds scaled together, counts unchanged:", fixed, "-> recovered", recover(*c3), "vs", recover(*c1), ":", "not killed" if fixed else "KILLED")
# P4: each part closes on its own: two closed loops joined at a point
E1 = polygon(5); E2 = polygon(7); E = np.r_[E1, E2]
r = recover(*counts(E, 5, 1.0, 3.0), tol=1e-9)
print("P4 parts each closed: recovery", r, ":", "not killed" if r is None else "KILLED")
# P5 rounding
E = polygon(30); k = 12; rho = 2.5
for step in (1e-1, 1e-2, 1e-3, 1e-4):
    a, Ua, b, Ub = counts(E, k, 1.0, rho)
    a = np.round(a/step)*step; b = np.round(b/step)*step
    print(f"P5 step {step:g}: relative error {abs(recover(a, Ua, b, Ub)/rho-1):.2e}")
