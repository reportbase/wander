# Only a name: where π and e do work, and where they do not

*The twenty-fourth of a series of essays on what can be known from where one stands. Draft, 14 November 2026. It gathers
one day's runs on where π and e sit in laws: a blind sort of where they enter (SPN R989; PIE), a rule for when they are
only notation and its count on the paper's laws (R990; NTN), the loops that come back turned computed in fractions
(R991; HLX), the same rule on a list of standard formulas (R995; NTX), and a blind tag that showed what sorts them (R996;
DVA). Three of the five runs killed a prediction of mine, and the numbers here are what was left.*

Everyone who did trigonometry at school learned two kinds of formula with π in them, and nobody told them they were
different kinds. One is the area of a circle, πr². Take away π and there is nothing left to say: the law is that the
area is that particular number times r². The other is the double-angle formula, cos 2θ = 1 − 2 sin²θ, with θ in radians,
so π is somewhere in the angle. Take away the angle and write the direction by its slope s instead, and the same law
reads cos 2θ = (1 − s²)/(1 + s²): a fraction of fractions, true at every slope, and no π anywhere. In the first, π does
work no other number could. In the second, it is only a name the angle brings with it.

This essay is about how often each happens. The question came out of the series' rule that a read uses no
trigonometry: a read has slopes and shares, and an angle, with the π it brings, is the blueprint's way of writing them
(*Reads and Writes* §1). If that is right, many laws among directions should not need π at all, and the ones that do
should need it for a reason that can be named. Both turned out to be true, and the first less often than I expected.

The order: the rule (§1), the paper's laws (§2), loops that come back turned (§3), a list nobody chose (§4), what sorts
them (§5), what stays content (§6), whether thirty of eighty is a lot (§7), what is classical and what is ours (§8), and
what it changes (§9).

*Demo: `notation.html` (one turn written two ways, π in a limit, all 189 laws as tiles, the cross-table).*

---

## 1. The rule

A rule had to be written before any law was looked at, or I would have found what I wanted. It was this (NTN,
`plans/ntn-plan.md`): a law's π or e is **notation** if the same relation can be restated using only rational operations
and square roots, with no π, no e and no trigonometric, hyperbolic or logarithmic function, and the restatement agrees
with the original to 10⁻³⁰ at three or more points. Otherwise it is **content**.

Three things do not count as a restatement. Taking a ratio of two laws to cancel the constant: that states a different,
weaker relation. Restating part of a law and leaving the rest: the part that keeps π still needs it. Moving the constant
to the other side and calling the result a definition: e^(iπ) = −1 does not lose its π by being read as a definition of
π. And one case was settled before the second list was tagged: renaming an exponential of an amount, k = e^(−t/τ), is
not a restatement, because the law is about t and τ and the renaming hides e in the new letter.

A script checked every claimed restatement: the agreement at 50 digits, and the absence of every forbidden token in both
the text and the code that computes it. A restatement that agreed but carried a stray "sin" in its prose failed. Two did,
on the second list, and stayed failed.

## 2. The paper's laws

*Reads and Writes* states 125 laws, listed by a fresh agent from the paper's text (LWS). A mechanical flag found 82 that
carry π or e. Before the rule, a second fresh agent, not told what I was looking for, sorted the 82 by where the
transcendental enters: on a chart where turns or scalings add (the angle, the logarithm), in a limit or a total, or
neither (PIE, `plans/pie-plan.md`). My prediction was that nearly every one, at least nine in ten, would be chart or
limit. It was killed: chart 34, limit 32, neither 16. The sixteen were projections (8), loops that come back turned (4),
identities among angles (3) and Kepler's third law (1).

The sixteen looked like shares in an angle's dress, which is what the rule was written to test. Its predictions were
committed first, and none was killed (NTN):

- ten of the eleven projections and identities are notation (at least nine predicted);
- none of the five others, the four loops and Kepler (at most one predicted);
- none of the 32 limits (at most eight predicted);
- twenty of the 34 charts (at least seventeen predicted).

So 30 of the 82. A projection's cos α is the share h of one length, 1/√(1 + s²); a chart's tan(φ/2) is the half-slope
itself; Lambert's cosine, the Cayley map, the boosted sky's stretch, a lens's falloff, the hyperbolic secant of a level,
sech(ln k) = 2k/(1 + k²): each turned out to be a relation among slopes that had been written in an angle or a
logarithm. What kept π was every limit (Wallis, the odd sums, the Gaussian's normalization, Euler's (1 + iθ/n)ⁿ), every
total stated for its own sake (the 2π that makes a density integrate to one over a screen), fourteen charts in which the
chart itself is the statement (ln as a level, gd as a turn), one identity, (θ/sin θ)·(sin θ/θ) = 1, whose two factors
are each a limit, and the five laws the rule left alone.

