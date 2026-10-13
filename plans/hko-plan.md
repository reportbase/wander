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
