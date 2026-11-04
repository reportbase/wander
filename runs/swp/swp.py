# SWP run 1: the shape swept whole, not the thumbs one by one (plans/swp-plan.md). mpmath at 50 digits, one seeded sample.
import mpmath as mp, numpy as np
mp.mp.dps = 50
ok = lambda c: 'not killed' if c else 'KILLED'
pi = mp.pi
rng = np.random.default_rng(20261105)
N = 1_000_000
def within(p_hat, p, n=N):            # a sampled share within 4 standard errors of its prediction
    se = np.sqrt(float(p) * (1 - float(p)) / n); return abs(p_hat - float(p)) <= 4 * se, (p_hat - float(p)) / se

# ---- W1: each thumb swept on its own, pan then tilt: n = (cos a cos ψ, sin a, cos a sin ψ), a, ψ even and independent
pv = (4 / pi**2) * mp.quad(lambda p: mp.atan(mp.cos(p)), [0, pi / 2])            # P(tan a <= cos ψ) = P(v <= h)
pvv2 = (4 / pi**2) * mp.quad(lambda p: mp.atan(mp.sin(p)), [0, pi / 2])          # P(v <= v2)
# near field: h largest: v <= h and v2 <= h  <=>  ψ <= π/4 and tan a <= cos ψ
near = (4 / pi**2) * mp.quad(lambda p: mp.atan(mp.cos(p)), [0, pi / 4])
print('W1 P(v2<=h) = 1/2 exactly (ψ <= 45°); P(v<=h) =', mp.nstr(pv, 15), '; P(v<=v2) =', mp.nstr(pvv2, 15), '; near field', mp.nstr(near, 15))
W1 = abs(pv - mp.mpf('0.342585')) < 5e-6 and abs(pv - pvv2) < 1e-40 and abs(near - mp.mpf('0.2326')) < 5e-5
print('W1', ok(W1))

# ---- W2: the shape swept whole: uniform turns (unit quaternions), the frame turned; the direction carried home is R^T e1 ...
# equivalently a uniform direction; take the look's image of a fixed direction under a uniform turn, folded into the octant
q = rng.standard_normal((N, 4)); q /= np.linalg.norm(q, axis=1, keepdims=True)
w, x, y, z = q.T
# R applied to d = (1,0,0): first column of the rotation matrix
d = np.stack([1 - 2 * (y * y + z * z), 2 * (x * y + w * z), 2 * (x * z - w * y)], 1)
n = np.abs(d)                                         # the octant: the wedge faced another way is the same wedge (R240)
h, v, v2 = n.T
res = {'v<=h': (v <= h).mean(), 'v2<=h': (v2 <= h).mean(), 'v2<=v': (v2 <= v).mean(), 'near': ((v <= h) & (v2 <= h)).mean(),
       'chamber h>v>v2': ((h >= v) & (v >= v2)).mean()}
exp = {'v<=h': 0.5, 'v2<=h': 0.5, 'v2<=v': 0.5, 'near': 1 / 3, 'chamber h>v>v2': 1 / 6}
W2 = True
for k in res:
    good, zz = within(res[k], exp[k]); W2 &= good; print(f'W2 {k:15s} {res[k]:.5f} vs {exp[k]:.5f}  ({zz:+.2f} se)')
print('W2', ok(W2))

