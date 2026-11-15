# DVB: a third list, the three-in-five predicted first

15 November 2026. Tom: "Do want to run a third list", then "Merge and run". DVA (R996) found, after the fact, that on two
lists every law taking a limit or total kept its π or e (74 of 74) and that laws relating only directions without a limit
were notation about three times in five (27 of 43 on *Reads and Writes*' list, 14 of 24 on NTX's standard formulas);
laws with an amount and no limit were notation at 43% (3 of 7) and 10% (4 of 41). That reading is untested. This run
tests it on a third list chosen by neither of us, with the numbers committed first.

## The list (fixed before anything is fetched)

The source is ten Wikipedia pages whose contents Wikipedia's editors chose, all physics:
List of equations in classical mechanics; List of equations in wave theory; List of equations in fluid mechanics; List of
equations in nuclear and particle physics; List of equations in quantum mechanics; List of electromagnetism equations;
List of equations in gravitation; List of photonics equations; List of relativistic equations; Table of thermodynamic
equations. (List of trigonometric identities was considered and left out: it is mathematics, not a list of laws of
physics, and would be nearly all directions.)

1. `runs/dvb/fetch.py` fetches each page's wikitext (`action=raw`) and records its revision id and sha256 in this plan's
   run entry. The wikitext is not committed (CC BY-SA, kept in the scratchpad).
2. The same script pulls every `<math>` block and every `{{math|…}}` block that contains π or e in any form: `\pi`, `π`,
   `e^`, `\exp`, `\ln`, `\log`, `\sin`, `\cos`, `\tan`, `\cot`, `\sec`, `\csc`, `\sinh`, `\cosh`, `\tanh`, `\arc…`,
   `\operatorname{…}` of those, and writes them with their page and the nearest heading or table label to
   `runs/dvb/candidates.md`.
3. A fresh agent gets `candidates.md` only (not this plan, not any earlier run or paper) and writes `runs/dvb/laws.md`,
   one law a line (`n. **name**: formula (page)`), in plain text, keeping every candidate that is an equation (a relation
   with an equals sign or a proportionality, or a defining formula of a quantity), merging exact duplicates, dropping only
   fragments that state no relation and formulas in which, written out, no π or e appears (a stray `e` for the charge).
   It records every dropped candidate and why at the foot of the file.
4. If more than 120 laws remain, `runs/dvb/sample.py` keeps a seeded sample of 120 (seed 15112026), in order.

## Blind sorting (each by its own fresh agent, given only `runs/dvb/laws.md` and the definitions, verbatim from before)

