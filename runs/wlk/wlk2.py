"""WLK run 2: the walk on Euler's circle, exact. Run from the repo root."""
import random
from fractions import Fraction as F
random.seed(12)
def w(x):                       # (x+i)/(x-i) = ((x^2-1) + 2xi)/(x^2+1)
    return ((x*x - 1) / (x*x + 1), 2*x / (x*x + 1))
def mul(a, b): return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])
xs = [F(random.randint(1, 10**6), random.randint(1, 10**4)) for _ in range(1000)]
E1 = all(sum(c*c for c in w(x)) == 1 for x in xs) and w(F(1)) == (0, 1) and w(F(0)) == (-1, 0) \
     and abs(w(F(10**30))[0] - 1) < F(1, 10**50) and mul(w(F(1)), w(F(1))) == (-1, 0)
E2 = all(mul(w(x), w(1/x)) == (-1, 0) for x in xs)
# E3: fixed points in the x chart (real line + infinity = the circle); x=inf <-> w=+1, x=0 <-> w=-1
d, q = F(7, 3600), F(1, 10)
# stride [[1,-d],[0,1]]: fixes inf only (x = x-d has no finite solution); trace^2 = 4
# share [[1-q,0],[0,1]]: fixes 0 and inf; normalised trace^2 = (2-q)^2/(1-q) > 4
# turn by slope t: x -> (x - t)/(t x + 1): fixed where t x^2 + t = 0 -> x^2 = -1, none real; trace^2 = 4/(1+t^2) < 4
t = F(1, 3)
E3 = (d != 0) and (2 - q)**2 / (1 - q) > 4 and 4 / (1 + t*t) < 4 \
     and all((x - d) != x and ((1 - q)*x == x) == (x == 0) and (x - t) != x*(t*x + 1) for x in xs + [F(0)])
def half_slope(x1, x2):         # slope of half the arc from w(x1) to w(x2): cot subtraction, s = 1/x
    return (x1 - x2) / (1 + x1*x2)
E4 = all(half_slope(x, x - d) == d / (1 + x*(x - d)) and half_slope(x, (1 - q)*x) == q*x / (1 + (1 - q)*x*x) for x in xs)
grid = [F(k, 1000) for k in range(1, 5001)]
best_share = max(grid, key=lambda x: q*x / (1 + (1 - q)*x*x)); best_stride = max(grid, key=lambda x: d / (1 + x*(x - d)))
E4 &= abs(float(best_share) - (1 - float(q))**-0.5) < 2e-3 and best_stride <= d + F(1, 1000)
x = F(1); n = 0
while x > 0: x -= d; n += 1
crossed = w(x)[1] < 0; past = w(x - 10**6)
y = F(1); never = True
for _ in range(5000):
    y *= (1 - q); never &= (w(y) != (-1, 0)) and w(y)[1] > 0
E5 = crossed and n == 515 and abs(past[0] - 1) < F(1, 10**11) and past[1] < 0 and never
E6 = len({(x - d) / x for x in xs[:200]}) == len(set(xs[:200])) and len({((1 - q)*x) / x for x in xs}) == 1
print('E1..E6:', E1, E2, E3, E4, E5, E6)
print('stride crosses the foot at stride', n, '(1/delta = 3600/7 = 514.29); best x for the share step', float(best_share),
      'vs 1/sqrt(1-q) =', (1 - float(q))**-0.5, '; best x for the stride', float(best_stride))
print('after 5000 fixed-share steps w =', tuple(float(c) for c in w(y)))
