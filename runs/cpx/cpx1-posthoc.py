# CPX run 1, post hoc (after the kills): what J5's and J6's failures are. Not a test.
import importlib.util, sys
spec = importlib.util.spec_from_file_location("cpx", "runs/cpx/cpx.py")
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
F = m.F
bad = [(A,n) for A,n in m.ret_bad if A != "constructed"]
print("J5 failures that are hyperbolic samples:", len(bad))
print("  all trace 0, det < 0, return at n = 2:", all(m.tr(A)==0 and m.det(A)<0 and n==2 for A,n in bad))
pos = [A for A in m.S if m.det(A) > 0 and m.disc(A) >= 0]
retpos = 0
for A in pos:
    P = A
    for n in range(1,65):
        if m.is_scalar(P): retpos += 1; break
        P = m.mul(P, A)
print("  det > 0 with disc >= 0:", len(pos), "samples, returning:", retpos)
for c2 in [F(1,4),F(2),F(9)]:
    K = (F(0),-c2,F(1),F(0)); Kt = (K[0],K[2],K[1],K[3]); Q = (F(1),F(0),F(0),c2)
    print("  K_c keeps h^2 + c^2 v^2 at c^2 =", c2, ":", m.mul(m.mul(Kt,Q),K) == m.sc(c2,Q))
