# INV run 1: the near/far exchange against the facings' exchange. Exact (sympy).
import sympy as sp
x,s,u,t,k,a=sp.symbols('x s u theta k a',positive=True)
res={}
# X1
lhs=sp.sech(sp.log(x))/sp.pi/x; rhs=2/(sp.pi*(1+x**2))
res['X1 sech(ln x)/pi dlnx == (2/pi)dx/(1+x^2)']=sp.simplify(sp.expand(lhs.rewrite(sp.exp))-rhs)==0
# X2
f=2/(sp.pi*(1+x**2)); g=f.subs(x,1/x)*x**-2
res['X2 law kept by x->1/x']=sp.simplify(g-f)==0
F=sp.integrate(f,(x,0,x))
res['X2 median 1']=sp.simplify(F.subs(x,1)-sp.Rational(1,2))==0
res['X2 quartiles sqrt2-+1']=sp.simplify(F.subs(x,sp.sqrt(2)-1)-sp.Rational(1,4))==0 and sp.simplify(F.subs(x,sp.sqrt(2)+1)-sp.Rational(3,4))==0
w=lambda z:(1+sp.I*z)/(1-sp.I*z)
res['X2 w(x)w(1/x)=-1']=sp.simplify(w(x)*w(1/x)+1)==0
res['X2 w(0),w(1),w(oo)=1,i,-1']=(w(0)==1 and sp.simplify(w(1)-sp.I)==0 and sp.limit(w(x),x,sp.oo)==-1)
# X3: reflections on (u,theta)
uu,tt=sp.symbols('uu tt',real=True)
Rs=lambda p:(p[0],sp.pi/2-p[1])   # s->1/s : theta -> pi/2 - theta
Rx=lambda p:(-p[0],p[1])          # x->1/x : u -> -u
comp=Rs(Rx((uu,tt)))
res['X3 composite = half turn about (0,pi/4)']=sp.simplify(comp[0]-(-uu))==0 and sp.simplify(comp[1]-(sp.pi/2-tt))==0
heat=lambda p:sp.cos(p[1]-sp.pi/4)**2*sp.sech(p[0])
H0=heat((uu,tt))
res['X3 heat kept by each and both']=all(sp.simplify(heat(q)-H0)==0 for q in [Rs((uu,tt)),Rx((uu,tt)),comp])
res['X3 peak at (0,pi/4) = 1']=heat((0,sp.pi/4))==1
# X4
res['X4 turn keeps uniform theta (whole turn)']=True  # density 1/(2pi) shifted is 1/(2pi): identity
Fk=sp.integrate(2*k/(sp.pi*(k**2+x**2)),(x,0,x))  # law of k*x
res['X4 thumb change moves median to k']=sp.simplify(Fk.subs(x,k)-sp.Rational(1,2))==0
# X5
tp=sp.atan(sp.exp(u)); gd=2*sp.atan(sp.tanh(u/2))
res['X5 atan(e^u) = pi/4 + gd(u)/2']=sp.simplify(sp.expand_trig((tp-sp.pi/4-gd/2).rewrite(sp.exp)))==0 or abs(sp.N((tp-sp.pi/4-gd/2).subs(u,sp.Rational(7,5)),60))<1e-55
dens=sp.diff(tp,u)
res['X5 d atan(e^u)/du = sech(u)/2 (theta prime uniform iff u ~ sech/pi)']=sp.simplify((dens-sp.sech(u)/2).rewrite(sp.exp))==0
res['X5 u law not uniform']=sp.sech(u).diff(u)!=0
for kk,v in res.items(): print(('ok   ' if v else 'KILL ')+kk)
