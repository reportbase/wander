"""CDW: a continuous read over discrete writes (SPN R1268, 27 Nov 2026).

Tom: "seems to me you can have a SHV sweep of a DHV sweep. in other words a continuous read heat sweeping a discrete
write heat." The read's heat from a focus f with thumb H, laid over writes at the whole numbers n, sums to

    S(H, f) = sum_n H / (pi (H^2 + (n - f)^2)) = sinh(2 pi H) / (cosh(2 pi H) - cos(2 pi f))

(Poisson summation of the Cauchy: the writer's mathematics, classical). Against the continuum's 1 the ripple is
S - 1 = 2 sum_k e^(-2 pi k H) cos(2 pi k f), so about 2 e^(-2 pi H): the writes' discreteness is seen by the read only
while a thumb spans about one write or fewer. Exact check at 40 digits, nothing predicted beyond the known identity.
Run from the repository's root: python3 runs/cdw/cdw.py
"""
from mpmath import mp, mpf, nsum, inf, pi, sinh, cosh, cos, exp

mp.dps = 40
worst = mpf(0)
print(f"{'H':>6} {'f':>5} {'sum over writes':>22} {'closed form':>22} {'S - 1':>12} {'2e^(-2piH)cos(2pif)':>20}")
for H in [mpf(1) / 8, mpf(1) / 4, mpf(1) / 2, mpf(1), mpf(2), mpf(4), mpf(8)]:
    for f in [mpf(0), mpf(1) / 4, mpf(1) / 2]:
        s = nsum(lambda n: H / (pi * (H ** 2 + (n - f) ** 2)), [-inf, inf])
        c = sinh(2 * pi * H) / (cosh(2 * pi * H) - cos(2 * pi * f))
        worst = max(worst, abs(s - c))
        lead = 2 * exp(-2 * pi * H) * cos(2 * pi * f)
        print(f"{mp.nstr(H, 4):>6} {mp.nstr(f, 3):>5} {mp.nstr(s, 18):>22} {mp.nstr(c, 18):>22} "
              f"{mp.nstr(s - 1, 3):>12} {mp.nstr(lead, 3):>20}")
print("largest |sum - closed form|:", mp.nstr(worst, 3))
