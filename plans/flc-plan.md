# FLC: a flat chart for the read in space

7 November 2026. Tom: "whats next", then "proceed" to "the space counterpart of the flat chart … as a plan with
predictions written first".

## The question

In the plane, Euler's plane ln(z/H) = ln(d/H) + iθ does two jobs at once (R736–R740, essay 18): every turn is a slide up
or down and every scaling (of the world or of the thumb) a slide across, and on the thumb's lay (g = ½ + gd(u)/π across,
θ up) the read's measure is flat: its heat per unit of that chart is constant (R737, `chartHeat`). Is there a chart in
space that does the same, one in which the read's measure is flat and every turn is a rigid move?

## Known beforehand

- The log-polar map in any dimension: x ↦ (u, ω) = (ln(|x|/H), x/|x|) takes the flat metric divided by |x|² to the
  product metric du² + dω², a cylinder ℝ × S^(n−1) (classical; the map is conformal). In the plane ℝ × S¹ is flat (it
  unrolls), which is why Euler's plane exists; in space ℝ × S² is not.
- Gauss's theorema egregium: no chart of a piece of the sphere is an isometry onto a flat region, so no flat chart takes
  every turn of the sphere to a rigid motion. Euler (1777): no map of the sphere is both conformal and equal-area.
- Lambert's azimuthal equal-area map about a pole, R = 2·sin(α/2), keeps area; its Tissot scales are cos(α/2) radially
  and 1/cos(α/2) across. The stereographic map w = 2·tan(α/2) keeps angles; its area factor is (1 + w²/4)⁻².
