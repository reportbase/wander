# KPL run 1: an orbit's clock from looks alone (plans/kpl-plan.md). Usage: python3 runs/kpl/kpl.py
import numpy as np, mpmath as mp
from scipy.optimize import least_squares
mp.mp.dps = 40

def kepler_E(M, e):
    E = M if e < 0.8 else mp.pi
    for _ in range(60): E = E - (E - e*mp.sin(E) - M)/(1 - e*mp.cos(E))
    return E

def world(e, w, a, GM, R, tick, ticks, tau=mp.mpf('0.137')):
    """looks at the given tick counts: direction nu, angular size alpha. tick = seconds per tick."""
    P = 2*mp.pi*mp.sqrt(a**3/GM)
    out = []
    for n in ticks:
        t = n*tick
        M = 2*mp.pi*(t/P - tau)
        E = kepler_E(mp.fmod(M, 2*mp.pi), e)
        nu = 2*mp.atan(mp.sqrt((1 + e)/(1 - e))*mp.tan(E/2)) + w
        r = a*(1 - e*mp.cos(E))
        out.append((nu, R/r))
    return out, P

e0, w0, a0, GM0, R0, c0 = mp.mpf('0.3'), mp.mpf('0.7'), mp.mpf('2.5'), mp.mpf('1.9'), mp.mpf('0.01'), mp.mpf('0.0137')
P0 = 2*mp.pi*mp.sqrt(a0**3/GM0)
ticks = [int(k) for k in np.linspace(0, float(2*P0/c0), 41)]
looks, _ = world(e0, w0, a0, GM0, R0, c0, ticks)

# K1: e, omega from directions and angular sizes alone (no time): alpha = A + B cos nu + C sin nu
X = mp.matrix([[1, mp.cos(n), mp.sin(n)] for n, _ in looks]); y = mp.matrix([al for _, al in looks])
sol = mp.lu_solve(X.T*X, X.T*y)
e1 = mp.sqrt(sol[1]**2 + sol[2]**2)/sol[0]; w1 = mp.atan2(sol[2], sol[1])
print('K1: e error %s, omega error %s' % (mp.nstr(abs(e1 - e0), 3), mp.nstr(abs(w1 - w0), 3)),
      '-> not killed' if abs(e1 - e0) < 1e-12 and abs(w1 - w0) < 1e-12 else '-> KILLED')

# K2 and K3: the mean anomaly from position alone, then against ticks
def M_of(nu, e, w):
    E = 2*mp.atan(mp.sqrt((1 - e)/(1 + e))*mp.tan((nu - w)/2))
    return E - e*mp.sin(E)
Ms = [M_of(n, e1, w1) for n, _ in looks]
# unwrap
U = [Ms[0]]
for m in Ms[1:]:
    d = m - U[-1]; d = d - 2*mp.pi*mp.floor((d + mp.pi)/(2*mp.pi)); U.append(U[-1] + d)
Xt = mp.matrix([[1, n] for n in ticks]); yt = mp.matrix(U)
lt = mp.lu_solve(Xt.T*Xt, Xt.T*yt)
res = max(abs(U[i] - lt[0] - lt[1]*ticks[i]) for i in range(len(ticks)))
P_ticks = 2*mp.pi/lt[1]
print('K2/K3: M/2pi linear in ticks, max residual %s; period %s ticks (truth %s): rel error %s' % (
    mp.nstr(res, 3), mp.nstr(P_ticks, 15), mp.nstr(P0/c0, 15), mp.nstr(abs(P_ticks/(P0/c0) - 1), 3)),
    '-> not killed' if res < 1e-12 and abs(P_ticks/(P0/c0) - 1) < 1e-12 else '-> KILLED')
# two looks alone, given e and omega
P2 = 2*mp.pi*(ticks[3] - ticks[1])/(U[3] - U[1])
print('     from two looks: rel error %s' % mp.nstr(abs(P2/(P0/c0) - 1), 3))

# K4: directions and ticks alone (no angular size): fit e, omega, P in ticks, tau
tk = np.array(ticks, float); nu_obs = np.array([float(n) for n, _ in looks])
def model_nu(q, tk):
    e, w, Pt, tau = q
    M = 2*np.pi*(tk/Pt - tau); E = M.copy()
    for _ in range(50): E = E - (E - e*np.sin(E) - M)/(1 - e*np.cos(E))
    return 2*np.arctan(np.sqrt((1 + e)/(1 - e))*np.tan(E/2)) + w
