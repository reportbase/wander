"""GEN run 2: G9' and G11' (plans/gen-plan.md). python3 runs/gen/gen2.py"""
import sympy as sp, mpmath as mp
mp.mp.dps = 40
f = lambda x, y: 2/mp.pi*(1+x*x+y*y)**mp.mpf(-1.5)
vals = {'octant': (mp.quad(f, [0, 1, mp.inf], [0, 1, mp.inf]), 1),
        'screen': (mp.quad(lambda x, y: (1+x*x+y*y)**mp.mpf(-1.5)/(2*mp.pi), [-mp.inf, 0, mp.inf], [-mp.inf, 0, mp.inf]), 1),
        'pair': (mp.quad(f, [0, 1], [0, 1, mp.inf]), mp.mpf(1)/2),
        'near': (mp.quad(f, [0, 1], [0, 1]), mp.mpf(1)/3),
        'order': (mp.quad(lambda x: mp.quad(lambda y: f(x, y), [x, mp.inf]), [1, mp.inf]), mp.mpf(1)/6)}
for n, (v, t) in vals.items(): print(n, mp.nstr(v - t, 5))
g9 = all(abs(v - t) < mp.mpf('1e-18') for v, t in vals.values())
d = sp.symbols('d', positive=True)
ident = sp.simplify((sp.sech(sp.log(d)) - 2*d/(1+d**2)).rewrite(sp.exp)) == 0
lo = mp.quad(lambda x: mp.sech(x)/mp.pi, [-mp.inf, 0]); hi = mp.quad(lambda x: mp.sech(x)/mp.pi, [0, mp.inf])
g11 = ident and abs(lo - hi) < mp.mpf('1e-30') and abs(lo + hi - 1) < mp.mpf('1e-30')
print("G9'", 'holds' if g9 else 'KILLED'); print("G11'", 'holds' if g11 else 'KILLED')
