"""AFM run 2, post hoc: how far apart the six far features lie, which sets how well a pair of them fixes a turn.
Run from the repository's root: python3 runs/afm/afm2-posthoc.py"""
import numpy as np
for seed in [11, 12, 13, 14, 15]:
    rng = np.random.default_rng(seed)
    for _ in range(50): rng.integers(6); rng.uniform([0, 0, 0], [5, 4, 2.5])
    for i in range(30): rng.uniform(0, 1, 3); rng.integers(3); rng.integers(2)
    D = []
    for _ in range(6):
        d = np.array([1.0, rng.uniform(-0.3, 0.3), rng.uniform(-0.1, 0.3)]); D.append(d / np.linalg.norm(d))
    ang = [np.degrees(np.arccos(np.clip(D[i] @ D[j], -1, 1))) for i in range(6) for j in range(i + 1, 6)]
    print(f"room {seed}: pair angles {min(ang):.1f} to {max(ang):.1f} deg, median {np.median(ang):.1f}")