## 3. Loops that come back turned

Four of those five were the holonomy laws: two turns about two axes and back, a turn and a stretch and back, two boosts
joined (the Thomas–Wigner rotation), and the leading term of a small loop. The rule could not restate them because each
states its leftover as an angle, Θ, and the angle is the one thing the restatement removes.

So the loops were computed, not restated (HLX, `plans/hlx-plan.md`). Every turn, stretch and boost was built from rational
half-slopes, the loop multiplied out in exact fractions (four quaternions; a 2 × 2 matrix; three 4 × 4 Lorentz matrices),
and the leftover read off at the end. Nothing was killed. In all fifteen cases the leftover's half-slope squared came out
rational and equal to the law: two turns of half-slope 2 and 3/4 about axes with cosine 2/3 between them leave
cos(Θ/2) = 17/25; a turn of half-slope 1/3 against a stretch of 9/4 leaves cosh ζ = 9/8; boosts of half-rapidity 1/5 and
2/3 at cosine 2/3 leave tan²(Θ/2) = 20/2401. The fourth law, the leading term ε²·sin φ, is a limit and stays one.

So the chain that does not close, the one shape essay 23 left untested, closes its own accounts in fractions. What it
leaves is a turn, and the turn's half-slope is rational. Its angle is notation.

## 4. A list nobody chose

Thirty of eighty-two is a count of laws written in this series' own framing, by the author of the framing. The obvious
worry is that the paper wrote its laws so they would pass. So the same rule was run on a list it did not write (NTX,
`plans/ntx-plan.md`): a fresh agent listed 107 standard formulas carrying π or e from its own knowledge, across geometry,
trigonometry, analysis, number theory, probability, mechanics, thermodynamics, electromagnetism, circuits, signals,
optics, quantum mechanics and relativity; another fresh agent classed them blind as before; I restated them, and the same checker judged.

The predictions, committed first:

- between 20% and 55% notation: **killed**, 18 of 107 (17%);
- at most 10% of the limits: not killed, none of 42;
- at least 40% of the charts: **killed**, 17 of 63 (27%);
- at least half of the neither class: as good as void, one of two, and that one carries no π as listed;
- the charts ahead of the limits by 30 points: **killed**, by 27.

My own reading of the borderline cases gives 16 of 106, not 18 of 107; the checker's count is the one reported. Either
way it is about one in six, half the paper's rate.

## 5. What sorts them

Why half? The rule is the same, the checker the same, the blind classes made the same way. The difference had to be in
the laws. So both lists were tagged blind once more, by a question that has nothing to do with π (DVA,
`plans/dva-plan.md`): does the law relate only directions and ratios of like quantities (D), or does an amount with a unit
enter, a time over a time constant, an energy over kT, a position over a scale (A)?

The predictions were that the tag would sort them: at least 60% of D laws notation and at most 10% of A laws, on each
list. Both **killed**. D laws were notation at 41% on the paper's list and 32% on the standard one; the paper's A laws at
19%. Two predictions held. Notation is nearly confined to D: 41 of the 48 notation laws are tagged D. And the lists differ
in their mix: D is 80% of the paper's list and 41% of the standard one.

Then, looking afterwards, the tags crossed with the blind classes:

| | Reads and Writes | standard formulas |
|---|---|---|
| directions, no limit | 27 of 43 (63%) | 14 of 24 (58%) |
| directions, a limit or total | 0 of 23 | 0 of 20 |
| an amount, no limit | 3 of 7 (43%) | 4 of 41 (10%) |
| an amount, a limit or total | 0 of 9 | 0 of 22 |
| all | 30 of 82 (37%) | 18 of 107 (17%) |

Two things stand out. Every limit and every total is content, 74 of 74, on both lists, whoever wrote them. And the laws
that relate directions without taking a limit are notation about three times in five on both lists, 63% and 58%: the rate
does not depend on who wrote the law. The paper's higher count is mostly that it holds more of those laws, a little over
half its list against a fifth of the standard one. The row that does not agree is the amounts without a limit, 43% against
10%, and the paper has only seven of them; it is too small to say whether its writing helped there.

The table was found after the runs, not predicted. "About three in five" is a reading of two lists, not a tested result.

## 6. What stays content

Content without a limit falls into a few kinds, and each has a reason that can be said.

- **A total stated for itself.** The 1/2π that makes a density over a screen integrate to one; the 4π of a whole sphere.
  The law is the total, and the total is that number.
