"""TPI: where 2/π shows up. See plans/tpi-plan.md (predictions written before the catalogue was gathered).

Each entry computes its constant from the step of its derivation where the turn enters (an integral over an angle or a
phase measured evenly, or the Gaussian pair's turn), and checks it against the value as the source writes it. Then P3
(the same construction in three and four dimensions) and P4 (an uneven turn moves the value). mpmath at 50 digits.
Run: python3 -I plans/tpi/tpi.py
"""
from mpmath import mp, mpf, pi, quad, sin, cos, tan, atan, asin, acos, sqrt, exp, besseli, gamma, log, inf, nprod, findroot

mp.dps = 50
TWO_PI = 2 / pi
TOL = mpf(10) ** -40
def q(f, a, b):
    with mp.workdps(2 * mp.dps):      # (run 2: endpoint singularities, as in the arcsine law, need the extra digits)
        return +quad(f, [a, b])
def qs(f, pts):
    with mp.workdps(2 * mp.dps):
        return +quad(f, sorted(pts))
results = []

# route (for P1): E an even turn in the standard derivation; H a hidden one of the kinds named in the plan (an
# equal-spread normal pair, a phase even in time, a Haar measure); S the circle as a shape only (a semicircle's area or
# the arcsine integral, a turn only after a substitution the derivation does not make); P a pole; U undetermined.
# form (for P2): (i)-(iv) as in the plan; 'D' a dimension over a turn; 'P' a pole; 'C' a convention; '(iv)*' only after
# a substitution; '?' not traced. Both are judgments, made from the derivation step as the source (or the catalogue)
# gives it; the computations check the constants, not the judgments.
def entry(name, form, turn, computed, target, note='', route='E', tol=None):
    t = TOL if tol is None else tol
    ok = abs(computed - target) < t * max(1, abs(target))
    results.append((name, form, turn, computed, target, ok, note, route))

# ---- known before the search (the plan's list) ----

# the sweep: an even quarter turn read as v/h = tan θ; its law at s is the share of the turn done
s = mpf(3)
entry('the sweep, P(v/h <= s), s = 3', '(ii)', 'θ even on [0, π/2], v/h = tan θ',
      q(lambda x: 2 / (pi * (1 + x * x)), 0, s), TWO_PI * atan(s))

# Buffon: centre x even on [0, d/2], angle even on [0, π/2]; crossing when x <= (ℓ/2) cos θ; ℓ = 0.7, d = 1
l, d = mpf('0.7'), mpf(1)
buf = q(lambda t: min(l / 2 * cos(t), d / 2), 0, pi / 2) / ((d / 2) * (pi / 2))
entry("Buffon's needle, l = 0.7 d", '(i)', 'needle angle even over the turn', buf, TWO_PI * l / d)

# Viète: one cosine per halving of the quarter turn
vi = nprod(lambda k: cos(pi / 2 ** (k + 1)), [1, 170])
entry("Viète's product", '(iii)', 'the quarter turn halved again and again', vi, TWO_PI)

# the arcsine law: x = sin²θ, θ even on [0, π/2]; also two equal-spread normals' share X²/(X² + Y²)
t = mpf('0.3')
entry('arcsine law, P(x <= 0.3)', '(ii)', 'θ even; x = sin²θ (or the share of an equal-spread pair)',
      q(lambda x: 1 / (pi * sqrt(x * (1 - x))), 0, t), TWO_PI * asin(sqrt(t)), route='H')

# an averaging AC meter: |sin| of a phase even in time
entry('AC meter: mean |sin| over a cycle', '(i)', 'phase even in time',
      qs(lambda p: abs(sin(p)), [0, pi, 2 * pi]) / (2 * pi), TWO_PI)

# a square pixel at Nyquist: the wave's phase runs evenly across the pixel, half a turn wide
entry("square pixel's response at Nyquist", '(iii)', 'phase even across the pixel, [-π/2, π/2]',
      q(lambda x: cos(pi * x), -mpf(1) / 2, mpf(1) / 2), TWO_PI)

# Van Vleck: two unit vectors at angle α, a direction g even over the turn; signs differ when g's line falls between
alpha = mpf('0.9'); rho = cos(alpha)
differ = qs(lambda th: 1 if (cos(th) > 0) != (cos(th - alpha) > 0) else 0,
            [0, pi / 2, alpha + pi / 2, 3 * pi / 2, alpha + 3 * pi / 2, 2 * pi]) / (2 * pi)   # (run 2: the breakpoints of run 1 were wrong)
