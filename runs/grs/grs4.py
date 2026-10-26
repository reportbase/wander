"""GRS run 4: the linear term of −ln P_in(k) (plans/grs-plan.md, run 4's predictions).

Run 3's Pfaffian with closed-form entries, k = 20 … 60, at DPS digits and again at DPS2 as a check.
Run from the repository's root: python3 runs/grs/grs4.py
"""
import time

import mpmath as mp

T0 = time.time()
DPS, DPS2 = 1400, 1800
KS = list(range(20, 61))
verdict = {}


def say(*a):
    print(*a, flush=True)


def S(r, s, L):
    """∫₀^L∫₀^L sign(ψ − φ) cos rφ cos sψ dφ dψ, in closed form (checked against run 3's sympy entries to 5·10⁻⁴¹)."""
    if r == 0:
        if s == 0:
            return mp.mpf(0)
        return 2 * (L * mp.sin(s * L) / s + (mp.cos(s * L) - 1) / s**2) - L * mp.sin(s * L) / s

    def sincos(a, b):  # ∫₀^L sin aψ cos bψ dψ
        t = (1 - mp.cos((a + b) * L)) / (a + b)
        if a != b:
            t += (1 - mp.cos((a - b) * L)) / (a - b)
        return t / 2
    c = L if s == 0 else mp.sin(s * L) / s
    return (2 * sincos(r, s) - mp.sin(r * L) * c) / r


def Bd(r, L):
    return L if r == 0 else mp.sin(r * L) / r


def mat(k, L):
    n = k + (k % 2)
    A = mp.matrix(n, n)
    for r in range(k):
        for s in range(k):
            A[r, s] = S(r, s, L)
        if k % 2:
            A[r, k] = Bd(r, L)
            A[k, r] = -Bd(r, L)
    return A


def pin(k):
    return mp.sqrt(abs(mp.det(mat(k, mp.pi / 2)) / mp.det(mat(k, mp.pi))))


# ---------------------------------------------------------------- the derivation's two integrals
mp.mp.dps = 60
# arcsine law on [−1, 1]: x = cos t, t uniform on [0, π]; on [0, 1]: x = (1 + cos t)/2
# ln w = −½ ln(1 − x²), with 1 − x² written so the endpoints do not round to ln 0 (the first launch did: +inf):
# x = cos t gives sin²t; x = (1 + cos t)/2 = cos²(t/2) gives sin²(t/2)·(1 + cos²(t/2))
I_full = mp.quad(lambda t: -mp.log(mp.sin(t)), [0, mp.pi / 2, mp.pi]) / mp.pi
I_half = mp.quad(lambda t: -mp.log(mp.sin(t / 2)) - mp.log(1 + mp.cos(t / 2) ** 2) / 2, [0, mp.pi / 2, mp.pi]) / mp.pi
ok_int = abs(I_full - mp.log(2)) < mp.mpf(10) ** -30 and abs(I_half - mp.log(1 + mp.sqrt(2))) < mp.mpf(10) ** -30
say(f"∫ ln w dμ: [−1, 1] {mp.nstr(I_full, 25)} (ln 2 {mp.nstr(mp.log(2), 25)}); "
    f"[0, 1] {mp.nstr(I_half, 25)} (ln(1 + √2) {mp.nstr(mp.log(1 + mp.sqrt(2)), 25)}): {'as derived' if ok_int else 'NOT AS DERIVED'}")
# the derivation uses only the difference, ln 2 − ln(1 + √2); checked apart from the plan's two values
ok_diff = abs((I_half - I_full) - (mp.log(2) - mp.log(1 + mp.sqrt(2)))) < mp.mpf(10) ** -30
say(f"  the difference [0, 1] − [−1, 1]: {mp.nstr(I_half - I_full, 25)} (ln 2 − ln(1 + √2) "
    f"{mp.nstr(mp.log(2) - mp.log(1 + mp.sqrt(2)), 25)}): {'as used for b' if ok_diff else 'NOT AS USED'}")

# ---------------------------------------------------------------- the Pfaffians
y = {}
for dps in (DPS, DPS2):
    mp.mp.dps = dps
    y[dps] = {}
    for k in KS:
        y[dps][k] = -mp.log(pin(k))
    say(f"  {dps} digits done ({time.time() - T0:.0f} s)")
mp.mp.dps = DPS
diff = max(abs(y[DPS][k] - y[DPS2][k]) for k in KS)
say(f"−ln P_in at {DPS} and {DPS2} digits: largest difference {mp.nstr(diff, 3)}")
Y = y[DPS2]
for k in (20, 30, 40, 50, 60):
    say(f"  k = {k}: −ln P_in = {mp.nstr(Y[k], 20)}")

mp.mp.dps = 50
a0 = mp.log(2) / 2
b0 = mp.log(1 + 1 / mp.sqrt(2))


def lsq(rows, rhs):
    A = mp.matrix(rows)
    v = mp.matrix(rhs)
    sol = mp.lu_solve(A.T * A, A.T * v)
    res = A * sol - v
    rms = mp.sqrt(sum(res[i] ** 2 for i in range(len(rhs))) / len(rhs))
    return sol, rms


# S1: a fixed
sol, rms1 = lsq([[k, mp.log(k), 1, mp.mpf(1) / k] for k in KS], [Y[k] - a0 * k * k for k in KS])
b1 = sol[0]
verdict["S1"] = abs(b1 - b0) <= 0.002
say(f"S1  a fixed: b = {mp.nstr(b1, 10)} (derived {mp.nstr(b0, 10)}, off {mp.nstr(b1 - b0, 3)}), d = {mp.nstr(sol[1], 8)}, "
    f"c = {mp.nstr(sol[2], 8)}, e = {mp.nstr(sol[3], 6)}; rms {mp.nstr(rms1, 3)}")
# S2: free
sol, rms2 = lsq([[k * k, k, mp.log(k), 1, mp.mpf(1) / k] for k in KS], [Y[k] for k in KS])
verdict["S2"] = abs(sol[0] - a0) <= mp.mpf(10) ** -4
say(f"S2  free: a = {mp.nstr(sol[0], 12)} (ln2/2 {mp.nstr(a0, 12)}, off {mp.nstr(sol[0] - a0, 3)}), b = {mp.nstr(sol[1], 10)}, "
    f"d = {mp.nstr(sol[2], 8)}; rms {mp.nstr(rms2, 3)}")
# S3: a, b fixed
sol, rms3 = lsq([[1, mp.log(k), mp.mpf(1) / k, mp.mpf(1) / k**2] for k in KS], [Y[k] - a0 * k * k - b0 * k for k in KS])
verdict["S3"] = rms3 < mp.mpf(10) ** -6
say(f"S3  a, b fixed: c = {mp.nstr(sol[0], 10)}, d = {mp.nstr(sol[1], 10)}, e = {mp.nstr(sol[2], 8)}, f = {mp.nstr(sol[3], 6)}; "
    f"rms {mp.nstr(rms3, 3)}")

say("")
if not ok_int:
    say("the plan's two integrals are not as written: by the plan's letter S1–S3 are void; "
        f"the difference b uses is {'as used' if ok_diff else 'ALSO WRONG'}, so they are reported as run")
for kk in ["S1", "S2", "S3"]:
    say(f"{kk}: {'not killed' if verdict[kk] else 'KILLED'}")
say(f"({time.time() - T0:.0f} s)")
