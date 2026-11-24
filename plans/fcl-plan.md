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