entry("Van Vleck: E[sgn X sgn Y], ρ = cos 0.9", '(ii)', 'the pair\'s direction even (isotropy)', 1 - 2 * differ, TWO_PI * asin(rho), route='H')

# Kosterlitz–Thouless: the vortex's phase winds evenly with the polar angle; energy (K/2)∫|∇θ|² = πK ln(R/a),
# the entropy of placing it ln((R/a)²) = 2 ln(R/a); the balance gives K = 2/π. Computed per level of R/a.
energy_per_level = (mpf(1) / 2) * q(lambda ph: 1, 0, 2 * pi) * q(lambda r: 1 / r, 1, mp.e)   # per unit K, ln(R/a) = 1
entry('Kosterlitz–Thouless jump K_c', 'D', 'phase winds evenly round the vortex (full turn, ½ from the energy); '
      'the 2 is the plane\'s dimension (positions ∝ (R/a)²)', 2 / energy_per_level, TWO_PI,
      'π = ½·(full even turn); 2 = dimension, not a turn')

# the median against the mean, and the sign test against the t test (normal law): 4 f(0)², f(0)² = 1/(2π), the
# Gaussian's normalisation being the isotropic pair's full even turn
gauss_sq = q(lambda ph: 1, 0, 2 * pi) * q(lambda r: r * exp(-r * r / 2), 0, inf)   # (∫ e^{-x²/2})² in polar form
entry('ARE of the median (and sign test) under a normal law', '(iv)', 'the normal\'s pair turned evenly (2π), four '
      'quadrants', 4 / gauss_sq, TWO_PI, route='H')

# (E|Z|)²: the pair's E|X||Y| = E[R²]·E|cos φ sin φ|, φ even
EabsXY = q(lambda r: r ** 3 * exp(-r * r / 2), 0, inf) * qs(lambda ph: abs(cos(ph) * sin(ph)), [0, pi / 2, pi, 3 * pi / 2, 2 * pi]) / (2 * pi)
entry('(E|Z|)² for a standard normal (and the one-bit loss)', '(i)', 'the pair\'s angle even (isotropy)', EabsXY, TWO_PI, route='H')

# half-wave dipole: current cos kz along z in [-λ/4, λ/4]; phase kz even along the wire over [-π/2, π/2]
entry('half-wave dipole: effective length / physical length', '(i)', 'phase even along the wire',
      q(lambda u: cos(u), -pi / 2, pi / 2) / pi, TWO_PI)

# rolling wheel: rim speed 2v|sin(φ/2)|, φ even in time; mean 4v/π = 2·(2/π)·v
entry('rolling wheel: mean rim speed / 2v', '(i)', 'the wheel\'s turn even in time',
      q(lambda ph: abs(sin(ph / 2)), 0, 2 * pi) / (2 * pi), TWO_PI)

# 2D effusion: flux per n·v̄ = (1/2π)∫_{-π/2}^{π/2} cos θ dθ = 1/π = ½·(2/π); velocity directions even
entry('2D gas through a line: flux / (n v̄ / 2)', '(i)', 'velocity directions even over the turn',
      2 * q(lambda th: cos(th), -pi / 2, pi / 2) / (2 * pi), TWO_PI)

# Jordan's inequality: the chord of sin over the quarter turn has slope sin(π/2)/(π/2)
entry("Jordan's inequality: the chord's slope", '(iii)', 'sin θ/θ at the quarter turn', sin(pi / 2) / (pi / 2), TWO_PI)

# Flamant: σ_r = A cos θ/r; equilibrium ∫_{-π/2}^{π/2} A cos²θ dθ = P gives A = 2P/π
entry("Flamant's half-plane: A/P", '(iv)', 'directions into the half-plane measured evenly, weight cos²',
      1 / q(lambda th: cos(th) ** 2, -pi / 2, pi / 2), TWO_PI)

# Hertz line contact: p0√(1 − x²/a²) carries P; x = a sin θ, ∫ cos²θ dθ over the half turn = π/2; p0·a/P = 2/π
entry('Hertz line contact: p0·a/P', '(iv)*', 'the semi-ellipse\'s area (a turn only after x = a sin θ)',
      1 / q(lambda x: sqrt(1 - x * x), -1, 1), TWO_PI, route='S')

# Wigner's semicircle: normaliser of √(1 − x²) on [-1, 1]; the shadow of an even disc on a line
entry("Wigner's semicircle: density at 0", '(iv)*', 'the semicircle\'s area (moments; a turn only via the disc\'s shadow)',
      1 / q(lambda x: sqrt(1 - x * x), -1, 1), TWO_PI, route='S')

