# Where 2/π appears: a catalogue

Compiled 15 Oct 2026. 2/π = 0.636620; π/2 = 1.570796; √(2/π) = 0.797885.

**Scope and conventions**

- The items the brief excludes are left out: the half-Cauchy distribution function, Buffon's needle in 2D and 3D, Viète, the arcsine laws and Jeffreys's binomial prior, the rectified-sine average, the square pixel's MTF at Nyquist, Van Vleck's one-bit correlation and one-bit loss, the KT jump, the efficiencies of the median and the sign test, (E|Z|)², the half-wave dipole's λ/π, the rolling wheel's 4v/π, 2D effusion, Jordan, Flamant, Hertz line contact, the Wigner semicircle, Sato–Tate, the Chebyshev/equilibrium measure, Goemans–Williamson, and the Bessel √(2/(πx)).
- **Check status.** "(checked)" means I saw the formula in the source itself or in a search snippet quoting it. "(from memory)" means I did not see it. "(partly checked)" means part was seen, and the entry says which part.
- **"Shares an integral with an excluded item"** marks an entry that is a distinct occurrence in its own field but whose 2/π comes from the same integral or identity as an excluded item. For example, the mean of |cos θ| over a uniform angle is the same integral as the rectified-sine average, and Sheppard's arcsine identity is behind Van Vleck. These entries are counted, and flagged so they can be set aside.
- **Multiples.** A multiple such as 4/π or 8/(3π) is included only where the source writes it as, or derives it from, a 2/π. The derivation is quoted when that is the only link.
- **"π step"** gives where π enters in the standard derivation as I found it. **"Angle?"** answers plainly whether that step has an angle, a phase or a rotation in it.

---

## Summary table (main catalogue: 45 entries)

