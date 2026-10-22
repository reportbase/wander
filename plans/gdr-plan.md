# GDR: GRD revisited (grid modules read with K, H, reading and writing)

*Plan, predictions and kills written 22 October 2026, before any computation for this plan and before the dataset was
fetched again (Claude, asked to revisit GRD in the light of what OFS has since settled). The lab rules hold: nothing above
the "Runs" line is edited after the run. Scripts and outputs in `runs/gdr/`.*

## Known beforehand

- **GRD run 1** (`plans/grd-plan.md`, 14 Oct; SPN R248): Gardner et al. 2022 (figshare 16764508 v6, CC0, sha256
  `56842a7a…d495372`), three rats. Module spacings (median of cells, autocorrelogram method fixed before the data was
  opened): Q 68.0, 95.0 cm; R 56.2, 83.6, 118.0 cm; S 54.7 cm. Adjacent ratios Q 1.397; R 1.487, 1.412 (pooled 1.432).
  Post hoc, rat R day 2: 53.0, 79.1, 90.2 cm (1.491, 1.141); the largest module (about 0.8 of a 1.5 m box) is not
  measured reliably. The two first steps, 1.397 and 1.487, are the reliable ratios: geometric mean 1.4413.
- **The literature as known from training** (to verify where marked): Stensola et al. 2012 mean adjacent ratio about
  1.42, roughly constant; up to four or five modules recorded in one rat, more presumed down the axis (to verify);
  Barry et al. 2007 about 1.7 and grids partly rescaling when a familiar box is stretched (to verify); Wei, Prentice and
  Balasubramanian 2015 (economy) √e in 2D, the general form e^(1/D) (to verify); their argument is radix economy
  (minimise levels × cost per level, r/ln r least at r = e), stated here from my recollection.
- **`plans/grd-landscape.md`**: SPN's slot as the measure-free baseline 2^(1/D), the coding theories as departures.
- **OFS §8, "A fixed count, aimed by H" and "Two readers, one K"**: K addresses of the uniform turn laid along distance at
  H·tan(kπ/2K), half inside H at every H; the reader's lay is d/H to the corner, then 1 + ln(d/H), each doubling of
  distance ln 2 wide and holding n·ln 2 of the n addresses across the near field; H a zoom; the writer's number line
  proportional, no corner. OFS §9, "Units within units": a hierarchy of units held in ratios alone, the factor between
  levels a ratio read one level up, one amount at the top.
- **Not checked**: draw's labs (the draw repository is not in this environment), so any overlap with them is unknown.

## The reading to test