# Sato–Tate: (2/π) sin²θ on [0, π], the Haar measure of SU(2) on its classes
entry('Sato–Tate density coefficient', '(iv)', 'Haar measure of SU(2) on its rotation angle',
      1 / q(lambda th: sin(th) ** 2, 0, pi), TWO_PI, route='H')

# Chebyshev: the equilibrium measure of [0, 1] (charge on a strip), x = sin²θ, θ even; its law (2/π) arcsin √x
x0 = mpf('0.6')
entry("Chebyshev's equilibrium measure on [0, 1], at x = 0.6", '(ii)', 'nodes at evenly spaced angles; x = sin²θ',
      q(lambda x: 1 / (pi * sqrt(x * (1 - x))), 0, x0), TWO_PI * asin(sqrt(x0)))

# Goemans–Williamson: a hyperplane with an even normal separates two vectors at angle θ with probability θ/π;
# against (1 − cos θ)/2 the worst ratio is (2/π)·min θ/(1 − cos θ)
th_star = findroot(lambda th: (1 - cos(th)) - th * sin(th), 2.33)
gw = TWO_PI * th_star / (1 - cos(th_star))
entry('Goemans–Williamson ratio / (2/π)', '(ii)', 'the hyperplane\'s normal even over the turn',
      gw / TWO_PI, th_star / (1 - cos(th_star)), 'α = %s' % mp.nstr(gw, 10), route='H')

# ---- the catalogue's entries (gathered by a fresh agent; scratchpad catalogue.md; run 2) ----
from mpmath import si, ellipk, ellipe, agm, struveh, bessely, nsum, quadosc, fac2, asinh, mpc, re as mre, im as mim
# 1 Wallis: Euler's product for sin x/x at the quarter turn
entry('C1 Wallis product', '(iii)', 'sin x/x at x = π/2 (or the Wallis integrals over [0, π/2])',
      nprod(lambda n: 1 - 1 / (4 * n * n), [1, inf]), TWO_PI)
# 2 Bauer–Ramanujan: Σ(−1)^k (4k+1) [(2k−1)!!/(2k)!!]³
entry('C2 Bauer–Ramanujan series', '?', 'a Fourier–Legendre expansion (step not seen)',
      nsum(lambda k: (-1) ** int(k) * (4 * k + 1) * (fac2(2 * k - 1) / fac2(2 * k)) ** 3, [0, inf]), TWO_PI,
      route='U', tol=mpf(10) ** -25)
# 3 square wave: half-range coefficient; the norm ∫₀^π sin² = π/2
b1 = q(lambda x: sin(x), 0, pi) / q(lambda x: sin(x) ** 2, 0, pi)
entry('C3 square-wave Fourier coefficient / 2', '(iv)', 'phase even over a half turn, norm ∫sin² = π/2', b1 / 2, TWO_PI)
# 4 Wilbraham–Gibbs: (2/π)Si(π), the partial-sum kernel integrated to the first zero
entry('C4 Gibbs overshoot (2/π)Si(π)', '(iv)', 'the sine kernel to its first zero; the series\' 2/π',
      TWO_PI * q(lambda t: sin(t) / t if t else mpf(1), 0, pi), TWO_PI * si(pi))
# 5 Fourier sine transform: Dirichlet's ∫₀^∞ sin x/x dx = π/2
dirichlet = quadosc(lambda x: sin(x) / x if x else mpf(1), [0, inf], omega=1)
entry('C5 Fourier sine/cosine transform prefactor', '(iii)', 'Dirichlet: ∫ sin x/x = π/2 (the inner reading summed)', 1 / dirichlet, TWO_PI, tol=mpf(10) ** -30)
# 6 Lebesgue constant of Chebyshev nodes: Rivlin's form; its slope per e-fold of n is 2/π
def leb(n): return sum(1 / tan((2 * k + 1) * pi / (4 * (n + 1))) for k in range(n + 1)) / (n + 1)
slope6 = (leb(4095) - leb(2047)) / log(mpf(4096) / 2048)
entry('C6 Lebesgue constant, Chebyshev nodes: slope in log n', '(ii)', 'node angles evenly spaced over the half turn',
      slope6, TWO_PI, tol=mpf(10) ** -6)
