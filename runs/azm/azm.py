"""AZM: V2 as the azimuth, the hand's second sweep. See plans/azm-plan.md (P1-P6).

The reader's horizon coordinates: altitude a from the horizontal up to the vertical v (the sweep from H to V), azimuth z
round the horizontal plane from the forward direction h to v2 square to it (the sweep that brings in V2). The direction
is (h, v, v2) = (cos a cos z, sin a, cos a sin z). mpmath at 60 digits; a direct count on a midpoint grid and
a seeded sample where the plan says so.
Run: python3 runs/azm/azm.py   (about a minute; needs mpmath)
"""
import math, random
import mpmath as mp
mp.mp.dps = 60
M = mp.mpf
PI = mp.pi
def verdict(ok): return "not killed" if ok else "KILLED"
results = {}
def direction(a, z): return (mp.cos(a) * mp.cos(z), mp.sin(a), mp.cos(a) * mp.sin(z))

# ---------------------------------------------------------------- P1: each sweep reads its own pair
w1 = M(0)
for i in range(200):
    for j in range(200):
        a, z = (i + M('0.5')) / 200 * PI / 2, (j + M('0.5')) / 200 * PI / 2
        h, v, v2 = direction(a, z)
        w1 = max(w1, abs(v2 / h - mp.tan(z)), abs(v / mp.sqrt(h * h + v2 * v2) - mp.tan(a)), abs(h * h + v * v + v2 * v2 - 1))
results['P1'] = (w1 < M('1e-50'), f"v2/h = tan z, v/√(h² + v2²) = tan a, h² + v² + v2² = 1; worst {mp.nstr(w1, 3)}")

# ---------------------------------------------------------------- P2: an even azimuth keeps its own pair's corner
# P(v2 <= h) = P(z <= 45°) under any altitude weight independent of z; computed as a double integral to be honest
def prob(indicator_z_limit, alt_weight):
    """P over z even on [0, pi/2] and a with density alt_weight on [0, pi/2] of the event z <= limit(a)."""
    norm = mp.quad(alt_weight, [0, PI / 2])
    return mp.quad(lambda a: alt_weight(a) * indicator_z_limit(a) / (PI / 2), [0, PI / 2]) / norm
weights = {"even in a": lambda a: M(1), "even in height": lambda a: mp.cos(a), "cos² a": lambda a: mp.cos(a) ** 2}
w2 = M(0)
p2 = {}
for name, wgt in weights.items():
    p = prob(lambda a: PI / 4, wgt)
    p2[name] = p; w2 = max(w2, abs(p - M('0.5')))
# altitude's own pair with a even: P(v <= horizontal reach) = P(a <= 45°)
p_alt = mp.quad(lambda z: mp.quad(lambda a: 1, [0, PI / 4]) / (PI / 2), [0, PI / 2]) / (PI / 2)
w2 = max(w2, abs(p_alt - M('0.5')))
results['P2'] = (w2 < M('1e-40'), f"P(v2 ≤ h) = ½ under each altitude weight, P(v ≤ reach) = ½; worst {mp.nstr(w2, 3)}")

# ---------------------------------------------------------------- P3: even in both angles is not the even octant
I_full = mp.quad(lambda z: mp.atan(mp.cos(z)), [0, PI / 2])
I_half = mp.quad(lambda z: mp.atan(mp.cos(z)), [0, PI / 4])
p_vh = 4 / PI ** 2 * I_full
p_v2v = 1 - p_vh
p_near = 4 / PI ** 2 * I_half
N = 2000
c_vh = c_v2v = c_near = 0
for i in range(N):
    a = (i + 0.5) / N * math.pi / 2
    ca, sa = math.cos(a), math.sin(a)
    for j in range(N):
        z = (j + 0.5) / N * math.pi / 2
        h, v, v2 = ca * math.cos(z), sa, ca * math.sin(z)
        c_vh += v <= h; c_v2v += v2 <= v; c_near += (h >= v and h >= v2)
g = [c / N ** 2 for c in (c_vh, c_v2v, c_near)]
d3 = max(abs(float(p_vh) - g[0]), abs(float(p_v2v) - g[1]), abs(float(p_near) - g[2]))
ok3 = d3 <= 2e-5 and p_vh < M('0.4') and p_near < M('0.3')
results['P3'] = (ok3, f"P(v ≤ h) = {mp.nstr(p_vh, 10)}, P(v2 ≤ v) = {mp.nstr(p_v2v, 10)}, near field {mp.nstr(p_near, 10)}; "
                      f"grid {g[0]:.6f}, {g[1]:.6f}, {g[2]:.6f}; closed forms vs grid {d3:.1e}")

