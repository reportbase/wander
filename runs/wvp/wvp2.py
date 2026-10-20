"""WVP run 2, P3': the mean's climb with its noise counted (plans/wvp-plan.md). 4,000 runs per N, 1,000 bootstraps.
Run: python3 runs/wvp/wvp2.py   (numpy; a few minutes)
"""
import numpy as np
from math import pi, log
R, Ns = 4000, [10**2, 10**5]
means = {}
for N in Ns:
    means[N] = np.array([np.tan(np.random.default_rng(10000 + j).uniform(0, pi / 2, N)).mean() for j in range(R)])
climb = (np.median(means[10**5]) - np.median(means[10**2])) / 3
bs = np.random.default_rng(1)
boot = [(np.median(bs.choice(means[10**5], R)) - np.median(bs.choice(means[10**2], R))) / 3 for _ in range(1000)]
se = np.std(boot, ddof=1)
iqr = {N: np.subtract(*np.percentile(means[N], [75, 25])) for N in Ns}
ratio = iqr[10**2] / iqr[10**5]
z = abs(climb - 2 / pi * log(10)) / se
print(f"medians of the mean: 1e2 {np.median(means[10**2]):.4f}, 1e5 {np.median(means[10**5]):.4f}")
print(f"average climb a decade {climb:.4f} vs (2/π)ln10 {2/pi*log(10):.4f}; bootstrap se {se:.4f}; off by {z:.2f} se")
print(f"IQR 1e2 {iqr[10**2]:.3f}, 1e5 {iqr[10**5]:.3f}; shrink ×{ratio:.2f}")
print("P3'", 'not killed' if z <= 3 and ratio <= 2 else 'KILLED')
