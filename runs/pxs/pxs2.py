"""PXS run 2: X2' and X4' (plans/pxs-plan.md). Run from the repository root."""
import numpy as np
exec(open('runs/pxs/pxs.py').read().split("out = []")[0])
rng = np.random.default_rng(20261103)
out = []; P = lambda *a: (print(*a), out.append(' '.join(map(str, a))))
ok = True
for g in [1e-3, 0.3]:
    for d in [1, 8]:
        cA, cB = reads(0, d, g, N); dh = 2/(cA + cB); r = (dh - d)/d; D = Dof(0, d, g)
        ke = ks(r, lambda t: ccdf(t, (D.real - d)/d, D.imag/d)); kf = ks(r, lambda t: ccdf(t, 0, 2*g*np.cosh(np.log(d))))
        good = ke < 0.002 and ((kf < 0.002) if (g == 1e-3 and d == 1) else True) and ((kf > 0.01) if g == 0.3 else True)
        ok &= good; P(f"X2' g={g} k={d}: KS exact={ke:.5f} KS first order={kf:.5f} {'ok' if good else 'FAIL'}")
P(f"X2' {'not killed' if ok else 'KILLED'}")
g = 0.1; M = 10**5; W1 = w(1, g); ok = True
se = np.sqrt(3/(16*M)) * 2*np.pi*W1.imag / np.sqrt(2)
for n in [1, 10, 100]:
    cA, cB = reads(0, 1, g, M*n); dh = (2/(cA + cB)).reshape(M, n)
    h = hiqr((1/dh).mean(axis=1)); z = (h - W1.imag)/se; hm = hiqr(np.median(dh, axis=1))
    if n == 1: m1 = hm
    ok &= abs(z) < 3; P(f"X4' n={n}: HIQR mean 1/d={h:.5f} law={W1.imag:.5f} z={z:+.2f} HIQR median d={hm:.5f}")
ok &= m1/hm > 5; P(f"X4' median narrows {m1/hm:.2f}x; {'not killed' if ok else 'KILLED'}")
open('runs/pxs/pxs-run2.txt', 'w').write('\n'.join(out) + '\n')
