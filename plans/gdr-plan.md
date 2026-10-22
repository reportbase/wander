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


### Run 1 (22 October; `python3 runs/gdr/gdr.py <data dir>`, 8 minutes; output `runs/gdr/gdr-run1.txt`)

Data: fetched again from figshare 16764508 (file 35078602, `Toroidal_topology_grid_cell_data.zip`, 319,902,753 bytes),
sha256 `56842a7ae8e8f9144e390c9cdd72494d8ea2c48f2ce89cdee4780a49ed495372`, matching GRD's; held under `/tmp`, not
committed. Set-up change, recorded: bin edges laid from the minimum by index (so they scale exactly with k), not by
`np.arange` as in GRD; at k = 1 this reproduces run 1 to the rounding shown (Q 68.01, 95.03; R 56.18, 83.55, 118.00;
S 54.72; first steps 1.3974, 1.4872, geometric mean 1.4416).

- **P1 (a) not killed; P1 (b) KILLED.** (a) With the bin and smoothing scaled with the world, every spacing is k times
  and every ratio the same to 0 (k = 0.5) and 2.2·10⁻¹⁶ (k = 7): an identity, as expected. (b) With the bin held at
  2.5 cm: k = 0.5 moves the first-step mean +0.0195 (1.4209, 1.5026; inside 0.03), but k = 2 moves it +0.133 (1.6801,
  1.4758; mean 1.5746). At k = 2 the method no longer measures the spacing: Q's small module reads 58.05 cm where 136 is
  true (its first step 1.68), R's three 111.4, 164.5, 213.0 against 112.4, 167.1, 236.0. Post hoc: with 2.5 cm bins in a
  3 m box each bin holds a quarter of the occupancy, the 0.1 s floor (a time amount per bin, so tied to the bin's area)
  drops bins, the σ = 2.5 cm smoothing is half as wide relative to the fields, and the autocorrelogram finds nearer
  maxima, the same failure as rat R's day 2 (thin data, nearer maxima). So the *ratio* is a reading, but GRD's
  *measurement* of it is not: it carries three amounts (the bin, the smoothing, the occupancy floor) and is
  trustworthy only in a band of bin-to-spacing and data-per-bin; run 1 sat inside it (k = 0.5 agrees within 0.02).
  My prediction trusted the method too far; the kill stands.
- **P2 not killed.** The K nearest √2 at the corner are 9 (1.4203) and 10 (1.3764). Ratios, K = 9: 2.064, 1.586,
  1.453, 1.420, 1.453, 1.586, 2.064 (longest run within 0.07 of √2: 3); K = 10: 2.052, 1.568, 1.426, 1.376, 1.376,
  1.426, 1.568, 2.052 (run 4). Log-steps grow outward as cosh: 1, 1.066, 1.315, 2.066 times the central one (K = 9).
  So the turn's own layout of scales looks like a constant ratio over at most five modules round its corner and departs
  by the sixth (1.586, 0.166 in log₂ off √2); the outermost finite step is always about 2 (it tends to 2: cot(π/2K)/
  cot(π/K)).
- **P3 not killed.** 0.3–10 m: √2 10.12 steps, 11 modules; 3/2 8.65, 9; √e 7.01, 8; 1.7 6.61, 7; 2 5.06, 6. The turn at
  K = 9 with H = √3 m puts all 8 boundaries inside (0.305 … 9.82 m; its interior span tan 80°/tan 10° = 32.16, against
  33.3). Post hoc: on this range the turn's nine addresses and √e's eight modules are the same count; the count of
  modules over a range does not separate the turn from economy, only the step profile does (P2).
- **P4 not killed.** At σ = 0.045 in log₂: 3/2 needs 5 independent first steps, √e, 1.7 and 2 one each; the turn's
  step at rank 3 out (1.586) needs 2 steps of that rank. GRD P3's "five animals with two modules" was the right size.
- **P5 not killed.** (a) A proportional plane doubles its count within d at √2 at every d (to 50 digits). (b) On the
  reader's lay the count Mn(1 + ln s) doubles at s′ = e·s², ratio e, 5.44, 27.2, 272 at s = 1, 2, 10, 100: no constant
  ratio; adding one level's addresses is ratio 2 at every s. (c) The lay is along distance only, so a level is a
  doubling of distance in the plane and the wedge alike.

**What it shows.** (1) The module ratio is a reading (scale-free, no amount); the spacings in cm and the method's own
bin, smoothing and occupancy floor are amounts, and the method's ratio holds only inside a band of them (P1(b) killed at
k = 2; GRD run 1 sat inside it). (2) OFS's levels are doublings of *distance*, so OFS's own baseline for a ladder of
scales is 2, in any dimension; √2 is a doubling of the count on a *proportional* (writer's) plane, a translation-invariant
lattice, which is what a grid module is. GRD's "a halving in D.1's sense, in its own dimension, 2^(1/D)" is SPN Appendix
D's reading, not anything OFS's lay supplies: on the settled lay √2 needs an added choice, to count levels by area. (3) The
turn's K addresses laid along scale (OFS §8) give a near-constant ratio only round their corner (five modules) and a
cosh-growing step outward; constant-ratio laws (√2, √e, 3/2) give a flat profile. Six or more modules in one animal,
with a box and method that hold the largest, would tell them apart; the module count over a range would not (the turn at
K = 9 and √e both give 8–9 over 0.3–10 m). (4) Each animal's smallest spacing is its H (a free zoom); only the ratio is
the geometry's. The data in hand (two rats, one with three modules) cannot test any of (2)–(4).
