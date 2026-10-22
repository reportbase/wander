"""TPR run 2: P2′ (plans/tpr-plan.md). The family w_a ∝ sin^a(2θ) at a = −0.9, −0.5, computed on [0, π/4] only, the
upper half folded onto it by the exchange θ ↦ π/2 − θ, so both singular ends sit at an exactly represented 0.
Run: python3 runs/tpr/tpr2.py | tee runs/tpr/tpr-run2.txt
"""
from mpmath import mp, mpf, pi, quad, sin, cos, nstr

mp.dps = 50
def Q(f, a, b):
    with mp.workdps(100):
        return +quad(f, [a, b])
run1 = {'-0.9': (mpf('0.530269309463401'), mpf('0.137798178978904')),
        '-0.5': (mpf('0.599070117367796'), mpf('0.456946581044464'))}
ok = True
for a_s, (c1, s1) in run1.items():
    a = mpf(a_s)
    lower = Q(lambda t: sin(2 * t) ** a, 0, pi / 4)
    upper = Q(lambda u: sin(2 * u) ** a, 0, pi / 4)   # the upper half, θ = π/2 − u, where sin 2θ = sin 2u
    total = lower + upper
    w = lambda t: sin(2 * t) ** a / total * (pi / 2)
    E = lambda f: Q(lambda t: (f(t) + f(pi / 2 - t)) * w(t), 0, pi / 4) / (pi / 2)
    Wq = lower / total
    ec2 = E(lambda t: cos(t) ** 2)
    ec, es = E(cos), E(lambda t: sin(2 * t))
    print(f"a = {a_s}: W(π/4) − ½ = {nstr(Wq - mpf(1)/2, 3)}; E[cos²θ] − ½ = {nstr(ec2 - mpf(1)/2, 3)}; "
          f"E[cos θ] = {nstr(ec, 20)} (run 1 {nstr(c1, 15)}); E[sin 2θ] = {nstr(es, 20)} (run 1 {nstr(s1, 15)})")
    ok &= abs(Wq - mpf(1) / 2) < mpf(10) ** -30 and abs(ec2 - mpf(1) / 2) < mpf(10) ** -30 \
        and abs(ec - c1) < mpf(10) ** -5 and abs(es - s1) < mpf(10) ** -5
print(f"P2′: {'not killed' if ok else 'KILLED'}")
