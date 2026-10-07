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

### Run 3 (7 October, `grn.run3()`, seed 31, 4,000 trials at each s): not killed

| s | 0.10 | 0.18 | 0.25 | 0.31 | 0.40 | 0.50 | 0.71 | 0.90 | 0.94 | 1.00 | 1.10 | 1.24 | 2.16 | 5.00 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P(two), measured | 0.097 | 0.159 | 0.258 | 0.297 | 0.395 | 0.498 | 0.708 | 0.903 | 0.938 | 1 | 1 | 1 | 1 | 1 |
| min(s, 1), predicted | 0.100 | 0.175 | 0.250 | 0.306 | 0.404 | 0.500 | 0.707 | 0.900 | 0.935 | 1 | 1 | 1 | 1 | 1 |

- **P1 not killed.** P(two) follows min(s, 1) at all 21 values of s tested. The largest departure is 2.7 standard
  errors (at s = 0.175), under the 3 allowed. From s = 1 on, two pixels are lit in every trial.
- **P2 holds by construction.** The reader reports a count, never a sub-pixel separation.

**What the three runs say together.** A reader that is given the system's shape (runs 1 and 2) can read below its
grain. That borrowed knowledge is situation 2's, the held whole. A reader with only its own pixels (run 3) cannot. For
that reader the corner is exact: s = 1 is the smallest size that cannot fit in one of its pixels, where "two" becomes
certain. Below it, "two" depends only on where the reader's grid happens to fall, with probability s: the reader's
accident, not the system's. In Tom's words, the pixel is ours, not theirs.

### Run 4: below the corner a chance, past it a certainty; and the slider (prediction written before run 4)

Tom: "the geometry should tell us what to expect from signals"; and "maybe the corner is adjustable, could the reader
move his h unit like a slider to get a better read on the situation." Same model-free reader as run 3: pixels one grain
wide, the grid's offset random on every look, and the reader counting lit pixels.

- **P1 (the kill), below the corner.** With the grain fixed at 1 and s < 1, each look shows "two" with probability s,
  independently. The looks needed until the first "two" average 1/s. Predicted within 3 standard errors at every s
  tested, from 0.05 to 0.9.
- **P2 (the kill), past the corner.** For s ≥ 1, every look shows at least two pixels, and the mean number of lit
  pixels is 1 + s. That is exact geometry: a span of s crosses s grid lines on average, at any s. Predicted within 3
  standard errors at every s tested, from 1 to 8. So the average grows smoothly through the corner, and what changes
  there is certainty, not the mean.
- **P3, the slider.** A reader that halves its grain after every look without "two" (h = 1, ½, ¼, …; s doubles each
  time) reaches its corner in about log₂(1/s) looks. Its mean looks are at most log₂(1/s) + 2 at every s, against 1/s
  for the fixed grain. The bound holds by construction (by look ⌈log₂(1/s)⌉ + 1, s has passed 1), so it is a check, not
  a test. Reported: the mean looks, and the s at which the slider stops, predicted to lie between 1 and 2. The slider
  reads just past its own corner, no finer.
- **What it would mean.** Below its corner a reader buys structure with time, at 1/s looks. Past it, structure comes
  in each look, s pixels at once. A reader that can move its h trades that reciprocal cost for a logarithmic one, by
  sliding its corner to the system, one doubling at a time.

### Run 4 (7 October, `grn.run4()`, seed 41, 20,000 trials at each s): not killed

| s | 0.05 | 0.1 | 0.2 | 0.3 | 0.5 | 0.7 | 0.9 |
|---|---|---|---|---|---|---|---|
| fixed grain: mean looks to "two" | 20.2 | 10.1 | 4.96 | 3.29 | 2.02 | 1.42 | 1.11 |
| predicted, 1/s | 20 | 10 | 5 | 3.33 | 2 | 1.43 | 1.11 |
| slider: mean looks | 3.97 | 3.14 | 2.37 | 1.98 | 1.50 | 1.31 | 1.10 |
| bound, log₂(1/s) + 2 | 6.32 | 5.32 | 4.32 | 3.74 | 3 | 2.51 | 2.15 |

| s | 1 | 1.5 | 2 | 3.3 | 5 | 8 |
|---|---|---|---|---|---|---|
| mean lit pixels | 2.000 | 2.494 | 3.000 | 4.299 | 6.000 | 9.000 |
| predicted, 1 + s | 2 | 2.5 | 3 | 4.3 | 6 | 9 |
| P(two), two points | 1 | 1 | 1 | 1 | 1 | 1 |

- **P1 not killed.** The mean looks follow 1/s at every s; the largest departure is 2.4 standard errors (s = 0.3).
- **P2 not killed.** The mean lit pixels follow 1 + s (largest departure 1.8 standard errors), and two points are seen
  as two in every look from s = 1 on.
- **P3 (check) holds.** The slider needs about one more look per halving of s, about 4 looks at s = 0.05 against 20.
- **Reported, and not as written.** The slider was predicted to stop between s = 1 and 2. It never stops past 2 (the
  largest is 1.8), but it often stops *before* its corner, as low as s itself. On any look below the corner it sees
  "two" by chance, with probability s, and then has no need to zoom further. So the slider stops at its corner or
  sooner, never later.

**What run 4 says.** For a model-free reader, the geometry alone sets what a signal will give:
- **Below the corner,** structure arrives as a chance per look (probability s), and costs about 1/s looks: serial.
- **Past the corner,** it arrives with certainty, about s pixels in each look: parallel.
- **The two are each other's flip:** looks needed below, 1/s, and pixels given past, s. The average grows smoothly
  through the corner; what changes there is certainty.
- **A reader that can move its h** trades the reciprocal cost for a logarithmic one, about one look per doubling, by
  sliding its corner toward the system. Here the logarithm is the cost of moving the corner, not an assumption.
