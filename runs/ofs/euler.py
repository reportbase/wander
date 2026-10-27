"""Review 32 (Gemini): checks of the Euler / Cayley / Cauchy-equation claims. Run: python3 runs/ofs/euler.py"""
import sympy as sp
t = sp.symbols('theta', real=True)
h, v = sp.cos(t), sp.sin(t)
# Thales circle on chord A=(0,0), B=(1,0); A's ray at theta meets it at P = cos(theta)*(cos, sin) = (h^2, hv)
P = sp.Matrix([h**2, h*v]); M = sp.Matrix([sp.Rational(1, 2), 0])
off = sp.simplify(P - M - sp.Rational(1, 2)*sp.Matrix([sp.cos(2*t), sp.sin(2*t)]))
print('P - M = (1/2)e^(2i theta):', off.T)
for th, name in [(0, 'zero'), (sp.pi/4, 'corner'), (sp.pi/2, 'horizon')]:
    print(f'  {name:8s} theta={th}: P = {tuple(P.subs(t, th))}, (h+iv)^2 = {sp.simplify(sp.exp(2*sp.I*th))}')
# Cayley: w = (s - i)/(s + i) at s = tan theta
s = sp.tan(t)
w = (sp.sin(t) - sp.I*sp.cos(t))/(sp.sin(t) + sp.I*sp.cos(t))  # (s - i)/(s + i) with s = tan theta, times cos
print("Cayley w = -e^(2i theta):", sp.simplify(sp.expand_complex(w*sp.exp(-2*sp.I*t))) == -1)
print('  Cayley images: s=0 ->', sp.simplify(((0 - sp.I)/(0 + sp.I))), '; s -> oo ->', sp.limit((sp.Symbol('x') - sp.I)/(sp.Symbol('x') + sp.I), sp.Symbol('x'), sp.oo))
# 3(g): periodicity alone forces imaginary eigenvalues; a non-isotropic Q is still preserved (no H, no V enters)
U = sp.Matrix([[2, 1], [0, 1]]); J = sp.Matrix([[0, -1], [1, 0]]); A = U*J*U.inv()
print('eigenvalues of a periodic generator U J U^-1:', A.eigenvals())
Phi = sp.simplify((A*t).exp())
print('Phi(2 pi) = I:', sp.simplify(Phi.subs(t, 2*sp.pi)) == sp.eye(2))
G = (U.inv()).T*U.inv()
print('preserved form Q = |U^-1 x|^2 (not the identity):', G.T, '; Phi^T G Phi - G =', sp.simplify(Phi.T*G*Phi - G).T)
