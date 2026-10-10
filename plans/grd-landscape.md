# Grid-cell modules: where SPN might slot in

*10 October 2026, Claude; Tom: "this is preliminary analysis, lets just establish the boundries, see how we might slot in.
than look for colloration or plan real world confirmation later." A reading, not a test and not a ruling. Nothing here is
evidence for SPN. It maps what is measured, what the existing theories say, and where SPN's claim would sit among them.
Items marked (to verify) come from memory or search snippets and were not read in the original.*

## What is measured

- The grid cells of the medial entorhinal cortex fall into a few discrete **modules**, each with its own lattice
  spacing, orientation and asymmetry. Spacing grows along the dorsoventral axis (Stensola et al., *Nature* 2012).
- **The ratio between adjacent modules.**
  - Stensola et al. report a mean near 1.42, roughly constant from module to module, in rats.
  - Other reports put it nearer 1.6–1.7 (Barry et al. 2007; to verify).
  - The field treats the range 1.4–1.7 as observed.
- **What is not settled:**
  - whether the ratio is truly constant;
  - how many modules there are, perhaps four or five in rats;
  - whether the ratio depends on the space's dimension. 3D recordings exist in flying bats (Ginosar et al. 2021), with
    local rather than global order; module ratios in 3D are not known to me (to verify).

## The theories, and what each supplies

| family | claim about the ratio | what sets it |
|---|---|---|
| **Efficient coding: economy** (Wei, Prentice and Balasubramanian, *eLife* 2015) | √e ≈ 1.65 for idealised neurons; 1.4–1.7 for realistic ones. A prediction for other dimensions too (the general form, e^(1/D) by my recollection, to verify) | minimising the neurons needed for a given resolution over a given range: a cost, i.e. an added measure |
| **Efficient coding: nested codes** (Mathis, Herz and Stemmler, *Neural Computation* 2012; *PRL* follow-up) | discrete scales with a constant ratio; resolution exponential in the number of neurons; short spacings outnumber long | maximising resolution, Fisher information or decoding error: an added measure |
| **Mechanism: self-organisation** (Kang and Balasubramanian, *eLife* 2019) | 1.4–1.7 in the published version (1.2–2.0 in the preprint), from geometric relations between triangular lattices | a smooth gradient of inhibition distance plus excitation along the axis: the brain's wiring |
| **SPN** (Appendix D, Proposition D.1) | a halving in the dimension of the reader's room: 2^(1/D), so √2 ≈ 1.414 in two dimensions | no measure at all: on a level with only its ends, order and flip, the halving is the only split supplied |

## The boundaries: where SPN sits

- **SPN is not a coding theory or a mechanism.** It makes no claim about neurons, wiring, noise or the number of
  modules, nor about absolute scale, orientation or field size. Those belong to the families above. SPN speaks only to
  the ratio, and only to what the ratio would be *without* any added measure.
- **The slot: SPN as the measure-free baseline.** D.1 says any ratio other than a halving needs a measure added from
  outside. The efficient-coding theories are exactly such measures: a cost in neurons, or a decoding error. So the two
  are not rivals in kind:
  - SPN gives the baseline, 2^(1/D);
  - a coding theory gives the departure from it its measure imposes;
  - and a measured ratio's distance from 2^(1/D) would read as how much the added measure matters.

  Read so, Stensola's 1.42 sits on the baseline, and the 1.65 of idealised economy sits off it by what economy adds.
- **Where SPN agrees with what is known** (and so adds nothing new): discrete levels, a constant ratio, no preferred
  scale.
- **Where SPN differs, and could be told apart:**
  - the dimension. SPN's baseline is 2^(1/D): 2, 1.41 and 1.26 in one, two and three dimensions. Economy's idealised
    value (if e^(1/D)) is 2.72, 1.65 and 1.40. Close in 2D, where the data spans both; apart in 1D and 3D.
  - the source of the ratio: forced by the geometry for SPN, chosen by optimising for the coding theories.
- **What SPN must not claim.** Its √2 in two dimensions was read *after* knowing 1.42 (`plans/grd-plan.md`, "What is
  already known to me"). The area reading, a level doubling the reader's room, is SPN's to defend in its own terms
  (ISQ's room per level), not something the grid data has shown.

## Where corroboration could come from later

- 3D: module ratios in flying bats, or in any animal mapping a volume. SPN's baseline is 1.26; economy's is 1.40 (to
  verify).
- 1D: a reader with discrete modules over a line, such as time cells or head direction if either is modular. SPN's
  baseline is 2.
- Per-animal ratios from a dataset not seen (`plans/grd-plan.md`). This is a consistency check in 2D, not a test.
- The theory side: whether D.1's "no added measure" can be made precise enough to say how a given measure moves the
  ratio off the baseline. That would let SPN and the coding theories be written in one frame.

## Sources consulted (search results only)

- Wei, Prentice and Balasubramanian, "A principle of economy predicts the functional architecture of grid cells", *eLife*
  2015 (PMC4616244).
- Mathis, Herz and Stemmler, "Optimal population codes for space: grid cells outperform place cells", *Neural
  Computation* 24(9), 2012.
- Kang and Balasubramanian, "A geometric attractor mechanism for self-organization of entorhinal grid modules", *eLife*
  2019.
- Stensola et al., "The entorhinal grid map is discretized", *Nature* 492, 2012.
