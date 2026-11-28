# BNT run 1: Born's weight as the read's share, on Weihs et al. 1998's CHSH counts
# (as tabulated in Gill, arXiv:2209.00702v3, Appendix E). Predictions in plans/bnt-plan.md.
from math import sqrt, erfc
from scipy.stats import chi2, norm

# rows: Alice + / -, columns: Bob + / -
W = {(1,1): [[1683, 418], [361, 1578]],
     (1,2): [[1100, 269], [156, 1386]],
     (2,1): [[1728, 313], [351, 1978]],
     (2,2): [[179, 1636], [1143, 294]]}
sign = {(1,1): 1, (1,2): 1, (2,1): 1, (2,2): -1}   # the CHSH pattern: three alike, one opposite

def corr(m):
    n = sum(map(sum, m)); E = (m[0][0] + m[1][1] - m[0][1] - m[1][0]) / n
    return E, sqrt((1 - E*E) / n), n

print("setting   N      E        sd")
Es = {}
for k, m in W.items():
    E, s, n = corr(m); Es[k] = (E, s); print(k, n, f"{E:+.4f} {s:.4f}")

# P1: one visibility, E = sign * v / sqrt(2)
w = [1/s**2 for (_, s) in Es.values()]
x = [sign[k]*E*sqrt(2) for k, (E, _) in Es.items()]       # each an estimate of v
sx = [s*sqrt(2) for (_, s) in Es.values()]
wv = [1/q**2 for q in sx]
v = sum(a*b for a, b in zip(wv, x)) / sum(wv); sv = 1/sqrt(sum(wv))
c2 = sum(((a - v)/q)**2 for a, q in zip(x, sx)); p1 = chi2.sf(c2, 3)
print(f"\nP1: v = {v:.4f} ± {sv:.4f}; chi2 = {c2:.2f} on 3, p = {p1:.3g}; v above 1 by {(v-1)/sv:+.1f} sd")

# P2: S against the linear share's bound 2
S = sum(sign[k]*E for k, (E, _) in Es.items()); sS = sqrt(sum(s*s for (_, s) in Es.values()))
print(f"P2: S = {S:.4f} ± {sS:.4f}; (S - 2)/sd = {(S-2)/sS:.1f}")
print(f"    Born at this v: 2*sqrt(2)*v = {2*sqrt(2)*v:.4f}; linear share at v = 1: 2")
# the linear share's best fit, E = sign * u / 2, u free
xl = [sign[k]*E*2 for k, (E, _) in Es.items()]; sl = [s*2 for (_, s) in Es.values()]
wl = [1/q**2 for q in sl]; u = sum(a*b for a, b in zip(wl, xl))/sum(wl); su = 1/sqrt(sum(wl))
print(f"    linear share fitted: u = {u:.4f} ± {su:.4f} (needs u <= 1: above by {(u-1)/su:.1f} sd)")

# P3: each side's marginal does not depend on the other side's setting
def two_prop(a, n1, b, n2):
    p = (a + b)/(n1 + n2); z = (a/n1 - b/n2)/sqrt(p*(1-p)*(1/n1 + 1/n2)); return a/n1, b/n2, z, erfc(abs(z)/sqrt(2))
print("\nP3:")
for i in (1, 2):
    m1, m2 = W[(i,1)], W[(i,2)]
    a = sum(m1[0]); n1 = sum(map(sum, m1)); b = sum(m2[0]); n2 = sum(map(sum, m2))
    pa, pb, z, p = two_prop(a, n1, b, n2); print(f"  Alice {i}: P(+) {pa:.4f} vs {pb:.4f}, z {z:+.2f}, p {p:.3g}")
for j in (1, 2):
    m1, m2 = W[(1,j)], W[(2,j)]
    a = m1[0][0] + m1[1][0]; n1 = sum(map(sum, m1)); b = m2[0][0] + m2[1][0]; n2 = sum(map(sum, m2))
    pa, pb, z, p = two_prop(a, n1, b, n2); print(f"  Bob {j}:   P(+) {pa:.4f} vs {pb:.4f}, z {z:+.2f}, p {p:.3g}")