- **An identity that states an angle's value.** arctan x + arctan(1/x) = π/2; Machin's π/4 = 4 arctan(1/5) − arctan(1/239);
  Euler's e^(iπ) + 1 = 0. Each has a form among slopes that keeps its relation (w(s)·w(1/s) = −1 is the series' own), but
  what the classical form states is the value, and the value is π.
- **A chart taken as the subject.** ln x = ∫ dt/t, decibels, Tsiolkovsky's rocket equation, the capstan's tension e^(μθ).
  The logarithm or the exponential is not dressing a relation among slopes; it is the relation.
- **A whole turn counted as a period.** Kepler's third law carries 4π² because a year is one whole turn counted in seconds.

And among amounts the rule almost never succeeds, because an amount brings its own exponential: e^(−E/kT), e^(−t/τ),
a Gaussian in x. The law is about the amount, and the e is how it falls.

## 7. Is thirty of eighty a lot?

Yes. More than a third of the laws in this paper that carry π or e do not need it, and that is not what one would guess
from looking at them: tan(φ/2), cos α, sech(ln k), e^(2iθ) all look as though π or e were built in.

Three things keep it in proportion. The paper chose its laws, and most of them relate directions; on a list nobody chose
for that, it is one in six. Some of the restatements are classical: the half-angle parametrization of the circle,
tan(θ/2) = s/(1 + √(1 + s²)), and the Cauchy as 1/(1 + s²) are old. And I made the restatements and judged the borderline;
a stricter or looser hand would move the count by a few, not by tens.

What does not need a qualifier is the split. On both lists, by a test written down first and judged by script, a limit
never lost its π or e, and a law among directions without a limit lost it more often than not.

## 8. What is classical and what is ours

Classical: every restatement. The half-angle substitution and the rational parametrization of the circle (Euler,
Weierstrass), the Cayley form of a rotation, tangent addition, the hyperbolic functions as rational functions of e^x,
quaternions and Lorentz matrices with rational entries, Wallis and Leibniz. That a law can be written without
trigonometry is no news to anyone who has rationalized an integral.

Ours: the count and the sorting. A fixed rule applied to two whole lists, one of them chosen by someone else, judged by
script; the blind classes and tags; the finding that limits keep π on both lists without exception; the table that puts
the two lists' different rates down to their mix of laws for directions without a limit; and the holonomy laws closed in
fractions. The restatements are mine, and so is the reading of what the content cases have in common.

## 9. What it changes

The series has said that a read uses no trigonometry and that π is the blueprint's (*Reads and Writes* §1, R909). These
runs put a number on how far that reaches into the laws themselves. Where a law relates directions and takes no limit, π
or e is more often than not a name the angle or the logarithm brings, and the law holds without it. Where a law takes a
limit, states a total or a value, or is about an amount, π or e does work, and saying so is not a criticism of the law:
it says what kind of law it is.

It also narrows a sentence. "Thirty of eighty-two" was this paper's count, and on its own it read as though the framing
made laws simpler. The second list says otherwise: the framing does not make a law shed its π; it is the kind of law that
does. The papers now say "about three in five, on both lists" where they said "thirty of eighty-two" (R996).