# ---- W3: the laws in the readings (s, s2) = (v/h, v2/h)
f_pt = lambda s, t: (4 / pi**2) / (mp.sqrt(1 + t * t) * (1 + s * s + t * t))
f_wh = lambda s, t: (2 / pi) * (1 + s * s + t * t) ** mp.mpf(-1.5)
I_pt = mp.quad(lambda t: mp.quad(lambda s: f_pt(s, t), [0, 1, mp.inf]), [0, 1, mp.inf])
I_wh = mp.quad(lambda t: mp.quad(lambda s: f_wh(s, t), [0, 1, mp.inf]), [0, 1, mp.inf])
ratio = f_pt(1, 0) / f_pt(0, 1)
print('W3 totals', mp.nstr(I_pt, 20), mp.nstr(I_wh, 20), '; thumb-by-thumb f(1,0)/f(0,1) =', mp.nstr(ratio, 20), '(√2 =', mp.nstr(mp.sqrt(2), 20), ')')
W3 = abs(I_pt - 1) < 1e-20 and abs(I_wh - 1) < 1e-20 and abs(ratio - mp.sqrt(2)) < 1e-20
# sampled cells: whole from the quaternion sample; thumb-by-thumb from even angles
a = rng.uniform(0, np.pi / 2, N); ps = rng.uniform(0, np.pi / 2, N)
hp, vp, v2p = np.cos(a) * np.cos(ps), np.sin(a), np.cos(a) * np.sin(ps)
S_wh, T_wh = v / h, v2 / h; S_pt, T_pt = vp / hp, v2p / hp
cells = [((0, 0.5), (0, 0.5)), ((0.5, 1.5), (0, 0.5)), ((0, 0.5), (0.5, 1.5)), ((1, 3), (1, 3))]
for (s0, s1), (t0, t1) in cells:
    p_pt = mp.quad(lambda t: mp.quad(lambda s: f_pt(s, t), [s0, s1]), [t0, t1])
    p_wh = mp.quad(lambda t: mp.quad(lambda s: f_wh(s, t), [s0, s1]), [t0, t1])
    m_pt = ((S_pt >= s0) & (S_pt < s1) & (T_pt >= t0) & (T_pt < t1)).mean()
    m_wh = ((S_wh >= s0) & (S_wh < s1) & (T_wh >= t0) & (T_wh < t1)).mean()
    g1, z1 = within(m_pt, p_pt); g2, z2 = within(m_wh, p_wh); W3 &= g1 and g2
    print(f'W3 cell s∈[{s0},{s1}) s2∈[{t0},{t1}): thumbs {m_pt:.5f} vs {float(p_pt):.5f} ({z1:+.2f}), whole {m_wh:.5f} vs {float(p_wh):.5f} ({z2:+.2f})')
print('W3', ok(W3))

# ---- W4: the whole sweep written in the thumbs' angles: even in ψ and in height sin a; the thumb-by-thumb density against it
# per unit solid angle on the octant: uniform 2/π; thumb-by-thumb (4/π²) / cos a  (dΩ = cos a da dψ)
ratio_at = lambda sin_a: (2 / pi) / mp.sqrt(1 - sin_a**2)
c_diag = ratio_at(1 / mp.sqrt(3))
print('W4 thumb-by-thumb over uniform: horizon', mp.nstr(ratio_at(0), 12), '; down the diagonal', mp.nstr(c_diag, 12),
      '(2/π·√(3/2) =', mp.nstr(2 / pi * mp.sqrt(mp.mpf(3) / 2), 12), '); at sin a = 0.999999', mp.nstr(ratio_at(mp.mpf('0.999999')), 6))
# the quaternion sample's height sin a = v is even, its azimuth atan2(v2, h) even
Wh = abs(np.histogram(v, bins=10, range=(0, 1))[0] / N - 0.1).max() < 4 * np.sqrt(0.09 / N)
Wz = abs(np.histogram(np.arctan2(v2, h), bins=10, range=(0, np.pi / 2))[0] / N - 0.1).max() < 4 * np.sqrt(0.09 / N)
W4 = abs(ratio_at(0) - 2 / pi) < 1e-40 and abs(c_diag - 2 / pi * mp.sqrt(mp.mpf(3) / 2)) < 1e-40 and Wh and Wz
print('W4 whole sweep even in height', Wh, ', even in azimuth', Wz, ';', ok(W4))

# ---- W5: order. tilt then pan: n' = (cos a cos ψ, sin a cos ψ, sin ψ)
pv_tp = (4 / pi**2) * mp.quad(lambda p: mp.mpf(1) * pi / 4, [0, pi / 2])       # sin a cos ψ <= cos a cos ψ  <=> a <= 45°
pv2_tp = (4 / pi**2) * mp.quad(lambda aa: mp.atan(mp.cos(aa)), [0, pi / 2])    # sin ψ <= cos a cos ψ  <=> tan ψ <= cos a
print('W5 tilt-then-pan: P(v<=h) =', mp.nstr(pv_tp, 15), '; P(v2<=h) =', mp.nstr(pv2_tp, 15))
def Rx(t): c, s = mp.cos(t), mp.sin(t); return mp.matrix([[1, 0, 0], [0, c, -s], [0, s, c]])
def Ry(t): c, s = mp.cos(t), mp.sin(t); return mp.matrix([[c, 0, s], [0, 1, 0], [-s, 0, c]])
def Rz(t): c, s = mp.cos(t), mp.sin(t); return mp.matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])
def axis_angle(R):
    tr = R[0, 0] + R[1, 1] + R[2, 2]; ang = mp.acos((tr - 1) / 2)
    ax = mp.matrix([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]); ax = ax / mp.norm(ax); return ax, ang
