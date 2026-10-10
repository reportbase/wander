# wander: notes for Claude

A world of solids you fly through, with a "lab" of experiments comparing what a
reader can recover from arriving signals against known physics. Two pages and the
world they share, served by GitHub Pages at https://reportbase.github.io/wander/. The owner works through
Claude Code: changes go on a branch, as a PR, and the owner merges. Merging to
`main` publishes.

## Files
Since 6 Oct 2026 (Tom's choice) the site is three files, no build step; only
Google Fonts load from outside:
- `world.js`: **Wander's world, shared by both pages**: the constants, the solids,
  the systems and their ticks (`tickSystem`), the signals' speed and arrival
  pieces, the readout's distance step, and the reading functions the live readout
  shares with the labs (`plxTwoPart`, `twoAt`, …). A classic script whose top-level
  names both pages' scripts see (that is how both can assign `starsNow`). Moved
  out of the old single page line for line. **A change here changes the labs'
  world: run every lab after it.** Since 9 Oct it also holds brightness (`lightAt`, L·A/(4πd²), the
  inverse square), read only by LAD's third run (the standard-candle rung past the resolution limit).
- `index.html`: the flying page (the world drawn, the controls, the readout, the
  live-view test hooks). Its "lab" button opens `labs.html` and its "demos" button `demos.html`; `?lab=CODE` and
  `?lab=all` forward there; `?lab=0` hides the button.
- `labs.html`: **the lab, and the file to edit for any lab.** The explainer and a
  card per lab on top; then THE LAB BUDGET comment, the lab notes (`#labPane`,
  hidden, the cards are built from it), and the script with THE LAB GUIDE and every
  lab's code. `?lab=all` / `?lab=CODE` run outright and show the full report (the
  smoke test reads it); `?run=…` does the same on the cards.
