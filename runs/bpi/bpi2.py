"""BPI run 2: B2' (plans/bpi-plan.md). Exact (sympy)."""
import itertools, sympy as sp, importlib.util, sys, io, contextlib
spec = importlib.util.spec_from_file_location('bpi', 'runs/bpi/bpi.py'); m = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
good = True
for name, (q, units, D) in m.EX.items():
    Dm = sp.Matrix(D); n, r = Dm.cols, Dm.rank()
    bad = []
    for S in itertools.combinations(range(n), r - 1):
        rk = m.rank_of_writing(D, S)
        indep = (Dm[:, list(S)].rank() == r - 1) if S else True
        if rk > n - 1 or (rk == n - 1) != indep: bad.append((S, rk, indep))
    print(f"{name}: n={n}, r={r}, sets of r-1 = {len(list(itertools.combinations(range(n), r-1)))}, failures {bad}")
    good &= not bad
print('B2prime', 'not killed' if good else 'KILLED')
