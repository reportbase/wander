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

