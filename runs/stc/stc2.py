"""STC run 2: run 1's shape floor read as the line estimator's bias, and a consistent construction. See
plans/stc-plan.md, "Run 2: predictions".

Same set-up as stc.py (seed 12, so the same figure). The line estimator is run 1's; the maximum-likelihood one takes
five Gauss-Newton steps on the angular residuals from it.
"""
import numpy as np
rng = np.random.default_rng(12)
def verdict(ok): return "not killed" if ok else "KILLED"

M, S, SIG_S, SIG_K, MU, TRIALS = 20, 10.0, 0.01, 0.1, 3.0, 2000
LX, LY = rng.uniform(-50, 50, M), rng.uniform(100, 200, M)
D = np.hypot(LX, LY)
NS = [16, 64, 256, 1024, 4096]

def construct(N, trials, sig_t, ml):
    u = np.linspace(-0.5, 0.5, N)
    th0 = np.arctan2(LY[None, :], LX[None, :] - S*u[:, None])
    out = np.empty((trials, M)); eps = rng.normal(0, SIG_S, trials)
    chunk = max(1, 4_000_000//(N*M))
    uu = u[None, :, None]
    for a in range(0, trials, chunk):
        b = min(trials, a + chunk)
        th = th0[None] + rng.normal(0, sig_t, (b - a, N, M))
        s, c = np.sin(th), np.cos(th)
        a11, a12, a22 = (s*s).sum(1), -(s*c).sum(1), (c*c).sum(1)
        b1, b2 = (s*s*uu).sum(1), -(s*c*uu).sum(1)
        det = a11*a22 - a12*a12
        px, py = (a22*b1 - a12*b2)/det, (a11*b2 - a12*b1)/det        # run 1's estimate
        if ml:
            for _ in range(5):                                         # Gauss-Newton on the angular residuals
                dx = px[:, None, :] - uu; rho2 = dx*dx + py[:, None, :]**2
                res = th - np.arctan2(py[:, None, :], dx)
                jx, jy = -py[:, None, :]/rho2, dx/rho2
                g11, g12, g22 = (jx*jx).sum(1), (jx*jy).sum(1), (jy*jy).sum(1)
                r1, r2 = (jx*res).sum(1), (jy*res).sum(1)
                dt = g11*g22 - g12*g12
                px, py = px + (g22*r1 - g12*r2)/dt, py + (g11*r2 - g12*r1)/dt
        out[a:b] = np.log(np.hypot(px, py)*S*np.exp(eps[a:b])[:, None]/D[None, :])
    return out

def measures(e):
    c = e.mean(1); d = e - c[:, None]
    return np.sqrt((d*d).mean(1)).mean(), c.std(), np.sqrt((d.mean(0)**2).mean()), c

def ladder(e, n_far):
    t = e.shape[0]
    lnLc = MU + rng.normal(0, SIG_K, (t, M)); F_c = np.exp(lnLc)/(4*np.pi*D[None, :]**2)
    lnL_hat = np.log(4*np.pi*(D[None, :]*np.exp(e))**2*F_c).mean(1)
    f = np.empty(t)
    for i in range(t):
        lnL = MU + rng.normal(0, SIG_K, n_far); d = rng.uniform(1e3, 1e4, n_far)
        F = np.exp(lnL)/(4*np.pi*d*d)
        f[i] = np.mean(np.log(np.sqrt(np.exp(lnL_hat[i])/(4*np.pi*F))/d))
    return f

# ---------------------------------------------------------------- P5: the line estimator's floor is its own bias
b1k = measures(construct(1024, TRIALS, 1e-3, False))[2]
b4k = measures(construct(4096, TRIALS, 1e-3, False))[2]
b4k_half = measures(construct(4096, TRIALS, 5e-4, False))[2]
ok5 = b4k >= 0.0008 and abs(b1k/b4k - 1) <= 0.20 and 3 <= b4k/b4k_half <= 5
print(f"P5 line estimator, per-landmark bias rms: N 1024 {b1k:.5f}, N 4096 {b4k:.5f} (ratio {b1k/b4k:.3f});"
      f" with the noise halved {b4k_half:.5f}, a factor {b4k/b4k_half:.2f} ->", verdict(ok5))

# ---------------------------------------------------------------- P6, P7: maximum likelihood
rows = []
for N in NS:
    e = construct(N, TRIALS, 1e-3, True)
    r, sdc, bias, c = measures(e)
    rows.append((N, r, sdc, bias, e, c))
    print(f"   ML, N = {N:>4}: shape error r {r:.5f}; sd of c {sdc:.5f}; per-landmark bias rms {bias:.5f}")
slope = np.polyfit(np.log(NS), np.log([x[1] for x in rows]), 1)[0]
ok6 = -0.55 <= slope <= -0.45 and rows[-1][3] <= 0.0003
print(f"P6 slope of ln r on ln N {slope:.3f}; bias rms at N 4096 {rows[-1][3]:.5f} ->", verdict(ok6))

sd = {x[0]: x[2] for x in rows}
within = all(abs(sd[N]/SIG_S - 1) <= 0.10 for N in NS if N >= 256); fall = sd[4096]/sd[64]
e4, c4 = rows[-1][4], rows[-1][5]
pred = np.sqrt(SIG_S**2 + SIG_K**2/(4*M))
f100, f10k = ladder(e4, 100), ladder(e4, 10_000)
cc = np.corrcoef(c4, f10k)[0, 1]
ok7 = (within and fall > 0.90 and abs(f100.std()/pred - 1) <= 0.10 and abs(f10k.std()/pred - 1) <= 0.10
       and abs(cc - SIG_S/pred) <= 0.10)
print(f"P7 sd of c at N >= 256 within 10% of {SIG_S}: {within}; ratio 4096/64 {fall:.3f}; far rung sd {f100.std():.5f}"
      f" (n_far 100), {f10k.std():.5f} (10,000), predicted {pred:.5f}; correlation with c {cc:.3f} ->", verdict(ok7))
