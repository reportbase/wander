# Wander

A world full of solids (pawns, rooks, knights, gems, vases, crystals and more),
above and below as well as all around, that you fly through. Behind it is a
world of stars, planets and travellers under gravity, seen only through the
signals that have reached you. A **lab** of experiments compares what you can
read from those signals against known results in physics.

**Fly:** https://reportbase.github.io/wander/ (once GitHub Pages is turned on
for this repo; see Publishing below)

## Controls

- **Look:** drag with one finger (or the mouse), sideways to turn, up or down to tilt
- **Fly:** drag with two fingers, up to go forward and down to go back
- **Go round a body:** tap it

## Link options

| Add to the link | What it does |
| --- | --- |
| `labs.html?lab=all` | Runs every lab and lists each one's latest verdict |
| `labs.html?lab=DOP` (or any lab code) | Runs that one lab and shows its full report |
| `index.html?lab=…` | Forwards to the same on `labs.html` |
| `index.html?lab=0` | Hides the lab button |

## Files

| File | What it is |
| --- | --- |
| `world.js` | Wander's world, shared by both pages: the constants, the solids, the systems and their ticks, the signals and their arrival, and the readings the live readout shares with the labs. A change here changes the labs' world too. |
| `index.html` | The flying page: the world drawn, the controls and the readout. Its "lab" button opens `labs.html`. |
| `labs.html` | The lab: what the labs are and how to read a verdict, a card per lab with a run button, the lab notes, and every lab's code. **THE LAB GUIDE**, a comment at the top of its script, explains how the labs work and how to add one. |
| `papers/` | The master copies of the papers: `serial-parallel-nowhere.md`, the paper the labs come from, `v-and-h.md`, every idea about v and h in one place, and `serial-parallel-nowhere-record.md`, SPN as first written (29 Sep – 1 Oct), kept unchanged as the record. Edited here (except the record); kept off the Pages site by `_config.yml`. |
| `plans/` | Working notes and reviews: `what-deserves-attention.md`, which ideas to take up next. Kept off the Pages site by `_config.yml`. |
| `tests/smoke.mjs` | The smoke test (see below). |

Only the fonts (Google Fonts) load from outside. Without them the page still
works, with fallback fonts.

## Running it locally

```sh
python3 -m http.server 8000
# then open http://localhost:8000/
```

## Smoke test

Every pull request runs `tests/smoke.mjs` in GitHub Actions, in two parts:

1. **Fly:** opens the page, presses Fly, looks around and flies for a few seconds.
2. **Labs:** opens `labs.html?lab=all`, which runs every lab, and reads the summary.
3. **labs.html:** checks there is a card for every lab, runs one (BAL) from its button, and checks that `index.html?lab=` forwards to `labs.html`.

It fails on any uncaught error, and on any lab that comes back "error" or with
no verdict. A lab that comes back "killed" is a recorded open question, not a
fault, so it is listed but does not fail the run. To run it yourself:

```sh
npm install
npx playwright install chromium
npm test
```

## Publishing

Turn on GitHub Pages once: **Settings → Pages → Deploy from a branch → `main`,
`/ (root)` → Save**. After that, merging to `main` updates the live site within
a minute or two.
