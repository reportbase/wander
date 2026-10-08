# Who else works near this

*7 October 2026, by Claude, at Tom's "yes, do that search": is anyone working on problems like these? A first search,
not a survey: the closest neighbours found, what each already has, and where SPN differs. Sources at the end; some
were read only through search summaries (several publisher sites are blocked from this environment), and those are
marked.*

## Short answer

Nobody found here puts the pieces together as SPN does: one relation v/h, read according to what the reader knows,
giving the corner, the flip, the dyadic levels, the horizon and the five situations, and then tested against physics.
But several fields hold large pieces of it, some very close, and two of them already have SPN's exact formulas.

## The closest neighbours

### 1. Visual space with a finite horizon: Gilinsky (1951), Erkelens (2015, 2017)

Gilinsky modelled perceived distance with a finite vanishing point. In Erkelens's restatement, perceived distance
z_v against physical distance z_p is

  z_v = v_d · z_p / (v_d + z_p),

with v_d the finite vanishing distance, inferred at about 30 m or more (search summary of Erkelens 2017).

**This is SPN's normalization by the sum**, v/(v + h) (`plans/normalizations.md`), with h = v_d. Divide by v_d:
z_v/v_d = s/(1 + s), s = z_p/v_d. So perceived distance is proportional near the eye, reaches half the horizon when
the object is at v_d (the corner), and approaches the vanishing distance without arriving (the horizon). Gilinsky's
vanishing distance plays the part of the reader's h, and it is fitted from data, not chosen. This is the strongest
empirical neighbour found: a measured human reading of distance with SPN's corner and horizon in it.

What SPN adds: the reason (a reader knowing one breadth, dividing by it), the flip, the levels past the corner, and
the comparison with the circle's normalization.

### 2. The visual cortex's log-polar map: Schwartz (1977, 1980)

The map from the visual field to primary visual cortex is fitted by w = log(z + a), z the position in the visual
field as a complex number; the cortical magnification is about k/(r + a) at eccentricity r. Near the centre of gaze
(r much less than a) it is close to linear; far out, logarithmic; a is the switch.

**This is SPN's "proportional before the corner, logarithmic past it"**, built into eyes, with a as the corner. It is
R176's lay, measured in anatomy. What SPN adds: the flip (the log-polar map has no reciprocal facing), and the reading
of a as a reader's own unit rather than a fitted constant.

*Added 8 October.* A human fit: magnification M = 17.3/(E + 0.75) mm per degree (Horton and Hoyt 1991, *Arch.
Ophthalmol.* 109:816–824), so cortical distance 17.3 · ln(1 + E/0.75) mm, with a ≈ 0.75°; other fits differ (Engel et al.
1997). Its integral is ln(1 + s) in s = E/a, proportional below s = 1 and logarithmic above: SPN's sweep over the level of
detail (SPN §3.3, "The eye").

### 3. Number lines as proportion judgment: Barth and Paladino (2011)

Children's number-line placements, long read as a shift from logarithmic to linear (Siegler; Dehaene), are fitted
better by cyclic power models of proportion judgment: placement relative to reference points, the endpoints and the
half, accurate there and biased between (search summaries). This bears directly on NLE (`plans/nle-plan.md`), whose
run 1 on Chan and Mazzocco's kindergartners killed the corner's prediction: the proportion account says the
midpoint, ½ of the line, is a reference point, which is the corner of the normalization by the whole line (the sum),
not of the reading by a unit h. Worth a look before any second NLE run, under the lab rules.

### 4. Magnitude as a ratio to the reader's own reference

- **Dehaene and others**: the mental number line compressed logarithmically, Weber's law as constant ratio.
- **Laming, *The Measurement of Sensation* (1997)**: no absolute scale; each judgment is relative to what came before.
- **Petzschner, Glasauer and Stephan (2015)**: a Bayesian account of magnitude estimation, biased toward a prior; one
  framework across loudness, distance and time.

All three hold "magnitude read against the reader's own reference", SPN's h as the focus. None has the corner as a
fixed point of a flip, or a horizon past it.

