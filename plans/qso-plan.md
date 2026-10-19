# QSO: what the situated framing offers quantum mechanics

*16 October 2026 (Tom's local date). Tom, about 05:45: "i wonder if the situated observer framing offers any new ideas
for quantum?"; then, about 05:50, "yes, proceed" to Claude's three candidates and the offer of an exact plan. Physics,
so for `physics.md`, not OFS (R201). Follows QBT (`plans/qbt-plan.md`).*

## The claim, and what is already known

The situated view is not new in quantum mechanics. Relational quantum mechanics (Rovelli 1996), QBism (Fuchs and
Schack) and quantum reference frames (Bartlett, Rudolph and Spekkens 2007, *Rev. Mod. Phys.* 79, 555; Giacomini,
Castro-Ruiz and Brukner 2019) all make states relative to an observer or a frame. What this plan tests is whether three
pieces of our geometry read known quantum results cleanly. Nothing here is new physics; each result below is textbook or
in print, and the reading is ours.

**The bridge.** Amplitudes are unit relations (h = |⟨0|ψ⟩|, v = |⟨1|ψ⟩|); Born's rule carries them to frequencies.
For Gaussians the bridge is a width, an amount against a chosen reference width (the H). No other amounts.

**Not covered, and not claimed:** entanglement as a resource, Bell's theorem, contextuality, the measurement problem.

The three candidates:

1. **Without a shared frame, relations survive and amounts do not** (Jaynes's group, as Bartlett, Rudolph and
   Spekkens's twirl). A party who cannot fix a frame averages the state over the group (the twirl,
   ∫ dg U(g) ρ U(g)†). A Bloch vector is then lost, like V*/H without a unit; an overlap between two states survives,
   like v/h.
2. **Weak values as addresses, the expectation as the payload's mean.** A weak value A_w = ⟨f|A|i⟩/⟨f|i⟩ is a ratio of
   amplitudes. Its Born-weighted mean over a basis of final states is ⟨A⟩. Known beforehand (search results only, not
   the full text): Berry and Shukla (2010, *J. Phys. A* 43, 354024) find a "generalized Lorentzian" law for many
   eigenvalues and a superweak probability (|Re A_w| past the spectrum) up to 1 − 1/√2; Berry, Dennis, McRoberts and
   Shukla (2011, "Weak value distributions for spin 1/2", *J. Phys. A* 44, 205301) find 1/3 for spin ½ with both states
   uniform on the Bloch sphere.
3. **H is the reference width; the corner is where two Gaussians are most alike.** Two Gaussian packets of widths in
   ratio k overlap (squared) by 2k/(1 + k²) = sech(ln k): the duality relation's visibility 2hv (as a function of the
   amplitudes' log-ratio) and the Lorentz factor 1/γ (as a function of the Doppler factor, MOT run 3), one function.

## Predictions (written 16 Oct about 05:55, before any run)

Exact where possible (mpmath, 40 digits). Twirls are computed as finite averages that are exact for the degree
involved: over the phase group U(1), the average of e^{iα} over N ≥ 2 equally spaced phases; over SU(2) for one copy
or two copies, the 24-element single-qubit Clifford group, a unitary 2-design (so exact for ρ ↦ UρU† and for
ρ ↦ (U⊗U)ρ(U⊗U)†). Bloch vectors n = (⟨σx⟩, ⟨σy⟩, ⟨σz⟩).

**Idea 1, frames (F).**
- **F1. Without a phase reference.** Twirling a qubit over phases about z sends n to (0, 0, n_z): the visibility
  2hv = |n_⊥| goes to 0, the predictability h² − v² = n_z is kept (DUO's foil becomes a mixture at the same
  predictability). Checked at 20 random states (seed 5), each to 10⁻³⁰.
- **F2. Without an orientation reference.** Twirling one qubit over SU(2) sends every state to I/2 (n = 0).
- **F3. Two copies keep their relation.** For ψ₁ ⊗ ψ₂ twirled by U ⊗ U, the result is
  p·|Ψ⁻⟩⟨Ψ⁻| + ((1 − p)/3)·Π_triplet with p = (1 − n₁·n₂)/4, so it depends on the pair only through n₁·n₂, and the
  overlap |⟨ψ₁|ψ₂⟩|² = (1 + n₁·n₂)/2 = 1 − 2p is read back from it. Checked at 20 random pairs.
- **F4. The amount is lost, the reading kept.** Two pairs related by one rotation R (n₁, n₂ and Rn₁, Rn₂) give the same
  twirled state to 10⁻³⁰; pairs with different n₁·n₂ give twirled states differing by more than 10⁻³ in trace distance
  unless their n₁·n₂ agree within 10⁻³. The swap's expectation (the overlap) is unchanged by the twirl.
- **F5. Relative phase survives a common phase twirl.** For ψ(α₁) ⊗ ψ(α₂) twirled by e^{iασz/2} ⊗ e^{iασz/2}, each
  qubit's transverse Bloch component is 0, but ⟨σ₊ ⊗ σ₋⟩ keeps its value (sin 2θ₁ sin 2θ₂/4)·e^{i(α₁ − α₂)}, up to the
  sign convention of σ±: only the difference of the phases.

**Idea 2, weak values (W).** For a qubit and A = σz, with Bloch vectors n (pre-selected) and m (post-selected):
- **W1. The weak value in Bloch form.** A_w = (n_z + m_z + i·((m × ẑ)·n))/(1 + m·n) up to the sign of the imaginary
  part, checked against the matrices at 30 random pairs. Re A_w is unbounded as m → −n.
- **W2. The foot gives back the expectation.** Weighting by the post-selection probability (1 + m·n)/2 (Born's rule,
  the foot), the mean of Re A_w over m uniform on the sphere is exactly n_z (so the bounded payload's mean comes out of
  unbounded ratios).
- **W3. The weak value is a stereographic address.** With n = x̂ (pre-selected on the equator) and m at angle a from
  x̂ and turn b about it, Re A_w = tan(a/2)·sin b: a component of the stereographic chart of m from −n, tan(a/2) being the
  half-angle reading s = v/h of m against n. So, for m uniform:
  - the law of Re A_w is ½(1 + x²)^(−3/2) (a Student t with 2 degrees of freedom), its CDF ½(1 + sin(arctan x)): the
    sine of the address angle even on [−1, 1], Archimedes' even-in-height, not the even turn (which would give the
    Cauchy). It has a mean (0) and no variance; P(|Re A_w| > x) = 1 − x/√(1 + x²), so tail 1/x²;
  - the superweak probability P(|Re A_w| > 1) = 1 − 1/√2 = 0.2929, the boundary |Re A_w| = 1 at the address angle 45°,
    the corner;
  - weighted by the foot, the law is (3/4)(1 + x²)^(−5/2), tail 1/x⁴, variance finite (1/2), superweak probability
    1 − 5/(4√2) = 0.1161.
  Checked by quadrature to 10⁻³⁰ and by 10⁶ seeded samples to 3 standard errors.
