"""MGP run 2: a fifth scale-nuisance model, Weibull with shape zeta and scale kappa. See plans/mgp-plan.md (P4').

As mgp.py: B1 integrates kappa out under kappa^(-k); B2 uses the law of the ratios by the integral over the scale group.
Run: python3 mgp/mgp2.py   (about fifteen minutes)
"""
import random
import mpmath as mp
mp.mp.dps = 50
M = mp.mpf
rng = random.Random(1973)
INF = mp.inf
KS = [M(0), M('0.5'), M(1), M('1.5'), M(2)]
def verdict(ok): return "not killed" if ok else "KILLED"
n = 4
def lik(zeta, kap, ls):
    out = M(1)
    for l in ls:
        w = l / kap
        out *= zeta * w ** (zeta - 1) * mp.exp(-w ** zeta) / kap
    return out
def ratio(k, zeta, ls):
    a = mp.quad(lambda kp: lik(zeta, kp, ls) * kp ** (-k), [0, 1, INF])
    b = mp.quad(lambda lam: lam ** (n - 1) * lik(zeta, M(1), [lam * l for l in ls]), [0, 1, INF])
    return a / b
ls = [tuple([M(1)] + [M(rng.uniform(0.2, 4)) for _ in range(n - 1)]) for _ in range(50)]
zt = [M(rng.uniform(0.6, 4)) for _ in range(20)]
out = {}
for k in KS:
    R = [[ratio(k, t, d) for d in ls] for t in zt]
    spread = max(max(abs(r / row[0] - 1) for r in row) for row in R)
    gap = max(abs(R[i][p] * R[0][0] / (R[i][0] * R[0][p]) - 1) for i in range(len(zt)) for p in range(len(ls)))
    out[k] = (spread, gap)
ok = out[M(1)][0] < M('1e-30') and all(out[k][0] > M('1e-6') and out[k][1] > M('1e-6') for k in KS if k != 1)
print(f"P4': {verdict(ok)}. Weibull, shape of interest, scale nuisance: "
      + "; ".join(f"k = {mp.nstr(k, 2)}: a/b spread {mp.nstr(s, 3)}, factorization gap {mp.nstr(g, 3)}" for k, (s, g) in out.items()))
