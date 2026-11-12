# OMP run 1: Omega = pi/2 helps (S' < S) against the blind source class.
import csv
from fractions import Fraction as F
def H(q): return max(abs(q.numerator), q.denominator)
L={r['id']:r for r in csv.DictReader(open('runs/omp/list.tsv'),delimiter='\t')}
C={r['id']:r for r in csv.DictReader(open('runs/omp/classes.tsv'),delimiter='\t')}
tab={}
for i,r in L.items():
    c2=F(r['c2']); k=F(r['k']); c2p=c2*F(2)**int(2*k)   # c' = c*2^k, so c'^2 = c^2*4^k
    S,Sp=H(c2),H(c2p); v='helps' if Sp<S else ('hurts' if Sp>S else 'tie')
    cl=C[i]['class']; tab.setdefault(cl,[]).append((i,r['constant'],S,Sp,v))
    print(i,cl,r['constant'],S,Sp,v,r['name'][:38],sep='\t')
print()
for cl in 'QTLO':
    xs=tab.get(cl,[]);
    if not xs: continue
    h=sum(x[4]=='helps' for x in xs); t=sum(x[4]=='tie' for x in xs)
    print(f"{cl}: n={len(xs)} helps={h} ({h/len(xs):.0%}) ties={t} hurts={len(xs)-h-t}")
TL=tab.get('T',[])+tab.get('L',[]); h=sum(x[4]=='helps' for x in TL)
print(f"T+L: n={len(TL)} helps={h} ({h/len(TL):.0%})")