- **W4. Both uniform.** With n and m both uniform and unweighted, P(|Re A_w| > 1) = 1/3 (Berry et al. 2011, known
  beforehand), by quadrature to 10⁻²⁰ and samples to 3 standard errors.

**Idea 3, widths (G).** Real Gaussians g_σ(x) = (2πσ²)^(−1/4)·exp(−x²/(4σ²)), σ the position spread.
- **G1.** |⟨g_σ₁|g_σ₂⟩|² = 2k/(1 + k²) = sech(ln k), k = σ₁/σ₂, by quadrature at 12 values of k, to 10⁻³⁰; the same at
  k and 1/k, greatest (1) at k = 1.
- **G2.** With h = σ₁/√(σ₁² + σ₂²), v = σ₂/√(σ₁² + σ₂²), it is 2hv = sin 2θ, the duality relation's visibility; and
  2hv = sech(ln(v/h)), as 1/γ = sech η with η = ln k the rapidity (MOT run 3).
- **G3. The squeezed vacuum.** The vacuum's overlap with the squeezed vacuum, from the Fock series
  ⟨2n|S(r)|0⟩ = (cosh r)^(−1/2)·(−tanh r)ⁿ·√((2n)!)/(2ⁿ n!), is normalised (the series sums to 1 to 10⁻³⁰ at r = 0.3, 1,
  2) and its squared overlap with |0⟩ is sech r: G1 at k = e^r, the squeezing a pan of one level of the width per r/ln 2.
- **G4. H is a zoom.** The overlap depends on σ₁ and σ₂ only through their ratio: multiplying both by any c (choosing a
  different reference width) changes nothing, to 10⁻³⁰.

*Killed if* an identity is off by more than its stated tolerance or a sampled value by more than 3 standard errors. A kill
in F, G, W1, W2 or W4 is my computation or my statement of known results; a kill in W3 is my derivation (written above
before running).

## Runs

### Run 1 (16 Oct about 06:05, `runs/qso/qso.py`, output in `runs/qso/run1.txt`; 1 min)

- **F1, F2, F3, F5 not killed** (to 4·10⁻⁴¹). Without a phase reference the visibility goes and the predictability
  stays; without an orientation one qubit is I/2; two copies twirled together are p·singlet + ((1 − p)/3)·triplet with
  p = (1 − n₁·n₂)/4, the overlap read back from them; a common phase twirl keeps only the phase difference.
- **F4 killed, by my set-up.** The rotated pair's twirled state equals the original's and the swap is kept (to 6·10⁻⁴¹).
  The "told apart" clause printed False because a `sed` edit I made before the run, meant to delete a dead condition,
  left `sep = False` under every pair whose n₁·n₂ differ, whatever their trace distance.
