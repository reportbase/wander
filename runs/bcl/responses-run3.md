# BCL run 3: the third blind classifier's answers, verbatim

10 Nov 2026. A third fresh agent, told to read one file only, `runs/bcl/definitions-run3.txt` (D1–D7 and the passage
with both tables, as revised through R822; §12's O9 not included), and given the twelve cases. Its tool calls were one
read of that file and the hand-back of this report. The report is below, unedited.

---

BLIND CLASSIFICATION BY D1–D7 (only the definitions file was read; nothing else was opened)

Conventions used below. "Length scaling" is D5's geometric test (every length ×k, thumb and stride included, units outside). "Time scaling" and "brightness scaling" are D5's general test applied to that one dimension. "Repaint" is D6's change of what arrives with the standpoint and turn kept.

---------------------------------------------------------------
CASE 1. The direction from a standpoint to a visible point.

(a) D5, length scaling: nothing changes. The point goes from d·u to k·d·u; u is the same.
(b) D6: standpoint and turn held. The direction itself stays. What changes is what lies on it: D7 says "a read is a direction, not a pairing of a direction with a source: which thing paints a direction is part of what arrives". If "move the light" moves this particular point, then "the direction to that point" changes, while the direction as an element of the read does not.
(c) Two quantities are run together in the wording:
   1. the direction along which something is seen (direction of arrival, [h : v] or [h : v : v₂]);
   2. the pairing "this point is on that direction".
(d) Needed: whether the case means 1 or 2; and whether the light travelled straight (if not, see case 8).
Classification: quantity 1 is a READ (D2, first table row). Confidence high. Quantity 2 is "part of what arrives" (D7); the definitions give that no kind-name. It is not a ratio of payloads and not an amount in a unit, so for quantity 2: none of the supplied names. Confidence medium.

---------------------------------------------------------------
CASE 2. The angular separation of two visible points, seen from one standpoint.

(a) D5, length scaling: unchanged. Separately, a change of units (degree to radian) changes its number; D4 says explicitly that this is not scaling and that "an angle in degrees is the writer's coordinate on a read".
(b) D6: standpoint and turn held. The two directions stay, so the separation between those two directions stays. Which points paint them changes; if the points move, the separation "of those two points" changes (same split as case 1).
(c) A relation between two directions belonging to one read (D2: a read is "every sweep of the thumb at once … given whole", so both directions are in the same read). As a number in degrees or radians it is the writer's coordinate (D1, D4). The reader's version would be some trig-free function of the two [h : v]'s; the file does not say what that is, especially in space.
(d) Needed: a statement that a function of two directions within one read is itself a read. D2 says a read "is the direction", and the table row is "a direction [h : v]"; neither says a relation among directions is a read. Also needed: what "the turn" is. A separation is unchanged if the whole frame is turned, whereas a single [h : v] is not, so the two may behave differently under whatever "keeping the turn" excludes.
Classification: READ, more exactly the writer's coordinate on (part of) one read: unmoved by scaling, held by one standpoint, stays under D6. Not a write despite carrying a unit of angle (D4's explicit exception). Confidence medium. The definitions imply this rather than state it.

---------------------------------------------------------------
CASE 3. The ratio of two distances, obtained by parallax from two standpoints.

(a) D5, length scaling: unchanged (d₁/d₂; the step between standpoints scales too).
(b) D6: the second table puts a place in the column "stays when what arrives changes". That holds only if the things whose distances are taken stay where they are. D6's own examples ("move the light", "replace a wall by a row of trees") can move the thing at the end of a direction, and then d₁/d₂ along those directions changes. So I had to assume the repaint does not relocate the two things.
(c) d₁/d₂, a gap across. "Obtained by parallax" is how it was had; D7 says the kind does not depend on that.
(d) Nothing further for the name. For D6, a statement of whether the distance to "whatever is met along a direction" belongs to the geometry or to what arrives.
Classification: PLACE (named verbatim in D3 and the first table). Confidence high on the name, medium on whether D6 is actually satisfied as worded.

---------------------------------------------------------------
CASE 4. A dimensionless probability attached to an observation at one standpoint.

(a) D5: unmoved by any scaling (length, time, brightness). D6 says in so many words that this shows nothing: "a probability … is unmoved by scaling and is still not a direction".
(b) D6: cannot be run as given. A standpoint is named; no turn is named, and "attached to an observation" does not say whether the probability is of what arrives or of the directions. Two readings:
   - a probability of what arrives (e.g. that the paint on a direction is red): changes with repainting; the second table names it a ratio of payloads;
   - a probability over the directions themselves (the share of the turn falling in some set of directions): this looks like what D2 calls the read's "heat", which is "given" and stays under D6.
