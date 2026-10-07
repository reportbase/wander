# GRN: serial or parallel is set by the reader's grain, not by the system

*Plan, prediction and kill written 7 October 2026, before the script was written or run (Claude). From Tom: "just
imagine we are observing a system from across the universe … moving closer to us … when its very far away, we are just
getting a signal that is below our grain or resolution … then the system gets close enough that our grain can represent
it. i just described how a serial signal becomes a parallel signal"; and "the idea is that serial and parallel is just
our perspective, not the system's." Synthetic, as Tom asked ("with synthetic data, we can precisely model the situation
quickly"). The lab rules hold: nothing above the "Runs" line is edited after the run.*

## The claim, in SPN's terms

Let the reader's grain be h (its resolution, an angle) and the system's apparent size v (its extent over its distance).
Below the corner, s = v/h < 1, the system is a part of one grain: the reader gets one point, and learns about the system
only over time (serial). Past it, s > 1, a grain is a part of the system: the reader gets many points at once
(parallel). If serial and parallel are the reader's perspective, which reading works should depend on s alone, and
change over at the corner.

## The system and the two readers

**The system:** a binary of two equal stars, equal mass, on a circular orbit seen edge-on, true separation a, at
distance D. Its apparent separation is θ = a/D, so s = θ/h. The thing to recover is a.

- **The parallel reader:** one image at greatest separation. Each star is a Gaussian spot of width h/2 (so h is the
  grain), on pixels h/4 wide, with the same noise in every pixel. It fits two equal spots, centred on the known middle,
  for their separation, and reads a = θ̂·D.
- **The serial reader:** one point, no image. It reads the stars' velocity difference over one orbit, 20 times evenly
  spaced, with noise: Δv = aω·sin ωt. It fits the amplitude and reads a = K̂/ω. Nothing in this reading depends on D.

Both readers get the same light at every distance (the 1/D² fall in light is left out, as it would hurt both alike).
Noise is set so that the serial reader's error in a is 5%. 300 trials at each of 15 values of s, from 0.1 to 5.

## What holds by construction

The parallel reader's image depends on the system only through θ = a/D. So two systems of different size, at distances
that give the same s, look the same to it. That is the claim in its exact form, and it holds by construction, so it is
not tested. It is checked as a sanity test: three systems, a = 0.1, 1 and 10, at distances giving the same s, must give
the same error to within the sampling noise.

## Prediction

- **P1 (the kill): the knee is at the corner.** The parallel reader's error in a rises steeply as s falls below about 1.
  Call the knee the s at which its RMS relative error is twice its value at s = 5. Predicted between s = 0.5 and 2.
  Where the knee falls is set by the grain (the spot width), not by the noise level, which only sets how high the curve
  sits.
- **P2: the serial reader is flat.** Its error does not depend on s (within 10% across the range).
- **P3 (reported): the switch.** At this noise the serial reader wins below some s and the parallel reader wins above
  it. Reported, not predicted, since where they cross depends on the noise chosen for each; P1 is the part that does not.

## Kill

- **P1 killed** if the knee falls outside 0.5 to 2. Then the corner of resolution is not where the change from serial
  to parallel happens, even for a reader built this way.
- **P2 killed** if the serial reader's error varies by more than 10% across s. (It should not; that would be a bug.)

## Runs

### Run 1 (7 October, `python3 plans/grn/grn.py`, seed 5, 300 trials at each s): P1 and P2 killed

| s | 0.10 | 0.18 | 0.31 | 0.40 | 0.54 | 0.71 | 0.94 | 1.24 | 1.64 | 2.16 | 2.86 | 3.78 | 5.00 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| parallel, RMS relative error | 0.967 | 0.585 | 0.227 | 0.116 | 0.073 | 0.042 | 0.027 | 0.018 | 0.014 | 0.011 | 0.009 | 0.007 | 0.0054 |
| serial | 0.049 | 0.049 | 0.050 | 0.051 | 0.051 | 0.051 | 0.047 | 0.050 | 0.053 | 0.050 | 0.048 | 0.051 | 0.053 |

- **P1 killed.** The parallel reader's error reaches twice its s = 5 value at s = 2.28, outside 0.5 to 2.
- **P2 killed.** The serial reader's error spans 0.0470 to 0.0534 across s, a spread of 13.6%, over the 10% allowed.
- **Reported:** the parallel reader first beats the serial one between s = 0.54 and 0.71. Sanity check passed: at
  s = 0.8, systems of size 0.1, 1 and 10 give 0.035, 0.035, 0.034.

**Why, read after the run (not a rescue: both kills stand).**
- *P1's measure could not see a knee.* Once the stars are resolved, the parallel reader's error in the separation is
  a fixed angle, so its relative error falls as 1/s, halving with every doubling of s, all the way out. "Twice the value
  at s = 5" therefore lands near s = 2.5 whatever the grain does. The measure tracked that tail, not the corner. The
  fault was in the plan.
- *P2's tolerance ignored sampling noise.* With 300 trials an RMS error is itself uncertain by about 4%, and the
  largest and smallest of 15 such values can easily differ by 13%. The serial error shows no trend with s. The fault was
  in the kill condition, not the reader.
