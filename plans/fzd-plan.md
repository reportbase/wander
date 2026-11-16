# FZD: Fizeau's moving water as the boost's composition

16 Nov 2026. SPN R1060. Tom: "1 2 3", to "Fizeau's moving water as a check against real data" after PYK.

## The question

PYK found one rule for composing two readings, s ⊕ a = (s + a)/(1 − κsa), with κ = −1 for boosts (s a speed in units of
light's). Light in water moving at u has, in the water's own frame, speed c/n. Composed with the water's speed, the rule
alone says what a standpoint at rest reads for it. Fizeau (1851) and later Michelson and Morley (1886) and Zeeman
(1914–1915) measured how much of the water's speed the light picks up: the drag coefficient f in
w = c/n + f·u. This plan states f from the rule before looking up any measured number, and checks it against the
published ones.

This is known physics (Laue 1907 gave this derivation), so the test is one the reading could fail, not a new result.
It cannot discriminate between relativity and Fresnel's partial ether drag (1818), which predicts the same first-order f;
it can discriminate against Galilean addition (κ = 0), which predicts f = 1, and against no drag, f = 0.

## Predictions (committed before any published value is looked up; `runs/fzd/fzd.py`)

- **F1. The coefficient from the rule.** With s = 1/n and a = u/c, (s ⊕₋₁ a)·c = c/n + (1 − 1/n²)·u + O(u²/c),
  symbolically: the first-order drag is f₀ = 1 − 1/n², with no free number; Galilean composition gives f = 1. Exact.
- **F2. The second order is negligible.** At Fizeau's water speeds (a few m/s; I expect under 10 m/s) the next term is
  under 10⁻⁸ of the first. Exact.
- **F3. Dispersion is the Doppler factor's.** The light's frequency in the water's frame is shifted by the Doppler factor
  k (PYK K5), so n is taken at the shifted wavelength; to first order f = 1 − 1/n² − (λ/n)·dn/dλ (Lorentz's term). For
  water at the sodium D lines (n ≈ 1.333, dn/dλ from a published dispersion formula), the term lowers f by 1–3%. Exact
  given n(λ).
- **F4. Michelson and Morley 1886.** Their reported coefficient agrees with f₀ for water within 2 of their stated
  uncertainties, and is more than 10 of them from Galilean f = 1 and from f = 0.
- **F5. Fizeau 1851.** His reported value agrees with f₀ within his own stated uncertainty if he gives one; if he gives
  none, within 15% (the era's figure is rough). Recorded either way.
- **F6. Zeeman 1914–1915.** Where Zeeman reports measured against predicted shifts at several wavelengths, the prediction
  with F3's dispersion term fits his measurements better than f₀ without it (smaller summed squared difference over his
  stated wavelengths).

Kill conditions are each prediction's own. The published values go into the Runs section as found, with their source;
where only a secondary source can be reached, that is said and the item is marked secondary.

## Runs
