# DVI: the chart rule with ranges and turn totals settled, on a fresh list, predicted first

15 November 2026. Tom: "fx and test" (fix and test). DVH (R1004) held the chart side (98%) and leaked on the other side
at one boundary: ranges of an angle and a whole turn added to one (DVH 27, 29, 30, 55, 74), which the judge classed "a
turn as a range or total" and the restater took as statements about directions; and an approximation whose right side
restated whole (108). This run settles both in the same words in both briefs, keeps DVH's two sentences, and tests the
rule on a tenth list from ten Wikipedia articles not used before: Spherical coordinate system, Polar coordinate system,
Quaternions and spatial rotation, Haversine formula, Total internal reflection, Stereographic projection, Lorentz factor,
Waveplate, Precession, Ellipse.

## The sentences, in both briefs

DVH's two, unchanged:
1. **An angle given by an inverse circular or hyperbolic function of quantities** forming a ratio of like quantities is
   that ratio's chart: the judge classes it chart; the restater restates it by the angle's slope (or share, or
   half-slope) equal to the same expression.
2. **A stated value of a direction's angle** (θ = π/2, φ = 0, ±π) is a chart: chart; restated as the direction's shares
   or slope.

Added:
3. **A range of a direction's angle** (0 ≤ θ ≤ π, 0 ≤ φ < 2π) is a statement about which directions are meant: the
   judge classes it chart; the restater restates it as the same set of directions in shares or slopes. **But an angle
   carrying whole or half turns as an amount** (2π + 2·arctan(b/a), a total turned through, a number of turns, 2πn
   counted) is not a direction's angle: the judge classes it other; the restater marks it content, since its direction
   alone drops the turns.
4. **An approximation** (≈, ≅, ∼, O(·), "to first order") is not an exact relation: the judge classes it other; the
   restater marks it content, whatever its sides restate to.

## The list, the class, the restatements (as DVH)

`runs/dvi/fetch.py`, a fresh lister to `runs/dvi/laws.md`, `runs/dvi/sample.py` (seed 15112026, 120 if more); a fresh blind
judge with DVG's definition and the four sentences to `runs/dvi/chart.md`; a fresh restater with NTN's rule, the four
sentences and the checker to `runs/dvi/restate.py`, the checker printing no class split to it; I read every passing
restatement and record, before counting, any I judge not the same relation; the count by the rule is the one scored.

## Predictions (committed before any fetch)

- **I1** Laws judged chart are notation at 85% or more. Kill: under 85%; void if fewer than 15 chart laws.
- **I2** Laws judged other are notation at 10% or less. Kill: over 10%; void if fewer than 15 other laws.
- **I3** The overall notation share is (0.92·n(chart) + 0.03·n(other))/n, computed from the blind classes before the
  restatements are checked, and the true share is within 8 percentage points of it. Kill: further.

The rates are DVG's and DVH's, unchanged.

## Runs

(appended below as they come out; nothing above this line edited afterwards)

### Run 1 (15 Nov 2026; `runs/dvi/fetch.py`, list `runs/dvi/laws-all.md` sampled by `runs/dvi/sample.py` to `runs/dvi/laws.md`,
### class `runs/dvi/chart.md`, restatements `runs/dvi/restate.py`, each by its own fresh agent; scored by `runs/dvi/dvi.py`,
### I3's expectation `runs/dvi/dvi-expect.txt` committed before the check, output `runs/dvi/dvi-run1.txt`)

Pages fetched (revision id, timestamp, sha256 of the wikitext; the wikitext not committed):

| page | revision | timestamp | sha256 |
|---|---|---|---|
| Spherical coordinate system | 1383917922 | 2026-11-05T15:59:06Z | 37656a03dfdbd5d53b7a402efb77394363d0dc3c46d20a40c8059a1856604507 |
| Polar coordinate system | 1382008000 | 2026-10-26T00:56:32Z | 70d876257e4114c98ade1cd8ca2694cb01f2aac16f14aec7131c989634be69c6 |
| Quaternions and spatial rotation | 1370422953 | 2026-08-21T01:55:03Z | 9c747ca8287802831133304f2e7234b49d7ce0ecb1fd6d615d9e3029ca3023b9 |
| Haversine formula | 1383688779 | 2026-11-04T04:51:17Z | 443969909ff7c054992a1efc58db51e58db6ad968de8e20472dec729b6a5f88a |
| Total internal reflection | 1380935616 | 2026-10-18T22:10:48Z | acd48737e289b158fa30c1bebe85a050b0a0b816a497b9a1ea7d388daa45a45b |
| Stereographic projection | 1376614858 | 2026-09-25T05:26:19Z | 9c044320092b7ed8084970dd494839602a66caf8ec1a54cdf4d50a01ccc5e21d |
| Lorentz factor | 1382103367 | 2026-10-26T16:49:24Z | e97c4bcaab1663a511aa3a27864f42800453a2a46f3e22050040bfe2bb228393 |
| Waveplate | 1359162193 | 2026-06-13T14:32:19Z | 6d198813fcde2e7fdcb4b334d2c4a809dcfcbde8a057a3271f118c916c50457d |
| Precession | 1385526762 | 2026-11-13T19:30:28Z | 3531ae023097e5bde2fc21bb6dff7a42e33b87f481a27ee0ba9607817a74d243 |
| Ellipse | 1385637208 | 2026-11-14T11:17:39Z | 1ce9052da785ab6ed78c81a01efcaaa6b5624371f39572e24065ebbb408307b9 |

297 candidate blocks; a fresh agent listed 187 laws (`runs/dvi/laws-all.md`), sampled to 120. The lister left out bare
ranges and domain conditions as relations not stated (its own call), so sentence 3 is tested here only inside laws (96's
0 ≤ t ≤ 2π). The blind judge: chart 89, other 31. I3's expectation, written before the check: (0.92·89 + 0.03·31)/120 =
69.0%. A fresh restater marked 89 notation, every one passing the checker (0 failed), the checker printing it no class
split. I read every passing restatement before counting and judge none not the same relation (59 is restated as printed,
which the restater notes may be off by a factor of 2 from the true composition; the restatement and the original agree).

- **I1 not killed**: chart laws 87 of 89 notation (97.8%). The two content: 87 and 88 (tanh φ = β; γ = cosh φ), which
  this restater called a rapidity "a hyperbolic amount", against the chart rule and against DVH's restater, who restated
  rapidities by their slope.
- **I2 not killed**: other laws 2 of 31 notation (6.5%): 50 (α = 2π/3) and 51 (the unit quaternion from it), which the
  judge read as a total turned through and the restater as a stated value of a direction's angle.
- **I3 not killed**: 89 of 120 = 74.2%, against 69.0% ± 8.

Said plainly: for the first time all three predictions held, on a fresh list with the rule and both briefs written before
it. Read, post hoc and untested: what is left is two calls, each made one way by one agent and the other way by another:
whether a rotation angle stated as a number (2π/3) is a direction's value or a total, and whether a rapidity is a chart
(DVG, DVH) or an amount (this restater). Neither brief names rapidity's restatement as sentence 1 names an angle's. One
list; sentence 3 hardly met; nothing in the papers changed.
