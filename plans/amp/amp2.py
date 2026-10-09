"""AMP run 2 (plans/amp-plan.md): P3 with each level fitting its leftover on its own region only. Seeded."""
import numpy as np
import importlib.util, sys, os
spec = importlib.util.spec_from_file_location('amp', os.path.join(os.path.dirname(__file__), 'amp.py'))
# reuse run 1's definitions without re-running it
src = open(spec.origin).read().split('out = []')[0]
ns = {}; exec(src, ns)
K, N, M, DELTA = ns['K'], ns['N'], ns['M'], ns['DELTA']
home, width, level_val, target, inject, region_pts = (ns[n] for n in ('home', 'width', 'level_val', 'target', 'inject', 'region_pts'))
xr = (np.arange(M) + 0.5) / M * 0.5              # a level's own region, x in [0, 1/2)
xr_last = (np.arange(M) + 0.5) / M                 # the last level's region is its whole support
def build(js, shape):
    held = []
    def recon(g, upto):
        r = np.zeros_like(g)
        for k, a, inj in held[:upto]:
            r += level_val(a, k, g)
            if inj: r += inject(shape, k, g)
        return r
    left = {}
    for k in range(K):
        x = xr_last if k == K - 1 else xr
        g = home(k) + width(k) * x
        resid = target(g) - recon(g, k)
        B = np.cos(np.pi * np.outer(x, np.arange(N)))
        a, *_ = np.linalg.lstsq(B, resid, rcond=None)
        held.append((k, a, k in js))
        left[k] = (x, resid - B @ a)
    return (lambda g: recon(g, K)), left
def region_err(R, k):
    g = region_pts(k); return np.max(np.abs(R(g) - target(g)))
out = []
P = lambda *a: (print(*a), out.append(' '.join(str(x) for x in a)))
R0, left0 = build([], 'flat')
base = [region_err(R0, k) for k in range(K)]
ok = {'a': max(base) < 1e-9, 'b': True, 'c': True, 'd': True}
P(f'baseline error {max(base):.1e}')
for shape in ('flat', 'sloped'):
    for j in range(K - 1):
        R, left = build([j], shape)
        A = [(region_err(R, k) - base[k]) / DELTA for k in range(K)]
        below = max(abs(A[k]) for k in range(j + 1, K))
        if shape == 'flat':
            ok['b'] &= abs(A[j] - 1) <= 0.01 and below < 1e-9
            P(f'  flat   j={j}: A(j->j) {A[j]:.4f}; below max {below:.1e}')
        else:
            ok['c'] &= below < 0.01
            fr = []
            for k in range(j + 1, K):
                x, d = left[k]; d0 = left0[k][1]; e = np.abs(d - d0)
                span = x.max()
                fr.append(e[x < 0.1 * span].sum() / e.sum() if e.sum() > 0 else 1.0)
            ok['d'] &= min(fr) >= 0.5
            P(f'  sloped j={j}: A(j->j) {A[j]:.4f}; below max {below:.2e}; next to home min {min(fr):.3f}', ' per child', ' '.join(f'{f:.2f}' for f in fr))
for kk in 'abcd': P(f"P3'{kk}", 'held' if ok[kk] else 'FAILED')
P('P3 run 2', 'NOT KILLED' if all(ok.values()) else 'KILLED')
open(os.path.join(os.path.dirname(__file__), 'amp-run2.txt'), 'w').write('\n'.join(out) + '\n')
