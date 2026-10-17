# HTP: parallax from turning the head

*17 October 2026 (Tom's local date). Tom, 12:14: "can you get parallax from just rotating your head"; 12:16: "yes", to
Claude's answer going into OFS (SPN R339, OFS §9 "Turning in place gives no parallax"); 12:59: "1,2,3", whose second
item was this test (SPN R340). Predictions written before the script (`htp/htp.py`) exists.*

## The claim (R339)

A turn about the point the reader sees from gives directions, the frame and the corner, and no distance. A head is not
a pure turn: the eye's centre of projection sits a distance r from the axis it turns about, so a turn through Δ carries
it along a chord B = 2r·sin(Δ/2), and that translation is a baseline. The parallax is the translation's, not the
turn's; in the reader's own unit (r, or anything it is laid in) the chord sizes things against itself, and metres need
r carried in.

## Set-up (exact, mpmath at 50 digits)

The head's axis at the origin, facing +y at the start. The eye at E(Δ) = r·(sin Δ, cos Δ) after a turn Δ, facing the
turned direction. A point P is read as a bearing in the head's frame: the angle of P − E(Δ) from the facing. Two looks,
at Δ = 0 and Δ = Δ₁, the turn Δ₁ known (felt, or read from anything far). Triangulation: each bearing, turned back into
the start frame, is a ray from its eye position; the two rays cross at P.

## What was known before writing

- Classical: motion parallax, stereo triangulation, the nodal point's offset from the eye's centre of rotation.
- **Ocular parallax** (found by a search made while writing this plan, before the script): the eye's nodal point sits
  about 7.6 mm in front of its centre of rotation (Atchison 2017, as cited by Konrad, Angelopoulos and Wetzstein,
  "Gaze-contingent ocular parallax rendering for virtual reality", ACM TOG 2020; arXiv 1906.09740), so turning the eye
  alone gives a small parallax; they report it an effective ordinal depth cue in VR. Santini and Rucci (2006, 2007)
  built a robot with the human eye's geometry and found the parallax from small gaze shifts gives reliable depth at
  nearby distances. Chameleons and the sandlance rely on it. The head's eye-to-neck-axis distance r ≈ 0.1 m is taken
  here as an assumption, not a measurement.

## Predictions

- **P1 (a pure turn gives no parallax).** With r = 0, the angle between the bearings of any two points is the same
  before and after any turn (to 10⁻⁴⁰), and the triangulation is singular: the two rays from one eye position are the
  same ray, nothing is placed. *Killed* if any pair's angle changes, or a point is placed.
- **P2 (the chord is the baseline).** With r > 0 and 0 < Δ₁ < 180°, the two eye positions are 2r·sin(Δ₁/2) apart, and
  triangulating the two bearings with the turn and r known recovers every point exactly (to 10⁻⁴⁰), for points at
  distances from 0.5 r to 10⁶ r in every direction seen in both looks. *Killed* if any point is off.
- **P3 (in the reader's own unit).** With r not known, the reader can lay everything in r: every recovered distance
  over r, and every ratio of distances, is unchanged when the world and r are scaled together by k = 10⁻³, 7, 10³ (to
  10⁻⁴⁰). To write metres needs r. *Killed* if any reading in r moves with k.
- **P4 (the reach).** For a point straight ahead at distance d from the axis, the parallax angle (the angle the chord
  subtends at the point, which is what the bearings differ by against a point at infinity) is to first order
  r·sin Δ₁/d: the eye's sideways step, not the chord. So the farthest point placed by a reader of resolution ε is
  d_max ≈ r·sin Δ₁/ε, largest at a quarter turn, not a half (at Δ₁ = 180° the eye steps straight back). *Killed* if the
  exact d where the parallax equals ε differs from r·sin Δ₁/ε by more than 1% for ε = 10⁻³ and Δ₁ = 30°, 90°, 150°.
- **P5 (the numbers).** Arithmetic on the values above, recorded so they can be compared with what is known:
  - the head, r = 0.1 m, a quarter turn: d_max = 100 m at ε = 1 mrad, about 344 m at ε = 1 arcmin;
  - the eye alone, r = 7.6 mm, a 10° gaze shift, ε = 1 arcmin: d_max ≈ 4.5 m, "nearby distances" as Santini and Rucci
    found. *Killed* if this lies outside 1 to 10 m.
- **P6 (fixating).** If the reader keeps one point F, at distance d_F straight ahead, fixed in view while turning (as
  the eyes do), a point on the same line of sight shifts against F by a signed amount that is zero only at d = d_F and
  opposite in sign nearer and farther (classical); with r = 0 nothing shifts at all. *Killed* if the sign does not change
  exactly at d_F, or anything shifts at r = 0.

## What would and would not be shown

P1–P4 make R339 exact: the parallax of a head turn is the eye's translation, with no contribution from the turn, and
the reach is set by the eye's sideways step over the resolution. P5 compares the reach with what is known of ocular
parallax; it does not test human perception. Nothing here says how a brain reads the parallax, only what the geometry
gives.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (17 Oct, `python3 -I htp/htp.py 1`; output `htp/htp-run1.txt`)

- **P1 killed, by my set-up.** The largest change in a pair's angle came out 6.28, which is 2π: a pair's angle
  difference crossed ±π and wrapped, and I compared it without reducing it to one turn. No point was placed.
- P2 not killed: 95 points recovered from 0.5 r to 10⁶ r, largest relative error 1.5·10⁻⁴⁴; the eye's two places
  2r·sin(Δ₁/2) apart to 3·10⁻⁵².
- P3 not killed: every reading in r unchanged by k = 10⁻³, 7, 10³, to 10⁻⁴⁴.
- P4 not killed: the exact reach at ε = 10⁻³ is 50.087 m, 100.000 m and 49.913 m at 30°, 90°, 150° against
  r·sin Δ₁/ε = 50, 100, 50 m: off 0.17%, 3·10⁻⁷ and 0.17%.
- P5 not killed: the head (r = 0.1 m, a quarter turn) 100 m at 1 mrad, 343.8 m at 1 arcmin; the eye alone (7.6 mm, a
  10° gaze shift, 1 arcmin) 4.54 m.
- P6 not killed: fixating a point 2 m off, points on the line of sight shift +0.094, +0.029, +0.009 rad nearer (0.5, 1,
  1.5 m) and −0.009, −0.021, −0.026 farther (3, 10, 1000 m), zero at 2 m; with r = 0 nothing shifts.

### Run 2 (17 Oct, `python3 -I htp/htp.py 2`; output `htp/htp-run2.txt`)

**P1′**, P1 as written with each pair's angle taken modulo a whole turn (stated before the run): the largest change
1·10⁻⁵⁰, no point placed. Not killed. P2–P6 as in run 1.

**Reading.** A head turn's parallax is the eye's translation: with the eye on the axis no pair's angle changes and
nothing is placed; off it, the eye's two places are a chord 2r·sin(Δ/2) apart and every point is recovered exactly,
in r, unchanged by scaling the world with r. The reach is set by the eye's sideways step, r·sin Δ, over the resolution,
so a quarter turn reaches farthest, a turn of 150° no farther than one of 30°, and a half turn, which steps the eye
straight back, not at all. The eye's own turn alone reaches a
few metres, as Santini and Rucci found by robot. Fixating, near points move one way and far points the other, the
fixated distance between them; with no offset, nothing moves.
