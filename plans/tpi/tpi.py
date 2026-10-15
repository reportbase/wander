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

def entry(name, form, turn, computed, target, note=''):
    ok = abs(computed - target) < TOL * max(1, abs(target))
    results.append((name, form, turn, computed, target, ok, note))

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
      q(lambda x: 1 / (pi * sqrt(x * (1 - x))), 0, t), TWO_PI * asin(sqrt(t)))

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
entry("Van Vleck: E[sgn X sgn Y], ρ = cos 0.9", '(ii)', 'the pair\'s direction even (isotropy)', 1 - 2 * differ, TWO_PI * asin(rho))

# Kosterlitz–Thouless: the vortex's phase winds evenly with the polar angle; energy (K/2)∫|∇θ|² = πK ln(R/a),
# the entropy of placing it ln((R/a)²) = 2 ln(R/a); the balance gives K = 2/π. Computed per level of R/a.
energy_per_level = (mpf(1) / 2) * q(lambda ph: 1, 0, 2 * pi) * q(lambda r: 1 / r, 1, mp.e)   # per unit K, ln(R/a) = 1
entry('Kosterlitz–Thouless jump K_c', '(?)', 'phase winds evenly round the vortex (full turn, ½ from the energy); '
      'the 2 is the plane\'s dimension (positions ∝ (R/a)²)', 2 / energy_per_level, TWO_PI,
      'π = ½·(full even turn); 2 = dimension, not a turn')

# the median against the mean, and the sign test against the t test (normal law): 4 f(0)², f(0)² = 1/(2π), the
# Gaussian's normalisation being the isotropic pair's full even turn
gauss_sq = q(lambda ph: 1, 0, 2 * pi) * q(lambda r: r * exp(-r * r / 2), 0, inf)   # (∫ e^{-x²/2})² in polar form
entry('ARE of the median (and sign test) under a normal law', '(iv)', 'the normal\'s pair turned evenly (2π), four '
      'quadrants', 4 / gauss_sq, TWO_PI)

# (E|Z|)²: the pair's E|X||Y| = E[R²]·E|cos φ sin φ|, φ even
EabsXY = q(lambda r: r ** 3 * exp(-r * r / 2), 0, inf) * qs(lambda ph: abs(cos(ph) * sin(ph)), [0, pi / 2, pi, 3 * pi / 2, 2 * pi]) / (2 * pi)
entry('(E|Z|)² for a standard normal (and the one-bit loss)', '(i)', 'the pair\'s angle even (isotropy)', EabsXY, TWO_PI)

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
entry('Hertz line contact: p0·a/P', '(iv)', 'x = a sin θ, θ even over the half turn, weight cos²',
      1 / q(lambda th: cos(th) ** 2, -pi / 2, pi / 2), TWO_PI)

# Wigner's semicircle: normaliser of √(1 − x²) on [-1, 1]; the shadow of an even disc on a line
entry("Wigner's semicircle: density at 0", '(iv)', 'x = cos θ, weight sin²θ over the half turn; the even disc\'s shadow',
      1 / q(lambda x: sqrt(1 - x * x), -1, 1), TWO_PI)

# Sato–Tate: (2/π) sin²θ on [0, π], the Haar measure of SU(2) on its classes
entry('Sato–Tate density coefficient', '(iv)', 'Haar measure of SU(2) on its rotation angle',
      1 / q(lambda th: sin(th) ** 2, 0, pi), TWO_PI)

# Chebyshev: the equilibrium measure of [0, 1] (charge on a strip), x = sin²θ, θ even; its law (2/π) arcsin √x
x0 = mpf('0.6')
entry("Chebyshev's equilibrium measure on [0, 1], at x = 0.6", '(ii)', 'nodes at evenly spaced angles; x = sin²θ',
      q(lambda x: 1 / (pi * sqrt(x * (1 - x))), 0, x0), TWO_PI * asin(sqrt(x0)))

# Goemans–Williamson: a hyperplane with an even normal separates two vectors at angle θ with probability θ/π;
# against (1 − cos θ)/2 the worst ratio is (2/π)·min θ/(1 − cos θ)
th_star = findroot(lambda th: (1 - cos(th)) - th * sin(th), 2.33)
gw = TWO_PI * th_star / (1 - cos(th_star))
entry('Goemans–Williamson ratio / (2/π)', '(ii)', 'the hyperplane\'s normal even over the turn',
      gw / TWO_PI, th_star / (1 - cos(th_star)), 'α = %s' % mp.nstr(gw, 10))

# ---- report ----
print("entry | form | where the turn enters | computed | as written | match")
for name, form, turn, c, tg, ok, note in results:
    print(f"{name} | {form} | {turn} | {mp.nstr(c, 15)} | {mp.nstr(tg, 15)} | {'yes' if ok else 'NO'}" + (f" | {note}" if note else ''))

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
