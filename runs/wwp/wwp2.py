"""WWP run 2: Jaynes's restriction rule (1973, eq. 4) added. See plans/wwp-plan.md (P3').

A method answers each statement [a, b] with a law on it. The rule: on [a, c'] inside [a, b], the method's own law must
be its law on [a, b] conditioned on [a, c']. One density for the family passes by construction of conditioning; the
average of the answers over x and over 1/x renormalizes its mixture for each range. mpmath at 50 digits.
Run: python3 runs/wwp/wwp2.py   (a few seconds)
"""
import random
import mpmath as mp
mp.mp.dps = 50
M = mp.mpf
rng = random.Random(1973)
def verdict(ok): return "not killed" if ok else "KILLED"

def cdf_density(f):
    """a method that is one density f on every range: P(x <= c | [a, b])"""
    return lambda a, b, c: mp.quad(f, [a, min(c, b)]) / mp.quad(f, [a, b])
methods = {
    'levels': cdf_density(lambda x: 1 / x),
    'even share': cdf_density(lambda x: 1 / (1 + x) ** 2),
    'even turn': cdf_density(lambda x: 1 / (1 + x * x)),
    'hyperbola': cdf_density(lambda x: mp.sqrt(1 + 1 / x ** 4)),
    'average': lambda a, b, c: ((min(c, b) - a) / (b - a) + (1 / a - 1 / min(c, b)) / (1 / a - 1 / b)) / 2,
}
def restriction_gap(m, a, b, cp, c):
    """|the method on [a, cp] at c  -  its law on [a, b] conditioned on [a, cp], at c|, for a < c < cp < b"""
    direct = m(a, cp, c)
    conditioned = m(a, b, c) / m(a, b, cp)
    return abs(direct - conditioned)
gaps = {k: M(0) for k in methods}
for _ in range(50):
    a = M(10) ** M(rng.uniform(-2, 0)); b = a * M(10) ** M(rng.uniform(0.5, 3))
    cp = a + (b - a) * M(rng.uniform(0.3, 0.9)); c = a + (cp - a) * M(rng.uniform(0.2, 0.8))
    for k, m in methods.items():
        gaps[k] = max(gaps[k], restriction_gap(m, a, b, cp, c))
stated = restriction_gap(methods['average'], M(1) / 3, M(3), M(2), M(1))
single_ok = all(gaps[k] < M('1e-40') for k in methods if k != 'average')
avg_fails = stated > M('1e-6')
# the unit's change, as run 1: answers at lambda = 2 against lambda = 1 on Deakin's statement
def answer(m, lam): return m(lam / 3, 3 * lam, 2 * lam)
unit_ok = {k: abs(answer(m, M(2)) - answer(m, M(1))) < M('1e-40') for k, m in methods.items()}
both = [k for k in methods if unit_ok[k] and (gaps[k] < M('1e-40'))]
ok = single_ok and avg_fails and both == ['levels']
print(f"P3': {verdict(ok)}. restriction rule, worst gap over 50 nested ranges: "
      + ", ".join(f"{k} {mp.nstr(g, 3)}" for k, g in gaps.items())
      + f"; the average on [1/3, 2] at x = 1: direct {mp.nstr(methods['average'](M(1)/3, M(2), M(1)), 6)}, conditioned from [1/3, 3] "
      + f"{mp.nstr(methods['average'](M(1)/3, M(3), M(1)) / methods['average'](M(1)/3, M(3), M(2)), 6)}; unchanged by the unit: "
      + f"{[k for k in methods if unit_ok[k]]}; pass both: {both}")
