# JAY: building on Jaynes, the reader's ignorance as a group

*14 October 2026 (Tom's local date). Tom, about 11:18: "It would be nice to find and lean on one paper that well cited
that has overlap with our ideas, and we just build on that." Claude proposed E. T. Jaynes's principle of transformation
groups ("Prior Probabilities", 1968; "The Well-Posed Problem", 1973). Tom, about 11:24: "ok, if we find another great
paper to lean on, we can just add it to Jaynes." (SPN R243.) Exact arithmetic: Python's `fractions` where the numbers
are rational, mpmath at 60 digits elsewhere; predictions written before the script (`runs/jay/jay.py`) exists.*

## What Jaynes proved, and what is still to check against his text

Neither paper could be read in full here: the author's copies (bayes.wustl.edu), PhilArchive, Wikipedia and the Internet
Archive are all refused by this environment's network policy (14 October). What follows is from the papers' published
abstracts, the secondary literature seen as search results, and the standard textbook statements of the results. Each
item marked **(check)** is to be checked against the text once Tom supplies the PDFs; until then OFS cites the results,
not Jaynes's wording.

**Jaynes, E. T. (1968). Prior probabilities. *IEEE Transactions on Systems Science and Cybernetics* SSC-4(3), 227–241,
doi 10.1109/TSSC.1968.300117.**
- The problem (from the abstract): decision theory is not complete until the prior is assigned without arbitrariness.
  Maximum entropy fixes a prior on a discrete space given constraints; on a continuous space entropy needs a measure,
  and the remaining ambiguity is fixed by the group of transformations that leave the problem unchanged.
- The principle: if two problems differ only by a transformation the observer cannot detect, it must assign them the
  same prior. The prior is then a density f with f(x) = f(gx)·|∂(gx)/∂x| for every g in the group: the measure the
  group leaves unchanged (Haar's, where the group acts transitively).
- Location and scale: a sampling law p(x | μ, σ) = φ((x − μ)/σ)/σ, unchanged under μ ↦ μ + b, σ ↦ aσ, gives the prior
  f(μ, σ) ∝ 1/σ: even in μ, even in log σ. This is Jeffreys's prior for a scale (Jeffreys 1939). **(check:** that 1968
  derives exactly this, and the section.)
- An unknown share, "complete ignorance" of a probability θ: unchanged under θ ↦ aθ/(1 − θ + aθ), which multiplies the
  odds θ/(1 − θ) by a, gives f(θ) ∝ 1/(θ(1 − θ)), Haldane's prior (Haldane 1932): even in the log-odds. **(check:** that
  this is in the 1968 paper and not only in the later book, *Probability Theory: The Logic of Science*, 2003, ch. 12.)
- A Poisson rate under a change of time unit: 1/λ. **(check.)**

**Jaynes, E. T. (1973). The well-posed problem. *Foundations of Physics* 3(4), 477–493, doi 10.1007/BF00709116.**
- Bertrand's chord (Bertrand 1889): "a chord drawn at random" in a circle is longer than the inscribed equilateral
  triangle's side with probability 1/3, 1/2 or 1/4 according to how "at random" is read (random endpoints, random
  distance along a radius, random midpoint in the disc).
