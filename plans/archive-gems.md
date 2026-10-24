# Gems in the archived papers

*11 October 2026. Tom: "here are some older papers where we have thought about the denominator. they have been archived
but off many gems we should pull forward, for example the 'tower'." The seven papers are now in `papers/archive/`, kept
as received. This note lists what is worth pulling forward, where it is, how it stands against the current view, and
where it went. Survey by Claude (five readers in parallel, two papers read directly); a reading, not a ruling.*

**Before reusing anything from the archive, check its terms.** Every one of these papers predates 9 October. They use
"density", "the view from everywhere" (now "nowhere"), "inside/outside" (now serial/parallel), "fulcrum" (now the
corner), arctan as the sweep (not permitted, R148/R177), h and v often as breadths or as one circle's components
rather than fill levels capped at 1, recursive corners and depth (superseded by R188), and the old situation numbers
(1 circle, 2 shapes, 3 fisheye, 4 impossible, 5 approximate). The archived *Reader Geometry as Addressing* holds rulings
R1–R151 only; R152–R187 are quoted in SPN's Appendix A.

## The tower

The word has several senses across the papers. They are one structure: **levels of an address, each a fixed pitch, so
that the level is the count and a hand steering by its own ratio steps exactly one level per rung.**

| sense | where | what it is |
|---|---|---|
| the drill-down tower | Browsing L767–770 | halving the window S, one level per halving; 30 levels to one element in a billion; the window looks the same at every level |
| the calendar tower | Browsing L772–797, L801; Radix §4–§5 | fixed pitch per level, so an address never moves when the list grows (positional notation; a timestamp 100/12/31/24/60/60); empty slots are the price; "milliseconds do not have leap days; calendars do" |
| the tower of bits | Radix §1–§3; Order of Limits L413–419, L639–670, L803–805; One Reader L1447–1461 | one rung of the reader's dial is exactly one bit of the address when the base equals the reader's ratio; the exponent is the level and the mantissa the reading (floating point); "the length of a quadkey equals the level of detail" |
| the bare tower of unit circles | Browsing L1033 | an angle of an angle of an angle: positional notation whose digits are directions; binary with two per circle; data only at the bottom |
| the tower of grouped holds | Degrees of Freedom §5.10, L1670–1841 | inside a group its hold cancels; between groups exactly one factor survives, removed by the level above; "neighbours cost nothing; strangers cost the depth"; always n − 1 independent factors |
| the two-group tower (the stitch) | Order of Limits L53–54, L2494–2530; One Reader L823–824 | two readers with different holds: closure recovers the one factor that crosses, the ratio of their holds (0.5, 2, 3.7003 recovered as 0.5000, 2.0000, 3.7003) |
| the indirection tower | Degrees of Freedom §5.11, L1842–1887 | addresses of addresses; rank n − 1 of n, the missing direction the hold: "depth is free precisely because it never produces a coordinate"; "an address that addresses itself is the corner" |

**What the Radix adds, and how it sits with the current view.**
- *A base is the pitch of an address's ladder; the reader's ladder has a pitch too, its grain. Where the two agree, one
  rung is one level* (Radix §1–§4, measured: nine rungs, nine steps of one in base two; four uneven changes in ten).
- *The lens forces a ratio ladder; the grain picks the ratio* (§5). Current view: past the corner the levels are plain
  doublings (R188, R189), and D.1 says only the halving is supplied without a measure. The Radix's "a reader with grain
  ln 3 matches base three" is that measure: **"Uniformity can be free. Variation has to be represented somewhere — in
  the reader's grain, or in information handed to it"** (§11). Consistent, and a sharper statement of D.1's escape.
- *A mixed address costs a table* (§5–§6); a variable grain matches it exactly (§11).
- *The floor is the container's grain* (§7): an address kept as a number inherits the number's step (2^53 in a double);
  kept as digits it has none. Five real failures, each "a number asked to hold something finer than its own grain".
- *The carry is the address's own event* (§3): a step at level b disturbs 1, 6 or 33 of 53 levels depending on where
  the address stood.
- *"The address is the pyramid"* (§10): content indexed on the reader's own ladder needs no separate level-of-detail
  table. Current view: the count is the level of detail (R190); this is that, built.

