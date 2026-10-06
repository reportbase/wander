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
- `papers/`: **the master copies of the owner's papers**, edited here from now on
  (branch, PR, merge, like the page). `serial-parallel-nowhere.md` (SPN) is the
  paper behind the labs (§9.9 the labs, §11.4 the conjecture, §12–§14 their
  standing); `v-and-h.md` gathers every idea about v and h, by item.
  `serial-parallel-nowhere-record.md` is SPN as written 29 Sep – 1 Oct, before the
  rewrite: **a frozen record, never edited.** Section and proposition numbers cited
  in the corpus before the rewrite are the record's; SPN's opening note maps them to
  the current ones. The papers cite others not in this repo (*Reader Geometry as
  Addressing*, `plans/…`): leave those references as they are. `_config.yml`
  keeps `papers/` and `plans/` off the Pages site.
- `plans/`: working notes, reviews and lab plans, as the corpus cites them
  (`plans/…`). `what-deserves-attention.md` is a review of what to take up next
  (6 Oct 2026): a reading, not a ruling. `hrt-plan.md` (the run for the 2: three
  runs, stopped) and `nle-plan.md` (number lines in people: run 1 on
  Chan and Mazzocco's kindergartners killed the corner's prediction) follow the lab rules: prediction first, runs recorded as they
  came out, nothing above a plan's "Runs" line edited afterwards.
  `part-one-audit.md` checks SPN Part I's proofs and numbers (6 Oct 2026): sound,
  with six fixes, applied to SPN on 6 Oct (marked *Corrected* there).
  `near-far-classification.md` answers one of its open questions: which near/far
  laws are fair to the facings (shares of a two-part split are; components are not).
  `horizon-recursion.md` (+ `spiral/`): the horizon with no preferred rung forces
  recursion; each octave a quarter turn for any ratio; the reading a logarithmic
  spiral (situations 1–2 the circle, k = 0). In SPN §3.3 as Propositions 3.11–3.13.
  `wavelets.md` (+ `wavelets/`): the system on one page, and what filters, wavelets
  and hearing scales already have of it (much), and what the situated view adds.
  `standpoint-axis.md` (+ `standpoint/`): a second axis, the standpoint (nowhere,
  outside, inside) beside the breadths known; the hemisphere observer as outside with
  the breadths known. Superseded by Tom's situations list 0–4 (SPN §2.1).

SPN's situations, since 6 Oct 2026 (Tom): 0 nothing known; 1 the circle; 2 shapes;
3 parallel, one hemisphere counted (outside); 4 serial, one point at a time
(inside); 3 and 4 possibly approximate. Older text uses the old numbers (its
"situation 3" is 3 and 4); SPN §2.1 has the mapping. Keep to the core: the sweep
(any two points; 0 to π/2 as a turn, 0 to 1 as distance), the 90° turn, the
octave, the logarithmic spiral.

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
  1. **Fly:** presses Fly, looks around, flies and taps a body.
  2. **Labs:** runs `labs.html?lab=all` (a few minutes; TMP and TRK are the slow ones).
  3. **labs.html:** a card per lab, BAL run from its button, and `index.html?lab=`
     forwarding to `labs.html`.

  It fails on an uncaught error, or on a lab returning "error" or no verdict.
  "Killed" is listed but doesn't fail the run, because the page treats it as a
  recorded result. When this was set up, WOB, ELV and EQV were the killed ones.
- Run `npm test` before every PR.

## Related repos
games, draw, 3d and flare are the owner's other projects. wander doesn't depend
on any of them.