# 7 Kac: Crofton through the equal-spread pair: crossings per unit length = E|Y|·f_X(0) = 1/π; E_n ≈ (2/π) log n
entry('C7 Kac: crossings per unit length × 2', '(i)', 'the pair (g·p, g·t) of a random direction, equal spreads',
      2 * q(lambda y: abs(y) * exp(-y * y / 2) / sqrt(2 * pi), -10, 10) * (1 / sqrt(2 * pi)) if False else
      2 * 2 * q(lambda y: y * exp(-y * y / 2) / sqrt(2 * pi), 0, inf) / sqrt(2 * pi), TWO_PI, route='H', tol=mpf(10) ** -30)
# 8 alternating permutations: Euler zigzag numbers exactly (Seidel–Entringer), A_n/n! against 2(2/π)^{n+1}
def zigzag(N):
    row, out = [1], [1]
    for n in range(1, N + 1):
        new = [0]
        for k in range(n): new.append(new[-1] + row[n - 1 - k])
        row = new; out.append(row[-1])
    return out
A = zigzag(240)
from math import factorial
ratio8 = mpf(A[240]) / factorial(240) / (2 * TWO_PI ** 241)
entry('C8 alternating permutations: A_n/n! ÷ 2(2/π)^{n+1}, n = 240', 'P', 'the pole of sec x + tan x at π/2 (no measure)',
      ratio8, mpf(1), route='P')
# 9 complete elliptic K: (2/π)K(k) = 1/agm(1, k′); the mean over an even quarter turn
k9 = mpf('0.6')
entry('C9 (2/π)K(k) = 1/agm(1, k′), k = 0.6', '(iv)', 'mean over θ even on [0, π/2]',
      TWO_PI * q(lambda th: 1 / sqrt(1 - k9 ** 2 * sin(th) ** 2), 0, pi / 2), 1 / agm(1, sqrt(1 - k9 ** 2)))
# 10 Struve H₁ − Y₁ → 2/π: 1/(Γ(½)Γ(3/2)), Γ(½)² = π from the equal-spread pair's turn
gauss2 = q(lambda ph: 1, 0, 2 * pi) * q(lambda r: r * exp(-r * r), 0, inf)          # ∫∫ e^{−x²−y²} in polar form
entry('C10 Struve H₁ − Y₁ → 2/π (1/(Γ(½)Γ(3/2)))', '(iv)', 'Γ(½)² = ∫∫e^{−x²−y²}: the pair\'s full turn',
      1 / (sqrt(gauss2) * sqrt(gauss2) / 2), TWO_PI, route='H')
z10 = mpf(10) ** 6
entry('C10b H₁(z) − Y₁(z) at z = 10⁶', '(iv)', 'as above', struveh(1, z10) - bessely(1, z10), TWO_PI, route='H', tol=mpf(10) ** -11)
# 11–13 Sheppard's quadrant (Kendall's τ, Nesterov, Krivine): τ = 4P(X>0,Y>0) − 1, the wedge angle after whitening
rho13 = mpf(1) / 2
wedge = acos(-rho13)          # the angle of the positive quadrant after whitening
P13 = q(lambda ph: 1, 0, wedge) / (2 * pi)
entry("C13 Kendall's τ under normality, ρ = ½", '(ii)', 'the whitened wedge\'s angle over the turn (Sheppard)',
      4 * P13 - 1, TWO_PI * asin(rho13), route='H')
entry('C12 Krivine: c = (2/π) ln(1 + √2), sinh(cπ/2) = 1', '(ii)', 'the same sign-rounding identity',
      sinh_c := (exp(TWO_PI * log(1 + sqrt(2)) * pi / 2) - exp(-TWO_PI * log(1 + sqrt(2)) * pi / 2)) / 2, mpf(1), route='H')
entry('C11 Nesterov: E sgn·sgn = (2/π) arcsin, at ρ = 0.3', '(ii)', 'a Gaussian direction (the pair)',
      1 - 2 * acos(mpf('0.3')) / pi, TWO_PI * asin(mpf('0.3')), route='H')
# 14 centroid of a semicircular arc: ∫₀^π sin θ dθ / π
entry('C14 semicircular arc centroid ȳ/r', '(i)', 'θ even along the arc', q(lambda th: sin(th), 0, pi) / pi, TWO_PI)
# 15 mean chord between random points on a circle / 2r
entry('C15 mean chord on a circle / 2r', '(i)', 'the central angle even', q(lambda th: sin(th / 2), 0, pi) / pi, TWO_PI)
# 16 pendulum: T/T₀ = (2/π)K(sin θ₀/2), the period computed from the motion itself
th0 = mpf('1.2')
T_over_T0 = q(lambda th: 1 / sqrt(2 * (cos(th) - cos(th0))), 0, th0) * 4 / (2 * pi)
entry('C16 pendulum T/T₀ at θ₀ = 1.2', '(iv)', 'sin u = sin(θ/2)/sin(θ₀/2), u even over the quarter turn',
      T_over_T0, TWO_PI * ellipk(sin(th0 / 2) ** 2), tol=mpf(10) ** -25)
