# LWL: line width against lifetime, on more pairs

9 Nov 2026. Tom: "yes", to taking up the line-width test after the dipole was parked (SPN R772). It grows TIM's T5
(`plans/tim-plan.md`), which found Γτ = 1.0010 ± 0.0025 on one pair, sodium's D2 line.

## What is tested

*Reads and Writes in Physics* §4.3 reads a line's Lorentzian as the heat of a phase's uniform turn. The width Γ and the
decay time τ are then one quantity, the standpoint's height, read in two units: in frequency by sweeping a probe across
the line, in time by watching the excited state empty.
- **The bridge.** The clock, which has to be carried in for each factor alone and cancels from the product.
- **The prediction, from that reading alone.** Γ·τ = 1, with Γ the full width at half maximum in angular frequency
  (equivalently Γ in energy against ħ/τ), for every transition where both are measured independently.
- **Classical.** This is Weisskopf and Wigner (1930). What the reading adds is that the product is free and each factor
  is an amount.
- **How it can fail.** A pair outside its errors. Weisskopf–Wigner holds for an isolated exponential decay, so a
  confirmed failure would be a measurement's problem, or a decay that is not one exponential.

## Pairs: what counts, fixed now

A pair is one transition (or one particle's decay) with:
- **a width measured in frequency or energy:** a line shape, a resonance scan, a Mössbauer absorption line, or a
  Primakoff cross-section, which measures a radiative width; and
- **a lifetime measured in time:** a decay curve, decay in flight, or delayed coincidence.

These do not count:
- a width computed from a lifetime, or a lifetime from a width (compilations often give one from the other);
- a lifetime inferred from a molecular potential's dispersion coefficient (photoassociation's C₃). That is a third
  route, neither a line shape nor a clock. It is recorded but kept apart.

Where several measurements of one kind exist, the most precise published value of each kind is used, decided by its
quoted error before the two are compared. Where a branching ratio enters (a partial width against a total lifetime), the
branching ratio is carried in, named as a third amount, and its error added.

Each value is read from its paper's abstract or text, as reachable here (OpenAlex, arXiv's export, the journals' pages).
For each one the plan records the source, how it was measured, and the sha256 of the response read.

## Known beforehand (from memory unless marked, every number to be checked in the run)

- **Na 3p ²P₃/₂** (read in TIM): Oates, Vogel and Hall 1996, against Volz et al. 1996. Γτ = 1.0010 ± 0.0025.
- **The neutral pion.**
  - The Primakoff width: PrimEx-II (Larin et al. 2020), Γ(π⁰ → γγ) about 7.80 eV.
  - The direct decay length: Atherton et al. 1985, τ about 0.90·10⁻¹⁶ s, so ħ/τ about 7.3 eV.
  - A known tension of about 2σ. The branching ratio to γγ (98.8%) is the third amount.
- **The alkali resonance lines.** These were the subject of the 1990s lifetime discrepancies, resolved by
  photoassociation and by better decay measurements. Whether independent line-shape widths exist for Li, K, Rb and Cs, I
  do not know.
- **⁵⁷Fe's 14.4 keV Mössbauer line.**
  - The lifetime by delayed coincidence: about 141 ns.
  - The natural width ħ/τ: about 4.7 neV.
  - Measured Mössbauer widths are broadened by the source and the absorber's thickness. A pair counts only where the paper
    extracts the natural width itself.

## Predictions

- **L1.** Every pair found: |Γτ − 1| under 3 combined standard errors.
- **L2.** All pairs together: χ² of (Γτ − 1)/σ with p above 0.001.
- **L3** (the one place it can fail on what is known now). The neutral pion's Γτ within 3 combined errors of 1, the
  branching ratio carried in.