**Where it went:** SPN Proposition 1.2, "The tower: the levels as an address" (a reading).
Since 16 Oct (SPN R315) the calendar tower and the tower of grouped holds are also in OFS §9 as reading and writing:
"Growth, the test's other form" (a derived address moves as the list grows, a fixed-slot one is written and does not) and
"Units within units" (the factor between levels a ratio read one level up, n − 1 ratios however grouped, one amount at
the top, R316; the ISO thread, with the basic profile's exact ratios in place of Degrees of Freedom's 0.61343, which is
ISO 965's root depth).

## The denominator

| gem | where | standing now | where it went |
|---|---|---|---|
| "The reader's capacity is the only unit in the room"; H is the denominator because it is held when V arrives, and swapping them takes another experiment, not a change of notation | Browsing L62–66 | new; the vantage reason for the private ruler | `vantages.md` §F |
| the bucket and the water: "whichever is greater must be divided"; past the corner the reader keeps itself as the unit and counts, so the logarithm | Relation Space §9 | an older derivation of the two address spaces; consistent with Prop 1.2 | `vantages.md` §F (cited) |
| "The equation is a third party": a page, a shared scale or an equation lends its terms to the answer (a spring scale); a balance cancels | Relation Space §6, §17 | new as stated; it is the completed vantage named | `vantages.md`, the three vantages |
| "A symmetric account holds the figure and cannot state the rate; an asymmetric one states the rate and cannot hold the figure" | Relation Space §6 | new | `vantages.md`, the three vantages |
| the two friends: dividing the reads cancels what the seats share, multiplying cancels what is private; "a denominator paradox is the shape a missing purchase takes when it is mistaken for a fact" | Degrees of Freedom §4.1, L718–766 | the denominator paper's exchange as arithmetic | `vantages.md` §F (cited) |
| cos² + sin² = 1 is "the receipt that the two readings were taken against the same denominator" | Degrees of Freedom L768–806 | consistent with Prop 1.2(c): the circle is what one unit for both means | noted |
| "Three more than me needs a unit; three times me does not" | RGA L149–150; Relation Space §19 | consistent | noted |
| "The unit only comes from agreement; it is not geometric"; "a solo reader would have no need for a unit" | RGA R89, L1908–1915 | the denominator paradox at its root; SPN §8.4 has it | `vantages.md` §F (cited) |
| "An index has no unit to change; a crate is not a larger egg; the log navigates, the digits address" | One Reader L1412–1430; Order of Limits L393–457 | supports R189 (the logarithm fundamental) | the tower entry |
| the disagreement D = V_A·H_B − V_B·H_A: sameness, order and the corner, with no division | Relation Space §25 | not in the current papers | queued |

## Paradoxes for `vantages.md`

Moved into the catalogue as entries (§G, from the archive): the address measure against the arrival measure (RGA Prop
14–15, L884–946; the inspection paradox); a growing list looks finished (Order of Limits L279–362); the three counts
M ≤ V_ε ≤ V ≤ N, a hemisphere's N quoted as the whole's (Order of Limits L1027–1103); a uniform address space cannot
report position (Browsing L1008–1017); "an address is not supposed to have an average" (One Reader L501–514; Browsing
L963–975); "more points eventually means less seen", the ceiling about 1.12/ε (One Reader L896–909; Order of Limits
L1754–1845).

## Other gems (pulled forward 11 October, Tom: "yes"; see below)

- **Two registers make one group.** Turning (angle) and rescaling (ratio) together generate exactly PSL(2,ℝ); each alone
  gives half (One Reader L384–443). This is the group behind the single principle's three transformations
  (`observation-from-somewhere.md` §12.1).
- **Two octaves.** The angle doubling 2s/(1 − s²) and the scale doubling 2s agree near home and part at the corner; the
  current "plain doublings" are the scale doubling (One Reader L445–471; Order of Limits L1876–1890).
- **The corner is the best place to stand.** The kernel d/(x² + d²) is largest at d = x, v = h (Degrees of Freedom
  L2663–2672): an earlier form of Prop 1.2's "the best H puts the thing read at the corner"; Boyd's map parameter as the
  dial's radius (Order of Limits L1904–1906).
- **Closure is symmetry about the corner, not coverage** (Degrees of Freedom L3617–3650).
- **2ⁿ facings by parity, no angle** (Degrees of Freedom L1133–1178), with its graded claims: 2ⁿ regions derived; that
  they tile a sphere at π/2 each is imported measure. Pull the grading into Prop 1.2(d).
- **Why observation comes in steps:** a complete observer would be a copy of what it reads, and a thing has no vantage on
  itself (Relation Space §1).
- **A mark the reader carries never moves; a mark laid in the world does**; "a reader that has only the first can never
  say where it is" (Browsing L120–126).
- **Keep the address until contact**: rounding once costs half a step, rounding every move grows as √k (RGA L334–337).
- **The order of limits**: classical takes ε → 0 first, then N → ∞; readers have ε fixed and N unknown (Order of Limits
  L937–943; RGA L1422–1424). A candidate statement of what "completed" means.
- **Literature One Reader cites and the current papers lack**: Cuadras 2002, Pitman and Williams 1967 (the Cauchy from a
  uniform turn; projective invariance); Haraway 1988 ("the god trick"); Lamping, Rao and Pirolli 1995 (the hyperbolic
  browser: a pixel budget independent of N); Williams 1983, Mallat 1989 and the Bing Maps quadkey (levels of detail as
  dyadic levels); Boyd 1982/1987 (rational Chebyshev points, the Cauchy's quantiles); Stigler 1974 (the history of the
  Cauchy "pathology"); Koenderink 1984 (the occluding contour).
- **A coincidence to check**: the 2D Cauchy puts 1 − 1/√2 of its weight inside the corner circle (One Reader L538–542);
  `facing.html`'s arc stands off the line by 1 − 1/√2 at the corner. Same number, different objects; not yet shown to be
  more.

**Where they went (11 October).** One group, which doubling, the corner as the best place to stand, 2ⁿ by parity and
the disagreement: SPN Proposition 1.2, "Five more from the archive"; `v-and-h.md` items 426–429; the review paper (§2
the disagreement, §3(d) the parity count, §4 which doubling, §6 the best place to stand, §12.1 the group). The order of
limits: `vantages.md`, with the completed view, and the review paper §11. The literature: the review paper §1, §5, §6,
§11 and its references (Cuadras, Pitman and Williams, Stigler, Lamping et al., Williams, the Bing Maps tile system,
Haraway). Not pulled: the coincidence of 1 − 1/√2 (still to check), and the items marked new in the other lists above
(why observation comes in steps; carried and laid marks; keeping the address until contact).

**Moved into `observation-from-somewhere.md` (11 October, Tom: "proceed according to your recommendation").** The equation
as a third party (§1, "What the completed view costs"); why the median survives and the mean does not (§5, proved); two
absences kept apart (§5, reading); what another ratio costs (§3, reading, after *The Radix*); more points, less seen
(§6, checked as `plans/cei-plan.md`: exact, P2 narrowly killed); a shared fact buys exactly one factor (§7, checked as
`plans/tgt-plan.md`: exact, nothing killed). Not moved: why observation comes in steps (lower priority).

## Conflicts: settled by R192

Tom, 11 October: "Any conflicts of archived papers should defer to papers that are not archived." So each of the three below is settled for the paper that is not archived: the outer
hemisphere is a situated vantage of its own and meets a horizon (`vantages.md`, R191); its reading is the current bell;
and V = H is the reader's representation (R190), which is not a normalisation by a known V, so R135 does not conflict
with it. The archive's versions stay in the archive as the record.

*As first listed:*

1. **Does the parallel reader meet a horizon, and is it situated?** `vantages.md` says both situated vantages meet
   horizons (the 22 September ruling). The archive's R41–R42 (RGA L1723–1729) overrode that: "the horizon belongs to the
   serial reader alone", the parallel reader's h = 0 "an ordinary zero"; and R139 said "only fisheye is view from
   somewhere". Today's R191 names the outer hemisphere as a vantage of its own. Which stands?
2. **What shape is the parallel reading?** The archive (R44) says Gaussian, centred on home; the current table says the
   bell ½·sech(ln s), sharpest at the corner (from `number-line.md` §5).
3. **Can the fisheye be normalised?** R135: "you cant noramlize the fisheye, it is asymetric." R190: V = H forced as the
   reader's representation. Probably compatible (V = H is a representation, not a normalisation by a known V), but worth
   saying so.

## Special Relativity, Through the Fisheye (added 11 October)

*Tom, 11 October: "here is a earlier paper on SR". Dated 4 September 2026, it is now
`papers/archive/sr-through-the-fisheye.md` (sha256 b362ca06…6e8279), kept as received. It cites sr.md, The Fulcrum, The
Bounded Observer in Motion, The Unit Circle, Reader-geometry and The Two Settings, none of which is in this repo. Its
numbers were recomputed where they can be (`runs/srf/check.py`). This survey is Claude's, a reading and not a ruling.*

**Terms to convert before reusing anything.** Each of these predates 9 October; under R192 the papers that are not
archived stand.
- **"Fulcrum"** is the corner.
- **"Rung"** is a level.
- **"The lens", "the reader is a circle", "focus", "radius"** describe the reader's laying; here the boost is "the
  lens", and "a lens is orthogonal to the data" is its governing claim. Current view: the fisheye is the sweep in one
  facing seen from the standpoint (geometry), and the observer applies no lens (`v-and-h.md` item 107). Its "the boost
  is a zoom" agrees with Proposition 1.2's "H is a zoom".
- **The tilt θ with sin θ = β, cos θ = 1/γ, tan θ = γβ** is the angle shortcut (R148). In current terms, v = β and
  h = 1/γ are the unit relations, the reading v/h is the celerity, and the hold v² + h² = 1 defines γ (`v-and-h.md`
  item 48).
- **§10's "k = h_now/h_then … holds ḧ/h and never h"** uses h for an amount: H, by the case rule.

**What its numbers came to** (`runs/srf/check.py`).
- **Recomputed and agreeing:** C0 (half-angle aberration, to 2.5e-14); C2 (fore 0.577 and 0.229, aft 1.732 and 4.359;
  the forward hemisphere within 60.0° and 25.8°; within exactly 45° at β = 1/√2, k = 1 + √2); C3 (the k-ladder 3/5,
  15/17, 63/65, …; celerities 0.75, 1.875, 3.94, 7.97, 15.98, 31.99; rapidity in doublings minus log₂ celerity 1.093,
  1.023, 1.006, 1.001, 1.0004); C4 (η′ − η = ln k = 0.693147180560 at all four directions); C8 (k = 10.8151 and a
  Wigner rotation of 17.87°, by matrices and the closed form); C9 (quartiles 0.8000, 1.2000, median 1).
- **C1 holds only for a circle sky (2+1 dimensions).** There the readings tan(θ/2) are standard Cauchy and a boost
  scales them by 1/k: quartiles ±0.99998, ±0.57734 and ±0.22941. On the sphere (3+1) they are not Cauchy: tan(θ/2) has
  CDF r²/(1 + r²) with median 1, and one signed coordinate's quartiles are ±1/√3. "The sky is a Cauchy" needs "in 2+1
  dimensions".
- **C10's 0.795** is a grid value; Cauchy half-widths add exactly, so it is 0.8.
- **C8's bench match is to three digits, not four.** *Browsing the Fisheye* §7 prints "R/12 becomes R/10.8 at a third
  of a radian". At a third of a radian (0.667 doubled) the composition gives 10.92; the SR paper's 0.35 rad and 10.815
  come from the bench script, which is not in this repo. 10.8 is reached at 0.3523 rad.

**Gems.**

| gem | where | standing now | where it would go |
|---|---|---|---|
| Three exchanges, three fixed points: k ↔ 1/k fixes rest, slope ↔ 1/slope fixes β = 1/√2 (celerity 1), fore ↔ aft fixes the transverse plane | §4 | the current rule "name the pair before saying the corner", in SR: three pairs, three corners | `physics.md` motion dictionary (queued) |
| β below the corner, rapidity above it; the k-ladder of rational speeds on doublings, rapidity and celerity one level apart in the tail | §4 | `v-and-h.md` item 102 (asinh: proportional below the corner, logarithmic above) already has it; checked | noted |
| Pseudorapidity is a direction's level, −ln tan(θ/2); a boost along the axis shifts every one by ln k (a pan in levels); detectors segmented evenly in η are the logarithmic lay, built | §5 | known physics; a reading; checked | `physics.md` dictionary (queued) |
| An even sky is a Cauchy and a boost is its scale; the scale is the account's, not the sky's | §2 | in 2+1 dimensions only (above); consistent with OFS Theorem 6 (the reach cancels from every reading) | corrected here; queued with the 2+1 qualifier |
| The moving observer's sky is magnified aft and crowded fore (the headlight effect), correcting sr.md §9.2.1 | §3 | known physics; the correction is to a paper not in this repo | noted |
| A pan between levels costs radius: the Wigner rotation | §6 | checked (17.87°); the bench match to three digits | noted |
| The uniformly accelerated observer: horizon one radius 1/a behind; clocks on the Rindler ladder geared by radius; the forward cone's tangent halving every ln 2 of rapidity, so levels at even proper time | §7 | known physics (Rindler); a reading; compare MOT P4, where at constant speed the levels of an approach come ever faster | MOT (queued) |
| Open and closed: the worldline open (its horizon holds the future); the sky closed (a seam at the fore point); the k-line closed (a seam at light) | §8 | a reading | noted |
| The fourth star as audit: a boost leaves every cross ratio of four directions fixed (a Möbius map); light deflection by the Sun moves it (up to 6e-7, against 1e-15 under aberration) | §9, §14 | physics: the Lorentz group is the Möbius group of the sky; the deflection half is the claim, testable on astrometry of one field with the Sun near and far | `physics.md` §4 queue (data blocked here) |
| β filed as a magnitude, rapidity the count; the Breit–Wigner line as an evenly spread phase, the energy an address into it (E_R the place, Γ/2 the scale, the Argand circle drawn) | §12 | consistent with OFS's main result (the Cauchy is addresses, not payload); the history ("physics missed it") is a reading, not a finding | `physics.md` dictionary (queued) |
| The lead killed in its own run: overlapping resonances add their widths (a Cauchy sum), not nested readers | §12 | kept as the record's kill | noted |
| Reader space is velocity space; the zoom-and-pan between two views is a hypercycle, not the geodesic, the gap being the Thomas precession | §13 | not rechecked here | noted |

**One link to MOT run 2** (Claude's, checked in `runs/srf/check.py`, not in the archived paper). In the Doppler pair's levels,
ζ = ln k, γ = (k + 1/k)/2 = cosh ζ is even (stationary at rest, the pair's corner), and γβ = (k − 1/k)/2 = sinh ζ is
odd (zero at rest, approach against recession): the two kinds of corner of `plans/mot-plan.md` run 2. And
1/γ = 2k/(1 + k²) exactly, the facing's sine. That is the same form as a launch's range and a baseline's conditioning,
so (β, 1/γ) is the Doppler pair's facing: β = −cos F, 1/γ = sin F, with k = tan(F/2). The algebra is standard (Bondi's
k, the tangent half-angle); the reading is ours. A MOT run 3 would put it to predictions first.

**Where it went (11 October):** archived. Then, at Tom's "yes", into MOT run 3 (`plans/mot-plan.md`; nothing killed) and
`physics.md` §1 and §2.2: the three pairs and their corners (§4), pseudorapidity as a direction's level (§5), β below the
corner and rapidity above it (§4, tested as rapidity being the reader's lay smoothed), and the link above. The fourth
star, the Breit–Wigner line and the Rindler gearing are not moved.

## Observation Is a Sphere: The Handshake at the Horizon (added 24 October)

*Tom: "here is an old paper. Any gems?", then "yes" to filing it and pulling these forward. `papers/archive/observation-is-a-sphere.md`,
kept as received (undated; its own sections place it after the December 2025 *Universal Semantic Horizon* paper, which
CAH read). It is the source of ψ₁ψ₂ = (2/π)(1/2) = 1/π, the Ω_m share `plans/omm-plan.md` set aside. Read by Claude,
every number below checked exactly before sorting; a reading, not a ruling.*

**Gems:**
- **The Cayley transform** (its Appendix C): w = (z − i)/(z + i) sends the reading s = tan θ to w = −e^(2iθ), the circle's
  point 2θ round from home's image, and i to the centre (checked to 10⁻¹⁶ at three θ). The inscribed θ and the central
  2θ (III.20) are one point under the map; the uniform turn about the centre is carried to the Cauchy on the line, the
  harmonic measure from i. **Went to** OFS §4, after "What each sweep reads", with Cayley 1846 cited (SPN R470).
- **The handshake, π/2 · 2/π = 1**: in the paper a number times its reciprocal labelled inside and outside; its intuition
  (one boundary, two vantages) is what OFS kept, with content: one turn from its two pivots (R223, R329, R450).
- **ψ by dimension**: its 2/π (S¹), ½ (S²), 4/(3π) (S³) are E|cos θ| for a uniform direction in 2, 3, 4 dimensions,
  Γ(d/2)/(√π·Γ((d + 1)/2)), SIT run 1's hemisphere numbers inverted. Its "S² is the only rational one" is wrong: every
  odd d gives a rational (3/8 at d = 5, 5/16 at d = 7).
- **ln 2 and the floor**: the doubling map x ↦ 2x mod 1 (Lyapunov exponent ln 2, the Bernoulli shift) moves one binary
  digit from the remainder into the key a step: the floor's remainder (R464) as dynamics, one level a step. **Went to**
  OFS §8's "Every level is the next" and the CS companion's §7.2 (SPN R470). The paper gives ln 2 to every Chebyshev
  T_n; T_n has ln n, only T₂ ln 2.
- **π_p least at p = 2**: in the p-norms "π" runs from 4 down to π, least for the circle (Adler and Tanton 2000, *College
  Mathematics Journal* 31(2), 102–106, checked). Bears on OFS's Euclidean choice. **Went to** OFS §5, "The Euclidean choice" (R471), with Keller and Vakil 2009 (π_p = π_q for conjugate p, q). The paper's
  L₁ value 2.83 is wrong (4).
- **K and N**: "K finite, N unbounded"; "K is discrete to its creator, but continuous to its observer". Early forms of K
  apart from N (OFS §8) and writers within writers (OFS §11.2 question 8). Already in OFS in their present form.

**Not to pull forward:**
- The extraction rate: ∫₋₁¹ dx/(1 + x²) = π/2, not 2, so the share captured by the aperture [−1, 1] is ½ (the corner),
  not 2/π.
- 1/π = (2/π) × ½ multiplies means from two dimensions as if sequential filters; with it Ω_m (stays set aside, OMM).
- The drift section argues against itself (§14: only exactly 2/π avoids drift; §15: near-misses cancel); Weyl's theorem
  does not cancel a wrong rate's linear drift; Beatty's theorem is true and unrelated; "3 looks 95.5%, 4 looks 127%" is
  3/π and 4/π.
- Slepian–Pollak's 2/π is a units conversion (c = πWT against the Shannon number 2WT).
- Appendix B's biology: retinal ganglion density does not fall as 1/(1 + ρ²) (cortical magnification goes roughly as
  1/(E + E₂)); the fish-drift and bee-dance figures look unverifiable. Check every citation before any use.
- Its terms predate 9 October throughout (inside/outside, extraction, S¹ "odd", S² as "the line"): check before reuse.

## The Algebra of Discrete Observation (added 24 October)

*Tom: "here is an old paper. any gems?", then "yes". `papers/archive/algebra-of-discrete-observation.md` (1.1 MB, kept as
received; it audits itself in §15 and retracts much of its §13 physics). Read by three readers in parallel (lines 1–1000,
1000–2110, 2110–3441), each checking every claim with sympy or mpmath; the main ones re-checked by Claude. A reading, not
a ruling.*

**Taken into OFS (SPN R472):**
- *The corner fixed by home and the horizon* (its §8.5, L1443): (1, −1; x, 1/x) = −1 for every x (exact fractions), the
  reciprocal's fixed points harmonic conjugates of every pair it swaps, (0, ∞) among them. OFS §4, after "The reader's
  line, closed", with the bracket D = v₂h₁ − v₁h₂ (order by sign, zero on one direction, scaled by a drawing's
  determinant) and Lagrange's identity D² + dot² = |a|²|b|² (its §1.07, L332–346, L241). Coxeter 1987.
- *Niven's closure* (its §10.1, L1787): repeating a rational step closes only at t = 0, 1, ∞; other steps equidistribute
  (Weyl). OFS §2, "Zero, and a new zero"; the CS companion §2.4.
- *No group law on three parties' directions* (its §12.4a, L2172): χ(RP²) = 1, a compact Lie group's χ = 0; a new zero
  in the wedge is a rotation in SO(3). OFS §2.
- *Halving by square roots* (its §10.1, L1781): tan(π/7), tan(π/9) of degree 6 (sympy), so no ruler and compass divide a
  half turn into seven or nine; halving reaches every tan(π/2ᵏ). OFS §5, "Why halving" (Wantzel 1837), pointing to
  Viète's product, already in OFS §3.4.
- *The three rulers as the three 2D number systems* (its §15, L3260–3266): complex, split-complex and dual numbers, unit
  sets the circle, the hyperbola and the tangent line, each multiplying by adding its ruler's coordinate (Yaglom 1968).
  OFS §6, after "One figure, three rulers".
- *For engineering* (its L730, L975, L1824): the equi-angular cubemap (solid angle within √2 across a face, against 3√3
  for the gnomonic, computed); exact tangent addition in Gaussian integers, ½·log₂ of the odd part of h² + v² bits a step
  (400 exact steps: 1.1609 against 1.1610 at (3, 1), 1.8499 against 1.8502 at (5, 1), 0 at the corner); Fibonacci
  hashing, ⌊2³²/φ⌋ = 2,654,435,769 (Knuth), with the three-distance theorem (Sós 1958). OFS §11.4 and the companion §12.

**Kept here, not moved:**
- The exact Thomas angle: a circular velocity loop turns the frame by 2π(γ − 1), the hyperbolic disc's area (one turn
  at v = √3/2, checked); perpendicular boosts tan ω = sinh a·sinh b/(cosh a + cosh b) (to 10⁻¹⁶). OFS §11.4 cites Thomas
  only qualitatively. Aravind 1997 to check before citing.