# 17 Onsager: the normalised (2/π)K, as 9
entry("C17 Onsager's (2/π)K = ₂F₁(½,½;1;k²), k² = 0.5", '(iv)', 'Fourier modes θ even', TWO_PI * ellipk(mpf('0.5')),
      1 / agm(1, sqrt(mpf('0.5'))))
# 18 resistor grid: R(1,1)/R from the Brillouin-zone integral, the inner integral done by residues
def r18(x):
    A = 2 - cos(x); s2 = sqrt(A * A - 1)
    return mpf(1) if s2 == 0 else (1 - A * cos(x)) / s2 + cos(x)      # (its limit at the zone's centre is 1)
entry('C18 infinite grid, diagonal R(1,1)/R', '?', 'wave-vector phases even over the zone', qs(r18, [-pi, 0, pi]) / (2 * pi), TWO_PI, tol=mpf(10) ** -30)
# 19 sticks' excluded area: mean |sin γ| over γ even
entry('C19 random sticks: ⟨A_ex⟩/L²', '(i)', 'relative angle even', qs(lambda g: abs(sin(g)), [0, pi]) / pi, TWO_PI)
# 20 Stoner–Wohlfarth, axes random in the plane
entry('C20 Stoner–Wohlfarth remanence, axes in a plane', '(i)', 'easy axes even in the plane', q(lambda p: cos(p), 0, pi / 2) / (pi / 2), TWO_PI)
# 21 Bell's local model: signs differ on θ/π of the directions
th21 = mpf('1.1')
diff21 = qs(lambda l: 1 if (cos(l) > 0) != (cos(l - th21) > 0) else 0, [0, pi / 2, th21 + pi / 2, 3 * pi / 2, th21 + 3 * pi / 2, 2 * pi]) / (2 * pi)
entry("C21 Bell's model: P(a,b) + 1 at θ = 1.1", '(ii)', 'λ even over directions', 2 * diff21, TWO_PI * th21)
# 22 Kramers–Kronig, one-sided: a Lorentz oscillator's real part from its imaginary part
w0, gm, w = mpf(1), mpf('0.3'), mpf('0.7')
chi = lambda x: 1 / (w0 ** 2 - x ** 2 - 1j * gm * x)
g22 = lambda x: x * mim(chi(x)) / (x + w)
pv = qs(lambda x: (g22(x) - g22(w)) / (x - w) if x != w else mpf(0), [0, w, w0, 2 * w]) + qs(lambda x: g22(x) / (x - w), [2 * w, 3, 10, inf])   # (split at the peak)
entry('C22 Kramers–Kronig, one-sided: χ₁ from χ₂', '(iv)', 'a half turn about the pole, folded to ω ≥ 0', TWO_PI * pv, mre(chi(w)), tol=mpf(10) ** -20)
# 23 Gaussian beam: P = ∫ I₀ e^{−2r²/w²} 2πr dr
entry('C23 Gaussian beam I₀w²/P', 'C', 'azimuth even (2π); the radial ¼ from the 1/e² convention',
      1 / (q(lambda ph: 1, 0, 2 * pi) * q(lambda r: r * exp(-2 * r * r), 0, inf)), TWO_PI)
# 24 binary π-phase grating: first-order amplitude of a ±1 square transmission
a24 = abs(qs(lambda x: (1 if x < pi else -1) * exp(-1j * x), [0, pi, 2 * pi]) / (2 * pi))
entry('C24 binary phase grating |a±1|', '(iv)', 'Fourier phase even', a24, TWO_PI)
# 25 thin disc: the potential at the centre, ∫₀^a dr/√(a² − r²) = π/2
entry('C25 disc capacitance C/(4πε₀a)', '(iv)*', 'radial arcsine integral (no turn in the step)',
      1 / q(lambda r: 1 / sqrt(1 - r * r), 0, 1), TWO_PI, route='S')
