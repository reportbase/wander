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
**Run 1** (16 Nov, `runs/fzd/fzd.py`, output `runs/fzd/fzd-run1.txt`). 4 of 6 not killed; F2 and F3 killed by my own
estimates, their exact parts holding.

Sources, read as primary (not committed; sha256 of the files fetched):
- Fizeau 1851, *C. R. Acad. Sci.* 33, 349–355, the Académie's scan
  (academie-sciences.fr/pdf/dossiers/Fizeau/Fizeau_pdf/CR1851_p349.pdf, sha256 4ee44aa7…8b7202), p. 353: nineteen
  observations, double displacement 0.46 of a fringe at 7.069 m/s; full drag computed 0.92, Fresnel 0.40; no
  uncertainty stated.
- Michelson and Morley 1886, *Am. J. Sci.* 31, 377–386 (Wikisource transcription, read secondary to the journal): x = .434,
  "possible error" ±.02; Fresnel's (n² − 1)/n² = .437 with n² = 1.78; water at 8.72, 7.65, 5.67 m/s.
- Zeeman 1914, *Proc. KNAW* 17, 445–451 (dwc.knaw.nl PU00012688, sha256 44730082…da17f1c), the method; Zeeman 1915,
  *Proc. KNAW* 18 I, 398–408 (PU00012515, sha256 ee671b4f…49ad52), p. 403's table: shifts at 4500, 4580, 5461, 6440,
  6870 Å, computed with Fresnel's coefficient and with Lorentz's, and observed with probable errors (6440 one reading,
  no error, left out).
- Water's n(λ): Daimon and Masumura 2007, *Appl. Opt.* 46, 3811, 20.0 °C (refractiveindex.info database, CC0).

Results:
- F1 not killed: the first order of (1/n ⊕₋₁ u/c)·c is (1 − 1/n²)·u exactly; Galilean gives 1. The second-order
  coefficient is −(n² − 1)/n³.
- F2 killed by my bound: the second order is s·a = u/(nc) of the first, 1.4–2.2 × 10⁻⁸ at the speeds used (under 10⁻⁸
  only below 4 m/s). I guessed the size; it is still four orders below any fringe reading.
- F3 killed in its sign and size: composing with n taken at the Doppler-shifted wavelength gives Lorentz's term
  −(λ/n)·dn/dλ exactly (symbolic, not killed), but since dn/dλ < 0 the term **raises** f, by 3.1% at the D lines
  (0.4375 → 0.4513), where I wrote "lowers … by 1–3%". My slip in the sign, recorded as killed.
- F4 not killed: 0.434 ± 0.02 against f₀ = 0.4375 (0.18 of their error); 28 errors from Galilean 1 and 22 from no drag.
- F5 not killed, at its edge: Fizeau's 0.46 of 0.92 is f = 0.500, 14.3% above f₀ at the D lines (15.0% above his own
  Fresnel figure 0.40). He gives no uncertainty; he says the water's speed across the tube was not corrected, which
  MM 1886 later did.
- F6 not killed: Zeeman's observed coefficients (0.465, 0.464, 0.452, 0.445 at 4500, 4580, 5461, 6870 Å) against f₀
  without dispersion χ² = 47.5 on 4, with the dispersion term 0.27 on 4; summed squares 1.2 × 10⁻³ against 9.3 × 10⁻⁶.
  Our ratios of the two coefficients from Daimon's n(λ) match Zeeman's own to 0.1%.

What the run shows: the boost's composition rule, with one input (water's n), gives the drag Fizeau, Michelson and
Morley, and Zeeman measured; with n read at the frequency the Doppler factor gives in the water's frame, it gives the
colour dependence Zeeman measured to his errors, which Fresnel's coefficient alone misses (χ² 47 on 4). Galilean
composition, f = 1, is 28 of MM's errors away. Classical (Laue 1907 for the rule, Lorentz 1895 for the term); this does
not tell relativity from Fresnel's partial drag with Lorentz's term, which agree to first order. The sorting: the drag
is the composition of two readings, the dispersion term the payload's frequency moved by the Doppler factor.
