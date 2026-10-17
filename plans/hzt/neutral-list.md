# Occurrences of the Cauchy law and its kin

Gathered from the compiler's own knowledge of the standard literature; no web searches were run and no file in this repository was read. DOIs are given from memory where the compiler is fairly confident of them and have not been checked online; entries without a DOI cite the book or paper only. Standard form used below: f(x) = (1/π)·γ/((x − x₀)² + γ²), centre x₀, half-width at half-maximum (scale) γ.

| ID | Name | Field | Formula as it appears | Source | Range in the source |
|---|---|---|---|---|---|
| H1 | Cauchy distribution (Poisson's and Cauchy's counterexample) | Probability theory | f(x) = 1/(π(1 + x²)); φ(t) = e^(−\|t\|) | Poisson 1824; Cauchy 1853; Stigler 1974, Biometrika 61:375, doi:10.1093/biomet/61.2.375 | Whole line |
| H2 | Ratio of two independent centred normals | Statistics | X/Y, X, Y ~ N(0, σ²): f(r) = 1/(π(1 + r²)); unequal σ: scale σ_X/σ_Y | Johnson, Kotz and Balakrishnan 1994, *Continuous Univariate Distributions* vol. 1, ch. 16 | Whole line |
| H3 | Student's t with one degree of freedom | Statistics | t₁: f(t) = Γ(1)/(√π Γ(½))·(1 + t²)^(−1) = 1/(π(1 + t²)) | Student 1908, Biometrika 6:1, doi:10.1093/biomet/6.1.1 | Whole line |
| H4 | The lighthouse problem | Bayesian data analysis | Flash at shore position x from lamp at (α, β), uniform angle: f(x) = β/(π(β² + (x − α)²)) | Gull 1988 (in *Maximum Entropy and Bayesian Methods*); Sivia and Skilling 2006, *Data Analysis*, §2.4 | Whole line (angles −π/2 to π/2) |
| H5 | Witch of Agnesi | Plane geometry | y = 8a³/(x² + 4a²) | Agnesi 1748, *Instituzioni analitiche*; Fermat and Grandi earlier; Stigler 1974 | Whole line (curve) |
| H6 | Poisson kernel of the upper half-plane | Potential theory, harmonic analysis | P_y(x) = (1/π)·y/(x² + y²) | Stein and Weiss 1971, *Introduction to Fourier Analysis on Euclidean Spaces*, ch. II | Whole boundary line |
| H7 | Symmetric stable law of index 1 | Probability theory | φ(t) = exp(iμt − γ\|t\|), density Cauchy(μ, γ) | Lévy 1925, *Calcul des probabilités*; Samorodnitsky and Taqqu 1994, *Stable Non-Gaussian Random Processes* | Whole line |
| H8 | Hitting point of planar Brownian motion on a line | Stochastic processes | BM from (0, y) first hits the x-axis at X: density (1/π)·y/(x² + y²) | Spitzer 1958, Trans. AMS 87:187, doi:10.1090/S0002-9947-1958-0104296-5; Durrett 1984, *Brownian Motion and Martingales in Analysis* | Whole line |
| H9 | Cauchy process by subordination | Stochastic processes | B(T_a), T_a the first passage of an independent BM to a: B(T_a) ~ Cauchy(0, a) | Bochner 1949; Feller 1971, *An Introduction to Probability Theory* vol. II, ch. VI | Whole line |
| H10 | Spitzer's winding law | Stochastic processes | 2θ(t)/ln t → standard Cauchy, θ(t) the winding angle of planar BM about the origin | Spitzer 1958, Trans. AMS 87:187 | Whole line (limit law) |
| H11 | Wrapped Cauchy (Poisson kernel of the disc) | Directional statistics | f(θ) = (1/2π)(1 − ρ²)/(1 + ρ² − 2ρ cos(θ − μ)) | Lévy 1939; Mardia and Jupp 2000, *Directional Statistics*, §3.5 | Whole circle |
| H12 | Stereographic image of the uniform circle | Geometry | Uniform φ on the circle, x = tan(φ/2) (projection from a point of the circle): x standard Cauchy | McCullagh 1996, Ann. Statist. 24:787, doi:10.1214/aos/1032894465 | Whole line |
| H13 | Möbius-closed family | Statistics | X ~ C(θ), θ = μ + iγ: (aX + b)/(cX + d) ~ C((aθ + b)/(cθ + d)) | McCullagh 1992, Biometrika 79:247; McCullagh 1996 | Whole line |
| H14 | Cauchy-distributed functions of Cauchy variates | Probability theory | X standard Cauchy: (X − 1/X)/2 and 2X/(1 − X²) also standard Cauchy | Pitman and Williams 1967, Ann. Math. Statist. 38:916, doi:10.1214/aoms/1177698885 | Whole line |
| H15 | Free stable law | Free probability | Cauchy is ⊞-stable; μ ⊞ Cauchy = μ ∗ Cauchy for every μ | Bercovici and Voiculescu 1993, Indiana Univ. Math. J. 42:733 | Whole line |
| H16 | Real zeros of Kostlan (SO(2)-invariant) random polynomials | Probability, algebraic geometry | Density of real zeros √n/(π(1 + x²)) | Edelman and Kostlan 1995, Bull. AMS 32:1, doi:10.1090/S0273-0979-1995-00571-9 | Whole line (exact at every n) |
| H17 | Natural (radiative) line width | Atomic spectroscopy, QED | I(ω) ∝ (Γ/2)/((ω − ω₀)² + (Γ/2)²), Γ = 1/τ | Weisskopf and Wigner 1930, Z. Phys. 63:54, doi:10.1007/BF01336768 | Near ω₀; the form fails far in the wings (ω ≪ ω₀ and ω ≫ ω₀) |
| H18 | Collision (pressure) broadening, impact limit | Spectroscopy | Lorentzian with half-width γ = 1/(2πτ_c) per frequency unit, τ_c mean time between collisions | Lorentz 1906; Van Vleck and Weisskopf 1945, Rev. Mod. Phys. 17:227, doi:10.1103/RevModPhys.17.227 | Core only; far wings go over to the quasistatic regime |
| H19 | Damping wings of strong absorption lines | Astrophysics | Voigt profile, Lorentzian wings ∝ γ/(π Δν²); damped Lyman-α column densities fitted on the wings | Mihalas 1978, *Stellar Atmospheres*; Wolfe, Gawiser and Prochaska 2005, ARA&A 43:861 | Fitted over the observed window |
| H20 | X-ray core-hole lifetime widths | X-ray spectroscopy | Lorentzian of FWHM Γ_K, Γ_L… tabulated per level | Krause and Oliver 1979, J. Phys. Chem. Ref. Data 8:329, doi:10.1063/1.555595 | Near the edge or line |
| H21 | Driven damped oscillator near resonance | Classical mechanics, optics | Absorbed power ∝ (γ/2)²/((ω − ω₀)² + (γ/2)²) for \|ω − ω₀\| ≪ ω₀ | Jackson 1999, *Classical Electrodynamics*, §7.5 (Lorentz model) | Near resonance (approximation) |
| H22 | Power-broadened two-level resonance | Quantum optics | Steady-state excited population ∝ (Ω²/4)/(Δ² + Ω²/2 + Γ²/4): Lorentzian in Δ of half-width √(Γ²/4 + Ω²/2) | Allen and Eberly 1975, *Optical Resonance and Two-Level Atoms* | Whole detuning axis (rotating-wave approximation) |
| H23 | NMR absorption line | Nuclear magnetic resonance | Bloch equations: v(Δω) ∝ T₂/(1 + T₂²Δω²) | Bloch 1946, Phys. Rev. 70:460, doi:10.1103/PhysRev.70.460 | Whole axis in the unsaturated linear limit |
| H24 | Motional narrowing | Magnetic resonance | Fast modulation: Lorentzian of half-width Δ²τ_c | Kubo 1954; Anderson 1954, J. Phys. Soc. Jpn. 9:316; Kubo and Toyabe 1967 | Core; the wings depart for \|Δω\| ≳ 1/τ_c |
| H25 | Dilute random dipoles: field distribution | Magnetic resonance, solid state | Uniform random positions in 3D, field ∝ 1/r³: Lorentzian of width ∝ concentration | Margenau 1935; Stoneham 1969, Rev. Mod. Phys. 41:82, doi:10.1103/RevModPhys.41.82 | Cut off at the nearest-neighbour distance in a lattice |
| H26 | Mössbauer line | Nuclear spectroscopy | Source and absorber each Lorentzian Γ; transmission dip Lorentzian of width 2Γ | Mössbauer 1958, Z. Phys. 151:124; Greenwood and Gibb 1971, *Mössbauer Spectroscopy* | Over the velocity sweep |
| H27 | Breit–Wigner resonance (non-relativistic) | Nuclear physics | σ(E) = (π/k²)·g·Γ_aΓ_b/((E − E_r)² + Γ²/4) | Breit and Wigner 1936, Phys. Rev. 49:519, doi:10.1103/PhysRev.49.519 | Near an isolated resonance |
| H28 | Relativistic Breit–Wigner (Z line shape) | Particle physics | σ(s) ∝ sΓ_ee Γ_ff/((s − M²)² + s²Γ²/M²); Lorentzian in √s near the pole | Particle Data Group, *Review of Particle Physics*, "Resonances"; ALEPH, DELPHI, L3, OPAL, SLD 2006, Phys. Rep. 427:257 | Near the pole; radiative corrections reshape it |
| H29 | Energy spectrum of a decaying state | Quantum mechanics | Exponential survival e^(−Γt/ħ) ↔ \|a(E)\|² ∝ 1/((E − E₀)² + Γ²/4) | Krylov and Fock 1947, Zh. Eksp. Teor. Fiz. 17:93; Khalfin 1958 | Cut off below threshold (the spectrum is bounded below), hence non-exponential late decay |
| H30 | Fano profile, large q | Atomic physics | (q + ε)²/(1 + ε²), ε = 2(E − E_r)/Γ; q → ∞ gives the Lorentzian 1/(1 + ε²) | Fano 1961, Phys. Rev. 124:1866, doi:10.1103/PhysRev.124.1866 | Near the resonance |
| H31 | Fabry–Pérot transmission peak | Optics | Airy T = 1/(1 + F sin²(δ/2)); near a peak ≈ 1/(1 + (F/4)(δ − 2πm)²) | Born and Wolf 1999, *Principles of Optics*, §7.6 | Periodic; Lorentzian only near each order |
| H32 | Schawlow–Townes laser linewidth | Laser physics | Phase diffusion: S(ν) ∝ (Δν/2)/((ν − ν₀)² + (Δν/2)²), Δν = πhν(δν_c)²/P | Schawlow and Townes 1958, Phys. Rev. 112:1940, doi:10.1103/PhysRev.112.1940 | Core; 1/f noise adds Gaussian parts |
| H33 | Spectrum of exponentially correlated noise | Signal processing | Random telegraph or OU noise, C(τ) = σ² e^(−\|τ\|/τ_c): S(ω) = 2σ²τ_c/(1 + ω²τ_c²) | Machlup 1954, J. Appl. Phys. 25:341, doi:10.1063/1.1721637; Wiener 1930; Khinchin 1934 | Whole frequency axis |
| H34 | First-order low-pass filter | Electrical engineering | \|H(f)\|² = 1/(1 + (f/f_c)²), f_c = 1/(2πRC) | Any circuits text, e.g. Oppenheim and Willsky 1997, *Signals and Systems*, §6.5 | Whole frequency axis |
| H35 | Drude conductivity | Condensed matter | Re σ(ω) = σ₀/(1 + ω²τ²) | Drude 1900, Ann. Phys. 306:566; Ashcroft and Mermin 1976, ch. 1 | Whole frequency axis (model) |
| H36 | Debye relaxation, real part | Dielectrics | ε′(ω) − ε_∞ = Δε/(1 + ω²τ²) | Debye 1929, *Polar Molecules* | Whole frequency axis (model) |
| H37 | Quasiparticle spectral function | Many-body physics | A(k, ω) = (1/π)·\|Im Σ\|/((ω − ε_k − Re Σ)² + (Im Σ)²) | Mahan 2000, *Many-Particle Physics*, ch. 2–3 | Near the quasiparticle pole |
| H38 | Lloyd model | Disordered systems | Site energies Cauchy(0, γ): averaged Green's function G(E) = G₀(E + iγ) exactly | Lloyd 1969, J. Phys. C 2:1717, doi:10.1088/0022-3719/2/10/303 | Whole line (the disorder law) |
| H39 | Virtual bound state (Friedel–Anderson) | Condensed matter | Impurity density of states ρ_d(ε) = (1/π)·Δ/((ε − ε_d)² + Δ²), Δ = πV²ρ₀ | Friedel 1956; Anderson 1961, Phys. Rev. 124:41, doi:10.1103/PhysRev.124.41 | Within the conduction band (wide-band limit) |
| H40 | Resonant tunnelling through a double barrier | Mesoscopic physics | T(E) = Γ_LΓ_R/((E − E_r)² + (Γ_L + Γ_R)²/4) | Büttiker 1988, IBM J. Res. Dev. 32:63, doi:10.1147/rd.321.0063; Stone and Lee 1985 | Near an isolated level |
| H41 | Lorentzian (Cauchy) ensemble of scattering matrices | Random matrix theory | Hamiltonians with P(H) ∝ det(λ² + (H − ε)²)^(−(βN+2−β)/2); for N = 1 the Cauchy density | Brouwer 1995, Phys. Rev. B 51:16878, doi:10.1103/PhysRevB.51.16878; Hua 1963 | Whole line |
| H42 | Ornstein–Zernike structure factor | Critical phenomena | S(q) = S(0)/(1 + q²ξ²) | Ornstein and Zernike 1914, Proc. KNAW 17:793; Stanley 1971, *Phase Transitions and Critical Phenomena* | Small q (qa ≪ 1); fails at the critical point (η ≠ 0) |
| H43 | Dynamic light scattering (Rayleigh line) | Soft matter | Diffusing particles: S(q, ω) ∝ Dq²/(ω² + (Dq²)²) | Berne and Pecora 1976, *Dynamic Light Scattering* | Whole frequency axis (diffusion limit) |
| H44 | Quasielastic neutron scattering | Neutron scattering | Translational diffusion: S(Q, ω) = (1/π)·ħDQ²/((ħω)² + (ħDQ²)²) | Bée 1988, *Quasielastic Neutron Scattering* | Small Q; convolved with the instrument resolution |
| H45 | Raman phonon line | Raman spectroscopy | Anharmonic decay: I(ω) ∝ Γ/((ω − ω₀)² + Γ²/4), Γ(T) | Balkanski, Wallis and Haro 1983, Phys. Rev. B 28:1928, doi:10.1103/PhysRevB.28.1928 | Near the line |
| H46 | Solar p-mode peaks | Helioseismology, asteroseismology | Stochastically excited damped oscillators: P(ν) = H/(1 + (2(ν − ν₀)/Γ)²) | Anderson, Duvall and Jefferies 1990, ApJ 364:699, doi:10.1086/169452 | Near each mode; neighbouring modes overlap |
| H47 | Optical tweezers power spectrum | Biophysics | Bead in a harmonic trap: P(f) = D/(2π²(f_c² + f²)), f_c = κ/(2πγ) | Berg-Sørensen and Flyvbjerg 2004, Rev. Sci. Instrum. 75:594, doi:10.1063/1.1645654 | Fitted below the Nyquist and hydrodynamic corrections |
| H48 | Ion-channel noise | Neurophysiology | Two-state channel: S(f) = S(0)/(1 + (f/f_c)²), f_c = (α + β)/2π | Neher and Stevens 1977, Annu. Rev. Biophys. Bioeng. 6:345; Conti and Wanke 1975 | Measured band; sums of Lorentzians for more states |
| H49 | Charge induced by a line charge above a grounded plane | Electrostatics | σ(x) = −(λ/π)·d/(x² + d²) | Jackson 1999, §2.2 (method of images); Smythe 1950, *Static and Dynamic Electricity* | Whole plane (ideal conductor) |
| H50 | Irradiance from an infinite line source | Illumination engineering | Line source at height h: E(x) ∝ h/(h² + x²) | Moon 1936, *The Scientific Basis of Illuminating Engineering* | Whole plane (infinite source idealization) |
| H51 | Aggregate interference in a planar Poisson network | Wireless communications | Amplitude loss r^(−b): symmetric α-stable with α = 2/b; b = 2 (power r^(−4)) Cauchy | Sousa and Silvester 1990, IEEE JSAC 8:762; Win, Pinto and Shepp 2009, Proc. IEEE 97:205, doi:10.1109/JPROC.2008.2008764 | Whole line if interferers come arbitrarily close; a guard zone truncates |
| H52 | Mandelbrot's stable Paretian prices | Finance | Log price changes stable with α < 2; Cauchy the α = 1 member (fitted α ≈ 1.7 for cotton) | Mandelbrot 1963, J. Business 36:394, doi:10.1086/294632; Fama 1965 | Whole line in the model; truncated Lévy in later work (Mantegna and Stanley 1994) |
| H53 | Lévy flight foraging, μ = 2 | Biology, ecology | Step lengths p(ℓ) ∝ ℓ^(−μ), optimum μ ≈ 2 (Cauchy-tailed, index 1) | Viswanathan et al. 1999, Nature 401:911, doi:10.1038/44831 | Cut off below at ℓ_min and in practice above |
| H54 | Cauchy and 2Dt seed dispersal kernels | Plant ecology | 2Dt: k(r) = (p/(πu))(1 + r²/u)^(−(p+1)); Cauchy-type at p = ½ in 2D; 1D Cauchy kernel in spread models | Clark et al. 1999, Ecology 80:1475; Shaw 1995 | Cut off by the landscape and sampling distance |
| H55 | Jeffreys's Cauchy prior on effect size | Bayesian statistics | δ ~ Cauchy(0, 1) in the one-sample test; Zellner–Siow g-prior | Jeffreys 1961, *Theory of Probability*, §5.2; Zellner and Siow 1980 | Whole line |
| H56 | Half-Cauchy prior on a scale | Bayesian statistics | p(σ) = 2A/(π(σ² + A²)), σ > 0 | Gelman 2006, Bayesian Analysis 1:515, doi:10.1214/06-BA117A | Half-line (folded) |
| H57 | Cauchy combination test (ACAT) | Statistical genetics, multiple testing | T = Σ wᵢ tan((0.5 − pᵢ)π), P ≈ ½ − arctan(T/Σwᵢ)/π | Liu and Xie 2020, JASA 115:393, doi:10.1080/01621459.2018.1554485 | Whole line; exact tail approximation as p → 0 |
| H58 | Cauchy (Lorentzian) robust loss | Robust statistics, computer vision | ρ(x) = (c²/2)·ln(1 + (x/c)²): the negative log Cauchy likelihood | Holland and Welsch 1977, Commun. Statist. A6:813; Black and Anandan 1996, CVIU 63:75 | Whole line |