# 27 baffled piston: X₁(2ka) = 2H₁(2ka)/(2ka) against 8ka/(3π) at small ka
ka = mpf(10) ** -8
entry('C27 piston reactance at small ka ÷ 8ka/(3π)', '(iv)', 'Struve\'s series, as C10', 2 * struveh(1, 2 * ka) / (2 * ka) / (8 * ka / (3 * pi)),
      mpf(1), route='H', tol=mpf(10) ** -14)
# 28 penny-shaped crack, Irwin's route: K = σ√(πa)/E(0), E(0) the ellipse angle's integral
entry('C28 penny crack K_I/(σ√(πa))', '(iv)', 'the ellipse\'s parametric angle (Irwin); none by Sneddon\'s route',
      1 / q(lambda ph: 1, 0, pi / 2), TWO_PI)
# 29, 30 Sneddon's cone and Oliver–Pharr: d = a tan θ ∫₀¹ dx/√(1 − x²)
d29 = q(lambda x: 1 / sqrt(1 - x * x), 0, 1)
entry('C29 Sneddon cone: contact depth / total depth', '(iv)*', 'Abel/arcsine integral (no turn in the step)', 1 / d29, TWO_PI, route='S')
entry('C30 Oliver–Pharr ε for a cone', '(iv)*', 'from C29', 2 * (1 - 1 / d29), 2 * (pi - 2) / pi, route='S')
# 31 loaded circle on a half-space: edge/centre deflection, ∫₀^π 2√(a² − r² sin²φ) dφ at r = a and r = 0
entry('C31 loaded circle: edge/centre deflection', '(iv)', 'polar angle φ about the field point, even',
      qs(lambda ph: 2 * sqrt(1 - sin(ph) ** 2), [0, pi / 2, pi]) / q(lambda ph: 2, 0, pi), TWO_PI)   # (split at the kink)
# 32 stress drop, surface-breaking fault: mean/peak slip of the half-ellipse π/4, mirrored: 2/π
entry('C32 stress drop C (surface-breaking)', '(iv)*', 'area under the semi-elliptical slip (no turn in the step)',
      1 / (2 * q(lambda x: sqrt(1 - x * x), -1, 1) / 2), TWO_PI, route='S')
# 33 fibres random in a plane
entry('C33 fibre orientation factor (2D)', '(i)', 'fibre angle even in the plane', q(lambda t: abs(cos(t)), -pi / 2, pi / 2) / pi, TWO_PI)
# 34, 40, 41 the square wave's fundamental: (2/π)∫₀^π sin t dt = 4/π
entry('C34 relay describing function N·A/(2T)', '(i)', 'time phase even', TWO_PI * q(lambda t: sin(t), 0, pi) / 2, TWO_PI)
entry('C40 Campbell–Robson: square/sine sensitivity / 2 (measured: 4/π)', '(i)', 'the square wave\'s fundamental', q(lambda t: sin(t), 0, pi) / pi, TWO_PI)
# 35 saturation describing function at T/A = ½, by its Fourier coefficient
TA = mpf(1) / 2; psT = asin(TA)
a35 = 4 / pi * (q(lambda p: sin(p) ** 2, 0, psT) + q(lambda p: TA * sin(p), psT, pi / 2))
entry('C35 saturation describing function, T/A = ½', '(iv)', 'Fourier phase even', a35, TWO_PI * (asin(TA) + TA * sqrt(1 - TA ** 2)))
# 36, 39 six-step inverter and the air-gap MMF: fundamental of a ±½ square wave
entry('C36 six-step inverter V₁/V_DC', '(i)', 'Fourier phase even', 2 * q(lambda t: sin(t) / 2, 0, pi) / pi, TWO_PI)
# 37 switching mixer: LO square wave (4/π), halved by the product
entry('C37 switching mixer G_c/g_m', '(i)', 'Fourier phase even', (4 / pi) / 2, TWO_PI)
# 38 class B: worst dissipation where d/dV[(2/π)V·Vcc − V²/2] = 0
entry('C38 class B: worst-dissipation swing / V_CC', '(i)', 'the rectified sine\'s mean (phase even)',
      findroot(lambda V: TWO_PI - V, 0.5), q(lambda t: sin(t), 0, pi) / pi)
# 42 canopy, vertical leaves: mean over leaf azimuth of |sin ψ cos φ|
psi = mpf('0.7')
entry('C42 canopy G for vertical leaves / sin ψ', '(i)', 'leaf azimuth even',
      qs(lambda ph: abs(sin(psi) * cos(ph)), [0, pi / 2, 3 * pi / 2, 2 * pi]) / (2 * pi) / sin(psi), TWO_PI)
