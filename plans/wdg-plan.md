# WDG: the wedge, made with the Cauchy

*13 October 2026 (Tom's local date, about 7:00). Tom: "the unit sphere could point every address in the universe." To Claude's
answer (every place as a direction and a level log₂(|x|/H)): "but that is the unsituated readers sphere, he would have
to know the size if the universe. the situated reader has to sweep and set V = V2 = H. and create the sweep wedge using
the cauchy." Then "yes" to an exact check and a write-up, with: "if we put a rotatable sphere inside the unit cube, we
could show that every point on the sphere maps to every point on the inner cube. the inner cube could be any size,
however its extent must be known." Exact arithmetic (mpmath, 30 digits) and identities checked to rounding.
Predictions written before the script (`wdg/wdg.py`) exists. It builds on `observation-from-somewhere.md` Propositions
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

### Run 1 (13 October, `wdg/wdg.py`)

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