## Derivation steps

**H1.** Defined directly as the density 1/(π(1 + x²)), the derivative of (1/π)arctan x + ½. Poisson used it to show the mean of many observations need not converge, and Cauchy showed its characteristic function is e^(−|t|), so the sample mean of n draws has e^(−n|t/n|) = e^(−|t|), the same law.

**H2.** Write the joint normal density of (X, Y), change variables to (R = X/Y, Y) with Jacobian |y|, and integrate y out: ∫|y| e^(−y²(1 + r²)/2σ²) dy/(2πσ²) = 1/(π(1 + r²)). The factor 1 + r² comes from the quadratic form x² + y² evaluated at x = ry.

**H3.** Student's density is proportional to (1 + t²/ν)^(−(ν+1)/2), obtained by integrating a normal over a chi-square-distributed precision. At ν = 1 the exponent is −1 and the normalizing constant Γ(1)/(√π Γ(½)) = 1/π, giving the Cauchy exactly.

**H4.** The lamp at (α, β) emits at angle θ uniform on (−π/2, π/2); the flash reaches the shore at x = α + β tan θ. Changing variables, dθ/dx = β/(β² + (x − α)²), so the density of x is that divided by π.

**H5.** Agnesi's construction: from a circle of diameter 2a tangent to the x-axis at the origin, a line from the origin cuts the circle and the line y = 2a; the point taking the x of the second intersection and the y of the first traces y = 8a³/(x² + 4a²). The square of the slope parameter gives the denominator.

