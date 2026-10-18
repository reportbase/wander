# REA: the 58 Cauchy occurrences classified under "address, not payload"

Classified from `plans/hzt/neutral-list.md` only (no other file of the repository read). The hypothesis was applied as
given, not argued: a Cauchy variable is a direction (the tangent or ratio a uniform turn lands at), never an amount; its
parameters z = m + iγ are amounts, the foot m and the height γ of the standpoint the turn is made from.

## Conventions

- **Layer.** 1 theorem; 2 measurement (a published number); 3p conclusion about the payload (what arrives, or what emits
  it); 3m conclusion about a method or instrument. Where several apply, the one carrying the source's conclusion is
  starred (*).
- **Turn.** What turns uniformly, about what, counted against what. "Explicit" means the source's own derivation names it;
  "hidden" means it is there in standard mathematics but the source does not use it; "none found" says why.
- **The damped phasor** (cited as DP): every Lorentzian that is the Fourier transform of e^(−γ·abs(t)), or the modulus
  squared of 1/(γ + iΔω), carries one turn: the phase lag φ of the response, tan φ = Δω/γ, which sweeps from −90° to
  +90° as the frequency (or energy) is swept through the line. The normalized offset Δω/γ is the tangent the turn lands
  at; the Lorentzian is (1/π)·dφ/dω (the frequency axis counted against the phase's uniform turn), and as a profile it is
  cos²φ (sin² of the phase shift for a Breit–Wigner). The amounts are the centre ω₀ (foot) and the half-width γ (height,
  a rate: 1/lifetime, a collision rate, a damping). The frequency itself is an amount on the writer's axis; what is
  Cauchy is the offset over the width.
- **Classes.** U unaffected (theorem or measurement only); R restated (the conclusion survives as a statement about the
  turn and the amounts, same predictions); D different prediction; F falls (the payload's nature inferred from the
  Cauchy form alone). F was given nowhere: no source here rests a conclusion about the payload on the form and nothing
  else.
- Confidence high / medium / low; "alt" the class I was torn toward.

## Table

| ID | Name | Claim (source's own terms) | Layer | Turn | Amount(s) | Class | Reason | Test (D/F) | Conf. | Alt |
|---|---|---|---|---|---|---|---|---|---|---|
| H1 | Cauchy distribution | The mean of n draws has the same law as one draw; averaging does not converge | 1* | Hidden: x = tan of a uniform angle (the density is the derivative of arctan); not used by Poisson or Cauchy | Centre 0, scale 1 | U | Pure theorem; no payload concluded | – | high | – |
| H2 | Ratio of centred normals | X/Y is Cauchy; unequal spreads give scale σ_X/σ_Y | 1* | Explicit in the algebra: the isotropic normal pair's direction is uniform (x² + y² the only invariant); X/Y = tan of it | σ_X/σ_Y (height, a ratio of amounts) | U | Theorem; the unequal-spread case is the stretch c moving the height | – | high | – |
| H3 | Student's t₁ | t with one degree of freedom is Cauchy | 1* | Hidden: t₁ = Z/abs(Z′), the ratio of two independent normals, so H2's uniform direction | Scale 1 | U | Theorem | – | high | – |
| H4 | Lighthouse | A uniform-angle lamp gives Cauchy flashes; the shore position α is found by likelihood or median, never by the mean of flashes | 1, 3m* | Explicit: the lamp's beam angle, uniform, about the lamp, counted by its own turning | α (foot), β (height: the lamp's distance off shore) | R | The hypothesis is this case; the method's conclusion (median/likelihood, not mean) is unchanged | – | high | U |
| H5 | Witch of Agnesi | A curve from a circle and a line through the origin | 1* | Explicit as a construction (a line turning about the origin cuts circle and line); a curve, not a density | a | U | Geometry only | – | high | – |
| H6 | Poisson kernel (half-plane) | Bounded harmonic extension of boundary data | 1* | Hidden in the source, standard: the harmonic measure seen from x + iy is the angle subtended, uniform from that point | x (foot), y (height of the interior point) | U | Theorem; z = x + iy is literally the standpoint | – | high | – |
| H7 | Symmetric stable, index 1 | The α = 1, β = 0 stable law is Cauchy(μ, γ) | 1* | None in the source (characteristic function only); a turn exists via H8 (Brownian landing) | μ, γ | U | Theorem | – | high | – |
| H8 | Planar BM hitting a line | The hitting point from (0, y) is Cauchy(0, y) | 1* | Explicit: by conformal invariance the exit direction is uniform, x = y·tan θ | y (height of the start), foot 0 | U | Theorem | – | high | – |
| H9 | Subordination B(T_a) | B at an independent first-passage time is Cauchy(0, a) | 1* | Hidden: (B, W) is a planar BM; B(T_a) is where it lands on the line W = a, so H8's uniform exit direction | a | U | Theorem | – | high | – |
| H10 | Spitzer's winding | 2θ(t)/ln t tends to a standard Cauchy | 1* | Hidden: in log-polar coordinates (skew product) the winding is the landing point of a planar BM on the level ½ ln t, H8 again; the Cauchy variable is an accumulated angle rescaled, a landing point, not a tangent of the winding | ½ ln t (height, a clock in levels) | U | Theorem | – | medium | – |
| H11 | Wrapped Cauchy | Poisson kernel of the disc; a model for directional data | 1* | Hidden: harmonic measure of the circle from an interior point ρe^(iμ), a uniform turn from that point (a Möbius image of the uniform circle) | μ, ρ (the interior standpoint) | U | Theorem; the horizon closes on the circle | – | high | – |
| H12 | Stereographic image | Uniform φ projected from a point of the circle lands Cauchy | 1* | Explicit: the inscribed angle φ/2, uniform | Foot 0, height 1 | U | Theorem; the hypothesis's own model | – | high | – |
| H13 | Möbius-closed family | Real Möbius maps act on θ = μ + iγ | 1* | Explicit through the Poisson-kernel form (PSL(2,R) acting on the standpoint) | μ, γ | U | Theorem | – | high | – |
| H14 | Pitman–Williams | (X − 1/X)/2 and 2X/(1 − X²) are again standard Cauchy | 1* | Explicit: X = cot Θ, the maps double the uniform angle | – | U | Theorem | – | high | – |
| H15 | Free stable law | Cauchy is ⊞-stable; free and classical convolution with it agree | 1* | Hidden: G(z) = 1/(z + iγ), convolving raises the standpoint by iγ (a shift of z) | γ | U | Theorem | – | medium | – |
| H16 | Kostlan zeros | Real zeros of the SO(2)-invariant ensemble have density √n/(π(1 + x²)) | 1* | Explicit: the SO(2) (Haar) invariance on the projective line [x : 1]; each zero's direction is uniform | n (count), foot 0, height 1 | U | Theorem | – | high | – |
| H17 | Natural line width | The excited state decays exponentially; the emitted line's width is its decay rate, Γ = 1/τ | 1, 2, 3p* | DP: the emitted field's phase lag against the driving frequency | ω₀, Γ/2 (a rate) | R | Lifetime from width is the height read as an amount; same numbers | – | high | U |
| H18 | Collision broadening | Collisions reset the dipole's phase; the width gives the collision rate | 3p*, 2 | DP: the dipole's phase advancing uniformly, cut by exponential waiting times | ω₀, 1/τ_c | R | Collision rate is the height; the far wings leave the form (quasistatic), an amount entering | – | high | – |
| H19 | Damping wings | Column densities of damped Lyman-α absorbers from the Lorentzian wings | 2, 3p* | DP for the damping part; the Gaussian core is an amount convolved in (Voigt), which breaks the family in the core and leaves the tails | N·γ (the wing strength), b (Doppler) | R | The column comes from the wings' strength, an amount; unchanged | – | medium | – |
| H20 | X-ray core-hole widths | Tabulated widths; a line's width the sum of its two levels' | 2* | DP (lifetime) | Γ_K, Γ_L … | U | A table of measurements; the sum rule is the heights adding (a relay) | – | high | R |
| H21 | Driven damped oscillator | The Lorentz model of matter: absorption near resonance | 1, 3p* | Explicit: the steady-state phase lag turns 0 to π through ω₀; tan φ = γω/(ω₀² − ω²) | ω₀, γ/2 | R | The model's predictions are the amounts' | – | high | U |
| H22 | Power broadening | The width grows with intensity as √(Γ²/4 + Ω²/2) | 1, 3p* | DP in the rotating frame: the Bloch vector's steady phase against the detuning | Δ offset over the height √(Γ²/4 + Ω²/2) | R | The height is an amount (decay and drive combined); same prediction | – | high | – |
| H23 | NMR line | Absorption Lorentzian; T₂ from the width | 2, 3p* | DP: the transverse magnetization's phase in the rotating frame | ω₀, 1/T₂ | R | T₂ is the height | – | high | – |
| H24 | Motional narrowing | Fast modulation narrows the line to Δ²τ_c | 3p* | DP once t ≫ τ_c (the relaxation function exponential); the core only, wings depart past 1/τ_c (an amount, τ_c, entering) | Δ², τ_c | R | Height Δ²τ_c; the wings' failure is where the amount enters | – | medium | – |
| H25 | Dilute dipoles | The field distribution is Lorentzian, width ∝ concentration | 1, 3p* | None found cleanly: the form comes from a uniform 3D density with a 1/r³ field (a Lévy measure dA/A², scale-invariant), not from a named turn; isotropic orientations set only the scale | Concentration (height), lattice cutoff | R | Width ∝ concentration survives as the height; the cutoff at the nearest neighbour is the amount breaking the tails | – | low | D |
| H26 | Mössbauer line | Source and absorber Lorentzians; the dip has width 2Γ | 2* | DP (lifetime), the two heights adding on convolution (a relay) | Γ, the Doppler velocity scale | U | Measurement and a convolution identity | – | high | R |
| H27 | Breit–Wigner | An isolated level is a quasibound state of width Γ (lifetime ħ/Γ), with partial widths | 1, 3p* | Explicit: the phase shift δ turns through π across the level, tan δ = (Γ/2)/(E_r − E); σ ∝ sin²δ | E_r, Γ/2, Γ_a, Γ_b | R | The resonance's widths are the heights | – | high | – |
| H28 | Z line shape | M_Z, Γ_Z, and the invisible width giving N_ν ≈ 3 | 2, 3p* | DP in √s: the propagator's phase turns through the pole | M (foot), Γ/2 (height), peak cross-section | R | N_ν comes from amounts (the peak height and the widths); radiative corrections are amounts reshaping it | – | high | – |
| H29 | Decaying state | Exponential decay and a Lorentzian energy spectrum; Khalfin: not exact, the spectrum bounded below | 1*, 3p | DP; the turn cannot reach its lower horizon because the energy is bounded below, so the tails and late decay depart | E₀, Γ/2, the threshold | R | Khalfin's departure is "the tails go last": the bound is an amount entering | – | medium | – |
| H30 | Fano profile | Discrete–continuum interference; the Lorentzian only as q → ∞ | 1, 3p* | DP for the discrete path; the direct path is an added amplitude (an amount) that moves the profile off the family | E_r, Γ, q | R | The asymmetry is the amount; the Lorentzian limit is the turn alone | – | medium | – |
| H31 | Fabry–Pérot peak | Transmission peaks, Lorentzian near each order | 1* | Explicit: the round-trip phase δ advances uniformly with frequency; on the circle (Airy), Lorentzian only near each order | F (finesse), order m | U | Optics theorem; the horizon closes on the circle | – | high | – |
| H32 | Schawlow–Townes | The laser line's width from phase diffusion; Δν from cavity width and power | 3p*, 1 | DP: the field's phase advancing at ω₀ while it diffuses, autocorrelation e^(−D·abs(τ)) | ν₀, D (a rate) | R | The width is the phase-diffusion rate; 1/f parts are amounts adding a Gaussian | – | high | – |
| H33 | Exponentially correlated noise | A random telegraph or OU process has a Lorentzian spectrum with corner 1/τ_c | 1* | DP: e^(iωτ) against e^(−abs(τ)/τ_c) | σ², τ_c | R | Wiener–Khinchin; the corner is the height | – | high | U |
| H34 | RC low-pass | Half-power at f_c = 1/(2πRC) | 1* | Explicit: arg H = −arctan(f/f_c); the response is cos²φ of that turn | f_c | U | Circuit theorem | – | high | – |
| H35 | Drude conductivity | Free carriers with relaxation time τ | 3p*, 2 | DP: the current's phase lag against the field's frequency | σ₀, 1/τ | R | τ is the height | – | high | – |
| H36 | Debye relaxation | Dipoles relax exponentially with time τ | 3p*, 2 | DP | Δε, 1/τ | R | τ is the height | – | high | – |
| H37 | Quasiparticle spectral function | A quasiparticle's lifetime is 1/abs(Im Σ); ARPES widths as scattering rates | 3p*, 2 | DP near the pole | ε_k + Re Σ (foot), abs(Im Σ) (height) | R | z = ε + Re Σ + i·Im Σ is the standpoint; same | – | high | – |
| H38 | Lloyd model | Averaging over Cauchy site energies gives G₀(E + iγ) exactly | 1* | Explicit: the average evaluates at the Cauchy's pole, i.e. raises the standpoint by iγ; the disorder chosen for this property | γ | U | A solvable model, a theorem | – | high | – |
| H39 | Virtual bound state | A localized level hybridized with a band has a Lorentzian density of width Δ = πV²ρ₀ | 3p*, 1 | DP in energy: G_dd's phase through ε_d | ε_d, Δ | R | Δ is the height | – | high | – |
| H40 | Resonant tunnelling | Transmission peaks at a quasibound level, unity when Γ_L = Γ_R | 1, 3p* | Explicit (Breit–Wigner form): the phase through the level | E_r, Γ_L, Γ_R | R | Same as H27 | – | high | – |
| H41 | Lorentzian ensemble | Cauchy Hamiltonians give circular-ensemble (Poisson-kernel) S-matrices | 1* | Explicit: S = e^(iφ) uniform on the circle (Haar), H its Cayley/stereographic image | λ, ε | U | Theorem; the hypothesis's case | – | high | – |
| H42 | Ornstein–Zernike | S(q) gives the correlation length ξ; ξ diverges at the critical point | 2, 3p* | DP in q (the 3D Fourier of e^(−r/ξ)/r: the phase e^(iqr) against the decay) | S(0), 1/ξ | R | ξ is the height; the failure at criticality (η ≠ 0) is where the form stops being a damped phasor | – | medium | – |
| H43 | Dynamic light scattering | Width Dq² gives D, and through Stokes–Einstein a particle size | 2, 3p* | DP in ω: F(q, t) = e^(−Dq²abs(t)) | Dq² (height), ω₀ (foot) | R | Size comes from D, an amount, plus a bridge (kT, viscosity); unchanged | – | high | – |
| H44 | Quasielastic neutrons | Width ħDQ² gives the self-diffusion constant | 2, 3p* | DP | ħDQ² | R | As H43 | – | high | – |
| H45 | Raman phonon line | Width Γ(T) is the phonon's anharmonic decay rate | 2, 3p* | DP | ω₀, Γ(T) | R | Γ is the height | – | high | – |
| H46 | Solar p-modes | Mode widths give damping rates of stochastically driven modes | 2, 3p* | DP | ν₀, Γ, H (peak height) | R | Damping from heights; peak asymmetry is an amount entering | – | high | – |
| H47 | Optical tweezers | The corner f_c and D calibrate trap stiffness and position | 2, 3m* | DP (overdamped: the bead's response phase) | f_c = κ/(2πγ), D | R | Calibration of amounts; unchanged | – | high | U |
| H48 | Ion-channel noise | The corner frequency gives the channel's kinetics (α + β); sums of Lorentzians for more states | 2, 3p* | DP (two-state Markov, exponential correlation) | (α + β), S(0) | R | Kinetics from the height; "one Lorentzian, two states" is Wiener–Khinchin, not the hypothesis | – | high | – |
| H49 | Image charge | The induced density on a grounded plane below a line charge | 1* | Explicit in substance: in 2D the line charge's field lines leave isotropically (uniform angle) and half the flux, with the image's, lands on the plane at x = d·tan θ | λ (total), d (height) | U | Electrostatics theorem | – | high | – |
| H50 | Line-source irradiance | E ∝ h/(h² + x²) | 1* | Explicit: the angle at the source line to the point, x = h·tan φ; E = cos²φ/h | h, source strength | U | Photometry theorem | – | high | – |
| H51 | Interference in a Poisson network | Aggregate interference is symmetric α-stable, α = 2/b; Cauchy at b = 2; guard zones truncate | 1, 3m* | Partly: random phases (uniform on the circle) give the symmetry; the index comes from the uniform planar density and r^(−b), a scale-invariant Lévy measure, no named turn | Density, power, b, guard radius | R | The outage results survive as the amounts' (density, guard zone); a guard zone is an amount breaking the tails | – | low | D |
| H52 | Mandelbrot's prices | Log price changes are stable Paretian with α < 2 (≈ 1.7); the Cauchy only a member of the family | 3p*, 2 | None found: price changes are amounts, and the conclusion uses α ≈ 1.7, not 1 | α, scale | U | The conclusion does not rest on the Cauchy; the hypothesis (no amount exactly Cauchy) agrees with α ≠ 1 and later truncation | – | medium | D |
| H53 | Lévy flight, μ = 2 | μ = 2 is the optimal search strategy for sparse revisitable targets; foragers should (and some do) move so | 1, 3p* | Not in the source. One the hypothesis can name: a straight leg at a uniform heading from a point a distance y off a straight edge (a boundary, a patch's side) has length y/cos θ, whose tail is exactly ℓ^(−2); μ = 2 is the law of isotropic legs ending on edges | y (distance to the edge), ℓ_min | D | The hypothesis reads μ = 2 as the geometry of a uniform heading stopped by straight boundaries (the landscape), not an evolved optimum of the walker | Movement tracks with habitat maps (Movebank, public): if μ ≈ 2 comes from the turn, the tail's scale follows the distance to the nearest edge and goes away in open habitat; the optimal-search reading predicts μ ≈ 2 regardless of edges. Public data; needs track–map pairing | low | F (the empirical Lévy claims rest on fitted tails, and some, e.g. the albatross, were revised for other reasons) |
| H54 | Seed dispersal kernels | Fat-tailed (Cauchy-type, 2Dt) kernels explain fast spread (Reid's paradox) | 2, 3p* | Source: a scale mixture of Gaussians (an amount mixed in). The hypothesis can name one: a seed leaving its release height h at a uniform angle and travelling straight lands h·tan θ off, the lighthouse | u (scale), p, release height | D | The hypothesis predicts a Cauchy kernel's scale set by the release height (the foot and height of the standpoint), the mixture reading by the spread of dispersal events | Seed-trap data with release heights (Clark et al. 1999 and later trap networks; partly public): Cauchy scale ∝ release height (in 1D) decides for the turn; scale uncorrelated with height, for the mixture | low | R |
| H55 | Jeffreys's Cauchy prior | A Cauchy prior on δ = μ/σ gives Bayes factors consistent at n = 1 and n → ∞ | 3m* | Hidden: δ is a ratio, the direction [μ : σ]; Cauchy(0, 1) is the uniform angle of that direction (Zellner–Siow's mixture is the normal pair of H2) | Foot 0, height 1 (the reference scale) | R | The prior is the uniform turn on [μ : σ]; the Bayes-factor properties are unchanged | – | medium | U |
| H56 | Half-Cauchy on a scale | A weakly informative prior for a hierarchical σ, flat near 0, heavy-tailed | 3m* | Hidden: σ/A = tan φ, φ uniform on [0, 90°): the direction [σ : A]; its median at σ = A, the corner | A (height) | R | σ is an amount, but the prior is a law on its ratio to A; Gelman's reasons (behaviour near 0, tails) stand | – | low | D (the hypothesis would prefer dσ/σ for an amount, which Gelman rejects as improper) |
| H57 | Cauchy combination test | tan((0.5 − p)π) summed with weights gives a valid P under arbitrary dependence | 1, 3m* | Explicit: each p uniform is a uniform angle (0.5 − p)π; the weighted sum a relay of standpoints, scale Σw | w_i (heights adding) | R | The test is the hypothesis's model; same calibration | – | high | – |
| H58 | Cauchy (Lorentzian) loss | A bounded, redescending M-estimator robust to outliers | 3m* | None needed: justified by its influence function, not by the residuals being Cauchy; it can be written as −2 ln cos φ of the residual's direction [x : c] | c | U | The method's claim does not rest on the residuals' nature | – | medium | R |

## Counts

| Class | Count | Entries |
|---|---|---|
| U | 25 | H1–H3, H5–H16, H20, H26, H31, H34, H38, H41, H49, H50, H52, H58 |
| R | 31 | H4, H17–H19, H21–H25, H27–H30, H32, H33, H35–H37, H39, H40, H42–H48, H51, H55–H57 |
| D | 2 | H53, H54 |
| F | 0 | – |

Low confidence: H25, H51, H53, H54, H56. The D's are both cases where an amount (a step length, a dispersal distance) is
modelled with a Cauchy tail; the hypothesis forces a turn to be named, and the one that can be named (a uniform heading
stopped by an edge, a uniform launch angle from a height) gives a testable dependence on the standpoint's height.

## Checked on the web

None. Every entry was classified from the catalogue's own text and the classifier's memory of the sources; no source was
opened.
