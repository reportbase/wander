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