**H6.** Solve Laplace's equation in y > 0 with boundary values f(x): Fourier transform in x gives û(ξ, y) = f̂(ξ) e^(−y|ξ|), the bounded solution. Inverting e^(−y|ξ|) gives (1/π)·y/(x² + y²). Equivalently it is Re(1/(πi)·1/(t − z)) of the Cauchy kernel.

**H7.** Stable laws have characteristic functions exp(−γ^α|t|^α(1 − iβ sgn t ω(t, α)) + iμt). Setting α = 1, β = 0 leaves exp(iμt − γ|t|), whose inverse Fourier transform is the Lorentzian of centre μ and half-width γ.

**H8.** The hitting density is the harmonic measure of the half-plane seen from (0, y): the probability is a harmonic function of the start with the boundary indicator as data, so it is the Poisson kernel of H6. Alternatively, by conformal invariance the exit angle is uniform, and x = y tan θ.

**H9.** The first passage time T_a of a BM to level a has Laplace transform e^(−a√(2λ)). Then E e^(itB(T_a)) = E e^(−t²T_a/2) = e^(−a|t|), the Cauchy characteristic function.

**H10.** Write the planar BM as e^(Z) with Z a complex BM run on a random clock (the skew-product); the winding is the imaginary part at the clock time, which at large t is controlled by the hitting time of level ½ ln t by the real part. Imaginary BM at an independent hitting time is Cauchy (H9), with the scale ½ ln t.