### 0. The oldest: Mercator's map (1569)

Added 7 October. On the globe at latitude φ, v = sin φ and h = cos φ; Mercator's map divides each circle of latitude by
its h, and its height is y = asinh(v/h) = ln tan(π/4 + φ/2): proportional near the equator, logarithmic past 45°, each
doubling of v/h a near-equal step of ln 2, and the pole a horizon the map never reaches. It is the globe's relation v/h scaled locally by 1/h and accumulated (dividing by h alone is the central cylindrical
projection, y = v/h), the situated normalization, four centuries before the rest of this list (SPN §2.1, "Mercator's map, framed in v and h").

### 5. Geometry of visual space: Luneburg (1947), Heelan (1983)

Luneburg argued binocular visual space is hyperbolic, the infinite rendered as a dome; Heelan, a philosopher of
science, took perception as world-building, with an outer horizon. Both are about the geometry of space as seen from
a standpoint. SPN's horizon and its hyperbola ("The relation forces the logarithm") are neighbours; SPN does not claim
visual space is hyperbolic.

### Further off, already in the corpus

Projective geometry (dividing by h is homogeneous coordinates; the horizon is the point at infinity); wavelets,
constant-Q analysis and hearing scales (`plans/wavelets.md`); the Cauchy distribution as the ratio of two normals
(`plans/normalizations.md`); Nagel's view from nowhere (SPN §2.1, "Situated and unsituated"). Relational accounts in
physics (relational quantum mechanics, symmetry and reference frames) turned up but were not read.

## What this suggests

- **SPN should cite Gilinsky and Schwartz.** Both have its shapes in measured human vision: Gilinsky the corner and the
  horizon (by the sum), Schwartz proportion-then-logarithm (by the unit). Possible correspondences, in the paper's own
  sense: not proofs.
- **A lab could test Gilinsky's law**: a *Wander* reader judging distance with a finite vanishing distance, predicted
  to read half the horizon at the corner. And it could ask which normalization people use: by the sum (Gilinsky,
  Barth) or by the unit (Schwartz's log past a).
- **NLE should meet Barth and Paladino** before any second run.

## Sources

- Erkelens, C. J. (2017). Perspective space as a model for distance and size perception. *i-Perception*.
  https://journals.sagepub.com/doi/10.1177/2041669517735541 (Gilinsky's formula as restated there; read via search)
- Erkelens, C. J. (2015). The extent of visual space inferred from perspective angles. *i-Perception*.
  https://journals.sagepub.com/doi/pdf/10.1068/i0673
- Gilinsky, A. S. (1951). Perceived size and distance in visual space. *Psychological Review* 58.
- Schwartz, E. L. (1977, 1980), the complex-logarithmic model of V1: https://en.wikipedia.org/wiki/Eric_L._Schwartz ;
  https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2015.00003/full
- Barth, H. C. and Paladino, A. M. (2011). The development of numerical estimation: evidence against a representational
  shift. *Developmental Science* 14. Summarised in
  https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.01021/full
- Dehaene, S. (2003). The neural basis of the Weber–Fechner law: a logarithmic mental number line. *Trends in
  Cognitive Sciences* 7. https://homepage.uni-tuebingen.de/andreas.nieder/Dehaene(2003)TICS.pdf
- Laming, D. (1997). *The Measurement of Sensation*. Oxford. https://academic.oup.com/book/8787
- Petzschner, F. H., Glasauer, S. and Stephan, K. E. (2015). A Bayesian perspective on magnitude estimation. *Trends in
  Cognitive Sciences* 19, 285–293. https://www.bccn-munich.de/news/news/a-bayesian-perspective-on-magnitude-estimation-new-paper-by-petzschner-et-al.html
- Luneburg, R. K. (1947). *Mathematical Analysis of Binocular Vision*. Princeton. https://en.wikipedia.org/wiki/Visual_space
- Heelan, P. A. (1983). *Space-Perception and the Philosophy of Science*. University of California Press.
  https://www.ucpress.edu/books/space-perception-and-the-philosophy-of-science/paper
