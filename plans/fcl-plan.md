# FCL: what a place with no facing takes in

24 November 2026. Tom: "that seems important to me. Here is a connection between an shv read, and a dhv read.", "seems to me when V
is not known, the cauchy emerges. And there now seems to be two ways to read, with the SHV and the DHV.", "explore further first.
right, if you don't have a facing, you get all facings at once, kind of like the god's eye view.", then "yes, write the plan and
test".

Exploration only. Nothing here is a ruling; R890, R967 (the dual vantage has no standpoint) and R1173 (never call gravity a read)
stand, and the plan uses a working name, "a faceless take", for a place that takes in every direction at once as a sum, so that
no ruling is pre-empted.

## The claim

A look (the single hemispherical vantage) has a place and a facing: it holds directions kept apart and in order, with no amount.
A thing with a place and no facing takes in every direction at once and cannot keep them apart: what it has is the sum, here
Newton's pull g(p) = Σ mᵢ (xᵢ − p)/|xᵢ − p|³ (G = 1), one arrow. Claude's reading, to be tested: this is not the view from no
standpoint (which holds every thing apart, with its size). The faceless take holds only sums; its direction is unmoved by scaling
and its length is an amount; what it keeps of a far body is its moments in order; several faceless takes at different places
recover a scene as parallax does for looks, with the amount coming too. Whether the takes share a frame matters: a thing with no
facing has no frame of its own, so the arrow's direction means something only against a frame carried in.

