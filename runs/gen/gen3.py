"""GEN run 3: G14, G15 (plans/gen-plan.md). python3 runs/gen/gen3.py"""
import sympy as sp
ok14 = True
for n in (1, 2, 3):
    r = sp.symbols(f's1:{n+1}', real=True)
    R2 = sum(x**2 for x in r)
    h = 1/sp.sqrt(1+R2)
    X = sp.Matrix([1, *r])                      # the pick, thumb on the first leg
    U = X*h                                     # its shadow one thumb out
    J = U.jacobian(r)                           # (n+1) x n
    G = sp.simplify(J.T*J)
    vol = sp.sqrt(sp.factor(G.det()))
    target = (1+R2)**sp.Rational(-(n+1), 2)
    hit = sp.simplify(vol**2 - target**2) == 0
    # the two factors: across part of a step and the distance
    e = sp.Matrix([0]*n); e[0] = 1              # a step along s1
    step = sp.Matrix([0, *e])
    unit = X*h
    across = step - (step.dot(unit))*unit
    across_len2 = sp.simplify(across.dot(across))
    dist = sp.simplify(sp.sqrt(X.dot(X)))
    fac = sp.simplify(across_len2 - (1 + R2 - r[0]**2)/(1+R2)) == 0 and sp.simplify(dist - 1/h) == 0
    print(f'n={n}: volume factor {sp.simplify(vol)}  equals h^{n+1}: {hit}; across/distance factors: {fac}')
    ok14 &= hit and fac
s = sp.symbols('s', positive=True)
w1 = 1/(1+s**2)                                 # first leg's line, reading s
x = 1/s; w2 = sp.simplify(1/(1+x**2)*sp.Abs(sp.diff(x, s)))  # second leg's line, reading 1/s, pulled back
ok15 = sp.simplify(w1 - w2) == 0 and sp.solve(sp.Eq(s, 1/s), s) == [1]
print("G14", 'holds' if ok14 else 'KILLED'); print("G15", 'holds' if ok15 else 'KILLED')