def r4(q): return np.angle(np.exp(1j*(model_nu(q, tk) - nu_obs)))
best = None
for es in (0.1, 0.5):
    for ts in (0.0, 0.5):
        fit = least_squares(r4, [es, 0.0, float(P0/c0)*0.97, ts], xtol=1e-15, ftol=1e-15, gtol=1e-15)
        if best is None or fit.cost < best.cost: best = fit
q = best.x
print('K4: e error %.2e, omega error %.2e, P rel error %.2e' % (abs(q[0] - float(e0)), abs(np.angle(np.exp(1j*(q[1] - float(w0))))),
      abs(q[2]/float(P0/c0) - 1)), '-> not killed' if max(abs(q[0] - float(e0)), abs(q[2]/float(P0/c0) - 1)) < 1e-10 else '-> KILLED')

# K5: untimed directions alone: every e passes through every direction (each nu occurs once a period on any ellipse)
ok5 = True
for etest in (mp.mpf('0.05'), mp.mpf('0.9')):
    for n, _ in looks[:10]:
        E = 2*mp.atan(mp.sqrt((1 - etest)/(1 + etest))*mp.tan((n - w0)/2))
        n_back = 2*mp.atan(mp.sqrt((1 + etest)/(1 - etest))*mp.tan(E/2)) + w0
        ok5 &= abs(mp.sin((n_back - n)/2)) < 1e-30
print('K5: every direction lies on orbits of e = 0.05 and 0.9 as on 0.3:', ok5, '-> not killed' if ok5 else '-> KILLED')

# K6: scale a and planet radius by lam and the tick by lam^1.5; or GM by mu and the tick by mu^-0.5
worst = 0
for lam, mu in ((mp.mpf(7), 1), (1, mp.mpf(11)), (mp.mpf('0.03'), mp.mpf(5))):
    tick2 = c0*lam**mp.mpf(1.5)/mp.sqrt(mu)
    looks2, _ = world(e0, w0, a0*lam, GM0*mu, R0*lam, tick2, ticks)
    for (n1, a1), (n2, a2) in zip(looks, looks2):
        worst = max(worst, abs(n1 - n2), abs(a1 - a2))
print('K6: every look unchanged under Kepler-III scalings, max change %s' % mp.nstr(worst, 3),
      '-> not killed' if worst < 1e-30 else '-> KILLED')

# K7: noise, 200 looks over two periods, bootstrap
rng = np.random.default_rng(1210)
ticks7 = np.linspace(0, float(2*P0/c0), 200).round()
looks7, _ = world(e0, w0, a0, GM0, R0, c0, [int(x) for x in ticks7])
nu_t = np.array([float(n) for n, _ in looks7]); al_t = np.array([float(a) for _, a in looks7])
def fit7(nu, al, tk):
    # joint fit: e, omega, P, tau, and the size scale s (alpha = s*(1 + e cos(nu - omega)))
    def r(q):
        e, w, Pt, tau, s = q
        rn = np.angle(np.exp(1j*(model_nu([e, w, Pt, tau], tk) - nu)))/1e-4
        nm = model_nu([e, w, Pt, tau], tk)
        ra = (s*(1 + e*np.cos(nm - w)) - al)/(1e-3*al)
        return np.r_[rn, ra]
    s0 = al.mean()
    return least_squares(r, [0.25, 0.6, float(P0/c0)*0.99, 0.1, s0], x_scale='jac').x
nu_o = nu_t + rng.normal(0, 1e-4, 200); al_o = al_t*(1 + rng.normal(0, 1e-3, 200))
q7 = fit7(nu_o, al_o, ticks7)
boot = []
for b in range(200):
    i = rng.integers(0, 200, 200)
    boot.append(fit7(nu_o[i], al_o[i], ticks7[i]))
boot = np.array(boot); se = boot.std(axis=0)
ze = abs(q7[0] - float(e0))/se[0]; zp = abs(q7[2] - float(P0/c0))/se[2]; relP = se[2]/q7[2]
print('K7: e %.6f (truth 0.3, %.2f se), P %.4f ticks (truth %.4f, %.2f se), bootstrap rel error on P %.2e' % (
    q7[0], ze, q7[2], float(P0/c0), zp, relP), '-> not killed' if ze < 3 and zp < 3 and relP < 1e-4 else '-> KILLED')
