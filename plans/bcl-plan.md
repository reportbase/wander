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

### Run 1 (10 Nov 2026)

The agent's answers, verbatim: `runs/bcl/responses.md`. Its only tool call was the one handing the report back.

Its classifications: 1 read (high); 2 read, a relation within one read, the angle the writer's notation (medium);
3 place (high); 4 none of these (medium); 5 none of these, a ratio of payloads (medium-high); 6 read, as the heat that
comes with it (medium); 7 none of these on the plain reading, turning on what the two normals are (medium-low); 8 read
as the direction of arrival (medium-high), the pairing with the source and the straight-line direction not settled;
9 the frequency in a unit a write (medium), the shift as a ratio none of these (low), the phrase as a whole not
settled; 10 not settled as one thing, counted directions carrying amounts in a unit, a write if forced (low).

Against the intended answers: all ten agree in substance. No case of 1–5 came back against them.

- B1 not killed. B2 not killed (weak, as stated).
- B3 not killed. Asked whether D6 could be applied from D1–D7 alone, it answered "No. It applied cleanly only in cases
  5 and 6", and of case 7: "cannot be applied without more information, because the case names no standpoint, no turn
  and no direction"; "D6 assumes the observation comes already divided." It also said no test looks at a distribution
  alone and tells its kind: "D6 has to be applied to the situation, not to the law."
- B4 killed. It split arrival from the source's position in case 8 as predicted, but case 8 was not where it was least
  sure: those were 9 and 10, then 7.

What it found that the predictions did not name (its findings, to weigh, none yet acted on):

1. Four boxes, three names. The two tests sort into moved by scaling; unmoved and a direction; unmoved and a gap
   across; unmoved and neither. D1–D7 name three; the fourth (a probability, a ratio of payloads) is acknowledged in
   D6 and named only in the paragraph after D7, which the agent did not have.
2. D4 and D7 give different criteria for a write. D4: "the across axis's zero tied to a unit" (a distance). D7: "being
   an amount in a unit is what makes it a write" (anything). A frequency in hertz or a pixel value is a write by D7 and
   not by D4, though D4 itself lists "a second".
3. D5 is stated for lengths only. What scaling does to times, speeds and the speed of light is not said, so the first
   test does not settle a Doppler shift; nor wavelengths against a sensor's passbands, nor brightness.
4. "The direction to a thing" is a pairing of a direction with what is met along it. D6 keeps the directions, not the
   pairing: replace or move the thing, or bend its light, and the pairing changes though no direction has.
5. D6 does not say a place stays. "Replace a wall by a row of trees" changes the distances met; only D3's "gap across"
   tells a place from paint.
6. D7's "what it is, not how it was had" sits awkwardly beside cases 6 and 7, which differ only in how one law was
   obtained. Its way out: the kind attaches to the variable (a direction's slope against a quotient of amounts), not
   to the law the two share.
7. D4's "a change of units … moves no read" is not true of a read stated as an angle in degrees, the writer's
   coordinate.
8. "Heat", "paint", "payload" and "the turn" are undefined within D1–D7. Partly the test's own doing: the paper
   defines them in §3 and §4, which the agent was not given.

Reading. The vulnerability the test was aimed at is real and is the one R820's first sentence states: D6 tests a
candidate once its standpoint and turn are named. R820's second sentence (the direction of arrival) answers finding 4
for refraction. Findings 2 and 3 are gaps in the definitions the edits do not touch.

Limits: one agent, one run, and a model that knows the classical material. Cases 4 and 5 are named in D6's own text, so
agreement there shows little.

### Run 2: the revised definitions (planned 10 Nov 2026, before the run)

After ChatGPT's reply to run 1 and Tom's "yes, second brach": D4, D5, D6 and D7 revised (SPN R820, R821), and the
paragraph and grid after D7 given to the agent as well, since they now carry the fourth box's name. A second fresh
agent, the same four questions, the same ten cases and two new ones:

11. The ratio of the brightness of two sources seen along two different directions from one standpoint.
12. The change in the received frequency of a source's light when the observer is boosted to a stated speed toward it,
    the source's own emission unchanged.

Intended answers: 1–10 as before, with 4, 5 and 7 now named ratios of payloads (4 and 7 only once said to be of what
arrives), 9's frequency in hertz a payload's write and its ratio a ratio of payloads, 10 several variables of several
kinds. 11: a ratio of payloads (the two directions are reads). 12: the received frequency in hertz a payload's write,
moved by a scaling of times; the ratio of received to emitted frequency a ratio of payloads; the same boost also moves
the direction of arrival, a read, and the test sorts the quantities, not the cause.

Predictions (Claude's, before the run):

- C1. Cases 1–3 read, read, place again.
- C2. Cases 4, 5, 7, 11 placed in the fourth box by name, 4 and 7 with the condition that they are of what arrives.
- C3. Case 9 and case 12 settled where run 1 could not settle 9: the frequency in a unit a write, the ratio a ratio of
  payloads, with D5 applied as a scaling of times. Killed if it again says D5 cannot be applied.
- C4. Case 10 answered as several variables, not "cannot be settled as one thing".
- C5. It will still name at least one thing the definitions do not supply. My guess at which: what a scaling of times
  does to the speed of light and so to the boost in case 12.
- Killed outright if a case that agreed in run 1 now comes back against the intended answer.