# 43 animals at equal speeds, directions even: mean relative speed / 2v
entry('C43 animal encounters ⟨v_rel⟩/2v', '(i)', 'heading difference even', q(lambda th: sin(th / 2), 0, pi) / pi, TWO_PI)
# 44 rotational broadening: normaliser of √(1 − x²)
entry('C44 rotational broadening kernel at 0 × Δλ_L', '(iv)*', 'the half disc\'s area (no turn in the step)',
      1 / q(lambda x: sqrt(1 - x * x), -1, 1), TWO_PI, route='S')
# 45 Fabry–Pérot: full width at half maximum in phase over the free spectral range 2π
F45 = mpf(40)
half = findroot(lambda ph: 1 / (1 + F45 * sin(ph / 2) ** 2) - mpf(1) / 2, 0.3)
entry('C45 Fabry–Pérot FWHM / FSR, F = 40', '(ii)', 'round-trip phase even over the turn', 2 * half / (2 * pi),
      TWO_PI * asin(1 / sqrt(F45)))

# ---- report ----
print("entry | route | form | where π enters | computed | as written | match")
for name, form, turn, c, tg, ok, note, route in results:
    print(f"{name} | {route} | {form} | {turn} | {mp.nstr(c, 15)} | {mp.nstr(tg, 15)} | {'yes' if ok else 'NO'}" + (f" | {note}" if note else ''))
print(f"\nall constants match: {all(r[5] for r in results)} ({sum(r[5] for r in results)} of {len(results)})")
routes = {}
for r in results: routes.setdefault(r[7], []).append(r[0])
for k in 'EHSPU':
    if k in routes: print(f"route {k}: {len(routes[k])}" + (': ' + '; '.join(routes[k]) if k in 'SPU' else ''))
bad_form = [(r[0], r[1]) for r in results if r[1] not in ('(i)', '(ii)', '(iii)', '(iv)')]
print("P1: " + ('KILLED by ' + '; '.join(routes.get('S', []) + routes.get('P', [])) if routes.get('S') or routes.get('P') else 'not killed')
      + (f" (undetermined: {'; '.join(routes['U'])})" if 'U' in routes else ''))
print("P2: " + ('KILLED by ' + '; '.join(f'{n} [{f}]' for n, f in bad_form) if bad_form else 'not killed'))

# ---- P3: the dimension rule ----
print("\nP3, the two families")
mean_abs = lambda n: gamma(mpf(n) / 2) / (sqrt(pi) * gamma((mpf(n) + 1) / 2))           # mean |x1| on the sphere S^{n-1}
ball_norm = lambda n: gamma(mpf(n) / 2 + 1) / (sqrt(pi) * gamma((mpf(n) + 1) / 2))       # density at 0 of the n-ball's shadow
# Buffon in n dimensions: the mean |cos| of an even direction, computed by integrating over the sphere's polar angle
def mean_abs_cos(n):
    w = lambda t: sin(t) ** (n - 2)
    return (q(lambda t: abs(cos(t)) * w(t), 0, pi / 2) + q(lambda t: abs(cos(t)) * w(t), pi / 2, pi)) / q(w, 0, pi)   # (run 2: split at the kink)
def ball_shadow_at0(n):        # density at 0 of x₁ for an even n-ball: ∫(1 − x²)^((n−1)/2) normalised
    return 1 / q(lambda x: (1 - x * x) ** ((mpf(n) - 1) / 2), -1, 1)
for n, want1, want2 in [(2, TWO_PI, TWO_PI), (3, mpf(1) / 2, mpf(3) / 4), (4, 4 / (3 * pi), 8 / (3 * pi))]:
    a, b = mean_abs_cos(n), ball_shadow_at0(n)
    print(f"  n = {n}: mean shadow {mp.nstr(a, 12)} (family {mp.nstr(want1, 12)}), even ball's shadow at 0 "
          f"{mp.nstr(b, 12)} (family {mp.nstr(want2, 12)})")
    p3ok = abs(a - want1) < TOL and abs(b - want2) < TOL
# the physical ones: Buffon between planes (ℓ/(2d)) and the 3D gas through a wall (n v̄/4 = n v̄·½·½)
effuse3 = q(lambda t: cos(t) * sin(t), 0, pi / 2) / q(lambda t: sin(t), 0, pi)     # (1/4π)∫cosθ dΩ over the hemisphere
print(f"  Buffon between planes: P·d/ℓ = {mp.nstr(mean_abs_cos(3), 12)} (½); 3D gas through a wall: flux/(n v̄) = "
      f"{mp.nstr(effuse3, 12)} (¼ = ½·½)")