# ---------------------------------------------------------------- P4: Archimedes; even area is even in azimuth and height
random.seed(4)
w4 = M(0)
for _ in range(100):
    z1, z2 = sorted(M(random.uniform(0, math.pi / 2)) for _ in range(2))
    v1, v2_ = sorted(M(random.uniform(0, 1)) for _ in range(2))
    a1, a2 = mp.asin(v1), mp.asin(v2_)
    area = mp.quad(lambda a: mp.cos(a), [a1, a2]) * (z2 - z1)          # the sphere's element cos a da dz
    w4 = max(w4, abs(area - (z2 - z1) * (v2_ - v1)))
results['P4'] = (w4 < M('1e-45'), f"100 patches: area = Δz·Δv to {mp.nstr(w4, 3)} (Lambert's map equal-area; altitude density cos a)")

# ---------------------------------------------------------------- P5: swept even in azimuth and height, every pair at its corner
# P(v <= h): v <= cos z·√(1 - v²)  <=>  v <= cos z/√(1 + cos² z)
P_vh = 2 / PI * mp.quad(lambda z: mp.cos(z) / mp.sqrt(1 + mp.cos(z) ** 2), [0, PI / 2])
P_v2h = 2 / PI * mp.quad(lambda z: 1, [0, PI / 4])                     # v2 <= h: z <= 45°
P_vv2 = 2 / PI * mp.quad(lambda z: mp.sin(z) / mp.sqrt(1 + mp.sin(z) ** 2), [0, PI / 2])
P_near = 2 / PI * mp.quad(lambda z: mp.cos(z) / mp.sqrt(1 + mp.cos(z) ** 2), [0, PI / 4])
w5 = max(abs(P_vh - M('0.5')), abs(P_v2h - M('0.5')), abs(P_vv2 - M('0.5')), abs(P_near - M(1) / 3))
def joint_sweeps(A, B):
    return 2 / PI * mp.quad(lambda z: A * mp.cos(z) / mp.sqrt(1 + A * A * mp.cos(z) ** 2), [0, mp.atan(B)])
def joint_cauchy(A, B):
    return mp.quad(lambda a: mp.quad(lambda b: 2 / (PI * (1 + a * a + b * b) ** M('1.5')), [0, B]), [0, A])
w5c = M(0)
for A, B in ((M(1), M(1)), (M(2), M('0.5')), (M('0.5'), M(3)), (M(10), M(10))):
    w5c = max(w5c, abs(joint_sweeps(A, B) - joint_cauchy(A, B)))
results['P5'] = (w5 < M('1e-40') and w5c < M('1e-30'),
                 f"medians ½, ½, ½ and near field ⅓ to {mp.nstr(w5, 3)}; joint law = the 2D half-Cauchy to {mp.nstr(w5c, 3)}")

# ---------------------------------------------------------------- P6: the hat-box belongs to three unit relations
random.seed(6)
S, BINS = 10 ** 6, 10
dens = {2: lambda t: 2 / PI / mp.sqrt(1 - t * t),
        3: lambda t: M(1),
        4: lambda t: 4 / PI * mp.sqrt(1 - t * t)}
def bin_prob(k, f):                                                   # exact bin probability of the stated density
    return float(mp.quad(f, [M(k) / BINS, M(k + 1) / BINS]))
worst6, detail6 = 0.0, []
for n, f in dens.items():
    counts = [0] * BINS
    for _ in range(S):
        x = [abs(random.gauss(0, 1)) for _ in range(n)]
        r = math.sqrt(sum(c * c for c in x))
        t = x[1] / r                                                  # the height: one coordinate of an even direction
        counts[min(int(t * BINS), BINS - 1)] += 1
    zs = []
    for k in range(BINS):
        p = bin_prob(k, f)
        se = math.sqrt(p * (1 - p) / S)
        zs.append(abs(counts[k] / S - p) / se)
    worst6 = max(worst6, max(zs)); detail6.append(f"{n} relations: worst {max(zs):.2f} s.e.")
results['P6'] = (worst6 <= 4, "; ".join(detail6) + " (densities (2/π)/√(1 − t²), 1, (4/π)√(1 − t²))")

for k, (ok, msg) in results.items():
    print(f"{k}: {verdict(ok)}. {msg}")