**H11.** Wrap Cauchy(μ, γ) around the circle: Σ_k f(θ + 2πk). By Poisson summation its Fourier coefficients are e^(−γ|n|) = ρ^|n|, and summing the geometric series gives (1 − ρ²)/(2π(1 + ρ² − 2ρ cos(θ − μ))), the Poisson kernel of the disc.

**H12.** A uniform point on the unit circle at angle φ, projected from the opposite point of the circle onto the tangent or diametral line, lands at x = tan(φ/2) (inscribed angle half the central). Then dφ/dx = 2/(1 + x²), and with φ uniform on (−π, π) the density is 1/(π(1 + x²)).

**H13.** Parametrize the law by θ = μ + iγ in the upper half-plane; its density is (1/π)Im(1/(x − θ̄)) and its characteristic structure transforms under real Möbius maps by the same map on θ. The proof writes the density as a Poisson kernel, which is conformally natural.

**H14.** With X = cot Θ, Θ uniform, (X − 1/X)/2 = cot 2Θ and 2Θ mod π is again uniform. Pitman and Williams characterize the rational functions with this property through inner functions of the half-plane.

**H15.** The Cauchy law's Cauchy transform is G(z) = 1/(z + iγ), so its R-transform is the constant −iγ; free convolution with it shifts the argument z → z + iγ, which is the same as classical convolution with the Poisson kernel.

