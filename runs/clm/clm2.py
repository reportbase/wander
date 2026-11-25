"""CLM run 2: C2' (plans/clm-plan.md), the outside shell summed over directions, quadrature in w = sin^2(theta)."""
import mpmath as mp
mp.mp.dps = 40
out = []
ok = True
for d in (mp.mpf(3), mp.mpf('1.5'), mp.mpf(10)):
    # F = integral over w in [0, 1/d^2] of pi * 2 * sigma * a / sqrt(a^2 - d^2 w), a = sigma = 1
    F = mp.quad(lambda w: 2*mp.pi/mp.sqrt(1 - d**2*w), [0, 1/d**2])
    diff = F - 4*mp.pi/d**2
    s = f"d={mp.nstr(d,3)}: F = {mp.nstr(F, 30)}, 4 pi/d^2 = {mp.nstr(4*mp.pi/d**2, 30)}, diff {mp.nstr(diff, 3)}, real: {isinstance(F, mp.mpf)}"
    print(s); out.append(s)
    ok = ok and isinstance(F, mp.mpf) and abs(diff) < mp.mpf('1e-25')
out.append("C2' " + ("not killed" if ok else "KILLED")); print(out[-1])
open('runs/clm/clm-run2.txt', 'w').write("\n".join(out) + "\n")