p3 = all(abs(mean_abs_cos(n) - w1) < TOL and abs(ball_shadow_at0(n) - w2) < TOL
         for n, w1, w2 in [(2, TWO_PI, TWO_PI), (3, mpf(1) / 2, mpf(3) / 4), (4, 4 / (3 * pi), 8 / (3 * pi))]) \
     and abs(mean_abs_cos(3) - mpf(1) / 2) < TOL and abs(effuse3 - mpf(1) / 4) < TOL
sph = lambda f: q(lambda t: f(t) * sin(t), 0, pi) / 2                    # mean over directions even on the sphere (polar angle t)
hemi = lambda f: q(lambda t: f(t) * sin(t), 0, pi / 2)                   # mean over the hemisphere
rebuilt = [
    ('C14 arc centroid -> hemispherical shell centroid / r', hemi(lambda t: cos(t)), mpf(1) / 2),
    ('C20 remanence, axes random in space', hemi(lambda t: cos(t)), mpf(1) / 2),
    ('C33 fibres random in space', hemi(lambda t: cos(t)), mpf(1) / 2),
    ('C42 canopy, leaves random in space (spherical): G', hemi(lambda t: cos(t)), mpf(1) / 2),
    ('C19 sticks -> rods: mean |sin γ| over the sphere', sph(lambda t: sin(t)), mpf(1) / 2),
    ('C15 mean chord on a sphere / 2r', sph(lambda t: sin(t / 2)), mpf(1) / 2),
    ('C43 encounters in space: mean relative speed / 2v', sph(lambda t: sin(t / 2)), mpf(1) / 2),
]
for name, val, want in rebuilt:
    ok = abs(val - want) < TOL
    p3 &= ok
    print(f"  {name}: {mp.nstr(val, 12)} ({'½, as the family' if ok else 'not ½'})")
print(f"P3: {'not killed' if p3 else 'KILLED'}")

# ---- P4: evenness is what gives it ----
print("\nP4, uneven turns (von Mises concentration κ about 0; spreads in ratio c)")
vm = lambda k: (lambda th: exp(k * cos(th)) / (2 * pi * besseli(0, k)))
def vm_mean(f, k):
    return qs(lambda th: f(th) * vm(k)(th), [-pi, -pi / 2, 0, pi / 2, pi])
p4 = True
rows = []
for k in [mpf('0.5'), mpf(1), mpf(2)]:
    buf_k = vm_mean(lambda th: abs(cos(th)), k)                     # Buffon / AC / effusion: mean |cos| of the orientation
    ac_k = vm_mean(lambda th: abs(sin(th)), k)                      # an AC phase spending more time near 0
    pix_k = qs(lambda th: cos(th) * exp(k * cos(2 * th)), [-pi / 2, 0, pi / 2]) / qs(lambda th: exp(k * cos(2 * th)), [-pi / 2, 0, pi / 2])
    rows.append((k, buf_k, ac_k, pix_k))
    p4 &= all(abs(v - TWO_PI) > mpf(10) ** -6 for v in (buf_k, ac_k, pix_k))
for k, a, b, c in rows:
    print(f"  κ = {mp.nstr(k, 3)}: mean |cos| {mp.nstr(a, 10)}, mean |sin| {mp.nstr(b, 10)}, pixel with uneven phase {mp.nstr(c, 10)}  (2/π = {mp.nstr(TWO_PI, 10)})")
for cc in [mpf(1) / 2, mpf(2)]:
    sweep_c = TWO_PI * atan(1 / cc)                                  # P(v/h <= 1) drawn at V = cH: the median moves
    arcs_c = TWO_PI * atan(sqrt(t / (1 - t)) / cc)                  # P(Y²/(X²+Y²) <= t), spreads 1 and c
    print(f"  c = {mp.nstr(cc, 3)}: sweep P(v/h <= 1) = {mp.nstr(sweep_c, 10)} (½ at c = 1); share P(x <= 0.3) = "
          f"{mp.nstr(arcs_c, 10)} (arcsine {mp.nstr(TWO_PI * asin(sqrt(t)), 10)})")
    p4 &= abs(sweep_c - mpf(1) / 2) > mpf(10) ** -6 and abs(arcs_c - TWO_PI * asin(sqrt(t))) > mpf(10) ** -6
print(f"P4: {'not killed' if p4 else 'KILLED'}")
