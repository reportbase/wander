# TWC: two completions, a blind test

11 Nov 2026. SPN R834. Tom: "the hope is that the read / write framing might untangle these equations in an
interesting way."; then "yes" (to a blind test before more equations go into *Reads and Writes* §9).

## The question

After STT and CHS the equations on §9's list seemed to differ only in which of two things the writer has completed:
the turn (π) and the length (e). Is that a rule that predicts, or a relabelling of cases already seen? TPI (R251–R255)
is the precedent: a broad claim about 2/π was killed by a blind catalogue and a narrower one kept.

## The rule under test (fixed here, before any list is seen)

- **P (the turn).** π appears in a result exactly when its derivation takes whole the measure of a turn in a plane:
  the directions of a pair taken over a whole, half or quarter turn; or a figure a turn makes (a circle's or sphere's
  length, area or volume; a pair of equal-spread Gaussian amounts); or a period of the turn (a root of unity, a
  winding). It does not appear when no turn is taken whole, or when two such measures stand in a ratio that cancels.
- **E (the length).** e appears in a result exactly when its derivation completes an open amount by endlessly
  repeated proportional steps: a limit of the kind (1 + x/n)ⁿ, a product of unboundedly many near-equal factors, or
  what follows from "the amounts add and the chances multiply" over an unbounded range. It does not appear when the
  only exponential is a choice of chart (a logarithmic scale) or when the amounts are bounded and merely counted.

The rule's known weak point, stated beforehand: STT found π absent for an even number of parties, so P is the
plane's and may fail among more parties.

## Protocol

1. A fresh agent, not shown this plan, the rule or the conversation, chooses fifteen results with closed-form
   constants from at least five fields (probability, geometry, analysis, combinatorics, number theory, physics),
   avoiding the ones named in *Reads and Writes* §9 (the circle, the Cauchy, the Gaussian, the exponential, Euler's
   identity, Student's t, the logistic map, Stirling, Buffon, Wallis). It writes two files: `runs/twc/list.md`, each
   result described by its construction with every constant withheld (written as C), and `runs/twc/answers.md`, the
   full statement, whether π and whether e appear, and a numerical check of the constant.
2. I read `list.md` only, write a prediction (π yes/no, e yes/no, one line of reason from the rule, and whether I
   recognised the result from memory) for each into `runs/twc/predictions.md`, and commit it.
3. Then I read `answers.md` and score.

Blindness is imperfect: I may know a result from memory. Each prediction is marked "recognised" or "not", and the
scores are given for all fifteen and for the unrecognised ones apart. A prediction must follow the rule even where
memory disagrees; where it does, that is recorded as a predicted miss.

## Predictions (committed before the list exists)

- **W1.** P is right on at least 12 of 15. Kill: 11 or fewer.
- **W2.** E is right on at least 12 of 15. Kill: 11 or fewer.
- **W3.** Both right on at least 10 of 15. Kill: 9 or fewer.
- **W4.** The rule beats the baseline "predict the commoner answer for every item" on both constants, counted over all
  fifteen. Kill: it does not, on either.
- **W5.** Any miss of P involves more than two parties (a sphere, a Gamma function at a half-integer, a volume in
  higher dimensions). Kill: a miss of P in the plane.

## Runs

### Run 1 (11 Nov 2026; list and answers by a fresh agent, `runs/twc/list.md`, `answers.md`, `check.py`; my predictions `runs/twc/predictions.md`, committed before the answers were opened)

The agent's fifteen: 4 with π only (3, 6, 9, 13), 4 with e only (2, 7, 11, 15), 3 with both (4, 8, 12), 4 with
neither (1, 5, 10, 14); all its numerical checks agree with the closed forms (fourteen to 10⁻¹⁹ or better).

- **W1 killed.** P right on 11 of 15. Misses: 6 (∫ ln x·ln(1 − x) = 2 − π²/6), 8 (Lévy's constant, e^(π²/(12 ln 2))),
  9 (squarefree density 6/π²), 13 (∫ x³/(eˣ − 1) = π⁴/15). All four are ζ(2) or ζ(4).
- **W2 not killed.** E right on 13 of 15. Misses: 13 (the rule's letter said e from the Bose factor; integrating over
  the whole range leaves none) and 15 (the expected number of uniform draws to pass 1 is e, from Σ 1/n!, with no
  compounding in the construction).
- **W3 not killed, at its edge.** Both right on 10 of 15.
- **W4 not killed.** The baseline "always no" gets 8 of 15 on each constant; the rule 11 and 13.
- **W5 killed.** The misses of P are not among more parties: 6, 9 and 13 have no parties at all.

The test was not blind for me: I recognised all fifteen from memory, and said so in the predictions file before
scoring. The predictions followed the rule's letter against memory (five were marked "expect a miss", and all five
missed), so the score is the rule's, but an unrecognised subset does not exist to score apart.

### Reading

- P as stated is killed by the even zeta values. π enters 6, 8, 9 and 13 with no turn in the construction: through
  Σ 1/n², a sum over the whole numbers. The classical derivations of ζ(2) do pass through a turn's period (the sine's
  product, a Fourier series), and the rule lists "a period of the turn"; but nothing in the constructions shows it,
  and counting it would be TPI's hidden turns again (R252): a rule that can always find its turn afterwards predicts
  nothing. As a predictor from the construction, "π exactly when a turn is taken whole" fails one way: no false
  yes in fifteen, four false no.
- E did better and failed in two instructive ways. Integrating a completed exponential over its whole range can
  remove the e (13; the Gaussian integral √π, known beforehand, is the same case and I should have written the rule
  to exclude it). And e can arrive by counting orderings, Σ 1/n!, with no proportional growth anywhere (15).
- What survives: where a turn is taken whole and not divided out, π is there (3, 4, 12, and 14's ratio cancelling
  as the rule said); where rare independent events or the exponential map are completed, e is there (2, 7, 4, 11, 12).
  One direction of each rule holds on this list; "exactly when" does not.
- So the two-completions table is a relabelling of the cases it was built from, plus a one-way rule. It is not put
  into *Reads and Writes* as an organising principle.