A = Rx(pi / 2) * Ry(pi / 2); B = Ry(pi / 2) * Rx(pi / 2)
axA, angA = axis_angle(A); axB, angB = axis_angle(B); axC, angC = axis_angle(A * B.T)
deg = lambda r: r * 180 / pi
print('W5 e1 then e2:', mp.nstr(deg(angA), 15), '° about', [mp.nstr(c, 6) for c in axA], '; other order:', mp.nstr(deg(angB), 15), '° about', [mp.nstr(c, 6) for c in axB])
print('W5 the two poses differ by a turn of', mp.nstr(deg(angC), 15), '°')
W5 = (abs(pv_tp - mp.mpf(1) / 2) < 1e-40 and abs(pv2_tp - pv) < 1e-40 and abs(deg(angA) - 120) < 1e-12 and abs(deg(angB) - 120) < 1e-12
      and mp.norm(axA - axB) > 0.1 and abs(deg(angC) - 120) < 1e-12)
# Haar unchanged by composing with a fixed turn: left and right composition of the sample keeps the shares
Fq = np.array([np.cos(0.4), np.sin(0.4) * 0.6, np.sin(0.4) * 0.8, 0.0])       # a fixed turn
def qmul(p, r):
    a1, b1, c1, d1 = p.T if p.ndim == 2 else p; a2, b2, c2, d2 = r.T if r.ndim == 2 else r
    return np.stack([a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                     a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2], -1)
def near_of(qq):
    w, x, y, z = qq.T; dd = np.abs(np.stack([1 - 2 * (y * y + z * z), 2 * (x * y + w * z), 2 * (x * z - w * y)], 1)); hh, vv, ww = dd.T
    return ((vv <= hh) & (ww <= hh)).mean(), (vv <= hh).mean()
for name, qq in (('fixed∘R', qmul(np.broadcast_to(Fq, q.shape), q)), ('R∘fixed', qmul(q, np.broadcast_to(Fq, q.shape)))):
    nr, vh = near_of(qq); g1, _ = within(nr, 1 / 3); g2, _ = within(vh, 0.5); W5 &= g1 and g2
    print(f'W5 {name}: near {nr:.5f}, v<=h {vh:.5f}')
print('W5', ok(W5))

# ---- W6: every thumb-by-thumb pose is one turn of the frame
W6 = True
for (aa, pp) in ((0.3, 1.1), (1.2, 0.2), (0.7, 0.7)):
    R = Ry(-mp.mpf(pp)) * Rz(mp.mpf(aa))                    # pan about the up thumb, tilt toward it: carries e1 to n
    nvec = R * mp.matrix([1, 0, 0])
    want = mp.matrix([mp.cos(aa) * mp.cos(pp), mp.sin(aa), mp.cos(aa) * mp.sin(pp)])
    orth = mp.norm(R.T * R - mp.eye(3)); det = mp.det(R); ax, an = axis_angle(R)
    fixed = mp.norm(R * ax - ax)
    W6 &= mp.norm(nvec - want) < 1e-40 and orth < 1e-40 and abs(det - 1) < 1e-40 and fixed < 1e-40
    print(f'W6 a={aa}, ψ={pp}: carries e1 to n {mp.nstr(mp.norm(nvec - want), 3)}, |RᵀR−I| {mp.nstr(orth, 3)}, det {mp.nstr(det, 20)}, one turn {mp.nstr(deg(an), 10)}° (axis fixed {mp.nstr(fixed, 3)})')
print('W6', ok(W6))

# ---- W7: marks carried
LOOK = mp.matrix([1, 1, 1]) / mp.sqrt(3); E1s = mp.matrix([1, -1, 0]) / mp.sqrt(2); E2s = mp.matrix([-1, -1, 2]) / mp.sqrt(6)
def screen(u, R):
    L, a1, a2 = R * LOOK, R * E1s, R * E2s; dd = (u.T * L)[0]; return mp.sqrt(((u.T * a1)[0] / dd)**2 + ((u.T * a2)[0] / dd)**2)
