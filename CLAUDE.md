# wander: notes for Claude

A world of solids you fly through, with a "lab" of experiments comparing what a
reader can recover from arriving signals against known physics. One page, served
by GitHub Pages at https://reportbase.github.io/wander/. The owner works through
Claude Code: changes go on a branch, as a PR, and the owner merges. Merging to
`main` publishes.

## Files
- `index.html`: **the whole thing and the file to edit.** One self-contained page
  with no build step; only Google Fonts load from outside.
- `labs.html`: a page that explains the labs and runs them. It holds no lab of its
  own: it reads each lab's note (`#labPane`) and `LAB_REGISTER` out of `index.html`
  and runs a lab via `index.html?lab=CODE` in a hidden iframe. Keep those (and the
  "KILLED"/"not killed" status wording) as they are and it needs no edits.
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
  (6 Oct 2026): a reading, not a ruling.

The repo is public, so the papers can be read on GitHub; the owner is fine with
that for now (6 Oct 2026) and will decide later where they live. They are still
kept off the Pages site. Don't move or remove them without asking.

## Read this first: THE LAB GUIDE
The labs have their own rules, written in the page itself. Read two comments
before touching anything lab-related:
- **THE LAB GUIDE**, at the top of the lab section of the script
- **THE LAB BUDGET** comment, before `#labPane`

In short:
- A lab's prediction and kill condition are written into its note **before** it
  runs.
- A killed run stays recorded as killed. A fix is a new run with its own
  prediction; never edit an old prediction to fit.
- After every change, run `?lab=all` (also the lab pane's "run every lab"). A
  lab going from "not killed" to "killed" or "error" means something broke; fix
  that before adding anything.

## Testing
- `npm test` runs `tests/smoke.mjs` in headless Chromium:
  1. **Fly:** presses Fly, looks around, flies and taps a body.
  2. **Labs:** runs `?lab=all` (a few minutes; TMP and TRK are the slow ones).
  3. **labs.html:** a card per lab, and BAL run from its button.

  It fails on an uncaught error, or on a lab returning "error" or no verdict.
  "Killed" is listed but doesn't fail the run, because the page treats it as a
  recorded result. When this was set up, WOB, ELV and EQV were the killed ones.
- Run `npm test` before every PR.

## Related repos
games, draw, 3d and flare are the owner's other projects. wander doesn't depend
on any of them.
