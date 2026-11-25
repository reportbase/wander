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

## Run 8: bodies with size, and a lens of two masses

Tom, 24 November, after run 7 and essay 33: "merge, 1, 2, 3" (3: "More runs. Two candidates are left: bodies with size
(where the meeting point falls inside one of them), and a lens of two masses."). PR #489 merged before this was written.

Set-up A, two uniform balls. Masses M₁ and M₂, radii R₁ and R₂, centres D apart, not overlapping, at rest. Outside a
ball its pull is a point's; inside, in proportion to the distance from its centre (run 2). Places on the line between
the centres, s measured from ball 2's centre toward ball 1. Exact, mpmath, 30 digits.

Set-up B, two lens masses on one line. Run 5's lens with two point masses at a and b on a line, strengths ε₁ and ε₂
(in units where the sum's Einstein radius is 1). For sources and images on that line the lens equation is
y = u − ε₁/(u − a) − ε₂/(u − b).

Said beforehand: I worked these out on paper just before writing them. A3's "a third" surprised me and may be wrong.
Classical where it is known to me (the shell theorem; inner functions keeping the Cauchy).

### Predictions (committed before running)

- **A1, size adds balance points inside.** With the point meeting place (ρ = √μ, run 3) outside both balls, there are
  exactly three balance points on the line between the centres: that one, unmoved by the radii, and one inside each
  ball near its centre, where the ball's own pull has fallen to the other's. Kill: a count other than three, or the
  outer one off √μ past 10⁻²⁵, in any of four seeded cases.
- **A2, the inner one is the play's.** For a far, light companion the inner point stands at s ≈ M₁R₂³/(M₂D²) from its
  ball's centre: it carries both masses and the ball's radius, and the exchange ρ ↔ μ/ρ does not hold inside. Kill: off
  that by more than 2% where it predicts s under D/100; or reciprocal pull ratios at ρ and μ/ρ to 10⁻⁶ for a pair of
  places with one inside the ball.
- **A3, the meeting place does not enter a ball: it merges and goes.** When the point meeting place would fall inside
  ball 2, it and ball 2's inner point are both inside, and as ball 2 is made lighter they meet and vanish together,
  leaving one balance point on the line (inside ball 1). They meet exactly a third of the way from ball 2's centre to
  ball 1's, whatever the masses and radii, when M₂/M₁ = (27/4)·(R₂/D)³. So the count is three or one, never two.
  Kill: the count on either side of that mass ratio (1% above and below) not three and one; or the meeting place off
  D/3 by more than 10⁻⁶·D at the ratio itself; in three cases with R₂ > D/3.
- **B1, two lens masses on a line keep the Cauchy along it.** Images along the line that follow a Cauchy with point z
  come from sources that follow exactly the Cauchy with point z − ε₁/(z − a) − ε₂/(z − b). Kill: off past 10⁻²⁰ in the
  distribution function at any of seven points, for three z and two pairs of masses.
- **B2, three images, three Cauchys.** Sources along the line following a Cauchy with point w are seen as the sum of
  exactly three Cauchys, one for each image, their points the three solutions of the lens equation above the line, and
  those three points add to w + a + b. Kill: the density off the sum past 10⁻²⁰ at any of twelve places; a solution
  not above the line; the sum off past 10⁻²⁵.

Not in this run: sources off the line of a two-mass lens (three or five images, classical), bodies in motion.

### Run 8 (`runs/fcl/fcl8.py`, output `runs/fcl/fcl8-run.txt`), 24 November: nothing killed

| | result | |
| --- | --- | --- |
| A1 | three balance points in all four cases (closed form and a 20,000-step scan agree); the outer one at ρ = √μ to 5·10⁻⁴¹ whatever the radii | not killed |
| A2 | inner point off M₁R₂³/(M₂D²) by 0.2%, 0.4%, 0.6%, 1.65%; with one place inside the ball the pull ratios at ρ and μ/ρ multiply to 27, 4.096, 3.375 (points: 1), which is (R₂/s)³ | not killed |
| A3 | at R₂ = 0.45, 0.5, 0.6 D: three points 1% above M₂/M₁ = (27/4)(R₂/D)³, one 1% below; the pair meet at s = D/3 exactly | not killed |
| B1 | six cases, seven points each: gap at most 2.3·10⁻⁴¹ | not killed |
| B2 | six cases: three points above the line, adding to w + a + b exactly, density gap under 10⁻³⁹ | not killed |

As with run 3, each was worked out on paper beforehand, so the run is a check of the working, not a finding.

### What run 8 says, as a reading (Claude's, not ruled)

- Size leaves the point meeting place alone while it stays outside both bodies (the shell theorem), and adds one more
  balance point inside each body, near its centre. Those inner points carry both masses, the separation and the body's
  radius: three amounts. The exchange ρ ↔ μ/ρ fails inside by exactly (R/s)³, the share of the ball that still pulls.
- The meeting place never crosses a surface. When it would, it is already paired with the body's inner point, and the
  two close on each other and go, at one third of the way between the centres, for every mass and radius. The count on
  the line is three or one. The ⅓ is the play's (the largest value of s(D − s)²), not the stage's corner.
- Along the line of two lens masses the Cauchy family is kept, as with one (run 5): images Cauchy(z) come from sources
  Cauchy(f(z)), and Cauchy sources are seen as one Cauchy per image. This holds for any number of masses on the line,
  since f(u) = u − Σ εᵢ/(u − aᵢ) carries the upper half-plane into itself with real poles (classical: such maps keep
  the Cauchy; Letac 1977 as I remember it, not opened). Run 5's pairing z₂ = −1/z₁ is the one-mass case only; with two
  masses the three points are tied only by their sum.

## Run 9: can the corner an amount owns be had from ratios of pulls alone?

Tom, 24 November: "merge, 1, 2" (2: open item 2 of *Reads and Writes* §7's "Gravity on the stage": whether the corners
owned by an amount can be had from ratios of pulls alone, as a read's corner is had by looking, without the masses
written). PR #492 merged before this was written. A prior-work search (item 1) runs beside it and is not used here.

Set-up. Two point masses M₁, M₂ at rest at unknown places, μ = M₁/M₂. An observer takes the net pull at several places
a counted step apart (the places known in steps, in one frame). From each take it keeps only what scaling both masses
alike cannot move: the pull's direction (two numbers), and in R4 also the ratios of the pulls' strengths between
places. No G, no mass, no unit of force. Unknowns: the two masses' places (six numbers, in steps) and μ: seven.
Doubles, scipy's least squares (installed for the run; not exact arithmetic).

Said beforehand: R1, R2 and R5 follow from the pull being linear in the masses; R3 and R4 are counts of equations
against unknowns, which can fail (a count gives no guarantee of one solution). I expect R3's "four places" to hold and
am unsure of it.

### Predictions (committed before running)

- **R1, nothing a ratio keeps can give a mass.** Multiply both masses by λ = 10⁻³, 7, 10⁶: every direction and every
  ratio of strengths is unchanged, to 10⁻¹² (doubles). So no set of them gives M₁ or M₂. Kill: any moved.
- **R2, the meeting place is met by direction alone, on the line.** Along the line between the masses the pull's
  direction is one sign, and it flips once, at the meeting place. Halving steps on the sign alone (no strength, no mass)
  close on s = D·√M₂/(√M₁ + √M₂) to 10⁻¹², and the distances' ratio there, squared, is μ: the corner gives the masses'
  ratio as a read's corner gives a breadth in thumbs. Kill: off past 10⁻¹⁰ in any of four cases.
- **R3, four places' directions give everything but the amounts.** From directions at four places in general position
  (eight numbers for seven unknowns) both masses' places and μ come back, and so the meeting place, to 10⁻⁶ of a step,
  in at least 18 of 20 seeded scenes, from starts not near the truth (the best of 40 random starts, residual under
  10⁻¹⁰), up to naming the masses the other way round. From three places (six numbers) they do not: in at least 15 of 20
  scenes a solution with residual under 10⁻¹⁰ lies more than 10⁻² of a step from the truth. Kill: either count missed.
- **R4, with ratios of strengths, three places are enough.** Directions and strength ratios at three places (eight
  numbers) give the same, in at least 18 of 20 scenes. Kill: fewer.
- **R5, one amount then gives both masses.** With the scene solved, one pull's strength in a unit, with G carried in,
  gives M₁ and M₂ to 10⁻⁸ relative. Without G it gives only GM. Kill: off.

The reading if these hold: the corner two masses own is had by looking at pulls, with no mass written, as a read's
corner is; the masses stand to it as V stands to a read (never in a ratio; one amount carried in gives both).

### Run 9 (`runs/fcl/fcl9.py`, output `runs/fcl/fcl9-run.txt`), 24 November: nothing killed

| | result | |
| --- | --- | --- |
| R1 | both masses scaled by 10⁻³, 7, 10⁶: the worst change in any direction or ratio of strengths 4·10⁻¹⁶ | not killed |
| R2 | halving on the pull's sign alone meets the meeting place to 12 digits in four cases; (d₁/d₂)² there 1, 3, 10, 0.4, the masses' ratio | not killed |
| R3 | directions at four places: both masses' places and μ found in 20 of 20 scenes (10⁻¹⁵), no second solution in any; at three places the truth in 0 of 20 and a wrong exact solution in 20 of 20 | not killed |
| R4 | directions and ratios of strengths at three places: 20 of 20, no second solution | not killed |
| R5 | one strength in a unit gives GM₂ alone; with G both masses to 10⁻⁸ | not killed |

Doubles and a least-squares solver, 40 random starts a scene, so "no second solution" means none was found.

### What run 9 says, as a reading (Claude's, not ruled)

- The corner two masses own is had by looking at pulls. On the line it is where the pull's direction flips, found with
  no strength, no mass and no G; off the line, directions at four places (or directions and strength ratios at three)
  fix both masses' places and their ratio in the observer's steps.
- The masses themselves are in no ratio. They stand to the pulls as V stands to a read: never in what scaling leaves
  alone, and had only with one amount carried in. Even a strength in a unit gives only GM, as a read with a size
  carried in still gives a breadth only in that size's unit; G is a second carried amount.
- The corner then gives a ratio of the things that own it: the distances' ratio at the meeting place, squared, is the
  masses' ratio. A read's corner gives a breadth in thumbs the same way (the walk to the corner, *Reads and Writes* §6).
- The count is parallax's. One place gives a direction and places nothing; places a counted step apart place the
  sources in steps; an amount is needed only for the size. FCL run 1 had this for strengths in a unit; run 9 has it
  with ratios alone, which is the closer match to a read.

## Run 10: does the subtraction have a form on the read's side?

Tom, 24 November: "merge, then the subtraction on the read's side" (open item 1 of *Reads and Writes* §7's "Gravity on
the stage"). PR #493 merged before this was written.

The proposal, worked out on paper before any run. A look and a pull are both moments of one paint laid on the stage,
and what they do across opposite halves is set by the moment's parity, nothing else.

- The stage's own law is even under its reversal: the look's under the exchange s ↔ 1/s (equal heat either side of the
  corner), the sky's under n ↔ −n. So every odd moment of the bare stage is zero: the read's median sits at the corner,
  and an even sky pulls nowhere.
- A count or a total is the moment of order 0, a scalar: the halves add. A pull is the moment of order 1, a vector, each
  source's amount over its distance squared times its direction: opposite halves subtract. "Adds for a look, subtracts
  for a pull" is scalar against vector.
- A read has an odd moment of its own: the heat met below the corner less the heat met above it. It is zero on the bare
  stage, and it is what moves the median of what is met off the corner. That is the subtraction on the read's side.
- The two subtractions have the same parity and are different moments. The read's weighs each direction by a sign (which
  half it is in) and never by an amount. The pull's weighs each by its amount and the cosine to the facing. So the read's
  is an order statistic and the pull's is a sum: the split of *Reads and Writes* §4 (the median the heat's, the mean the
  paint's) met again.

Said beforehand: T1, T2 and T3a are orthogonality and symmetry and could fail only by my code; T3b's exactness, T4's
angle and T5's counts are the tests. Known already and named: where light and mass go together, a pull's direction is
the direction of the sky's brightness dipole (both fall as the inverse square), used in cosmology to estimate the Local
Group's pull from galaxy surveys; from memory, not opened.

### Predictions (committed before running)

- **T1, the pull is the paint's first moment over two looks back to back.** For twenty seeded scenes of point masses,
  the sum over every source of (amount/d²) × direction equals the pull, and equals F(n)·n-wise the front take less the
  back take along any facing, to 10⁻¹² (doubles). With brightness in proportion to mass the brightness dipole points
  along the pull exactly. Kill: off.
- **T2, an even paint gives no odd moment, on either side.** (a) A sky with density 1 + ε·(a·P₂ + b·P₄) about any axis
  pulls nowhere, to 10⁻²⁵, for three (ε, a, b). (b) A quarter turn weighted 1 + ε·f with f unchanged by the exchange
  (f(θ) = f(Ω − θ), three such f) keeps its median exactly at the corner, to 10⁻²⁵. Kill: either moved.
- **T3, of an odd paint each takes one moment.** (a) A sky 1 + ε·(a·P₁ + b·P₃ + c·P₅): the pull is ε·a·(4π/3) along
  the axis whatever b and c, to 10⁻²⁵. (b) A quarter turn weighted 1 + ε·f with f reversed by the exchange: the median
  moves by −ε·∫₀^(Ω/2) f to first order (ratio to that within 2% at ε = 10⁻³), and for an f reversed by the exchange
  whose integral over the near half is zero (f = sin 8(θ − Ω/2)) the median stays at the corner exactly, to 10⁻²⁵,
  though the paint's mean angle moves. Kill: any.
- **T4, same parity, different moments: the two part.** On a full circle of directions painted 1 + ε·(cos θ + 0.8·cos(3θ
  − 1)), the first moment points along θ = 0 exactly, whatever ε. The balance axis, the direction with equal paint on
  its left and right, is off it by between 5° and 15° (my working gives about 9°), the same for every small ε. Kill:
  outside that band, or the first moment off 0 past 10⁻²⁰.
- **T5, one is a sum and the other a count.** Twenty seeded scenes of thirty point masses in a plane. Replace every
  amount m by m³ (an increasing map): the pull's direction moves by more than 1° in at least 18 of 20, and the count's
  balance axis (as many sources on its left as on its right) does not move at all in any. Kill: either count missed.

The reading if these hold: the subtraction is on the read's side too, as its one odd moment, the near half less the far
half; a pull is the same parity taken with amounts. Not a mechanism and not new physics.

### Run 10 (`runs/fcl/fcl10.py`, output `runs/fcl/fcl10-run.txt`), 24 November: nothing killed

| | result | |
| --- | --- | --- |
| T1 | twenty scenes: front less back equals the first moment along the facing, and the brightness dipole lies along the pull, to 7·10⁻¹⁵ | not killed |
| T2 | even skies (P₂, P₄) pull 0; exchange-even weights keep the median at the corner to 10⁻⁴² | not killed |
| T3 | (a) the pull ε·a·4π/3 whatever the P₃ and P₅ parts; (b) the median moves by −ε·∫ of the near half (ratios 0.9999995, 0.99999985, 0.9999995); for sin 8(θ − Ω/2) the median stays at the corner exactly while the mean angle moves by −0.0375 | not killed |
| T4 | the first moment at 0° exactly; the balance axis at 8.2489°, the same at ε = 0.01, 0.1, 0.5 (my working said about 9°) | not killed |
| T5 | m → m³: the pull's direction moved over 1° in 20 of 20; the count's balance axis unmoved in 20 of 20 | not killed |

T1, T2, T3a and the unmoved half of T5 are identities (the first moment's linearity, parity, orthogonality, a count
that takes no amount); they could have failed only by my code. T3b, T4 and T5's first half are the tests.

### What run 10 says, as a reading (Claude's, not ruled)

- The subtraction is on the read's side too. A read's one odd moment is the heat met below the corner less the heat met
  above it. On the bare stage it is zero, which is the corner being the median; a lopsided paint makes it non-zero, and
  to first order it is exactly how far the median of what is met moves.
- A pull is the same parity taken with amounts: the first moment of the paint (each source's amount over its distance
  squared) over two looks back to back. Opposite halves subtract because the moment is a vector, as a total's halves add
  because it is a scalar. "A look adds, a pull subtracts" is order 0 against order 1 of one paint.
- They are different moments. The read's weighs a direction by which half it is in; the pull's by its amount and its
  cosine to the facing. A paint can move one and not the other (T3b, T4: 8.25° apart), and an increasing map of the
  amounts moves the pull and never the count (T5). So the read's is an order statistic and the pull's a sum: §4's split,
  the median the heat's and the mean the paint's, with gravity on the paint's side.
- This places the pull: it is the payload's centre of gravity taken on the stage, in the literal sense, which is R1098
  (the Cauchy has a median; the centre of gravity is the density's). It also says why a pull has no facing: a first
  moment over the whole sphere needs none.
- Where light goes with mass, the pull's direction is the sky's brightness dipole. Known and used (galaxy flux dipoles
  against the Local Group's motion); from memory, not opened. It is the nearest thing to reading a pull by looking.

## Run 11, planned 24 November: the depth rule on a measured profile (Tom: "3")

*Reads and Writes* §7's open item 3: a check on measured gravity profiles over bodies of known depth. Everything in runs
1–10 is exact arithmetic on set-ups of our own; this is the thread's first use of measurements.

**The search for data** (a fresh agent, 24 November; nothing found as a table). No openly reachable table of station
against gravity over a compact body of independently known depth was found. Opened and usable only as published
figures: one clean case and one poor one. Opened and not usable: Manatee Springs conduit (WES TR GL-83-1 report 4,
contour maps only), the Senec test cellar (anomaly cut off by the lot, body wider than its depth), the Trnava crypts
(maps only), Ape Cave (height errors as large as the signal). The classic field examples of the inversion papers
(Mobrun, Camagüey, Louga, Humble) were set aside: the "drilling depths" quoted for them disagree between papers (Mobrun
30.5 m and 23.34 m) and none of the papers opened tabulates its profile.

**The data.**

- **Březno railway tunnel, Czech Republic** (the test). Blecha and Mašín, "Observed and calculated gravity anomalies
  above a tunnel driven in clays: implication for errors in gravity interpretation", authors' preprint
  (`web.natur.cuni.cz/uhigug/masin/download/BM_NSG13-pp.pdf`, sha256 `ad85f96e…e3680f0c`; no licence stated, so cited
  and not committed; published in *Near Surface Geophysics*, volume and pages not checked). A tunnel 1,758 m long, inner
  cross-section 43.7 m², concrete lining 0.6 m on the walls and 1.2 m on the bottom. Two profiles 100 m long square to
  its axis, 130 m and 160 m from the portal, a station every 5 m, 21 stations each; Scintrex CG-3M, a fifth of stations
  repeated, mean square error 0.004 mGal; flat ground; a straight-line regional already taken out by the authors, fitted
  on 0–20 m and 80–100 m. Built geometry, independent of the gravity: on P1 the roof 12.5 m and the floor 20 m below
  the surface; P2 1 m deeper. So the mid-height is 16.25 m (P1) and 17.25 m (P2): my arithmetic, the paper states no
  axis depth. The numbers are not published as a table: they were read from the paper's Figure 2a and 2b by template
  matching on the plotted markers (the agent's estimate ±0.0003 mGal, under a tenth of the measurement error; P1's
  minimum reads −0.0455 against the paper's stated −0.046). The 42 values are in `runs/fcl/fcl11.py`.
- **Medford Cave, Florida, the 80 N-S line** (recorded as a counter-case, not a test). Butler 1983, US Army WES
  Technical Report GL-83-1, report 1 (DTIC ADA124574, public domain; sha256 `ab6a8bb2…bce2fb27`), Figure 43: 23
  stations 10 ft apart, read by eye to about ±2 µGal. A mapped cave passage, verified by borings in two places, crosses
  under the line at a depth to centre of about 24 ft, 9 ft across.

**What was seen before these predictions** (so they are not blind). The agent's report gave me the 42 tunnel values and
a rough half-width from straight-line interpolation: about 17 m on P1 and 14–15 m on P2. It also gave Medford's values
and said its dip rests on three stations, about 8–9 ft half-width. No fit had been made. The kill conditions below were
fixed before any fit; M1 is recorded as already seen to fail.

**The claim.** Outside a round cylinder of even density the pull is exactly a line mass's on its axis, and a round
lining concentric with it changes the amount, never the shape. So across a long tunnel the missing pull is
g(x) = −A·d/((x − x₀)² + d²), the Cauchy's curve with scale d: the depth of the axis is the curve's half-width at half
height, read with no density at all (GRV; classical, the depth rule for a horizontal cylinder).

**The fit.** Each profile by least squares to c − A·d/((x − x₀)² + d²), four numbers (c, A, x₀, d), every station
weighted alike with σ = 0.004 mGal; d's error from the fit's covariance and, beside it, from a bootstrap of the
residuals (2,000 draws, seeded). The same with the ball's curve c − A·d³/((x − x₀)² + d²)^(3/2).

**Predictions, with kills.**

- **D1, the depth from the shape alone.** The fitted d lies within two of its own standard errors of the mid-height on
  each profile (16.25 m on P1, 17.25 m on P2), and the two profiles' weighted mean lies within 20% of 16.75 m (the
  paper's own figure for how far a fixed-density model goes wrong when the lining is left out). Kill: either.
- **D2, inside the tunnel.** Each profile's fitted d lies between its roof and its floor (12.5–20 m, 13.5–21 m), and
  the tunnel's place x₀ within one station (5 m) of 50 m. Kill: either, on either profile.
- **D3, the law is the line's, not the ball's.** Fitted with the ball's curve, the depth comes out deeper by a factor
  between 1.2 and 1.4 (the rules' ratio is 1/0.766 = 1.305), which puts the weighted mean below the tunnel's floor
  (past 20.5 m). The data will not tell the two curves apart by goodness of fit: the difference in χ² under 4 on each
  profile. Kill: the factor outside the band, the ball's depth inside the tunnel, or a χ² difference of 4 or more
  either way.
- **D4, the scatter is the instrument's.** χ² per degree of freedom of the line fit between 0.4 and 2.5 on each
  profile (17 degrees of freedom, σ = 0.004 mGal). Kill: outside on either.
- **D5, no amount needed, and one amount gives one.** Multiplying every gravity value by 7 leaves the fitted d and x₀
  unchanged to 10⁻⁶ of themselves (an identity of the fit; it can fail only by my code). Reported, not predicted: the
  mass missing per metre, A/(2G), in tonnes a metre, which is what the amplitude gives once G is carried in.
- **M1, the counter-case (seen beforehand to fail).** Medford's dip fitted the same way gives a depth under half the
  24 ft the borings give: the dip is too narrow for a passage that deep, as Butler's own account of shallow pinnacles
  and clay pockets says. Recorded so that the rule's failure on a messy site stands beside its test on a clean one.

What this can and cannot show. Two profiles over one tunnel, digitized from a figure, with a regional the authors
removed using the profile's own ends (which pulls the wings toward zero and so narrows the curve a little: by my
estimate a few per cent in d; not corrected). If D1 and D2 hold, the classical rule works on this site to the profile's
noise; nothing about the framing is tested beyond that, since the rule is classical. If they fail, the first suspects
are the regional and a tunnel that is not round.

### Run 11 (`runs/fcl/fcl11.py`, output `runs/fcl/fcl11-run.txt`), 24 November: D3 killed in one clause; D1 at its edge

Least squares in doubles (scipy), σ = 0.004 mGal, 17 degrees of freedom a profile.

| | P1 (mid-height 16.25 m, roof 12.5, floor 20) | P2 (17.25 m, 13.5, 21) |
| --- | --- | --- |
| line: depth d | 18.89 ± 2.33 m (bootstrap 2.85) | 13.64 ± 1.81 m (bootstrap 1.89) |
| (d − mid-height)/error | +1.13 | −1.9993 |
| place x₀ | 51.64 ± 0.80 m | 47.67 ± 0.78 m |
| χ² per degree of freedom | 1.79 | 1.24 |
| ball: depth | 23.50 ± 2.58 m | 17.48 ± 2.04 m |
| ball over line | 1.244 | 1.282 |
| χ², ball less line | −0.45 | −0.81 |
| values × 7: d moves by | 3·10⁻¹⁰ | 2·10⁻¹⁰ |
| missing mass per metre, A/(2G) | 78 t/m | 49 t/m |

Weighted mean of the two, line: 15.61 ± 1.43 m against 16.75 m, 6.8% short. Ball: 19.81 m.

| | | |
| --- | --- | --- |
| D1 | both within two errors of the mid-height (P2 by its letter only, −1.9993; by the bootstrap error −1.92); the mean 6.8% off | not killed, P2 at the edge |
| D2 | both depths inside the tunnel (P2's 13.64 m is 0.14 m under its roof); x₀ within 2.4 m of 50 m | not killed, P2 at the edge |
| D3 | the factor 1.244 and 1.282, in the band; χ² differences under 1, the curves not told apart; but the ball's mean depth is 19.81 m, not below the floor | **killed** in that clause |
| D4 | 1.79 and 1.24 | not killed |
| D5 | unmoved to 10⁻⁹ | not killed (an identity) |
| M1 | Medford's dip fits as 7.1 ± 1.6 ft against 24 ft to centre (χ² 17.6 on 5) | fails as recorded beforehand |

What it shows, plainly.

- The rule works on this site to the profile's noise and no better. The half-width of the missing pull gives the
  tunnel's depth to about 2 m a profile (12% and 13% of the depth), and the two profiles, 30 m apart over one tunnel,
  differ from each other by 5.3 m, 1.8 of their joint error: one high by 16%, one low by 21%. Their mean is 7% short.
  Twenty-one stations at 0.004 mGal on a 0.045 mGal dip do not fix a width better than that.
- The depth came with no density and no amount (D5), which is the point of the rule: the width is the shape's. The
  paper's own modelling, which fixes densities, reports a 20% (2.5 m) error from leaving the lining out; the shape's
  estimate here is no closer than that, from noise instead.
- D3's killed clause was mine: I predicted the ball's law would put the depth below the floor. It did on P1 (23.5 m)
  and not on P2 (17.5 m), because P2's fit is narrow; the mean, 19.8 m, is just inside. The ratio between the two laws'
  depths held (1.24 and 1.28 against the rules' 1.305). The data cannot tell the line's curve from the ball's by fit
  (χ² differences 0.5 and 0.8, slightly favouring the ball), so the law of the fall-off is not tested here; only the
  depth is, given the law.
- The amplitudes differ more than the depths: 78 and 49 tonnes a metre missing, where an empty bore of 43.7 m² in clay
  near 2 t/m³ would miss about 87 less the lining's concrete. A and d trade off in the fit (a wider curve needs more
  mass), so these follow the depths' scatter; not a test.
- The regional. My estimate above the Runs line, that the authors' straight line through the profile's ends would
  narrow the curve by a few per cent, was wrong: with the fit's constant left free a noise-free curve treated the same
  way comes back at 16.25 m exactly (the constant takes it up, 0.0068 mGal; the fitted constants are 0.010 and 0.005).
- Medford is what a messy site does to the rule: a dip three stations wide over a passage 24 ft down reads as 7 ft.
  Butler's report says the flanks are shallow pinnacles and clay pockets; the passage's own dip, about 10 µGal by his
  model's scale, is under them. The rule needs the body to own the profile.

Limits, kept with the result: one tunnel, two profiles, values read from a figure by a program (not the authors'
numbers), predictions made after the values and a rough half-width had been seen, a body that is not exactly round
(7.5 m high, lining thicker at the bottom). Classical throughout (the depth rule for a horizontal cylinder); nothing
about a read is tested. The search found no table of such data in the open; a second clean site would need one of the
paywalled originals (Arzi 1975, a drilled cavity 6.4 m to centre; Davis, Jackson and Richter 1957, Camagüey).

## Run 12, planned 25 November: observation's depth beside gravity's (Tom: "yes, run the test")

R1193 (Tom: "Observation has it's own version of depth, seems analagous to gravy's depth."), recorded as open. The test
asks how far the likeness goes, taking each depth two ways: as it is laid along one direction, and as it is had from two
places a step apart.

**The two depths.** Observation's: how far along a direction, in thumbs. Laid by the thumb, the share within d is the
half-Cauchy's, half within one thumb H, and d ↔ H²/d trades the near share for the far one (§6); from two looks a step B
apart it is 1/(d/B) = 1/s₁ + 1/s₂ (§9). Gravity's: the column along a direction, the density times the length of matter
on that line (GRV; R1192).

**Worked beforehand** (so most of these are checks of my working, and say so).

- Along a direction through even matter the inverse square cancels against the volume, so every unit of length counts
  alike at any distance: the share of that direction's pull from within d is d/L, L the matter's depth.
- For the flat lay d/L, the worst departure of F(d) + F(c²/d) from 1 over c²/L ≤ d ≤ L is max(α², 1 − 2α) with
  α = c/L, least at α = √2 − 1, where it is 3 − 2√2 = 0.1716.
- A point mass, two pull strengths a step B apart along the line: g(d)/g(d + B) = ρ gives d/B = 1/(√ρ − 1), with no
  mass and no G; a small relative error ε in ρ moves d by (x + 1)·ε/2 of itself, x = d/B.
- Two equal masses 2a apart seen from two places 2b apart at depth d: the two pull directions cross on the axis at
  d·(1 + 3(a/d)²) when the pair lies across the line of sight and d·(1 − 3(a/d)²) when it lies along it, to second
  order, whatever b.
- A ball of radius R: the pull along a line through its centre is r/R inside and (R/r)² outside, in units of the
  surface's, so the pull at the partner R²/r of an inside place r is (r/R)², the square of the pull at r.

**Predictions, with kills** (mpmath at 40 digits).

- **Z1, laid flat.** A thin cone of even matter from distance a to b: the share of its pull from within d is
  (d − a)/(b − a), to 10⁻²⁵, at five d and three cone widths (the width to second order only: within 10⁻³ of it for a
  cone of half-slope 1/100). Half the pull comes from the nearer half of the matter's length. An identity of the
  cancellation; it can fail only by my code. Kill: any departure.
- **Z2, whose the half point is.** The look's half point along a direction is one thumb whatever the matter; the
  pull's is the middle of the matter, (a + b)/2, whatever the thumb. Tripling the matter's depth triples the pull's
  half point and leaves the look's; tripling the thumb does the reverse. Exact. Kill: either moves the other.
- **Z3, no exchange for the flat lay.** For every c the flat lay misses the look's complement: the least worst
  departure over c is 3 − 2√2, found within [0.15, 0.20] and at c/L within 0.01 of √2 − 1, where the look's own lay
  has it 0 to 10⁻³⁰ at c = H. Kill: outside either band.
- **Z4, scaling.** Lengths × k with the density kept: the column, and so the direction's pull, × k; with the masses
  kept, × 1/k². The look's lay, thumb scaled with the world, unmoved to 10⁻³⁰. Kill: any other power.
- **Z5, depth from two pulls along the line.** d/B = 1/(√ρ − 1) returns the depth to 10⁻³⁰ at x = 1/10, 1, 10, 100
  for three masses a millionfold apart (no mass, no G in it). Its sensitivity to ε = 10⁻⁶ in ρ is (x + 1)/2 within 1%
  at each x: least near, growing in proportion far off, with no place of least error between, where two looks' error
  ε·cosh(ln(2d/B)) is least at d = B/2. Kill: the depth off, the ratio outside 1%, or an interior minimum.
- **Z6, depth from two pull directions across.** (a) One point mass: two pull directions a step apart cross on the
  mass, by the two looks' own formula 1/(d/B) = 1/s₁ + 1/s₂, to 10⁻³⁰ (a direction is a direction: an identity).
  (b) Two equal masses: the crossing is off their centre by +3(a/d)² across and −3(a/d)² along, the ratio to that
  within [0.9, 1.1] at d/a = 10, 20, 40 with b = a/2, while two looks at either mass cross on it to 10⁻³⁰. Kill: any
  clause.
- **Z7, the ball's exchange is one power off.** g(R²/r) = g(r)² exactly for r inside, at five r, to 10⁻³⁰; the look's
  near reading d/H and far reading H/d′ at the partner d′ = H²/d are equal. Kill: any departure.

The reading if these hold. The two depths are alike in where they lie (along the direction, square to the stage's
heat) and in how they are had from two places (a step turns two takes into a depth in steps, no amount needed). They
differ in the lay: observation's depth is laid by the thumb, the standpoint's own, with a corner and an exchange;
gravity's is laid flat, every length alike, its half point owned by the matter. And a pull's direction is a sum, so
two of them cross on a single mass but not on a body's centre. Classical throughout (the column; depth from a
gradient, which geophysics uses as Euler deconvolution, from memory; the quadrupole). Not a mechanism; a pull is not a
read.