- Jaynes asks what an experimenter with no skill, who does not know the circle's place or size, would see: straws
  tossed onto a circle drawn on the floor. The answer must be unchanged by turning the circle (rotation), by changing
  its size (scale) and by moving it (translation). Rotation and scale invariance alone give the family
  f(r) = q·r^(q − 2)/(2πR^q) for the chord's midpoint at distance r from the centre (per unit area); translation
  invariance then forces q = 1, f(r) = 1/(2πRr): the chord's distance from the centre even on [0, R], and the
  probability 1/2. **(check:** the family's exact form and the order of the steps.)
- The experiment (from the abstract): "the distribution obtained by invariance under a transformation group is by far
  the most likely to be observed experimentally, since it requires the least skill." Straws tossed at a circle agreed
  with 1/2 and not with 1/3 or 1/4. **(check:** the number of tosses, 128 as remembered, and the test used.)
- The invariant measure on lines that it amounts to is Crofton's (1868), dp·dφ for the line at distance p and angle φ:
  classical integral geometry (Santaló 1976).

**The objections.** Drory (2015) shows that each of Bertrand's three answers (and others) follows from the same
symmetries imposed in different ways, according to how the random selection is made; OFS already grants this (§11.2,
question 2): which selection is made is a choice, and the median at the corner survives it. A 2018 experiment
(arXiv 1806.00308, seen as a search result only, not read) is reported to find practical tosses giving answers between 0
and 1/2. Neither touches what we take from Jaynes: the method (state the ignorance as a group, use the measure it leaves
unchanged), not the claim that one physical selection is forced.

## What we take, and what we add

The method is Jaynes's. Applied to a situated reader, its ignorance has two unknowns and three transformations:
- its own **attitude** θ, which way its bar points (a place on the circle): unknown up to a **turn**;
- the other party's **size** κ = V*/H (a scale): unknown up to a **rescaling**;
- **which party is which**: the **exchange**, θ ↦ 90° − θ and κ ↦ 1/κ.

This is Jaynes's location–scale problem with the location on a circle. What the run is to check is that the measures
these leave unchanged are the corpus's: the even turn and its Cauchy (OFS Propositions 5, 7.1), the logarithm past the
corner (Proposition 4, premise (S)), the corner (Proposition 1) and the drawing V = H with the median as the best size
(Propositions 3(e), 13). What is not Jaynes's:
- *the reader's group*: that a situated reader's ignorance is these three, and that being situated removes the
  translations Jaynes's straw-thrower keeps (P5, P6); chosen as a statement of ignorance, not derived (OFS §11.1);
- *the corner*: the near field, where the reader holds H, is laid in proportion, and the two lays meet at the
  exchange's fixed point; a scale prior alone has no corner;
- *the address reading*: the measure fixed by the group is the reader's addresses, not its payload (OFS §7).

## Predictions

- **P1. Rescaling fixes the levels, and on a share it is Haldane's prior.** (a) The only densities on (0, ∞) with
  f(x) = λ·f(λx) for every λ > 0 are c/x (one line: put λ = 1/x); of the candidates 1/x, 1/x², x^(−1/2),
  1/(1 + x²), 1/(1 + x)² and e^(−x), only 1/x passes at 200 rational pairs (x, λ), exactly. (b) Under c/x every level
  [2^k, 2^(k + 1)] carries c·ln 2, for k = −30 … 30: the levels past the corner are equal (the reader's lay, 1 + ln s).
  (c) On the share t = s/(1 + s) the rescaling of s acts as t ↦ λt/(1 − t + λt), and the density it leaves unchanged
  is 1/(t(1 − t)), Haldane's; the change of variables carries ds/s to dt/(t(1 − t)) exactly. **Killed if** any
  candidate other than 1/x passes, or 1/x fails, at any of the 200 rational pairs; or a level's mass differs from ln 2
  by more than 1e-50; or Haldane's density fails the invariance, or the change of variables, exactly at 200 rational
  (t, λ).
- **P2. Turns fix the even turn, the Cauchy at the point i, and on the chord Jeffreys's prior.** Write a Cauchy law
  with median m and scale γ as the point z = m + iγ of the upper half-plane (McCullagh 1996). (a) A turn of the bar by
  α acts on the reading x = v/h as the Möbius map x ↦ (x cos α + sin α)/(cos α − x sin α); for 50 random maps g of
  determinant > 0 and 50 random z, the law of g(X), X ~ Cauchy(z), is Cauchy(g(z)) at 20 points each; for the exchange
  x ↦ 1/x (determinant < 0) it is Cauchy at the mirror of g(z), 1/z̄. (b) Every turn fixes i and only i; the exchange
  fixes i; a rescaling by λ sends i to λi. So among Cauchy laws the even turn's, Cauchy(0, 1), is the only one every
  turn and the exchange leave alone; on the quarter turn it is the half-Cauchy 2/(π(1 + s²)), median 1. (c) The foot
  of the arc point on the chord (Euclid VI.8, THL P2) divides it h² : v²; under the even turn the share t = h² follows
  the arcsine law, 1/(π√(t(1 − t))), which is Jeffreys's prior for a share (Jeffreys 1946: the square root of the
  Fisher information 1/(t(1 − t))); the Fisher–Rao length from t = 1 to t = cos²θ is 2θ, the facing. (d) With three
  unit relations, the even octant's squares (h², v², v₂²) follow Dirichlet(½, ½, ½), Jeffreys's prior for three shares:
  every mixed moment E[h^(2a) v^(2b) v₂^(2c)], a, b, c ≤ 4, from the octant's area element cos a da dz equals the
  Dirichlet moment. **Killed if** any pushforward density in (a) differs from the predicted Cauchy's by more than 1e-45
  relative; any turn moves i by more than 1e-50 or fixes a sampled z ≠ i; the arcsine CDF differs from the even turn's
  at 2,000 points by more than 1e-50; the Fisher–Rao length differs from 2θ by more than 1e-40; or any moment in (d)
  differs by more than 1e-40 relative.
- **P3. The exchange fixes the corner and the median, not the law.** (a) On (0, ∞) the exchange s ↦ 1/s fixes only
  s = 1; on the share t ↦ 1 − t only t = ½. (b) The three classical priors for a share are each unchanged by the
  exchange and each has its median at ½ (Haldane's, improper, on every symmetric range [1/K, K] of s): Bayes and
  Laplace's even share (the line h + v = 1 swept evenly), Jeffreys's arcsine (the arc's foot), Haldane's (the levels).
  Read as s = v/h they are 1/(1 + s)², 2/(π(1 + s²)) after a change of variable (the even turn read as v/h is the
  half-Cauchy; its law on the foot is the arcsine), and 1/s, each with f(s) = f(1/s)/s². (c) They differ: at t = ¼
  their shares below are ¼, ⅓ and, on [1/K, K] with K = 1000 in s, 0.4205 (to four places). **Killed if** any of the
  three fails the exchange exactly at 200 rational points (the arcsine through its CDF, at 60 digits, to 1e-50); any
  median is off ½ by more than 1e-50; or the three shares below t = ¼ do not differ.
- **P4. Turn and rescaling together give the location–scale prior; the exchange fixes the corner and the drawing; the
  median in levels is Proposition 13.** (a) On (θ, κ), θ on the circle and κ > 0, the measure dθ·dκ/κ is unchanged by
  every turn, every rescaling and the exchange (θ, κ) ↦ (90° − θ, 1/κ), exactly (Jacobians at 200 rational points, θ
  in turns). (b) The exchange's fixed points are θ = 45° (the corner) and κ = 1 (the drawing V = H). (c) Restricted to
  bounds V₋ ≤ V* ≤ V₊, the median of dκ/κ is κ = √(V₋V₊)/H, the corner of the bounds, Proposition 13(a); with bounds
  symmetric about H, κ = 1, Proposition 13(c). **Killed if** any Jacobian fails exactly; or, for 100 random bounds
  over 10⁻⁶ … 10⁶, the median found by quadrature differs from √(V₋V₊) by more than 1e-45 relative.
- **P5. Jaynes 1973 rederived, and the situated reader's version.** (a) Crofton's measure on lines, dp·dφ: for a
  circle of radius R centred anywhere, the lines that cut it have their distance r from its centre even on [0, R] (for
  each φ the cutting p form an interval of length 2R, whatever the centre), so a chord is longer than √3·R with
  probability ½. (b) The family q·r^(q − 2)/(2πR^q) is normalized for every q > 0, keeps its form when restricted to a
  concentric circle of radius aR (scale), and gives P(r < R/2) = 2^(−q): q = 1 gives ½ (radius, Jaynes), q = 2 gives
  ¼ (midpoint); the random-endpoint law, density proportional to 1/√(R² − r²) in r, gives ⅓ and is in no member of the
  family. (c) A situated reader at home, distance D from the centre, sweeping its rays evenly: the share of rays
  cutting the circle that make a chord longer than √3·R is asin(R/(2D))/asin(R/D) for D ≥ R: ⅓ from a home on the
  circle (Bertrand's endpoints, since the rays from a point on the circle are the chords from one endpoint), rising
  toward ½ as D/R grows (its pencil turning parallel: Jaynes's answer is the situated reader's from far off), a
  function of R/D alone. **Killed if** (a) fails at 50 rational centres and radii exactly; a normalization or
  restriction in (b) is off by more than 1e-50, or the endpoint law fits any q to 1e-6 at three radii; or in (c) the
  value at D = R is not ⅓ to 1e-50, it does not increase with D at 200 values, or at D = 10⁸R it is off ½ by more
  than 1e-15, or a seeded count of 10⁶ even rays at D = 2R differs from the closed form by more than 4 standard errors.
- **P6. Being situated removes the translations: the reader's measure is log-polar.** The similarity transformations
  that keep home fixed are the turns and dilations about it, z ↦ az for complex a ≠ 0. The measure they leave
  unchanged on the plane less home is dx·dy/(x² + y²) = dθ·dr/r: even in direction and even in levels of distance,
  P4's measure on the plane. Area dx·dy, the straw-thrower's (no place preferred), is unchanged by translations and
  turns and multiplied by |a|² under a dilation: it is not the situated reader's, and the two differ by the factor
  1/r². **Killed if** dx·dy/(x² + y²) fails the invariance exactly (Jacobian |a|² against |az|²/|z|²) at 200 complex
  rational (z, a); or area passes it for any a with |a| ≠ 1.
- **P7. The drawings lie on a line of the hyperbolic plane, and levels are its distance.** The even turn of a bar drawn
  at V = cH gives readings Cauchy(0, c), the point ci; V = H is i. Under the distance of the upper half-plane,
  arccosh(1 + |z − w|²/(2·Im z·Im w)), the distance from i to ci is |ln c|, so the number of levels between the drawing
  and a size c is the distance over ln 2; and this distance is unchanged by every Möbius map of determinant > 0 and by
  the exchange (z ↦ 1/z̄). So if the error of a size estimate is to be measured by a distance the reader's group leaves
  unchanged, it is in levels (Proposition 13's premise; the uniqueness of that distance, up to a constant factor, is
  classical: Beardon 1983). **Killed if** the readings' CDF at c differs from Cauchy(0, c)'s at 2,000 points by more
  than 1e-50, the distance from i to ci from |ln c| by more than 1e-50 for 200 c over 10⁻⁹ … 10⁹, or any of 100
  random maps changes the distance of 100 random pairs by more than 1e-40 relative.

## What the run would and would not show

All seven are classical: Haar's measures, Möbius's action on the Cauchy family, Jeffreys's and Haldane's priors,
Crofton's measure, the hyperbolic plane. The run checks that the corpus's lay, sweep, corner and best estimate are, as
stated, the measures Jaynes's method gives for the stated ignorance, with no slip in the bookkeeping. It does not show
that a situated reader's ignorance is exactly these three transformations; that stays a choice (OFS §11.1). It does not
read Jaynes's text; the items marked (check) wait for it.

## Runs

### Run 1 (14 October; `python3 runs/jay/jay.py`, about 4 minutes)

```
P1: not killed. invariant candidates: ['1/x']; worst level mass - ln 2: 0.0; Haldane invariant and ds/s = dt/(t(1-t)) exactly: True
P2: KILLED. pushforward = Cauchy(g(z)) to 7.78e-61; turns move i by 0.0, least move of z != i 0.124; arcsine = even turn's foot to 3.67e-33; Fisher-Rao length - 2θ 1.15e-32; octant moments = Dirichlet(½,½,½) to 3.11e-61
P3: not killed. fixed point only at 1; f(s) = f(1/s)/s² exactly for the line, the turn, the levels: True; arcsine symmetric to 7.78e-61; medians at ½; below t = ¼: 0.25, 0.3333, 0.4205
P4: not killed. dθ·dκ/κ unchanged by turns, rescalings and the exchange, exactly: True; fixed point (45°, κ = 1); median of dκ/κ on bounds = √(V₋V₊) to 3.89e-61
P5: KILLED. Crofton: ½ at every centre and radius, exactly: True; the family normalized and kept under scale, 2^-q, to 4.54e-20; endpoints ⅓ (0.333333), fits a power: False; situated: ⅓ on the circle (3.89e-62 off), rising: True, ½ − 6.25e-18 at 10⁸R, 0.482584 at D = 2R (counted 0.48254 ± 0.00087)
P6: not killed. dx·dy/(x²+y²) unchanged by every z -> az, exactly: True; area passes for some |a| ≠ 1: False
P7: not killed. readings at V = cH Cauchy(0, c) to 6.25e-56; distance i to ci = |ln c| to 2.49e-60; kept by maps and the exchange to 8.25e-59
```

P2 and P5 killed, both by my set-up, not by the mathematics: each fell short where a quadrature met a density with an
algebraic singularity at an end of its range, which mpmath's tanh-sinh rule at the working precision of 60 digits
resolves only to about 10⁻³³ (the arcsine, 1/√(u(1 − u))) and 10⁻²⁰ (the family's q·r^(q − 1) at q = 0.3, whose
r^(−0.7) is the steepest). Found after the run: the other clauses of P2 and P5 passed, and every other value of q passed
to 10⁻⁶¹. The Fisher–Rao length also integrated toward the singular end 1 from an interval that shrinks onto it as θ → 0.
Tried after the run, before any new prediction: at 150 working digits the arcsine's shortfall falls to 4 × 10⁻⁷⁸, at
200 the family's to 5 × 10⁻⁶²; reflecting the Fisher–Rao integral by w = 1 − u (the integrand is symmetric) puts the
singular end at 0, 10⁻¹⁰⁴ at 200 digits.

**Predictions for run 2**, the claims and bounds of P2 and P5 unchanged, the method changed:
- **P2′.** As P2, with the arcsine's CDF and the Fisher–Rao length integrated at 200 working digits (the comparison at
  60), and the Fisher–Rao length from t = 1 to cos²θ computed as ∫ from 0 to sin²θ of dw/√(w(1 − w)) (the reflection
  w = 1 − u). **Killed if** any clause of P2 fails at its bound.
- **P5′.** As P5, with every quadrature of the family q·r^(q − 2)/(2πR^q) and of the endpoint law at 200 working digits.
  **Killed if** any clause of P5 fails at its bound.
P1, P3, P4, P6 and P7 are not rerun as new predictions; run 2 repeats them unchanged.

### Run 2 (14 October; `python3 runs/jay/jay.py`, 6.5 minutes on three cores)

```
P1: not killed. invariant candidates: ['1/x']; worst level mass - ln 2: 0.0; Haldane invariant and ds/s = dt/(t(1-t)) exactly: True
P2: not killed. pushforward = Cauchy(g(z)) to 7.78e-61; turns move i by 0.0, least move of z != i 0.124; arcsine = even turn's foot to 5.81e-61; Fisher-Rao length - 2θ 9.57e-60; octant moments = Dirichlet(½,½,½) to 3.11e-61
P3: not killed. fixed point only at 1; f(s) = f(1/s)/s² exactly for the line, the turn, the levels: True; arcsine symmetric to 7.78e-61; medians at ½; below t = ¼: 0.25, 0.3333, 0.4205
P4: not killed. dθ·dκ/κ unchanged by turns, rescalings and the exchange, exactly: True; fixed point (45°, κ = 1); median of dκ/κ on bounds = √(V₋V₊) to 3.89e-61
P5: not killed. Crofton: ½ at every centre and radius, exactly: True; the family normalized and kept under scale, 2^-q, to 2.33e-61; endpoints ⅓ (0.333333), fits a power: False; situated: ⅓ on the circle (3.89e-62 off), rising: True, ½ − 6.25e-18 at 10⁸R, 0.482584 at D = 2R (counted 0.48254 ± 0.00087)
P6: not killed. dx·dy/(x²+y²) unchanged by every z -> az, exactly: True; area passes for some |a| ≠ 1: False
P7: not killed. readings at V = cH Cauchy(0, c) to 6.25e-56; distance i to ci = |ln c| to 2.49e-60; kept by maps and the exchange to 8.25e-59
```

P2′ and P5′ not killed; P1, P3, P4, P6 and P7 as in run 1, to the digit. Notes:
- Two attempts before this one gave no verdict and are not runs. The first was stopped by my own 15-minute limit on the
  command, before anything printed. The second ran the 2,000 arcsine quadratures on four cores and a worker was killed
  for memory: mpmath keeps the nodes of every interval it integrates over, and at 200 digits 2,000 intervals took
  about 14 GB (one process reached it; the test run beside it lost its browser page the same way). The script now drops
  each interval's nodes after use and keeps the standard ones; memory stays near 35 MB a process. The rule, the
  precision and the comparisons are unchanged.
- P5's far value, ½ − 6.25 × 10⁻¹⁸ at D = 10⁸R, is the closed form's own approach to ½, from below by R²/(16D²) to
  leading order, within the 10⁻¹⁵ bound; not rounding.

**What it shows.** The measures Jaynes's method gives for a situated reader's stated ignorance are the corpus's: a
rescaling of the other's size fixes 1/x, every level alike, and on a share Haldane's prior; a turn fixes the even
turn, the Cauchy law at the one point i of the upper half-plane that every turn and the exchange leave, and read at
the arc's foot on the chord Jeffreys's prior, the Fisher–Rao length being the facing; the exchange fixes the corner and
the median, not the law; together, turn and rescaling give Jaynes's location and scale on a circle, dθ·dκ/κ, with the
median of any bounds at their corner, Proposition 13's estimate. Jaynes's ½ for Bertrand's chord is Crofton's measure;
read from home the same question gives arcsin(R/2D)/arcsin(R/D), Bertrand's ⅓ from a home on the circle rising toward
½ as the circle recedes; and the measure that keeps home fixed is log-polar, not area. The drawings V = cH lie on a
line of the hyperbolic plane, levels its distance. All classical; what is checked is the bookkeeping that makes them
the corpus's lay, sweep, corner and estimate. That a situated reader's ignorance is exactly this group stays a choice.

### Jaynes's text, read (14 October, after run 1)

The papers could not be fetched at first: their hosts were outside the cloud environment's network access, which was the
default setting, Trusted (GitHub and the package registries only), not a rule of Tom's. Tom set it to Full (about 12:06,
"done"), and both papers were then read in full from the author's copies at bayes.wustl.edu (Jaynes's own retyped
versions; not committed): `prior.pdf`, 10 pages, sha256 d1e8bfbce2321146ce78d862abe7a7aaca6aa6e42bc9a32b77ddac718bbc8cfd;
`well.pdf`, 10 pages, sha256 7b792e23c2ccbd39a8d40eff0c72e62576216de9e5bfe927550d06f413abe5cd. The items marked
(check) above, item by item; the text above the "Runs" line is left as written.

**1968, "Prior Probabilities".**
- *Location and scale* (§VII, eqs. 47–54): the group μ′ = μ + b, σ′ = aσ; the functional equation
  f(μ, σ) = a·f(μ + b, aσ); its solution const/σ, "which is the Jeffreys rule". Stands.
- *A rate* (eqs. 55–58): two observers whose watches run at different rates; f(λ) = q·f(qλ); the prior dλ/λ. Stands.
- *An unknown share* (eqs. 59–68): "a large population of individuals who hold varying beliefs about the probability of
  success", all given one more piece of evidence E; Bayes's theorem maps each belief θ to θ′ = aθ/(1 − θ + aθ) (62),
  a = p(E | SX)/p(E | FX), so every belief's odds are multiplied by a; "total confusion" is the population unchanged by
  it; the solution f(θ) = const/(θ(1 − θ)) (68), "which has the qualitative property anticipated by Jeffreys". It is in
  the 1968 paper, not only the later book. Jaynes does not name Haldane; the name is ours (Haldane 1932). With r
  successes in n trials the posterior mean is r/n, and the Bayes–Laplace uniform prior is the posterior after one
  success and one failure. Stands.
- *The discussion* (headed "VII" a second time in this copy, between VII and IX): when the group has as many parameters
  as the problem, the group's "fundamental domain … reduces to a point and the form of the prior is uniquely
  determined"; with the change of scale alone, f = k(μ)/σ, k arbitrary. The principle is "indifference between problems,
  rather than indifference between events". The group's measures cannot be normalized: "The pre-prior distribution
  resulting from a transformation group does not strictly represent any realistic state of knowledge, but it does
  define the invariant measure for our parameter space." Bertrand is mentioned: invariance under infinitesimal
  displacements of the circle "uniquely determines the solution", the proof deferred to 1973.

**1973, "The Well-Posed Problem".**
- *The three answers* (§1): uniform density of (A) the distance between the centres of chord and circle, ½; (B) the
  angles of intersection on the circumference, ⅓; (C) the chord's centre over the area, ¼. Ten authors' views are
  quoted in an appendix. The invariant measure on lines is credited to Poincaré (1912) and Kendall and Moran (1963), the
  density (u² + v²)^(−3/2) for the line ux + vy = 1: Crofton's measure in those coordinates.
- *Rotation* (§2): "the statement of the problem does not specify whether the observer is facing north or east"; so
  f(r, θ) = f(r). Rotational symmetry is "irrelevant to the distribution of chord lengths".
- *Scale* (§3): a concentric circle of radius aR; the functional equation (6); its normalized solutions
  f(r) = q·r^(q − 2)/(2πR^q) (7), q > 0 not fixed by scale. B is eliminated: it "could be true for, at most, only one
  size of circle"; A (q = 1) and C (q = 2) remain. Stands, the form and the order of steps as the plan had them.
- *Translation* (§4–5): two equal circles a distance b apart; equal probabilities for corresponding regions if and only
  if q = 1; f(r, θ) = 1/(2πRr) (12); the chord-length law x dx/√(1 − x²), x = L/2R (13), Borel's conjecture (1909).
  Jaynes adds that translation alone already fixes (12): scale "was not really necessary".
- *Frequency correspondence and the experiment* (§6): any rain of straws that does not give (13) gives different
  distributions on different circles, so (13) is what a tosser whose "region of uncertainty" is large compared with the
  circle will see. Jaynes and Charles E. Tyler tossed broom straws from a standing position onto a 5-inch circle drawn
  on the floor; in ten categories of chord length, "128 successful tosses confirmed Eq. (13) with an embarrassingly low
  value of chi-squared". Stands (128).
- *Conjectures* (§8): von Mises's water and wine is "overdetermined": "so many things are left unspecified that the
  invariance group is too large, and no solution can conform to it".

**One correction to the plan's sources.** The 2018 experiment is Liu and Adams, "Experimental tests of Bertrand's
question and the Duhem–Quine problem" (arXiv 1806.00308, abstract read through arXiv's API): the answer depends on the
ratio of the circle's diameter to the straw's length, 2R/L, and Jaynes's ½ (the case they identify with Laplace's
principle of indifference) is reached only in the limit 2R/L → 0, straws of unbounded length; they see a systematic
discrepancy near 2R/L → 1. Not "answers between 0 and ½", as the plan had it from a search result.

