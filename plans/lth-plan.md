# LTH: the distance ladder as a tower of holds

*Plan, predictions and kills written 16 October 2026, before Hubble's 1929 table, any modern distance for his galaxies,
or the SH0ES per-anchor values were opened in this environment (Claude; Tom: "how does the tower of holds and parallax
help each other", then "yes" to a section in `papers/parallax.md` and this plan; SPN R317). The lab rules hold:
nothing above the "Runs" line is edited after the run.*

## The claim

The tower of grouped holds (*Degrees of Freedom* §5.10; OFS §9, "Units within units"; SPN R316): lengths read against
nested units cancel each unit inside its own level; what links two levels is itself a ratio, read one level up; one
amount is written, at the top or the bottom. Read as the distance ladder (`papers/parallax.md` §7, "The ladder as a tower
of holds"): each rung is a level of unit (a baseline, or a kind calibrated on the rung below), the links are ratios, and
the one written amount is the metre.

What the tower predicts that a list of methods does not:
- **A shared factor per rung.** A rung's hold is common to everything read on it and above it. An error in that hold
  moves every distance on and above the rung by one factor, and leaves every ratio within the rung as it was.
- **Errors add by rung.** With independent errors on each rung's link, a distance on rung k carries the errors of
  rungs 1 to k; two distances on one rung are related by that rung's own scatter alone.

## Keep the case

Distances d are amounts (Mpc, m). Every quantity tested is a ratio of two distances, a pure number, reported in levels
(log₂). **The bridge** is the identification: *a rung of the ladder is one level of unit in the tower*. No unit relation
h or v is used; the test is on amounts and their ratios only.

## What is already known to me (stated so the test is not mistaken for blind where it is not)

From training, before this plan:
- Hubble's 1929 constant was about 500 km/s/Mpc against about 70 today, so his distances are short by roughly a factor
  of 7, about 2.8 levels, on average.
- Baade (announced 1952; *PASP* 68, 5, 1956) found the Cepheid zero-point used by Hubble too faint by about 1.5 mag, a
  factor of about 2 in distance, about 1 level; Sandage (*ApJ* 127, 513, 1958) found that many of Hubble's "brightest
  stars" were HII regions, a further large factor for galaxies placed by them.
- So the historical story already says the deeper rungs were off by more. What I have not seen is Hubble's table
  object by object, which rung each distance came from, or any per-galaxy comparison with modern distances. The tests
  below are on that per-object structure, which the story does not state.
- SH0ES (Riess et al. 2022, *ApJL* 934, L7) quote H₀ = 73.04 ± 1.04 km/s/Mpc from three geometric anchors (NGC 4258's
  masers, Milky Way parallaxes, the LMC's eclipsing binaries); I recall that the single-anchor values agree, roughly,
  but not their numbers.

## The data (to be supplied, in this order, each recorded here before it is opened for more than its layout)

1. **Hubble 1929**, *PNAS* 15(3), 168–173, doi:10.1073/pnas.15.3.168 (free): Table 1 (the nebulae with distances) and
   the text saying how each distance was found. **The rung of each object is assigned from Hubble's text alone, before
   any modern distance is looked up**, into: (a) resolved stars of a calibrated kind (Cepheids, novae), (b) the
   brightest stars, (c) a cluster's mean luminosity (the Virgo members). If the text does not say for an object, it is
   left out, and the count left out is recorded.
2. **Modern distances** for the same objects: the NASA/IPAC Extragalactic Database's redshift-independent distances
   (NED-D), the median of the Cepheid and tip-of-the-red-giant-branch values where there are any, else the median of all;
   or Cosmicflows-4 (the Extragalactic Distance Database) if NED-D cannot be reached. Source, version, licence and
   sha256 recorded here; the choice of median fixed now, not after.
3. **SH0ES 2022** single-anchor H₀ values and the anchors' own quoted distance uncertainties, from the paper's tables.

## Predictions

Let r_i = log₂(d_modern / d_Hubble) for object i, in levels. Group by Hubble's rung (a), (b), (c).

- **P1 (deeper rungs, larger factors).** The rung means satisfy mean(a) < mean(b) and mean(a) < mean(c): the rungs
  built on the Cepheid rung carry its factor and their own. *Kill:* either inequality fails. (Weak, given what is known
  above; written so that it is on record.)
- **P2 (a shared factor per rung).** Within each rung with at least four objects, the spread of r (its standard
  deviation) is smaller than the difference between that rung's mean and rung (a)'s mean. The tower says each rung
  carries one factor common to its members; a list of independent per-object errors does not. *Kill:* for rung (b), sd(b)
  ≥ |mean(b) − mean(a)|.
- **P3 (ratios survive better than distances).** For pairs of objects on the same rung, the log ratio of their
  distances, log₂(d_i/d_j), is closer to the modern value than either distance is: the median over same-rung pairs of
  |log₂(d_i/d_j)_Hubble − log₂(d_i/d_j)_modern| is less than half the median over objects of |r_i|. *Kill:* it is half
  or more.
- **P4 (the anchors as the bottom hold).** Swapping the bottom hold moves H₀ by the anchors' ratio only, so the
  single-anchor H₀ values differ by no more than the anchors' own geometric uncertainties allow: χ² of the single-anchor
  values about their weighted mean, with each value's uncertainty taken as its anchor's geometric term alone, is at most
  2 per degree of freedom. *Kill:* χ²/dof > 2. (Weak if the paper's single-anchor uncertainties already include terms
  shared above the anchor; then the shared terms are removed using the paper's own budget, and how is recorded here
  before the χ² is computed.)

## Exact part (no data)

- **E1.** Given independent errors σ_j (levels) on each rung's link, a distance on rung k has error √(Σ_{j≤k} σ_j²)
  against the bottom amount, and two distances on rung k have a ratio error set by the rung's own scatter alone,
  independent of k. An identity of independent sums; checked symbolically in the run script, not a test of the world.

## What would count against the reading, beyond the kills

If P2 and P3 are killed together, Hubble's errors were object by object, not rung by rung, and the tower adds nothing to
a list of methods for his ladder. If P4 is killed, something above the anchors depends on which anchor is used, and the
ladder is not a tower with one bottom hold.

## Data, recorded before the run

**Hubble 1929** (recorded 16 Oct, before any modern distance was looked up). The publisher, PubMed Central, Europe PMC
and the web archive refused this environment; two course copies were used:
- `hubble.1929.pdf`, www.astro.rug.nl/~weygaert/tim1publication/cosmo2007/literature/hubble.1929.pdf (a retyped
  transcription, 5 pages), sha256 6b3a60069c31e3b616dc4ea70d612b62d3d9487b3a8b187a5bb589d990629775;
- `hubble1929.pdf`, www.hep.shef.ac.uk/roszkowski/phy306/papers/hubble1929.pdf (a scan with OCR, 6 pages), sha256
  bc98cc36e172a76db65988d813510c1fe34b7ba2ea15ccefa2ef413cd6499ba2.

The two agree on every distance in Table 1. Public domain in the US (published 1929). Not committed.

**The rungs, from Hubble's text** ("The first seven distances are the most reliable, depending, except for M 32 the
companion of M 31, upon extensive investigations of many stars involved. The next thirteen distances, depending upon
the criterion of a uniform upper limit of stellar luminosity, are subject to considerable probable errors … The last
four objects appear to be in the Virgo Cluster. The distance assigned to the cluster, 2 x 10⁶ parsecs, is derived from
the distribution of nebular luminosities, together with luminosities of stars in some of the later-type spirals"):

| rung | objects (Hubble's r, Mpc) |
|---|---|
| (a) stars involved, Cepheids and others (7) | SMC 0.032, LMC 0.034 (Shapley's values), NGC 6822 0.214, NGC 598 0.263, NGC 221 0.275, NGC 224 0.275, NGC 5457 0.45 |
| (b) brightest stars (13) | NGC 4736 0.5, 5194 0.5, 4449 0.63, 4214 0.8, 3031 0.9, 3627 0.9, 4826 0.9, 5236 0.9, 1068 1.0, 5055 1.1, 7331 1.1, 4258 1.4, 4151 1.7 |
| (c) cluster mean luminosity (4) | NGC 4382, 4472, 4486, 4649, all 2.0 (Virgo) |

Two notes, made now: NGC 221 (M 32) is in rung (a) by Hubble's grouping but has its distance by association with
M 31, not from its own stars; it stays in (a), as the plan assigns by Hubble's text. The four Virgo members share one
distance, so within rung (c) the spread of r is the spread of their modern distances alone, and P3 has no Hubble ratio
within (c) to test (all are 1); P3 uses rungs (a) and (b) only.

**NED-D** (recorded 16 Oct, after the rungs above were committed): NED30.5.1-D-17.1.2-20200415.csv, from
ned.ipac.caltech.edu/Archive/Distances/, NED-D version 17.1.0 (15 Apr 2020), 41,077,792 bytes, sha256
fe818b6d652d9e8e822002aeb619a166e6611172d4d7496ee23c0223e1a05f55. NED asks for its acknowledgement; © Caltech. Not
committed. NED names the Messier objects by their Messier numbers; NGC 5194 is taken as MESSIER 051a (M 51a, the
galaxy itself, not the pair). Every row with a positive distance is used, whatever its exclusion code.

**SH0ES 2022** (recorded 16 Oct): arXiv:2112.04510 (the accepted version), 9,544,553 bytes, sha256
572e5d2c0f32bf6e80a118eec13ed0107e1e2830f9ebe90b5bc4e9d1b7fa5df1. The single-anchor values are its fits 10–12 (the
"Geometric Anchors Variants" of its table of variants): N4258 72.51 ± 1.54, Milky Way 73.02 ± 1.19, LMC 73.59 ± 1.36
km/s/Mpc. These quoted uncertainties include terms shared above the anchors (the SN Ia calibrators, the hosts' P–L), so,
as the prediction says, they are replaced. **How, fixed before the χ² is computed:** each value's uncertainty is its
anchor's distance term in the paper's error budget (its Table 7, "σµ,anchor, Anchor distance", this work): N4258 1.5%,
MW 1.0%, LMC 1.2%, as a percentage of that value. That is the prediction's "geometric term alone". Reported beside it,
not a kill clause: the same with the budget's "subtotal per anchor" (N4258 1.8%, MW 1.0%, LMC 1.4%), which adds the
anchor's own P–L mean, zero-points and metallicity term. χ² about the inverse-variance weighted mean, 2 degrees of
freedom.

## Runs

(none yet)
