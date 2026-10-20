"""AFM run 3: a robust turn (plans/afm-plan.md, "Before run 3"). Run from the repository's root:
python3 runs/afm/afm3.py"""
import numpy as np
from scipy.optimize import least_squares
from scipy.spatial.transform import Rotation as Rot

THINGS = [((1.0, 2.0, 0.0), (1.2, 0.8, 0.75)), ((3.4, 0.9, 0.0), (0.5, 0.5, 0.5)), ((1.4, 2.2, 0.75), (0.24, 0.24, 0.24)),
          ((4.2, 3.0, 0.0), (0.6, 0.5, 1.8))]
GAMMA, K, SEEDS, NR, NF = 1e-3, 8, [11, 12, 13, 14, 15], 80, 12
TOL_R, TOL_T, TOL_S = 10 * GAMMA, 20 * GAMMA, 10 * GAMMA


def scene(seed):
    """Run 2's room, but the far features at directions uniform over the sphere."""
    rng = np.random.default_rng(seed)
    pts = []
    for _ in range(50):
        face = rng.integers(6); p = rng.uniform([0, 0, 0], [5, 4, 2.5]); p[face // 2] = [0, 5, 0, 4, 0, 2.5][face]; pts.append(p)
    for i in range(30):
        c, s = THINGS[i % 4]; p = np.array(c) + rng.uniform(0, 1, 3) * s
        f = rng.integers(3); p[f] = c[f] + s[f] * rng.integers(2); pts.append(p)
    for _ in range(NF):
        d = rng.normal(size=3); pts.append([2.5, 2, 1.25] + 1e6 * d / np.linalg.norm(d))
    P = np.array(pts)
    X = rng.uniform([1.5, 1, 1], [3.5, 3, 2], size=(K, 3))
    Rw = Rot.random(K, random_state=seed).as_matrix()
    s = np.linalg.norm(X[1] - X[0]); R0 = Rw[0]
    Pl = (R0.T @ (P - X[0]).T).T / s
    Xl = (R0.T @ (X - X[0]).T).T / s
    Rl = np.array([R0.T @ Rw[k] for k in range(K)])
    return Pl, Xl, Rl


def read(P, X, R, f, rng):
    U = np.empty((K, len(P), 3))
    for k in range(K):
        for i, p in enumerate(P):
            u = R[k].T @ (p - X[k]); u /= np.linalg.norm(u)
            d = np.arctan(abs(GAMMA * np.tan(np.pi * (rng.random() - 0.5))))
            a = rng.normal(size=3); a -= u * (a @ u); a /= np.linalg.norm(a)
            v = u * np.cos(d) + a * np.sin(d)
            if rng.random() < f: v = rng.normal(size=3); v /= np.linalg.norm(v)
            U[k, i] = v
    return U


def triad(a1, a2, b1, b2):
    def frame(x, y):
        e1 = x / np.linalg.norm(x); e2 = np.cross(x, y); e2 /= np.linalg.norm(e2); return np.column_stack([e1, e2, np.cross(e1, e2)])
    return frame(a1, a2) @ frame(b1, b2).T


def median_rotation(Rs):
    q = Rot.from_matrix(np.array(Rs)).as_quat()
    q *= np.sign(q @ q[0])[:, None]
    m = np.median(q, axis=0); return Rot.from_quat(m / np.linalg.norm(m)).as_matrix()


def median_direction(V):
    V = np.array(V); V *= np.sign(V @ V[0])[:, None]
    m = np.median(V, axis=0); return m / np.linalg.norm(m)


def closest(o1, u1, o2, u2):
    w = o1 - o2; b = u1 @ u2; d, e = u1 @ w, u2 @ w; den = 1 - b * b
    if den <= 1e-15: return None
    t = (b * e - d) / den; s = (e - b * d) / den
    return t, s, ((o1 + u1 * t) + (o2 + u2 * s)) / 2


def af_point(X, D):
    mids = []
    for a in range(len(X)):
        for b in range(a + 1, len(X)):
            c = closest(X[a], D[a], X[b], D[b])
            if c and c[0] > 0 and c[1] > 0: mids.append(c[2])
    return np.median(np.array(mids), axis=0) if mids else None


def angle(a, b):
    return np.arctan2(np.linalg.norm(np.cross(a, b), axis=-1), (a * b).sum(-1))


def sign_vote(t, U0, Uk, idx):
    votes = 0
    for i in idx:
        c = closest(np.zeros(3), U0[i], t, Uk[i])
        if c: votes += 1 if (c[0] > 0 and c[1] > 0) else -1 if (c[0] < 0 and c[1] < 0) else 0
    return t if votes >= 0 else -t


def places(U, Rk, X):
    pts = []
    for i in range(NR + NF):
        D = np.array([Rk[k] @ U[k, i] for k in range(K)])
        p = af_point(X, D); pts.append(p if p is not None else D[0] * 1e6)
    return np.array(pts)


def af2(U):
    """Run 2's AF2 unchanged: medians at every stage."""
    far = range(NR, NR + NF)
    Rk = [np.eye(3)]
    for k in range(1, K):
        Rk.append(median_rotation([triad(U[0, i], U[0, j], U[k, i], U[k, j]) for i in far for j in far if i < j]))
    T = [np.zeros(3)]
    for k in range(1, K):
        n = [np.cross(U[0, i], Rk[k] @ U[k, i]) for i in range(NR)]
        cand = [np.cross(n[i], n[j]) for i in range(NR) for j in range(i + 1, NR) if np.linalg.norm(np.cross(n[i], n[j])) > 1e-12]
        t = median_direction([c / np.linalg.norm(c) for c in cand])
        T.append(sign_vote(t, U[0], (Rk[k] @ U[k].T).T, range(NR)))
    X = [np.zeros(3), T[1]]
    P12 = []
    for i in range(NR):
        c = closest(X[0], U[0, i], X[1], Rk[1] @ U[1, i]); P12.append(c[2] if c else None)
    for k in range(2, K):
        ss = []
        for i in range(NR):
            if P12[i] is None: continue
            c = closest(np.zeros(3), T[k], P12[i], -(Rk[k] @ U[k, i]))
            if c and c[0] > 0: ss.append(c[0])
        X.append(T[k] * np.median(ss))
    X = np.array(X)
    return np.array(Rk), X, places(U, Rk, X)


def af2_vote(U):
    """The same candidates; at each pose stage the one with most agreeing readings, then the median over those."""
    far = list(range(NR, NR + NF))
    Rk = [np.eye(3)]
    for k in range(1, K):
        best, cands = -1, []
        for a in range(NF):
            for b in range(a + 1, NF):
                i, j = far[a], far[b]
                R = triad(U[0, i], U[0, j], U[k, i], U[k, j])
                inl = [m for m in far if angle(U[0, m], R @ U[k, m]) < TOL_R]
                if len(inl) > best: best, keep = len(inl), inl
        Rs = [triad(U[0, i], U[0, j], U[k, i], U[k, j]) for a, i in enumerate(keep) for j in keep[a + 1:]]
        Rk.append(median_rotation(Rs) if Rs else R)
    T, IN = [np.zeros(3)], [None]
    for k in range(1, K):
        Uk = (Rk[k] @ U[k].T).T
        n = np.cross(U[0, :NR], Uk[:NR]); nn = np.linalg.norm(n, axis=1); nh = n / nn[:, None]
        best = -1
        for i in range(NR):
            c = np.cross(nh[i], nh[i + 1:]); cn = np.linalg.norm(c, axis=1); ok = cn > 1e-12
            if not ok.any(): continue
            c = c[ok] / cn[ok][:, None]
            score = (np.abs(c @ nh.T) < TOL_T).sum(1)
            j = int(np.argmax(score))
            if score[j] > best: best, tbest = int(score[j]), c[j]
        inl = np.where(np.abs(nh @ tbest) < TOL_T)[0]
        cand = [np.cross(nh[a], nh[b]) for x, a in enumerate(inl) for b in inl[x + 1:]]
        cand = [c / np.linalg.norm(c) for c in cand if np.linalg.norm(c) > 1e-12]
        t = median_direction([c * np.sign(c @ tbest) for c in cand]) if cand else tbest
        T.append(sign_vote(t, U[0], Uk, inl)); IN.append(set(inl.tolist()))
    X = [np.zeros(3), T[1]]
    P12 = []
    for i in range(NR):
        c = closest(X[0], U[0, i], X[1], Rk[1] @ U[1, i]); P12.append(c[2] if (c and i in IN[1]) else None)
    use = [i for i in range(NR) if P12[i] is not None]
    for k in range(2, K):
        Uk = (Rk[k] @ U[k].T).T
        cand = []
        for i in use:
            c = closest(np.zeros(3), T[k], P12[i], -Uk[i])
            if c and c[0] > 0: cand.append(c[0])
        def agree(s):
            o = T[k] * s; out = []
            for j in use:
                w = P12[j] - o; d = np.linalg.norm(w)
                if angle(w / d, Uk[j]) < TOL_S: out.append(j)
            return out
        best = -1
        for s in cand:
            a = agree(s)
            if len(a) > best: best, keep = len(a), a
        ss = []
        for j in keep:
            c = closest(np.zeros(3), T[k], P12[j], -Uk[j])
            if c and c[0] > 0: ss.append(c[0])
        X.append(T[k] * np.median(ss))
    X = np.array(X)
    return np.array(Rk), X, places(U, Rk, X)


def pack(R, X, P):
    return np.concatenate([Rot.from_matrix(R[1:]).as_rotvec().ravel(), X[1:].ravel(), P.ravel()])


def unpack(z):
    R = np.concatenate([np.eye(3)[None], Rot.from_rotvec(z[:3 * (K - 1)].reshape(K - 1, 3)).as_matrix()])
    X = np.concatenate([np.zeros((1, 3)), z[3 * (K - 1):6 * (K - 1)].reshape(K - 1, 3)])
    return R, X, z[6 * (K - 1):].reshape(-1, 3)


def resid(z, U):
    R, X, P = unpack(z)
    out = []
    for k in range(K):
        W = (R[k].T @ (P - X[k]).T).T; W /= np.linalg.norm(W, axis=1)[:, None]
        out.append((W - U[k] * (W * U[k]).sum(1)[:, None]).ravel())
    out.append([1e3 * (np.linalg.norm(X[1]) - 1)])
    return np.concatenate(out)


def ba(U, R, X, P):
    z = least_squares(resid, pack(R, X, P), args=(U,), loss='cauchy', f_scale=GAMMA, method='trf', max_nfev=200).x
    return unpack(z)


def err(Pt, Pe):
    return np.linalg.norm(Pe[:NR] - Pt[:NR], axis=1) / np.linalg.norm(Pt[:NR], axis=1)


def rot_err(Rt, Re):
    return max(np.degrees(Rot.from_matrix(Rt[k].T @ Re[k]).magnitude()) for k in range(1, K))


res, turn = {}, {}
for f in (0.0, 0.1, 0.2, 0.3):
    e = {'AF2-wide': [], 'AF2-vote': [], 'BA-CB': []}; tw, tv = [], []
    for seed in SEEDS:
        Pt, Xt, Rt = scene(seed)
        U = read(Pt, Xt, Rt, f, np.random.default_rng(seed * 104729 + int(f * 100)))
        R, X, P = af2(U); tw.append(rot_err(Rt, R)); e['AF2-wide'] += list(err(Pt, P))
        R, X, P = af2_vote(U); tv.append(rot_err(Rt, R)); e['AF2-vote'] += list(err(Pt, P))
        _, _, P2 = ba(U, R, X, P); e['BA-CB'] += list(err(Pt, P2))
    res[f] = {k: float(np.median(v)) for k, v in e.items()}; turn[f] = (max(tw), max(tv))
    print(f"f = {f:.1f}: AF2-wide {res[f]['AF2-wide']:.3e}  AF2-vote {res[f]['AF2-vote']:.3e}  BA-CB {res[f]['BA-CB']:.3e}   "
          f"worst turn error: wide {turn[f][0]:.4f} deg, vote {turn[f][1]:.4f} deg", flush=True)
c = res[0.0]
print("\nratios to f = 0:")
for f in (0.1, 0.2, 0.3):
    print(f"  f = {f:.1f}: AF2-wide {res[f]['AF2-wide']/c['AF2-wide']:.2f}x  AF2-vote {res[f]['AF2-vote']/c['AF2-vote']:.2f}x  "
          f"BA-CB {res[f]['BA-CB']/c['BA-CB']:.2f}x")
h1 = c['AF2-wide'] <= 2.5e-3 and turn[0.0][0] <= 0.2
h2 = res[0.1]['AF2-wide'] <= 3 * c['AF2-wide'] and res[0.2]['AF2-wide'] > 10 * c['AF2-wide']
h3 = res[0.3]['AF2-vote'] <= 3 * c['AF2-vote']
h4 = res[0.3]['BA-CB'] <= 3 * c['BA-CB'] and res[0.3]['BA-CB'] <= res[0.3]['AF2-vote']
for name, ok in (('H1', h1), ('H2', h2), ('H3', h3), ('H4', h4), ('H5', h1 and h2 and h3)):
    print(name, "not killed" if ok else "KILLED")