- A fix is a new run with its own prediction, below.

### Run 2: prediction and kill (written before run 2; informed by run 1, see below)

**Not blind.** Run 1's table already holds the parallel reader's *absolute* error, the relative error times s. Read off
it, that error is about 0.02 of a grain from s = 5 down to about 1 and rises below. So this prediction was written after
seeing those numbers. It runs on a new seed with 1,000 trials at each s. A pass here tests whether run 1's pattern holds
up, not whether it was foreseen.

- **P1′ (the kill): the knee in absolute error is at the corner.** The parallel reader's RMS error in θ, in grains, is
  flat for large s, the plateau being its mean over s ≥ 2. The knee is the largest s at which it reaches twice the
  plateau. Predicted between s = 0.5 and 2. Killed if outside.
- **P2′: the serial reader shows no trend with s.** Fitted against log s, its log error has a slope between −0.03 and
  0.03. Killed if not.
- **Reported:** where the parallel reader first beats the serial one, as in run 1.

### Run 2 (7 October, `grn.run2()`, seed 23, 1,000 trials at each s): P1′ killed, P2′ not killed

| s | 0.10 | 0.18 | 0.23 | 0.31 | 0.40 | 0.54 | 0.71 | 0.94 | 1.24 | 1.64 | 2.16 | 2.86 | 3.78 | 5.00 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| parallel, RMS error in θ (grains) | 0.100 | 0.104 | 0.096 | 0.069 | 0.052 | 0.038 | 0.032 | 0.025 | 0.023 | 0.023 | 0.024 | 0.026 | 0.027 | 0.027 |
| serial, RMS relative error | 0.050 | 0.049 | 0.051 | 0.051 | 0.050 | 0.049 | 0.051 | 0.053 | 0.050 | 0.051 | 0.049 | 0.051 | 0.049 | 0.050 |

- **P1′ killed.** The plateau (s ≥ 2) is 0.026 of a grain, and the largest s at which the error reaches twice that is
  0.31 (0.40 gives 0.0516, just under the 0.0522 needed). The knee lies below the corner, outside 0.5 to 2.
- **P2′ not killed.** The serial reader's log error against log s has a slope of +0.003.
- **Reported:** the parallel reader first beats the serial one at s = 0.71, as in run 1 (0.54 to 0.71).
- Below s ≈ 0.2 the parallel error is about s itself: it reads the two stars as one (separation about 0).

**What the two runs say.**
- **Supported, by construction:** the reading depends on the system only through s, its size against the grain.
  Systems of size 0.1, 1 and 10 at the same s read alike. In this exact sense, serial or parallel is the reader's
  perspective, not the system's.
- **Supported, measured:** as the system comes closer, the reading that works changes from serial to parallel. Here the
  change falls at s ≈ 0.7, and it would move with the noise given to each reader.
- **Not supported:** that the change sits at the corner, s = 1, set by the grain alone. With this much light, the
  parallel reader resolves the pair down to about 0.3 to 0.4 of a grain. How far below the grain an image still
  resolves depends on how much light there is, not on the grain alone. The corner of resolution is a soft edge, moved by
  signal against noise, not a fixed line at s = 1.
- **A next run, if wanted:** the same at several light levels. That would predict, before running, how the knee moves
  with signal-to-noise, for example as a power of it.

### Run 3: the pixel is the reader's (prediction and kill written before run 3)

Tom, after run 2: "well, if we are getting one pixel of data, then all of a sudden we are getting two pixels of data,
something happened. the pixel is ours, not theirs."

**What runs 1 and 2 borrowed.** Their parallel reader had pixels a quarter of its grain, and it fitted a model it was
given ("two equal stars"). Knowing the shape beforehand is situation 2's knowledge, a held whole, not a situated
reader's. That is what let it read below its grain. Run 3 takes both away: the reader's pixel *is* its grain, and it
has no model. It only counts how many pixels are lit.

**The reader.** Pixels 1 grain wide, with the grid's offset random against the system. Two point stars, apparent
separation s, each lighting the pixel it falls in, with pixel noise. A pixel counts as lit if its light passes a
threshold set well above the noise. The reader reports one thing or two by whether one pixel or more is lit.

**Prediction.**
- **P1 (the kill): two pixels are certain from the corner on.** For s ≥ 1 the two stars are never in the same pixel, so
  the reader sees two for every trial. Below the corner it sees two only when the grid happens to fall between them,
  with probability s. Predicted: P(two) = s for s < 1, and 1 for s ≥ 1, within sampling error (3 standard errors) at
  every s tested.
- **P2:** no sub-grain separation is read. The reader reports a count, never a separation smaller than one pixel.
  Built in, and checked.

**What this would mean.** It is geometry, so it holds almost by construction; that is the point. For a reader with no
model, the corner s = 1 is exactly where "two" becomes certain: the smallest size that cannot fit in one of its own
pixels. Below it, "two" is a matter of where the reader's grid happens to fall, the reader's accident, not the
system's.

**Kill.** P1 killed if P(two) differs from min(s, 1) by more than 3 standard errors at any tested s.
