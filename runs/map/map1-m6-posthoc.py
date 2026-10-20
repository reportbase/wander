# MAP run 1, post hoc: where M6's place bound failed (room 15). Run from the repository's root.
import sys; sys.argv=['x']
exec(open('runs/map/map.py').read().split('SEEDS = [11')[0])
N=86
W = room(15); a, b = read(W, 'A'), read(W, 'B')
Ad = np.array([[float(x) for x in a[i]] for i in range(80, N)]); Bd = np.array([[float(x) for x in b[i]] for i in range(80, N)])
U_, S_, Vt = np.linalg.svd(Bd.T @ Ad); D = np.diag([1, 1, np.sign(np.linalg.det(U_ @ Vt))]); Rh = (U_ @ D @ Vt).T
oB, RB = in_A(W, 'B'); o = mvec([0,0,0]); Rm = mp.matrix(Rh.tolist())
errs=[(float(norm(approach(o, a[i], oB, Rm * b[i])[1] - truth_in_A(W, i))), float(norm(truth_in_A(W,i))), i) for i in range(80)]
errs.sort(reverse=True)
for e,d,i in errs[:5]:
    tA=truth_in_A(W,i); ang=float(mp.acos(dot(unit(tA),unit(tA-oB))))
    print(f"feature {i}: error {e:.2e}, distance {d:.2f} |AB|, parallax angle {ang:.3f} rad, error/(d^2) {e/d**2:.2e}")
