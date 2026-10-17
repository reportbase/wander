# HZT: the horizon test, the unbounded face

*17 October 2026 (Tom's local date). Tom, 12:59: "1,2,3", to Claude's list, whose third item was the horizon test
proposed in `plans/tpi-report.md` §6.5 (SPN R255; Tom then: "Maybe a sweep is the better clue, there needs to b a
horizon and a sweep over it.."). SPN R340. Predictions written before the search, before the classifier and before any
script exists.*

## The claim

TPI gathered the bounded face of a sweep, its share or shadow, 2/π on the circle. This test gathers the unbounded face:
the reading laid on a line, with its median at the corner and no mean. On the even turn that face is the Cauchy; the
Lorentzian, the Breit–Wigner shape and the half-plane's Poisson kernel are the same law under other names.

Tom's suggestion, as a claim: **the unbounded face shows up where something is swept, evenly, to a horizon**, an end
where one of the two parties vanishes and the reading v/h runs off. A sweep is an angle or a phase taken evenly, or a
line swept evenly, from one end to the other.

**The bridge to "situated"** is the corpus's, named and not tested here (R233, R240): a turn, and a division by one's
own party, belong to a situated reader. The test asks where the face comes from, not whether each system is a reader.

## The method

1. **Gather.** A fresh agent collects occurrences of the Cauchy and its kin across fields: each with its formula, its
   field, a source, and the step of the standard derivation where the Cauchy form arises. It is not shown this plan,
   the corpus or the suggestion. It is asked for occurrences, not for sweeps.
2. **Classify, blind.** A second fresh agent, shown only the gathered list stripped of the gatherer's commentary,
   answers three questions for each entry, with a confidence and an alternative where it is unsure:
   - **Q1 (a sweep to a horizon).** Is an angle or phase taken evenly, or a line swept evenly, to where one of two
     amounts vanishes, so that their ratio runs off? Yes, hidden (the evenness comes from an isotropic or
     equal-spread pair, or a uniform phase), or no.
   - **Q2 (traversed).** Is that angle, phase or line traversed in order by a process, held at once as a set, or not
     traversed (an identity, a limit, a convention)?
   - **Q3 (whose evenness).** The observer's or an instrument's own sweep; a source's or a system's; a population's;
     or none.
3. **Check.** Each entry's Cauchy form is computed exactly (mpmath) from the derivation step it gives, where the step
   can be put as a computation: the law, its half-width, the share within one half-width of the centre (½), and the
   mean's divergence (the integral to S grows as (1/π)·ln S for the standard form).

## What was known before writing

- From the corpus and TPI: the lighthouse (Gull 1988), the resonance phase (Beth and Uhlenbeck 1937), the harmonic
  measure of a half-plane (Kakutani 1944), an inverted noisy parallax (Bailer-Jones 2015), the ratio of two
  independent centred normals of equal spread, the t law with one degree of freedom, the stable law of index 1, the
  Lorentzian line shape of a damped oscillator and of pressure broadening, the Breit–Wigner resonance, Jaynes's
  Cauchy and the lighthouse in Sivia and Skilling.
- Thought of while writing, before any search: the Lorentzian as the Fourier transform of e^(−γ|t|) (an exponential
  decay); the Cauchy as the hitting point of a two-dimensional Brownian motion on a line; the Cauchy as the image of a
  uniform angle under tan; the Cauchy as a stable law, the limit of sums of variables with tails ~1/x²; the Cauchy
  kernel in the Poisson integral; Lorentz–Lorenz and the Drude response near a pole; the Voigt profile's Lorentzian
  part; the Cauchy as a Student t with ν = 1; the Cauchy as the ratio of a normal to an independent |normal|.

## Predictions

- **H1 (the claim).** Every occurrence traces to a sweep reaching a horizon (Q1 yes or hidden). *Killed* by any
  occurrence whose standard derivation, traced, has no such sweep. **A kill is named in advance as likely**: the Cauchy
  reached as the stable limit of summed heavy-tailed amounts (index 1), with no angle or phase taken evenly. If that
  kills H1, the clue is bounded to a mechanism: a sweep reaching a horizon gives the face, and so does a sum whose
  terms have the right tail.
- **H2 (traversed or held).** Among Q1-yes or hidden entries, those held at once (a population, a static field) are at
  least as many as those traversed in order by a process, as in TPI run 4. *Killed* if the traversed outnumber the
  held by more than two to one.
- **H3 (whose evenness).** Among Q1-yes or hidden entries, the observer's or instrument's own sweep is at most a
  quarter; the source's, the system's or a population's are the rest. *Killed* if the observer's own is more than a
  quarter.
- **H4 (the corner).** In every Q1-yes entry where the sweep is an even turn or phase over its quarter (or half) to the
  horizon, half of the law lies within one half-width of its centre, and that half-width is where the sweep stands at
  half its range (45° of a quarter turn, or the phase's middle ± 45°). *Killed* if any such entry's half-width falls
  elsewhere, computed exactly.
- **H5 (no mean).** Every occurrence's law has no mean: its first moment diverges as the range grows. *Killed* by any
  that has one; truncated forms (a Lorentzian cut at a finite band) are recorded as truncated, not as kills, if the
  source says it cuts.

## What would and would not be shown

If H1 holds, every unbounded face found traces to a sweep reaching a horizon, across fields: the structure Tom
suggested. If it is killed by the stable limit as expected, the face has (at least) two origins, the sweep and the
heavy-tailed sum, and the clue is the sweep's only where a sweep is present. Neither outcome shows that a system is a
reader. H3 says how often the sweep is the observer's own; if rarely, that says where the situated reader is left out
of the textbooks, as TPI run 4 found for the bounded face.

## Runs

(None yet. Nothing above this line is edited after a run.)
