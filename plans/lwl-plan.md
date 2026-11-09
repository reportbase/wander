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

(Nothing yet.)
