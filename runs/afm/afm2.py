"""AFM run 2: the poses not given (plans/afm-plan.md, "Before run 2"). Run from the repository's root:
python3 runs/afm/afm2.py"""
import numpy as np
from scipy.optimize import least_squares
from scipy.spatial.transform import Rotation as Rot

THINGS = [((1.0, 2.0, 0.0), (1.2, 0.8, 0.75)), ((3.4, 0.9, 0.0), (0.5, 0.5, 0.5)), ((1.4, 2.2, 0.75), (0.24, 0.24, 0.24)),
          ((4.2, 3.0, 0.0), (0.6, 0.5, 1.8))]
GAMMA, K, SEEDS, NR, NF = 1e-3, 8, [11, 12, 13, 14, 15], 80, 6


def scene(seed):
    rng = np.random.default_rng(seed)
    pts = []
    for _ in range(50):
        face = rng.integers(6); p = rng.uniform([0, 0, 0], [5, 4, 2.5]); p[face // 2] = [0, 5, 0, 4, 0, 2.5][face]; pts.append(p)
    for i in range(30):
        c, s = THINGS[i % 4]; p = np.array(c) + rng.uniform(0, 1, 3) * s
        f = rng.integers(3); p[f] = c[f] + s[f] * rng.integers(2); pts.append(p)
    for _ in range(NF):
        d = np.array([1.0, rng.uniform(-0.3, 0.3), rng.uniform(-0.1, 0.3)]); pts.append([2.5, 2, 1.25] + 1e6 * d / np.linalg.norm(d))
    P = np.array(pts)
    X = rng.uniform([1.5, 1, 1], [3.5, 3, 2], size=(K, 3))
    Rw = Rot.random(K, random_state=seed).as_matrix()            # standpoint k's frame: world = Rw[k] @ local
    # into standpoint 1's frame, |AB| = 1
    s = np.linalg.norm(X[1] - X[0]); R0 = Rw[0]
    Pl = (R0.T @ (P - X[0]).T).T / s
    Xl = (R0.T @ (X - X[0]).T).T / s
    Rl = np.array([R0.T @ Rw[k] for k in range(K)])              # standpoint k's local -> standpoint 1's frame
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


def af2(U):
    far = range(NR, NR + NF)
    Rk = [np.eye(3)]
    for k in range(1, K):
        Rs = [triad(U[0, i], U[0, j], U[k, i], U[k, j]) for i in far for j in far if i < j]
        Rk.append(median_rotation(Rs))
    T = [np.zeros(3)]
    for k in range(1, K):
        n = [np.cross(U[0, i], Rk[k] @ U[k, i]) for i in range(NR)]
        cand = [np.cross(n[i], n[j]) for i in range(NR) for j in range(i + 1, NR) if np.linalg.norm(np.cross(n[i], n[j])) > 1e-12]
        cand = [c / np.linalg.norm(c) for c in cand]
        t = median_direction(cand)
        votes = 0
        for i in range(NR):
            c = closest(np.zeros(3), U[0, i], t, Rk[k] @ U[k, i])
            if c: votes += 1 if (c[0] > 0 and c[1] > 0) else -1 if (c[0] < 0 and c[1] < 0) else 0
        T.append(t if votes >= 0 else -t)
    X = [np.zeros(3), T[1]]
    P12 = []
    for i in range(NR):
        c = closest(X[0], U[0, i], X[1], Rk[1] @ U[1, i]); P12.append(c[2] if c else None)
    for k in range(2, K):
        ss = []
        for i in range(NR):
            if P12[i] is None: continue
            c = closest(np.zeros(3), T[k], P12[i], -(Rk[k] @ U[k, i]))   # the step line against the ray back from the point
            if c and c[0] > 0: ss.append(c[0])
        X.append(T[k] * np.median(ss))
    X = np.array(X)
    pts = []
    for i in range(NR + NF):
        D = np.array([Rk[k] @ U[k, i] for k in range(K)])
        p = af_point(X, D); pts.append(p if p is not None else D[0] * 1e6)
    return np.array(Rk), X, np.array(pts)


def pack(R, X, P):
    rv = Rot.from_matrix(R[1:]).as_rotvec().ravel()
    return np.concatenate([rv, X[1:].ravel(), P.ravel()])


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


def ba(U, R, X, P, loss):
    z = least_squares(resid, pack(R, X, P), args=(U,), loss=loss, f_scale=GAMMA if loss == 'cauchy' else 1.0,
                      method='trf', max_nfev=200).x
    return unpack(z)


def err(Pt, Pe):
    return np.linalg.norm(Pe[:NR] - Pt[:NR], axis=1) / np.linalg.norm(Pt[:NR], axis=1)


def rot_err(Rt, Re):
    return max(np.degrees(Rot.from_matrix(Rt[k].T @ Re[k]).magnitude()) for k in range(1, K))


res = {}
for f in (0.0, 0.1, 0.2, 0.3):
    e = {'AF2': [], 'BA-LS': [], 'BA-CB': []}; rmax = []
    for seed in SEEDS:
        Pt, Xt, Rt = scene(seed)
        U = read(Pt, Xt, Rt, f, np.random.default_rng(seed * 104729 + int(f * 100)))
        R, X, P = af2(U); rmax.append(rot_err(Rt, R)); e['AF2'] += list(err(Pt, P))
        _, _, P1 = ba(U, R, X, P, 'linear'); e['BA-LS'] += list(err(Pt, P1))
        _, _, P2 = ba(U, R, X, P, 'cauchy'); e['BA-CB'] += list(err(Pt, P2))
    res[f] = {k: float(np.median(v)) for k, v in e.items()}
    print(f"f = {f:.1f}: AF2 {res[f]['AF2']:.3e}  BA-LS {res[f]['BA-LS']:.3e}  BA-CB {res[f]['BA-CB']:.3e}   "
          f"AF2's worst turn error {max(rmax):.4f} deg (median over rooms {np.median(rmax):.4f})")
c = res[0.0]
g1 = c['AF2'] <= 3 * 1.233e-3 and c['BA-CB'] <= c['AF2'] and c['BA-LS'] > c['BA-CB']
g2 = res[0.1]['AF2'] <= 3 * c['AF2'] and res[0.2]['AF2'] > 10 * c['AF2']
g3 = res[0.1]['BA-LS'] > 10 * c['BA-LS']
g4 = res[0.1]['BA-CB'] <= 3 * c['BA-CB']
print("\nratios to f = 0:")
for f in (0.1, 0.2, 0.3):
    print(f"  f = {f:.1f}: AF2 {res[f]['AF2']/c['AF2']:.2f}x  BA-LS {res[f]['BA-LS']/c['BA-LS']:.2f}x  BA-CB {res[f]['BA-CB']/c['BA-CB']:.2f}x")
for name, ok in (('G1', g1), ('G2', g2), ('G3', g3), ('G4', g4), ('G5', g1 and g2)):
    print(name, "not killed" if ok else "KILLED")
