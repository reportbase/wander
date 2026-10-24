"""Checks for the arrays paragraphs (SPN R484): Metropolis under a rescaled array,
the log-values' DC term, and the copy bound of geometric growth. Exact or seeded."""
import math, random
from fractions import Fraction

# 1. Metropolis-Hastings uses only ratios: rescaling the weights by k changes no step,
#    and only the normalizing constant Z moves (by k).
def mh_chain(w, steps, seed):
    rng = random.Random(seed); x = 0; out = []
    for _ in range(steps):
        y = (x + rng.choice((-1, 1))) % len(w)
        if rng.random() < min(1.0, w[y] / w[x]): x = y
        out.append(x)
    return out
w = [math.exp(math.sin(i / 3.0)) for i in range(40)]
for k in (1e-6, 7.0, 1e9):
    same = mh_chain(w, 20000, 1) == mh_chain([k * a for a in w], 20000, 1)
    print(f"MH k={k:g}: chain identical {same}; Z ratio {sum(k*a for a in w)/sum(w):.6g}")

# exact version on rationals: acceptance ratios unchanged
wq = [Fraction(i * i + 1) for i in range(10)]; kq = Fraction(355, 113)
print("exact ratios unchanged:", all((kq*wq[j])/(kq*wq[i]) == wq[j]/wq[i] for i in range(10) for j in range(10)))

# 2. ln of values minus their mean is unchanged by a common factor; the mean (DC) moves by ln k.
v = [math.exp(0.3 * math.cos(2 * t) + 0.1 * math.cos(3 * t)) * 5.0 for t in [2 * math.pi * i / 64 for i in range(64)]]
def shape(a):
    l = [math.log(x) for x in a]; m = sum(l) / len(l); return [x - m for x in l], m
s1, m1 = shape(v)
for k in (1e-3, 7.0, 1e6):
    s2, m2 = shape([k * x for x in v])
    print(f"DC k={k:g}: shape max diff {max(abs(a-b) for a, b in zip(s1, s2)):.1e}; DC moved {m2-m1:.12f} (ln k {math.log(k):.12f})")

# 3. Geometric growth by factor g: total element copies over N appends, against g*N/(g-1).
def copies(N, g):
    cap, n, c = 1, 0, 0
    for _ in range(N):
        if n == cap:
            c += n; cap = max(cap + 1, math.ceil(cap * g))
        n += 1
    return c
for g in (2.0, 1.5, 1.25):
    worst = max(copies(N, g) / N for N in range(1, 200001, 997))
    print(f"g={g}: worst copies/N {worst:.4f}, bound g/(g-1) = {g/(g-1):.4f}")
lin = copies(20000, None) if False else None
def copies_add(N, step):
    cap, n, c = step, 0, 0
    for _ in range(N):
        if n == cap: c += n; cap += step
        n += 1
    return c
for N in (10000, 20000, 40000):
    print(f"fixed step 64, N={N}: copies/N {copies_add(N, 64)/N:.1f}")

# 4. Worked example (R485): K = 8 slots laid by the uniform turn; index from a reading s = v/h by
#    k = floor(K * (2/pi) * atan2(v, h)), the horizon clamped to the last slot.
K = 8
def idx(v, h): return min(K - 1, math.floor(K * (2 / math.pi) * math.atan2(v, h)))
print("bounds tan(k*pi/16):", [round(math.tan(k * math.pi / (2 * K)), 4) for k in range(K + 1)][:-1] + ['inf'])
print("slot middles (Cauchy quantiles):", [round(math.tan((k + 0.5) * math.pi / (2 * K)), 4) for k in range(K)])
for s in (0.1, 0.5, 1.0, 2.0, 3.0, 10.0, 1000.0):
    g = (2 / math.pi) * math.atan(s)
    print(f"s={s:g}: g={g:.4f} k={idx(s,1)}  reciprocal 1/s -> k={idx(1,s)}  sum {idx(s,1)+idx(1,s)}")
print("horizon v=1,h=0 ->", idx(1, 0), "; home v=0,h=1 ->", idx(0, 1))
for kk in (1e-3, 7, 1e6): print(f"scaled by {kk:g}: s=3 ->", idx(3 * kk, kk))
# the central sweep: the same point at central angle phi = 2*theta, index floor(K*phi/pi)
for s in (0.1, 0.5, 2.0, 10.0):
    th = math.atan(s); phi = 2 * th
    print(f"s={s:g}: inscribed k={idx(s,1)}, central floor(K*phi/pi)={min(K-1, math.floor(K*phi/math.pi))}")
# situation 2 against the turn: amounts x on [0, X], count index floor(N x/X) needs X; turn index needs H
N, X, H = 8, 100.0, 10.0
for x in (10, 50, 99):
    print(f"x={x}: count index {math.floor(N*x/X)}, turn index at H=10 {idx(x, H)}, at H=50 {idx(x, 50)}")
