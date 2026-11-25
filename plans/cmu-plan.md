# CMU: is the Cauchy misunderstood, on cases not yet looked at?

25 November 2026 (Tom: "1 2 3", the second being a test of R1203's finding, "We have found repeatedly that cauchy is
misunderstood", on new cases). Predictions committed before the list is made.

**What is tested.** R1203: where the Cauchy turns up, the usual account treats it as a law of amounts (a heavy-tailed
quantity, its missing mean a pathology), and a turn laying directions can be named apart from the law's shape, the
amount carried by something else. The bound (R719, TCF): a fat tail from a mixture of amounts is no turn.

**Method.**
1. A fresh agent lists 30 occurrences of the Cauchy (or Lorentzian, Breit–Wigner, wrapped Cauchy, Poisson kernel,
   Lévy index 1) in science, engineering and statistics from its own knowledge, excluding the 58 of HZT's list
   (`plans/hzt/neutral-list.md`) and the cases already sorted (LIGO, canonical correlation, Fieller, gravity's Poisson
   kernel, Kepler's anomaly, seed dispersal). For each: field, what variable is Cauchy, how it arises, how the standard
   account describes it (two or three sentences, with a source it names).
2. A second fresh agent, shown neither the predictions nor R1203, classes each blind:
   - **origin**: T (a uniform angle, phase or direction, nameable in the system, maps to the variable by a tangent or
     a Möbius map), P (a pole a half-width off the real line, a damped oscillation or resonance), S (a stable sum or
     limit), M (a mixture of amounts, e.g. a scale mixture), O (other or unclear);
   - **account**: A (the standard account describes the variable as an amount: a heavy-tailed quantity, the missing
     mean or variance as a difficulty to handle) or D (it names the angle, phase or direction the law belongs to).
3. Claude checks each class against its own reading, the disagreements kept.

**Predictions.**
- **C1.** T and P together are at least half of the 30 (a phase turning at a steady rate is a turn, R362).
- **C2.** M at most a quarter.
- **C3.** Of the cases classed T or P, at least two thirds are classed A: the account treats the variable as an amount
  though a turn lays it. This is R1203's claim itself.
- **C4.** Of the cases classed T, the account names the angle (D) in at most half: a turn named in the derivation and
  dropped in the description.

Kills as stated; a kill by the classifier's reading against mine is reported as such, not overridden.

## Run 1

The list (`plans/cmu/list.md`, 30 entries, a fresh agent from memory) and the blind classification
(`plans/cmu/classification.md`, a second fresh agent shown only the list) came back as:

- Origin: T 2 (#2 Ott–Antonsen, #20 an irrelevant instrument), P 15 (resonances, line shapes, damped oscillations),
  S 4 (#5, 21, 23, 24), M 1 (#18 crystallite-size broadening), C 7 (chosen by a designer: #1, 3, 4, 22, 25, 26, 28),
  O 1 (#27 random Fourier features).
- Account: A 30, D 0.

**Verdicts.** C1 not killed (T + P = 17 of 30). C2 not killed (M = 1). C3 not killed (17 of 17 T or P cases classed A).
C4 not killed (0 of 2 T cases named the angle), weakly: two cases.

**Claude's check.** I agree with every origin. The classifier's own close calls: #2 and #4 have an angle as the
variable and were still classed A, since the accounts treat the law as a phase density or a concentration; #14 (phase
noise) and #15 (Hanle) are P, the Lorentzian from a decay rather than a named even phase. I would keep both.

**What it shows, and what it does not.**
- Unforeseen: a quarter of the cases (C, 7) are the Cauchy chosen as a tool for its heavy tail or its stability
  (sketches, hashing, annealing, mutation, Metropolis proposals, t-SNE, Kuramoto's tractable frequencies). There no
  system produces it, so R1203 does not bear on them: they are a designer's amounts by construction.
- Half the cases are P. That a pole a half-width off the line is a phase turning at a steady rate and fading is this
  corpus's reading (R362), not the classifier's; so C1's count of P as a turn rests on R362.
- C3 held at 17 of 17, but the label A included "a line shape or width", so the test asked only whether the account
  names the turn, and in none of 30 did it. That every account describes the law without its angle is the finding;
  that they are wrong to is R1203's reading of it.
- One mixture (#18) among 30: TCF's bound met once more.
