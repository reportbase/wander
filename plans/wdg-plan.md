# WDG: the wedge, made with the Cauchy

*13 October 2026 (Tom's local date, about 7:00). Tom: "the unit sphere could point every address in the universe." To Claude's
answer (every place as a direction and a level log₂(|x|/H)): "but that is the unsituated readers sphere, he would have
to know the size if the universe. the situated reader has to sweep and set V = V2 = H. and create the sweep wedge using
the cauchy." Then "yes" to an exact check and a write-up, with: "if we put a rotatable sphere inside the unit cube, we
could show that every point on the sphere maps to every point on the inner cube. the inner cube could be any size,
however its extent must be known." Exact arithmetic (mpmath, 30 digits) and identities checked to rounding.
Predictions written before the script (`runs/wdg/wdg.py`) exists. It builds on `observation-from-somewhere.md` Propositions
3 and 5 (the circle, forward and back), `number-line.md` §8 (the sphere of three unit relations, the octant, the six
chambers, the triple corner, the unit cube) and Tom's line of 8 October there: the wedge is made at every observation.*

## Set-up, with the case kept

**Amounts:** H, the reader's breadth; V and V₂, the breadths it assigns to two other parties, drawn at V = c₁H and
V₂ = c₂H; e, the half-extent of a cube (an amount, known or not).

**Unit relations:** h, v, v₂ ∈ [0, 1], each relating its party to its assigned breadth. **Readings:** a = v/h and
b = v₂/h, two relations against the one h (and v/v₂ = a/b, the third pair).

**The wedge.** With V = V₂ = H the attitudes are the directions of one rigid bar of length 1, the sphere
h² + v² + v₂² = 1, and one facing of each freedom is the octant h, v, v₂ ≥ 0: area π/2. The situated reader makes this
wedge at each observation; the whole sphere is the eight wedges drawn together, a picture of the complete system and
not something a situated reader holds. **Sweeping the wedge evenly** is every direction alike: uniform by area.

**Unsituated against situated.** Placing every place in the universe by its direction and a level log₂(|x|/H) needs
every |x|, an amount: the unsituated reader's sphere. The situated reader holds readings, a and b, and lays them on
the wedge.

## Predictions

- **P1. The even wedge is the two-dimensional Cauchy.** Laid on the readings (a, b) ∈ [0, ∞)², the octant's area
  element is da·db/(1 + a² + b²)^(3/2) (the gnomonic map, the plane h = 1), its total π/2, so the even wedge's readings
  have density 2/(π(1 + a² + b²)^(3/2)). **Killed if** the area element of the map (a, b) ↦ (1, a, b)/√(1 + a² + b²),
  taken from its partial derivatives in mpmath, misses (1 + a² + b²)^(−3/2) by more than 1e-20 (relative) on a grid
  of a, b in 2^(−8) … 2^8, or the total misses π/2 by more than 1e-15.
- **P2. Every pair keeps its corner.** Each of v/h, v₂/h and v/v₂ is half-Cauchy, 2/(π(1 + x²)), with its median at
  its own corner, 1, and no mean. **Killed if** the marginal of a (integrating out b) misses 2/(π(1 + a²)) by more than
  1e-15 at a = 2^(−8) … 2^8, or P(a/b ≤ r) misses (2/π)·arctan r by more than 1e-15 at r = ¼, ½, 1, 2, 4.
- **P3. Six equal chambers; the near field a third.** Each of the six orderings of (h, v, v₂) holds 1/6 of the wedge.
  So near in both relations (h the largest: a, b < 1) holds 1/3, past in exactly one 1/3, and past in both 1/3, where
  the circle's near and far were halves. The 1/3 is π/6 of π/2, a quarter of a cube's face seen from the centre.
  **Killed if** any of these, by quadrature of P1's density, misses its value by more than 1e-15.
- **P4. The wedge requires V = V₂ = H.** Draw V = c₁H and V₂ = c₂H and sweep evenly by direction in the drawing. Then
  (c₁a, c₂b) is P1's law, so v/h has its median at 1/c₁, v₂/h at 1/c₂ and v/v₂ at c₂/c₁, and the readings follow P1's
  law, every pair's median at its corner and each chamber 1/6, if and only if c₁ = c₂ = 1. **Killed if**, at
  (c₁, c₂) = (1, 1), (2, 1), (1, 2), (2, 2) and (½, 3), any median misses its value by more than 1e-15, or the share
  "near in both" equals 1/3 within 1e-6 at any (c₁, c₂) ≠ (1, 1) of these.
- **P5. A rotatable sphere in a cube points every point of it, and the cube's extent must be known.** From the centre,
  each point u of the unit sphere goes to u·e/‖u‖_∞ on the surface of the cube of half-extent e, the face of u's
  largest component: a one-to-one map of the sphere onto the cube's surface, for every e > 0 and after any turn R of the
  sphere (u ↦ Ru). Every point x of the solid cube but its centre is t·e·u/‖u‖_∞ for exactly one u and one
  t = ‖x‖_∞/e ∈ (0, 1], a unit relation. The address (u, t) is the same at every e; the point in amounts is e times it,
  so e must be known. **Killed if**, for 10⁵ random points at e = 10⁻⁶, 1 and 10⁶ and random turns, the round trip
  x → (u, t) → x misses by more than 1e-12 (relative), any address (u, t) differs between the three extents by more
  than 1e-12, or the face reached is not that of the largest |component|.
- **P6. On the cube's faces the even sphere is the Cauchy too.** Each face of the cube holds 1/6 of the even sphere, at
  density ∝ (1 + a² + b²)^(−3/2) in its own coordinates (a, b) ∈ [−1, 1]², so the middle quarter of a face by area
  (|a|, |b| ≤ ½) takes 4·arctan(1/(4√1.5))/(2π/3) ≈ 0.385 of the face's directions, not 0.25, and a face's centre is
  3^(3/2) ≈ 5.196 times as dense as its corners. **Killed if** the quadrature misses 4·arctan(1/(4√1.5))/(2π/3) by more
  than 1e-15, or a face's quadrature misses 1/6 of the sphere by more than 1e-15.

Known already: the gnomonic projection of a uniform direction is the multivariate Cauchy (the multivariate t with one
degree of freedom), its marginals Cauchy; the solid angle of a rectangle; the radial map between a sphere and a convex
body around its centre. What WDG adds is the reading: the situated reader's sphere is a wedge made by sweeping with
V = V₂ = H, its even measure is the Cauchy, the near field is a third, and a cube of any size is pointed by it only once
its extent is known.

## Runs

### Run 1 (13 October, `runs/wdg/wdg.py`)

mpmath at 30 digits (20 for P4's root-finding); numpy for P5, seed 20; three minutes.

| | prediction | result | |
|---|---|---|---|
| P1 | the octant's area element in the readings is (1 + a² + b²)^(−3/2), total π/2 | to 2.0e-31 on the grid; total π/2 to 4.9e-16 | not killed |
| P2 | v/h, v₂/h and v/v₂ each half-Cauchy, median at the corner | the marginal to 2.0e-31; P(v/v₂ ≤ r) = (2/π)·arctan r to 5.9e-24; P(v/h ≤ 1) = 0.5 | not killed |
| P3 | six chambers 1/6 each; near in both, past in one, past in both 1/3 each | every chamber 0.166666666667; 1/3, 1/3, 1/3 to 3.9e-16 | not killed |
| P4 | medians 1/c₁, 1/c₂, c₂/c₁; near in both 1/3 only at c₁ = c₂ = 1 | medians exact at all five drawings; near in both 0.333, 0.436, 0.436, 0.590, 0.279 | not killed |
| P5 | the radial map one-to-one at any extent and turn; the address the same at every e | round trip to 7.5e-16; addresses across e = 10⁻⁶, 1, 10⁶ to 4.4e-16; the face always the largest component's | not killed |
| P6 | a face 1/6; its middle quarter by area takes 0.385 of the face | 1/6 to 20 digits; 0.38456530109385 as predicted | not killed |

P4 in full (medians of v/h, v₂/h, v/v₂; share near in both):

| drawing | v/h | v₂/h | v/v₂ | near in both |
|---|---|---|---|---|
| V = H, V₂ = H | 1 | 1 | 1 | 0.3333 |
| V = 2H, V₂ = H | 0.5 | 1 | 0.5 | 0.4359 |
| V = H, V₂ = 2H | 1 | 0.5 | 2 | 0.4359 |
| V = 2H, V₂ = 2H | 0.5 | 0.5 | 1 | 0.5903 |
| V = ½H, V₂ = 3H | 2 | 0.333 | 6 | 0.2789 |

**Reading.**
- **The situated reader's sphere is a wedge made with the Cauchy.** Sweeping the octant evenly and laying the readings
  (v/h, v₂/h) by the two-dimensional Cauchy are one statement (P1): the density is the octant's own area seen through
  the readings. The reader needs no size of anything to make it.
- **Each pair's corner needs that pair drawn at one length.** At V = V₂ = 2H the pair (v, v₂) keeps its corner (its
  median 1), while both pairs with h lose theirs by one level (P4). The wedge, all three corners and the triple corner
  at its centre, needs V = V₂ = H: the circle's V = H, once per party.
- **The near field is a third.** With three parties the reader is near in both relations for a third of its addresses,
  past in one for a third, past in both for a third (P3). The circle's halves were the case of two.
- **A cube of any size is pointed, once its extent is known.** Every point of the sphere reaches one point of the cube's
  surface, through any turn, at any size (P5); every point inside is that point times a unit relation t. The address
  (u, t) is the same at every extent; the point in amounts is the extent times it. With the extent unknown the reader
  holds the address and draws the cube at its own breadth, which is V = H again: right as an address, off as an amount
  by the true extent over H.
- **On the cube the even sphere is still the Cauchy** (P6): each face is a reading plane, its middle quarter by area
  taking 38% of the face's directions, its centre 5.2 times as dense as its corners.

### Run 2 (13 October, about 12:15; `runs/wdg/wdg2.py`): n other parties

*Tom, 13 October, about 12:13, to a fifth ChatGPT message (a reader drawing five parties at V₁ = … = V₅ = H;
`plans/ofs-review-6.md`): "from the geometry's perspective, its job is done, what ever the true breadth makes no
difference." Then "yes" to this run, which carries P1–P4 from two other parties to n. Predictions written before the
script existed.*

**Set-up, with the case kept.** The reader's h and n other parties' v₁, …, v_n, unit relations in [0, 1], each party
drawn at V_i = H; the attitudes are the unit sphere in n + 1 dimensions and one facing of each is its positive orthant;
sweeping it evenly is uniform by area. Readings a_i = v_i/h. For n = 1 this is the circle, for n = 2 run 1's wedge. No
amounts enter; the true breadths V_i* appear nowhere.

- **P7. The even orthant is the n-dimensional Cauchy.** The readings have density
  c_n·(1 + |a|²)^(−(n+1)/2) on [0, ∞)ⁿ, c_n = 2ⁿ·Γ((n+1)/2)/π^((n+1)/2) (2/π for n = 1 and 2, 8/π² for 3, 12/π² for 4,
  64/π³ for 5). **Killed if**, for any n from 1 to 5, the area element of a ↦ (1, a)/√(1 + |a|²), from the Gram
  determinant of its derivatives in mpmath, misses (1 + |a|²)^(−(n+1)/2) by more than 1e-20 (relative) at 20 random
  points of [2⁻⁶, 2⁶]ⁿ, or the density's total, by radial quadrature, misses 1 by more than 1e-25.
- **P8. Every reading and every pair keeps its corner.** Integrating out all readings but one gives the circle's
  2/(π(1 + x²)), median at 1, for every n; integrating out all but two gives run 1's 2/(π(1 + x² + y²)^(3/2)), so by
  run 1's P2 every v_i/v_j is half-Cauchy with its median at 1. **Killed if** either marginal, by radial quadrature,
  misses by more than 1e-25 (relative) at x, y in 2⁻⁸ … 2⁸ (even powers), for n = 2 … 5 (one-reading) and 3 … 5 (two).
- **P9. The near field in all readings is 1/(n + 1), and the count past the corner is even.** The share with every
  reading below its corner (h the largest of the n + 1) is 1/(n + 1): ½, ⅓, ¼, ⅕, ⅙ for n = 1 … 5. More: the number of
  readings past their corner is spread evenly over 0, 1, …, n, each 1/(n + 1) (run 1's P3 is n = 2). The reason
  expected: the even sphere treats the n + 1 unit relations alike, so h's rank among them is spread evenly. **Killed
  if** product Gauss–Legendre quadrature of P7's density over [0, 1]ⁿ (24 nodes an axis, float64) misses 1/(n + 1) by
  more than 1e-12 for any n, or, over 10⁷ even points drawn on the orthant (normalized Gaussian vectors made positive,
  numpy, seed 21), any count's share is more than 5 standard errors from 1/(n + 1).
- **P10. The drawing is required.** Drawn at V_i = c_iH and swept evenly in the drawing, the near-in-all share is the
  base law's mass on the box ∏[0, c_i] (as run 1's P4), 1/(n + 1) at every c_i = 1 and not otherwise. **Killed if**, for
  n = 5, the share at (1, 1, 1, 1, 1) misses ⅙ by more than 1e-12, or the share at any of (2, 1, 1, 1, 1),
  (2, 2, 2, 2, 2), (½, 1, 1, 1, 3), (½, ½, 2, 2, 1) is within 1e-6 of ⅙.

Known already: the gnomonic projection of a uniform direction on Sⁿ is the multivariate Cauchy (the multivariate t with
one degree of freedom), its marginals Cauchy of lower dimension; a uniform rank among exchangeable coordinates. What
run 2 adds is the reading: each further party drawn at H keeps every pair's corner, and the reader's near field in all
its readings shrinks to 1/(n + 1).

Result (mpmath at 40 digits; numpy, seed 21; eighteen seconds):

| | prediction | result | |
|---|---|---|---|
| P7 | the even orthant's readings the n-dimensional Cauchy, n = 1 … 5 | the area element to 3.5e-38 at 100 points; every total 1 to 2.3e-41 | not killed |
| P8 | every reading the circle's half-Cauchy; every pair run 1's wedge | to 1.2e-39 and 3.9e-40 | not killed |
| P9 | near in all 1/(n + 1); the count past the corner even over 0 … n | ½, ⅓, ¼, ⅕, ⅙ to 8.3e-17; every count within 2.6 standard errors of 1/(n + 1) | not killed |
| P10 | n = 5: ⅙ only when every party is drawn at H | 0.166667 at (1, 1, 1, 1, 1); 0.195, 0.450, 0.129, 0.097 at the four others | not killed |

The count past the corner, from 10⁷ even points each:

| n | k = 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 1 | 0.4999 | 0.5001 | | | | |
| 2 | 0.3334 | 0.3332 | 0.3334 | | | |
| 3 | 0.2498 | 0.2503 | 0.2500 | 0.2499 | | |
| 4 | 0.2000 | 0.2002 | 0.1998 | 0.2000 | 0.2001 | |
| 5 | 0.1668 | 0.1667 | 0.1664 | 0.1667 | 0.1667 | 0.1667 |

**Reading.**
- **Each further party drawn at H keeps every pair's corner.** The readings are the n-dimensional Cauchy; each reading
  alone is the circle's law and each pair the wedge's (P7, P8). Nothing about the pairs already held changes when a
  party is added.
- **The reader's near field in all its readings is 1/(n + 1).** With one other party it is half the addresses, with two
  a third, with five a sixth; and the number of readings past their corner is spread evenly over 0 … n (P9). It is the
  even sphere treating the n + 1 unit relations alike: h is the largest of them as often as any other.
- **The drawing is the geometry's whole job** (Tom: "from the geometry's perspective, its job is done, what ever the
  true breadth makes no difference"). Drawn unequally, the shares move (P10); drawn at H, nothing here depends on any
  party's true breadth, which never entered the run. Each true breadth is one number of the amounts, a shift in levels
  for that party alone.
