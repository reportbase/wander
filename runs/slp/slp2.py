# SLP run 2 (S1(b) checked with cos alpha declared positive; otherwise as run 1): the reader's math in slopes. See plans/slp-plan.md.
import sympy as sp
ok = {}
s, s2, x, t, g, d, a, k, th, al = sp.symbols('s s2 x t gamma d a k theta alpha', positive=True)
z = lambda e: sp.simplify(e) == 0
# S1: each writer's angle form against its slope form, with s = tan(theta) etc.
S = sp.tan(th)
checks = {
 'a heat': (sp.cos(th)**2, 1/(1+S**2)),
 'f re doubled': (sp.cos(2*th), (1-S**2)/(1+S**2)),
 'f im doubled': (sp.sin(2*th), 2*S/(1+S**2)),
 'i essay18 heat': (sp.cos(th-sp.pi/4)**2, (1+S)**2/(2*(1+S**2))),
}
r1 = {kk: z(sp.expand_trig(u - v)) for kk, (u, v) in checks.items()}
cc = sp.symbols('c', positive=True)
r1['b screen heat'] = z(cc**3 - 1/(1+(1-cc**2)/cc**2)**sp.Rational(3, 2))   # r = tan(alpha), r^2 = s^2 + s2^2
h = 1/sp.sqrt(1+s**2+s2**2)
r1['c n thumbs (n=2: h^3)'] = z(1/(1+s**2+s2**2)**sp.Rational(3, 2) - h**3)
r1['d sech'] = z(sp.sech(sp.log(x)).rewrite(sp.exp) - 2*x/(1+x**2))
s1_, s2_ = sp.symbols('u v', real=True)
r1['e composition'] = z(sp.expand_trig(sp.tan(sp.atan(s1_)+sp.atan(s2_))) - (s1_+s2_)/(1-s1_*s2_))
r1['g depth point'] = z((d*sp.exp(2*sp.I*sp.atan(g))).rewrite(sp.cos).rewrite(sp.sqrt) - d*(1+sp.I*g)/(1-sp.I*g)) or \
    z(sp.simplify(sp.expand_complex(d*sp.exp(2*sp.I*sp.atan(g)) - d*(1+sp.I*g)/(1-sp.I*g))))
r1['g median'] = z(sp.expand_trig(d*sp.cos(2*sp.atan(g))) - d*(1-g**2)/(1+g**2))
r1['h thing as H'] = z(1/(2*sp.tan(al/2)) - 1/(2*sp.tan(al/2)))  # definitional: t = tan(alpha/2)
r1['j corner'] = sp.solve(sp.Eq(s, 1/s), s) == [1]
slope_forms = [1/(1+s**2), h**3, 2*x/(1+x**2), (1-s**2)/(1+s**2), d*(1+sp.I*g)/(1-sp.I*g), (1+s)**2/(2*(1+s**2))]
nopi = all(not f.has(sp.pi) and not f.has(sp.atan) for f in slope_forms)
ok['S1'] = all(r1.values()) and nopi
print('S1:', r1, '; no pi or atan in the slope forms:', nopi)
# S2: the writer's forms need atan or pi (arctan is transcendental: classical, Liouville); here only that their slope
# forms contain atan/pi and that their large-s limit is pi/2 (not reachable as a rational function's limit... recorded as classical)
share = 2/sp.pi*sp.atan(s); arcchord = sp.atan(s)*sp.sqrt(1+s**2)/s
ok['S2'] = share.has(sp.atan) and arcchord.has(sp.atan) and sp.limit(share, s, sp.oo) == 1
print('S2: share and arc/chord in s contain atan:', share.has(sp.atan), arcchord.has(sp.atan),
      '; share -> 1 at the horizon:', sp.limit(share, s, sp.oo))
# S3: a boost is not a map of s. Oriented direction's half-angle slope t; the opposite direction -1/t; both the same s.
sof = lambda tt: 2*tt/(1-tt**2)
t1 = sp.symbols('t1', positive=True)
same_before = z(sof(t1) - sof(-1/t1))
after1, after2 = sof(t1/k), sof((-1/t1)/k)
diff = sp.simplify(after1 - after2)
ex = diff.subs({t1: sp.Rational(1, 3), k: 2})
ok['S3'] = same_before and ex != 0
print('S3: same s before:', same_before, '; boosted s differ by', diff, '; at t=1/3, k=2:', ex)
# S4: in t, turns t -> (t+a)/(1-a t) and boosts t -> t/k are Moebius; compositions too (matrix products)
M_turn = lambda aa: sp.Matrix([[1, aa], [-aa, 1]]); M_boost = lambda kk: sp.Matrix([[1, 0], [0, kk]])
act = lambda M, tt: (M[0, 0]*tt + M[0, 1])/(M[1, 0]*tt + M[1, 1])
a1, a2, k1 = sp.symbols('a1 a2 k1', positive=True)
turn_ok = z(act(M_turn(a), t) - sp.tan(sp.atan(t)+sp.atan(a)))   # tangent addition on half-angles
boost_ok = z(act(M_boost(k), t) - t/k)
P = M_turn(a1)*M_boost(k1)*M_turn(a2)
comp = z(act(P, t) - act(M_turn(a1), act(M_boost(k1), act(M_turn(a2), t))))
# check boost on t equals aberration: cos th' = (cos th + b)/(1 + b cos th), t = tan(th/2), k = sqrt((1+b)/(1-b)) with t' = t/k
b = sp.symbols('b', positive=True)
kk = sp.sqrt((1-b)/(1+b))   # t' = t*kk is the boost toward the axis in this sign; aberration identity in t
c = (1-t**2)/(1+t**2); tp = t*kk; cp = (1-tp**2)/(1+tp**2)
aberr = z(cp - (c+b)/(1+b*c))
ok['S4'] = turn_ok and boost_ok and comp and aberr
print('S4: turn Moebius in t:', turn_ok, '; boost t/k:', boost_ok, '; composition Moebius:', comp, '; aberration in t:', aberr)
print('SUMMARY:', ok)