W7 = True
for R in (Rx(mp.mpf('0.37')) * Ry(mp.mpf('1.9')) * Rz(mp.mpf('-0.8')), A, Rz(mp.mpf(2))):
    nn = mp.matrix([mp.mpf('0.3'), mp.mpf('0.5'), mp.mpf('0.81')]); nn = nn / mp.norm(nn)
    E = [mp.matrix([1, 0, 0]), mp.matrix([0, 1, 0]), mp.matrix([0, 0, 1])]
    dr = max(abs(((R * nn).T * (R * e))[0] - (nn.T * e)[0]) for e in E)
    rt = [screen(R * e, R) for e in E]; rh = [screen(R * (E[i] + E[j]) / mp.sqrt(2), R) for i, j in ((0, 1), (1, 2), (0, 2))]
    W7 &= dr < 1e-40 and all(abs(r - mp.sqrt(2)) < 1e-40 for r in rt) and all(abs(r - 1 / mp.sqrt(2)) < 1e-40 for r in rh)
    print('W7 readings moved', mp.nstr(dr, 3), '; thumbs at', [mp.nstr(r, 15) for r in rt], '; homes at', [mp.nstr(r, 15) for r in rh])
print('W7', ok(W7))

# ---- W8: the plane
t1, t2 = mp.mpf('0.4'), mp.mpf('1.1')
R2 = lambda t: mp.matrix([[mp.cos(t), -mp.sin(t)], [mp.sin(t), mp.cos(t)]])
comm = mp.norm(R2(t1) * R2(t2) - R2(t2) * R2(t1))
W8 = comm < 1e-40
print('W8 plane turns commute', mp.nstr(comm, 3), '; the even turn its own Haar measure; pair at ½ by the exchange;', ok(W8))

# ---- W9: any linear map of the thumbs' space keeps the family (an elliptical 2D Cauchy on the screen square to e1)
W9 = True
Y = rng.standard_normal((N, 3))
for seed in (1, 2, 3):
    M = np.random.default_rng(seed).standard_normal((3, 3))
    Z = Y @ M.T; s = Z[:, 1:] / Z[:, :1]
    C = M @ M.T; b = C[1:, 0] / C[0, 0]; Sg = (C[1:, 1:] - np.outer(C[1:, 0], C[0, 1:]) / C[0, 0]) / C[0, 0]
    worst = 0
    for th in np.linspace(0, np.pi, 8, endpoint=False):
        u = np.array([np.cos(th), np.sin(th)]); p = s @ u; g = np.sqrt(u @ Sg @ u); m0 = u @ b
        # the share below the predicted median and within the predicted quartiles, each a binomial count
        for share_hat, share in (((p <= m0).mean(), 0.5), (((p > m0 - g) & (p <= m0 + g)).mean(), 0.5)):
            good, zz = within(share_hat, share); worst = max(worst, abs(zz)); W9 &= good
    print(f'W9 map {seed}: location {np.round(b, 4)}, scatter {np.round(Sg, 4).tolist()}, worst of 16 shares {worst:.2f} se')
# a turn keeps the round hill (scatter the identity, location 0)
Q, _ = np.linalg.qr(np.random.default_rng(9).standard_normal((3, 3))); C = Q @ Q.T
Sg = (C[1:, 1:] - np.outer(C[1:, 0], C[0, 1:]) / C[0, 0]) / C[0, 0]; b = C[1:, 0] / C[0, 0]
print('W9 a turn: location', np.round(b, 4), 'scatter', np.round(Sg, 4).tolist(), '(a turn of the screen about its point: round; the look itself moves)')
print('W9', ok(W9))

# ---- W10: stacking. cf of an elliptical Cauchy: exp(-γ√(kᵀΣk)) (location 0)
S1 = mp.matrix([[1, 0], [0, 1]]); S2 = mp.matrix([[4, 1], [1, 1]])
q_ = lambda S, k: mp.sqrt((k.T * S * k)[0])
ks = [mp.matrix([1, 0]), mp.matrix([0, 1]), mp.matrix([1, 1]) / mp.sqrt(2)]
same = max(abs(mp.mpf('0.7') * q_(S2, k) + mp.mpf('1.6') * q_(S2, k) - mp.mpf('2.3') * q_(S2, k)) for k in ks)
# different shapes: fit Σ' on three directions from (√(kΣ1k) + √(kΣ2k))², test a fourth
tgt = lambda k: (q_(S1, k) + q_(S2, k))**2
s11 = tgt(ks[0]); s22 = tgt(ks[1]); s12 = tgt(ks[2]) - (s11 + s22) / 2
Sp = mp.matrix([[s11, s12], [s12, s22]])
k4 = mp.matrix([1, -2]) / mp.sqrt(5)
miss = abs(q_(Sp, k4) - (q_(S1, k4) + q_(S2, k4)))
print('W10 one shape, γ 0.7 + 1.6:', mp.nstr(same, 3), 'from 2.3 ; two shapes: the Σ\' fitted on three directions misses a fourth by', mp.nstr(miss, 8))
W10 = same < 1e-40 and miss > 1e-3
print('W10', ok(W10))