- draw's *The Tangent Bridge* §15.2 ("The measure the torus carries"): the even pan × tilt grid is not the uniform measure
  on directions. Wander's EUL (`plans/eul-plan.md`) and essay 13: in space the plane's one law parts into several, and
  turns of space do not commute (`euler.html`'s space view: 120° apart for two quarter turns; a small loop α·β).

So the outcome is mostly forced by classical results. What the test settles is the exact shape of the failure and what
survives: which job the space chart can keep, which it must give up, and by how much.

## The read's measure

The read (R700, R702) is the hemisphere of directions in front of the look, uniform by solid angle, (1/2π)·dΩ, and in
distance the thumb's overlay, (1/π)·sech(u)·du with u = ln(d/H). Their product is the read's measure on (direction,
distance).

## Predictions (written before any run)

- **F1 (the cylinder).** The map x ↦ (ln(|x|/H), x/|x|) from space less the eye onto ℝ × S² is conformal with factor 1/|x|:
  the pulled-back metric of du² + dω² is |dx|²/|x|², to 10⁻¹² at 1,000 seeded points (finite differences in mpmath at 40
  digits, so the tolerance is the differencing's). Kill if any point departs by more than 10⁻¹⁰.
- **F2 (writing is still a slide, and still commutes).** Scaling the world by k, or the thumb by 1/k, is u ↦ u + ln k with
  ω unmoved, exactly; it commutes with every turn of space, exactly (both orders land within 10⁻¹⁴ of each other on 1,000
  seeded points and 100 seeded turns, in doubles). Kill if not.
- **F3 (the flat chart for the measure).** On Lambert's azimuthal map about the look (the disc of radius √2 for the
  hemisphere) crossed with the thumb's lay g, the read's measure has the constant density 1/(2π) per unit of chart area
  (disc area times g). Checked two ways: the Jacobian identically (to 10⁻¹²), and 2·10⁶ seeded draws from the read's
  measure binned into 16 × 16 × 16 cells of equal chart volume, every cell's count within 5 standard errors of the mean.
  Kill if either fails.
- **F4 (turns keep the measure, not the shape).** Turning the look by φ about an axis square to it, pulled back to the
  Lambert chart, keeps area exactly (Jacobian 1 to 10⁻¹¹ over the directions in both hemispheres) for every φ, so the heat
  stays flat under every turn. But it is rigid only for turns about the look: for φ ≠ 0 its largest stretch
  (Tissot's σ) at the old look is exactly 1/cos(φ/2) (√2 at φ = 90°), and at the two directions square to both looks it is
  the largest singular value of [[cos φ, −½·sin φ], [2·sin φ, cos φ]], which is 2 at φ = 90°; over all directions in both
  hemispheres the largest stretch is at most 2 for every φ ≤ 90°, reaching 2 only at φ = 90°. Kill if any number differs
  by more than 10⁻⁹ or the bound fails on a grid of 400 × 400 directions at φ = 15°, 30°, …, 90°. (Method: the Jacobian
  and the named stretches at 2,000 seeded directions a φ in mpmath at 30 digits, central differences of step 10⁻¹²; the
  grid in doubles, step 10⁻⁵, for the bound only, allowed 10⁻⁶ over 2.)
- **F5 (the conformal chart instead).** On the stereographic chart about the look (w = 2·tan(α/2), the hemisphere a disc
  of radius 2), every turn is a Möbius map (angles kept: the two Tissot scales equal to 10⁻⁹ at 1,000 points and 10
  turns), but the measure is not flat: the read's density per unit of chart area at the rim is exactly ¼ of the
  centre's. Kill if the scales differ or the ratio is not ¼ to 10⁻¹².
- **F6 (the plane, the contrast).** The same construction one dimension down (θ × g) has every turn rigid (a slide in θ,
  stretch exactly 1) and the measure flat, at once. Kill if not.
- **F7 (no third way).** Of 2,000 seeded smooth charts of the hemisphere (Lambert and stereographic composed with random
  area-preserving or conformal disc maps), none has both a turn of 30° rigid (σ < 1 + 10⁻⁶ everywhere) and the measure
  flat. A demonstration of Gauss and Euler on examples, not a proof. Kill if one is found (that would be my error).

What the answer would then say: in space the read's two jobs part. Writing (scaling) is still a slide on the cylinder's
straight direction and commutes with every reading; the read's measure can be laid flat (Lambert × the lay); but no
flat chart makes the turns rigid, because the sphere of directions is curved. The plane is the one case where a single
chart does both, the same parting as essay 13's.

## Runs

**Run 1** (7 Nov 2026; `python3 runs/flc/flc.py`, output `runs/flc/flc-run1.txt`, about 2 minutes). Nothing killed.

| | prediction | measured | |
|---|---|---|---|
| F1 | the log-polar map conformal onto ℝ × S², metric \|dx\|²/\|x\|² | worst departure 7·10⁻²³ (1,000 points) | not killed |
| F2 | scaling a slide in u, commuting with every turn | worst difference 1.4·10⁻¹⁵ in either order (100 turns, k from 10⁻⁶ to 10⁶) | not killed |
| F3 | Lambert × the lay flat for the read's measure | Jacobian 1 to 3·10⁻²⁶; 2·10⁶ draws in 4,096 equal cells, worst 3.52 standard errors | not killed |
| F4 | turns keep area, stretch 1/cos(φ/2) at the old look, the matrix's σ at the square directions, at most 2 | det 1 to 7·10⁻¹⁸; at 90°: √2 and 2.0 exactly; at 15°, 30°, 45°, 60°, 75°: 1.0086, 1.0353, 1.0824, 1.1547, 1.2605 and 1.2128, 1.4430, 1.6623, 1.8419, 1.9593; grid maxima 1.211 … 1.988, all ≤ 2 | not killed |
| F5 | stereographic: turns conformal, the rim's density ¼ of the centre's | anisotropy 9·10⁻¹⁶; ratio 0.25 | not killed |
| F6 | the plane's (θ, g): turns rigid, measure flat | turn's Jacobian the identity; 10⁶ draws, worst 4.28 standard errors | not killed |
| F7 | no random chart both flat and rigid under a 30° turn | 0 of 2,000 | not killed |

Notes after the run. F1 and F5 are classical and were checked, not discovered; F6 holds by construction (the plane's turn
is θ ↦ θ + φ), so its check is of the draws, not of the turn; F7 is a demonstration on examples, Gauss's theorem the
proof. The stretch at the old look agreed to 10⁻¹¹ (read 10⁻⁹ off the centre, where the polar form's differences are
singular), inside the stated 10⁻⁸. The grid's 90° maximum, 1.988, is short of 2 only because the grid misses the exact
direction (1, 0, 0); the mpmath value there is 2.0.

What it says. In space the plane's one chart splits:
- **Writing is still a slide.** On the cylinder ℝ × S² (the log-polar map, conformal in any dimension), scaling the world
  or the thumb moves u alone and commutes with every turn of space. What R740 called "writing across" survives whole.
- **The read's measure can be laid flat.** Lambert's azimuthal equal-area map about the look, crossed with the thumb's
  lay g, carries the read's measure (uniform by solid angle, sech in distance) at the constant density 1/(2π). Every turn
  keeps that chart's area exactly, so the heat stays flat whatever the look does.
- **But no flat chart makes the turns rigid.** The same turn that keeps area bends the chart: a turn of the look by φ
  stretches the old look's direction by 1/cos(φ/2) and the directions square to both looks by up to 2 (at a quarter
  turn), and over both hemispheres never by more than 2. The conformal chart (stereographic) keeps every turn's angles
  but not the heat (a quarter of the centre's at the rim). Gauss and Euler say no chart does both; on Euler's plane one
  chart does both, because ℝ × S¹ is flat.
So "reading up and down, writing across" (R740) holds in space for writing and for the measure, not for the turns: there
is no single straight "up" for reading in space, only the sphere of directions with its own turns, which commute neither
with each other (essay 13) nor with any flat drawing of them.
