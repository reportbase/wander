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
