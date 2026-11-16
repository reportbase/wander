"""FZD run 1 (plans/fzd-plan.md): Fizeau's moving water as the boost's composition.
Run from the repository's root: python3 runs/fzd/fzd.py
Published values typed in from the sources named in the plan (not committed); water's n(lambda) from
Daimon and Masumura 2007 at 20.0 C (refractiveindex.info, formula 2, CC0)."""
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
V = {}
s, a, n, lam = sp.symbols("s a n lambda", positive=True)
op = lambda p, q, kap: (p + q) / (1 - kap * p * q)

print("== F1. The coefficient from the rule ==")
w = op(1 / n, a, -1)
ser = sp.series(w, a, 0, 3).removeO()
f0 = sp.simplify(ser.coeff(a, 1))
f_gal = sp.simplify(sp.series(op(1 / n, a, 0), a, 0, 2).removeO().coeff(a, 1))
print(f"   first order: {f0}  (Galilean: {f_gal}); second-order coefficient: {sp.simplify(ser.coeff(a, 2))}")
V["F1"] = sp.simplify(f0 - (1 - 1 / n**2)) == 0 and f_gal == 1

# water: Daimon & Masumura 2007, 20.0 C, lambda in micrometres
B = [5.684027565e-1, 1.726177391e-1, 2.086189578e-2, 1.130748688e-1]
C = [5.101829712e-3, 1.821153936e-2, 2.620722293e-2, 1.069792721e1]
def nw(l):
    l2 = l * l
    return mp.sqrt(1 + sum(b * l2 / (l2 - c) for b, c in zip(B, C)))
F0 = lambda l: 1 - 1 / nw(l)**2
FL = lambda l: F0(l) - l / nw(l) * mp.diff(nw, l)

print("== F2. The second order ==")
c = 299792458
worst = 0
for u in (2, 4, 7, 7.069, 8.72, 7.65, 5.67, 5.536):
    av = mp.mpf(u) / c
    full = op(1 / nw(0.5893), av, -1) - 1 / nw(0.5893)
    first = F0(0.5893) * av
    r = abs(full - first) / first
    worst = max(worst, r)
    print(f"   u = {u} m/s: second order / first = {mp.nstr(r, 4)}")
V["F2"] = worst < 1e-8

print("== F3. Dispersion is the Doppler factor's ==")
lD = mp.mpf("0.5893")
print(f"   water at the D lines: n = {mp.nstr(nw(lD), 6)}, f0 = {mp.nstr(F0(lD), 5)}, with Lorentz's term {mp.nstr(FL(lD), 5)}, lowered by {mp.nstr((F0(lD) - FL(lD)) / F0(lD) * 100, 3)}%")
# the term from the Doppler factor: the frequency seen in the water is shifted by k ~ 1 - a n (to first order, light
# along the flow); n taken there and composed again gives the extra first-order term; check it equals -(lambda/n) dn/dlambda
nn = sp.Function("N")
lam0 = sp.symbols("lambda0", positive=True)
# in the water frame wavelength (vacuum) lam' = lam0 * (1 + a*N) to first order (light and water along one line, beta = a)
nprime = nn(lam0) + sp.diff(nn(lam0), lam0) * lam0 * a * nn(lam0)
wd = sp.series(op(1 / nprime, a, -1), a, 0, 2).removeO().coeff(a, 1)
target = 1 - 1 / nn(lam0)**2 - lam0 / nn(lam0) * sp.diff(nn(lam0), lam0)
okF3 = sp.simplify(wd - target) == 0
pct = (F0(lD) - FL(lD)) / F0(lD) * 100
print(f"   composed with n at the Doppler-shifted wavelength, first order = Lorentz's f: {okF3}")
V["F3"] = okF3 and 1 <= pct <= 3

print("== F4. Michelson and Morley 1886 ==")
x, pe = 0.434, 0.02
print(f"   measured {x} +/- {pe}; f0(D) = {mp.nstr(F0(lD), 4)} ({mp.nstr(abs(x - F0(lD)) / pe, 3)} of their error); "
      f"from their own n^2 = 1.78: {1 - 1/1.78:.4f}; Galilean 1: {(1 - x) / pe:.1f}; none 0: {x / pe:.1f}")
V["F4"] = abs(x - F0(lD)) <= 2 * pe and (1 - x) > 10 * pe and x > 10 * pe

print("== F5. Fizeau 1851 ==")
f_fiz = 0.46 / 0.92      # double displacement observed / computed for full drag (C. R. 33, p. 353)
print(f"   0.46 of 0.92 for full drag: f = {f_fiz:.3f}; Fresnel by Fizeau's own calculation 0.40/0.92 = {0.40/0.92:.4f}; "
      f"against f0(D) {mp.nstr(F0(lD), 4)}: off by {mp.nstr((f_fiz - F0(lD)) / F0(lD) * 100, 3)}%; against his 0.40: "
      f"{(0.46 - 0.40) / 0.40 * 100:.1f}%; no uncertainty stated")
V["F5"] = abs(f_fiz - F0(lD)) / F0(lD) <= 0.15

print("== F6. Zeeman 1915 ==")
# KNAW Proc. 18 I, p. 403: lambda (A), shift Fresnel without dispersion, Lorentz, observed, probable error
Z = [(4500, 0.786, 0.825, 0.826, 0.007), (4580, 0.771, 0.808, 0.808, 0.005), (5461, 0.637, 0.660, 0.656, 0.005),
     (6870, 0.500, 0.513, 0.511, 0.007)]   # 6440 has one reading and no error; left out
ss0 = ssL = 0; chi0 = chiL = 0
for (L, dF, dL, dx, p) in Z:
    l = mp.mpf(L) / 10000
    fx = F0(l) * dx / dF            # observed coefficient, scaled by the shift Zeeman computed without dispersion
    sig = F0(l) * (p / 0.6745) / dF
    ss0 += (fx - F0(l))**2; ssL += (fx - FL(l))**2
    chi0 += ((fx - F0(l)) / sig)**2; chiL += ((fx - FL(l)) / sig)**2
    print(f"   {L} A: observed f = {mp.nstr(fx, 4)} +/- {mp.nstr(sig, 2)}; f0 {mp.nstr(F0(l), 4)}, with dispersion {mp.nstr(FL(l), 4)}"
          f"  (Zeeman's own ratio of Lorentz to Fresnel {dL/dF:.4f}, ours {mp.nstr(FL(l)/F0(l), 4)})")
print(f"   summed squares: f0 {mp.nstr(ss0, 3)}, with dispersion {mp.nstr(ssL, 3)}; chi2 on 4: {mp.nstr(chi0, 4)}, {mp.nstr(chiL, 4)}")
V["F6"] = ssL < ss0

print("== verdicts ==")
for k_, v in V.items():
    print(f"  {k_}: {'not killed' if v else 'KILLED'}")