- **Class** (PIE's and NTX's definitions): **A** π or e enters through an additive chart, a coordinate in which turns or
  scalings add (an angle, a logarithm, an exponential as the chart's inverse); **L** through a limit, a series, an
  infinite product, or an integral over a whole or unbounded range, including a normalizing total; **X** neither. Writes
  `runs/dvb/blind-class.md`.
- **Tag** (DVA's definitions): **D** every quantity the law relates is a direction or a ratio of like quantities,
  dimensionless by construction (an angle, a slope, a share, a cosine, a rapidity, a ratio of two lengths or two
  intensities), and the law relates them among themselves; **A** an amount with a unit enters the law (a time, a length,
  an energy, a mass, a temperature, a frequency, a charge, a count), including where it is divided by a scale to make an
  exponent or an argument (t/τ, E/kT, ωt, x/a), or where the law's constant normalizes a density over amounts. Writes
  `runs/dvb/tags.md`.

## Restatements (a fourth fresh agent, given the list and the rule, not the classes, tags or predictions)

NTN's rule, unchanged: a law's π or e is notation if the same relation can be stated with slopes s = v/h (several for
several directions), the shares h = 1/√(1 + s²), v = s/√(1 + s²), rational operations and square roots of rational
expressions only, with no π, Ω, e, exponential, logarithm, circular or hyperbolic function, agreeing exactly (10⁻³⁰ at
50 digits) at three or more points; the same relation, not a ratio, a part, or the original with a constant moved.
Otherwise it is content. DVA's borderline, settled before: renaming an exponential of an amount (k = e^(−t/τ)) is not a
restatement. The agent writes `runs/dvb/restate.py` in NTN's format and is told that the checker rejects the forbidden
names anywhere in the restatement's text (so it writes "the slope's" in words, never "sin" or a lone "e").

`runs/dvb/check.py` is NTX's checker with the paths changed. I read every passing restatement and record, before
counting, any I judge not the same relation; the count by the rule is the one scored.

## Predictions (committed before any fetch)

Cells are the blind tag crossed with the blind class: "no limit" means class A or X, "a limit" class L.

- **Q1** Every law classed L is content. Kill: one notation law classed L.
- **Q2** Laws tagged D with no limit are notation at 45% to 75%. Kill: outside, or fewer than 10 such laws (then void).
- **Q3** Laws tagged A with no limit are notation at under 20%. Kill: 20% or more.
- **Q4** The overall notation share is 0.60·n(D, no limit) + 0.10·n(A, no limit), divided by the number of laws, computed
  from the blind tags and classes before the restatements are checked, and the true share is within 8 percentage points
  of it. Kill: further.

## Runs

(appended below as they come out; nothing above this line edited afterwards)

### Run 1 (15 Nov 2026; `runs/dvb/fetch.py`, list `runs/dvb/laws.md`, tags `runs/dvb/tags.md`, classes
### `runs/dvb/blind-class.md`, restatements `runs/dvb/restate.py`, each by its own fresh agent; scored by `runs/dvb/dvb.py`,
### Q4's expectation `runs/dvb/dvb-expect.txt` committed before the check, output `runs/dvb/dvb-run1.txt`)

Pages fetched (revision id, timestamp, sha256 of the wikitext; the wikitext not committed):

| page | revision | timestamp | sha256 |
|---|---|---|---|
| List of equations in classical mechanics | 1344409255 | 2026-03-20T07:57:28Z | e437b88151e9c7276d68e27f7c27a6e0fa0139b4f4f234a975baef1bf068cdb8 |
| List of equations in wave theory | 1331052854 | 2026-01-04T05:55:31Z | 91262668baa7ce7026c72c8d5006a18956bd8410c664b102b8e6f9ea77b38c13 |
| List of equations in fluid mechanics | 1189740927 | 2023-12-13T18:30:57Z | 0a7708292114ce6ee78f5fceff48ef924137c116816f03a6a6ba7adc1c9024a2 |
| List of equations in nuclear and particle physics | 1232378203 | 2024-07-03T12:54:45Z | 733f7294c2407f9f6fb523df53951df2149895e435b57c7514a653a49b29f0c8 |
| List of equations in quantum mechanics | 1345767720 | 2026-03-28T01:56:33Z | c696a00983d04ad91ef6a0b77c76fb7a4d943596aeec95f8f25cd693e215978b |
| List of electromagnetism equations | 1373572934 | 2026-09-06T18:16:53Z | 2d0a76b398c6ada9d833cbd8f6a283c91bcec71af906fca8534b9a8d4c0c6c05 |
| List of equations in gravitation | 1189741062 | 2023-12-13T18:32:05Z | 8b9e6c0bcc7075c22a246f09ccc201ce4363e27d5629e4457ed11e0bf4d6e7a4 |
| List of photonics equations | 1023739471 | 2021-05-18T02:17:38Z | 70a3dac6245bb0ca96b113de2cbcce53b4e80e5a8b8b497885cbccb15fc18645 |
| List of relativistic equations | 1282100692 | 2025-03-24T09:37:20Z | f792506d840c3460f21dd63c4dee472d5c7f575a834bc9c6d0995f81da003828 |
| Table of thermodynamic equations | 1355018747 | 2026-05-19T13:44:15Z | 75c52dbcd4007886e6b01ece838450b544bcbd3382dd323ebd998fd92d15ce36 |

92 candidate blocks (the photonics page has no `<math>` at all; fluid mechanics none carrying π or e); the list agent kept
83 laws and dropped 9 (four with no π or Euler's e, five fragments), under 120, so no sample. Tags D 4, A 79; classes
A 68, L 15, X 0. Q4's expectation, written before the check: (0.60·4 + 0.10·64)/83 = 10.6%. The restater claimed 9
notation; all 9 pass the check, and read before counting I judge all 9 the same relation (an angle entering only through
its cosine, sine or cosecant, written as a share of its slope or half-slope: 14 Mach's cone, 33 Rutherford's csc⁴(χ/2),
44 the AC phase, 45 the AC power factor, 62 the rotating body's field, 63–66 the relativistic Doppler shift and the
photon's momentum component).

- **Q1 not killed**: none of the 15 laws classed L is notation (with DVA's 74, 89 of 89 on three lists).
- **Q2 void**: only 4 laws tagged D with no limit (2 notation: 14, 44; content: 12, the phase as a share of the whole
  turn, φ/2π, and 13, the decibel level, a logarithm taken as the subject). The plan's own condition; the three-in-five
  reading is untested by this run.
- **Q3 not killed**: 7 of 64 laws tagged A with no limit are notation (10.9%, under 20%).
- **Q4 not killed**: 9 of 83 = 10.8%, against the 10.6% expected (0.2 points).

Said plainly: on a physics list chosen by Wikipedia's editors, laws relating directions alone are almost absent (4 of 83),
so the run could not test the rate that mattered most. What it did test held: every limit kept its π or e, laws with an
amount and no limit were notation about one time in ten (as on NTX's list, against the paper's 3 of 7), and the overall
rate was predicted from the list's mix before any restatement was checked, to 0.2 points.

Post hoc, untested: 7 of the 9 notation laws are tagged A, and in every one the π enters only through an angle that is a
direction inside an amount law (the power factor's φ, the Doppler shift's θ, the cross-section's χ). The tag asks whether
an amount enters; what the notation laws share is narrower: π or e entering only through a direction's angle, used only
by its cosine, sine or tangent. A test of that, on a list where such angles are common, would be the next step; this run
does not make it.
