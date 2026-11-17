# MUT checks made while writing essay 30 (17 Nov). NOT committed predictions: worked by hand, checked here, reported as checks.
# Three places where run 1's clean collapse may not hold: the heat on each read, a read one round late, strides in amounts.
import numpy as np
rng = np.random.default_rng(1)
a, b, g = 0.0, 3.0, 0.05          # corners in levels (d_A = 1, d_B = e^3), the read's half-width in levels
out = []
def say(s): print(s); out.append(s)

# (1) each read spread by a Cauchy of half-width g in levels: x' = x + al(a - x + eA) + be(b - x + eB)
# worked: x - x* -> sum (1-al-be)^k (al eA + be eB), a Cauchy of half-width g(al+be)/(1-|1-al-be|): g whenever al+be <= 1
for al in (0.1, 0.25, 0.5, 0.7):
    M = 200000; x = np.full(M, 1.5)
    for n in range(400):
        x = x + al * (a - x + g * rng.standard_cauchy(M)) + al * (b - x + g * rng.standard_cauchy(M))
    q = np.quantile(x, [0.25, 0.5, 0.75])
    say(f"heat: share {al} each: median {q[1]:.4f} (x* 1.5), half-IQR {(q[2]-q[0])/2:.5f}, worked {g*2*al/(1-abs(1-2*al)):.5f}")

# (2) both read one round late: x_(n+1) = x_n + al(a - x_(n-1)) + al(b - x_(n-1)); worked: z^2 - z + 2al = 0, stable iff al < 1/2
for al in (0.25, 0.45, 0.5, 0.55, 0.6):
    x = [-5.0, -5.0]
    for n in range(2000): x.append(x[-1] + al * (a - x[-2]) + al * (b - x[-2]))
    say(f"late: share {al}: after 2000 rounds {x[-1]:.6g} (x* 1.5)")

# (3) strides in amounts: each steps S*ln(s), S its own stride, s its reading; d' = d + S ln s_A + S ln s_B
# worked: rest at s_A s_B = 1, d* = sqrt(d_A d_B) = 4.4817; factor 1 - 2S/d* a round near it, stable iff S < d*
dstar = np.exp((a + b) / 2)
for S in (0.5, 2, 4, 4.4, 4.6, 5, 15):
    d = 50.0; h = []
    for n in range(4000):
        d = d + S * np.log(np.exp(a) / d) + S * np.log(np.exp(b) / d); h.append(d)
        if not (0 < d < 1e12): break
    tail = sorted(set(round(v, 4) for v in h[-8:]))
    say(f"strides: S {S} (S/d* {S/dstar:.3f}): last values {tail}")
open('runs/mut/mut3-checks.txt', 'w').write("\n".join(out) + "\n")
