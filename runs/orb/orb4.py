# ORB run 4: where the orbit's stage has its standpoint. Predictions Q1-Q5 in plans/orb-plan.md, committed first.
#   python3 runs/orb/orb4.py
import random
import sympy as sp
import mpmath as mp

mp.mp.dps = 50
TOL = mp.mpf('1e-45')
out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)
ok = {}

# Q1: e = sin(phi), beta = tan(phi/2), k = (1+beta)/(1-beta)
ph = sp.symbols('phi', positive=True)
e = sp.sin(ph)
beta = (1 - sp.sqrt(1 - e**2))/e
k = sp.sqrt((1 + e)/(1 - e))
q1a = sp.simplify(sp.trigsimp((beta - sp.tan(ph/2)).subs(sp.sqrt(1 - sp.sin(ph)**2), sp.cos(ph))))
q1b = sp.simplify(sp.trigsimp(((1 + sp.tan(ph/2))/(1 - sp.tan(ph/2)))**2 - (1 + e)/(1 - e)))
say('Q1 beta - tan(phi/2) =', q1a, '; ((1+t)/(1-t))^2 - k^2 =', q1b)
ok['Q1'] = q1a == 0 and q1b == 0

# Q2: e = tanh(eta), k = exp(eta), beta = tanh(eta/2), in the speed's chart
et = sp.symbols('eta', positive=True)
ee = sp.tanh(et)
q2a = sp.simplify((sp.exp(2*et) - (1 + ee)/(1 - ee)).rewrite(sp.exp))
bb = sp.tanh(et/2)
q2b = sp.simplify((2*bb/(1 + bb**2) - ee).rewrite(sp.exp))
say('Q2 e^(2eta) - (1+e)/(1-e) =', q2a, '; 2b/(1+b^2) - e =', q2b)
ok['Q2'] = q2a == 0 and q2b == 0
worst = mp.mpf(0)
for es in ['0.01', '0.1', '0.3', '0.6', '0.9', '0.99']:
    ev = mp.mpf(es); b = (1 - mp.sqrt(1 - ev*ev))/ev; kk = mp.sqrt((1 + ev)/(1 - ev))
    assert abs(2*mp.atanh(b) - mp.atanh(ev)) < TOL
    for i in range(200):
        n = -mp.pi + 2*mp.pi*(i + mp.mpf('0.5'))/200
        push = mp.diff(lambda x: 2*mp.atan(mp.tan(x/2)/kk), n)/(2*mp.pi)
        w = -b                                     # the standpoint, on the far side
        pois = (1 - w*w)/(2*mp.pi*(1 + w*w - 2*w*mp.cos(n)))
        worst = max(worst, abs(push - pois))
say('Q2 push-forward of uniform E against the Poisson kernel from -beta, worst', mp.nstr(worst, 3),
    '; 2 artanh(beta) = artanh(e) at all six')
ok['Q2'] &= worst < TOL

# Q3: composing the maps
rng = random.Random(4)
def tmap(e_, x):                                   # nu from E
    return 2*mp.atan(mp.sqrt((1 + e_)/(1 - e_))*mp.tan(x/2))
w3 = mp.mpf(0)
for _ in range(30):
    e1 = mp.mpf(rng.random()*0.95); e2 = mp.mpf(rng.random()*0.95)
    e3 = (e1 + e2)/(1 + e1*e2)
    b = lambda q: (1 - mp.sqrt(1 - q*q))/q
    w3 = max(w3, abs(b(e3) - (b(e1) + b(e2))/(1 + b(e1)*b(e2))))
    for x in [mp.mpf('0.3'), mp.mpf('1.7'), mp.mpf('-2.9')]:
        w3 = max(w3, abs(tmap(e2, tmap(e1, x)) - tmap(e3, x)))
say('Q3 composing two maps against velocity addition, worst', mp.nstr(w3, 3))
ok['Q3'] = w3 < TOL

# Q4: e/2 < beta < e, and the series
es_ = sp.symbols('e', positive=True)
ser = sp.series((1 - sp.sqrt(1 - es_**2))/es_, es_, 0, 6).removeO()
say('Q4 series of beta:', ser)
q4 = sp.expand(ser).coeff(es_, 1) == sp.Rational(1, 2) and sp.expand(ser).coeff(es_, 3) == sp.Rational(1, 8)
between = all(mp.mpf(q)/2 < (1 - mp.sqrt(1 - mp.mpf(q)**2))/mp.mpf(q) < mp.mpf(q)
              for q in ['0.01', '0.1', '0.3', '0.6', '0.9', '0.99'])
say('Q4 e/2 < beta < e at all six:', between)
ok['Q4'] = q4 and between

# Q5: the ratios at the ends
nu = sp.symbols('nu')
st = sp.sqrt(1 - es_**2)/(2*sp.pi*(1 + es_*sp.cos(nu)))
pay = (1 - es_**2)/(1 + es_*sp.cos(nu))
clk = st*pay
kk2 = (1 + es_)/(1 - es_)
r1 = sp.simplify(st.subs(nu, sp.pi)/st.subs(nu, 0) - kk2)
r2 = sp.simplify(pay.subs(nu, 0)/pay.subs(nu, sp.pi) - 1/kk2)
r3 = sp.simplify(clk.subs(nu, sp.pi)/clk.subs(nu, 0) - kk2**2)  # the clock's far/near, predicted k^4
say('Q5 stage far/near - k^2 =', r1, '; payload near/far - 1/k^2 =', r2,
    '; clock far/near - k^4 =', r3)
ok['Q5'] = r1 == 0 and r2 == 0 and r3 == 0
say('verdicts:', ', '.join(f'{a} {"not killed" if v else "KILLED"}' for a, v in ok.items()))
open('runs/orb/orb-run4.txt', 'w').write('\n'.join(out) + '\n')
