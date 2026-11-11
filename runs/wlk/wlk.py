"""WLK run 1: the even ladder on the walk to the mountain. Exact (fractions). Run from the repo root."""
import re, random
from fractions import Fraction as F
src = open('approach.html').read()
m = re.search(r'THUMB = ([\d.]+), ARM = ([\d.]+).*?STRIDE = ([\d.]+)', src)
THUMB, ARM, S = (F(x) for x in m.groups()); HL = THUMB / ARM
THINGS = {n: F(v) for n, v in re.findall(r"(\w+): \{ V: (\d+)", src)}
print('constants from approach.html: H/L =', HL, ' stride =', S, ' things =', {k: str(v) for k, v in THINGS.items()})
random.seed(11)
res = {}
def x_of(d, V, hl=HL): return d * hl / V          # h/v = d/d_c
for name, V in THINGS.items():
    dc = V / HL; delta = S / dc
    starts = [F(random.randint(1, 10**9), 10**6) % (16 * dc) + 2 * S for _ in range(1000)]
    # W1
    w1 = all(x_of(d, V) - x_of(d - S, V) == delta for d in starts)
    # W2
    count = 1 / delta; w2 = (count == dc / S) and (count * HL * S == V)
    js = re.search(r'stridesFromCorner = .*?=> (.*?);', src).group(1)
    # W3
    w3 = True; prev = None
    for n in range(2, 200):
        step = 1 / x_of((n - 1) * S, V) - 1 / x_of(n * S, V)
        w3 &= step == 1 / (delta * n * (n - 1))
        if prev is not None: w3 &= step < prev          # walking in, n falls, so steps grow: step(n) < step(n-1)... checked as n rises
        prev = step
    # W4
    w4 = True
    for k in (F(1, 100), F(7), F(100)):
        for d in starts[:50]:
            w4 &= x_of(k * d, k * V, (k * THUMB) / (k * ARM)) == x_of(d, V)
        w4 &= (k * S) / (k * V / HL) == delta                       # all scaled: same rung, same count
        w4 &= S / (k * V / HL) == delta / k                         # stride kept: the count moves by k
    # W5
    w5 = True
    for d in starts:
        x1, x2 = x_of(d, V), x_of(d - S, V)
        w5 &= x2 / (x1 - x2) == (d - S) / S and HL / (x1 - x2) == V / S
    # W6
    eps = F(1, 3) * S
    before = x_of(dc + eps + S, V) - x_of(dc + eps, V); across = x_of(dc + eps, V) - x_of(dc + eps - S, V)
    after = x_of(dc - eps, V) - x_of(dc - eps - S, V)
    w6 = before == across == after == delta
    res[name] = (w1, w2, w3, w4, w5, w6)
    print(f'{name}: V*={V} d_c={dc} delta={delta} count corner->foot={count} (= {float(count):.4f})  V* back = {count*HL*S}')
    print('   W1..W6:', res[name])
print('approach.html stridesFromCorner body:', js)
# W7: even in x and in ln x both: x, x-a, x-2a with (x-a)^2 = x(x-2a)  =>  a^2 = 0
w7 = all((x - a)**2 - x * (x - 2 * a) == a * a for x, a in
         ((F(random.randint(1, 10**6), 997), F(random.randint(-10**6, 10**6), 991)) for _ in range(1000)))
print('W7: (x-a)^2 - x(x-2a) = a^2 at 1000 random fractions:', w7, ' -> even in x and in ln x only at a = 0')
q = F(1, 10); xx = F(1); ok = True
for n in range(2000): xx *= (1 - q); ok &= xx > 0
print('W7: fixed share q=1/10, 2000 steps, x still > 0:', ok, ' x ~ %.3e' % float(xx))
print('ALL:', all(all(v) for v in res.values()) and ok and w7)
