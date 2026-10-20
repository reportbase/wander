"""PAM run 2, A4′ (plans/pam-plan.md): the payload's distance from the normal against the Edgeworth series' first term.
Run: python3 runs/pam/pam2.py   (about 15 s)
"""
import numpy as np
from math import erf, sqrt
th, M = 0.3, 2_000_000
r = np.random.default_rng(12)
zz = np.linspace(0, 5, 200001); G = np.abs(np.exp(-zz**2 / 2) / np.sqrt(2 * np.pi) * (zz**3 - 3 * zz)).max()
Phi = np.vectorize(lambda z: 0.5 * (1 + erf(z / sqrt(2))))
ok = True
for K in (2, 4, 8, 16, 32, 64):
    n = np.arange(1, K + 1)
    k4 = (np.cos(n * th)**4 + np.sin(n * th)**4).sum() * (-2 / 15) / (K / 3)**2
    pred = abs(k4) / 24 * G
    p = np.zeros(M)
    for j in range(K):
        p += r.uniform(-1, 1, M) * np.cos(n[j] * th) + r.uniform(-1, 1, M) * np.sin(n[j] * th)
    z = np.sort(p / np.sqrt(K / 3)); F = Phi(z); i = np.arange(1, M + 1)
    D = max((i / M - F).max(), (F - (i - 1) / M).max())
    good = abs(D - pred) <= 0.25 * pred + 0.001 if K <= 8 else D <= pred + 0.0015
    ok &= good
    print(f"K {K:3}: κ₄ {k4:+.5f}  predicted {pred:.5f}  measured {D:.5f}  {'ok' if good else 'OFF'}")
print("A4′", 'not killed' if ok else 'KILLED')