**H16.** For p(x) = Σ aₖ √(n choose k) xᵏ with iid N(0, 1) aₖ, the Kac–Rice formula gives the expected density of real zeros as (1/π)√(∂ₓ∂ᵧ ln K(x, y))|_{y=x}, with K = (1 + xy)ⁿ. This evaluates to √n/(1 + x²) over π.

**H17.** Weisskopf–Wigner: the excited amplitude decays as e^(−Γt/2) in the pole approximation (coupling to a flat continuum, Markov limit). The emitted field's spectrum is the Fourier transform of a decaying exponential, |1/(i(ω − ω₀) + Γ/2)|², which is the Lorentzian.

**H18.** In the impact approximation each collision resets the phase of the radiating dipole, and the times between collisions are exponentially distributed with mean τ_c. The autocorrelation is e^(iω₀τ − |τ|/τ_c), and its Fourier transform is a Lorentzian of half-width 1/τ_c (angular).

**H19.** The Voigt profile is the convolution of the Gaussian Doppler core with the damping Lorentzian (H17, H18). Far from the centre the Gaussian contributes nothing and the profile becomes γ/(πΔν²); damped Lyman-α absorbers are fitted on these wings to get the column density.

**H20.** The core vacancy decays radiatively and by Auger processes with total rate Γ/ħ; as in H17 an exponential lifetime gives a Lorentzian energy width. The emission line's width is the sum of the widths of the initial and final vacancy levels.