The next test is the obvious one: a third list, from a source nobody here chose (a physics handbook's index, say), with
"three in five for laws among directions without a limit, none for limits" committed before the tagging. That would turn
a reading into a result, or kill it. §10 is that test, and seven lists more.

## 10. Eight more lists, and where the line is

The third list came, and seven more after it (R998–R1006). Each was drawn from ten Wikipedia articles nobody here had used,
listed by one fresh agent, classed blind by another, restated by a third and checked by the same script, the predictions
committed before the fetch. The rule for what counts as notation never changed. What changed, list by list, was the line
the blind judge was asked to draw beforehand.

| list | the line drawn first | its side | the other side | overall, against expected |
|---|---|---|---|---|
| DVB (physics list pages) | directions or amounts | void (4 laws) | 10.9% | 10.8% against 10.6% |
| DVC (optics, crystals, the sky) | directions or amounts | 92.4% | 75.5% | 84.9% against 37.7% |
| DVE | where π or e enters | 52 of 52 | 19.1% | 54.2% against 41.6% |
| DVF | the same, sharpened | 13 of 13 | 23.1% | 35.9% against 17.8% |
| DVG | a chart of a ratio of like quantities | 84.1% | 3.9% | 50.0% against 54.2% |
| DVH | the chart, angle outputs and values settled | 98.0% | 30.0% | 86.7% against 77.2% |
| DVI | and ranges, turns, approximations settled | 97.8% | 6.5% | 74.2% against 69.0% |
| DVJ | the same briefs, unchanged | 92.0% | 35.0% | 82.5% against 77.2% |

(DVG's second run, the same list with the restater's one open call settled, gave 98.6% and 19.6%; not a fresh test.)

The chart side held from DVG on. Where π or e enters only through a circular or hyperbolic function of an angle or a
rapidity, and that angle stands for a ratio of two like quantities (a direction, a speed against light's, a phase of two
like coefficients), the law restates exactly in slopes and shares: 335 of 358 on four fresh lists, 94%. Of the 23 that
did not, eleven are DVG's, mostly Euler angles read back from a matrix, which that run's restater called content because
the angle was the output, before the briefs said how to treat it; the rest are a hyperbolic side read as a length, a
logarithm of lengths that is an inverse hyperbolic function in disguise, an angle differentiated, a matrix exponential of
amounts.

The other side held whenever the judge was clear. Amounts inside a function (ωt, kx, a time over a time constant),
whole turns as periods and totals (2π a revolution, 4π a sphere, 2π a wavelength), integrals, series and limits,
logarithms of amounts, and an angle used beside its own sine as in Kepler's equation stayed content on every list.

What never settled was the edge, and the edge moved every time it was named. Settle angles given by an inverse function
and the leaks are stated values (θ = π/2); settle those and they are ranges (0 ≤ θ < 2π) and a whole turn added to an
angle; settle those and they are supplements written outside a function (A′ = π − a, the azimuth's ± π branches). In
none of them did the script fail. Each time two agents read one symbol two ways: the judge, by the letter of its brief,
as an amount of turning, the restater as a direction.

That is the finding I would keep, and it is a reading, made after the runs and untested as a claim: classical notation
writes one letter for two things. θ in cos θ is a direction; θ in θ + 2π, in Kepler's E − e·sin E, in "turned through 3π"
is an amount of turn, a count. The law's text does not say which, and the rule cannot be made to say it for the law. Where
θ is a direction, its π is a name (the read's side, R909); where θ is an amount of turn, π is doing work, the turn
counted (the count's side, R896). Most laws make plain which; the ones that do not are where the lists leaked.

Three things keep it in proportion. The restatements are classical (the half-angle substitution, Weierstrass's). Every
agent was a fresh instance of one model, blind to the others but not independent the way different people would be. And
the overall share was within its window on four of the eight lists that predicted it; it depends on each list's mix.

Essay 25 takes the other side of the same line. Counted as a direction, the turn's π is never reached: equal small reads
composed in whole numbers pass the horizon at a count that bounds π from above, landing exactly only at the corner's two
clicks. Where π and e cancel in one equation, as in e^(iπ) = −1, the result is one of a read's three landmarks, and the
theorems behind it hold the turn completed.

---

## Sources

- `../../plans/bld-plan.md`, `../../runs/bld/`: counts of reads toward π and e (BLD run 1); essay 25.
- `../../plans/pie-plan.md`, `../../runs/pie/`: the 82 flagged laws and their blind classes (PIE run 1).
- `../../plans/ntn-plan.md`, `../../runs/ntn/`: the rule, the restatements and the checker on the paper's laws (NTN run 1).
- `../../plans/hlx-plan.md`, `../../runs/hlx/`: the three holonomy laws computed in fractions (HLX run 1).
- `../../plans/ntx-plan.md`, `../../runs/ntx/`: the 107 standard formulas, their blind classes, restatements and checker
  (NTX run 1).
- `../../plans/dva-plan.md`, `../../runs/dva/`: the blind direction/amount tags, the cross with both checkers, and
  `laws.json` (all 189 laws with tag, class, verdict and restatement, written by `export.py`) (DVA run 1).
- `../../plans/lws-plan.md`, `../../runs/lws/`: the 125 laws of *Reads and Writes* (LWS).
- *Reads and Writes* (`../readers-and-writers.md`) §1 "A read uses no trigonometry", "The shape of a law" and "Where π and
  e are content"; *Reads and Writes in Physics* §5.4.
- Essay 2 §9 (the three grades of cost), essay 13 §4 (holonomy), essay 14 §6, essay 15 §6, essay 23 §8.
- `../../plans/dvb-plan.md`, `dvc-plan.md`, `dve-plan.md`, `dvf-plan.md`, `dvg-plan.md`, `dvh-plan.md`, `dvi-plan.md`,
  `dvj-plan.md` and `../../runs/dv{b,c,e,f,g,h,i,j}/`: the eight further lists (R998–R1006).
- Demo: `../../notation.html`.
