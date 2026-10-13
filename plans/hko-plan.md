# HKO: H kicks off the chain

*13 October 2026 (Tom's local date, about 12:50). Tom: "draw.html has demos of this idea. how to recover the shape.
lets build stand alone demos of H kicks of the entire chain of logic. explore what H acutally is. what is H of 0. what
is H of infinity. Picking an H creates the unit relational space. The number of V's determine its shape, but we don't
actaully sweep the full shape, we sweep the cauchy fisheye of it. the shape is constructed virtually, over many
observations, which implies that it might have something to do with parallax." It follows SPN R226 (H is not a measured
size but the value the reader chooses to start the system; the geometry a shape and one H) and R227 (physics assigns
the values). Exact arithmetic (mpmath); predictions written before the script (`hko/hko.py`) exists. The pages that
show it come after the run.*

## Set-up, with the case kept

**Amounts:** H > 0, the value the reader chooses to start the system; x > 0, amounts in a world (given from nowhere,
or once physics has assigned values, R227); a and b, the ends of a window of amounts; d, a distance; B = 2H, a
baseline.

**Unit relations and readings:** an amount read against H is s = x/H, placed at the direction θ = arctan s on the
quarter circle, from home (θ = 0) to the horizon (θ → 90°), the corner at θ = 45°, x = H.

**The lays** (OFS §6): the reader's lay L(s) = s to the corner and 1 + ln s past it; the in-place lay I(s) = s to the
corner and 2 − 1/s past it. On a window, a lay is compared with a ruler up to an affine map (a ruler's form, OFS
Proposition 14): normalized to run from 0 at a to 1 at b.

**The question.** What is H? Every reading of directions is the same at every H (OFS Proposition 3(b)); H enters only
where amounts are placed. So "H of 0" and "H of ∞" are asked of the placing: where the world lands, what its lay
becomes, and what parallax with half-baseline H can recover.

## Predictions

- **P1. The two limits of H are the two corner-free rulers.** On any window [a, b]: once H ≥ b, both lays are x/H on
  it, affinely the number line (normalized, (x − a)/(b − a)); once H ≤ a, the reader's lay is 1 + ln(x/H), affinely
  the logarithm (ln(x/a)/ln(b/a)), and the in-place lay 2 − H/x, affinely the reciprocal ruler
  ((1/a − 1/x)/(1/a − 1/b)). These are OFS Proposition 14's rulers that favour no amount: the power p = 1, the
  logarithm, the power p = −1. Only for a < H < b does the window hold a corner: the lay's second derivative jumps there
  and nowhere else, at x = H. **Killed if**, on the windows [1, 10], [10⁻³, 10³] and [2, 2.5], at H = b, 10b, 10⁶b and
  at H = a, a/10, a/10⁶, any normalized lay misses its ruler by more than 1e-30 at 50 points; or, at H = √(ab), a
  normalized lay is within 1e-3 of every point of any of the three rulers; or the second derivative from the left and
  the right differs by less than 1e-6 (relative) at x = H, or by more than 1e-25 at any of 20 other points.
- **P2. Lost three ways.** With a finite count, n addresses across the near field and the reader's lay held to L_max
  levels, a world on [a, b] is lost whole at both ends of H, in three different ways: as H grows, into home's first
  address once H ≥ n·b (both lays); as H shrinks, past the held far edge once H < a·e^(1 − L_max) (the reader's lay,
  where the world keeps its width ln(b/a) and only moves out), or into the horizon's last address once H ≤ a/n (the
  in-place lay, where the world shrinks to width H(1/a − 1/b)). **Killed if**, for the world 10^(k/5), k = −15 … 15,
  with n = 32 and L_max = 12, the count of distinct addresses held is not 1, 0 and 1 just past each threshold (by a
  factor 1.001), or is still 1, 0 and 1 just short of it.
- **P3. The best H to tell two amounts apart is their geometric mean.** For two amounts x₁ < x₂, ratio r = x₂/x₁, the
  angle between them on the quarter circle, arctan(x₂/H) − arctan(x₁/H), is largest at H = √(x₁x₂), the corner of the
  pair, where it is 2·arctan(√r) − 90°; it falls to 0 as H → 0 and as H → ∞; and in levels of the reading the two are
  ln r apart at every H. So H decides how much of the quarter turn a world takes, never its pattern in levels.
  **Killed if**, for r = 2, 10, 10⁶ (x₁ = 1, 7 and 10⁻³), the maximizing H found by root-finding misses √(x₁x₂) by more
  than 1e-25 (relative), the maximum misses 2·arctan(√r) − 90° by more than 1e-30, or the angle at H = x₁·10⁻⁸ or at
  H = x₂·10⁸ exceeds 1e-6 rad.