**H21.** For x'' + γx' + ω₀²x = F cos ωt, the steady amplitude is F/(ω₀² − ω² − iγω). Near resonance ω₀² − ω² ≈ 2ω₀(ω₀ − ω), so the absorbed power ∝ 1/((ω − ω₀)² + γ²/4).

**H22.** The optical Bloch equations with Rabi frequency Ω, detuning Δ and decay Γ are solved for the steady state. The excited-state population is (Ω²/4)/(Δ² + Ω²/2 + Γ²/4), a Lorentzian in Δ whose width grows with intensity.

**H23.** The Bloch equations with transverse relaxation T₂ and a weak rotating field B₁ are solved in the rotating frame for the steady state. With saturation negligible (γ²B₁²T₁T₂ ≪ 1), the absorption component is ∝ T₂/(1 + T₂²(ω − ω₀)²).

**H24.** The resonance frequency fluctuates with variance Δ² and correlation time τ_c. The relaxation function is exp(−Δ²τ_c²(e^(−t/τ_c) − 1 + t/τ_c)); when Δτ_c ≪ 1 it is exp(−Δ²τ_c t) for t ≫ τ_c, whose Fourier transform is a Lorentzian of half-width Δ²τ_c.

**H25.** Each spin's resonance shift is a sum of dipolar fields ∝ (3cos²θ − 1)/r³ from randomly placed spins at low concentration. The log-characteristic function is n∫(1 − e^(itA(θ)/r³))d³r; the substitution u = 1/r³ makes it linear in |t|, giving a Lorentzian whose width is proportional to the concentration.

