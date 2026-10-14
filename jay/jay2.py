"""JAY run 3: left and right Haar measures. See plans/jay-plan.md (P8).

Location and scale (x -> a x + b) is a group whose left- and right-invariant measures differ (1/a^2 and 1/a); the
reader's turns and rescalings commute, so they have one (1/lambda), and the exchange keeps it. Exact (fractions).
Run: python3 jay/jay2.py   (instant)
"""
from fractions import Fraction as F
import random
rng = random.Random(20261014)
def rat(lo=1, hi=60): return F(rng.randint(lo, hi), rng.randint(lo, hi))
def verdict(ok): return "not killed" if ok else "KILLED"

ok_a = True
left_right_mix = False
for _ in range(200):
    a, b = rat(), F(rng.randint(-60, 60), rng.randint(1, 9))       # the element g = (a, b)
    ah, bh = rat(), F(rng.randint(-60, 60), rng.randint(1, 9))     # the multiplier h
    # left: g -> h g = (ah a, ah b + bh); Jacobian of (a, b) -> (ah a, ah b + bh) is ah^2
    # right: g -> g h = (a ah, a bh + b); Jacobian of (a, b) -> (a ah, a bh + b) is det [[ah, 0], [bh, 1]] = ah
    La, Lb, Lj = ah * a, ah * b + bh, ah * ah
    Ra, Rb, Rj = a * ah, a * bh + b, ah
    left = lambda a_, b_: 1 / a_ ** 2
    right = lambda a_, b_: 1 / a_
    if left(a, b) != left(La, Lb) * Lj: ok_a = False
    if right(a, b) != right(Ra, Rb) * Rj: ok_a = False
    if ah != 1 and (left(a, b) == left(Ra, Rb) * Rj or right(a, b) == right(La, Lb) * Lj): left_right_mix = True
ok_a = ok_a and not left_right_mix

ok_b = True
for _ in range(200):
    al, lam, alh, lamh = rat(), rat(), rat(), rat()
    if (al + alh, lam * lamh) != (alh + al, lamh * lam): ok_b = False   # commutes
    f = lambda al_, lam_: 1 / lam_
    # left and right multiplication are the same map (al + alh, lam lamh), Jacobian lamh
    if f(al, lam) != f(al + alh, lam * lamh) * lamh: ok_b = False
    if f(al, lam) != f(alh + al, lamh * lam) * lamh: ok_b = False
    # the exchange (al, lam) -> (-al, 1/lam): Jacobian |-1| * 1/lam^2
    if f(al, lam) != f(-al, 1 / lam) * (1 / lam ** 2): ok_b = False
ok = ok_a and ok_b
print(f"P8: {verdict(ok)}. location and scale: left 1/a², right 1/a, exactly, and never each other's: {ok_a}; "
      f"turns and rescalings commute, left = right = 1/λ, the exchange keeps it, exactly: {ok_b}")
