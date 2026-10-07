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
  world: run every lab after it.**
- `index.html`: the flying page (the world drawn, the controls, the readout, the
  live-view test hooks). Its "lab" button opens `labs.html`; `?lab=CODE` and
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
  and the labs: an array of pairs (v, h) divided by its own h, laid on the unit sweep
  g = (2/π)·atan(v/h) and read by a cursor, serially (4) or all at once (3), with the
  quarter circle (divided by the whole) beside it. `?ex=planets|shape|spread|line`,
  `?mode=parallel`. Not linked from index.html yet.
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
  octave, recursion, spiral), a map of how the parts depend, and the standing of each;
  then the central result and the open question (what fixes the ratio between rungs).
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
  pixels a look; a reader sliding its h by halvings needs about log₂(1/s) looks (not killed).
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

  It fails on an uncaught error, or on a lab returning "error" or no verdict.
  "Killed" is listed but doesn't fail the run, because the page treats it as a
  recorded result. When this was set up, WOB, ELV and EQV were the killed ones.
- Run `npm test` before every PR.

## Related repos
games, draw, 3d and flare are the owner's other projects. wander doesn't depend
on any of them.
