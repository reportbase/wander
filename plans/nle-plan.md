# NLE: number lines in people, against the corner

*Plan, prediction and kill written 6 October 2026, before any data was seen (Claude; Tom: "try both, proceed").
`plans/what-deserves-attention.md`, item 4. Script: `plans/nle/nle.py`. No dataset could be reached from the session
that wrote this (OSF, figshare and PubMed Central are blocked there), so the data is to be supplied; this plan is fixed
first. Results go below the line, as they fall; nothing above it is edited after data is seen.*

## The question

SPN's central hypothesis wants "an independent fact, not built to fit, that only a nesting reader explains", and names an
unchecked candidate: how people place numbers on a line, "proportional for familiar numbers, compressed beyond them,
with the switch point moving as the familiar range grows". R176's picture of a reader's scale is the same shape:
proportion from home to the corner, then a count of doublings past it.

The established rivals for bounded number lines (0–100, 0–1000) are the logarithm (Siegler and Opfer 2003) and
proportion judgment, a power model anchored at both ends and often the middle (Barth and Paladino 2011; Hollands and
Dyre 2000), which recent work tends to favour. So the corner has a real rival, and can lose.

## The models, fitted to each participant

| model | form | parameters |
|---|---|---|
| LIN | p = a·n + c | 2 |
| LOG | p = a·ln n + c | 2 |
| PWR1 | p = N·nᵇ / (nᵇ + (N − n)ᵇ), proportion judgment, one cycle | 1 |
| CNR | p = c + a·min(n, h) + a·h·ln(max(n, h)/h): proportion up to the corner h, then each doubling the same length, joined smoothly | 3 |

Least squares per participant, compared by BIC. A participant **departs from a straight line** if LOG beats LIN, or PWR1
beats LIN with its exponent outside 0.8–1.25 (at 1 it is a straight line), or CNR beats LIN with its corner inside the
line (h < 0.8 N).

## Calibration (made-up children, before any data; a check of the instrument, not a result)

200 made-up children per model, 24 targets on 0–100, noise sd 8 (`python3 plans/nle/nle.py --selftest`):

| made as | best: LIN | LOG | PWR1 | CNR | depart | of those, CNR beats PWR1 | PWR1 beats CNR |
|---|---|---|---|---|---|---|---|
| LIN | 80 | 0 | 114 | 6 | 37 | 6 | 31 |
| LOG | 0 | 190 | 0 | 10 | 200 | 200 | 0 |
| PWR1 | 25 | 0 | 171 | 4 | 175 | 4 | 171 |
| CNR | 0 | 55 | 0 | 145 | 200 | 200 | 0 |

What it says about the instrument, all found before data and fixed in the definitions above:
- PWR1 at b = 1 is a straight line with one parameter fewer than LIN, so "best fitted" is no guide to who is linear;
  hence the definition of departing.
- The head-to-head CNR against PWR1 is fair: each wins its own children. Its leftover bias runs **against** CNR (straight
  placers that slip in count for PWR1, 31 of 37).
- CNR against PWR1 cannot tell a corner from a plain logarithm (CNR wins LOG's children too). CNR against LOG can, but
  BIC's charge for the third parameter gives plain-log children to LOG (190 of 200) and 55 of 200 corner children too:
  it leans against the corner.

## Prediction (written before any data)

- **P1 (the kill).** Among participants who depart from a straight line, CNR beats PWR1 (lower BIC) for a majority.
- **P1b (reported, not a kill).** Among the same, CNR beats LOG for a majority: a front side in proportion is visible,
  not a plain logarithm from the start.
- **P2.** Where ages or grades are given, the fitted corner h rises with age (Spearman ρ > 0): the switch point moves
  as the familiar range grows.
- **P3.** Where each child's counting range is given, the fitted h falls within a factor 2 of it for a majority.

## Kill

- **P1 killed** if PWR1 beats CNR for a majority of those who depart. Then proportion judgment, anchored at the line's
  ends, describes the data better than a corner, and this candidate fact does not support the hypothesis.
- **P2 killed** if ρ < 0. **P3 killed** if h is within a factor 2 of the counting range for half or fewer.
- If P1b fails while P1 holds, the data is compressed but shows no front side: a logarithm, not a corner.

## What would count, and what would not

A pass on P1 and P1b says the corner model describes number-line placement better than its rivals on data the project
did not build. It does not say *why*, and it does not reach the 2: the corner h is fitted, not predicted. P3 is the part
that ties h to something outside the fit (the familiar range), and is the strongest if a dataset has it.

## Data wanted

One CSV of trials: participant, target, estimate (in the line's numbers), and if possible age or grade and counting
range. Candidates found but not reachable from the session: the OSF dataset of 28 targets on 0–1000 for third and fifth
graders (osf.io/74fzn); Chan and Mazzocco's materials on OSF; the Macquarie dataset of 324 Singapore kindergarteners on
0–100 (researchdata.edu.au; figshare, possibly embargoed). Then:

    python3 plans/nle/nle.py data.csv --max 100 [--participant ... --target ... --estimate ... --age ... --count ...]

## For Chan and Mazzocco's data (osf.io/kqe2w), fixed before seeing it

*Added 6 October from the paper (Chan and Mazzocco 2024, J. Exp. Child Psych. 245, 105965), before any of its data was
seen.* 104 U.S. kindergartners (mean age 5.9), tested at Time 1 and, after six weeks of training, at Time 2. Lines 0–20
and 0–100, each with and without a labelled midpoint, eight trials a type; the line runs on past its upper end, and one
or two targets a type lie beyond it (105, 120; 22, 24, 31, 33).

- **Which trials.** The 0–100 lines, both kinds (with and without the midpoint) pooled within a time: 14 targets
  inside 0–100 per child per time. Targets beyond 100 are left out, as PWR1 has no reading past the line's end. The
  labelled midpoint invites anchoring, which favours PWR1: a bias against the corner, accepted.
- **Which time decides.** **Time 1** (before training) carries the kill; Time 2 is reported beside it.
- **The 0–20 lines** are run the same way and reported, not part of the kill (kindergartners count to about 20, so
  most will be straight there).
- **Ages** are given only as a group (SD 0.34 years); P2 and P3 are not tested on this dataset.
- If the file holds only error scores (PAE, sequence errors) and not each estimate, it cannot be used, and this is
  recorded as such.

## References

- Barth, H. C. and Paladino, A. M. (2011). The development of numerical estimation: evidence against a representational
  shift. *Developmental Science* 14, 125–135.
- Hollands, J. G. and Dyre, B. P. (2000). Bias in proportion judgments: the cyclical power model. *Psychological Review*
  107, 500–524.
- Chan, J. Y.-C. and Mazzocco, M. M. M. (2024). New measures of number line estimation performance reveal children's
  ordinal understanding of numbers. *Journal of Experimental Child Psychology* 245, 105965. Data: osf.io/kqe2w.
- Siegler, R. S. and Opfer, J. E. (2003). The development of numerical estimation: evidence for multiple
  representations of numerical quantity. *Psychological Science* 14, 237–243.

---

## Runs

*(none yet: waiting on data)*
