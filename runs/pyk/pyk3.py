"""PYK run 3 (plans/pyk-plan.md): K3'' at 120 digits. Run from the repository's root: python3 runs/pyk/pyk3.py"""
import mpmath as mp
mp.mp.dps = 120
errs = {n: abs(mp.quad(lambda z: 1 / (1 - z**2), [0, 1 - mp.mpf(10)**-n]) - mp.log(2 * mp.mpf(10)**n - 1) / 2)
        for n in (1, 5, 10, 20, 50)}
print("K3'' errors:", {n: mp.nstr(e, 3) for n, e in errs.items()})
print("  K3'':", "not killed" if all(e < mp.mpf(10)**-40 for e in errs.values()) else "KILLED")
