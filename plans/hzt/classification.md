# Classification of the neutral list (H1–H58)

Classifier's conventions, applied throughout:

1. **Lorentzians from exponential decay or a single pole** (Fourier transform of e^(−|t|/τ), |1/(x + iγ)|², a resolvent near a pole): Q1 = **no**. The swept variable (frequency, energy, detuning) is the ratio itself, not an angle; the free phase e^(iω₀t) advancing in time is not what produces the shape. Where a reader might argue the free phase, it is noted as the alternative.
2. **Stable-law / characteristic-function / Laplace-transform / contour derivations**: Q1 = **no**, even when an isotropic process sits underneath, unless the standard derivation itself passes through the angle (then hidden or yes).
3. **A density equal to dθ/dx, θ the angle seen from a point whose emission or field is isotropic** (Poisson kernel, line charge, line source): Q1 = **hidden** (isotropy / rotation invariance), even though the textbook route is images or Fourier; "no" is given as the alternative.
4. **Ratios of an isotropic, equal-spread normal pair** (including t₁ and Kostlan's SO(2) ensemble) and **Haar measure of U(1)/SO(2)**: Q1 = **hidden**.
5. **Q2 "held"** for a sampling distribution, ensemble or static field; **"not traversed"** for a pure identity or change of variables with no physical or statistical set behind it.
6. **Q3 "population"** for an ensemble of independent draws or members; **"source-or-system"** for a field or emitter whose isotropy is physical; **"none"** for pure mathematics.
7. Shapes (a curve, not a density) with a pencil of lines but no stated uniform measure: Q1 = **no**.

| ID | name | Q1 | what is even, or what produces the form | Q2 | Q3 | confidence | alternative |
|---|---|---|---|---|---|---|---|
| H1 | Cauchy distribution | no | Defined directly as a density; stability from the characteristic function e^(−\|t\|) | n/a | n/a | medium | yes / not traversed / none: the CDF is ½ + arctan(x)/π, i.e. x = tan of a uniform angle |
| H2 | Ratio of two centred normals | hidden | Isotropic equal-spread pair (X, Y): its angle is uniform; X/Y = cot of it, runs off as Y → 0 | held | population | high | — |
| H3 | Student's t₁ | hidden | t₁ = Z/\|Z′\|, an isotropic normal pair; the chi-square mixing hides the angle | held | population | medium | no: the derivation is a normal integrated over a chi-square precision |
| H4 | Lighthouse problem | yes | Emission angle θ uniform on (−π/2, π/2); amounts β (distance off shore) and x − α; tan θ → ∞ at the ends | traversed | source-or-system | medium | held / population: Gull's flashes are independent random azimuths, not a scan in order |
| H5 | Witch of Agnesi | no | A rational curve from a pencil of lines through the origin; denominator the slope squared; no measure on the pencil | n/a | n/a | medium | yes / traversed / none: the construction sweeps a line through the origin to horizontal |
| H6 | Poisson kernel, half-plane | hidden | Harmonic measure = (angle subtended from the point)/π, by rotation invariance of the Laplacian | not traversed | none | low | no: the standard derivation is the Fourier transform e^(−y\|ξ\|) |
| H7 | Symmetric stable, α = 1 | no | Characteristic function exp(iμt − γ\|t\|) inverted | n/a | n/a | high | — |
| H8 | Planar BM hitting a line | hidden | Exit angle uniform by rotation/conformal invariance of BM; x = y tan θ | held | population | medium | no: harmonic-measure (Poisson-kernel) route; or yes, since the alternative route states it |
| H9 | Cauchy process by subordination | no | Laplace transform of first passage, e^(−a\|t\|) | n/a | n/a | medium | hidden: it is H8 in disguise (2D BM hitting a line) |
| H10 | Spitzer's winding law | no | Skew-product and hitting-time limit (H9) | n/a | n/a | medium | hidden: rotation invariance of planar BM underlies the skew-product |
| H11 | Wrapped Cauchy | no | Wrapping plus Poisson summation, Fourier coefficients ρ^\|n\| | n/a | n/a | medium | hidden: it is the Möbius image of the uniform circle |
| H12 | Stereographic image of the uniform circle | yes | φ uniform on the circle; x = tan(φ/2) runs off at the projection point | not traversed | none | high | — |
| H13 | Möbius-closed family | no | Poisson-kernel covariance under real Möbius maps | n/a | n/a | medium | hidden: the family is the Möbius orbit of the uniform (Haar) circle |
| H14 | Cauchy functions of Cauchy variates | yes | X = cot Θ, Θ uniform; 2Θ mod π uniform again | not traversed | none | high | — |
| H15 | Free stable law | no | R-transform constant −iγ; subordination identity | n/a | n/a | high | — |
| H16 | Kostlan real zeros | hidden | SO(2)-invariance of the ensemble: zeros' directions on the projective line uniform (Haar), x = tan of them | held | population | medium | no: the standard route is Kac–Rice on K = (1 + xy)ⁿ |
| H17 | Natural line width | no | Exponential amplitude decay (pole), Fourier transform | n/a | n/a | high | hidden / traversed / source-or-system: free phase advancing in time |
| H18 | Collision broadening | no | Exponential waiting times between phase resets, Fourier transform | n/a | n/a | high | — |
| H19 | Damping wings | no | Lorentzian component of the Voigt convolution (H17, H18) | n/a | n/a | high | — |
| H20 | X-ray core-hole widths | no | Exponential lifetime (H17) | n/a | n/a | high | — |
| H21 | Driven damped oscillator | no | Pole of the response near resonance; ω₀² − ω² ≈ 2ω₀(ω₀ − ω) | n/a | n/a | high | yes / traversed / observer: the response phase runs −π/2 → π/2 as the drive frequency is swept (but not evenly) |
| H22 | Power-broadened two-level | no | Steady state of optical Bloch equations, rational in Δ | n/a | n/a | high | — |
| H23 | NMR absorption | no | Steady state of Bloch equations with T₂ decay | n/a | n/a | high | — |
| H24 | Motional narrowing | no | Exponential relaxation in the fast-modulation limit | n/a | n/a | high | — |
| H25 | Dilute random dipoles | no | Uniform positions in volume, 1/r³ field, Campbell formula gives index 1 | n/a | n/a | medium | hidden / held / population: uniform random placement |
| H26 | Mössbauer line | no | Convolution of two lifetime Lorentzians | n/a | n/a | high | — |
| H27 | Breit–Wigner | no | S-matrix pole at E_r − iΓ/2 | n/a | n/a | high | — |
| H28 | Relativistic Breit–Wigner | no | Propagator pole | n/a | n/a | high | — |
| H29 | Decaying-state spectrum | no | Fourier pair of the assumed exponential survival | n/a | n/a | high | — |
| H30 | Fano profile, large q | no | Discrete-continuum diagonalization; limit q → ∞ | n/a | n/a | high | — |
| H31 | Fabry–Pérot peak | no | Small-angle expansion of sin²(δ/2) in the Airy function | n/a | n/a | medium | yes / traversed / observer: the round-trip phase δ is advanced evenly by the frequency scan |
| H32 | Schawlow–Townes linewidth | no | Phase diffusion (Wiener process) gives exponential autocorrelation | n/a | n/a | high | — |
| H33 | Exponentially correlated noise | no | Wiener–Khinchin of e^(−\|τ\|/τ_c) | n/a | n/a | high | — |
| H34 | First-order low-pass | no | \|1/(1 + jωRC)\|², a single pole | n/a | n/a | high | yes / traversed / observer: the phase lag runs 0 → −π/2 as frequency is swept (not evenly) |
| H35 | Drude conductivity | no | Single relaxation pole σ₀/(1 − iωτ) | n/a | n/a | high | — |
| H36 | Debye relaxation | no | Exponential relaxation, single pole | n/a | n/a | high | — |
| H37 | Quasiparticle spectral function | no | Pole with constant self-energy | n/a | n/a | high | — |
| H38 | Lloyd model | no | Contour closed around the Cauchy pole (analyticity in a half-plane) | n/a | n/a | high | — |
| H39 | Virtual bound state | no | Constant self-energy −iΔ in the wide-band limit (pole) | n/a | n/a | high | — |
| H40 | Resonant tunnelling | no | Breit–Wigner pole of the quasibound level | n/a | n/a | high | — |
| H41 | Lorentzian ensemble of S-matrices | hidden | Haar measure of U(1) (circular ensemble) on S = e^(iφ); H a Möbius (tan) image of φ | held | population | medium | no: stated as a property of the Lorentzian ensemble under the map |
| H42 | Ornstein–Zernike | no | Small-q expansion of the direct correlation function | n/a | n/a | high | — |
| H43 | Dynamic light scattering | no | Fourier transform of e^(−Dq²\|t\|) | n/a | n/a | high | — |
| H44 | Quasielastic neutron scattering | no | Fourier transform of e^(−DQ²\|t\|) | n/a | n/a | high | — |
| H45 | Raman phonon line | no | Finite anharmonic lifetime, damped-oscillator pole | n/a | n/a | high | — |
| H46 | Solar p-mode peaks | no | Stochastically driven damped oscillator, pole | n/a | n/a | high | — |
| H47 | Optical tweezers spectrum | no | Overdamped Langevin, single pole | n/a | n/a | high | — |
| H48 | Ion-channel noise | no | Two-state Markov, exponential autocorrelation | n/a | n/a | high | — |
| H49 | Charge induced by a line charge | hidden | Isotropic field of a line charge: induced charge per dx = −(λ/π)·dθ/dx, θ the angle seen from the line | held | source-or-system | medium | no: the standard route is the method of images |
| H50 | Irradiance from a line source | hidden | Flux uniform in angle in the cross-section: E ∝ cos/r = dθ/dx | held | source-or-system | low | no: the standard route integrates point sources along the line |
| H51 | Planar Poisson interference | no | Campbell formula, stable index 2/b | n/a | n/a | high | hidden / held / population: uniform random interferers with random phases |
| H52 | Mandelbrot prices | no | Generalized CLT, stable family; Cauchy only a member | n/a | n/a | high | — |
| H53 | Lévy flight μ = 2 | no | Optimization over power-law step laws; tail only | n/a | n/a | high | — |
| H54 | 2Dt / Cauchy dispersal kernels | no | Scale mixture of Gaussians (inverse-gamma variance) | n/a | n/a | high | — |
| H55 | Jeffreys's Cauchy prior | no | Chosen for Bayes-factor consistency; normal/inverse-gamma mixture | n/a | n/a | medium | hidden: the mixture is a ratio of a normal to an independent normal's magnitude |
| H56 | Half-Cauchy prior | no | Chosen as weakly informative; half-normal scale mixture | n/a | n/a | high | — |
| H57 | Cauchy combination test | yes | Each p uniform under the null; tan((0.5 − p)π) is a uniform angle mapped through tan, running off as p → 0 or 1 | held | population | medium | not traversed / none: treated as a pure change of variables |
| H58 | Cauchy robust loss | no | Defined as the negative log-likelihood of Cauchy errors | n/a | n/a | high | — |

## Counts

- Q1: yes 4 (H4, H12, H14, H57); hidden 8 (H2, H3, H6, H8, H16, H41, H49, H50); no 46.
- Among the 12 yes or hidden, Q2: traversed 1 (H4); held 8 (H2, H3, H8, H16, H41, H49, H50, H57); not traversed 3 (H6, H12, H14).
- Among the 12 yes or hidden, Q3: observer 0; source-or-system 3 (H4, H49, H50); population 6 (H2, H3, H8, H16, H41, H57); none 3 (H6, H12, H14).