- **L4** (a reading, not counted). Wherever two measurements of one kind disagree with each other by more than their
  errors (the alkali lifetimes before 1995, Na's old time-domain values), the side that later moved is the one that
  moved toward Γτ = 1. The history is recorded, not tested.
- **Killed** if L1 or L2 fails on pairs that meet the rules above.
- **Untested**, said plainly, if fewer than three pairs besides sodium can be read here.

## Bridges, named

- **Width:** a frequency standard, or for the pion a beam energy and a cross-section's normalisation.
- **Lifetime:** a clock, or for the pion a decay length and a Lorentz factor (a speed carried in).
- **The product:** the clock cancels. For the pion, ħ converts eV·s, a conversion, not a measurement.

## Runs

### Run 1 (9 Nov; `runs/lwl/lwl.py`, output `runs/lwl/lwl-run1.txt`)

The search was made after this plan was committed. OpenAlex's free daily budget was spent and Semantic Scholar refused,
so abstracts and texts came from arXiv's export, PDG, Crossref, and pages found by web search.

**Pairs found: five, lifetimes from 10⁻¹⁷ s to 10⁻⁸ s.**

| Pair | Width, in frequency or energy | Lifetime, in time | Γτ | from 1 |
|---|---|---|---|---|
| Na 3p ²P₃/₂ | Oates, Vogel and Hall 1996, line shape: 16.237(35) ns | Volz et al. 1996, decay in flight: 16.254(22) ns | 1.0010 ± 0.0025 | +0.41σ |
| π⁰ | Larin et al. 2020 (PrimEx-II), Primakoff: Γ(γγ) = 7.802 ± 0.052 ± 0.105 eV, over B(γγ) = 98.823 ± 0.034% | Atherton et al. 1985, direct: (8.97 ± 0.22 ± 0.17)·10⁻¹⁷ s | 1.076 ± 0.037 | +2.05σ |
| Cd 5s5p ¹P₁ | arXiv:2210.11425 (2022), line shape: 1.60(5) ns | beam-foil 1973, the most precise time-domain value in that paper's table: 1.90(15) ns | 1.19 ± 0.10 | +1.86σ |
| Kr 3d hole | 88 ± 4 meV | Drescher et al. 2002, attosecond pump–probe: 7.9 (+1.0/−0.9) fs | 1.06 ± 0.14 | +0.41σ |
| Dy, 421 nm level | arXiv:1009.2962, line shape at zero intensity: 31.9(8) MHz | Curry, Den Hartog and Lawler 1997, as that paper quotes it: 33.1(17) MHz equivalent | 0.964 ± 0.055 | −0.66σ |

Notes on the pairs:
- **Kr's width** is read secondhand from publications.aob.rs/99/pdf/047-050.pdf. Its primary measurement was not read.
  The lifetime's two sides are averaged into one error, 0.95 fs.
- **Dy's lifetime** is the time-resolved laser-induced fluorescence of Lawler's group. That method is from memory: the
  1997 paper itself was not reachable.
- **The pion's two methods** are named by PDG 2024. PDG says Atherton 1985 is "the only direct measurement of the π⁰
  lifetime".

**Sources read** (sha256 of what was read, not committed):
- PDG 2024 π⁰ listing: `1d738eed1677e11d929fe59c23eec64b2f8ba039a10510b132dc2d6d94340821`
- arXiv:2210.11425 (Cd): `eb672663df38da1fa594da9f7030958fa61fd9fe6777db3625e9232f2c0bd8a7`
- arXiv:2309.03669 (Zn): `bf54a552f0b0f7875046b131f84ae93404d35ca57283619a377e783f2d4bc7a3`
- arXiv:1009.2962 (Dy): `4794135c6b227c1ddc4b89536295a82024d4ab0f9c45a40d1b69f6cb83f3c4ff`
- aob.rs Kr paper: `937476be87f094f10a29c9fe6420cfe6f8665feabfea519047dec719f3a0b11e`
- RePEc's record of Drescher et al. 2002, with its abstract: `981ecc2a1ac77b9ceec14ec4aaef8f66a6b4983dd4f30ce9d7589e9b96c5c014`
- Na: the OpenAlex responses recorded in TIM.

**Not pairs:**
- **Zn ¹P₁.** arXiv:2309.03669's width, 1.440(18) ns, is compared there only with a compiled average of five methods.
  No time-domain value was found.
- **Dy 741 nm.** Two time-domain methods, no width.
- **⁸⁷Sr ³P₀.** The cavity width is a ratio to ³P₁'s.
- **⁴⁵Sc.** No natural width measured.
- **Ar¹³⁺.** A lifetime only.
- **⁵⁷Fe Mössbauer.** No paper extracting the natural width was reached.

**Verdicts:**
- **L1 not killed.** Every pair lies within 3σ; the largest is the pion's, 2.05σ.
- **L2 not killed.** χ² 8.43 on 5, p = 0.134.
- **L3 not killed.** The pion is 2.05σ from 1. Without the branching ratio it would be 1.063, so the ratio matters at
  this precision.

The ties and choices the rules left, reported, not counted:
- Cd with the Hanle width 1.66(5) ns (1964, 1969) in place of the line shape: +1.49σ.
- Cd with the 2004 time-resolved fluorescence, 1.75(20) ns, in place of beam-foil: +0.72σ.

**Read after the run, not tested.**
- Four of the five lie above 1, each because the lifetime measured in time is the longer.
- For Cd, the beam-foil value is the culprit beam-foil is known for: cascades from higher levels refill the level and
  lengthen the decay.
- The pion's tension is the one in the literature (PDG's average uses both methods, scale factor 1.2).
- Nothing here asks for more than Weisskopf and Wigner.