| # | Name | Field | Form | Check | Angle in π step? |
|---|------|-------|------|-------|------------------|
| 1 | Wallis product | Analysis | 2/π = ∏(1 − 1/4n²) | checked | yes (sine's argument, or Wallis integrals over [0, π/2]) |
| 2 | Bauer–Ramanujan series | Series / number theory | 2/π = Σ(−1)ᵏ(4k+1)[(2k−1)!!/(2k)!!]³ | checked | not determined |
| 3 | Square-wave Fourier series | Fourier analysis | (2c/π)(sin ωx + ⅓ sin 3ωx + …) | checked | yes (Fourier phase) |
| 4 | Wilbraham–Gibbs overshoot | Fourier analysis | (2/π)Si(π) = 1.17898 | checked | yes (Fourier phase) |
| 5 | Fourier sine/cosine transforms | Analysis | F(α) = (2/π)∫₀^∞ f(x) sin αx dx | checked | yes (Fourier phase) |
| 6 | Lebesgue constant, Chebyshev nodes | Approximation theory | Λₙ ≈ (2/π) log(n+1) + 0.9625 | checked | yes (node angles) |
| 7 | Kac's real roots | Probability | Eₙ = (2/π) log n + 0.6257 + … | checked | yes (Crofton on the sphere) |
| 8 | Alternating permutations | Combinatorics | Aₙ ~ 2(2/π)^{n+1} n! | checked | **no** (pole of sec x + tan x) |
| 9 | Complete elliptic K and the AGM | Special functions | (2/π)K(k) = 1/agm(1, k′) | checked | yes (θ in Legendre's form) |
| 10 | Struve H₁ at large argument | Special functions | H₁(z) → 2/π | checked | **no** in the step found (Γ-function constant) |
| 11 | Nesterov's π/2 theorem | Optimisation / algorithms | (2/π)·SDP ≤ OPT ≤ SDP | checked | yes (angle between vectors) |
| 12 | Krivine's bound / cut norm | Functional analysis / algorithms | K_G ≤ π/(2 ln(1+√2)); c = (2/π) ln(1+√2) | checked | yes |
| 13 | Kendall's τ (Greiner) | Statistics | τ = (2/π) arcsin ρ | checked | yes (quadrant wedge angle) |
| 14 | Centroid of a semicircular arc | Statics / geometry | ȳ = 2r/π | checked | yes |
| 15 | Mean chord between random points on a circle | Geometric probability | s̄ = 4r/π | checked | yes |
| 16 | Pendulum period | Classical mechanics | T = (2/π)T₀K(sin θ₀/2) | checked | yes |
| 17 | 2D Ising internal energy | Statistical mechanics | U = −J coth 2βJ[1 + (2/π)(2tanh²2βJ − 1)K] | checked | yes (Fourier modes) |
| 18 | Infinite resistor grid, diagonal | Electrical networks | R(1,1) = (2/π)R | checked | yes (Brillouin zone) |
| 19 | Excluded area of random sticks | Percolation / condensed matter | ⟨A_ex⟩ = (2/π)L² | checked | yes |
| 20 | Stoner–Wohlfarth, in-plane random axes | Magnetism | M_r/M_s = 2/π | from memory | yes |
| 21 | Bell's linear local model | Quantum foundations | P(a,b) = −1 + 2θ/π | partly checked | yes |
| 22 | Kramers–Kronig, one-sided | Optics / EM / condensed matter | χ₁ = (2/π)P∫₀^∞ ω′χ₂/(ω′² − ω²) dω′ | checked | yes (half-turn about a pole) |
| 23 | Gaussian beam peak intensity | Laser optics | I₀ = 2P/(πw₀²) | checked | yes (azimuth) |
| 24 | Binary phase grating | Diffractive optics | a±₁ = ∓2i/π, η = (2/π)² | checked | yes (Fourier) |
| 25 | Capacitance of a thin disc | Electrostatics | C = 8ε₀a = (2/π)·4πε₀a | checked | **no** (radial arcsine integral) |
| 26 | Microstrip synthesis (Wheeler) | Microwave engineering | w/h = (2/π)[(d−1) − ln(2d−1)] + … | checked | not determined |
| 27 | Baffled piston reactance | Acoustics | X₁ ≈ 8ka/(3π); → 2/(πka) | checked | as #10 |
| 28 | Penny-shaped crack | Fracture mechanics | K_I = (2/π)σ√(πa) | checked | **no** by Sneddon's route; yes by Irwin's |
| 29 | Sneddon's conical indenter | Contact mechanics | F = 2E d²/(π(1−ν²) tan θ); d = (π/2)ε | checked | **no** (Abel/arcsine integral) |
| 30 | Oliver–Pharr ε for a cone | Nanoindentation | ε = 2(π−2)/π = 0.727 | partly checked | **no** (from #29) |
| 31 | Uniformly loaded circle on a half-space | Elasticity / geotechnics | w_edge/w_centre = 2/π | checked | yes (polar integration) |
| 32 | Earthquake stress drop, long fault | Seismology | Δσ = (2/π)μD̄/W | checked | **no** (area under the slip ellipse) |
| 33 | Fibre orientation factor, 2D random | Civil engineering (FRC) | α = 2/π | checked | yes |
| 34 | Ideal relay describing function | Control | N = 4T/(πA), from (2/π)∫₀^π T sin t dt | checked | yes (Fourier) |
| 35 | Saturation describing function | Control | N = (2/π)[arcsin(T/A) + (T/A)√(1−T²/A²)] | checked | yes (Fourier) |
| 36 | Six-step inverter | Power electronics | V₁ = (2/π)V_DC | checked | yes (Fourier) |
| 37 | Single-balanced switching mixer | RF / communications | G_c = 2g_m/π | checked | yes (Fourier) |
| 38 | Class-B output stage | Analog electronics | P_S = (2/π)(V̂/R_L)V_CC; worst dissipation at V̂ = (2/π)V_CC | partly checked | yes (time phase) |
| 39 | Air-gap MMF of a full-pitch coil | Electric machines | F₁ = (4/π)(Ni/2) | checked | yes (Fourier) |
| 40 | Square- vs sine-wave grating threshold | Perception / psychophysics | sensitivity ratio 4/π | checked | yes (Fourier) |
| 41 | Coltman's square-wave/sine-wave relation | Imaging | C(f) = (4/π)[M(f) − M(3f)/3 + …] | from memory | yes (Fourier) |
| 42 | Canopy G-function, vertical leaves | Plant ecology | G = (2/π) sin ψ, K = (2/π) tan ψ | checked | yes (leaf azimuth) |
| 43 | Ideal-gas model of animal encounter | Animal ecology | v̄_rel = 4v/π | checked | yes |
| 44 | Rotational broadening kernel (ε = 0) | Astrophysics | G(x) = 2√(1−x²)/(πΔλ_L) | checked | **no** (area of a half disc) |
| 45 | Fabry–Pérot Airy linewidth | Optics / interferometry | Δν/Δν_FSR = (2/π) arcsin[(1−√R₁R₂)/(2(R₁R₂)^{1/4})] | checked | yes (round-trip phase) |

Entries flagged as sharing an integral or identity with an excluded item: 11, 12 and 13 (Sheppard/Grothendieck arcsine identity, as Van Vleck and Goemans–Williamson); 14, 19, 20, 33 and 42 (mean of |cos| over an orientation, the same integral as the rectified-sine average and Buffon's); 15 and 43 (average of 2 sin(θ/2), the same integral as the rolling wheel's 4v/π); 38 (the rectified-sine average itself, entering an optimum); 44 (the same function as the Wigner semicircle). That is 13 entries; the other 32 do not share one.

---

## Main catalogue, in detail

### Mathematics

**1. Wallis product.** *Analysis.*
2/π = ∏_{n≥1} (1 − 1/(4n²)); equivalently π/2 = ∏ 4n²/(4n² − 1).
Source: Wikipedia, "Wallis product" (Wallis 1656), https://en.wikipedia.org/wiki/Wallis_product. (checked: "2/π = ∏(1 − 1/4n²)" derived by setting x = π/2 in Euler's sine product.)
π step: Euler's infinite product sin x/x = ∏(1 − x²/(n²π²)) evaluated at x = π/2, where sin x = 1. Wallis's own route takes the ratio of the Wallis integrals ∫₀^{π/2} sinⁿx dx.
Angle? Yes. x is the argument of sine, or the integration variable on [0, π/2].
π/2 reading: the product written for π/2 is the same identity inverted.

**2. Bauer–Ramanujan series.** *Series / number theory.*
2/π = 1 − 5(1/2)³ + 9(1·3/(2·4))³ − 13(1·3·5/(2·4·6))³ + … = Σ_{k≥0} (−1)ᵏ(4k+1)[(2k−1)!!/(2k)!!]³.
Source: Bauer, "Von den Coefficienten der Reihen von Kugelfunctionen einer Variablen", J. reine angew. Math. 56 (1859) 101–121; it appears in Ramanujan's first letter to Hardy (1913). The form is quoted in Campbell & Levrie (2024), https://sites.math.rutgers.edu/~zeilberg/akherim/CampbellLevrie2024.pdf. (checked: the formula and "Bauer, via a Fourier–Legendre expansion" in search snippets.)
π step: Bauer obtained it from a Fourier–Legendre expansion. The bracket is (−1)ᵏ P_{2k}(0), the Legendre polynomial at 0. **The step where π enters was not seen in the sources checked.**
Angle? Not determined.

**3. Square-wave Fourier series.** *Fourier analysis / signal processing.*
For a square wave stepping between ±c/2 with period L and ω = 2π/L: S_N = (2c/π)(sin ωx + ⅓ sin 3ωx + … + sin((2N−1)ωx)/(2N−1)). For a ±1 wave the coefficients are 4/(nπ) for odd n.
Source: Wikipedia, "Gibbs phenomenon", square-wave example. (checked.) The half-range form b_n = (2/π)∫₀^π f(x) sin nx dx is in e.g. Kreyszig, *Advanced Engineering Mathematics*. (from memory.)
π step: the Fourier coefficient integral over a period. With b_n = (2/π)∫₀^π sin nx dx = 4/(nπ) for odd n, the 2/π is the half-range normalisation (one over the half-period π, doubled by odd symmetry).
Angle? Yes (Fourier phase nx).

**4. Wilbraham–Gibbs overshoot.** *Fourier analysis.*
For a jump of c, the N-th partial sum peaks at (c/π)∫₀^π (sin t/t) dt = (c/2)·(2/π)Si(π). Relative to the half-jump, the peak is (2/π)Si(π) = 1.178980, an overshoot of 0.0894899·c. Si(π) = 1.851937 = π/2 + π(0.0894899).
Source: Wikipedia, "Gibbs phenomenon"; Finch, *Mathematical Constants* (CUP 2003) §4.1; Wilbraham (1848). (checked.)
π step: the partial-sum kernel near the jump becomes the sine integral. The first maximum is at t = π (the first zero of sin t), and the prefactor is the series' 2/π (entry 3).
Angle? Yes (Fourier phase).

**5. Fourier sine and cosine transforms (2/π convention).** *Analysis.*
F_s(α) = (2/π)∫₀^∞ f(x) sin(αx) dx and F_c(α) = (2/π)∫₀^∞ f(x) cos(αx) dx, with inverses without the factor. The symmetric convention puts √(2/π) on both sides (see √(2/π) section, Q4).
Source: Wikipedia, "Sine and cosine transforms", citing Coleman, *An Introduction to Partial Differential Equations with MATLAB* (2nd ed., 2013), p. 221. (checked.)
π step: Fourier inversion. For odd f, f(x) = (2/π)∫₀^∞ sin(αx)[∫₀^∞ f(t) sin(αt) dt] dα. The 1/(2π) of the full transform is doubled twice by folding both integrals onto [0, ∞), and the convention puts the whole 2/π on one side. Equivalently, it rests on Dirichlet's integral ∫₀^∞ sin(kx)/x dx = π/2.
Angle? Yes (Fourier phase).

**6. Lebesgue constant of Chebyshev-node interpolation.** *Approximation theory / numerical analysis.*
(2/π) log(n+1) + a < Λₙ(T) < (2/π) log(n+1) + 1, with a = 0.9625…. For stretched nodes, Λₙ(S) < (2/π) log(n+1) + 0.7219…. The best possible nodes also give ~(2/π) log n.
Source: Wikipedia, "Lebesgue constant" (citing Brutman 1997, *Ann. Numer. Math.* 4:111; Rivlin). (checked.)
π step: Chebyshev nodes are xₖ = cos θₖ with equally spaced angles θₖ = (2k+1)π/(2n+2). Rivlin's closed form Λₙ = (1/(n+1)) Σ cot((2k+1)π/(4(n+1))) with cot u ≈ 1/u gives (4/π)Σ1/(2k+1) ≈ (2/π) ln n. (Rivlin's formula from memory.)
Angle? Yes (the node angles θₖ).

**7. Expected number of real roots of a random polynomial (Kac).** *Probability / random polynomials.*
For degree n with i.i.d. standard normal coefficients: Eₙ = (2/π) log n + 0.6257358072… + 2/(nπ) + O(1/n²).
Source: Edelman & Kostlan, "How many zeros of a random polynomial are real?", Bull. AMS 32 (1995) 1–37, arXiv:math/9501224; Kac, Bull. AMS 49 (1943) 314–320. (checked in the paper.)
π step (Edelman–Kostlan): "the expected number of real zeros is … the length of the moment curve (1, t, …, tⁿ) projected onto the surface of the unit sphere, divided by π". This is the integral-geometry (Crofton) fact that a random great hypersphere crosses a curve of length L on average L/π times. The projected curve has length ≈ 2 log n.
Angle? Yes (rotation-invariant measure on the sphere; arc length).

**8. Alternating (zigzag) permutations.** *Combinatorics.*
Aₙ ~ 2(2/π)^{n+1} n!, so the probability that a random permutation of n is alternating is ~2(2/π)^{n+1}.
Source: Wikipedia, "Alternating permutation"; Stanley, "A survey of alternating permutations", Contemp. Math. 531 (2010) 165–196. (checked.)
π step: André's theorem gives Σ Aₙxⁿ/n! = sec x + tan x (the solution of 2y′ = 1 + y², y(0) = 1). Its nearest singularity is a simple pole at x = π/2, where cos x first vanishes. The coefficients therefore grow like (2/π)ⁿ. (Pole argument from memory.)
Angle? **No.** No angle, phase or rotation appears in the combinatorial derivation; π enters only as the location of the generating function's first pole.

**9. Complete elliptic integral K and the arithmetic–geometric mean.** *Special functions.*
K(k) = π/(2 agm(1, √(1−k²))), so (2/π)K(k) = 1/agm(1, k′). Also (2/π)K(k) = ₂F₁(½, ½; 1; k²), and K(0) = π/2. Gauss's constant 1/agm(1, √2) = (2/π)K(1/√2), and the ratio of an ellipse's perimeter to the circle's 2πa is (2/π)E(e).
Source: Wikipedia, "Elliptic integral" and "Arithmetic–geometric mean"; DLMF §19.8. (checked: K = π/(2 agm).)
π step: K(k) = ∫₀^{π/2} dθ/√(1 − k² sin²θ). At k = 0 the integral is the length π/2 of the θ-range, so the factor 2/π normalises K to 1 at k = 0.
Angle? Yes (θ in Legendre's form).

**10. Struve function H₁ at large argument.** *Special functions.*
H₁(z) − Y₁(z) → 2/π as z → ∞, so H₁(z) ≈ 2/π − √(2/(πz)) cos(z − π/4) + O(1/z). The general form is H_α(x) − Y_α(x) ≈ (x/2)^{α−1}/(√π Γ(α + ½)), which equals 2/π at α = 1. The small-z series is H₁(z) = (2/π)[z²/(1²·3) − z⁴/(1²·3²·5) + …].
Source: Aarts & Janssen, "Approximation of the Struve function H₁ occurring in impedance calculations", J. Acoust. Soc. Am. 113 (2003) 2635–2637, eqs. (5), (6), (8), https://nuhagphp.univie.ac.at/janssen/data/p124.pdf; Abramowitz & Stegun §12.1.31; Wikipedia, "Struve function". (checked.)
π step: the large-z constant is 1/(Γ(½)Γ(3/2)) = 1/(√π·√π/2) = 2/π. The defining integral is H₁(z) = (2z/π)∫₀¹ √(1−t²) sin(zt) dt.
Angle? **No** in the asymptotic step as found: π enters through Γ(½)² = π.

**11. Nesterov's "π/2 theorem".** *Optimisation / algorithms.*
For a positive semidefinite W, the SDP relaxation of q* = max{xᵀWx : x ∈ {±1}ⁿ} satisfies (2/π)s* ≤ q* ≤ s*. The paper states this as relative accuracy μ = π/2 − 1.
Source: Nesterov, "Semidefinite relaxation and nonconvex quadratic optimization", Optim. Methods Softw. 9 (1998) 141–160; CORE DP 1997044, https://ideas.repec.org/p/cor/louvco/1997044.html. (checked via snippets of secondary statements.)
π step: Gaussian sign rounding. E[sign(gᵀuᵢ) sign(gᵀuⱼ)] = (2/π) arcsin(uᵢᵀuⱼ), the angle between the two vectors over π; then arcsin(X) ⪰ X for a PSD correlation matrix X.
Angle? Yes. **Shares an identity with an excluded item:** it is the same identity as Van Vleck and Goemans–Williamson.

**12. Grothendieck's constant, Krivine's bound, cut-norm approximation.** *Functional analysis / algorithms.*
π/2 ≤ K_G^ℝ ≤ π/(2 ln(1+√2)) = 1.78221 (Krivine 1979). Equivalently 1/K_G ≥ (2/π) ln(1+√2) ≈ 0.56, the ratio used by Alon & Naor (SIAM J. Comput. 35 (2006) 787) for approximating the cut norm.
Source: Wikipedia, "Grothendieck inequality"; Krivine, Adv. Math. 31 (1979) 16–30. (checked for the bounds; the 0.56 ratio and Krivine's c from memory.)
π step: the same sign-rounding arcsine identity as entry 11. Krivine chooses c with sinh(cπ/2) = 1, so c = (2/π) sinh⁻¹(1) = (2/π) ln(1+√2).
Angle? Yes. **Shares an identity with an excluded item** (as entry 11). The π/2 lower bound is noted in the π/2 section.

**13. Kendall's τ (and Blomqvist's β) under bivariate normality: Greiner's relation.** *Statistics.*
τ = (2/π) arcsin ρ, with ρ the Pearson correlation. Blomqvist's medial β takes the same value for the normal copula; Spearman's is (6/π) arcsin(ρ/2), which is different.
Source: Lindskog, McNeil & Schmock, "Kendall's tau for elliptical distributions" (2003), https://staff.math.su.se/lindskog/KendallsTau.pdf; Greiner (1909), Kruskal (1958); Wikipedia, "Kendall rank correlation coefficient" ("Greiner's equality"). (checked.)
π step: Sheppard's quadrant probability P(X>0, Y>0) = ¼ + arcsin(ρ)/(2π). After whitening, the probability is the opening angle of a wedge over 2π. τ uses pair differences, which are again bivariate normal with the same ρ.
Angle? Yes. **Shares an identity with an excluded item:** the same arcsine identity as Van Vleck's one-bit correlation.

### Geometry and mechanics

**14. Centroid of a semicircular arc (wire).** *Statics / geometry.*
ȳ = 2r/π from the diameter; a quarter-circle arc has both coordinates 2r/π. By Pappus, 2π·(2r/π)·πr = 4πr² gives the sphere. The same integral gives the field at the centre of a uniformly charged semicircular rod, E = 2kQ/(πR²) (textbook exercise; from memory).
Source: Wikipedia, "List of centroids"; Mathalino; Beer & Johnston, *Vector Mechanics for Engineers: Statics*. (checked in the first two.)
π step: ȳ = ∫₀^π r sin θ · r dθ / (πr) = 2r²/(πr). The numerator integrates sin θ over a half turn; the denominator is the arc length πr.
Angle? Yes. **Shares an integral with an excluded item:** mean of sin over a half-turn.

**15. Mean distance between two random points on a circle.** *Geometric probability.*
s̄ = 4r/π, from chord s(θ) = 2r sin(θ/2) with θ uniform on [0, π].
Source: Weisstein, "Circle Line Picking", MathWorld: "s̄ = ∫₀^π s(θ)dθ / ∫₀^π dθ = 4/π". (checked.)
π step: averaging over the central angle θ, uniform on [0, π].
Angle? Yes. **Shares an integral with an excluded item:** the same average of 2 sin(θ/2) as the rolling wheel's 4v/π.

**16. Period of a pendulum at finite amplitude.** *Classical mechanics.*
T = (2T₀/π)K(k), with k = sin(θ₀/2) and T₀ = 2π√(ℓ/g). Near the top, Cromer's formula is T ≈ (2/π)T₀ ln(4/a), with a = cos(θ₀/2).
Source: Wikipedia, "Pendulum (mechanics)", eq. 3; Cromer, Am. J. Phys. 63 (1995) 112. (checked.)
π step: the substitution sin u = sin(θ/2)/sin(θ₀/2) turns the quarter-period integral into K(k) = ∫₀^{π/2} du/√(1 − k² sin²u). At small amplitude K = π/2, so the 2/π normalises T to T₀.
Angle? Yes.

### Statistical mechanics, condensed matter, quantum

**17. Onsager's internal energy of the square-lattice Ising model.** *Statistical mechanics.*
U = −J coth(2βJ)[1 + (2/π)(2 tanh²(2βJ) − 1)∫₀^{π/2} dθ/√(1 − 4k(1+k)^{−2} sin²θ)], with k = 1/sinh²(2βJ) in the isotropic case. The bracketed integral is K. Near T_c, K's logarithm gives the specific heat c ≈ −(8K_c²/π) ln|1 − T/T_c| = −(2/π)(2J/kT_c)² ln|1 − T/T_c| per site (K_c = J/kT_c). The amplitude 8K²/π is the r = 1 limit of a formula in arXiv:1304.2108; writing it as (2/π)(2J/kT_c)² is my algebra.
Source: Wikipedia, "Square lattice Ising model"; Onsager, Phys. Rev. 65 (1944) 117. (checked for U.)
π step: the free energy is −βF = ½ ln 2 + (1/2π)∫₀^π ln[…cos 2θ…] dθ, an integral over the transfer matrix's Fourier modes. Differentiating gives the normalised complete elliptic integral (2/π)K.
Angle? Yes (Fourier-mode angle θ).

**18. Resistance between diagonal nodes of an infinite square grid.** *Electrical networks / lattice Green's functions.*
R(1,1) = (2/π)R for unit resistors R. Adjacent nodes give R/2, and the knight's move gives (4/π − ½)R (the last from memory).
Source: Cserti, "Application of the lattice Green's function for calculating the resistance of an infinite network of resistors", Am. J. Phys. 68 (2000) 896, eq. (29), arXiv:cond-mat/9909120. (checked.)
π step: R(l₁, l₂) = R∫∫_{BZ} (dx₁dx₂/(2π)²) (1 − cos(l₁x₁ + l₂x₂))/(2 − cos x₁ − cos x₂), the lattice Fourier integral over the Brillouin zone [−π, π]².
Angle? Yes (Fourier phase over the Brillouin zone).

**19. Average excluded area of randomly oriented sticks.** *Percolation / nanowire and nanotube networks.*
For two rectangles of length l and width w at angle θ, A_θ = (l² + w²)|sin θ| + 2lw(1 + |cos θ|). Averaged isotropically, A_r = 2lw(1 + 4/π²) + 2(l² + w²)/π. For sticks (w = 0) this is ⟨A_ex⟩ = (2/π)l², from ⟨|sin γ|⟩ = ⟨|cos γ|⟩ = 2/π.
Source: Li & Zhang, arXiv:1604.01315 (eq. 2 and erratum); Chatterjee et al., arXiv:2405.13728 ("for an isotropic orientational distribution in two dimensions ⟨|sin γ|⟩ = ⟨|cos γ|⟩ = 2/π"); Balberg et al., Phys. Rev. B 30 (1984) 3933. (checked.)
π step: averaging |sin γ| over a uniform angle γ ∈ [0, π].
Angle? Yes. **Shares an integral with an excluded item:** the same orientation average as Buffon's needle.

**20. Stoner–Wohlfarth remanence for easy axes random in a plane.** *Magnetism / recording media.*
M_r/M_s = ⟨cos ψ⟩ over ψ uniform on [0, π/2] = 2/π ≈ 0.637, against ½ for axes random in 3D.
Source: (from memory.) The 3D value ½ is checked (arXiv:0907.4417; arXiv:1111.6267). A paper treating 2D and 3D ensembles is "The remanence of a Stoner–Wohlfarth particle ensemble as a function of the demagnetisation process", J. Magn. Magn. Mater. (1998), https://www.sciencedirect.com/science/article/abs/pii/S0304885397011359; I did not see the 2D value there.
π step: after saturation, each particle relaxes to its easy axis and keeps M_s cos ψ; the 2/π is the average over the in-plane orientations.
Angle? Yes. **Shares an integral with an excluded item:** mean of cos over a uniform angle.

**21. Bell's illustrative local hidden-variable model.** *Quantum foundations.*
With λ uniform over directions, A(a, λ) = sign(a·λ) and B(b, λ) = −sign(b·λ), the correlation is P(a, b) = −1 + 2θ/π, with θ the angle between a and b; quantum mechanics gives −cos θ. Bell's earlier example gives ⟨σ·a⟩ = 1 − 2θ′/π.
Source: Bell, "On the Einstein Podolsky Rosen paradox", Physics 1 (1964) 195–200, eqs. (5) and (10), https://www.informationphilosopher.com/solutions/scientists/bell/Bell_On_EPR.pdf. (partly checked: the OCR shows eq. (5) "1 − 2θ′/π" clearly, and eq. (10) garbled but of the form −1 + (…)θ. The 2θ/π form of (10) is also in arXiv:2511.03679 as the "triangle" model.)
π step: the signs disagree on the fraction θ/π of directions λ, the lune between the two planes normal to a and b.
Angle? Yes.

### Optics and electromagnetism

**22. Kramers–Kronig relations, one-sided form.** *Optics / electromagnetism / condensed matter.*
χ₁(ω) = (2/π) P∫₀^∞ ω′χ₂(ω′)/(ω′² − ω²) dω′ and χ₂(ω) = −(2ω/π) P∫₀^∞ χ₁(ω′)/(ω′² − ω²) dω′, for χ = χ₁ + iχ₂ causal with χ(−ω) = χ*(ω).
Source: Wikipedia, "Kramers–Kronig relations"; Jackson, *Classical Electrodynamics* §7.10. (checked.)
π step: Cauchy's theorem on the upper half-plane. The small semicircular indentation round the pole at ω contributes −iπχ(ω) (half a residue), which gives the 1/π (Hilbert kernel 1/(πω)). The 2 comes from folding (−∞, ∞) onto [0, ∞) by parity.
Angle? Yes (the half-turn about the pole in the complex plane).

**23. Peak intensity of a Gaussian beam.** *Laser optics.*
I₀ = 2P₀/(πw₀²), with P₀ the total power and w₀ the 1/e² intensity radius. Related: the focused waist 2w₀′ ≈ (4/π)λF#, i.e. w₀′ ≈ (2/π)λF#.
Source: Wikipedia, "Gaussian beam"; Siegman, *Lasers* (1986). (checked.)
π step: P = ∫₀^∞ I₀e^{−2r²/w²} 2πr dr = I₀πw²/2. The 2π is the azimuthal integration; the radial Gaussian integral contributes no π.
Angle? Yes (azimuth).

**24. Binary π-phase grating, first-order efficiency.** *Diffractive optics.*
With duty cycle ½ and phase step π, the first-order amplitudes are a±₁ = ∓2i/π, the efficiency is η±₁ = (2/π)² = 40.5% per order (81% in both), and even orders vanish. Generally η_m = (4/(π²m²)) sin²(πmD) sin²(φ/2).
Source: arXiv:2410.06301 ("Versatile optical accordion lattices using binary phase transmission gratings"). (checked.)
π step: the Fourier coefficient of a ±1 square-wave transmission, i.e. entry 3.
Angle? Yes (Fourier).
Note: the N-level quantised blazed grating's [sin(π/N)/(π/N)]² gives the same (2/π)² at N = 2. That is sinc(½), the same value as the excluded pixel MTF.

**25. Capacitance of a thin conducting disc.** *Electrostatics.*
C = 8ε₀a = (2/π)·4πε₀a: 2/π of a sphere of the same radius, or "27.32…% greater than half that of a sphere".
Source: Kirchhoff, as cited in arXiv:2601.00858 ("C = 8ε_out b"); Phys-L list, Feb 2001 thread on disc capacitance, https://www.phys-l.org/archives/2001/02_2001/msg00292.html. (checked.)
π step (standard route, from memory): the disc is the flat limit of an oblate spheroid, with surface density σ(r) = Q/(2πa√(a² − r²)). The potential at the centre is V = (1/4πε₀)∫₀^a σ·2πr dr/r = (Q/4πε₀a)∫₀^a a dr/(a√(a² − r²)) = (Q/4πε₀a)(π/2), using ∫₀^a dr/√(a² − r²) = arcsin 1 = π/2.
Angle? **No** angle variable in the step where π enters (a radial integral whose value is arcsin 1).
Same boundary problem, not counted: Saito's disc-microelectrode current 4nFDCa (against 2πnFDCa for a hemisphere), the conduction shape factor of a disc, and Holm's constriction resistance. No source seen states the 2/π ratio for these.

**26. Microstrip width synthesis (Wheeler's wide-strip formula).** *Microwave engineering.*
w/h = (2/π)[(d − 1) − ln(2d − 1)] + ((εr − 1)/(πεr))[ln(d − 1) + 0.293 − 0.517/εr], with d a function of Z₀ and εr. Pozar's version is W/d = (2/π)[B − 1 − ln(2B − 1) + ((εr − 1)/(2εr))(ln(B − 1) + 0.39 − 0.61/εr)], B = 377π/(2Z₀√εr).
Source: Steer, *Microwave and RF Design II*, §3.6 "Microstrip Design Formulas" (LibreTexts), https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Microwave_and_RF_Design_II_-_Transmission_Lines_(Steer)/03:_Planar_Transmission_Lines/3.06:_Microstrip_Design_Formulas (checked); Pozar, *Microwave Engineering*, §3.8 (from memory); Wheeler, IEEE Trans. MTT 13 (1965) 172.
π step: the formula inverts Wheeler's wide-strip impedance, which came from a conformal-mapping (Schwarz–Christoffel) analysis of the strip and its fringing field. **The exact step was not seen.**
Angle? Not determined.

### Acoustics

**27. Radiation reactance of a baffled piston; flanged end correction.** *Acoustics.*
Z_m = ρcπa²[R₁(2ka) − iX₁(2ka)], X₁(2ka) = 2H₁(2ka)/(2ka). For small ka, X₁ ≈ 8ka/(3π), which as a mass load is the flanged-pipe end correction 8a/(3π) ≈ 0.85a. For large ka, X₁ ≈ 2/(πka).
Source: Aarts & Janssen (2003), eqs. (2)–(9) (as entry 10); Rayleigh, *Theory of Sound* §302. (checked.)
π step: Rayleigh's fourfold Helmholtz integral over the piston face gives H₁. Small ka uses the first term of H₁'s series (2/π)(z²/3); large ka uses its constant 2/π (entry 10).
Angle? As entry 10.

### Solid mechanics, contact, fracture, geophysics

**28. Stress intensity factor of a penny-shaped crack.** *Fracture mechanics.*
K_I = (2/π)σ√(πa) = 2σ√(a/π), for a circular crack of radius a under remote tension σ.
Source: Wikipedia, "Stress intensity factor" (penny-shaped crack); Sneddon, Proc. R. Soc. A 187 (1946) 229; Tada, Paris & Irwin, *The Stress Analysis of Cracks Handbook*. (checked.)
π step, by two routes. (a) Sneddon reduces the problem to dual integral equations and then to an Abel integral equation, whose inversion carries a 2/π. The crack opening is u = (4(1−ν²)σ/(πE))√(a² − r²). (b) Irwin's embedded elliptical crack has K = σ√(πb)/Φ, with Φ = E(k) = ∫₀^{π/2}√(1 − k² sin²φ) dφ; for a circle Φ = π/2. (Both from memory.)
Angle? **No** by route (a) (Abel inversion, no angle variable); yes by route (b) (the ellipse parameter φ).

**29. Sneddon's rigid conical indenter.** *Contact mechanics.*
The contact depth is ε = a tan θ, the total depth d = (π/2)ε, and the force F = (πE/(2(1−ν²)))a² tan θ = (2E/(π(1−ν²)))d²/tan θ. Here θ is the angle between the plane and the cone's side.
Source: Wikipedia, "Contact mechanics" (conical indenter); Sneddon, Int. J. Eng. Sci. 3 (1965) 47. (checked.)
π step: Sneddon's general depth formula is d = ∫₀¹ f′(x)/√(1 − x²) dx (in units of a). For a cone f′ is constant, so d = (π/2)a tan θ (from memory).
Angle? **No** angle variable in the π step (an Abel/arcsine integral). θ is a fixed geometric parameter and contributes no π.
π/2 reading: d = (π/2)ε, i.e. the contact edge lies at the fraction 2/π of the indenter depth.

**30. Oliver–Pharr geometric constant for a cone.** *Nanoindentation.*
h_c = h − ε·P/S, with ε = 2(π − 2)/π ≈ 0.727 for a cone; 0.75 for a paraboloid, 1 for a flat punch.
Source: Oliver & Pharr, J. Mater. Res. 7 (1992) 1564 (from memory); the value "conical indenter ε = 0.72" is in TU Wien lecture slides (Zelaya Lainez, 2021), https://vowi.fsinf.at/images/f/f7/TU_Wien-Mechanische_Eigenschaften_biolog_Gewebe_VO_%28Zelaya_Lainez%29_-_Vorlesungsfolien_3_2021WS.pdf. (partly checked.)
π step: from entry 29, the surface at the contact edge has sunk h − h_c = h(1 − 2/π). P ∝ h² gives P/S = h/2, so ε = 2(1 − 2/π) = 2(π − 2)/π.
Angle? **No** (inherits entry 29).

**31. Uniformly loaded circle on an elastic half-space: edge against centre deflection.** *Elasticity / geotechnical settlement.*
w(r) = (4(1−σ²)p₀a/(πE))E(r/a) for r ≤ a. The centre (E(0) = π/2) gives 2(1−σ²)p₀a/E, the edge (E(1) = 1) gives 4(1−σ²)p₀a/(πE), and the mean is 16(1−σ²)p₀a/(3πE). Edge/centre = 2/π; this is the 0.64 edge influence factor of a flexible circular footing in settlement tables (tables from memory).
Source: NPTEL course 103104047, lecture 6 "Pressure applied to a circular region", https://archive.nptel.ac.in/content/storage2/courses/103104047/lecture6/6_2.htm (following Johnson, *Contact Mechanics* §3.4; Love 1929). (checked; equations read from the page images.)
π step: the deflection at a point is an integral over the loaded circle in polar coordinates (s, φ) centred on that point, ∫₀^π 2√(a² − r² sin²φ) dφ. This equals 4a·E(r/a), and E(0) = π/2.
Angle? Yes (polar angle φ about the field point).
Related, not counted: the potential at the rim of a uniformly charged disc is 2/π of that at its centre (the same integral; from memory).

**32. Stress drop of a long fault that breaks the surface.** *Seismology.*
Δσ = Cμ(D̄/l): C = 2/π with l = W (fault width) for a long strike-slip fault reaching the surface; C = 4/π for a buried two-dimensional fault (Knopoff 1958); C = 7π/16 with l = R for a circular fault (Keylis-Borok 1959).
Source: Boore & Dunbar, "Effect of the free surface on calculated stress drops", Bull. Seism. Soc. Am. 67 (1977) 1661, eqs. (1)–(6), https://w.daveboore.com/pubs_online/1977bssa_free_surface_stress_drops.pdf; Kanamori & Anderson, BSSA 65 (1975) 1073; Chinnery (1969). (checked.)
π step (from memory): a 2D antiplane crack under uniform stress drop slips in an elliptical profile ∝ √(a² − x²). Its mean over the width is (π/4) times the peak, the area of a half-ellipse. A surface-breaking fault of width W is half of a buried crack of width 2W (mirror image), which halves 4/π to 2/π.
Angle? **No** angle variable (the area under the semi-elliptical slip profile).

### Engineering (civil, control, power, RF, electronics, machines)

**33. Fibre orientation factor for 2D-random fibres.** *Civil engineering (fibre-reinforced concrete).*
α = 2/π ≈ 0.637 for fibres random in a plane, 0.5 for 3D-isotropic, 1 for aligned. It is the mean projection of fibre length on the normal of a cracked section, and enters the number of fibres crossing a section, N = αV_f A/A_f.
Source: Frattura ed Integrità Strutturale no. 31 (Gruppo Italiano Frattura), https://gruppofrattura.it/pdf/fig/numero31/50 ("two-dimensional distribution, = 2/π, [18] and … three-dimensional … = 0.5") (checked); Soroushian & Lee, ACI Materials J. 87 (1990) 433 (from memory).
π step: the mean of |cos θ| for θ uniform in the plane.
Angle? Yes. **Shares an integral with an excluded item:** the mean of |cos| over an orientation.

**34. Describing function of an ideal relay.** *Control (nonlinear systems).*
N(A) = 4T/(πA), for a relay switching ±T driven by A sin ωt.
Source: How, MIT OCW 16.30 *Feedback Control Systems*, Topic 21 (2010), https://ocw.mit.edu/courses/16-30-feedback-control-systems-fall-2010/312399a26d8edca27ed6821d1ee7edd5_MIT16_30F10_lec21.pdf: "a₁ = (1/π)∫₀^{2π} y sin t dt = (2/π)∫₀^π T sin t dt = 4T/π". (checked.) Coulomb friction is the same nonlinearity; its equivalent viscous damping 4F/(πωX) follows (from memory).
π step: the first Fourier coefficient of the square-wave output.
Angle? Yes (Fourier phase).

**35. Describing function of a saturation.** *Control.*
N(A) = (2/π)[arcsin(T/A) + (T/A)√(1 − (T/A)²)] for A > T (unit slope, limit T), and N = 1 for A < T. The dead zone is 1 − N.
Source: How, MIT 16.30 Topic 21 (as above). (checked.)
π step: the first Fourier coefficient a₁ = (4/π)∫₀^{π/2} y(ψ) sin ψ dψ, split at ψ_T = arcsin(T/A).
Angle? Yes.

**36. Six-step (square-wave) inverter and the modulation index.** *Power electronics.*
The maximum fundamental phase voltage of a three-phase inverter, reached in six-step mode, is (2/π)V_DC. The modulation index is defined against it. Linear-range space-vector PWM reaches V_DC/√3, an index of π/(2√3) = 0.907 (noted in the π/2 section).
Source: US patent 9,919,615, "Voltage generation with high modulation indices in inverter drives" (checked); Holtz, "Pulsewidth modulation — a survey", Proc. IEEE 80 (1992) 1194 (from memory).
π step: the Fourier fundamental of the ±V_DC/2 phase-leg square wave, (4/π)(V_DC/2).
Angle? Yes (Fourier).
Related, not counted: the single-phase diode rectifier's input-current distortion factor 2√2/π = 0.90.

**37. Conversion gain of a single-balanced switching mixer.** *RF / communications.*
G_c = 2g_m/π (unbalanced: g_m/π). As voltage gain the active mixer is (2/π)g_mR_D.
Source: Sánchez-Sinencio, ECEN 665 lecture notes "Mixers II", Texas A&M, https://people.engr.tamu.edu/s-sanchez/665%20MixersII.pdf (checked); Razavi, *RF Microelectronics* (from memory, for the R_D form).
π step: the IF current is (I_BIAS + g_mv_RF) times the ±1 LO square wave (4/π)(cos ω_LOt + …). The product-to-sum identity halves the 4/π to give (2/π)cos(ω_LO − ω_RF)t.
Angle? Yes (Fourier phase).

**38. Class-B push-pull output stage.** *Analog electronics.*
Supply power P_S = (2/π)(V̂_o/R_L)V_CC, efficiency η = (π/4)(V̂_o/V_CC) (at most π/4 = 78.5%). Device dissipation P_D = (2/π)(V̂_o/R_L)V_CC − V̂_o²/(2R_L) is greatest at V̂_o = (2/π)V_CC.
Source: Allen, ECE 6412 notes "Push-pull" (Georgia Tech, 2002), https://pallen.ece.gatech.edu/Academic/ECE_6412/Spring_2003/L060-Push-Pull(2UP).pdf (checked for P_supply and η_max = π/4); the maximum-dissipation point is in Sedra & Smith, *Microelectronic Circuits* (from memory).
π step: each device conducts a half-wave rectified sine, and the mean supply current is (2/π)Î. Setting dP_D/dV̂ = 0 puts the 2/π into the optimum.
Angle? Yes (time phase ωt). **Shares an integral with an excluded item:** the rectified-sine average.

**39. Fundamental of the air-gap MMF of a full-pitch coil.** *Electric machines.*
F_ag1 = (4/π)(Ni/2) cos θ_a for a two-pole machine; in general 4NI/(nπ·2p) for the n-th harmonic with p pole pairs.
Source: Kirtley, MIT OCW 6.685 *Electric Machines*, chapter 5, https://ocw.mit.edu/courses/6-685-electric-machines-fall-2013/dfdada3721c1a7a26637d0df45ebb08c_MIT6_685F13_chapter5.pdf (checked); Fitzgerald, Kingsley & Umans, *Electric Machinery*, ch. 4 (from memory).
π step: the Fourier fundamental of the rectangular MMF wave (±Ni/2) along the gap's electrical angle. 4/π = 2·(2/π) by the half-range coefficient of entry 3.
Angle? Yes.

### Perception, imaging, biology, astrophysics

**40. Visibility of square-wave against sine-wave gratings.** *Perception / psychophysics.*
Over a wide range of spatial frequencies, threshold is set by the fundamental's amplitude. A square wave of contrast m has fundamental 4m/π, so its contrast sensitivity is 4/π ≈ 1.27 times the sine grating's (Fig. 3's prediction line "at 4/π").
Source: Campbell & Robson, "Application of Fourier analysis to the visibility of gratings", J. Physiol. 197 (1968) 551–566, https://www.cns.nyu.edu/~msl/courses/2223/Readings/campbellrobson68.pdf. (checked.)
π step: the Fourier fundamental of the square wave (entry 3).
Angle? Yes (Fourier phase).

**41. Coltman's relation between square-wave and sine-wave response.** *Imaging (optical testing).*
C(f) = (4/π)[M(f) − M(3f)/3 + M(5f)/5 − …]; inverted, M(f) = (π/4)[C(f) + C(3f)/3 − C(5f)/5 + …]. C is the bar-target (CTF) response and M the MTF.
Source: Coltman, "The specification of imaging properties by response to a sine wave input", J. Opt. Soc. Am. 44 (1954) 468. (from memory; the search did not reach the text.)
π step: the square-wave Fourier series (entry 3).
Angle? Yes.

**42. Canopy G-function and extinction coefficient for vertical leaves.** *Plant ecology / canopy radiative transfer.*
G(ψ) = (2/π) sin ψ, so the black-leaf extinction coefficient is K = G/cos ψ = (2/π) tan ψ, for solar zenith ψ. Horizontal leaves give K = 1 and spherical K = 1/(2 cos ψ).
Source: crt1d (Moon), leaf_angle.py: `def G_vertical(psi): return 2 / PI * np.sin(psi)`, https://raw.githubusercontent.com/zmoon/crt1d/master/crt1d/leaf_angle.py (checked); Campbell & Norman, *An Introduction to Environmental Biophysics* (1998), ch. 15 (from memory).
π step: a vertical leaf's projection toward the sun is |sin ψ cos φ|, averaged over leaf azimuth φ uniform.
Angle? Yes (leaf azimuth). **Shares an integral with an excluded item:** the mean of |cos|.

**43. Ideal-gas model of animal encounters (2D).** *Animal ecology.*
Mean relative speed of two animals at equal speed v in independent uniform directions is 4v/π. The encounter rate per individual is 8ρDv/π, with detection distance D and density ρ. Unequal speeds involve a complete elliptic integral.
Source: Hutchinson & Waser, "Use, misuse and extensions of 'ideal gas' models of animal encounter", Biol. Rev. 82 (2007) 335–359, preprint https://malagr.de/hutch/hutchpub/biolrev2_pre.pdf, Fig. 1 caption: "∫₀^π 2D·2vt sin(θ/2) dθ/π = 8Dvt/π". (checked.)
π step: the relative trajectory length 2vt sin(θ/2), averaged over the heading difference θ uniform on [0, π].
Angle? Yes. **Shares an integral with an excluded item:** the same average as the rolling wheel's 4v/π.

**44. Rotational broadening kernel of a star without limb darkening.** *Astrophysics (stellar spectroscopy).*
G(Δλ) = [2(1−ε)(1 − x²)^{1/2} + (πε/2)(1 − x²)]/[πΔλ_L(1 − ε/3)], with x = Δλ/Δλ_L and Δλ_L = (λ/c)v sin i. For ε = 0 this is G = (2/(πΔλ_L))√(1 − x²). PyAstronomy's coefficients are c₁ = 2(1−ε)/(πΔλ_L(1−ε/3)) and c₂ = ε/(2Δλ_L(1−ε/3)).
Source: Gray, *The Observation and Analysis of Stellar Photospheres*; PyAstronomy documentation, "Rotational broadening profile", https://pyastronomy.readthedocs.io/en/latest/modelSuiteDoc/rotBroadProfile.html; arXiv:astro-ph/0206066. (checked.)
π step: at Doppler offset x the flux comes from a strip of the stellar disc of length ∝ √(1 − x²). Normalising by the half-disc area ∫₋₁¹√(1 − x²) dx = π/2 gives 2/π.
Angle? **No** angle variable (the area of a half disc). **Shares a function with an excluded item:** the same function as the Wigner semicircle.

**45. Fabry–Pérot Airy linewidth.** *Optics / interferometry.*
Δν_Airy = Δν_FSR·(2/π) arcsin[(1 − √(R₁R₂))/(2(R₁R₂)^{1/4})], so the finesse is 𝓕 = (π/2)[arcsin(…)]^{−1} ≈ π√F/2 = π√R/(1 − R). Here F = 4R/(1 − R)² is the coefficient of finesse.
Source: Wikipedia, "Fabry–Pérot interferometer" (following Ismail et al., Opt. Express 24 (2016) 16366). (checked.)
π step: transmission is 1/(1 + F sin²(φ/2)) in the round-trip phase φ. The half-maximum points are at φ = ±2 arcsin(1/√F), and the free spectral range is a phase of 2π. The full width over the FSR is 4 arcsin(…)/(2π) = (2/π) arcsin(…).
Angle? Yes (round-trip phase).
The same page normalises each Lorentzian mode as (2/π)Δν_c/(Δν_c² + 4(ν − ν_q)²), a Cauchy density. I did not count that line shape.

---

## π/2 read the other way

The same relation written with π/2, where the source writes π/2. These are not counted above, except where noted.

| # | Name | Field | Form (as written) | 2/π reading | Source | π step / angle? |
|---|------|-------|-------------------|-------------|--------|-----------------|
| R1 | Line-intersect length estimate | Stereology; root biology | Newman: root length R = πNA/(2H); stereology L_A = (π/2)P_L | intersections per unit test line = (2/π)·length per area | Newman, J. Appl. Ecol. 3 (1966) 139 (checked snippet); Underwood, *Quantitative Stereology* (1970) for L_A (from memory). Tennant's grid factor 11/14 ≈ π/4 (checked snippet) | mean of \|cos θ\| over random line orientation; yes. Shares an integral with Buffon. |
| R2 | Line-intersect volume of downed wood | Forestry / fire ecology | V = (π²/8L)Σd² | (π/2) orientation factor × (π/4)d² cross-section | Van Wagner, For. Sci. 14 (1968) 20 (from memory) | orientation average (yes) and circle area (no angle) |
| R3 | Noise-equivalent bandwidth of a one-pole filter | Signal processing / electronics | B_N = (π/2)f_3dB | f_3dB = (2/π)B_N | IEEE TechNav "Noise bandwidth"; rfessentials.com (checked) | ∫₀^∞ df/(1 + (f/f_c)²) = f_c·arctan(∞); **no angle**. Same arctan as the excluded half-Cauchy. |
| R4 | f-sum rule | Condensed-matter optics | ∫₀^∞ ω Im ε(ω) dω = (π/2)ω_p²; ∫₀^∞ Re σ dω = πne²/(2m) | ω_p² = (2/π)∫ωε″dω | arXiv:1508.05606; arXiv:cond-mat/0408054 (checked) | high-frequency limit of the one-sided KK (entry 22) |
| R5 | Bode gain–phase relation | Control | phase ≈ (π/2)·d ln\|G\|/d ln ω; −20 dB/decade ↔ −90° | slope = (2/π)·phase | Bode, *Network Analysis and Feedback Amplifier Design* (1945) (from memory); TI SLUP070 for −20 dB/dec ↔ −90° (checked) | Hilbert-transform kernel, ∫ ln coth(\|u\|/2) du = π²/2; a phase relation |
| R6 | Virial mass estimator | Astrophysics (galaxy groups, clusters) | M_VT = (3πN/2G)Σv_z²/Σ_{i<j}(1/R_⊥,ij) | ⟨1/r⟩ = (2/π)⟨1/R_⊥⟩ | arXiv:astro-ph/0010587 citing Heisler, Tremaine & Bahcall, ApJ 298 (1985) 8 (prefactor checked); deprojection from memory | ⟨1/sin θ⟩ over isotropic orientations = π/2; yes |
| R7 | Space-vector PWM linear limit | Power electronics | m_max = π/(2√3) = 0.907 | V_DC/√3 ÷ (2/π)V_DC | US 9,919,615 (checked) | Fourier (entry 36); yes |
| R8 | Simple/complex cell F1/F0 | Neuroscience (V1) | a half-wave rectified sinusoid has F1/F0 = π/2 (F0 = 1/π, F1 = ½); criterion F1/F0 > 1 | F0/F1 = 2/π | Skottun et al., Vision Res. 31 (1991) 1079: criterion checked via PMC citations; the π/2 value is arithmetic (from memory) | Fourier coefficients of a half-wave rectified sine; yes. Shares an integral with the excluded rectified sine. |
| R9 | Wagner's water-entry splash-up | Marine hydrodynamics (slamming) | wetted half-width c = (π/2)Vt cot β for a wedge of deadrise β | Wagner condition (2/π)∫₀^{π/2} f(c sin θ)dθ = Vt | Wagner, ZAMM 12 (1932) 193; Faltinsen, *Hydrodynamics of High-Speed Marine Vehicles* (2005) (from memory) | flat-plate potential √(c² − x²), Abel-type integral; substitution x = c sin θ |
| R10 | Spinon dispersion of the Heisenberg chain | Quantum magnetism | ε(k) = (π/2)J\|sin k\| (des Cloizeaux–Pearson) | linear spin-wave J\|sin k\| = (2/π)×exact | arXiv:cond-mat/0001147; arXiv:cond-mat/0505594 (checked) | Bethe-ansatz integral equation solved by Fourier transform in rapidity (from memory); no spatial angle in that step |
| R11 | Grothendieck's lower bound | Functional analysis | K_G ≥ π/2 | — | Wikipedia "Grothendieck inequality" (checked) | entry 12 |
| R12 | Sneddon cone depth | Contact mechanics | d = (π/2)ε | ε/d = 2/π | entry 29 | arcsine integral; no angle |
| R13 | Fabry–Pérot finesse | Optics | 𝓕 ≈ π√F/2 | √F = (2/π)𝓕 | entry 45 | round-trip phase |
| R14 | Miles' equation | Random vibration | x_rms = √((π/2)f_nQ·ASD) | — | Miles (1954) (from memory) | ∫\|H(f)\|²df of a lightly damped resonance; residue/arctan, no angle |
| R15 | Elliptic K at zero modulus | Special functions | K(0) = E(0) = π/2 | entries 9, 16, 28, 31 | — | — |

Two relations of the excluded items, read the other way, are noted and not counted. The variance of the sample median under normality is (π/2)σ²/n, the reciprocal of the excluded efficiency 2/π. The form factor of a sine, RMS/mean = π/(2√2) = 1.1107, is the calibration constant of average-responding meters and the reciprocal of the excluded rectified-sine mean over √2.

---

## √(2/π) (and √(π/2)), kept apart

| # | Name | Field | Form | Source | π step |
|---|------|-------|------|--------|--------|
| Q1 | Half-normal mean; mean absolute deviation of a normal; Geary's ratio | Statistics | E\|X\| = σ√(2/π) = 0.7979σ; Var\|X\| = σ²(1 − 2/π) | Wikipedia, "Half-normal distribution" (checked) | normal density's constant 1/√(2π); **no angle in the step** (Gaussian integral). The squared form is the excluded (E\|Z\|)². |
| Q2 | 1D random walk displacement | Probability | lim E\|Sₙ\|/√n = √(2/π) | Wikipedia "Random walk", citing MathWorld (checked) | CLT, then Q1 |
| Q3 | Real eigenvalues of a real Ginibre matrix | Random matrices | E(N_ℝ) ~ √(2n/π) | Edelman, Kostlan & Shub, J. AMS 7 (1994) 247 (checked) | from their density of a real eigenvalue (Gaussian ensemble), details not seen |
| Q4 | Symmetric Fourier sine/cosine transforms | Analysis | f̂_s = √(2/π)∫₀^∞ f sin dt | Wikipedia "Sine and cosine transforms" (checked) | Fourier inversion (phase) |
| Q5 | GELU activation, tanh form | Machine learning | 0.5x(1 + tanh[√(2/π)(x + 0.044715x³)]) | Hendrycks & Gimpel, arXiv:1606.08415 (checked) | matches the slope of Φ at 0, 2φ(0) = √(2/π): Gaussian constant |
| Q6 | Wilson statistics, centric | Crystallography | ⟨\|E\|⟩ = √(2/π) = 0.798 (acentric √π/2 = 0.886); ⟨\|E\|⟩² = 0.637 vs 0.785 | CCP4 "Basic Maths for Protein Crystallographers" (checked snippet) | centric E is Gaussian: P(\|E\|) = √(2/π)e^{−E²/2} |
| Q7 | Cost of dichotomising at the median | Psychometrics | Corr(X, X_d) = √(2/π) ≈ 0.80; Corr² = 2/π (loses about 36% of r²) | Springer, Stat. Papers, doi:10.1007/s00362-023-01521-1, citing Cohen, Appl. Psych. Meas. 7 (1983) 249 and MacCallum et al. (2002) (checked) | as Q1; the squared form is the excluded (E\|Z\|)² |
| Q8 | MRI background noise | Medical imaging | Rayleigh mean = σ√(π/2), so σ = mean/1.253 | Stanford Rad229 lecture 7A (checked); Henkelman (1985); Gudbjartsson & Patz (1995) | Rayleigh mean, Gaussian in 2D (polar integral) |
| Q9 | Half-normal detection function | Ecology (distance sampling) | effective strip half-width μ = σ√(π/2); f(0) = √(2/π)/σ | Buckland et al., *Introduction to Distance Sampling* (2001) (from memory) | Gaussian integral; no angle |
| Q10 | Maxwell–Boltzmann mean speed | Kinetic theory | v̄ = (2/√π)v_p = √(8kT/(πm)) = 2√(2/π)√(kT/m) | Wikipedia "Maxwell–Boltzmann distribution" (checked) | Gaussian integrals over 3D velocity (solid angle 4π) |
| Q11 | Spherical Bessel functions | Special functions / scattering | jₙ(x) = √(π/(2x)) J_{n+½}(x) | Wikipedia "Bessel function" (checked) | Γ(½) = √π in half-integer orders |
| Q12 | Brownian maximum; one-bit compressed sensing; at-the-money straddle | Probability; signal processing; finance | E max_{s≤t} B_s = √(2t/π); E[sign(⟨a,x⟩)a] = √(2/π)x (Plan & Vershynin); straddle ≈ √(2/π)σ√T S | (from memory) | reflection principle, then Q1; Gaussian constant |

---

## Near-misses: adjacent to excluded items, not counted

- **sinc(½) = 2/π, the excluded pixel MTF's value.** The rectangular window's DFT scalloping loss (−3.92 dB), the zero-order-hold droop at Nyquist, and the N = 2 case of quantised-grating efficiency [sin(π/N)/(π/N)]².
- **The excluded rectified-sine average, in other fields.** Mean speed of simple harmonic motion (2/π)v_max, and the mean/peak piston speed of an infinite connecting rod. Half-sine daily irradiance (daily total = (2/π)·peak·day length; no source seen). Average EMF of a generator coil (2/π)E₀. A phase-sensitive detector with a square-wave reference ((2/π)V cos φ). Coherent gain 0.64 of the sine window (Harris 1978). Average-responding meters. Thyristor rectifier (2V_m/π) cos α.
- **The Cauchy density (as the excluded half-Cauchy).** A Lorentzian of FWHM Γ has peak height 2/(πΓ). The Fabry–Pérot mode line shape is (2/π)Δν/(Δν² + 4(ν − ν_q)²) (checked in Wikipedia "Fabry–Pérot interferometer").
- **Checked and set aside because no source writes or derives a 2/π.** The elliptic-wing circulation Γ₀ = 4L/(ρV∞bπ) is a π/4 (MIT 16.01 F7 notes). Kirchhoff's slot contraction π/(π+2) = 1/(1 + 2/π) has no source seen deriving it with a 2/π. The disc microelectrode's 4nFDCa has no π.