Known beforehand, so the run is not mistaken for discovery: all of it is classical. The shell is Newton's (*Principia* I, Prop.
70); the far field as monopole, then quadrupole about the centre of mass, is the multipole expansion (MacCullagh's formula);
recovering sources from field readings is the gravity inverse problem, non-unique from a surface in general (a classical result
of potential theory) and here posed only for a finite number of point masses; a field's value at a point being a sum with no
record of its sources is superposition. PAY (`plans/pay-plan.md`) had the moments (order l down by (R/r)^l) and GRV
(`plans/grv-plan.md`) the sorting by direction. What is tested: the counts (how many numbers a take holds, with and without a
frame), two scalings Claude worked out from the expansion before running, and one detection law. Arithmetic, not evidence about
the world, and no new physics.

## Predictions (committed before any run)

mpmath at 50 digits. Scenes are seeded (Python's `random`, seed stated in the script): masses in [0.5, 2], positions in the cube
[−1, 1]³, takes at distances 3 to 5 from the origin unless said. "Rank" is the number of singular values of the Jacobian above
10⁻³⁰ of the largest.

- **F1** (the shell) At three places inside a uniform unit shell (0, 0.3, 0.9 from the centre) the pull, by quadrature over the
  shell, is zero to 10⁻²⁵, while a look from the same place meets the shell in every direction (share 1, by construction).
  Kill: a pull above 10⁻²⁵. Classical; it can fail only by my quadrature.
- **F2** (one take cannot part amount from distance) A mass m at distance d and a mass 4m at 2d in the same direction give the
  same arrow exactly. Under scaling the world by k = 7 with the masses kept, the arrow's direction is unchanged and its length
  is multiplied by k⁻²; with the masses scaled by k³ (one density), by k. Kill: any miss past 10⁻⁴⁰. An identity, stated as a check.
- **F3** (what a far body leaves) A body of 12 seeded masses within radius 1, read at r = 10·2^j, j = 0 … 7, along a fixed
  generic direction from its centre of mass. The arrow's relative difference from the monopole's (total mass at the centre of
  mass) falls as r^−2 (fitted slope −2 ± 0.05; the dipole about the centre of mass is zero), and with the quadrupole term added,
  as r^−3 (−3 ± 0.05). Kill: either slope outside its band.
- **F4** (two takes sharing a frame, one mass) Two takes read 6 numbers; one mass has 4 unknowns. The two arrows' lines cross
  at the mass (skew distance zero to 10⁻⁴⁰), which places it in baselines by directions alone; |g_A|/|g_B| = (d_B/d_A)² is then
  a check with nothing free; m = |g|·d². Recovered place and mass agree with the scene to 10⁻⁴⁰ in five seeded scenes. Kill: any miss.
- **F5** (two takes detect that a scene is not one mass) Two masses (1 and 1.7) a separation s apart about a point at distance r
  from two takes: the takes' lines miss each other by a distance that goes as s²/r. Fitted slopes: +2 ± 0.05 in s (s = 0.01·2^j,
  j = 0 … 6, r = 10) and −1 ± 0.05 in r (r = 10·2^j, j = 0 … 6, s = 0.1, the takes' places scaled with r). Kill: either slope
  outside its band. (My derivation: each line is off the centre of mass by an angle of order (s/r)², times the distance r.)
- **F6** (counting, with a shared frame) K takes hold 3K numbers; n masses have 4n unknowns. The Jacobian of readings against
  (mass, place) has rank min(3K, 4n) for every n = 1 … 4 and K = 1 … 6, in each of five seeded scenes. So one take holds 3
  numbers whatever n is (a look from the same place holds 2n, a direction per mass, and no mass). Kill: any rank short.
- **F7** (counting, with no shared frame) Without a frame a take holds one number, |g|. With the takes' mutual places known in
  baselines, the Jacobian of the K lengths against (mass, place) has rank min(K, 4n) for n = 1, 2 and K = 1 … 10 in five seeded
  scenes with the takes in general position. With the takes all in one plane, the scene mirrored in that plane gives the same K
  lengths exactly (to 10⁻⁴⁰): a twin no number of coplanar frameless takes removes; with a shared frame the twin's arrows differ.
  Kill: any rank short, or the twin's lengths differing.
- **F8** (the scale test, sorted) Scaling the world by k = 7 with masses kept: every arrow's direction, every ratio |g_A|/|g_B|
  and the place recovered in baselines are unchanged (10⁻⁴⁰); every |g| and the recovered m·(baseline)⁻² move. Kill: any miss.
  An identity; it sorts which of the take's numbers are unmoved and which are amounts.

What would count against the reading: F6 or F7 short of full rank (the take holds less than counted), F3 not falling by orders
(the take keeps more than moments in order), or F5 flat (two takes cannot tell one mass from two).

## Runs

### Run 1 (24 November 2026; `runs/fcl/fcl.py`, output `runs/fcl/fcl-run1.txt`; 3 seconds)

Nothing killed.

| | result | |
|---|---|---|
| F1 | the pull inside the shell 6·10⁻⁵⁸, 5·10⁻⁵⁷, 7·10⁻⁵³ at 0, 0.3, 0.9 from the centre | not killed |
| F2 | m at d and 4m at 2d give one arrow (exactly); under k = 7 the direction stays (10⁻⁵¹), the length × k⁻², one density × k | not killed |
| F3 | off the monopole 9.9·10⁻⁴ at r = 10 to 6.1·10⁻⁸ at 1,280, slope −1.9994; with the quadrupole −2.992 | not killed |
| F4 | two framed takes place one mass and give its amount, five scenes, to 10⁻⁵⁰; the length-ratio check holds | not killed |
| F5 | two takes' lines miss by 2.2·10⁻⁴ at s = 0.1, r = 10; slopes +2.0023 in s, −1.0004 in r | not killed |
| F6 | rank min(3K, 4n) in all 120 cases (n = 1–4, K = 1–6, five scenes) | not killed |
| F7 | rank min(K, 4n) in all 100 cases; a scene mirrored in the takes' plane gives the same lengths exactly, arrows 0.010 apart | not killed |
| F8 | direction, length ratio and place in baselines unmoved (10⁻⁵¹); \|g\| and m/B² both × 1/49 | not killed |

What it says, as a reading (Claude's, not ruled):

- **A faceless take is not the view from nowhere.** At one place it holds three numbers whatever the scene (one, a length,
  with no frame carried in): a sum. Inside the shell it holds nothing where a look meets the shell in every direction. One
  take cannot part amount from distance (F2). The view from no standpoint holds every thing apart, with its size.
- **Its numbers sort by the scale test like everything else.** The arrow's direction, ratios of lengths and a place in
  baselines are unmoved; each length is an amount (F8). So the take has a part that is unmoved by scaling, a single
  direction the world hands it, and a part that is an amount.
- **What it keeps of a far body is moments, in order** (F3): the total at the centre of mass, then a term down by (R/r)², then
  (R/r)³. A look keeps directions in order; the take keeps sums in order of fineness.
- **Several takes recover a scene as parallax does, amount included** (F4, F6): two framed takes place one mass in baselines by
  directions alone and then give its amount, with two numbers to spare; n masses need ⌈4n/3⌉ framed takes. Two takes tell one
  mass from two by their lines missing, by s²/r (F5): a pair closer than about √(r × the takes' grain) is one mass to them.
- **The frame is the price** (F7). A thing with no facing has no frame; without one carried in it holds one number, needs 4n
  takes, and a scene and its mirror in the takes' plane cannot be told apart. The arrow is the one direction it is given, and
  it means something only against a frame, which is a write's (things kept in place) or the dual vantage's.

Limits. All classical, and three of the eight (F1, F2, F8) are identities that could fail only by my code. The counts are
for point masses in general position; a continuous body is not recovered from finitely many takes, and from a closed surface
only its outside moments are (the classical non-uniqueness). Nothing here bears on whether a mass "reads"; that word is Tom's
to rule on. Not in any paper.

### After run 1: Tom's statements (24 November 2026), each with its limits

Recorded as said; nothing here is a ruling, and no paper is changed.

- "remember that cauchy is the stage, not the play itself. Its the heat map and as we have learned the cauchy plays nicely it
  merges and combines and remains a cauchy." Corrects the emphasis of the reading above, which led with the sums and amounts
  (the play). The stage is one: the even spread over directions, landing on a flat plane as the Cauchy, the same for a look
  and for a pull. What differs is the play (paint with no amount; mass with an amount) and how many facings are used (one
  hemisphere; all of it). Where "merges and remains a Cauchy" holds, by what is already run: exactly for stepping back (the
  pull at height h₁ + h₂ is the pull at h₁ spread by the Cauchy of scale h₂; GRV's e^(−kh)) and for readings added (the
  relay, SUM); approximately for sources overlaid, two masses being two Cauchys side by side that become one from afar, the
  difference falling as (size/distance)² (F3). R728's limit stands: heat maps overlaid are a heat map, not one Cauchy.
- "thats why I think this is possibly an importent conceptual insight about gravity, which is such a mystery." Claude's
  reading: a sorting of known gravity, not an explanation. The stage's part (the inverse square, the spread over a plane,
  the fading with height, the merging from afar) is geometry shared with light and with a look; gravity's own part is the
  play (mass as what sits there, one sign, no shielding, G). Not touched: why mass pulls, why with that strength, why the
  mass that pulls is the mass that resists. Where it stops, untested: in Einstein's gravity the mass moves the directions
  themselves, so the play changes the stage.
- "No, its not the complete story, for example, what is gravity specificaly. but lets not get bogged down, lets understand
  each small win to see where it takes us." Small wins, one at a time, each recorded with its limits. The first: **the
  stage is the same for a look and for a pull; only the play and the facings differ.**

## Run 2: does the pull have a corner? Predictions (committed before running)

24 November 2026. Tom: "proceed" (to the first of three next steps Claude offered: "Does the pull have a corner?"). A mass M at
height d over a plane; its pull through the plane is 2πGM times the kernel d/(2π(d² + x² + y²)^(3/2)), total 1. Shares below
are of that total. Then the pull along a line through a uniform ball of radius R. mpmath, 30 digits; "exact" means to 10⁻¹⁸
by quadrature of the kernel itself, not of a formula derived from it. All classical; C2's bound and C3's two numbers are my
own arithmetic and can fail.

- **C1** (one thumb's corner) The strip |x| ≤ d holds exactly ½ of the pull, and the strips |x| ≤ x₀ and |x| ≤ d²/x₀ hold shares
  adding to 1, for x₀/d = 0.2, 0.5, 2, 7. So across one thumb the pull has the look's corner and the look's exchange,
  x ↔ d²/x. Kill: any miss past 10⁻¹⁸.
- **C2** (round the foot) The disc of radius ρ about the foot holds 1 − 1/√(1 + r²), r = ρ/d: half at r = √3. The pairing
  that complements is c ↦ 1 − c in c = 1/√(1 + r²) (equal steps of height on the sphere), fixed at c = ½; it is not the
  reciprocal r ↦ 3/r, which misses 1 everywhere but √3, by an amount whose largest size lies between 0.01 and 0.05.
  Kill: the disc's share off the formula past 10⁻¹⁸, or the reciprocal's largest miss outside [0.01, 0.05].
- **C3** (two thumbs' corner) The square |x|, |y| ≤ a holds (2/π)·arcsin(v²), v² = s²/(1 + s²), s = a/d: exactly ⅓ at a = d (the
  near field in both thumbs, the look's third), and ½ at s = √(1 + √2) ≈ 1.5538. Kill: either number off past 10⁻¹².
- **C4** (along the line, through a body) The pull at distance x·R from the centre of a uniform ball, in units of GM/R², is x
  inside and 1/x² outside, greatest exactly at the surface; computed by integrating the ball's shells, at x = 0.2, 0.5, 0.9,
  1.1, 2, 5 (to 10⁻¹⁰). Places of equal pull are x and x^(−1/2), not x and 1/x: the near field is in proportion and the far
  field falls, as for a look, but the exchange is not the look's. Kill: any value off past 10⁻¹⁰.
- **C5** (the scale test) Every share in C1–C3 is unchanged when d, x₀, ρ and a are all multiplied by 7, and none depends on M.
  Kill: any change past 10⁻¹⁸. An identity.

What would count against "the pull has the look's corners": C1's exchange failing, or C3's third.

### Run 2 (24 November 2026; `runs/fcl/fcl2.py`, output `runs/fcl/fcl2-run2.txt`; 3 minutes)

| | result | |
|---|---|---|
| C1 | the strip \|x\| ≤ d holds ½; strips at x₀ and d²/x₀ add to 1 at all four x₀ (to 30 digits) | not killed |
| C2 | the disc's share on the formula (10⁻³¹), ½ at √3; c ↦ 1 − c complements exactly; the reciprocal r ↦ 3/r misses by up to **0.0607** (at r = 7.33), outside my [0.01, 0.05] | **killed**, by my bound |
| C3 | the square of one thumb each way holds ⅓; ½ at s = 1.553774; the formula to 10⁻³¹ | not killed |
| C4 | outside the ball 1/x² to 12 digits; inside x less 3·10⁻⁶·x | **killed**, by my code: I left a gap of 2·10⁻⁶·x about the shell through the point, and the miss is that gap's mass |
| C5 | strip, disc and square unchanged under ×7 | not killed |

C2's kill is of my guess at the size (I worked it at r = 1 only, 0.023, and guessed the range from that); the claim it
tested, that the reciprocal is not the disc's pairing, holds more strongly than I wrote. C4 is rerun below with the gap
closed, as a new run with its own prediction.

### Run 2b: prediction (committed before running)

- **C4′** The same six values as C4, the inside integral taken up to the shell through the point from each side with no gap:
  x inside and 1/x² outside to 10⁻¹⁰. Kill: any value off past 10⁻¹⁰.

### Run 2b (24 November 2026; `runs/fcl/fcl2b.py`, output `runs/fcl/fcl2b-run.txt`; 2 minutes)

The first attempt did not run: a quadrature node rounded onto the shell through the point and divided by zero (my code).
With that one node given the integrand's limit there, 1/(4x²): **C4′ not killed**, x inside and 1/x² outside at all six
places, largest miss 2·10⁻¹⁷. (Two values carry an imaginary part of 10⁻¹⁹, from a distance rounding a hair below zero
under the 3/2 power; it is below the tolerance and no part of the result.)

### What run 2 says, as a reading (Claude's, not ruled)

**Yes: on the plane the pull has the look's corners, because it stands on the look's stage.**

- **Across one thumb**, the look's corner and the look's exchange, exactly: half the pull lands within one height of the
  foot's line, and the strips at x₀ and d²/x₀ complement (C1).
- **Across two thumbs**, the look's third: the square one height each way holds ⅓ (C3), the same number as the near field
  in both readings of a look (wedge, R220).
- **Round the foot**, half within √3 heights, the same as a look's half within √3 thumbs of the look (R700). The pairing
  that complements there is equal steps of height on the sphere (c ↦ 1 − c), not a reciprocal of radii, which misses by
  up to 0.06 (C2).
- **None of it carries the mass, and none moves under scaling** (C5): the corners are the stage's.

**Along the line the pull has a near and a far, but not the look's exchange** (C4′). Inside a uniform ball the pull is in
proportion to the distance from the centre; outside it falls as the inverse square; it is greatest exactly at the
surface. So the body's own border splits near from far, as Tom said on 24 November ("The physical border is the near
field beyond is the far field"). But places of equal pull are x and x^(−1/2), not x and 1/x: the look's exchange belongs
to directions, and along the line the pull is an amount, with the body's own radius standing where the thumb stands for
a look. The radius is the play's, a size; the thumb is chosen.

Limits. Classical throughout (the Cauchy's marginals, the solid angle of a disc and of a square, Newton's shell theorem).
C5 is an identity. The ball is uniform; a body denser at its centre has its greatest pull inside its surface.

## Run 3: two masses on each other's stage

Tom, 24 November, after run 2: "proceed" (to Claude's next small step: "two masses on each other's stage: whether the
pair has a meeting point of its own, like the pair's corner for two looks").

Set-up. Two point masses, M₁ at the origin and M₂ a distance D along the axis, μ = M₁/M₂. A place on the axis between
them is named by ρ = x/(D − x), its distance from M₁ over its distance from M₂ (a ratio of two distances, no unit). A
place anywhere is named by a and b, its distances from M₁ and M₂. Exact, mpmath, 40 digits; μ = ¼, 1, 4, 9, 81.3.

Said beforehand: every prediction below I worked out on paper before writing it, so each can fail only by my algebra or
my code, not by the world. All of it is classical (the neutral point, the circle of Apollonius, the angle bisector
theorem, Newton's third law). What is being looked for is how it sorts.

### Predictions (committed before running)

- **T1, the meeting point.** The two pulls cancel at exactly one place, on the axis between the masses, at ρ = √μ. Off
  the axis they cancel nowhere. Kill: the axis zero off √μ past 10⁻³⁰; or a second zero found from 400 seeded starts in
  space.
- **T2, the exchange.** On the axis between the masses the pulls' ratio is |g₁|/|g₂| = μ/ρ². The places ρ and μ/ρ have
  reciprocal ratios, and the one place the exchange leaves alone is the meeting point: the look's exchange s ↔ 1/s with
  its corner, moved to √μ. Kill: the product of the ratios at ρ and μ/ρ off 1 past 10⁻³⁰ at any of six ρ.
- **T3, two centres.** The meeting point (ρ = √μ) and the centre of mass (ρ = 1/μ) lie on opposite sides of the middle
  for every μ ≠ 1, with ρ_meet² · ρ_centre = 1; both sit at the middle only at μ = 1. Both are unmoved by scaling every
  length by 7 and by scaling both masses by 7; both move when one mass alone is scaled. Kill: any clause off past 10⁻³⁰.
- **T4, the sphere of equal pulls.** The places where the two pulls are equal in size are a sphere (Apollonius): a/b =
  √μ, centre on the axis at D·μ/(μ − 1) from M₁, radius D·√μ/|μ − 1|; at μ = 1 the plane through the middle. It passes
  through the meeting point. Kill: |g₁| − |g₂| off zero past 10⁻³⁰ relative at any of 200 seeded points of the sphere,
  or zero at any of 200 seeded points off it (nearer than 10⁻³ relative counts as zero).
- **T5, every pull on that sphere aims at the meeting point.** At each place of the sphere the net pull points exactly
  at the meeting point (the inner bisector). Kill: the net pull's direction and the direction to the meeting point
  differing by more than 10⁻³⁰ at any of 200 seeded points.
- **T6, the plane through the meeting point.** Square to the axis there, each mass lays its own Cauchy on the plane, of
  scale its own distance (x and D − x) and total 2πG times its own mass, the two crossing in opposite senses. They are
  equal at the foot and nowhere else: off the foot the heavier's is the larger everywhere, their ratio rising steadily
  from 1 to μ^(3/2) far out (μ > 1). The net crossing is 2πG(M₁ − M₂) through this plane and through every plane
  between the masses, wherever it stands. Kill: either total off 2πGM past 10⁻²⁰; the ratio at the foot off 1 or its
  far limit off μ^(3/2) past 10⁻⁶ (at r = 10⁶ D); the ratio not increasing along 60 radii.
- **T7, shared and owned.** The force on each is the same size (M₂·g₁ at M₂ equals M₁·g₂ at M₁); the accelerations are
  in the ratio 1/μ. An identity, listed for the sorting: the product shared, the ratio owned, as for two looks (MRL).

Not in this run: motion (orbits, the rotating frame's balance points), more than two masses, bodies with size.

### Run 3 (24 November 2026; `runs/fcl/fcl3.py`, output `runs/fcl/fcl3-run.txt`; 25 seconds)

| | result | verdict |
|---|---|---|
| T1 | the pulls cancel at ρ = √μ at all five μ (10⁻⁴²): x = ⅓, ½, ⅔, ¾, 0.9002 D; no other zero from 400 starts | not killed |
| T2 | ratios at ρ and μ/ρ multiply to 1, the ratio μ/ρ², over 30 pairs (10⁻³⁹) | not killed |
| T3 | ρ_meet² · ρ_centre = 1; opposite sides of the middle; unmoved by lengths × 7 and by both masses × 7; one mass × 7 moves it | not killed |
| T4 | equal pulls on the sphere at 200 points (10⁻⁴⁰), at none of 200 points off it | not killed |
| T5 | the net pull aims at the meeting point at all 200 points of the sphere (10⁻³⁹) | not killed |
| T6 | each total 2πGM; the ratio 1 at the foot, rising to μ^(3/2) (8, 27, 733.05); the net the same through another plane | not killed |
| T7 | an identity | not killed |

Nothing killed, and as said beforehand nothing here could have been killed by the world. Not predicted, read off the
output: one lighter-distance out from the foot on the meeting plane the heavier's crossing is already 2.02, 2.41, 2.78
times the lighter's (μ = 4, 9, 81.3).

### What run 3 says, as a reading (Claude's, not ruled)

**Yes: the pair has a meeting point of its own, and it is a corner in the look's sense.**

- **The meeting point is the exchange's fixed point.** Along the line between the two, the pulls' ratio is μ/ρ², and the
  places ρ and μ/ρ carry reciprocal ratios (T2). The one place left alone is ρ = √μ, where the pulls are equal and
  cancel (T1). For two looks the corner is where the readings multiply to 1 (MUT, MRL); here it is where the pulls'
  ratio is 1. The same exchange, with the corner moved from 1 to √μ by the play.
- **Where it stands is a ratio of two masses, nothing else.** It does not move when every length is scaled, or when
  both masses are scaled together; it moves when one mass changes (T3). So its place, in units of the separation, is a
  number without a unit that only the two masses set: by R1178's wording, a ratio of two writes.
- **Two centres, one for each kind of arithmetic.** The meeting point sits at √μ, toward the lighter; the centre of
  mass at 1/μ, toward the heavier; ρ_meet² · ρ_centre = 1 (T3). The centre of mass is a mean (a sum over the masses,
  the play's own arithmetic); the meeting point is the exchange's fixed point (the stage's). They agree only when the
  masses are equal, at the middle.
- **Off the line, the corner is a sphere, and every pull on it aims at the meeting point** (T4, T5). The places of
  equal pull are Apollonius's sphere round the lighter mass; on it the net pull is the bisector, and all the bisectors
  pass through the one meeting point. At equal masses the sphere opens into the middle plane.
- **On the plane through the meeting point each mass lays its own Cauchy, on one stage** (T6): the same law, scales the
  two distances, totals the two masses. They cancel at the foot only. The totals do not cancel and do not depend on
  where the plane stands: 2πG(M₁ − M₂) through every plane between. So the meeting point is a matter of the heat at one
  place, not of the totals.
- **Shared and owned** (T7): the force is the pair's, one number; the accelerations are each one's own, in the ratio of
  the masses. For two looks the product was shared and the ratio owned (MRL); here likewise.

Limits. Classical throughout (the neutral point, Apollonius, the bisector theorem, Newton's third law), and every
prediction was worked out beforehand, so this run is a sorting, not a test. Two points at rest: with the pair in orbit
the balance points are others (Lagrange's), since the turning adds its own term; not looked at. The meeting point is a
saddle, not a resting place (Earnshaw): a thing put there stays only on the line's cross directions.

## Run 4: what motion adds (the pair in orbit)

Tom, 24 November, after run 3: "add it to to a note and proceed. whats next?" (the note: `plans/discussion-note.md`
item 24).

Set-up. The two masses of run 3 on circular orbits about their centre of mass, seen in the frame turning with them
(the classical circular restricted problem). G = 1, the separation D = 1, M₁ + M₂ = 1, m = M₂ the lighter's share, so
the turning rate squared is (M₁ + M₂)/D³ = 1. A small thing at rest in that frame feels the two pulls and the turning's
outward term from the centre of mass. A balance point is where the three cancel. Exact root-finding, mpmath, 30 digits.

Said beforehand: M1, M2, M5, M6 I can derive; M3 and M4 are leading terms I hold from memory and have not derived, so
they can fail by my memory as well as my code. Classical (Euler 1767, Lagrange 1772, Hill 1878).

### Predictions (committed before running)

- **M1, five in place of one.** For every m tried (½, 0.2, 0.01, 10⁻³, 10⁻⁶) there are exactly five balance points:
  three on the line (between the masses, beyond the lighter, beyond the heavier) and two off it. The rest pair had one.
  Kill: a count other than five from 600 seeded starts in the plane.
- **M2, off the line the corner goes back to 1.** The two off the line stand at a = b = D for every m: equal distances
  from both masses, and equal to the pair's own separation. The masses' ratio does not enter their place at all (at
  rest the meeting point stood at √μ). Kill: a or b off D past 10⁻²⁵ at any m.
- **M3, on the line the exponent changes from ½ to ⅓.** The balance point between the masses stands farther from the
  lighter than run 3's meeting point: for small m its distance is D·(m/3)^(1/3) to leading order (at rest D·√m). Kill:
  the slope of ln(distance) against ln m over m = 10⁻⁶ … 10⁻¹² off ⅓ by more than 0.005, or the distance over
  (m/3)^(1/3) farther than 0.01 from 1 at m = 10⁻⁹.
- **M4, two from memory.** (a) The inner and outer points about the lighter stand at r_H(1 ∓ r_H/3), r_H = (m/3)^(1/3):
  (outer − inner)/r_H² tends to ⅔. (b) The point beyond the heavier stands at D(1 − 7m/12) from it to leading order.
  Kill: (a) off ⅔ by more than 0.01 at m = 10⁻⁹; (b) (1 − distance)/m off 7/12 by more than 0.001 at m = 10⁻⁶.
- **M5, equal masses.** At m = ½ the point between stands at the middle, where run 3's did: rest and motion agree at the
  pair's own corner. Kill: off the middle past 10⁻²⁵.
- **M6, the scale test.** Every balance point's place in units of D is unmoved when all lengths are scaled by 7 and when
  both masses are scaled by 7 (the turning rate following from Kepler's law each time); it moves if the turning rate is
  set by hand instead. Kill: any of the five moving past 10⁻²⁰ under either scaling; or not moving when the rate is
  doubled by hand.

### Run 4 (24 November 2026; `runs/fcl/fcl4.py`, output `runs/fcl/fcl4-run.txt`; 32 seconds)

| | result | verdict |
|---|---|---|
| M1 | five balance points at m = ½, 0.2, 0.01, 10⁻³; at m = 10⁻⁶ the search found **one** | **killed**, by my search (see below) |
| M2 | the two off the line at a = b = D at every m where they were found (10⁻²⁷) | not killed |
| M3 | slope 0.33319; at m = 10⁻⁹ the distance 0.00069320, 0.99977 of (m/3)^(1/3); at rest it stood at 0.0000316 | not killed |
| M4 | (a) 0.66666662 against ⅔; (b) 0.5833333333 against 7/12 | not killed |
| M5 | the point between at the middle | not killed |
| M6 | unmoved under both scalings (10⁻²²); the rate doubled by hand moves the inner point 0.027 and 0.093 D | not killed |

M1's kill is my search's, as far as I can tell, not the count's: 120 starts a mass drawn over a box 4.5 by 4 D, Newton's
method, and at m = 10⁻⁶ the net term is tiny all round the circle of radius D, so Newton wanders and only one start
settled. (I also wrote "600 seeded starts" meaning 120 for each of five m; the letter was ambiguous.) It stays killed.
M3 and M4 found the three on the line at that m by bracketing, so three of the five are seen there; the two off the
line were not. Rerun below with its own prediction.

### Run 4b: prediction (committed before running)

- **M1′** At m = 10⁻⁶ and 10⁻⁹: (a) along the line the net term changes sign exactly three times away from the two
  masses (counted on 200,000 points from −3 D to 4 D); (b) from 400 seeded starts within 0.3 D of the circle of radius
  D about the heavier mass, with up to 400 Newton steps, the distinct balance points found off the line are exactly
  two, at a = b = D to 10⁻²⁰. Kill: a count other than three in (a) or other than two in (b), or a, b off D.

## Run 5: light past a mass (does the bending keep the Cauchy family?)

Tom, 24 November: "proceed with 2" (of three next steps offered; this one because it is where a mass acts on the
directions a look receives, the stage itself, and not only plays on it). Run 4b was still running when this was
written; its result is recorded where it finishes.

Set-up, all classical (Einstein 1936; Refsdal 1964): a point mass between the eye and a far sky, weak bending, small
angles, the thin-lens equation. Directions are laid on a flat screen square to the line to the mass, in units of the
Einstein radius (the mass, the distances and the speed of light enter only through that one radius; the factor in it
is general relativity's and is not tested here). A source at y on the screen is seen at u, with y = u − u/|u|²: along
any line through the mass, y = u − 1/u, u a signed position on the line. mpmath, 30 digits; counts seeded.

Said beforehand: L1, L2 and L6 are identities of the lens equation. L3 and L4 I derived on paper (the map u − 1/u
carries the upper half-plane into itself, so it should carry Cauchy to Cauchy; Boole 1857, Letac 1977 from memory). L5's
number is a guess from a few points worked by hand.

### Predictions (committed before running)

- **L1, two images and their exchange.** Every source off the line of sight has two images, on opposite sides of the
  mass, with u₊·u₋ = −1: the exchange u ↔ −1/u, whose fixed circle is the Einstein ring. A source on the line of sight
  is the ring. Kill: the product off −1 past 10⁻²⁵ at any of six y.
- **L2, half inside the ring, whatever the sky.** Each source has exactly one image inside the ring and one outside,
  so half of all images lie within one Einstein radius for every law of the sources (three seeded skies of 20,000: a
  2D Cauchy off centre, a Gaussian, a uniform disc). The outer image is the brighter, by exactly one source's worth:
  the magnifications differ by 1. Kill: a count off N; the difference off 1 past 10⁻²⁰.
- **L3, along a line the family is kept, images to sources.** If the images along a line through the mass are Cauchy
  with point z = m + iγ, their sources are exactly Cauchy with point z − 1/z. For images centred on the mass (z = iγ)
  the sources' scale is γ + 1/γ: least, 2, when the images' scale is the Einstein radius, and the same at γ and 1/γ.
  Kill: the sources' law off Cauchy(z − 1/z) past 10⁻²⁰ in its distribution function at any of seven points, for any
  of four z.
- **L4, along a line, sources to images: two Cauchys, exchanged.** If the sources along the line are Cauchy with point
  w, the images' density is exactly the sum of two Cauchy densities, with points z₁ and z₂ = −1/z₁ the two solutions of
  z − 1/z = w in the upper half-plane: one family member for each image, the pair swapped by the ring's exchange. Kill:
  the density off that sum past 10⁻²⁰ at any of twelve u, for any of three w.
- **L5, over the whole screen the family is not kept.** For a sky that is a 2D Cauchy centred on the mass (scale 1
  Einstein radius), the images' law over the screen is no 2D Cauchy and no pair of them: its density is zero on the
  ring, where every Cauchy is positive. The outer images' radial law stays at least 0.08 from every centred 2D Cauchy
  (largest gap in the distribution function, least over the scale). What breaks it is the stretch round the ring,
  which a line does not have. Kill: density on the ring not zero; or the least gap under 0.08.
- **L6, the scale test.** L1–L5 are stated in Einstein radii and hold for every mass and distance. The radius itself
  is an amount: with the mass fixed and every length scaled by k it scales as k^(−1/2) as an angle. An identity.

### Run 5 (24 November 2026; `runs/fcl/fcl5.py`, output `runs/fcl/fcl5-run.txt`; a few seconds)

| | result | verdict |
|---|---|---|
| L1 | u₊·u₋ = −1 at six y (10⁻²⁸) | not killed |
| L2 | 20,000 inside and 20,000 outside for each of three skies; the magnifications differ by 1 (10⁻²⁹) | not killed |
| L3 | images Cauchy(z) give sources Cauchy(z − 1/z) for four z (10⁻³¹); centred, scale γ gives γ + 1/γ: 4.25, 2.5, 2, 2.5, 4.25 at γ = ¼, ½, 1, 2, 4 | not killed |
| L4 | the images' density is the sum of the two Cauchys at z₁ and −1/z₁, three w, twelve u (10⁻³⁰) | not killed |
| L5 | the image density on the ring exactly 0; inside and outside each hold 1.0; least gap from a centred 2D Cauchy 0.144 (at scale 1.71), above my 0.08 | not killed |
| L6 | an identity, nothing run | not killed |

Nothing killed. Read off the output afterwards, not predicted (both are one line of algebra once seen):

- The two image points add to the source's: z₁ + z₂ = w (0.364 + 0.136 = 0.5 in height at w = 1 + 0.5i). The source's
  standpoint is the sum of its images' standpoints, as added readings add their points (SUM, R358).
- A centred sky of scale exactly 2 Einstein radii has both image points at i: its images along a line are one Cauchy,
  of scale the Einstein radius, counted twice.

### What run 5 says, as a reading (Claude's, not ruled)

**Along a line through the mass the bending keeps the Cauchy family; over the whole screen it does not.**

- **The ring is a corner, and the bending brings the look's exchange with it.** Every source has two images with
  u₊·u₋ = −1 (L1): the exchange s ↔ 1/s, with a change of side, and the Einstein ring its fixed circle. Half of all
  images lie inside the ring whatever the sky is (L2). That is the corner's property (half each side, for every
  payload), but here the corner's place is set by the mass: it is the play's corner, an amount, where the look's corner
  is chosen with the thumb.
- **On a line the lens is one of the family's own maps.** Reading u − 1/u along a line through the mass, Cauchy images
  come from Cauchy sources at z − 1/z (L3), and Cauchy sources are seen as two Cauchys, one for each image, their points
  swapped by the ring's exchange and adding to the source's (L4). So here Tom's "it merges and combines and remains a
  cauchy" holds exactly for the bending: the mass moves the standpoint and doubles it, and leaves the law.
- **The sources' spread is least when the images sit at the ring.** Images centred on the mass with scale γ come from
  sources of scale γ + 1/γ (L3): least at γ = 1, the same at γ and 1/γ. The exchange again, on the scale.
- **Over the whole screen the family breaks** (L5): the images of a Cauchy sky are no Cauchy, their density zero on
  the ring. What breaks it is the stretch round the ring (the tangential magnification), which the line does not have.
  It is the same split as the boosted sky's lens (IMS, `boost-sky.html`): a map that is one of the family's own keeps
  it, a map with a stretch of its own does not. A turn and a boost are the family's own on the whole sky; a mass's
  bending is the family's own only along lines through the mass.

Limits. A point mass, weak bending, small angles, a flat screen; the thin-lens equation is taken, not derived, and the
size of the Einstein radius (general relativity's factor) is not tested. Classical: Einstein 1936 and Refsdal 1964 for
the lens, Boole 1857 and Letac 1977 for u − 1/u keeping the Cauchy (cited from memory, not opened). The statement on a
line is about sources and images along one line through the mass with the line's own measure, not a slice of a 2D sky.
Not claimed: that the bending is a read, or anything about what gravity is.

### Run 4b (24 November 2026; `runs/fcl/fcl4b.py`, output `runs/fcl/fcl4b-run.txt`; about 25 minutes)

Recorded here, after run 5, because it finished after it.

**M1′ killed**, at m = 10⁻⁹, by my code as far as I can tell. At m = 10⁻⁶: three sign changes on the line and two
points off it at a = b = D (10⁻²⁹), so the five are all seen there. At m = 10⁻⁹: four sign changes counted and no point
off the line found. The fourth sign change is the lighter mass's own pole: its pull a grid step away is about 10, under
the 10³ I set to tell a pole from a zero. The search off the line found nothing in 400 starts: at that m the net term
is of order 10⁻⁹ all round the circle, and Newton's method did not settle within 400 steps. Checked afterwards, not a
prediction: at the equilateral place the net term at m = 10⁻⁹ is zero to 30 digits. So the count of five stands
confirmed down to m = 10⁻⁶ and is not established by counting below that; I have not rerun it.

## Run 6: what a facing adds to a pull

Tom, 24 November, after run 5: "proceed" (to Claude's next step: "what a second facing adds: the step between one look
and a pull that sums every direction … the closest test of your 'no facing means all facings at once'").

Set-up. At a place p the scene's pull arrives from directions u. A **faced take** with facing n keeps only what
arrives from in front and only its part along the facing: F(n) = Σ m (n·u)/r² over the masses with n·u > 0 (for a
spread mass, the same as an integral). It is what crosses a small window square to n from the front. The faceless take
of runs 1–5 is g = Σ m u/r². mpmath, 30 digits; seeded scenes of 8 masses.

Known beforehand: the screen law in S4 is ISX's disc (the share 1/(1 + s²) and its exchange), met there for light.
Said beforehand: S1, S3, S5 and S6 are identities I derived; S2's equality is Newton's own argument for the shell
(opposite cones), its size of variation a guess; S4 I derived for this run.

### Predictions (committed before running)

- **S1, a facing and its opposite subtract.** F(n) − F(−n) = n·g for every facing: the faceless take along any line is
  the difference of the two opposite faced takes. Joined, two opposite facings of a pull cancel what they share, where
  two opposite facings of a look are joined by adding. Kill: off past 10⁻²⁵ in any of 10 scenes × 5 facings.
- **S2, the shell, by facings.** Inside a uniform shell, at places 0.3, 0.6 and 0.9 of its radius from the centre,
  F(n) = F(−n) along the line through the centre: the shell's nothing is every facing equal to its opposite, each take
  being far from nothing. The takes do depend on the facing: at 0.9, F across the line and F along it differ by more
  than 1% (a guess). Kill: the pair unequal past 10⁻²⁰; or the two facings within 1% at 0.9.
- **S3, all facings at once.** Averaged over every facing, ⟨F⟩ = ¼·Σ m/r²: a number, the whole sky's amount, with no
  direction. Averaged with its facing attached, ⟨n·F(n)⟩ = g/6: the faceless take is six times the facing-weighted
  mean of the faced takes. So "no facing" is all facings at once, each carrying its own direction; without the
  directions the facings give only an amount. Kill: either off past 10⁻²⁰.
- **S4, a faced take has the look's exchange, with its corner at one thumb.** For a sky alike in every direction, what
  crosses the facing's flat screen (one thumb out) has density 1/(π(1 + r²)²), one more power than the look's heat
  1/(2π(1 + r²)^(3/2)). The share within r of the foot is r²/(1 + r²): half within r = 1, and the shares at r and 1/r
  add to 1 exactly, where the look's half is at √3 and run 2's point mass had no reciprocal pairing. Across one thumb
  the share within x₀ is x₀/√(1 + x₀²), half at 1/√3. Kill: any of these off past 10⁻²⁰.
- **S5, six facings are enough.** The three pairs of opposite facings along any three square axes give g exactly; no
  more facings are needed. Kill: g rebuilt from six takes off past 10⁻²⁵, in 10 scenes with seeded axes.
- **S6, the scale test.** Every F scales as k⁻² with lengths and as the masses; the ratio F(n)/F(−n) is unmoved by
  either. An identity.

### Run 6 (24 November 2026; `runs/fcl/fcl6.py`, output `runs/fcl/fcl6-run.txt`; 47 seconds)

| | result | verdict |
|---|---|---|
| S1 | F(n) − F(−n) = n·g at 50 facings (10⁻³¹) | not killed |
| S2 | inside the shell the two opposite takes equal (0.2559, 0.2778, 0.3482 at 0.3, 0.6, 0.9 of the radius); at 0.9 across the line 0.4358, 25% more than along it | not killed |
| S3 | the means exactly ¼ and ⅙; on a grid of 80,000 facings ⟨F⟩ within 7·10⁻⁶ of the sky's amount over 4 and 6⟨nF⟩ within 2·10⁻⁵ of g | not killed |
| S4 | share within r exactly r²/(1 + r²), ½ at one thumb, r and 1/r adding to 1; across one thumb ½ at 1/√3 (10⁻³²) | not killed |
| S5 | g rebuilt from six takes (10⁻³¹) | not killed |
| S6 | the ratio of opposite takes 0.35158 under both scalings; one take × k² | not killed |

Nothing killed. S2's variation was a guess of "more than 1%"; it is 25%. Read off afterwards: the faced take's two
half-marks (1 round the foot, 1/√3 across one thumb) are the look's (√3 and 1) each divided by √3.

### What run 6 says, as a reading (Claude's, not ruled)

**A facing gives a pull a front, and with the front the look's exchange comes back whole.**

- **"No facing" is all facings at once, each keeping its direction** (S3): g = 6·⟨n·F(n)⟩. Drop the directions and
  all the facings together give only an amount, the sky's total over four. So Tom's sentence holds in this exact
  form: the faceless take is the facings summed with their directions attached. Six of them, three square pairs, are
  already enough (S5).
- **Opposite facings subtract** (S1). For a look, a facing and its opposite are joined by adding (two hemispheres make
  the DHV's whole, 2Ω and 2Ω). For a pull they are joined by subtracting: what is alike in front and behind goes. That
  is the one sign that separates the two plays on the one stage.
- **The shell's nothing is a balance, not an absence** (S2). Inside a shell each facing takes in a good deal (0.26 to
  0.44 of the shell's mass over its radius squared), more across the line to the centre than along it; the pull is
  nothing because every facing equals its opposite (Newton's opposite cones). A look inside the shell sees it in every
  direction; a faced take feels it in every direction; only the difference is nothing.
- **A faced take of an even sky has the look's exchange exactly, its corner at one thumb** (S4): the share within r of
  the foot is r²/(1 + r²), the plane's own share v², half at r = 1, with r and 1/r complementing. The look's heat on
  the same screen has its half at √3 and run 2's single mass had no reciprocal pairing at all. The extra power is the
  facing's own cosine: a pull counts only its part along the facing. It is ISX's disc, met there for light.
- **A pair of opposite takes is a ratio no scaling moves** (S6): F(n)/F(−n) is unmoved by scaling lengths or masses,
  where each take alone is an amount.

Limits. Every prediction but S2's size was derived beforehand; classical (Newton's shell argument, Lambert's cosine,
the mean of a clipped cosine over the sphere). A faced take is a definition made for this run (what crosses a small
window from the front); it is not claimed that any thing in the world takes a pull this way. The even sky in S4 is a
sky alike in every direction in amount per direction, not a mass spread evenly through space.

## Run 7: the sheet, taken by facings

Tom, 24 November, after run 6: "merge, then 2 and 3" (2: "the sheet of mass from the earlier gravity run, taken by
facings, to see whether its Cauchy weighting is this same faced law"; 3: an essay). PR #488 merged before this was
written; this run and the essay are on a new branch.

The question. GRV found the pull above a flat sheet is 2πG times the sheet's density weighted by the 2D Cauchy of the
height, the look's law on a flat screen (half within √3 heights of the foot). Run 6 found that a faced take of a sky
alike in every direction follows another law, r²/(1 + r²) (half within one height). Which is the sheet's, and why?

Set-up. A flat sheet of surface density σ = 1, the take a height h above it, G = 1. A place on the sheet is ρ from the
foot, seen at slope r = ρ/h off the straight-down direction. Faced takes as in run 6. mpmath, 30 digits.

Said beforehand: I worked the answer out on paper before writing this, so the run can fail only by my algebra or code.
Classical (the infinite sheet's 2πGσ; Lambert's cosine).

### Predictions (committed before running)

- **W1, the sheet is not an even sky; it leans.** The sheet's mass over distance squared, per unit of direction, is
  σ·√(1 + r²): more the farther off the straight-down direction, without bound toward the horizon. Kill: the amount in
  thin rings of direction off that by more than 10⁻²⁰ at five r.
- **W2, the lean cancels the facing's cosine, exactly.** Facing straight down, what the sheet sends along the facing
  is the same from every direction: σ per unit of direction, the uniform turn. So on the sheet itself the weight is the
  look's law: share within r equal to 1 − 1/√(1 + r²), half at √3, total 2πσ at every height. It is not run 6's faced
  law. Kill: any share off past 10⁻²⁰; the total off 2π.
- **W3, the two laws are one sheet, thinned or not.** A sheet whose density thins as 1/√(1 + r²) is a sky alike in
  every direction, and its faced take has run 6's share r²/(1 + r²), half at one height, total πσ. Kill: off past
  10⁻²⁰ at four r.
- **W4, between two sheets, a balance.** Between two equal parallel sheets each facing square to them takes in 2πσ
  and the pull is nothing at every height between. Above one sheet the facing away from it takes in nothing, and
  the pull is the one take whole. Kill: either off past 10⁻²⁵.
- **W5, a sideways facing has no limit.** Facing along the sheet, the take from a disc of radius R about the foot is
  2σ·(asinh(R/h) − (R/h)/√(1 + (R/h)²)), growing by 2σ·ln 10 for each tenfold of R and never settling; the opposite
  facing takes the same, so the sideways pull is nothing while each take is without bound. Kill: the take off the
  formula past 10⁻¹⁵ at R/h = 10, 100, 1000; or the growth per tenfold off 2·ln 10 by more than 0.01 between the last
  two.
- **W6, the scale test.** The straight-down take, 2πσ, does not change with the height: at one surface density,
  scaling every length moves nothing. The shares are unmoved too. An identity of W2.

### Run 7 (24 November 2026; `runs/fcl/fcl7.py`, output `runs/fcl/fcl7-run.txt`; a few seconds)

| | result | verdict |
|---|---|---|
| W1 | the sheet's amount per unit of direction is √(1 + r²) at five slopes (10⁻⁴¹): 1.02, 1.41, 2, 5.10, 40.0 | not killed |
| W2 | facing down, the take per unit of direction is 1 at every slope; share 1 − 1/√(1 + r²), half at √3; total 2π | not killed |
| W3 | the sheet thinned by 1/√(1 + r²) is an even sky; its share r²/(1 + r²), half at one height; total π | not killed |
| W4 | between two sheets each facing takes 2π at three places, their difference nothing | not killed |
| W5 | sideways from discs of 10, 100, 1000 heights: 4.006, 8.597, 13.202, on the formula (10⁻²⁵); 4.6050 over the last tenfold against 2·ln 10 = 4.6052 | not killed |
| W6 | an identity of W2 | not killed |

Nothing killed; computed on the sheet, place by place, so the statements about directions were checked from the
other side.

### What run 7 says, as a reading (Claude's, not ruled)

**The sheet's weighting is the look's law, and the reason is a cancellation.**

- A flat sheet is not a sky alike in every direction: seen from above it leans, carrying √(1 + r²) times as much per
  unit of direction at slope r as straight down (W1), because a slanted line of sight crosses more of it and its far
  parts lie behind one another in direction.
- A pull, taken with a facing, counts only its part along the facing: one cosine, 1/√(1 + r²). The two cancel exactly
  (W2). What the sheet sends along the straight-down facing is the same from every direction: the uniform turn. So
  the sheet's weight, laid back on the sheet, is the look's own heat on a flat screen, the 2D Cauchy of the height.
  That is why GRV found the look's law there and not run 6's.
- Run 6's law is the same sheet with the lean taken out: thin the sheet by 1/√(1 + r²) and it is an even sky, half
  within one height, total πσ, half the whole sheet's (W3). The two laws are one sheet, thinned or not.
- So the flat sheet is the one arrangement of mass whose pull, faced square to it, lays out exactly as a look lays
  out. It is also why the sheet's pull has no height in it (W6): every direction gives the same, and the directions
  do not change with the height.
- Turn the facing along the sheet and there is no limit (W5): the lean is no longer cancelled, and the take grows by
  2σ·ln 10 for each tenfold of sheet, without end, like the Cauchy's own missing mean. The opposite facing grows the
  same, and their difference, the pull, is nothing. One facing of an endless even world has no total; two opposite
  facings have a difference (GRV's V6 found the same of a half-ball).

Limits. Classical (the infinite sheet's field; Lambert's cosine; the logarithm of a slab's sideways attraction).
Everything was derived before the run. A faced take is this plan's definition, not a claim about the world.
