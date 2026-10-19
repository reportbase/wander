# THL: the arc from the chord, by two rays

*14 October 2026 (Tom's local date). Tom, about 2:28: "the arc is the intersection of the two facings." Then, about
2:29: "the arc is the intersection of the rays that are swept over the two facings from horizontal to vertical." Then,
to Claude's reading (Thales' construction: from the chord's two ends, one ray reading v/h and the other h/v, crossing on
the semicircle), about 2:34: "yes, lean on whatever classical theory best describes this situation." It follows SPN R233
(the arc drawn by the head's turn, not the walk) and R234 (the unsituated view the chord, the situated the arc; the
chord prior to the circle). Exact arithmetic: rational arithmetic (Python's `fractions`) where the points are rational,
and mpmath at 60 digits elsewhere; predictions written before the script (`runs/thl/thl.py`) exists.*

## Set-up, with the case kept

**The chord.** Two parties at its ends, A = (0, 0) and B = (1, 0): the chord AB, of length 1 in the one unit both are
drawn in (V = H). No amount enters; everything below is unit relations and their readings.

**The two facings' rays.** From A a ray swept from horizontal (along AB) to vertical, at angle α above AB; its slope is
the reading s = v/h = tan α (the wedge read facing h, OFS §2). From B a ray reading the flip, h/v = 1/s, so that it makes
the angle β with BA where tan β = 1/s, and α + β = 90°. As A's ray goes from horizontal to vertical, B's goes from
vertical to horizontal. Where the two rays cross is P(s).

**Drawn at V = cH.** The same readings drawn with the vertical at c times the horizontal: A's ray of slope c·s, B's of
slope c/s measured from BA.

**Classical theory leaned on** (Tom: "lean on whatever classical theory best describes this situation"):
- *Thales' theorem* (Euclid, *Elements* III.31), with its converse: the points from which a segment is seen at a right
  angle are the circle on it as diameter.
- *The inscribed angle theorem* (*Elements* III.20): the angle at the centre is twice the angle at the circumference on
  the same arc. Its converse, the arc capable: the points seeing a segment under a fixed angle lie on an arc.
- *Steiner's generation of conics* (Steiner 1832): two pencils of lines at distinct centres, related by a projectivity
  that is not a perspectivity, meet in corresponding lines along a non-degenerate conic through both centres; a
  perspectivity gives a line. The conic is a circle when the two pencils are congruent (one is the other turned by a
  fixed angle).
- *The rational parametrization of the circle*, the tangent half-angle substitution: cos φ = (1 − t²)/(1 + t²),
  sin φ = 2t/(1 + t²) with t = tan(φ/2); at rational t the rational points, and with t = m/n *Euclid's formula* for
  Pythagorean triples (*Elements* X, lemma 1 to proposition 29).
- *The mean proportional* (*Elements* VI.8 and VI.13): in a right triangle the altitude to the hypotenuse is the mean
  proportional of the two pieces it cuts; on a segment x₁ + x₂, the semicircle's height over the join is √(x₁x₂).

## Predictions

- **P1. The crossing traces the semicircle on the chord (Thales).** P(s) = (1, s)/(1 + s²) for every s ≥ 0, and
  |P − (½, 0)| = ½: P runs from B (s = 0) over the top to A (s → ∞), the upper half of the circle on AB as diameter, and
  the rays meet at a right angle. **Killed if**, at s = m/n for all 1 ≤ m, n ≤ 40, the crossing computed by intersecting
  the two lines (not from the closed form) misses (x − ½)² + y² = ¼ in exact rational arithmetic, or the two rays'
  directions fail to be perpendicular exactly; or, at 2,000 values of s spread over 10⁻¹⁰ … 10¹⁰ at 60 digits, any
  distance from (½, 0) differs from ½ by more than 1e-50.
- **P2. The two rays are h and v.** AP = 1/√(1 + s²) = cos α = h and BP = s/√(1 + s²) = sin α = v, with h² + v² = 1
  the chord's square (Pythagoras on the chord). The foot of P cuts the chord into h² (from A) and v² (from B), and the
  height of P is hv, their mean proportional (*Elements* VI.8). **Killed if** any of these misses by more than 1e-50 at
  the 2,000 values of P1, or fails exactly at the rational s of P1 (for the squared lengths).
- **P3. The facing is twice the ray's angle; the reading is the facing's half-angle tangent.** The angle at the chord's
  middle from B to P is φ = 2α (the inscribed angle theorem), so s = tan(φ/2), and P's place on the circle is
  ((1 − s²)/(1 + s²), 2s/(1 + s²))/2 from the middle: the tangent half-angle form. At s = m/n the point is rational and
  (n² − m², 2mn, n² + m²) is a Pythagorean triple (Euclid's formula). **Killed if** φ, measured with atan2 from the
  crossing, differs from 2·atan(s) by more than 1e-50 at the 2,000 values; or, at the rational s of P1, the crossing's
  coordinates from the middle differ from the half-angle form in exact arithmetic, or (n² − m²)² + (2mn)² ≠ (n² + m²)².
- **P4. The corner is at the top, and the flip is the mirror.** At s = 1 both rays stand at 45°, and P = (½, ½), over
  the chord's middle, where AP = BP and φ = 90°. The flip s ↦ 1/s sends P(s) to its mirror image across the chord's
  perpendicular bisector, exchanging A and B. **Killed if** P(1) ≠ (½, ½) exactly, or P(1/s) is not (1 − x, y) for
  P(s) = (x, y) exactly at the rational s of P1.
- **P5. Steiner: a conic in every drawing, a circle only at V = H.** Drawn at V = cH, the crossing satisfies
  x² − x + y²/c² = 0, an ellipse through A and B with the chord as one axis; it is a circle only at c = 1. The
  correspondence between the two pencils (slope t from A to slope c²/t from B, measured from BA) is a projectivity: it
  keeps the cross-ratio of any four lines. It is not a perspectivity: the line AB from A (t = 0) goes to the vertical at
  B, not to AB. **Killed if**, at c = 2, ½, 3 and 1.0001 and the 2,000 values of s, the crossing misses the ellipse by
  more than 1e-45; or, at c ≠ 1 and s between 0.1 and 10 (away from A and B, the only points the ellipse shares with
  the circle), its distance from (½, 0) comes within 1e-6 of ½; or the cross-ratio of four lines from A differs from that of the four
  corresponding lines from B by more than 1e-50 for 50 random quadruples; or the correspondence sends AB to AB.
- **P6. Paired at equal angles instead, the crossing is a line.** If B's ray reads v/h too (the same angle as A's, not
  the flip), the two pencils are in perspective and every crossing lies on the perpendicular bisector x = ½, at height
  s/2: no arc, and no turn of the facing. **Killed if** any crossing at the 2,000 values has |x − ½| > 1e-50 or
  |y − s/2| > 1e-50.
- **P7. The even sweep of one ray is the even turn of the facing, and the readings are the half-Cauchy.** Turning A's
  ray in equal steps of α moves P in equal steps along the arc: with 10,000 equal steps over the quarter turn, every
  chord between successive crossings is the same, sin(Δα)·(radius ½)·2 = sin(Δα). Read as s = v/h, equal steps of α
  are the even turn, so the share of readings at or below s is (2/π)·atan s, ½ at the corner. **Killed if** any of the
  10,000 chords differs from sin(Δα) by more than 1e-50, or the count of the 10,000 step-midpoints with s ≤ 1 is not
  exactly 5,000, or the counted share at s = ½, 2, 10 differs from (2/π)·atan s by more than one step (10⁻⁴).
- **P8. The mean proportional is the corner of two amounts (Elements VI.13).** Lay two amounts x₁ and x₂ end to end as a
  chord of length x₁ + x₂; the crossing over the join has height √(x₁x₂), and there the reading is s = √(x₂/x₁). The
  geometric middle √(x₁x₂), which the corpus finds as the best H for two amounts (HKO P3) and as the corner of any two
  bounds, is Euclid's mean proportional, constructed by the same semicircle. **Killed if**, for 100 pairs (x₁, x₂)
  spread over 10⁻⁶ … 10⁶, the crossing (found by intersecting the rays of reading s = √(x₂/x₁), not from the closed
  form) has its foot off the join or its height off √(x₁x₂) by more than 1e-45 relative.

## What the run would and would not show

All eight are classical identities; the run checks that the reading given them here (the chord first, the two facings'
rays, their crossing) is stated without a slip, and that the drawing V = H is what makes the conic round. It does not
show that a reader draws the arc this way; that is a reading (SPN R235).

## Runs

### Run 1 (14 October; `python3 runs/thl/thl.py`, under 2 s)

```
P1: not killed. exact on 1600 rational readings; worst |PO - 1/2| over 1e-10..1e10: 1.17e-61
P2: not killed. AP = h, BP = v, foot h² | v², height hv; worst 3.11e-61; exact at the rationals: True
P3: not killed. worst |facing - 2 atan s| 3.11e-61; half-angle form and Euclid's triples exact: True
P4: not killed. P(1) = (Fraction(1, 2), Fraction(1, 2)); P(1/s) the mirror of P(s) at all 1600 rationals: True
P5: not killed. ellipse x² - x + y²/c² = 0 to 1.38e-61; nearest to the circle at c ≠ 1, s in [0.1, 10]: 2.0e-6 off; cross-ratio kept to 4.62e-54; AB goes to the vertical at B
P6: not killed. every crossing on x = 1/2 at height s/2, worst 0.0
P7: not killed. 10,000 chords equal to sin(Δα) to 2.34e-61; 5000 of 10000 readings at or below the corner; share vs (2/π)atan s within 4.9e-5
P8: not killed. foot at the join, height √(x₁x₂), worst relative 2.88e-61 over 100 pairs
```

Nothing killed. Notes:
- P5's distance from the circle, 2.0 × 10⁻⁶ against the bound 10⁻⁶, is the drawing c = 1.0001, chosen to sit close to
  V = H: drawn at c the crossing keeps its x and has its height multiplied by c, so its distance from the middle is
  √(¼ + (c² − 1)·y²), off ½ by about (c² − 1)·y² ≈ 2 × 10⁻⁴ × 0.0098 at s = 0.1 (y the height on the circle). Narrow by
  my choice of c, not by the geometry; the other drawings tried (c = 2, ½, 3) are off by more than 10⁻³.
- Before the first run, two things were changed in the set-up, and no prediction: P5's clause was restricted to s between
  0.1 and 10 (near A and B every ellipse through them comes within 10⁻⁶ of the circle, which would have killed it for
  a reason the prediction did not mean); and the script's test that the correspondence is not a perspectivity, at first
  written as a constant, was made a computation (A's line of slope t → 0 goes to B's line of slope −c²/t, unbounded:
  the vertical at B, not AB).

**What it shows.** On the chord drawn at V = H, the two facings' rays, one from each end, reading v/h and h/v, cross on
the semicircle (Thales), at distances h and v from the ends, with the facing twice the ray's angle (the inscribed angle
theorem) and the reading the facing's half-angle tangent (the rational parametrization; Euclid's formula at rational
readings); the corner at the top; the flip the mirror. The two pencils are projectively related and not in
perspective, so by Steiner the crossings lie on a conic through both ends; it is round only at V = H. Paired at equal
angles they meet on a line. An even sweep of one ray is an even turn along the arc, and its readings are the half-Cauchy.
Over two amounts laid end to end, the crossing above the join stands at their mean proportional, the corner of the two.