- `res/`: the suns, planets and moons, as `.tvf3d` fields (the 3d studio's and the games
  page's format: radius and colour as series in cos(nπh) and cos/sin(mθ)), written by
  `node res/make-bodies.mjs` (seeded, so it writes the same files; add a body there and
  list it in `BODY_FILES` in `index.html`). The flying page fetches them in the background
  (`fieldGrid` folds each onto the solids' grid) and dresses each system's star as a sun, its
  planets, moons and belt, chosen by the body's key; they are lit by their own star
  (`lightOf`, the 8th vec4 of a body's record), and suns give light. Each body's radius is held as
  its ball plus relief in three bands (broad, middle, fine, by max(n, m); `fieldGrid`), and
  the shaders add each band only once its features cover a few pixels (`bandW`): far off a
  body is a plain ball, close up its craters and mountains show. Looks only: motion,
  reading and the labs are unchanged, and `world.js` is not touched. Until they load, plain balls.
- `sweep.html`: **the sweep device** (7 Oct 2026), a standalone page outside the world
  and the labs: an array of pairs of amounts, each divided by its own second amount, laid on the unit sweep
  g = (2/π)·atan(v/h) and read by a cursor, serially (4) or all at once (3), with the
  quarter circle (divided by the whole) beside it. `?ex=planets|shape|spread|line`,
  `?mode=parallel`. Not linked from index.html yet.
- `dial.html`: **the H dial** (7 Oct 2026), a standalone page like `sweep.html`: GRN runs 3–5
  (`plans/grn-plan.md`) on one screen. A model-free reader with pixels H wide reads two points one apart;
  turn the dial, look, slide h, approach from afar; charts of P("two") = min(s, 1) and of the cost of a sure
  "two", (1 + s)·max(1, 1/s), least at one pixel across (GRN's "corner", s = 1, is the resolution limit). `?s=` sets the dial; test hook `window.__dial`.
- `sphere.html`: **the sphere** (7 Oct 2026), a standalone page like `dial.html`: `number-line.md` §8 on one screen.
  Three fill levels and a scale k; the address on the octant (k changes nothing there); six chambers and the triple corner;
  the unit cube's faces; near and far for a reader holding H; a body with relief in three bands shown by its size in
  pixels (as `bandW`). `?v=&h=&f=&k=&P=&map=chambers|faces|reader|whole`; test hook `window.__sphere`.
- `facing.html`: **the facing** (9 Oct 2026, after SPN §1, "The line, the arc and the facing"; Tom: "a line does not account
  for a second degree of freedom"), a standalone page like `dial.html`. One sweep from A to B in fill levels: the facing
  2θ turns from toward B through square to the line (the corner, θ = 45°) to toward A; beside it the quarter arc off the
  line h + v = 1, most (1 − 1/√2) at the corner. `?t=` (θ in degrees); test hook `window.__facing`.
- `levels.html`: **the levels** (9 Oct 2026, Tom: "a demo that shows the circle in the middle of the page and the logritmic
  circles that halve outside the circle … until they can't be seen anymore"), a standalone page like `facing.html`. The unit
  circle holds the near field in proportion (radius s); past it each ring is one doubling of s, half as wide as the last
  (radius 2 − 1/s, the in-place lay), toward the horizon at radius 2. A ring narrower than one grain is not drawn (the
  resolution limit), so about log₂(R ÷ grain) show. A perturbed circle (Tom: "a pertibated circle that wrapped the circle that crossed the various
  levels") wraps it, s(θ) = s₀·exp(Σ aₙ cos(nθ + φₙ)), and the reader's level of detail is a circle at s = 2^k (Tom: "another
  circle the represents the LOD of the user"): inside it the shape keeps every bump, past it only its broad form (n ≤ 3).
  "Divide out the size" (10 Oct, Tom: "the corner is v = h … which is also the baseline from which depth is calcualted")
  moves the shape's middle onto the corner's circle and shades the depth, log₂ s(θ) levels, outward and inward.
  A combo box picks the shape (10 Oct, Tom: "add the ablity load a tvf file. add a combo box let the user select the shape"):
  the built-in one, a body in res/, or a file from disk: a .tvf curve (the draw tool's format, draw.html `parseTvfText`; read from
  its centroid, the nearest wall in each direction) or a .tvf3d cut at a height h (the equator by default); the outline
  read as s(θ) = s₀·(r/r̄)^k with a relief slider k. `?g=&s=&shape=&lod=&depth=1&body=&relief=&cut=`; test hook `window.__levels`.
- `thin.html`, `ladder.html`, `sky.html`: **the physics correspondence** (9 Oct 2026, Tom: "create multiple demos that
  explain the physics correspndance"), standalone pages like `dial.html`. `thin.html`: the same signal, a smaller share
  (the inverse square; near, distance costs grains, far, light; the switch at one grain is the resolution limit;
  `?v=`, hook `window.__thin`). `ladder.html`: parallax, width and light, each giving out at its own limit (LAD;
  `?D=&photons=1`, hook `window.__ladder`). `sky.html`: Olbers' dark sky, the lit share 1 − e^(−L/λ) and every shell
  giving the same light (OLB; `?L=&always=1`, hook `window.__sky`).
- `play-points.html`, `play-resolve.html`, `play-ladder.html`, `play-sky.html`: **gameplay sketches** (9 Oct 2026, Tom:
  "explore game play possibilites in demos, each demo should focus on a narrow features. so they can be explored and
  iterated seperately"). Standalone, one mechanic each, nothing shared, so each can change alone: far bodies under a pixel
  (dim by 1/d², vanish, or a full-bright pixel; hook `__points`); events on approach (point, resolved, shape, terrain,
  surface; `__resolve`); distances earned rung by rung (parallax, then width and light per kind; `__navigator`); the sky
  filling as light arrives, the count a clock (`__skyfill`). Not in the flying page.
- `demos.html`: **the list of pages** (7 Oct 2026): the world, the lab and the five demos (sweep, dial, sphere, facing, levels) and the three on the physics correspondence, each
  with a description and a few direct links. No script. Add a card when a page is added. The flying page's "demos" button opens it.
- `papers/`: **the master copies of the owner's papers**, edited here from now on
  (branch, PR, merge, like the page). `serial-parallel-nowhere.md` (SPN) is the
  paper behind the labs (§9.9 the labs, §11.4 the conjecture, §12–§14 their
  standing); `v-and-h.md` gathers every idea about v and h, by item.
  `number-line.md` (7 Oct 2026) is a working paper Tom iterates on: how people meet the
  number line (its two infinities one under the flip; situation 3 within a window, 4 before
  and past it, a bounded line held whole). A reading; parts go to SPN only once tested or ruled.
  `serial-parallel-nowhere-record.md` is SPN as written 29 Sep – 1 Oct, before the
  rewrite: **a frozen record, never edited.** Section and proposition numbers cited
  in the corpus before the rewrite are the record's; SPN's opening note maps them to
  the current ones. SPN opens with the terms in order (relation, reading, corner, sweep,
  octave, recursion, spiral; since 8 Oct recursion is considered and rejected for
  level of detail: the levels exist whole, a thing's level is set by its size (smaller things have
  less detail; not a request), and nothing recurses), a map of how the parts depend, and the standing of each;
  then the central result and the open question (what fixes the ratio between rungs; demoted 8 Oct: the reader
  sweeps its level of detail, proportional then logarithmic, and the derivation of 2 is in Appendix D, with
  Proposition D.1 since 9 Oct: on a level with only its ends, order and flip, the halving is the only subdivision supplied;
  other branching factors need an added measure).
  `physics.md` (10 Oct 2026, Tom: "lets create a new physics paper and iterate there") is the working paper for the physics
  correspondences: the rules (real data or exact arithmetic, prediction first, keep the case, name the bridge), a
  dictionary from SPN's geometry to physics, the results by standing (real data, exact arithmetic, Wander's world as
  illustration only), the kills, and a queue of tests. New physics tests are planned in `plans/`, reported there, and
  promoted to SPN only once ruled.
  The papers cite others not in this repo (*Reader Geometry as
  Addressing*, `plans/…`): leave those references as they are. `_config.yml`
  keeps `papers/` and `plans/` off the Pages site.
- `plans/`: working notes, reviews and lab plans, as the corpus cites them
  (`plans/…`). `what-deserves-attention.md` is a review of what to take up next
  (6 Oct 2026): a reading, not a ruling. `hrt-plan.md` (the run for the 2: three
  runs, stopped) and `nle-plan.md` (number lines in people: run 1 on
  Chan and Mazzocco's kindergartners killed the corner's prediction) follow the lab rules: prediction first, runs recorded as they
  came out, nothing above a plan's "Runs" line edited afterwards.
  `nls-plan.md` (+ `nle/nls.py`, 7 Oct): the number-line split on synthetic readers (Tom: synthetic
  tests are fine for persuading each other); the switch is detectable at noise sd 8, the corner against a
  plain log is the fragile part.
  `grn-plan.md` (+ `grn/grn.py`, 7 Oct): serial or parallel set by the reader's grain (Tom: "serial and
  parallel is just our perspective"), on a synthetic binary. The reading depends only on size/grain (by
  construction); serial gives way to parallel near s ≈ 0.7; the knee at the corner was killed twice (runs 1, 2),
  a reader given the shape reading below its grain. Run 3, the pixel the reader's and no model: "two" is certain
  exactly from s = 1, and below it has probability s (not killed). Run 4: below the corner 1/s looks, past it s
  pixels a look; a reader sliding its h by halvings needs about log₂(1/s) looks (not killed). Run 5, h as a
  dial: paying per grain read, a sure reading costs (1+s)·max(1,1/s), least at one pixel across, same at s and 1/s.
  Run 6, steering by its own pixel count from any start (it cannot know its corner): about one look per
  doubling (P1 not killed); within [0.5, 3] killed at one start (luck at the last level below the corner); the
  gain is one-sided, large from below, none from above for a single answer.
  Run 7, the edge moved by light (reader given the shape): resolution limit ∝ light^(−0.499), knee steady
  (not killed).
  Run 8 (8 Oct), a pair receding under the inverse-square law: the reader given the shape loses it at
  v* ∝ a^0.51 F₀^0.25 (predicted ½, ¼); the model-free reader at one grain across, at any light (not killed).
  `anl-plan.md` (+ `anl/anl.py`, 7 Oct): a number line that recurses as needed against the ordinary line's
  depth everywhere. One close pair anywhere sets every number's depth on the ordinary line; with 5 twins the
  recursing line costs 0.375 of it, rising to 1 as detail spreads. Run 1's clustered prediction killed.
  `arb-plan.md` (+ `arb/arb.py`, 7 Oct): arithmetic baseline, an exact referee against float, fixed depth and
  a recursing line of cells: half the storage on mixed depths, 1.25 on the control; the fixed line overclaims
  by ~10⁶; √2·√2 = 2 undecided at every depth (nothing killed).
  `cal-plan.md` (+ `cal/cal.py`, 7 Oct): observation costs calories; a reader enters a level only if worth its
  price. Detail fading fast: depth is the log of worth (within 4%). Fading slowly (r = 0.7): killed, the reader
  prices from two noisy looks and quits early. Run 2 (running estimate): the log-of-worth slope holds within 3% at
  every r; the net still falls short at r = 0.7 (killed).
  `why2-plan.md` (+ `why2/why2.py`, 7 Oct): why the levels might be doublings (SPN's open question). A reader
  stepping its grain by ρ, paying per grain: content with a first sighting, no preferred step (run 1 killed);
  needing a sure reading (3 looks), cheapest ρ ≈ 2 on average and at worst (run 2). Broad valley. Run 3 (8 Oct): the 2
  holds for 2 to 5 confirming looks in one dimension (P1 not killed); when a look costs a whole image or volume, luck
  pulls the best step to ~1.25–1.35 or ~1.1 (P2 not killed, on its edge).
  `frc-plan.md` (+ `frc/frc.py`, 8 Oct): which ratios between levels are precomputable (Tom: "to prove 2 is forced, we
  must show that every other number is not pre-computable"). From the flip, its fixed point and nesting only powers of 2
  (P1 not killed); a chosen number, a root, arithmetic or 2/π each opens others. Bookkeeping for SPN's "A route to forcing
  2", not a proof; run 1's arithmetic row was capped (my set-up). Run 2 (exact fractions, no cap): base only powers of 2
  again; arithmetic opens a factor of 3 (P2a not killed). Run 3 (Tom: "does 2 allow us to do recursion without runtime
  logic"): on a level (identity and flip) only a split in 2 has every part of one kind, on the full turn every split does;
  a theorem (⌈b/2⌉ kinds), resting on the premise that a level's only symmetries are the identity and the flip.
  `isq-plan.md` (+ `isq/isq.py`, 10 Oct): is the in-place lay the inverse square? Past the corner it is 2 − 1/s,
  proportion in h/v, so its room per unit s is 1/s², the flip's Jacobian (all five predictions not killed); draw's piecewise
  lay is 1/s² at each level's geometric middle. Read s as d/Δ: the lay is an angular size, its 1/s² that size's rate,
  light's inverse square its square. A shared form with one origin, not a claim that the lay is light.
  `hzn-plan.md` (+ `hzn/`, 10 Oct): standing on the outline is standing on a world. From a place on a circle the readings
  are chords 2·sin φ; the corner is the radius, 30° below the horizon (on a ball 2/e of it); rising by e radii, the horizon
  is √(2e), half a level per doubling (P1–P4 not killed). Draw's levels page agrees to its grain: P5 and run 2 killed at a
  fixed grain; run 3, both grains doubled together, not killed.
  `ref-plan.md` (+ `ref/ref.mjs`, 10 Oct): the corner as the reference sphere. Published radii: rocky worlds within a
  hundredth of a level of their corner, giants a tenth (P4, P5 not killed). Wander's bodies (P1–P3 killed): one asteroid's
  corner 1.3% off its ball; the Moon 0.25 levels (the real one 0.0165), Mars 0.135; the middle band, not the broad, holds
  most relief in twelve bodies. Scaling `res/` relief to real levels is Tom's call.
  `mag-plan.md` (+ `mag/mag.py`, 10 Oct): on the Hipparcos stars (HYG v3.8 from GitHub, sha256 in the plan; parallax
  distance, V and spectral type only), light falls two levels per level of distance: G dwarfs 2.02, K0 giants 1.93 where
  complete (P1–P3 not killed), 1.61 past the limit; K0 III scatters 1.4 levels (P4 killed).
  `cnt-plan.md` (+ `cnt/cnt.py`, 10 Oct): star counts in levels on Hipparcos to V 7.3: about 1.2 levels of number per
  level of light at every brightness, not the even spread's 1.5 (P1, P2 not killed at their bands' edges); plane and poles
  alike, 1.229 and 1.227 (P3, P4 killed).
  `gcn-plan.md` (+ `gcn/gcn.py`, 10 Oct): star counts within 100 pc on the Gaia Catalogue of Nearby Stars (VizieR
  J/A+A/649/A6 table1c, from Tom; sha256 in the plan), kinds by colour on the main sequence. All four killed: the RUWE cut
  removes more near stars (steeper counts, poles past the plane), and a fifth of G/K colours within 50 pc are white dwarfs.
  Read after the run without the cut: 2.93–3.00 levels of number per level of distance for every kind, plane = poles.
  `grd-plan.md` (10 Oct, predictions only): the ratio between levels in a measured reader, the grid cells' modules.
  P1: a halving, √2 (area) or 2 (length), within 0.07; prior knowledge of the published means (~1.42, ~1.7) is stated in
  the plan, so it runs only on per-animal data not yet opened (Tom to supply; candidates listed there).
  `part-one-audit.md` checks SPN Part I's proofs and numbers (6 Oct 2026): sound,
  with six fixes, applied to SPN on 6 Oct (marked *Corrected* there).
  `near-far-classification.md` answers one of its open questions: which near/far
  laws are fair to the facings (shares of a two-part split are; components are not).
  `horizon-recursion.md` (+ `spiral/`): the horizon with no preferred rung forces
  recursion; each octave a quarter turn for any ratio; the reading a logarithmic
  spiral (situations 1–2 the circle, k = 0). In SPN §3.3 as Propositions 3.11–3.13.
  `wavelets.md` (+ `wavelets/`): the system on one page, and what filters, wavelets
  and hearing scales already have of it (much), and what the situated view adds.
  `resolution-recursion.md` (+ `spiral/resolution.py`): a reader of finite resolution
  facing a horizon must zoom without end, and far out every zoom is alike ((R) from the
  fisheye's tail); the quarter turn per level is still a premise. Unruled.
  `normalizations.md` (+ `normalizations/`): one relation divided by h (odds), by v + h
  (probability) and by the whole (the circle); two bells with dyadic tails; dividing by a noisy h
  gives a Cauchy tail. A reading.
  `neighbours.md`: who else works near this (a first search, 7 Oct): Gilinsky's perceived
  distance is the normalization by the sum, Schwartz's V1 map proportion-then-log; Barth and
  Paladino's proportion judgment bears on NLE.
  `standpoint-axis.md` (+ `standpoint/`): a second axis, the standpoint (nowhere,
  outside, inside) beside the breadths known; the hemisphere observer as outside with
  the breadths known. Superseded by Tom's situations list 0–4 (SPN §2.1).

SPN's situations, since 6 Oct 2026 (Tom): 0 nothing known; 1 the circle; 2 shapes;
3 parallel, one hemisphere counted (outside); 4 serial, one point at a time
(inside); 3 and 4 possibly approximate. SPN uses these numbers throughout
(converted 6 Oct), except in quotations, Appendix A's rulings and the earlier table in
§2.1, which keep the old ones (old 3 = 3 and 4, old 4 = 0, old 5 = 3 or 4 approximately).
SPN §2.1 opens with "The five, in brief". Keep to the core: the sweep
(any two points; g from 0 to 1, the corner at ½; an angle, 0 to 90°, only in 1 and 2,
where nothing is situated), the level (home, corner, far wall; 2h in place; the next
level nests in the back half), dyadic levels (one doubling apart: the layout's rule,
not derived), and the logarithmic spiral as a drawing of the levels. Since 6 Oct
(Tom) SPN says "level" and "dyadic", not "octave", except in quotations, the musical
octave and R172's "octave with two facings".

The repo is public, so the papers can be read on GitHub; the owner is fine with
that for now (6 Oct 2026) and will decide later where they live. They are still
kept off the Pages site. Don't move or remove them without asking.

## Read this first: keep the case of h, v, H, V
Since 9 Oct 2026 (Tom): lowercase **h, v** are fill levels, 0 to 1 (how much of H, how much of V): the geometry, scale-free.
Uppercase **H, V** are breadths, amounts (H the reader's, V the other's); with the distance **d**, a size **Δ** and the
reader's step **ε**, the physics. Never read v as V or v/h as V/H ((v·V)/(h·H) = (v/h)·(V/H)); the only bridge is a fill
level times its breadth, where that breadth is known. Before verifying, editing or summarising any paper, plan or lab,
check each symbol's case and domain, and name the bridge for any conclusion that crosses from geometry to physics. Text
before 9 Oct often conflates them (SPN's opening warning and §1, "H and h kept apart"; `plans/vh-rulings-review.md`,
`plans/physics-vh-audit.md`). "The corner" is h = v, which has no scale; a point set by amounts (one step across, a photon
count) is physics (the resolution limit), not the corner.
Where things stand (SPN §1 opens with "The settled view, 9 October"; read it before working on the papers):
- The sweep is every way h and v relate, from all of H to all of V; v fills against a full h up to the corner, then h
  empties against a full v. Any two parties have a sweep: name the pair before saying "the corner".
- The corner h = v is found by every reader (geometry). It is at 45° because the facing (the second degree of freedom a
  straight line lacks) is square to the line there; facing = 2θ (`facing.html`).
- V = H is a calibration a situated reader must set to read amounts, not part of the geometry; under it amounts equal fill
  levels numerically, which is why the conflation is easy. Every amount is then off by V/H, the same on both sides of the
  corner; physics' bridges (travel, a known constant, a known kind, a shared fact) remedy it (SPN Part II).
- The fisheye is the sweep in one facing, seen from the standpoint (geometry, the same for every shape); with V = H it is
  the situated fisheye reading.
- Still open: the ratio 2 between levels (binary branching is proved; the in-place lay being forced is deferred, SPN
  Appendix D); the weight on the sweep is a choice (SPN §14, "Burdens of proof").

## Read this first: the physics comes first
Since 10 Oct 2026 (Tom: "wanderer priority was user experience, not physics. the physics then became unexpextedly
interesting. we should do the correct physics testing, UI is secondary or even not needed"):
- **Real data or exact mathematics, never wander's world, as evidence.** The flying page and its bodies (`res/`) were made
  for looks; they illustrate, they do not test. A correspondence is tested on published measurements, or on arithmetic
  checked to the last digit (`plans/ref-plan.md`, run 1, is the example of what not to count).
- **Prediction first, from the theory alone**, with the bridge from fill levels to amounts named (see "keep the case").
- **No page needed.** A test is a plan, a script and an entry in the papers; a demo only where it helps to see.
- **Data.** This environment cannot reach the astronomy archives (VizieR, CDS, ESA: blocked); GitHub and PyPI are
  reachable. Record each dataset's source, licence and sha256 in its plan, and do not commit large data.

## Read this first: THE LAB GUIDE
The labs have their own rules, written in `labs.html`. Read two comments
before touching anything lab-related:
- **THE LAB GUIDE**, at the top of the lab section of the script
- **THE LAB BUDGET** comment, before `#labPane`

In short:
- A lab's prediction and kill condition are written into its note **before** it
  runs.
- A killed run stays recorded as killed. A fix is a new run with its own
  prediction; never edit an old prediction to fit.
- After every change, run `labs.html?lab=all` (or its "run every lab"). A
  lab going from "not killed" to "killed" or "error" means something broke; fix
  that before adding anything.

## Testing
- `npm test` runs `tests/smoke.mjs` in headless Chromium:
  1. **Fly:** presses Fly, looks around, flies and taps a body. Then the bodies load and wear
     their files, and moving about works: holding W gathers speed (5 to 30 a second) and
     letting go glides; a tap beside a small planet takes it, going round brings it to about
     40° across, and zooming brings it nearer (never closer than 1.35 of its radius).
  2. **Labs:** runs `labs.html?lab=all` (a few minutes; TMP and TRK are the slow ones).
  3. **labs.html:** a card per lab, BAL run from its button, and `index.html?lab=`
     forwarding to `labs.html`.
  4. **sweep.html:** every example lays on the sweep, and the cursor sweeps.
  5. **dial.html:** a sure "two" costs about 3, 2 and 3 at s = 0.5, 1 and 2 (least at one pixel across).
  6. **sphere.html:** the address is the same at any scale, the octant's area is π/2, and the body's bands are off far
     away and on close up.
  7. **demos.html:** every page it links to is there, and the flying page's "demos" button opens it.
  8. **thin.html:** grains lit × brightest grain is the light caught, 1/v² everywhere; near full brightness, far one grain dimming 4× per doubling.
  9. **ladder.html:** parallax gives out by 30,000, width by 400,000, light reads past both (and gives out with photons counted).
  10. **sky.html:** the lit share within 0.01 of 1 − e^(−L/λ); always been, the whole sky lit.
  11. **Gameplay sketches:** each page's one mechanic through its hook (dimming, stages, the ladder's locks and light, the
      sky's count read back as time).
  12. **facing.html:** the facing is 90° at the corner, 0° at A, 180° at B; the arc stands off the line 1 − 1/√2 there, its most.
  13. **levels.html:** the near field in proportion, each level past the corner half the width of the last (s = 8 at 1.875),
      and one level fewer seen per doubling of the grain; the shape crosses ring edges, its broad form fewer; with the size divided out
      the depth averages 0 on the corner; a body from res/ chosen in the combo box crosses ring edges, a non-.tvf file refused; a draw .tvf curve read
      from its centroid (a 5-pointed star's tip over its dip as drawn).

  It fails on an uncaught error, or on a lab returning "error" or no verdict.
  "Killed" is listed but doesn't fail the run, because the page treats it as a
  recorded result. When this was set up, WOB, ELV and EQV were the killed ones.
- Run `npm test` before every PR.

## Related repos
games, draw, 3d and flare are the owner's other projects. wander doesn't depend
on any of them.