- Bondi's k-calculus: β = (k² − 1)/(k² + 1), γ = (k + 1/k)/2, γ ≥ 1 by AM–GM (Bondi 1964), for OFS §7.8 if wanted.
- Gołąb 1932: over all norms the half-perimeter in the own norm runs over [3, 4] (hexagon to parallelogram); a footnote to
  π_p.
- The tilt b = (r − 1)/(r + 1) = tanh(½ ln r) and G = 4r/(1 + r)² = sech²(½ ln r); visible lattice points (v, h) in a disc
  give the Cauchy's quartiles (√2 − 1, 1, √2 + 1 at R = 600, a count-only uniform turn); Maxwell's fish-eye (index
  2/(1 + r²), the stereographic factor; rays circles to 2·10⁻¹¹); the interpolation kernel in slope form,
  Im[(1 + ir)ᴺ]/(N r (1 + r²)^(N/2)) = sin Nφ/(N tan φ); Sturm–Prüfer nodes as horizon passages and a Maslov ¾ (physics).

**Errors, not to pull forward:**
- "Over L_p norms π ranges across [3, 4]" (L1706): [π, 4]; [3, 4] is Gołąb's over all norms.
- The "absorber" refutation (L644) uses tanh addition (det 1 − g²); the paper's own ⊕ is tangent addition (det 1 + g²).
- "[0, 1) is a group under (a + b)/(1 + ab)" (L1061): no inverses; the group is on (−1, 1).
- The corner set's stabiliser has order 8, not 4 (L1013; the Cayley map (1 + r)/(1 − r) is in it).
- "71% wrong after a thousand conversions" (L1900): 1.001¹⁰⁰⁰ = 2.717, about 172%.
- "No identification of a torus yields a sphere" (L2519): the pillowcase T²/(z ↦ −z) is S².
- ζᴺ = −1 lands on the horizon, not home (L1477); the Prüfer node direction reversed (L2614); Fisher–Rao for a Cauchy
  location is uniform, not 1/(1 + s²) (L1362); the beam reads tanh only with pans hung below the pivot (L410); the
  "toll indexed by ambient dimension alone" (L2189) fails in ℝ⁴.