- **P4. Parallax's half-baseline is an H, with the same two limits and the same best value.** Two standpoints a
  baseline B = 2H apart read a target on the bisector at distance d. From the triangle alone (d = H/tan(γ/2), γ the
  angle the baseline subtends), the relative error of d per unit error of γ is 1/sin γ = cosh(ln(d/H)): 1 at the corner
  d = H, growing without bound as H → 0 and as H → ∞. Over targets at every distance in [a, b], the worst of it is least
  at H = √(ab), where it is cosh(½·ln(b/a)). **Killed if** the relative error computed by differentiating d(γ) in
  mpmath misses cosh(ln(d/H)) by more than 1e-25 at 30 points; or, for [a, b] = [1, 100], [10⁻³, 10³] and [5, 6], the
  minimizer of the worst error (golden-section search in ln H, then the analytic optimum's check) misses √(ab) by more
  than 1e-12 (relative), or the least worst error misses cosh(½·ln(b/a)) by more than 1e-20; or the error at a single
  target is below 10⁶ at H = d·10⁻⁷ or H = d·10⁷.

Known already: Proposition 14's rulers (Luce 1959); the Thales circle and stereo's error; the geometric mean as the
centre of a range in levels. What HKO adds is the reading: H is the one amount the reader's lay favours, its limits are
the rulers that favour none, and the best H for laying a world, for telling two amounts apart and for a parallax
baseline is the same corner, the geometric middle of what is read (as Proposition 13's best estimate within bounds).

## Runs

### Run 1 (13 October, `hko/hko.py`)

mpmath at 60 digits; under a second.

| | prediction | result | |
|---|---|---|---|
| P1 | past the window's ends the lays are the corner-free rulers; a corner only with H inside, at x = H | the number line, the logarithm and the reciprocal to 4.8e-55; with H = √(ab) every lay at least 0.007 from every ruler; the form's jump at x = H 1.0 (relative), elsewhere 7e-74 | not killed |
| P2 | lost into home, past the edge, into the horizon, at H = n·b, a·e^(1 − L_max), a/n | just past: 1 address (home), 0 held, 1 address (horizon); just short: 2, 1, 2; at H = 1 the world holds 24 addresses on the reader's lay, 17 on the in-place | not killed |
| P3 | the best H for a pair √(x₁x₂), widest angle 2·arctan(√r) − 90° | exact (0.0 relative) at r = 2, 10, 10⁶; 19.47°, 54.90°, 89.89°; 1e-8 rad at the ends | not killed |
| P4 | parallax's error per step cosh(ln(d/H)); the best half-baseline over [a, b] √(ab), worst error cosh(½ ln(b/a)) | to 3e-61; √(ab) to 8e-36; 5.05, 500.0005, 1.0042 to 4e-33; 5×10⁶ at H = d·10^±7 | not killed |

**Reading.**
- **H is the one amount the lay favours, and its limits favour none.** Push H past the top of whatever is read and the
  lay there is the number line; push it below the bottom and it is the logarithm (on the in-place lay, the reciprocal).
  These are exactly the rulers of OFS Proposition 14 that favour no amount. A corner exists only where H sits among
  the things read. H of ∞ is the number line, H of 0 the logarithm: neither is a reader's lay.
- **At both ends the world is lost, three ways.** H very large puts every amount in home's first address; H very small
  sends every amount past the held levels on the reader's lay, where it keeps its width in levels and only moves out,
  or into the horizon's last address on the in-place lay, where it is squeezed to nothing. "Picking an H creates the
  unit relational space": only a finite H spreads amounts over the quarter turn at all.
- **The same corner, three times.** The best H to tell two amounts apart is their geometric mean; the best
  half-baseline for parallax over a range of distances is the range's geometric mean; and OFS Proposition 13's best
  estimate within bounds is the bounds' geometric mean. Each puts what is read at the corner, as OFS §8 says for one
  thing. In levels the pattern never depends on H (P3: two amounts are ln r apart at every H); H decides only how much
  of the quarter turn, and of parallax's band, the world takes.
- **Parallax's half-baseline is an H** with the same two limits: a baseline of nothing leaves one standpoint and rays;
  an endless one puts every target near the baseline, where depth fails as badly. The shape built over many
  observations is built at a baseline, and the baseline is a choice of H.

Post hoc, from the numbers: the widest angle between two amounts is arcsin((r − 1)/(r + 1)) (19.47° at r = 2), the
same as 2·arctan(√r) − 90°.

### Run 2 (13 October; `hko/hko2.py`): detail per object

*Tom, about 13:14: "small H gives good fidelity to nearby objects, large h gives good fidelity to far away objects.
larger H moves the corner further away from the observer, which gives more proportional space. reader has fixed number
of addresses, so more proportional space means each object is given less level of detail." Then, to Claude's
per-object form, "Yes, and the OFS paper." Predictions written before the script.*

**Set-up.** An object spans the amounts [d, d + Δ] (a distance and an extent, or any stretch of amounts); the reader
has n addresses across its near field, so the number of addresses the object spans is n times the stretch of lay it
covers: the room it is given, whose log₂ is its level of detail (OFS §8, "Size sets the level").

- **P5. What a larger H gives and takes.** (a) Inside the corner (d + Δ ≤ H) the object spans nΔ/H: every doubling of
  H takes one level of detail from it. (b) Past the corner (d ≥ H) it spans n·ln(1 + Δ/d) on the reader's lay, whatever
  H is, and nΔH/(d(d + Δ)) on the in-place lay, which grows with H. (c) So, as H runs from 0 to ∞, the object's span
  on the reader's lay is constant until H reaches d and falls after; on the in-place lay it rises until H reaches d and
  falls after d + Δ, largest with the object at the corner (H in [d, d + Δ]), where it is within a factor 1 + Δ/d of
  nΔ/d. **Killed if** the spans counted from the lays by mpmath (the lay's value at d + Δ minus at d, times n) miss the
  closed forms of (a) and (b) by more than 1e-30 (relative) for d = 1, 10, 1000 and Δ/d = 10⁻³, 0.1, 1, at H spread
  over 10⁻³d … 10³d; or the reader's-lay span varies by more than 1e-30 over H ≤ d; or the in-place span's largest value
  over 2,001 values of H (log-spaced, plus d and d + Δ) is at an H outside [d, d + Δ], or misses nΔ/d by more than a
  factor 1 + Δ/d.

Result (mpmath at 60 digits; seconds):

| | prediction | result | |
|---|---|---|---|
| P5 (a), (b) | the spans nΔ/H inside the corner; n·ln(1 + Δ/d) and nΔH/(d(d + Δ)) past it | to 2e-58 and 1e-55 | as predicted |
| P5 (c) | the reader's lay flat over H ≤ d; the in-place largest with H in [d, d + Δ], within a factor 1 + Δ/d of nΔ/d | flat to 6e-59; largest at H/d = 1.001, 1.042, 1.413 for Δ/d = 0.001, 0.1, 1 (inside), but for Δ/d = 0.001 its value 0.031968032 equals the bound nΔ/(d + Δ) and failed the comparison | **killed** |

**P5 killed by my set-up, not by the geometry.** The grid of 2,001 values of H steps by a factor 1.007 and so has no
value inside [d, d + Δ] when Δ/d = 0.001 except the two ends I added; the largest it found was at H = d + Δ, where the
span is exactly nΔ/(d + Δ), the lower bound I had set, and rounding decided the comparison. Post hoc, found after the
run: with H inside [d, d + Δ] the in-place span is n·(2 − H/(d + Δ) − d/H), whose largest value is at
H = √(d(d + Δ)), the geometric middle of the object's own ends, where it is 2n·(1 − √(d/(d + Δ))) (18.745 at
Δ/d = 1, at H/d = √2; the grid found 18.745 at 1.4125). The reader's-lay span there is n·(1 + ln((d + Δ)/H) − d/H),
falling for H ≥ d, so the reader's lay has no peak, only its flat run up to d.

### Run 3 (13 October; `hko/hko3.py`): the peak found by search

*Prediction written before the script, after run 2's diagnosis.*

- **P5′. The in-place lay gives an object most detail at the corner of its own ends.** The in-place span is largest at
  H = √(d(d + Δ)), where it is 2n·(1 − √(d/(d + Δ))) (→ nΔ/d as Δ/d → 0); it rises for H below that and falls above
  it. On the reader's lay the span is n·ln(1 + Δ/d) for every H ≤ d and falls for every H > d. **Killed if**, for
  d = 1, 10, 1000 and Δ/d = 10⁻³, 0.1, 1, the maximizer found by golden-section search in ln H over [10⁻³d, 10³d]
  misses √(d(d + Δ)) by more than 1e-20 (relative), the largest span misses 2n·(1 − √(d/(d + Δ))) by more than 1e-30
  (relative), or the in-place span fails to rise (or the reader's-lay span fails to fall) between successive values
  of H on a log grid of 400 from 10⁻³d to the peak (or from d to 10³d).

Result (mpmath at 60 digits; golden-section search, 260 steps; seconds):

| | prediction | result | |
|---|---|---|---|
| P5′ | the in-place span largest at H = √(d(d + Δ)), value 2n(1 − √(d/(d + Δ))); rising before it; the reader's lay flat to d and falling after | the peak at H/d = √(1 + Δ/d) to 3.6e-31 (1.0004999, 1.0488088, 1.4142136); the value to 3.1e-58 (0.031976, 2.97839, 18.74517 at n = 32); both monotone as predicted | not killed |

**Reading.**
- **Inside the corner a larger H takes detail; past it, the lays part.** An object of extent Δ at d spans nΔ/H inside
  the corner: more proportional room, the same count, less detail, one level per doubling of H (Tom's point). Past the
  corner, on the reader's lay its detail is n·ln(1 + Δ/d), set by where it is and not by H; on the in-place lay it is
  nΔH/(d(d + Δ)), which grows as H does. A small H reads the near finely; a large H reaches the far, finely on the
  in-place lay and on the reader's lay by moving the held levels outward.
- **The best H for an object is the corner of its own ends**, √(d(d + Δ)), on the in-place lay; for a thin object, its
  distance. With P3 and P4: the best H for whatever is read is the geometric middle of it, whether a pair of amounts, a
  range of distances for parallax, or one object's two ends.
