# Parallax from the corner

*Started 12 October 2026, at Tom's word: "put it in a parallax paper and lets iterate there." A working paper: a reading,
revised as it is worked over, not a ruling. It gathers what the corpus has on parallax and says what each piece stands on:
SPN Proposition 9.6 (parallax as two situated directions and the reader's own travel), COR's "parallax against the grain"
(SPN §3), MOT P6–P7, LAD and the ladder, STC, and PXC runs 1–3 (`plans/pxc-plan.md`). `parallax.html` and `ladder.html`
show it. The rules are `papers/physics.md` §0: evidence is real data or exact arithmetic, predictions come first, keep the
case and name the bridge. A result goes into SPN only once it has been tested and ruled. For an evening it stood in
`observation-from-somewhere.md` as Proposition 11(d) (SPN R218); it was taken out to here (R219), and that paper keeps
Proposition 11(a)–(c), which this paper builds on.*

**Iterations**

- 12 October, first: the paper started from PXC runs 1–3. Three corrections to what had stood in
  `observation-from-somewhere.md` and `parallax.html`, found while asking whether it belonged there:
  - the depth error grows as cosh of the levels from the corner (1, 1.25, 2.125, 4.06, 8.03), about doubling per level
    only far off, not "doubling with each level away";
  - the corner is where the **depth** is read best, and only **on the bisector**. Across the line of sight the error
    keeps falling with distance; both together are least at d = √2·(B/2); off the bisector the circle is not the best
    place (§4);
  - the stars' presets were off by 2: published parallax precisions are for p = γ/2, so the step in γ is twice the
    quoted one, and Hipparcos's band ends near 1 kpc, Gaia's near 50 kpc (§5).
- 13 October: worked back from what parallax already knows (§6; Tom: "seems to me that we should be able to work
  backwards from known results of paralax and show the forced logical chain of logic"; PXC run 4, nothing killed). The
  astronomers' rule σ_d/d = σ_p/p is the far-field limit of γ/sin γ, the outer reading of the parallax angle, π/2 on the
  Thales circle; "best when square" is the flip's fixed point; the round error needs the two standpoints alike;
  inverting a noisy parallax keeps its median and loses its mean; the parsec is a far-field unit.
- 13 October, later (Tom: "can parallax be used to illustrate PI/2 * 2/PI = 1"): yes, with step 3 of §6, and one thing
  made explicit there: the turn in γ/sin γ is the pair's facing, twice its sweep angle, so its π/2 falls at the pair's
  corner, where on the thumb (`observation-from-somewhere.md` §10, step 3) it falls at the sweep's horizon. The same
  identity on two different angles.

**Standing marks.** Each claim carries one:
- **[classical]**: established outside this corpus (geometry, surveying, stereo vision, astrometry), quoted;
- **[exact]**: exact arithmetic, checked in a plan;
- **[data]**: measured on published data, in a plan;
- **[simulation]**: a simulation of our own, checked against a full referee, in a plan;
- **[reading]**: Claude's reading, unruled;
- **[illustration]**: a page or rounded published figures, which show and do not test.

**Keep the case.** B (the baseline), d (a distance), r₁ and r₂ (distances from the two standpoints) and ε (the step to
which a direction is read, in radians) are amounts. k = (B/2)/d is a ratio of two amounts, a pure number. Its corner, k = 1,
is the corner of the pair (half-baseline, distance), set by amounts; it is not the reader's own h = v. Where this paper says
"the corner", it names the pair. Laying the plane with H at the half-baseline (as `parallax.html` does) puts the two corners
together; they are still corners of different pairs.

**Conventions.**
- γ is the angle the baseline subtends at the place: the full parallax angle, and for two eyes the angle of convergence.
- Astronomy's annual parallax p is half of it, p = γ/2, the angle that half the baseline (1 AU) subtends. Published
  precisions are for p, so the step in γ is twice the quoted one.
- ε is the step in γ. In PXC runs 1–2 each direction is off by ε/√2, so γ is off by ε. In run 3 each direction is off by
  σ, so γ is off by σ√2.
- A level is a doubling of d. j levels from the corner means k = 2^(±j).

## 0. Known already: what this paper is, and is not

Parallax is among the oldest measurements there is, and nearly everything below has a standing counterpart:
- **Triangulation** (Snellius 1617): two directions and one measured length fix a place, and a chain of triangles carries
  the length. **[classical]**
- **The inscribed angle** (Euclid, *Elements* III.31): the places from which a segment is seen at a right angle are the
  circle on it as diameter, the Thales circle. **[classical]**
- **Strength of figure** (surveying): an intersection is best conditioned near a right angle and degrades as 1/sin γ; the
  error of an intersection is an ellipse, from the two lines' displacements (Ghilani 2010). **[classical]**
- **Stereo depth error** (computer vision): far off, the depth error grows as d²·ε/B (Hartley and Zisserman 2003).
  **[classical]**
- **Stellar parallax** (astrometry): p in arcseconds is 1/d in parsecs. Hipparcos measured p to about 1 mas (Perryman
  et al. 1997) and Gaia to tens of µas (Gaia Collaboration 2016). A small common offset in p, the zero-point, is
  measured and corrected (Lindegren et al. 2021). **[classical]**

So this paper is, like `inverse-square.md`, a **calibration case**: a translation into SPN's terms (the pair, its corner,
the facing, the bell, levels, the band), not a discovery. What the translation adds is a reading:
- parallax has a corner of its own;
- its depth precision across levels is the even turn's bell, for a stated reason (§3);
- the error splits into the depth, which parallax adds and which has the corner, and the direction, which one standpoint
  already holds (§4);
- the step sets a band of levels about the corner, and the baseline places the band as H places a reader's window (§5).

A result here that looks new should first be looked for in surveying's adjustment computations and in stereo vision.

## 1. The setting

Two standpoints S₁ and S₂, a baseline B apart, each read only directions; r₁ and r₂ are a place's distances from them.
The place read is at distance d from the baseline's middle. On the perpendicular bisector:
- **the pair** is (half-baseline, distance), with reading k = (B/2)/d;
- **the angle** γ that the baseline subtends satisfies tan(γ/2) = k;
- so **γ/2 is the sweep angle θ of the pair**, tan θ = k, and **γ = 2θ is the pair's facing** (SPN §1, "The line, the arc
  and the facing"; `facing.html`). **[exact]**, by definition;
- **the corner**, k = 1, is θ = 45° and γ = 90°: d = B/2, the top of the Thales circle. Inside the circle (γ > 90°) is
  parallax's near field, outside it the far field. **[classical]** for the circle, **[reading]** for near and far.

## 2. Why parallax and situated observation are both needed

- **One standpoint reads directions only.** Scaling the world leaves every reading unchanged
  (`observation-from-somewhere.md` Proposition 8(a)), so a standpoint holds the figure's directions and its order of
  turn but no distance: for each place, a line through it (Proposition 11(a)). **[classical]**
- **Parallax is the difference of two such readings, and one amount.** Two standpoints placed relative to each other up
  to scale fix every place both see, up to one common scale (Proposition 11(b)); one agreed length, B, fixes the scale
  (11(c)). The right side of SPN Proposition 9.6 is addresses alone; B is the bridge. **[classical]**
- **Neither alone gives distance.** Without the readings there is nothing to difference; without B nothing fixes the
  scale. **[classical]**
- **Past its band, parallax returns to situated observation.** There the two directions differ by less than a step, and a
  triangulated place is a ray again: what one standpoint holds alone (§5). **[exact]** (PXC P3), **[reading]** for the
  words.
- **A serial reader makes its own baseline by moving.** It reads, travels a known length, and reads again. To difference
  the two readings it must hold the first: order needs holding (`observation-from-somewhere.md` §7.6; draw's `ref` lab).
  The travel is the one amount (`flight.html`'s posts). **[reading]**

## 3. Depth across levels: the bell

**Proposition 1 (the depth's precision).** On the bisector the relative error in d per unit error in γ is
|d ln d/dγ| = 1/sin γ = cosh(ln k), and the precision of one reading of γ is sin γ = sech(ln k). **[exact]** (PXC P1, P2:
to 9.9e-43 from k = 2⁻³⁰ to 2³⁰, by complex step through d(γ) = (B/2)/tan(γ/2), never from the closed form.)

*Proof.* d = (B/2)/tan(γ/2), so d ln d/dγ = −1/sin γ; with tan(γ/2) = k, sin γ = 2k/(1 + k²) = 1/cosh(ln k). ∎

- **Least at the corner, the same at d and (B/2)²/d.** cosh is even in ln k.
- **Not "doubling per level".** At 0, 1, 2, 3 and 4 levels either side it is 1, 1.25, 2.125, 4.06 and 8.03. The ratio
  from one level to the next is 1.25, 1.7, 1.91, 1.98, tending to 2: far off the depth error is ε·d/B, stereo's d²
  law in relative terms.
- **Why it is the even turn's bell.** With θ = atan k, dθ/d ln k = k/(1 + k²) = ½ sin 2θ = ½ sech(ln k). The parallel
  reader's bell, the even turn's shares on the axis of levels, is ½·sech x = dθ/dx with x = ln k
  (`observation-from-somewhere.md` §7.1); parallax's precision is dγ/dx = 2·dθ/dx = sech x. They are one function
  because both are how fast the pair's facing turns per level of the pair's reading. Parallax reads depth best where the
  facing turns fastest, at the corner, and the even sweep lays its readings densest there for the same reason. **[exact]** for the identity, **[reading]** for the words.

## 4. The error's shape

Each direction is off by an independent error of spread σ. To first order the meeting point moves as the two lines move
across themselves.

**Proposition 2 (on the bisector).** With b = B/2 and r² = b² + d², relative to d:
- along the line of sight (the depth): σ√2·cosh(ln k), least at the corner, the same at k and 1/k;
- across it: σ√2·(1 + k²)/2, falling with distance toward σ√2/2, with no flip;
- their ratio, depth over across: d/b = 1/k, the pair's reading flipped. The error is round at the corner, stretched along
  the line of sight outside the circle and along the baseline inside it;
- both together: σ√2·(1 + k²)^(3/2)/(2k), least at k = 1/√2, d = √2·b, where it is (3√3/4)·σ√2 ≈ 1.299·σ√2, against
  1.414·σ√2 at the corner.

**[exact]** (PXC P8: each to 1.3e-48 against the exact triangulation's Jacobian; the least at k = 0.707106781186548. The
round error: P6, a Monte Carlo check, within 1.3%.)

*Proof.* Turn the readers' directions by δ₁ and δ₂. Each line moves across itself by r·δ at the place, so the meeting
point moves by Δ_along = r²(δ₁ + δ₂)/(2b) along the line of sight and Δ_across = r²(δ₂ − δ₁)/(2d) across it. The sum and
the difference of δ₁ and δ₂ are independent, each of spread σ√2. Divide by d and write k = b/d; the total is the root of
the sum of squares, and its derivative in k vanishes where 3k² = 1 + k². ∎

| levels from the corner | d / b | depth | across | total |
|---|---|---|---|---|
| −4 | 16 | 8.031 | 0.502 | 8.047 |
| −2 | 4 | 2.125 | 0.531 | 2.190 |
| −1 | 2 | 1.25 | 0.625 | 1.398 |
| 0 | 1 | 1 | 1 | 1.414 |
| +1 | ½ | 1.25 | 2.5 | 2.795 |
| +2 | ¼ | 2.125 | 8.5 | 8.762 |
| +4 | 1/16 | 8.031 | 128.5 | 128.75 |

(Over d, per σ√2. Negative levels are farther than the corner.)

- **The depth is parallax's; the across error is the direction's.** Far off, the error across the line of sight over d
  tends to a constant: the direction, which one standpoint already holds, is held as well at every distance. Parallax adds
  the depth, and only the depth has the corner. Inside the circle the across error grows as 1/d²: the place is between
  the standpoints and the two lines are nearly one. **[reading]**
- **The total is not a reading of the pair.** It has no flip, so its least is not at the corner. Which error a reader
  must keep small is the reader's question, not the geometry's. **[reading]**

**Proposition 3 (on the circle, round only at the top).** Where the baseline is seen at a right angle, the error's ellipse
has its axes along the two lines' normals, of lengths r₁σ and r₂σ. Its aspect is max(r₁, r₂)/min(r₁, r₂); seen from the
middle at angle φ from the baseline (measured from S₂'s side), r₁/r₂ = cot(φ/2). It is round only where r₁ = r₂, at the top. **[exact]** (PXC P9:
to 5.2e-50 at 5°, 10°, …, 175°; the cot(φ/2) form read after the run.)

*Proof.* Turning reader i's direction by δᵢ moves its line across itself by rᵢδᵢ at the place. At γ = 90° the lines are
square, so the two displacements lie along perpendicular normals and are independent. On the circle of radius b, r₁ = 2b
cos(φ/2) and r₂ = 2b sin(φ/2). ∎

The aspect on the circle is itself the reading of a pair, (distance from S₁, distance from S₂), round at that pair's corner.
**[reading]**

**Off the bisector, the circle is not the best place.** Along a ray from the middle at angle φ, the radial error over the
distance ρ is √[r₁⁴(ρ − b cos φ)² + r₂⁴(ρ + b cos φ)²]/(2bρ² sin φ) per σ. **[exact]** (PXC P10, to 6.7e-50.) It has no
flip off the bisector. **Measured, not predicted** (PXC run 3), along each ray it is least inside the circle:

| φ | least at ρ / b | least | on the circle |
|---|---|---|---|
| 15° | 0.968 | 0.268 | 0.366 |
| 30° | 0.892 | 0.565 | 0.707 |
| 45° | 0.826 | 0.889 | 1 |
| 60° | 0.830 | 1.184 | 1.225 |
| 75° | 0.936 | 1.363 | 1.366 |
| 90° | 1 | 1.414 | 1.414 |

On the circle the radial error is √2·sin φ·σ (at ρ = b the quantity under the root is 8b⁶ sin⁴φ), falling toward the
standpoints, where the distance from the middle is pinned. **[exact]**, read after the run. So the Thales circle is where
the baseline is seen square everywhere, and the corner of the depth only on the bisector. **[reading]**

## 5. The band, and the baseline as a zoom

**Proposition 4 (the band).** Read to a step ε in γ, the relative depth error ε·cosh(ln k) stays at or below 1 for
|ln k| ≤ acosh(1/ε): a band of acosh(1/ε)/ln 2 ≈ log₂(2/ε) levels on each side of the corner. Its far edge is near
d = B/ε, where γ is one step; its near edge is the flip, (B/2)²/(B/ε) = εB/4. **[exact]** (PXC P3: d·ε/B = 1.0 to 12
digits at ε = 10⁻⁶; 10.965783924 levels each side at ε = 10⁻³, by bisection on the error itself.)

- **Past the far edge a place is a ray.** The shift is under one step, COR's "shift of one address" seen from the corner.
- **The baseline is a second zoom.** Choosing B slides the band along the levels, as choosing H slides a reader's
  window (`observation-from-somewhere.md` §8, "H is a zoom"; `zoom.html`). Its width in levels is set by the step alone.
  **[reading]**

At published precisions, rounded: **[illustration]**

| reader | baseline B | step in γ | corner, d = B/2 | far edge, B/ε |
|---|---|---|---|---|
| two eyes | 6.5 cm | stereo acuity, about 20″ ≈ 10⁻⁴ | 3.25 cm | about 650 m |
| Earth's orbit, Hipparcos | 2 AU | 2 × 1 mas ≈ 9.7 × 10⁻⁹ | 1 AU | about 1 kpc |
| Earth's orbit, Gaia | 2 AU | 2 × 20 µas ≈ 1.9 × 10⁻¹⁰ | 1 AU | about 50 kpc |

Stereo acuity is a threshold on the disparity, a difference in γ itself, so the eyes' step needs no factor of 2. Two
readings follow, **[reading]**:
- The eyes' corner, 3 cm off, is nearer than they can focus: binocular depth is used only on the far side of its bell.
- Every star is many levels past the orbit's corner: 1 pc is 2.06 × 10⁵ AU, 17.7 levels out. Stellar parallax lives in
  the bell's far tail, where the relative depth error is ε·d/B.

## 6. Working back from what is known

Read backward, from results parallax already has to what they need, each step is forced by the one before. The known
results, each in print:

| | known result | source |
|---|---|---|
| K1 | d = a/tan p, with p the parallax and a the half-baseline (1 au); the parsec is defined in the small-angle form, (648 000/π) au exactly | classical; IAU 2015 Resolution B2, on the au of IAU 2012 Resolution B2 |
| K2 | the au was measured from outside the parallaxes it scales (transits of Venus, then radar ranging), and since 2012 it is fixed by agreement at 149 597 870 700 m exactly | IAU 2012 Resolution B2 |
| K3 | the relative distance error equals the relative parallax error, σ_d/d = σ_p/p, so σ_d = d²·σ_p/a | classical |
| K4 | inverting a parallax is reliable only while the fractional error is small; past about 20% a distance must be inferred, with a prior, rather than read as 1/p; a sample cut on parallax is biased by an amount set by σ_p/p | Bailer-Jones 2015; Lutz and Kelker 1973 |
| K5 | an intersection is best conditioned when its rays cross square | Ghilani 2010 |

(Here p is the parallax, half of the angle γ the baseline subtends, as in the conventions above.)

1. **From K1, the pair.** tan p = a/d is the ratio of two amounts. So parallax is the reading of the pair
   (half-baseline, distance): p is the pair's sweep angle, γ = 2p its facing, and its corner, d = a, is where the
   baseline is seen square (§1). **[exact]**
2. **From K2, one amount from outside.** Every reading is a ratio, so the angles fix distance only in units of a
   (`observation-from-somewhere.md` Proposition 8(a)), and one amount from outside the readings fixes them all (8(b)).
   The au was that amount, measured outside the parallaxes for two centuries, and is now an agreed unit, which is what
   that paper's §9 says a unit is. **[exact]**, **[reading]** for the history's words.
3. **From K3, the outer vantage.** The ratio of the relative errors is exactly (σ_d/d)/(σ_p/p) = γ/sin γ, the outer
   reading of the turn γ in `observation-from-somewhere.md` §3.4 (PXC P12). K3 is its far-field limit, 1; on the Thales
   circle it is π/2; near the baseline it grows without bound (2.77 one level inside the circle, 24.2 four levels in).
   Its reciprocal, sin γ/γ, is the inner reading, and their product is 1. The turn here is γ, the pair's facing, twice
   its sweep angle p: the outer reading reaches π/2 when γ is a right angle, which is at the pair's corner, d = a. On
   the thumb of `observation-from-somewhere.md` §10 the turn is the sweep angle itself, and π/2 comes at the sweep's
   horizon. It is the same identity read on two different angles, and the two places are not to be conflated. The
   product 1 holds at every γ, since the two ratios convert one relative error into the other and back; what parallax
   adds is that the π/2 is measured, the growth of a relative error on the Thales circle, not a unit chosen. So the
   rule of thumb is one vantage's reading of the parallax angle, exact only far off. Stellar parallax is all far field:
   there the rule holds to parts in 10¹¹. **[exact]**
4. **From K5, the flip.** The places at d and a²/d see the baseline at γ and π − γ (PXC P11), so the depth's precision,
   sin γ, is the same at both: the flip of the pair is the supplement of its angle. A precision unchanged by the flip is
   stationary at the flip's fixed point, and Proposition 1 shows it is greatest there. "Best when square" is the
   corner. **[exact]**
5. **What K5 needs of the two standpoints.** The depth takes the sum of the two direction errors, so its corner holds
   whatever their spreads. The error is round there only if the two standpoints read alike: its aspect at the corner is
   the ratio of their spreads (PXC P13). The exchange of the two standpoints is this pair's V = H, as drawing both
   parties at one length is the circle's. **[exact]**, **[reading]** for the parallel.
6. **From K4, the flip on the payload.** The distance is the flip of the reading, d = a/tan p. A reading whose error
   has any density at zero gives distances with a 1/d² tail and no mean, while the median passes through the flip
   (PXC P14): order kept and sums lost (`observation-from-somewhere.md` Theorem 6(b)–(c)), now on what arrives. At the
   band's far edge, where the reading's error equals the reading, 16% of readings fall at or below zero; K4's 20% lies
   2.3 levels inside that edge. The practice K4 describes, inferring the distance and never averaging inverted
   parallaxes, is what the flip forces. **[exact]**, **[reading]** for the words.
7. **From K1 again, the parsec.** Defined by the small-angle form, it differs from the tangent form by a·ε/3 = 242 km,
   with ε one arcsecond (PXC P15), the outer reading's first departure from 1. One parsec lies 17.65 levels past the
   pair's corner: astronomy's unit of distance was set in the far field. **[exact]**

**Read forwards,** the chain is this paper: the pair and its corner (§1), one amount from outside (§2), the bell and
its flip (§3), the error's shape (§4), the band (§5) and, past the band, the flip's missing mean. What it starts from is
small: one reading, the tangent of the parallax (K1); two standpoints that read alike (step 5); and one amount from
outside (step 2). The second is this pair's V = H; the third is the one number a situated reader lacks.

## 7. Parallax on the ladder

- **Past the band, distance goes on by a kind.** A kind calibrated inside the band (a width, a luminosity) carries
  distance outward by ratios read from one standpoint: the ladder (LAD; `ladder.html`; `inverse-square.md`). MAG's
  stars are such a calibration: their distances are Hipparcos parallaxes. **[classical]**, with
  **[data]** for MAG.
- **More readings improve the figure, never the scale.** In STC (`plans/stc-plan.md`), a figure read by 16 to 4,096
  standpoints and one outside length improved its shape as N^(−0.49), while its scale stayed at the outside length's 1%.
  An error in B is one shift in levels for every place it links: a payload error, not an address error.
  **[simulation]**; **[reading]** for the words.
- **The zero-point is the same kind of error.** A common offset in p shifts the levels of every star it touches and does
  not shrink with the number of stars (`physics.md` §4, queued; the archives are blocked here). **[reading]**

**The ladder as a tower of holds** (16 Oct; SPN R317, from *Degrees of Freedom* §5.10, the archive's tower of grouped
holds, and OFS §9, "Units within units"):
- **Each rung is a level of unit.** A parallax reads d/B, a ratio to its own baseline; the baseline is the rung's unit,
  its hold. The next rung's unit is a length already read, as a ratio, on the rung below: the AU in Earth radii (the
  transits of Venus), stellar distances in AU, a kind (Cepheids, then type Ia supernovae) calibrated on stars of known
  parallax. **[classical]**
- **Everything between rungs is a ratio.** What links two rungs is read one rung up, as a thread's P/D is; only one
  amount is written, at the bottom: the metre, through the AU, a defined number of metres since 2012. **[reading]**
- **Strangers cost the depth.** Two distances on one rung are related through that rung's ratios alone; a distance k
  rungs up is related to the metre through k of them. With independent errors σ_j on each rung's ratio (in levels), a
  distance on rung k carries √(σ_1² + … + σ_k²) against the metre, while two distances on rung k are related to each
  other with neither the rungs below nor the written amount: their ratio's error is the rung's own scatter. **[exact]**,
  given independent errors.
- **A rung's hold revised moves everything above it by one factor.** Baade's revision of the Cepheid zero-point
  (announced 1952; Baade 1956) and Sandage's finding that Hubble's "brightest stars" were HII regions (Sandage 1958)
  each moved every distance on and above the rung revised and none below, and left the ratios within a rung as they were. **[classical]** for the history;
  **[reading]** for the account; tested in LTH (`plans/lth-plan.md`).
- **Parallax sets the tower's pitch.** A tower of holds does not say how many levels one hold can carry. Proposition 4
  does: a rung read to a step ε holds about log₂(2/ε) levels each side of its corner, and past the far edge a place is a
  ray, so a new hold is needed, a longer baseline or a kind, calibrated inside the band. The two meet best where both
  read well, near the geometric mean of their ranges (OFS §8, the best H). **[exact]** for the band; **[reading]** for
  the pitch.
- **What the tower adds to §7.** "More readings improve the figure, never the scale" (STC) is the tower's last line: the
  written amount is shared by every rung and no ratio corrects it; each rung's own errors are what more readings shrink.
  **[reading]**

## 8. What stands on what

| claim | mark | where |
|---|---|---|
| one standpoint holds directions only; two and a length fix the figure and its scale | classical | OFS Props 8, 11(a)–(c) |
| γ/2 is the pair's sweep angle, γ its facing; the corner the Thales circle's top | exact | §1 |
| depth error per unit γ = cosh(ln k), precision sech(ln k) | exact | PXC P1, P2 |
| the bell is the facing's rate per level, the even turn's density | exact identity, reading | §3 |
| depth, across and total on the bisector; total least at √2·b | exact | PXC P8 |
| round at the corner, aspect d/b | exact (first order), Monte Carlo | PXC P6, P8 |
| on the circle, aspect cot(φ/2), round only at the top | exact | PXC P9 |
| off the bisector, the radial error least inside the circle | measured | PXC run 3 |
| the band acosh(1/ε)/ln 2 levels each side; far edge B/ε | exact | PXC P3 |
| "best when square" is the flip's fixed point: γ at d, π − γ at a²/d | exact | PXC P11 |
| σ_d/d = σ_p/p is the far limit of γ/sin γ, the outer reading; π/2 on the circle | exact | PXC P12 |
| the round error needs the two standpoints alike | exact | PXC P13 |
| inverting a noisy parallax: no mean, the median kept | exact | PXC P14 |
| the parsec a far-field unit, 242 km from the tangent form | exact | PXC P15 |
| the baseline as a second zoom | reading | §5 |
| the eyes and the stars at their corners | illustration | §5 |
| the ladder a tower of holds: ratios between rungs, one amount at the bottom, errors adding by rung | exact (given independent errors), reading | §7; LTH |

## 9. Open questions

1. **Off the bisector, where is the radial error least, and why?** Measured at 0.83–0.97 b along rays at 15°–75°. Is it
   the corner of some named pair?
2. **Which error should a reader keep small?** The depth has the corner; the total is least at √2·b; the ellipse's area
   (∝ r₁r₂/sin γ) is another. The geometry offers each; the reader chooses.
3. **The serial baseline.** A reader that travels its own baseline reads B with an error of its own, and holds the first
   reading while it travels. Prediction to write: the travel's error enters as one shift in levels for every place, as
   STC's outside length did, and the held reading's age as a turn of the first line.
4. **The zero-point on real data.** Queued in `physics.md` §4; the archives are blocked here.
5. **A reader that works at its corner.** Eyes and telescopes use only the far side of the bell. Two ears (about 15 cm
   apart) placing a near sound, or a rangefinder, might use the near side. Candidate, no prediction.
6. **In three dimensions.** By the symmetry about the baseline every plane through it repeats §1–§5: the places seen at
   a right angle are the sphere on the baseline, and the depth's corner is where that sphere meets the bisecting plane.
   What is new is the error out of each plane, a direction's error at each standpoint. Whether it has a corner: open.

## References

Baade, W. (1956). The period-luminosity relation of the Cepheids. *Publications of the Astronomical Society of the
Pacific* 68, 5.

Bailer-Jones, C. A. L. (2015). Estimating distances from parallaxes. *Publications of the Astronomical Society of
the Pacific* 127, 994–1009.

Euclid. *Elements*, Book III, Proposition 31.

Gaia Collaboration, Prusti, T. et al. (2016). The Gaia mission. *Astronomy & Astrophysics* 595, A1.

Ghilani, C. D. (2010). *Adjustment Computations: Spatial Data Analysis*, 5th ed. Wiley.

Hartley, R. and Zisserman, A. (2003). *Multiple View Geometry in Computer Vision*, 2nd ed. Cambridge University Press.

IAU (2012). Resolution B2, on the re-definition of the astronomical unit of length. XXVIII General Assembly, Beijing.

IAU (2015). Resolution B2, on recommended zero points for the absolute and apparent bolometric magnitude scales.
XXIX General Assembly, Honolulu.

Lindegren, L. et al. (2021). Gaia Early Data Release 3: parallax bias versus magnitude, colour, and position.
*Astronomy & Astrophysics* 649, A4.

Lutz, T. E. and Kelker, D. H. (1973). On the use of trigonometric parallaxes for the calibration of luminosity
systems: theory. *Publications of the Astronomical Society of the Pacific* 85, 573–578.

Perryman, M. A. C. et al. (1997). The Hipparcos Catalogue. *Astronomy & Astrophysics* 323, L49–L52.

Sandage, A. (1958). Current problems in the extragalactic distance scale. *Astrophysical Journal* 127, 513.

Snellius, W. (1617). *Eratosthenes Batavus*. Leiden.