- §13–14's physics (Born's rule, spin-½, "quantization is compactness", anyons from π₁(SO(2))) retracted by the paper's own
  §15 audit; its conclusion still states it.
- Its terms (the atom, registers, "the chart is never asked for", the two zeros) predate the current frame: check before
  reuse.

## The Balance (added 24 October)

*Tom: "any gems", then "yes". `papers/archive/the-balance.md` ("a working paper on the centre of gravity as the primitive
read", 234 KB, kept as received). Read by two readers in parallel (lines 1–1350, 1350–2680), every claim checked; the
three taken re-checked by Claude. A reading, not a ruling.*

**Taken into OFS (SPN R473):**
- *Why a turn and not a boost* (its §27, L1142; §31, L1686–1695; found by both readers): of the three one-parameter
  Möbius flows on the line only the elliptic (a turn) keeps a probability of full support, the Cauchy, uniquely; under a
  hyperbolic or parabolic flow every point drifts monotonically to a fixed point, so their invariant probabilities sit on
  the fixed points. OFS §7.1, after Proposition 5's first parts.
- *The square takes a centred conic to a focal one* (its L427–439): w = z² carries z = a cos t + i b sin t to
  |w| = ℓ + e·Re w, ℓ = 2a²b²/(a² + b²), e = (a² − b²)/(a² + b²) (at a = 2, b = 1: 1.6 and 0.6, residual 2·10⁻¹⁵), w
  once round as z goes twice (Bohlin 1911; Levi-Civita 1920; Arnold 1990). OFS §4, after the Cayley transform. The physics
  (Hooke's and Newton's laws, the two Bertrand keeps) left out.
- *A median in two registers* (its §37.2, L2180–2191, corrected): the sign of each comparison with steps k^(−0.6) and a
  running average (Robbins and Monro 1951; Polyak and Juditsky 1992) reaches the sample median's accuracy, √n·sd → π/2
  for the Cauchy (Claude: 1.592 over 40 runs at n = 10⁵; reader: 1.586). OFS §7.6 "Order needs the readings together";
  the CS companion after Theorem 6.

**Kept here:**
- The two reads' sensitivities: through the dot product and the bracket, Fisher informations sin²Δ/σ² and cos²Δ/σ²,
  summing to 1/σ², equal at the corner; the dot product blind at home (its estimate ∝ √σ, sd ≈ 0.48·√(2σ)).
- Rational group laws on the line are conjugate to x + y, (x + y)/(1 − xy) or (x + y)/(1 + xy) (the additive group, the
  norm-one torus, the multiplicative group): Yaglom's three algebras as algebraic groups.
- The correlation bound (r₁₃ within 0.3 ∓ 0.6928 for r₁₂ = r₂₃ = 0.6, and so on), statistics.

**Errors, not to pull forward:**
- L120–128: both curved cases "open at order Kd²"; its own hyperbolic column scales as d³.
- L142–156: the "centre of gravity" a force-weighted mean of positions (gap L²/2R); the usual centre of gravity gives
  3L²/(8R).
- L412–425: near-circular orbits close whenever √(3 + p) is rational, so "Bertrand's cut is exactly covering degree at
  most two" overstates.
- L1142: "no finite invariant measure at all" is false; point masses at the fixed points are invariant.
- L1219–1225: "charged by the room, not the cargo" fails in ℝ⁴ (a 2-plane onto a 2-plane 0.332, against 4/(3π) = 0.424);
  L1055 labels chord/arc = 1 "the corner", where in that pairing it is θ = 0.
- L1508–1512: its "√(2σ) prediction" column is 0.4795·√(2σ); L2184–2191's "sign-and-halve, M = 1" freezes early (a halved
  step), its ratios single-run noise; L1388–1390 and its table still say "total = πρ₀ = K", fixed only at §31.2 to (π/2)ρ₀.
- L1489–1491 calls Lagrange's identity "the Born rule" (conceded at its §34); L1474, L1485 "provably no fourth" and
  "nothing else is observable" overclaim the first fundamental theorem; appendix Y1's "exactly 3 gaps" is at most 3.