- **W1, W2 not killed.** The weak value's Bloch form holds (to 5·10⁻³⁹); the foot-weighted mean of Re A_w is n_z.
- **W3 not killed.** With n = x̂, P(|Re A_w| > 1) = 0.292893218813 = 1 − 1/√2, foot-weighted 0.116116523517 =
  1 − 5/(4√2), weighted variance ½, the tails as predicted (to 10⁻³⁵); 10⁶ samples 0.29254 ± 0.00045 and
  0.11593 ± 0.00026; P(|Re A_w| > 100) sampled 4.2·10⁻⁵ against 1/(2x²) = 5·10⁻⁵.
- **W4 not killed.** Both uniform: 1/3 by quadrature (to 10⁻²²), 0.33379 ± 0.00047 by samples.
- **G1–G4 not killed** (to 2·10⁻⁴¹). The squared overlap of two Gaussians is 2k/(1 + k²) = sech(ln k) = 2hv,
  unchanged when both widths are scaled; the squeezed vacuum's Fock series is normalised and gives sech r.

### Run 2, F4′ (prediction written 16 Oct about 06:08, before running)

The same claim as F4 with the condition repaired: for every two of the 20 pairs whose n₁·n₂ differ by more than 10⁻³,
the twirled states' trace distance is at least 10⁻³ (and, from the Werner form, equal to |Δ(n₁·n₂)|/3 to 10⁻³⁰).
*Killed if* any such pair falls below 10⁻³ or off |Δ(n₁·n₂)|/3 by more than 10⁻³⁰.

### Run 2 (16 Oct about 06:12, `runs/qso/qso.py`, output in `runs/qso/run2.txt`)

**F4′ killed, by my arithmetic.** Every two pairs whose n₁·n₂ differ by more than 10⁻³ are told apart (the least trace
distance 0.00116), but the distance is |Δ(n₁·n₂)|/4 at every pair (the ratio 0.25 to 20 digits), not the /3 I wrote. The
difference of two Werner states is Δp·(singlet) − (Δp/3)·(triplet), eigenvalues Δp once and −Δp/3 three times, so its
trace distance is (|Δp| + 3·|Δp|/3)/2 = |Δp| = |Δ(n₁·n₂)|/4; I had dropped the triplet's multiplicity.

### Run 3, F4″ (prediction written 16 Oct about 06:15, before running)

As F4′ with the distance |Δ(n₁·n₂)|/4. *Killed if* any pair whose n₁·n₂ differ by more than 10⁻³ has a trace distance
below 10⁻³ or off |Δ(n₁·n₂)|/4 by more than 10⁻³⁰.

### Run 3 (16 Oct about 06:17, `runs/qso/qso.py`, output in `runs/qso/run3.txt`)

**F4″ not killed.** Pairs whose n₁·n₂ differ are told apart at exactly |Δ(n₁·n₂)|/4; rotated pairs are not. Every other
check printed as in run 1. Nothing killed in run 3.

## What it shows

All of it is known quantum mechanics; what it shows is that three pieces of our geometry read it cleanly.

1. **Relations survive a missing frame; amounts do not.** A party who lacks the other's phase reference loses the
   visibility 2hv and keeps the predictability h² − v². One who lacks an orientation reference loses one qubit's
   Bloch vector altogether. Two copies twirled together keep exactly one number, n₁·n₂, the overlap: the twirled pair
   tells apart pairs with different overlaps and cannot tell apart pairs turned by a common rotation. This is
   Bartlett, Rudolph and Spekkens's twirl, and it is Jaynes's group in quantum dress: the measure on what cannot be
   fixed, averaged over. The Bloch vector is an amount (it needs an agreed frame, like V*/H needs a unit); the overlap
   is a reading (like v/h, it needs nothing).
2. **A weak value is a stereographic address, and the foot gives back the payload's mean.** Pre-selected on the
   equator, Re A_w = tan(a/2)·sin b: the half-angle reading s = v/h of the post-selected state against the
   pre-selected one, one component of the stereographic chart. Unbounded, but not Cauchy: the uniform sphere is even
   in height (Archimedes), not even in turn, so its law is ½(1 + x²)^(−3/2), with the superweak boundary |Re A_w| = 1 at
   the address angle 45°, the corner, and the superweak probability 1 − 1/√2 (the largest value Berry and Shukla report, for
   eigenvalues at the spectrum's two ends, seen in search results only; here one qubit pre-selected on the equator gives
   it; averaged over pre-selections, 1/3, Berry et al. 2011). Weighted by the
   foot (Born's post-selection probability) the tail falls from 1/x² to 1/x⁴, the variance becomes finite (½) and the
   mean is ⟨σz⟩ exactly: bounded means out of unbounded ratios, as in R289's density identity.
3. **H is the reference width.** Two Gaussian packets of widths in ratio k overlap by 2k/(1 + k²) = sech(ln k): the
   duality relation's visibility 2hv, the Lorentz factor's 1/γ and the squeezed vacuum's fidelity sech r are one
   function of a log-ratio, greatest at the corner (k = 1, equal widths, the coherent state) and the same at k and
   1/k. Scaling both widths, choosing a different reference width, changes nothing: H is a zoom.

What is new is at most the reading of point 2's corner and the even-in-height law as the address. None of this touches
entanglement as a resource, Bell's theorem, contextuality or the measurement problem.