1. **Reading and writing.** A module ratio λ₂/λ₁ is a quotient of two amounts in one unit: unchanged when every length is
   scaled by k, so a reading. A spacing in cm is a writing (the tracking's calibration carried in). But GRD's *method*
   also carries amounts in (2.5 cm bins and smoothing, fixed in cm), so the measured ratio is a reading only if the
   method's own amount does not move it. That is checkable on the data.
2. **The animal's H.** Each rat's smallest module is a free starting value (H, a zoom; GRD's λ₁ differs between the two
   rats by 0.138 in log₂, the ratio by 0.045). Not testable on two animals; it fixes what the next dataset must hold.
3. **Which lay the modules are.** Three candidate layouts of scales:
   - (c) a constant ratio r (√2 the halving of area; √e economy; 2 the halving of length; 3/2 and 1.7 named
     alternatives);
   - (t) the turn's own K addresses, boundaries at H·tan(kπ/2K), i.e. quantiles of the half-Cauchy: in ξ = ln(d/H) they
     are quantiles of the hyperbolic secant law, steps (π/K)·cosh ξ, least at the corner and growing outward;
   - (ℓ) the reader's lay: proportional to H (steps (k + 1)/k), then levels of ratio 2 (each n·ln 2 addresses).
   My reading before computing: a grid module is a translation-invariant lattice, the *writer's* proportional map with no
   corner; the ladder of modules is a tower of units (OFS §9) whose factor is a ratio. On that reading the √2 is a
   doubling of the *area* count of a proportional (writer's) lay, and is **not** the reader's lay counted in 2D: the
   reader's lay is along distance and its levels are doublings of distance (ratio 2) however many parties there are.
   GRD's plan and the landscape say "2^(1/D)" as if D.1's halving could be taken in area; OFS gives no area lay.

## Predictions

- **P1 (the ratio is a reading of the data, not of the method).** Re-run GRD run 1's method on the same file
  (sha256 checked) with every tracked position scaled by k:
  - (a) with the bin and the smoothing scaled by k too (2.5k cm), every module spacing comes out k times run 1's and
    every ratio identical, to a relative 10⁻⁹, at k = 0.5 and 7 (an identity: no amount enters);
  - (b) with the bin and smoothing kept at 2.5 cm (the method's amount carried in), at k = 0.5 and k = 2, the geometric
    mean of the two reliable first steps (Q M1→M2, R M1→M2) stays within 0.03 of its k = 1 value.
  *Killed* if (a) fails at 10⁻⁹, or (b) moves by 0.03 or more at either k. Untested if the data cannot be fetched.
- **P2 (the turn's layout looks constant only near the corner).** For the turn's K addresses, adjacent boundary ratios
  r_k = tan((k + 1)π/2K)/tan(kπ/2K): over K = 6 … 40, the K whose central ratio (the one at the corner) is nearest √2 are
  9 and 10; for them the longest run of consecutive r_k within 0.07 of √2 is at most 4 (five modules), and the outermost
  finite r_k exceeds 2. So at most five modules at √2 cannot tell (t) from (c); a sixth can. *Killed* if a run of 5 or
  more exists for K = 9 or 10, or the outermost finite r_k is 2 or less, or the nearest K are not 9 and 10.
- **P3 (counts across a range).** To span 0.3–10 m (a range of 100/3, ends included), a constant ratio needs
  1 + ⌊log(100/3)/log r⌋ modules: 11 at √2, 9 at 3/2, 8 at √e, 7 at 1.7, 6 at 2. The turn with K = 9 and H the range's
  geometric mean (√3 m) puts all 8 of its interior boundaries inside 0.3–10 m. *Killed* if any count differs.
- **P4 (what the next dataset must hold).** At the between-animal scatter of a step seen in run 1 (sd of log₂ ratio
  0.045, taken as σ), the number n of independent first steps needed so that 1.96σ/√n is under half the log₂ distance
  between √2 and an alternative is: 5 for 3/2, 1 for √e, 1 for 1.7, 1 for 2. *Killed* if any differs.
- **P5 (√2 is the writer's area count, not the reader's lay).** Exact: (a) on a proportional plane (count ∝ d²) the count
  within d doubles exactly at a ratio √2, at every d; (b) on the reader's lay in the plane (M directions, n addresses
  across the near field, count Mn(1 + ln s) past the corner), the ratio s′/s that doubles the count is not constant
  (it is s·e, i.e. s′ = e·s², ratio e·s), and the ratio that adds one level's addresses (Mn·ln 2) is 2 at every s;
  (c) equal addresses per level gives ratio 2 in the plane and in the wedge alike. *Killed* if (a) is not √2 at every d
  tested, if (b)'s doubling ratio is constant across s = 1, 2, 10, 100, or if (c) is not 2.

## Not yet computed

The turn's ratios for K = 9 and 10 and the run lengths; the P3 and P4 counts beyond my head arithmetic; P1 on the data.
Two readings left open, not predictions: on the reader's lay at n addresses across the near field, the step between
addresses past the corner is e^(1/n), so n = 2 gives √e and n = 3 gives e^(1/3) ≈ 1.3956 (numerology until a reason
fixes n); and whether cells per module (97/66, 166/168/149) say anything about K: no, the counts are set by where the
probes sat.

## Runs