(c) Undetermined: either a payload probability or a measure on directions.
(d) Needed: what the probability is a probability of, the turn, and a definition of "heat" (the file uses the word without defining it).
Classification: cannot be settled from the definitions, because D6 "does not find a read in a bare number" and the case does not say which side the probability is on. If it is a probability of what arrives: RATIO OF PAYLOADS (table, verbatim). If it is the turn's own measure on directions: it is the heat that "comes with" a read; the file never says whether heat is itself a read or a fifth thing. In neither reading is it a read. Confidence: high that it is not a read or a write; medium that it is unsettled; my lean, if forced, is ratio of payloads because the table lists "a probability of what arrives" there.

---------------------------------------------------------------
CASE 5. The ratio of two colour channels of the light arriving along one direction.

(a) D5: brightness scaling (every brightness ×k) leaves it unchanged, since both channels scale. Length scaling leaves it unchanged. Time scaling: I assumed unchanged, which requires the sensor's channel bands to scale with the light's frequencies (the reader's instruments counted as in the world, as the thumb is for lengths). The file does not say so.
(b) D6: standpoint, turn and the direction held; repaint and the ratio changes.
(c) One number, a quotient of two payload amounts at one direction. The direction it sits on is a separate variable (a read).
(d) Nothing more.
Classification: RATIO OF PAYLOADS (named verbatim in the passage and the second table). Confidence high.

---------------------------------------------------------------
CASE 6. A Cauchy distribution obtained from a uniform turn about a standpoint (the slope of a uniformly turned direction).

(a) D5, length scaling: neither the slope s = v/h nor its law changes.
(b) D6: standpoint and turn are named, so the test can be run. Repainting changes neither the slope nor its law.
(c) Two things:
   1. the variable, the slope of a direction: D7 calls this out ("a Cauchy law on a direction's slope");
   2. the law (the distribution) on that variable.
   D7: "The kind attaches to the variable, not to its law."
(d) Needed for item 2: a definition of "heat". I assumed the law of the uniform turn on the slope is what D2/D6 call the heat that comes with the directions and stays under D6. Also note that "uniform" is uniform in θ, which D1 calls the writer's coordinate; the definitions do not say in what sense the reader has the uniformity.
Classification: the variable is a READ, confidence high. The distribution is, on my assumption, the read's heat: geometry's side, given, unmoved by either test; whether "heat" counts as a read or as an unnamed companion of it is not stated. Confidence medium.

---------------------------------------------------------------
CASE 7. A Cauchy distribution obtained as the ratio of two independent zero-mean normal quantities of equal spread.

(a) D5: the quotient is unmoved by the scaling of whatever dimension the two quantities share (they must share one for "equal spread" to mean anything). Unmoved by scaling shows only that it is not a write.
(b) D6: cannot be run. No standpoint and no turn are named; D6 says that in that case "nothing is concluded".
(c) The variable is a quotient of two amounts; the law is Cauchy. D7 says explicitly this is a different variable from case 6 with the same law, "and the law alone does not say which is which".
(d) Needed: what the two normal quantities are.
   - two payload amounts at one standpoint: ratio of payloads;
   - two distances: a place (though "zero-mean" implies signed quantities, and D3's distances are not signed, so this fits poorly);
   - the two components of a displacement from a named standpoint: the quotient would be a direction's slope, but then a standpoint and turn would have to be named, and the law would be a fact about how the things are scattered (what arrives), not about a turn.
Classification: cannot be settled from the definitions, because the variable's identity is not given and D6 cannot be run on a bare quotient. It is not a write, and it is not shown to be a read. Most natural reading: RATIO OF PAYLOADS (a "ratio of two amounts", D6's own phrase). Confidence high that it is unsettled as stated and that it must not be classed with case 6; low on any specific name.

---------------------------------------------------------------
CASE 8. The direction in which a source is seen when its light has been bent by refraction on the way.

(a) D5, length scaling: unchanged, assuming the bending medium's shape scales with everything else and its refractive index (dimensionless) is untouched.
(b) D6 addresses this directly: "The direction it keeps is the direction of arrival at the standpoint: light bent on the way, by a lens or by refraction, changes which source paints a direction and moves no direction, and where that source lies is a further inference, the writer's." So: the directions stay; which source paints which direction changes (putting in or taking out the refracting medium is a change of what arrives).
(c) Three quantities:
   1. the direction of arrival (the apparent direction);
   2. the pairing "this source is seen along that direction";
   3. the direction in which the source actually lies.
(d) Nothing more for 1. For 2 and 3 the definitions say what they are not, and whose they are, but supply no kind-name.
Classification: 1 is a READ, confidence high (D6 is explicit). 2 is part of what arrives (D7), changes under D6; none of the supplied names fits (not a ratio, not an amount in a unit). 3 is "a further inference, the writer's": it is unmoved by length scaling and is a direction, yet no read at the standpoint holds it; the definitions do not name its kind. Note that the case's wording, "the direction in which a source is seen", literally names quantity 2 (a direction tied to a source), and under that literal reading the quantity does change under D6. Confidence on 2 and 3 being unnamed: medium.

---------------------------------------------------------------
CASE 9. The Doppler shift of the light arriving from a moving source.

(a) D5: time scaling moves the received frequency in hertz and the difference Δf in hertz; it does not move f/f_rest (D5 says exactly this). Length scaling: D5 says "nothing here makes times follow lengths", so frequencies do not move; but if the shift is quoted as a wavelength in metres it does move under length scaling. Whether the ratio survives length-only scaling physically depends on whether the speed of light, a constant of compound dimension, is scaled; D5 says "the world's constants of that dimension included" and does not say what to do with a constant of mixed dimension. I assumed the ratio is unmoved.
(b) D6: standpoint (including its state of motion, per D6) and turn held; change the source or its motion ("move the light") and the shift changes. So it is on the payload side. The direction it arrives along stays.
(c) Several variables:
   1. received frequency in hertz;
   2. the shift as a difference, Δf in hertz (or Δλ in metres);
   3. the shift as a ratio, f/f_rest (or z).
(d) Needed: which of 1–3 is meant; and where the rest frequency comes from. It does not arrive with the light; it is a reference held by the observer or taken from another source. The table nonetheless lists "a frequency over a rest frequency" as a ratio of payloads.
Classification: 1 and 2 are WRITES (payload column: "a frequency in hertz"), confidence high. 3 is a RATIO OF PAYLOADS (table, verbatim), confidence medium-high; the reservation is that one term of the ratio is not something that arrives. D6's remark that the test "sorts quantities, not causes" applies: the source's motion may also move where it appears, which is a separate variable.

---------------------------------------------------------------
CASE 10. A finite sensor's record (a grid of pixel values) of a continuous optical field.

(a) D5: brightness scaling moves each pixel value (in the sensor's unit) and no ratio between pixels and no grid index. Length scaling moves none of them, assuming the sensor scales with the world.
(b) D6: standpoint and turn (the sensor's pointing) held; repaint and the pixel values and their ratios change; the grid positions, and the directions they stand for, do not.
(c) The closing paragraph of the passage separates them, and I follow it:
   1. a pixel's value in the sensor's unit;
   2. a pixel's ratio to its neighbour;
   3. a pixel's position in the grid;
   and I add 4. the record as a whole, as a kept object.
(d) Needed: a kind-name for item 3. The passage calls it "a writer's count of directions". D7 says "a count, or a mark kept, is how a write is recorded; being an amount in a unit is what makes it a write". A grid index is a count, is not obviously an amount in a unit carried in from outside, and is unmoved by scaling. I read it as a writer's coordinate on a read, like D4's angle in degrees, but the file does not say that. Also unclear: whether the sensor's unit counts as "carried in from outside the world" (D4) when the sensor is inside the world.
Classification: 1 is a WRITE (payload's), 2 is a RATIO OF PAYLOADS, both verbatim, confidence high. 3: the writer's coordinate/count on a read; not a read as the reader holds it, not a write by D5; none of the four names cleanly; confidence medium. 4: the record as a whole is not one variable; "a mark kept" is how writes are recorded (D7), so it is a recording of payload writes indexed by a writer's count of directions. No single name applies; confidence medium.

---------------------------------------------------------------
CASE 11. The ratio of the brightness of two sources seen along two different directions from one standpoint.

(a) D5: brightness scaling leaves it unchanged. Length scaling leaves it unchanged (even if received brightness depended on distance, both would change alike).
(b) D6: standpoint, turn and the two directions held; repaint (dim one source, swap one) and the ratio changes.
(c) A quotient of two payload amounts, taken across two directions. The two directions are separate variables (reads); which source is on which is a pairing (what arrives).
(d) Nothing more for the name. The table's first example is within one direction (colour channels), but the passage's "its ratio to its neighbour" for pixels is across directions, so cross-direction ratios are covered.
Classification: RATIO OF PAYLOADS. Confidence high. One caution the definitions leave untreated: if a writer knows the two sources are of one kind, the same number yields a ratio of distances (a place) by inference. By D7 ("the kind attaches to the variable"; "what it is, not how it was had") the brightness ratio stays a ratio of payloads and the inferred d₁/d₂ is a different variable, a place. The definitions do not discuss a single number serving as both.

---------------------------------------------------------------
CASE 12. The change in the received frequency of a source's light when the observer is boosted to a stated speed toward it, the source's own emission unchanged.

(a) D5: time scaling moves Δf in hertz, and does not move the factor f′/f. The "stated speed": in metres per second it moves under length scaling or under time scaling; as a fraction of the speed of light it moves under neither only if the world's constant is scaled along with it, which D5 says for constants "of that dimension" without covering a constant of mixed dimension.
(b) D6: here D6 cannot be applied to the change the case describes. D6 holds the standpoint fixed and says "a boost is a change of standpoint, so it is not among the changes of what arrives, and it moves the read". The case's change is exactly a change of standpoint with what arrives (the emission) held fixed, the reverse of D6's set-up. What D6 can be asked is: at the two standpoints, with the boost fixed, change what arrives (a different emitted frequency). Then Δf in hertz changes, but the factor f′/f does not (it depends on the boost and the direction, not on what was emitted). So the factor stays when what arrives changes, which puts it in the table's geometry column; yet it is neither a direction nor a gap across.
(c) Three variables:
   1. Δf = f′ − f in hertz;
   2. the factor f′/f;
   3. the stated speed (in a unit, or as a fraction of light's speed).
(d) Needed: the ruling D6 itself marks as missing: "How a relation between two standpoints is to be classed when it is not a distance is open (§12, O9)." Items 2 and 3 are such relations.
Classification:
   1. Δf in hertz: a WRITE (payload's write: an amount in hertz, moved by time scaling). Confidence high.
   2. f′/f: cannot be settled from the definitions. It is unmoved by scaling; it is a ratio of two payload amounts in form (the table would then say "ratio of payloads"), but it does not change with what arrives, which is the table's defining test for that column; it is a relation between two standpoints that is not a distance, which D6 declares open. Confidence medium-high that it is unsettled.
   3. The speed in metres per second: a WRITE. As a dimensionless fraction: a relation between two standpoints (states of motion), open by the same sentence. Confidence medium.
   Also: D6 says the boost "moves the read". For a source dead ahead its own direction would not move, though the rest of the read would; the definitions speak of the read as a whole and do not address this.

---------------------------------------------------------------
CLOSING QUESTIONS

(i) Could D5 and D6 be applied using only what the file states? Not fully. Every assumption I made:

1. "Heat" is never defined. I assumed it is the turn's own weight/density over directions (used in cases 4 and 6).
2. "The turn" is never defined. I assumed it is the orientation or sweep about the standpoint that fixes which directions are which. This matters for case 2 (a separation does not depend on the frame; a single [h : v] does) and for cases 4 and 7 (D6 cannot run without it).
3. "Paint", "payload" and "what arrives" I treated as one thing. The file uses all three and never equates them.
4. Which part is "the directions" and which "what arrives":
   - I took the identity of the point or source on a direction as what arrives (D7 says so), which makes the literal wording of cases 1, 2 and 8 ("direction to a point", "direction in which a source is seen") mixed quantities.
   - I took the refracting medium as part of what arrives (D6 implies it by listing a lens with repainting).
   - For places (case 3) I had to assume the things whose distances are taken do not move when the world is "repainted". D6's examples ("move the light", "replace a wall by a row of trees") do move or replace things, so whether "the distance to what is met along this direction" is geometry or payload is not settled by the text. The second table simply asserts a place "stays when what arrives changes".
   - For case 9 I took the source's motion as part of what arrives and the observer's motion as part of the standpoint (the latter stated in D6, the former not).
5. For payload scalings I assumed the observer's instruments (channel bands, sensor) are inside the world and scale with it, by analogy with "the reader's thumb and stride included". The file states this only for lengths.
6. I assumed brightness scaling and time scaling are independent of length scaling ("nothing here makes times follow lengths" covers times; nothing is said about brightness).
7. Constants of compound dimension (the speed of light): D5 says constants "of that dimension" are scaled; I assumed dimensionless ratios such as v/c and the Doppler factor are unmoved, which the file does not establish (cases 9 and 12).
8. The rest frequency (case 9): I accepted the table's listing although the rest frequency does not arrive along the direction.
9. Case 2: I assumed a function of two directions inside one read is itself of the read's kind.
10. Case 10: I assumed the sensor's unit counts as a unit "carried in from outside the world", though the sensor is in the world.
11. Case 12: D6 could not be run on the stated change at all; I substituted a different question (vary the emission at fixed boost).

(ii) Undefined or ambiguous terms, and internal disagreements.

Undefined or ambiguous: heat; turn; paint; payload (never defined, only exemplified); "what arrives"; sweep; home; "up" and "across"; party and "true breadth" V*; reader and writer (used as known roles); "the step"; the reader's "ticks"; "orders" (D7: "places and orders"); "hung from the same thumb"; "the world" against "outside the world"; "the world's constants of that dimension"; "amount"; "the geometry's quantities" (D5 uses this to restrict its conclusion, but which quantities are geometric is only decided by D6, so D5's sentence "among the geometry's quantities, what stays is a read or a place" presupposes the later test); "place" used in two senses (D3's gap across, and "the pixel's place in the grid").

Disagreements or tensions:
1. D2 says a read "comes with its heat, given, and the paint met along it"; D6 says the paint changes while the read stays; D7 says which thing paints a direction is part of what arrives. Whether the paint is part of a read or merely accompanies it is not consistent.
2. D5 says "what moves is a write"; D4 and D7 say being "an amount in a unit" is what makes a write. An angle in degrees is an amount in a unit and does not move; D4 patches this by exception (writer's coordinate on a read). A count (pixel index, count of directions) is called by D7 "how a write is recorded", yet such a count is unmoved by scaling and the passage attaches it to directions. The two criteria (moved by scaling; amount in a unit) are not shown to coincide.
3. D3 defines a place as "a gap across: a distance", then lists "a time to contact counted in the reader's own ticks" as a place, and D7 says joining two moments gives places. D6's last sentence says a relation between two standpoints that is not a distance is unclassified. A time to contact is a relation across moments that is not a distance and has been classed; a boost factor or a relative speed is left open. The boundary is not stated.
4. The second table defines the payload column as "changes with what arrives". Under a boost the colour of what arrives changes while what arrives (the emission) is unchanged, and D6 files the boost under standpoint. So a payload quantity changes without a change of what arrives, and a ratio such as f′/f does not change with what arrives though formed from payloads. The column headings do not cover standpoint changes.
5. D2 fixes a read to one standpoint "at one moment"; D6 extends the standpoint to include its state of motion. A state of motion is not given by one moment at one position, so what a read needs in order to be named has grown between D2 and D6.
6. The first table gives "held by one standpoint? no" for a write, while the payload's writes (a frequency in hertz, a pixel value) are held at one standpoint. The text says the first table is only for geometric quantities, so this is a scope limit rather than a contradiction, but the word "write" then carries two different rows of properties.
7. D4 says a write's unit is "carried in from outside the world"; D5 scales "the world's constants". A rest frequency or a standard candle's brightness is a world constant used as a reference; a ratio to it is called a ratio of payloads, though only one term arrives.
8. The second table asserts that a place stays when what arrives changes, while D6's examples of changing what arrives include moving and replacing the things that distances run to.

(iii) Least sure.

Case 12 is the one I am least sure of. The stated change is a change of standpoint, which D6 excludes from its own test, so D6 cannot be run on it; the factor f′/f passes D5 as a ratio, behaves under D6 like geometry (indifferent to what was emitted), is built from payload amounts, and is neither a direction nor a distance. D6's own final sentence says this class is open, so "cannot be settled" is what the definitions themselves say, but I am not certain the author would not simply call it a ratio of payloads from the table's "a frequency over a rest frequency".

Case 4 is second. "A probability" appears in the table only as "a probability of what arrives", while the heat that comes with a read is also, on any reading I can give the word, a dimensionless weight on directions. Without a definition of heat and without knowing what the probability is of, the two cannot be told apart, and they fall on opposite sides of D6.

(Case 2 is a runner-up: the definitions never say that a relation between two directions of one read is a read; I inferred it from D2's "given whole" and D4's remark about degrees.)
