# OPN: how shapes open into the fisheye (for observation-from-somewhere.md §7.4)

*11 October 2026. Tom, to adding the shape-opening contrast to the paper: "ok". The 73-shape run it repeats is SPN §2.4
and `v-and-h.md` item 331 (`vh/unclose.py`, on svg.html's shape library, not in this repository); this plan repeats the
method on shapes defined exactly, so the paper's numbers can be reproduced here: `ofs/opening.py`.*

**Method.** Each shape is read from its centre as v/h = |y|/|x|, laid two ways: evenly by direction, and in equal steps of
arc length along its outline (2,000,000 points). Four numbers: corner P(s < 1); middle, the median of s; head
P(s < e)/e at e = 0.025; tail s·P(S > s) at s = 40. Shapes: circle, square, astroid, an ellipse twice as tall as wide.

**Prediction** (written into the script before it ran). By direction every shape gives (0.5, 1, 0.637, 0.637), the
circle's. Along the outline, shapes unchanged when x and y are swapped keep corner 0.5 and middle 1 and differ only in
head and tail; a shape not so symmetric moves its corner and middle too. Killed if a shape laid by direction departs from
the circle's numbers, or a swap-symmetric shape moves its corner off 0.5.

## Runs

### Run 1 (11 October)

| shape | laid | corner | middle | head | tail |
|---|---|---|---|---|---|
| every shape | direction | 0.5000 | 1.0000 | 0.636 | 0.636 |
| circle | outline | 0.5000 | 1.0000 | 0.637 | 0.637 |
| square | outline | 0.5000 | 1.0000 | 0.500 | 0.500 |
| astroid | outline | 0.5000 | 1.0000 | 3.151 | 3.151 |
| ellipse, b = 2 | outline | 0.3728 | 1.4786 | 0.413 | 0.826 |

Not killed. Against the library run (item 331): circle 0.636 and square 0.500 agree; the astroid's 3.151 against 3.141
differs in the third figure, the cusp making the head sensitive to how the outline is sampled.
