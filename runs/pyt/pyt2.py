"""PYT run 2 (plans/pyt-plan.md): P7', the screen-to-sphere Gram determinant without a square root.
Run from the repository's root: python3 runs/pyt/pyt2.py"""
import sympy as sp
ok = True
for n in (1, 2, 3, 4):
    ss = sp.symbols(f"s1:{n+1}", real=True)
    R2 = 1 + sum(q**2 for q in ss)
    u = sp.Matrix([1] + list(ss)) / sp.sqrt(R2)
    J = u.jacobian(sp.Matrix(ss))
    det = sp.factor(sp.simplify((J.T * J).det()))
    good = sp.simplify(det - R2**(-(n + 1))) == 0
    print(f"n = {n}: det(J^T J) = {det}: {good}")
    ok &= good
print("P7':", "not killed" if ok else "KILLED")
