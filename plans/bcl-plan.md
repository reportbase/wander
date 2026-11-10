# BCL: a blind classification by D1–D7

10 Nov 2026. After ChatGPT's first classification stress test of *Reads and Writes* (pasted by Tom; "Yes—make the
three small edits and run the blind classification exercise"). The question: can D6 be applied from the stated
definitions alone, or does applying it silently import a split between geometry and payload that D1–D7 have not
established?

## Method

A fresh agent, with no access to the paper, is given D1–D7 verbatim as they stand on main before this plan's edits,
and ten cases described neutrally. For each case it answers four questions (what changes under D5; what is held fixed
under D6; what quantity is being classified; what further information is needed) and commits a classification. Its
answers are kept verbatim in `runs/bcl/responses.md`. Only then are they compared with the intended answers below.

Limits, stated beforehand: one agent, one run; the agent is a language model that may know the classical material
(dimensional analysis, aberration, the ratio of normals); its blindness to the paper rests on its instructions (it is
told to use no tools and no files).

## Cases

1. The direction from a standpoint to a visible point.
2. The angular separation of two visible points, seen from one standpoint.
3. The ratio of two distances, obtained by parallax from two standpoints.
4. A dimensionless probability attached to an observation at one standpoint.
5. The ratio of two colour channels of the light arriving along one direction.
6. A Cauchy distribution obtained from a uniform turn about a standpoint (the slope of a uniformly turned direction).
7. A Cauchy distribution obtained as the ratio of two independent zero-mean normal quantities of equal spread.
8. The direction in which a source is seen when its light has been bent by refraction on the way.
9. The Doppler shift of the light arriving from a moving source.
10. A finite sensor's record (a grid of pixel values) of a continuous optical field.

## Intended answers (the paper's)

1. Read. 2. Read (two directions of one read; the angle is the writer's coordinate on them). 3. Place. 4. Not a read:
unmoved by scaling, not a direction; D6 sorts it out, the table does not hold it. 5. A ratio of payloads, a direction
in the payload's own space; not a read. 6. The read's heat, given with the directions. 7. A direction in the payload's
space; a Cauchy with no turn at a standpoint, not the read's heat. 8. The direction of arrival is a read; the source's
position is a further inference. 9. Payload; in hertz a write, as a ratio to a rest frequency a payload ratio needing
that frequency carried in. 10. A record: a count of cells and amounts in a unit; the field's directions are the read,
and no instrument is a pure read.

## Predictions (Claude's, before the run)

- B1. Cases 1–3 classified read, read, place.
- B2. Cases 4, 5 and 7 classified as not reads though unmoved by scaling (D6's own text names a probability and a ratio
  of amounts, so this is weak evidence).
- B3, the diagnostic. In at least one of cases 6, 7, 8 and 10 the agent says, unprompted, that D6 cannot be applied
  until something D1–D7 do not supply is settled (which standpoint and turn; what "direction" means once light bends).
  Killed if it applies D6 to all ten with no such flag.
- B4. Case 8 is where it is least sure: it either splits arrival from source position or asks which is meant.
- Killed outright (the definitions unclear) if two or more of cases 1–5 come back against the intended answers.

## Runs
