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

## Other gems, queued (not yet pulled)

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

## Conflicts that need Tom's ruling

1. **Does the parallel reader meet a horizon, and is it situated?** `vantages.md` says both situated vantages meet
   horizons (the 22 September ruling). The archive's R41–R42 (RGA L1723–1729) overrode that: "the horizon belongs to the
   serial reader alone", the parallel reader's h = 0 "an ordinary zero"; and R139 said "only fisheye is view from
   somewhere". Today's R191 names the outer hemisphere as a vantage of its own. Which stands?
2. **What shape is the parallel reading?** The archive (R44) says Gaussian, centred on home; the current table says the
   bell ½·sech(ln s), sharpest at the corner (from `number-line.md` §5).
3. **Can the fisheye be normalised?** R135: "you cant noramlize the fisheye, it is asymetric." R190: V = H forced as the
   reader's representation. Probably compatible (V = H is a representation, not a normalisation by a known V), but worth
   saying so.