**H26.** The source emission and absorber cross-section are each lifetime-broadened Lorentzians (H17) of width Γ; scanning the Doppler velocity convolves them. A convolution of two Lorentzians is a Lorentzian with the widths added (characteristic functions e^(−Γ|t|/2) multiply), giving 2Γ in the thin-absorber limit.

**H27.** Near an isolated level the S-matrix element has a pole at E_r − iΓ/2: S ≈ 1 − iΓ/(E − E_r + iΓ/2). The reaction cross-section is proportional to |S_ab|², giving Γ_aΓ_b/((E − E_r)² + Γ²/4).

**H28.** The Z propagator 1/(s − M² + isΓ/M) (the self-energy's imaginary part) gives |propagator|². Writing s − M² ≈ 2M(√s − M) near the pole turns it into a Lorentzian in √s of half-width Γ/2.

**H29.** The survival amplitude is the Fourier transform of the energy density |a(E)|²; if it is assumed exponential, e^(−Γt/2ħ), the density is Lorentzian. Khalfin showed that because a real spectrum is bounded below, |a(E)|² cannot be exactly Lorentzian, and the decay departs from the exponential at very short and very long times.

**H30.** A discrete state coupled to a continuum, with a direct path to the same continuum, interferes; Fano's diagonalization gives the ratio of cross-sections (q + ε)²/(1 + ε²). As q → ∞ the direct path is negligible and the profile is 1/(1 + ε²) up to a factor.

**H31.** Summing the multiply reflected waves gives T = 1/(1 + F sin²(δ/2)), F = 4R/(1 − R)². Near δ = 2πm, sin²(δ/2) ≈ (δ − 2πm)²/4, so each peak is Lorentzian in the phase, with half-width 2/√F.

**H32.** Spontaneous emission into the lasing mode makes the phase a Wiener process with diffusion constant D. The field's autocorrelation e^(iω₀τ − D|τ|) Fourier transforms to a Lorentzian of FWHM D/π, which Schawlow and Townes computed from the cavity width and power.

**H33.** For a random telegraph signal with switching rate λ (or an Ornstein–Uhlenbeck process), the autocorrelation is σ²e^(−|τ|/τ_c). By Wiener–Khinchin the power spectrum is ∫σ²e^(−|τ|/τ_c)e^(−iωτ)dτ = 2σ²τ_c/(1 + ω²τ_c²).

**H34.** The RC voltage divider has H(jω) = 1/(1 + jωRC). Its squared magnitude is 1/(1 + ω²R²C²), which is the Lorentzian in frequency with half-power point at f_c.

**H35.** The electron momentum obeys dp/dt = −p/τ − eE. For E e^(−iωt), the steady response is σ(ω) = σ₀/(1 − iωτ), and the real part is σ₀/(1 + ω²τ²).

**H36.** Dipoles relax exponentially, φ(t) = e^(−t/τ), toward equilibrium. The susceptibility is the Fourier–Laplace transform, Δε/(1 + iωτ); its real part is Δε/(1 + ω²τ²) and the imaginary part Δεωτ/(1 + ω²τ²).

**H37.** The Green's function is 1/(ω − ε_k − Σ(k, ω)). Taking Σ as roughly constant near the pole, the spectral function −(1/π)Im G is a Lorentzian centred at ε_k + Re Σ with half-width |Im Σ|, the inverse lifetime.

**H38.** The Green's function G(E) for fixed site energies is analytic in each εᵢ in one half-plane; averaging over a Cauchy εᵢ is evaluating the integrand at εᵢ = iγ (contour closed around the Cauchy pole). So the disorder average equals the clean G at E + iγ, exactly.

**H39.** A localized d level at ε_d hybridizes with a flat conduction band through V. The d-electron self-energy is −iΔ with Δ = πV²ρ₀ in the wide-band limit, so G_dd = 1/(ε − ε_d + iΔ), and the density of states is the Lorentzian.

**H40.** An electron at energy E crosses two barriers with a quasibound level E_r between them, leaking at rates Γ_L, Γ_R. Summing multiple reflections (or a Breit–Wigner form for the level) gives T = Γ_LΓ_R/((E − E_r)² + Γ²/4), reaching 1 at E_r when Γ_L = Γ_R.

**H41.** Brouwer showed that the Lorentzian ensemble of Hamiltonians gives scattering matrices distributed by the circular ensemble (Poisson kernel). For N = 1 the density det(λ² + (H − ε)²)^(−1) is the Cauchy law of H6; the key property is that the Cauchy law is preserved by the Möbius map from H to S.

**H42.** Ornstein and Zernike split the total correlation into a short-range direct correlation c(r) and its chain. Expanding ĉ(q) ≈ ĉ(0) − Rq² for small q gives S(q) = 1/(1 − ρĉ(q)) ≈ S(0)/(1 + ξ²q²), the Lorentzian in q.

**H43.** Fick's law gives the intermediate scattering function F(q, t) = e^(−Dq²|t|). Its Fourier transform in time is the Lorentzian of half-width Dq² centred on the incident frequency.

**H44.** As in H43, a self-diffusing atom has I_s(Q, t) = e^(−DQ²|t|). The incoherent scattering law S(Q, ω) is its time Fourier transform, a Lorentzian of half-width ħDQ² in energy transfer.

**H45.** The optical phonon decays into two (or three) lower phonons at a rate Γ(T) set by anharmonic terms (Klemens). The finite lifetime makes the Raman response a damped oscillator near ω₀ and so a Lorentzian of FWHM Γ(T).

**H46.** Each mode is a damped oscillator driven by turbulent convection with a broadband force. The power spectrum of such a driven oscillator near its frequency is the Lorentzian H/(1 + (2(ν − ν₀)/Γ)²); the width gives the damping rate.

**H47.** The bead obeys the overdamped Langevin equation γẋ + κx = F_thermal with white force. Fourier transforming, |x̂(f)|² = (thermal force spectrum)/(γ²(2π)²(f_c² + f²)), the Lorentzian in f with corner f_c.

**H48.** A channel flips between closed and open with rates α and β, a two-state Markov process. Its current autocorrelation decays as e^(−(α+β)|τ|), and the spectrum is a Lorentzian with corner frequency (α + β)/2π (H33).

**H49.** Replace the plane by an image line charge −λ at depth −d. The normal field at the plane is from both lines: E_y = −(λ/πε₀)·d/(x² + d²), and σ = ε₀E_y gives the Lorentzian.

**H50.** For an infinite Lambertian line source at height h, integrating the point-source contributions along the line gives intensity falling as 1/r with r = √(h² + x²); the receiving plane's cosine factor is h/r. The product h/r² = h/(h² + x²).

**H51.** Interferers form a Poisson point process in the plane; the aggregate amplitude is a sum of r^(−b) terms with random signs or phases. Its characteristic function, by the Campbell formula, is exp(−c|t|^(2/b)), a symmetric stable law; b = 2 gives index 1, the Cauchy.

**H52.** Mandelbrot argued that price changes are sums of many contributions with infinite variance, so by the generalized central limit theorem their law is stable with α < 2. The Cauchy is the member with α = 1, β = 0; the estimates from cotton prices were α ≈ 1.7, so the Cauchy is a special case of the family, not the fitted law.

**H53.** For a searcher with randomly placed sparse targets, the rate of encounters per distance travelled is maximized over power-law step laws ℓ^(−μ). In the non-destructive case the optimum is μ = 2, the tail of a law of index 1 (Cauchy-like in tail, not in shape).

**H54.** The 2Dt kernel is a scale mixture: a Gaussian dispersal kernel whose variance is drawn from an inverse-gamma law across seeds or events, which gives a Student-t form in two dimensions. Small p gives fat Cauchy-type tails; the 1D Cauchy kernel is used in integrodifference spread models for the same reason.

**H55.** Jeffreys needed a prior on the standardized effect for which the Bayes factor behaves consistently at n = 1 and n → ∞. A Cauchy prior has these properties; Zellner and Siow obtained it as a normal prior δ | g ~ N(0, g) with g ~ inverse-gamma(½, ½), whose marginal is Cauchy.

**H56.** Gelman proposes the half-Cauchy as a weakly informative prior on a hierarchical standard deviation. It is the folded t₁, which arises as the marginal of a half-normal whose scale has an inverse-gamma mixing law; its density is flat near 0 and heavy in the tail.

**H57.** Each p-value pᵢ is uniform under the null, so tan((0.5 − pᵢ)π) is standard Cauchy (H4 with uniform angle). A weighted sum of standard Cauchy variables is Cauchy with scale Σwᵢ; Liu and Xie show the tail approximation stays accurate under arbitrary dependence of the tests.

**H58.** The negative log-likelihood of Cauchy errors is ln(1 + (x/c)²) up to constants. Its influence function 2x/(c² + x²) is bounded and redescending, which is why it is used as an M-estimator and as the Lorentzian error norm in optical flow.
