"""A situated reader of finite resolution δ (plans/resolution-recursion.md, 6 October): how many octaves it resolves,
whether its rim, magnified, is its own view one octave on, and how its resolved window compares with the projective
octave and the logarithmic reading.

    python3 plans/spiral/resolution.py
"""
import math
D=math.degrees; R=math.radians
print("1. octaves resolved per side, ring width >= delta")
for dd in (10,1,0.1,1/60):
    d=R(dd); n=0
    while math.atan(2**(n+1))-math.atan(2**n)>=d: n+=1
    print(f"  delta={dd:.4g} deg  octaves={n}  log2(1/delta)={math.log2(1/d):.2f}")
print("2. rim magnified x2 vs fisheye one octave on: 2*atan(1/s) vs atan(2/s)")
for s in (2,4,16,64,256):
    a=2*math.atan(1/s); b=math.atan(2/s); print(f"  s={s}  {D(a):.4f} {D(b):.4f} rel err {(a-b)/b:.2e}")
print("3/4. window [tan d, cot d], r=cot d; stretch of fisheye vs projective vs log")
for dd in (26.565,10,1):
    d=R(dd); r=1/math.tan(d); worst_p=worst_l=0
    for i in range(1,2000):
        x=-math.log(r)+2*math.log(r)*i/2000; s=math.exp(x)
        lin=(math.atan(s)-d)*(math.pi/2)/(math.pi/2-2*d)
        proj=math.atan2(r*s-1,r-s)
        lg=(x/(2*math.log(r))+0.5)*math.pi/2
        worst_p=max(worst_p,abs(lin-proj)); worst_l=max(worst_l,abs(lin-lg))
    print(f"  delta={dd} r={r:.3f}  max |stretch-projective|={D(worst_p):.2f} deg  max |stretch-log|={D(worst_l):.2f} deg")