**L4 (history, not counted).** On sodium the time-domain values moved toward the width in 1996, as TIM recorded. On
cadmium, the 2022 width sits under every time-domain value, and its authors call it the one less open to systematics.

**What the run says.**
- One quantity read two ways agrees over nine orders of magnitude of lifetime: from 10⁻¹⁷ s (the pion) through 10⁻¹⁴ s
  (an inner-shell hole) to 10⁻⁸ s (sodium).
- What differs between the two reads is the standard each needs, a frequency or a clock. The product needs neither.
- That is the reading of *Reads and Writes in Physics* §4.3, and it survived a test that could have failed. It is still
  classical physics.

## Run 2 predictions (9 Nov 2026, Tom: "1,2,3,4", the fourth "⁵⁷Fe for the line-width test"; written before the search)

The rules above stand (independent width and lifetime, the most precise of each kind by its quoted error, every value read
from a reachable source with its sha256). Run 2 looks for ⁵⁷Fe's 14.4 keV level, and records any further pair met on the way.

- **L5.** ⁵⁷Fe: a natural width extracted in the energy domain (a Mössbauer line extrapolated to zero absorber thickness,
  a synchrotron Mössbauer source's line, or an interferometric or γ-resonance width), against a lifetime measured in time
  (delayed coincidence, or nuclear forward scattering's decay): Γτ within 3 combined errors of 1.
- **L6.** All pairs of runs 1 and 2 together: χ² of (Γτ − 1)/σ with p above 0.001.
- **Untested**, said plainly, if no energy-domain natural width for ⁵⁷Fe is reachable. A width computed from the lifetime
  (as compilations give it) does not count; nor does a measured line width with no extraction of the natural part.

### Run 2 (9 Nov 2026), web search only; L5 untested

Two extended web searches for an energy-domain natural width of ⁵⁷Fe's 14.4 keV level. What came back:
- 0.097 mm/s (half width) and 4.66 neV as "the natural width": each, where its derivation shows, is ħ/τ from the lifetime
  (141.8 ns in the ELTE lab notes), so by the rules it does not count.
- 15 neV, the ESRF synchrotron Mössbauer source's bandwidth: an instrument's, not the line's.
- Student reports (MIT) that extrapolate absorber widths to zero thickness: the intercept includes the source's width, its
  units were not recoverable from the snippets, and the Wisconsin copy was blocked by this session's network
  (moessbauer.chem.wisc.edu not allowed). Not a primary measurement with an error.

**L5 untested**: no energy-domain extraction of ⁵⁷Fe's natural width, with its own error, was reachable here. **L6** is
unchanged from run 1 (five pairs, χ² 8.43 on 5). A run 3 would need a primary paper that fits the thickness series with
the source's width as a free parameter (or a synchrotron line with known instrument function), read in full.
