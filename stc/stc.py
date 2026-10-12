"""STC: why the construction from situated observations can succeed. See plans/stc-plan.md.

Amounts throughout (positions, lengths, luminosities, fluxes); no unit relation is used. A figure of M landmarks is
read by N standpoints along a baseline known only up to scale; one outside length fixes the scale, with its own error;
a standard-candle rung is calibrated on the landmarks and carried out to far members. The referee is the true figure.
"""
import numpy as np
rng = np.random.default_rng(12)
def verdict(ok): return "not killed" if ok else "KILLED"

M, S, SIG_T, SIG_S, SIG_K, MU, TRIALS = 20, 10.0, 1e-3, 0.01, 0.1, 3.0, 2000
LX, LY = rng.uniform(-50, 50, M), rng.uniform(100, 200, M)           # the figure, fixed
D = np.hypot(LX, LY)                                                 # true distances from the baseline's middle
NS = [16, 64, 256, 1024, 4096]

def construct(N, trials):
    """per trial: the landmarks' log-distance errors e (trials x M) and the outside length's draw"""
    u = np.linspace(-0.5, 0.5, N)                                    # the readers' placement, in their own unit
    X = S*u                                                          # where they truly stand
    th0 = np.arctan2(LY[None, :], LX[None, :] - X[:, None])          # true bearings, N x M
    out = np.empty((trials, M)); eps = rng.normal(0, SIG_S, trials)
    chunk = max(1, 4_000_000//(N*M))
    for a in range(0, trials, chunk):
        b = min(trials, a + chunk)
        th = th0[None] + rng.normal(0, SIG_T, (b - a, N, M))
        s, c = np.sin(th), np.cos(th)
        uu = u[None, :, None]
        a11, a12, a22 = (s*s).sum(1), -(s*c).sum(1), (c*c).sum(1)    # normal equations of the bearing lines
        b1, b2 = (s*s*uu).sum(1), -(s*c*uu).sum(1)
        det = a11*a22 - a12*a12
        px, py = (a22*b1 - a12*b2)/det, (a11*b2 - a12*b1)/det          # each landmark, in the readers' unit
        S0 = S*np.exp(eps[a:b])[:, None]                             # the outside length, with its error
        out[a:b] = np.log(np.hypot(px, py)*S0/D[None, :])
    return out, eps

def ladder(e, n_far):
    """the candle rung calibrated on the landmarks (their distances as constructed), carried to n_far far members"""
    t = e.shape[0]
    lnLc = MU + rng.normal(0, SIG_K, (t, M))                         # calibrators' luminosities
    F_c = np.exp(lnLc)/(4*np.pi*D[None, :]**2)                       # fluxes, read exactly
    d_hat = D[None, :]*np.exp(e)
    lnL_hat = np.log(4*np.pi*d_hat**2*F_c).mean(1)                   # the kind's luminosity, as calibrated
    f = np.empty(t)
    for i in range(t):
        lnL = MU + rng.normal(0, SIG_K, n_far); d = rng.uniform(1e3, 1e4, n_far)
        F = np.exp(lnL)/(4*np.pi*d*d)
        f[i] = np.mean(np.log(np.sqrt(np.exp(lnL_hat[i])/(4*np.pi*F))/d))
    return f

rows = []
for N in NS:
    e, eps = construct(N, TRIALS)
    c = e.mean(1); r = np.sqrt(((e - c[:, None])**2).mean(1))
    C = np.corrcoef(e.T); corr = (C.sum() - M)/(M*(M - 1))
    rows.append((N, r.mean(), c.std(), corr, e, c))
    print(f"N = {N:>4}: shape error r {r.mean():.5f}; common shift c sd {c.std():.5f} (outside length's {SIG_S});"
          f" mean pairwise correlation of the landmarks' errors {corr:.3f}")

lnN = np.log([x[0] for x in rows]); lnr = np.log([x[1] for x in rows])
slope = np.polyfit(lnN, lnr, 1)[0]
ok1 = -0.55 <= slope <= -0.45
print(f"P1 slope of ln r on ln N: {slope:.3f} ->", verdict(ok1))

sd = {x[0]: x[2] for x in rows}; rr = {x[0]: x[1] for x in rows}
within = all(abs(sd[N]/SIG_S - 1) <= 0.10 for N in NS if N >= 256)
fall = sd[4096]/sd[64]
ok2 = within and fall > 0.90
print(f"P2 sd of c at N >= 256: {', '.join(f'{sd[N]:.5f}' for N in NS if N >= 256)} (within 10% of {SIG_S}: {within});"
      f" sd ratio N 4096/64 {fall:.3f} while r falls {rr[64]/rr[4096]:.2f}x ->", verdict(ok2))

cors = [x[3] for x in rows]
ok3 = cors[-1] >= 0.95 and all(b > a for a, b in zip(cors, cors[1:]))
print(f"P3 correlation by N: {', '.join(f'{x:.3f}' for x in cors)} ->", verdict(ok3))

e4, c4 = rows[-1][4], rows[-1][5]
pred = np.sqrt(SIG_S**2 + SIG_K**2/(4*M))
f100, f10k = ladder(e4, 100), ladder(e4, 10_000)
r100, r10k = f100.std()/pred, f10k.std()/pred
cc = np.corrcoef(c4, f10k)[0, 1]
ok4 = abs(r100 - 1) <= 0.10 and abs(r10k - 1) <= 0.10 and abs(cc - SIG_S/pred) <= 0.10
print(f"P4 far rung's mean error sd: n_far 100 {f100.std():.5f}, n_far 10,000 {f10k.std():.5f} (predicted {pred:.5f});"
      f" shrink from 100 to 10,000 members {f10k.std()/f100.std():.3f}; correlation with the shift below {cc:.3f}"
      f" (predicted {SIG_S/pred:.3f}) ->", verdict(ok4))
