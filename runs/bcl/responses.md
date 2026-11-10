# BCL run 1: the blind classifier's answers, verbatim

10 Nov 2026. A fresh agent given only D1–D7 (as on main before R820's edits) and the ten cases of
`plans/bcl-plan.md`, with four questions a case and three closing questions. Its only tool call was the one that
handed this report back. The report is below, unedited.

---

CLASSIFICATION OF TEN CASES UNDER D1–D7
(No tools used. Worked only from the seven definitions as quoted. Where I had to assume something the definitions do not say, I mark it "ASSUMED".)

A point that affects almost every case, stated once: D6 says "the directions and their heat stay; the paint changes". Read literally, the thing that stays is the set of directions available at the standpoint (and its heat), not "the direction of thing X". If a wall is replaced by a row of trees, the direction along which the wall's corner used to be seen is still there, but the corner is not. So "the direction to a named thing" is a pairing of a direction with what is met along it, and D6 treats the two halves of that pairing differently. D1–D7 never say which half a phrase like "the direction to a visible point" names. I return to this in the closing questions.

------------------------------------------------------------
CASE 1. The direction from a standpoint to a visible point.

(a) D5: nothing changes. Multiplying every length by k about the standpoint moves the point along its own ray; [h : v] (or [h : v : v₂]) is the same. ASSUMED: the scaling is taken about the standpoint, or equivalently the standpoint is scaled with the world. D5 does not say what the centre of the scaling is; for directions between points of the world it does not matter.
(b) D6: held fixed are the standpoint, the turn, and the direction itself as one of the reader's directions, with its heat. What changes is what is met along it. If "the visible point" is itself part of what arrives (a mark on the wall that is replaced by trees), the point may cease to exist while the direction remains.
(c) The quantity is a direction, [h : v], or its slope s = v/h: the "up" part of D1's point. It is one direction out of the read, not the whole read (D2 says the read is "every sweep of the thumb at once ... given whole").
(d) Nothing more is needed to classify it. A reader of the definitions would want to know only whether "a read" may be said of one direction or only of the whole; D2's first sentence ("A read is the direction") allows the former.

Classification: READ. Confidence: high.

------------------------------------------------------------
CASE 2. The angular separation of two visible points, seen from one standpoint.

(a) D5: nothing changes; both directions are unchanged, so is any relation between them.
(b) D6: the two directions and the relation between them stay; what is met along each changes. Whether there are still "two visible points" there depends on what arrives.
(c) Two things should be separated:
   (i) the relation between two directions held in one read, at one standpoint and one moment (for instance the pair of slopes, or the slope of one counted from the other);
   (ii) that relation expressed as an angle, a number of degrees or radians. D1 says θ is "the writer's coordinate on the direction, the one in which turns add", and that the reader "uses no trigonometry". So the angle as a number is the writer's notation for (i).
(d) What D1–D7 do not settle:
   - Whether a relation between two directions inside one read counts as "a read". D2 defines the read as the direction(s), given whole; D7 speaks only of joining reads from two standpoints or two moments. Two directions of one read is a case neither covers by name. I take it as contained in the read because both are given at once and no second standpoint is needed.
   - A unit question. An angle in degrees changes its number under a change of units (degrees to radians). D4 says a change of units "moves every write's number and no place, no read". By that sentence taken alone, an angle in degrees behaves like a write under unit change, while under D5 it behaves like a read. D4 restricts a write to "the across axis's zero tied to a unit", and an angle is on the up axis, so it is not a write by definition. But D4's last sentence is then not strictly true of a read stated in the writer's angle. The definitions would need to say that a read's number in the writer's coordinate may depend on the writer's angular unit, or that the reader's form (slopes) is the one meant.

Classification: READ (a relation within one read; the angle is the writer's notation for it). It is not a place: it is not a gap across and needs no second standpoint. It is not a write: D5 leaves it unchanged. Confidence: medium, because of the two gaps under (d).

------------------------------------------------------------
CASE 3. The ratio of two distances, obtained by parallax from two standpoints.

(a) D5: nothing changes. Both distances and the step between the standpoints are multiplied by k; d₁/d₂ is the same.
(b) D6: this is where the definitions say least. D6 states only what happens to directions, heat and paint. A distance is a distance to something. If the change in what arrives is a repainting or a moved light, the things stay where they are and d₁/d₂ stays. If it is "replace a wall by a row of trees", what is met along each direction is now at a different distance, and the ratio of the distances met changes. So a place is unchanged by D6 only for changes that leave the positions of things alone. D6 does not say this; I infer it.
(c) The quantity is d₁/d₂: one distance against another, which D3 names word for word as a place.
(d) Nothing more is needed. Note that d₁/d₂ does not even need the step's length, only that there was a step. D7's last sentence also means the phrase "obtained by parallax" is not what makes it a place; it would be a place however it was had.

Classification: PLACE. Confidence: high.

One observation: D6's parenthesis says "a ratio of two amounts is unmoved by scaling and is still not a direction". d₁/d₂ is a ratio of two amounts in that sense. So D6 correctly keeps it out of "read", but D6 gives no means of telling a place from any other ratio of two amounts. That work is done only by D3's words "a gap across", that is, by the amounts being distances.

------------------------------------------------------------
CASE 4. A dimensionless probability attached to an observation at one standpoint.

(a) D5: nothing changes (D6 says so explicitly: "a probability ... is unmoved by scaling").
(b) D6: it depends entirely on what the probability is a probability of, which the case does not say.
   - If it is the share of the reader's directions falling in some set of directions (the measure the turn gives, which I take to be what D2 and D6 call "heat"), it stays under D6.
   - If it is a probability about what arrives (that the light along this direction is red, that a detector fires, that a thing is present), it changes when what arrives changes.
(c) The quantity is a dimensionless number in [0, 1] attached to an observation. That is all the case gives. It is not a direction, not a distance or ratio of distances, and not an amount in a unit.
(d) Needed: what event the probability is of, and over what it is taken (over directions of the turn, or over what arrives).

Working through the kinds:
   - Read: D6 says in so many words that a probability "is still not a direction". D2 says the read "comes with its heat, given", so a probability that is the heat belongs with the read; but D2 does not say the heat is a read, and "heat" is not defined in what I was given.
   - Place: no. D3 requires a gap across (a distance in thumbs or a ratio of distances) and a second standpoint. The case has one standpoint and no distance.
   - Write: no. D5 does not move it, and it has no unit.

Classification: NONE OF THESE, because D6 excludes it from "read" by name, D3 excludes it from "place" (no gap across), and D5 excludes it from "write". If it is the heat of a set of directions it accompanies a read without being one; if it is about what arrives it is a statement about paint. D1–D7 name three kinds and supply no fourth name for scale-invariant quantities that are neither directions nor distances, though D6 plainly acknowledges they exist ("a ratio of payloads"). Confidence: medium (high that it is not a place or a write; medium on whether the author would file the heat-type probability under "read").

------------------------------------------------------------
CASE 5. The ratio of two colour channels of the light arriving along one direction.

(a) D5: I believe nothing changes, but D5 does not settle it. D5 multiplies "every length in the world" by k. A wavelength is a length in the world. If wavelengths are scaled and the reader's channels (their passbands) are scaled too, the ratio is unchanged. If wavelengths are scaled and the channels are not, the light shifts across the channels and the ratio changes. If wavelengths are not counted among "lengths in the world", nothing changes. D5 names "the reader's thumb and stride" as included and says nothing of the reader's sensor. ASSUMED: either wavelengths are left alone or the sensor scales with them, so the ratio is unchanged.
(b) D6: the standpoint, the turn and the direction are fixed; the channel ratio changes when the world is repainted or the light is moved. This is exactly what D6 calls paint.
(c) Three things are in the case:
   (i) the direction along which the light arrives: a read (as case 1);
   (ii) each channel's amount: a payload amount in some unit of the sensor;
   (iii) the ratio of the two amounts: the quantity asked about.
(d) Needed to be fully sure: whether "paint met along it" in D2 is part of the read or only comes with it; and D5's treatment of wavelengths (above).

Classification of the ratio: NONE OF THESE, because it is a ratio of payloads: unmoved by scaling (so not a write), not a gap across (so not a place), and changed by D6 (so not a direction). It is the example D6 was written for. Confidence: medium-high.

A caution on D2's wording: "It comes with its heat, given, and the paint met along it." A reader could take this to mean the paint is part of the read, which would make this ratio "part of a read". D6 pulls the other way. I followed D6, because D6 is the test and D2's sentence can be read as "accompanies".

------------------------------------------------------------
CASE 6. A Cauchy distribution obtained from a uniform turn about a standpoint (the slope of a uniformly turned direction).

(a) D5: nothing changes. No length enters: the slope is a ratio of the two shares of one direction, and the turn has no size.
(b) D6: nothing changes. The standpoint and the turn are exactly what D6 holds fixed; the law of the slopes depends on nothing that arrives.
(c) Two things:
   (i) the slope s = v/h of one direction: a read, in the reader's own form (D1);
   (ii) the distribution of s over the turn: a law on the directions. I take this to be what D2 and D6 call the "heat" of the directions. ASSUMED: "heat" means the density of the reader's directions per unit of the reading. D1–D7 use the word three times and never define it (D2 refers to §4, which I do not have).
(d) Needed: the definition of "heat", and whether the heat is counted as part of the read. Also, "uniform" is uniform in θ, which D1 calls the writer's coordinate; so the statement "the turn is uniform" is made in the writer's notation even though the resulting law is on the reader's slopes. The definitions do not say whether that matters for the kind.

Classification: READ, in the sense that it is the heat that comes with the read (D2: "It comes with its heat, given"; D6: "The directions and their heat stay"). It is not itself a single direction. Confidence: medium-high on "belongs with the read and passes both tests"; medium on calling a distribution "a read", since D2 says the read is the direction and the heat comes with it.

------------------------------------------------------------
CASE 7. A Cauchy distribution obtained as the ratio of two independent zero-mean normal quantities of equal spread.

(a) D5: nothing changes, in either reading. If the two normal quantities are lengths, both are multiplied by k and the ratio is unchanged. If they are not lengths (voltages, counts), D5 does not touch them at all.
(b) D6: cannot be applied without more information, because the case names no standpoint, no turn and no direction. If the two quantities are things that arrive (two measured amounts), then changing what arrives (unequal spreads, a non-zero mean, a different law) changes the distribution of the ratio; it is then a ratio of payloads. If instead the two quantities are the two components of one arriving vector whose direction is seen from the standpoint, the ratio is that direction's slope, and equal spread with independence is a statement that the directions are uniform by turn; it is then case 6 reached by another route, but its uniformity is now a property of what arrives rather than of the turn, so D6 would still move it (make the spreads unequal and the law changes).
(c) Two things:
   (i) the variable: a quotient X/Y of two quantities;
   (ii) its distribution: the same mathematical law as in case 6.
   The kinds in D1–D7 attach to (i), not to (ii). The same law can sit on a direction's slope (case 6) or on a quotient of two amounts (here).
(d) Needed: what X and Y are. Specifically, whether they are two payload amounts or the two shares of one direction; and, if the latter, whether the uniformity comes from the turn (fixed under D6) or from the source (changed under D6).

Classification: NONE OF THESE, because on the plain reading it is a ratio of two payload amounts: D5 leaves it unchanged (not a write), it is not a gap across (not a place), and D6's own parenthesis says such a ratio "is still not a direction". Confidence: medium-low, since the answer turns on (d).

A tension I could not resolve from the text: D7 says "A quantity's kind is what it is, not how it was had." Cases 6 and 7 differ, as stated, only in how the Cauchy "was obtained". If the object classified is the distribution, D7 would seem to say the two cases must have one kind, while D6 says they differ. The way out is that the object classified is the variable (a direction against a quotient of amounts), and the two cases have different variables that happen to share a law. But D7 does not say that; it is my reading. The definitions also give no test that looks at a distribution alone and says which kind it is, and I think none is possible: D6 has to be applied to the situation, not to the law.

------------------------------------------------------------
CASE 8. The direction in which a source is seen when its light has been bent by refraction on the way.

(a) D5: nothing changes, provided the refracting medium is scaled with the world (its shape multiplied by k, its refractive index, a pure number, unchanged). Then every ray is the same figure enlarged and arrives along the same direction. ASSUMED: the medium is part of "the world" for D5. If the medium has its own fixed length that is not scaled (D5 says every length is scaled, so this should not happen), the apparent direction could move.
(b) D6: this depends on which quantity is meant (see (c)), and on whether the refracting medium counts as part of "what arrives". D6 lists "move the light" among its changes. Changing the medium moves the light. Under that change the reader's directions and heat stay; but the direction along which this particular source is seen changes.
(c) Three things:
   (i) the direction of arrival: the direction, at the standpoint, along which the source's light comes in. This is what the reader holds: [h : v] with that paint on it.
   (ii) the pairing "this source is seen along that direction". This is a direction together with what is met along it.
   (iii) the straight-line direction from the standpoint to where the source is, D1's u in d·u. No read at this standpoint holds it; getting it needs knowledge of the medium.
(d) Needed: which of (i)–(iii) is meant; whether the medium is "what arrives" or part of the fixed setting; and whether, for the author, "the direction" in D1 is the straight-line direction to the point or the direction of arrival. D1 writes the point as d·u, which is the straight-line picture, and says nothing about bent paths.

Classification: (i) the direction in which the source is seen, as a direction of arrival: READ. Confidence: medium-high. It is a direction, it is what one standpoint at one moment is given, and D5 leaves it unchanged.
For (ii), the pairing: it is a read together with its paint; D6 changes it (bend the light differently and the same source paints a different direction). D1–D7 have no name for the pairing.
For (iii), the straight-line direction: by D7's "what it is, not how it was had" it is still a direction and so of the read's kind, but it is not had by any read here; D1–D7 do not say what to call a direction that has to be worked out from other knowledge. I would say: cannot be settled from D1–D7.

This case shows most clearly that D6 is a test of the reader's set of directions, not of the direction of a thing. A reader of the definitions could apply D6 here and conclude "the direction changed when the light was moved, so it is paint", and could equally conclude "the direction is a direction, so it is a read". Both follow from the wording.

------------------------------------------------------------
CASE 9. The Doppler shift of the light arriving from a moving source.

(a) D5: not settled by the definitions. D5 multiplies lengths. It says nothing about times, speeds, or the speed of light.
   - If times are left alone, a source's speed is multiplied by k. If the speed of light is a speed "in the world" and is multiplied by k too, the ratio of the two is unchanged and so is the shift. If the speed of light is not scaled, the shift moves under D5, and by D5's rule ("what moves is a write") a pure number would be called a write.
   - If times are scaled along with lengths, speeds are unchanged and the shift is unchanged.
   - The observed wavelength is a length in the world and is multiplied by k on any reading; the observed frequency in hertz depends again on what is done with times.
   ASSUMED for the classification below: the shift, as a ratio of observed to emitted frequency (or wavelength), is unchanged by D5.
(b) D6: the standpoint, the turn and the direction of the source stay. The observed frequency is what arrives and changes if the source is replaced by one emitting at another frequency or moving otherwise. The ratio of observed to emitted frequency does not change when the source is replaced by another emitting a different line at the same velocity; it changes when the source's motion is changed. So D6's "change what arrives" does not act on it in one way: it depends on which feature of what arrives is changed.
(c) Several things go by the name "Doppler shift":
   (i) the observed frequency or wavelength, as an amount in hertz or metres;
   (ii) the ratio of observed to emitted frequency, or z: a pure number. It needs the emitted (rest) frequency, which no single arrival carries; it is brought in from elsewhere (a known line);
   (iii) the velocity inferred from it, in metres per second.
(d) Needed: which of (i)–(iii) is meant; what D5 does to times and to the speed of light; whether an amount that is not a length (a frequency) can be a write under D4, which speaks only of "the across axis's zero tied to a unit" yet lists "a second" among its units; and whether a rest frequency known beforehand counts as "a unit carried in from outside the world".

Classification:
   (i) observed frequency or wavelength in a unit: WRITE, by D7's criterion ("being an amount in a unit is what makes it a write") and D4's mention of the second. Confidence: medium. The doubt is that D4 defines a write on the across (distance) axis, and a frequency is not on it.
   (ii) the shift as a ratio: NONE OF THESE, because it is a ratio of two payload amounts: not a direction (D6), not a gap across (D3), and on my assumption not moved by D5. Confidence: low, because D5's treatment of speeds is not given, and because one of the two amounts is carried in from outside, which D4 associates with writing.
   (iii) the velocity in metres per second: WRITE. Confidence: medium-high (an amount in units; moved by D5 if times are left alone).
   Taken as the single phrase "the Doppler shift" without choosing among these: CANNOT BE SETTLED FROM D1–D7, because D5 is stated for lengths only and the case is about frequency and motion.

One relation to D3 worth noting: D3 counts "a time to contact counted in the reader's own ticks" as a place, so the definitions do admit a time-like quantity as a place when it is counted in the reader's own unit. A Doppler ratio is not a time between two moments at the reader, and needs no second standpoint or second moment, so I did not class it as a place; but the definitions do not say why a time to contact is "a gap across", and a reader extending that example might reach a different answer here.

------------------------------------------------------------
CASE 10. A finite sensor's record (a grid of pixel values) of a continuous optical field.

(a) D5: the position on the grid at which a given feature falls is unchanged, if the sensor is scaled with the world or is treated as the reader's (directions do not change). The pixel values: not settled. If every length is multiplied by k, including the sensor's aperture and the sources' sizes, the light collected per pixel may change (by k² for an aperture's area, for instance) or not, depending on what is held fixed about the sources' brightness. D5 says nothing about amounts that are not lengths. The number of pixels does not change.
(b) D6: the grid (which pixel looks along which direction) stays; the values change. This is the cleanest part of the case.
(c) At least four things:
   (i) the grid: a finite, counted set of directions, one per pixel;
   (ii) the pixel values: amounts of what arrived, in the sensor's unit (counts, digital numbers);
   (iii) the record as a kept object: marks that persist after the moment;
   (iv) the relation of the record to the continuous field: a finite sample of something not finite.
(d) Needed: whether a counted, finite set of directions is still a read (D2 says the read is "given whole", "every sweep ... at once"; a grid is neither whole nor every sweep); whether paint recorded as an amount in a sensor's unit is a write (D7: "A count, or a mark kept, is how a write is recorded; being an amount in a unit is what makes it a write") even though it is not on the across axis (D4); whether the sensor's unit is "carried in from outside the world"; and whether an exposure of finite duration is "one moment" (D2).

Applying the definitions piece by piece:
   - (i) the grid's directions are of the read's kind, but as recorded they are a count of K cells laid out by the sensor's maker. D7 says a count is how a write is recorded. So the grid is a record, in counted form, of directions.
   - (ii) the pixel values are amounts in a unit, kept as marks. By D7's criterion they are writes. By D4's definition (the across axis's zero tied to a unit) they are not, since they are not distances. By D6 they are paint.
   - (iii) the record as a whole is a kept mark. D7 says a kept mark is how a write is recorded, but does not say every kept mark is a write.
   - (iv) nothing in D1–D7 speaks of finiteness, sampling or loss.

Classification: CANNOT BE SETTLED FROM D1–D7 as one thing, because the record is a composite: counted directions (a record of a read's directions) carrying amounts in a unit (paint written down). If forced to one word for the record as a kept object with values in a unit, I would say WRITE, on D7's sentence, with the reservation that D4's definition of a write is narrower than D7's criterion. Confidence: low.

------------------------------------------------------------
CLOSING QUESTIONS

(i) Could D6 be applied in each case using only what D1–D7 state?

No. It applied cleanly only in cases 5 and 6. Everything I had to assume:

1. Which part of an observation is "the directions" and which is "what arrives". D6 assumes the observation comes already divided. The definitions give examples of changing what arrives (repaint, move the light, replace a wall by trees) but no rule for dividing an arbitrary observation. I ASSUMED: the directions are the reader's own set of lines of sight at the standpoint, fixed by standpoint and turn alone; everything about which thing, colour, brightness or frequency is found along them is what arrives.

2. Whether "the direction to a thing" is a direction or a pairing (cases 1, 2, 8). Under D6's own example the thing can be replaced while the direction stays. So the direction of a named thing changes under some D6 changes (move the thing, bend its light) though no direction of the reader's has changed. I ASSUMED the phrase names the direction, not the pairing. Under the other assumption cases 1, 2 and 8 would come out as "a read together with its paint", for which there is no name.

3. Whether the positions of things are part of "what arrives" (case 3). "Replace a wall by a row of trees" changes distances as well as colours. D6 says only that directions and heat stay and paint changes; it does not say whether a place stays. I ASSUMED a place stays under repainting and relighting and may change when things are replaced or moved. This means D6 does not separate a place from paint in general; only D3's "gap across" does.

4. Whether a medium between source and reader is "what arrives" (case 8). I ASSUMED it is, since D6 lists "move the light".

5. What "heat" is (cases 4, 6). Undefined in D1–D7. I ASSUMED it is the density of the reader's directions per unit of reading, fixed by the turn.

6. What "the turn" is in D6 ("keeping the standpoint and the turn"). I ASSUMED it is the reader's sweep of its thumb about the standpoint, with its uniform measure. D2 speaks of "every sweep of the thumb"; "the turn" appears first in D6 without definition.

7. What the standpoint, turn and direction are in a case that names none (cases 4 and 7). D6 cannot be applied to a bare probability or a bare quotient of two normal quantities until someone says what observation they belong to. For case 7 I ASSUMED the two normals are amounts that arrive.

8. That a source's intrinsic properties and its motion are both "what arrives" (case 9). D6 then moves the Doppler ratio under some changes and not others, so "changes under D6" has no single answer there.

9. That the sensor's layout is on the side of "standpoint and turn" and its values on the side of "what arrives" (case 10).

D5 also needed assumptions, which I list because they bear on (a) throughout: the centre of the scaling; whether wavelengths are "lengths in the world" (case 5); what happens to times, speeds and the speed of light (case 9); what happens to amounts that are not lengths, such as brightness (cases 5, 10); and whether the reader's instruments other than thumb and stride are scaled (cases 5, 10).

(ii) Terms I found undefined or ambiguous, and their effect.

- "heat" (D2, D6): undefined. Affected cases 4 and 6: I could say the Cauchy of case 6 passes both tests, but calling it "the heat" was an inference.
- "paint" and "payload" (D2, D6): used as if the same; neither defined. "Payload" appears only in D6's last sentence. Affected cases 5, 7, 9, 10.
- "comes with" (D2): whether heat and paint are parts of the read or accompany it. Affected cases 4, 5, 6: if they are parts of the read, cases 5 and 6 are both "read" and the second test separates nothing among them; I took "accompany".
- "the turn" (D6) and "sweep of the thumb" (D2): not defined; their uniformity is not stated in D1–D7 at all, though case 6 and the notion of heat depend on it.
- "the direction" of a point (D1, D2): straight-line direction to where the point is, or direction of arrival of its light. Affected case 8.
- "a read" said of one direction, of a relation between two directions, of the whole, or of a distribution over directions. Affected cases 1, 2, 6.
- "gap across" (D3): defined by examples (d/H, d₁/d₂, V*/H, a time to contact in own ticks). The time example shows it is not only about distance, but no rule says which scale-invariant quantities are gaps across. Affected cases 4, 9.
- "amount" (D4, D6, D7): D4 defines a write as the across axis's zero tied to a unit, which is about distance; D7 says "being an amount in a unit is what makes it a write", which is wider; D4 itself lists "a second". Whether a frequency, a brightness or a pixel value in a unit is a write depends on which sentence governs. Affected cases 5, 9, 10.
- "a unit carried in from outside the world" (D4): whether a sensor's digital number, or a known rest frequency, is such a unit. Affected cases 9, 10.
- "every length in the world" (D5): wavelengths, instrument sizes, and by silence times and speeds. Affected cases 5, 9, 10.
- "one moment" (D2): whether an exposure qualifies. Affected case 10.
- "what it is, not how it was had" (D7): clear for a place handed over by another observer; unclear when two cases share a mathematical object and differ only in origin (cases 6 and 7), and for a direction that must be computed rather than seen (case 8, item iii).
- The scheme has three kinds and D6 acknowledges a fourth sort of thing (a probability, a ratio of payloads) without naming it. That is why cases 4, 5, 7 and part of 9 came out "none of these". I regard this as the main finding: the two tests together sort quantities into four boxes (moved by scaling; unmoved and a direction; unmoved and a gap across; unmoved and neither), and only three have names.
- A smaller inconsistency: D4's "a change of units ... moves every write's number and no place, no read" is not true of a read stated as an angle in degrees (case 2), nor of a place stated as "d in thumbs" if one changed which thumb; the sentence holds only for the reader's own forms.

(iii) The cases I was least sure of.

Case 9 (Doppler shift). D5 is stated for lengths and gives no rule for times, speeds or the speed of light, so I could not determine from the text whether the shift moves under the first test; the phrase covers three quantities of different kinds; and D6 moves the ratio under some changes of what arrives and not others. My "none of these" for the ratio rests on an assumption about D5 that the definitions do not supply.

Case 10 (the sensor's record). It is a composite of counted directions and recorded amounts, and D4 and D7 give different criteria for whether a recorded amount that is not a distance is a write. The definitions also say nothing about a finite record of something given whole, which is the feature the case seems chosen to test.

Close behind: case 7, where the answer depends wholly on what the two normal quantities are, and where D7's "not how it was had" sits awkwardly beside a pair of cases distinguished only by how the same law was obtained.

------------------------------------------------------------
SUMMARY TABLE

1. Direction to a visible point: READ (high)
2. Angular separation, one standpoint: READ, a relation within one read, the angle the writer's notation (medium)
3. Ratio of two distances by parallax: PLACE (high)
4. Dimensionless probability: NONE OF THESE; not a direction, not a gap across, not scale-variant (medium)
5. Ratio of two colour channels: NONE OF THESE; a ratio of payloads, paint (medium-high)
6. Cauchy from a uniform turn: READ, as the heat that comes with it (medium to medium-high)
7. Cauchy from a ratio of two normals: NONE OF THESE on the plain reading, a ratio of payloads; turns on what the normals are (medium-low)
8. Direction seen after refraction: READ as the direction of arrival (medium-high); the pairing with the source and the straight-line direction not settled
9. Doppler shift: observed frequency or wavelength in a unit WRITE (medium); the shift as a ratio NONE OF THESE (low); as one phrase, CANNOT BE SETTLED, since D5 covers lengths only
10. Finite sensor record: CANNOT BE SETTLED as one thing; counted directions carrying amounts in a unit; if forced, WRITE on D7's sentence (low)