**What the reading changes in the papers** (Claude's, unruled):
- Jaynes's rotation is already an observer's facing; the reader's turn is its bar's attitude.
- His group measure is a "pre-prior", the invariant measure a prior is built on, not a state of knowledge. That is
  nearer the corpus's addresses than the plan's "a distribution of belief"; OFS §2 now says so.
- A group with more parameters than the problem leaves it overdetermined. The turns and rescalings, acting on the
  reading alone, generate PSL(2,ℝ), under which no probability on readings is unchanged; acting on the two unknowns,
  attitude and size, they are as many as the problem and fix dθ·dκ/κ (OFS §11.1).
- Liu and Adams's answer depends on a pair of lengths (2R, L) as P5(c)'s does on (R, D), and in both Jaynes's ½ is a
  limit: unbounded straws, a circle far off.
- Von Mises's water and wine is a ratio of two parties. With bounds on the ratio, the exchange and rescaling give dκ/κ
  on them and the median at the bounds' corner, Proposition 13's estimate (for wine to water between 1 and 3, √3);
  Jaynes left it open. Not tested here; whether others have resolved it this way is to check.

### Since 1973, and run 3 (14 October)

Tom, about 12:18: "its a pretty old paper, what has happend since then?" Then, to Claude's answer and its three
suggestions (cite Norton beside the pre-prior; note that the reader's group commutes, so the left and right Haar
measures agree; cite Liu and Adams beside the situated Bertrand), about 12:26: "ok, proceed" (SPN R244).

**What has happened since, as checked here.** Citation counts from OpenAlex (14 October): 1968, 1,749; 1973, 292.
- *Objective Bayes went on by other rules, and met the group where there is one.* Reference priors (Bernardo 1979;
  formally defined by Berger, Bernardo and Sun 2009, *Annals of Statistics* 37(2), 905–938) and Jeffreys's rule became
  the standard. For location and scale the left- and right-invariant Haar priors are σ⁻² and σ⁻¹; Jeffreys's general
  rule gives the left, Jaynes's group argument the right; the right one is Bernardo's reference prior when either
  parameter is of interest and gives exact frequentist coverage (Datta, Ghosh and Mukerjee 2000), and "usually enjoys
  more optimality properties" (Ghosh 2011, *Statistical Science* 26(2), 187–202, §5, read in full through arXiv).
- *Improper priors.* Dawid, Stone and Zidek (1973), "Marginalization paradoxes in Bayesian and structural inference",
  among the most cited works citing the 1973 paper (Semantic Scholar's list); Jaynes replied in 1980. Not read here.
- *Bertrand.* Shackel (2007, *Philosophy of Science*) concludes, testing Marinoff's and Jaynes's resolutions, that the
  paradox "continues to stand in refutation of the principle of indifference" (abstract); Drory (2015) as OFS has it;
  Liu and Adams (2019, *European Journal of Physics* 40(6), 065801; arXiv 1806.00308): the answer depends on 2R/L.
- *Ignorance is not a probability.* Norton (2008), "Ignorance and Indifference", *Philosophy of Science* 75(1), 45–68
  (abstract read through Crossref): "The epistemic state of complete ignorance is not a probability distribution";
  indifference and the invariance of ignorance under redescription are "so innocuous as almost to be platitudes", and
  generate paradoxes only "when conjoined with the assumption that an epistemic state must be a probability
  distribution".
- From memory, not checked: Shore and Johnson's axioms for maximum entropy (1980); Amari's information geometry, where
  Jeffreys's prior is the volume of the Fisher–Rao metric; Jaynes's book (2003), ch. 12.

**Prediction for run 3** (`runs/jay/jay2.py`, written before the script):
- **P8. The reader's group has one Haar measure; location and scale have two.** (a) The maps x ↦ ax + b (a > 0),
  composed (a₁, b₁)(a₂, b₂) = (a₁a₂, a₁b₂ + b₁): the density on (a, b) unchanged by every left multiplication is 1/a²,
  by every right multiplication 1/a (Jacobians a_h² and a_h), and the two differ. (b) Turns and rescalings,
  (α, λ)(α′, λ′) = (α + α′, λλ′), commute, and the densities unchanged by left and by right multiplication are both 1/λ;
  the exchange, (α, λ) ↦ (−α, 1/λ), carries 1/λ to itself, so the group with the exchange added has the one measure
  too (a group of two cannot make it lopsided). **Killed if** any of these Jacobian identities fails exactly at 200
  rational group elements; or, in (a), 1/a² passes the right test or 1/a the left at any element with a ≠ 1; or, in
  (b), any product fails to commute.

### Run 3 (14 October; `python3 runs/jay/jay2.py`, instant)

```
P8: not killed. location and scale: left 1/a², right 1/a, exactly, and never each other's: True; turns and rescalings commute, left = right = 1/λ, the exchange keeps it, exactly: True
```

**What it shows.** Classical (an abelian group is unimodular, and so is a finite extension of one): the question that
has followed Jaynes's location and scale since, which of its two invariant measures to use, does not arise for the
situated reader's group. Its one measure, dθ·dκ/κ, is what both readings give. Made: OFS §2 (the commuting group,
Ghosh 2011; Norton beside the pre-prior; Liu and Adams beside the situated Bertrand), three references.

### Correction (14 October, after review 9)

An outside read (`plans/ofs-review-9.md`, SPN R247) found that the reading above ran two groups together, and three
sizes. The runs stand; these readings are corrected:
- The reader's ignorance group (turns of θ, rescalings of κ) and the Möbius action on readings (turns and changes of the
  drawing, PSL(2,ℝ)) are different groups. κ touches no reading. P6 and P7's hyperbolic line belong to the second; the
  drawing V = cH is c, required to be 1, not an unknown; P4's dθ·dκ/κ belongs to the first.
- The exchange acts on readings and drawings (v ↔ h); κ ↦ 1/κ is not an exchange of what the reader knows (it holds H,
  not V*), but a separate premise of symmetric ignorance used for the estimate (Proposition 13(c)).
- The levels' error measure (P7) applies to the estimate ĉ through amounts: the even turn of the true bar is the Cauchy
  law at iκ in amounts, the estimate's at iĉ, the distance |ln(κ/ĉ)|; invariance gives a function of it, not a unique
  error, and the median needs absolute loss.
- "Since 1973" said "Jaynes's group argument the right": his own group (1968, eq. 49) commutes, and its measure
  coincides with the right-invariant measure of the location-and-scale family's affine group, which is the
  non-commuting one. P8 checked the affine group, correctly so named in its own text.
