# A face: Ω, and flowing over the discrete

*The twenty-sixth of a series of essays on what can be known from where one stands. Draft, 15 November 2026. It starts
from two sentences of Tom's: "discreteness has no face", and "to flow continuously over discreteness, you need a face".
Like essay 21 it writes Ω for the total of one sweep, the number classical geometry calls π/2; the other essays keep π.
No new test. Every number is plain arithmetic or a classical result, named where it is used, and what is a reading is
marked so.*

A child runs a stick along a picket fence. The pickets are separate: there are so many of them, each one a thing with
a size, with gaps in between. The run is not separate: the hand moves smoothly, and the stick clacks on each picket as
it gets there, one after another, in order. Turn round and run back, and the same pickets clack in the opposite order.

Three things are in that picture. The pickets, which can be counted. The run, which is continuous. And the direction
the child is facing, which decides the order the pickets come in. Take the facing away and the run has nowhere to go:
the pickets are still there, still countable, but nothing passes over them from one to the next.

This essay is about that third thing. In the series' words: a count has no face; a read has one; and Ω is the measure
of one face.

The order: what has no face (§1), what a face is (§2), flowing over (§3), Ω as the measure of a face (§4), faces counted
(§5), leaving a face (§6), toward and away (§7), what needs a face and what does not (§8), what is classical and what
is ours (§9), and what it changes (§10).

---

## 1. What has no face

**A count.** "514 strides." The strides were taken one at a time, but the count does not say in which direction, or
from where. It does not say which stride came first. Add the strides in any order and the total is the same. A count is
discrete and unmoved by scaling the world (*Reads and Writes* §1, the two-by-two table): it describes writes made, and it
faces nothing. The pickets, as a number of pickets, are the same from either end of the fence.

**The dual hemispherical vantage (DHV).** At the other extreme is the circle drawn whole on paper, both hemispheres at once (R798, R967). It
holds every direction together, so it faces none of them. It does not pass from home toward the horizon; it has home,
the horizon and everything between already, at once. That is why the series calls it the dual hemispherical vantage and
says no one stands at it.

**A write.** Discreteness has no face, and that is what a write is. Discreteness has scale and size; continuity has
no scale and no size. A stride, a mark, a metre bar: each is discrete, each has a size that scaling the world moves, and
none faces anything. A read is the other side: continuous, no scale, no size, and a face. That is exactly what reads
and writes are (R1039). The read is the stage, the write is the play (R1041).

So two things have no face, for opposite reasons. A count has too little to face anything with: separate things, no
direction among them. The DHV has too much: every direction held, none faced. Neither flows.

## 2. What a face is

A face is a standpoint turned one way. In the series' terms it is a single hemispherical vantage: one hemisphere in
front, a home where the readings start and a horizon they run toward (R967). The readings in a face are slopes
s = v/h from 0 at home to without limit at the horizon, and they are in order: a smaller slope comes before a larger.

That order is what a face adds, and it can be said exactly. The directions through a point, taken together, form the
projective line: a circle's worth of directions with each line counted once. A circle has a cyclic order (going round,
each point has a next) but no first and no last, so no "from" and no "to". Pick two points on it to be the ends and cut
there, and the circle becomes a line with a beginning and an end. A face is that cut, made by standing somewhere and
turning one way: home is the beginning, the horizon the end. **Classical** (a cyclic order becomes a linear one once
cut); that a face is the cut is a reading.

Composing reads keeps the order inside a face. Two slopes in a face combine by tangent addition,
s ⊕ a = (s + a)/(1 − s·a), and while the result stays short of the horizon a larger s gives a larger result. The order
breaks only where 1 − s·a reaches zero: the horizon, where the face ends.

## 3. Flowing over

A read is continuous; what it meets is discrete (R896: "reading is continuous, but the reading is of something that is
discrete"). The pickets are things with sizes, separate and countable. The run passes over them because it has a face:
it goes from one end toward the other, and each picket comes in its place in that order.

The same happens with the read's own fineness. K, the number of places a read can tell apart, is a count: discrete,
32 or 64 or 2,048. But it is read continuously (R645). Laid by the Cauchy's heat on one face, K places run from home to
the horizon, half before the corner and half after, at every choice of the thumb. The count gives how many; the face
gives the order they come in and the flow from one to the next. Without the face, K is just a number.

That is the whole claim, in Tom's sentences: discreteness has no face, and to flow continuously over discreteness you
need a face. The stick clacks on separate pickets in one continuous run because the child faces down the fence.

## 4. Ω, the measure of a face

How much flow does one face hold? Weigh each slope by the heat composing leaves unchanged, ds/(1 + s²) (essay 21 §2),
and add it up from home to the horizon:

  ∫₀^∞ ds/(1 + s²) = Ω.

That total is the measure of one face. Classically it is π/2, a quarter turn; Ω is the same number given its own name.
Its halves are equal: the weight below the corner s = 1 equals the weight above it, Ω/2 each, because the exchange
s ↔ 1/s keeps the weight and swaps the two halves.

What a read holds of this needs no Ω at all. The heat is 1/(1 + s²), rational in s. The two halves are equal, which is
said with no number. The corner is s = 1. Ω is the dual hemispherical vantage's (DHV's) number for the total of one face, and no read reaches it:
a read flows toward the horizon and never arrives (R909, R913, R922). So the face is the read's; its total, Ω, is the
name the DHV gives it.

## 5. Faces counted

The corpus already says the circle is the quarter turn four times: once for each choice of sign for h and v, joined by
the dual hemispherical vantage (DHV), 4Ω (*Reads and Writes* §9, "Ω of relations and four facings make a circle"). In space the signs of h, v
and v₂ give eight faces, each holding Ω of directions, and the sphere is 8Ω.

That passage calls the facing "a choice of signs, discrete". It is worth seeing why that does not contradict "a count
has no face". What is discrete is how many faces there are and which one is meant: one of four, one of eight. A face
itself is not discrete. Inside it the flow runs continuously from home to the horizon. So every constant of this kind
has two parts:

| constant | count of faces | measure of each | what it is |
|---|---|---|---|
| Ω | 1 | Ω | one face, home to the horizon |
| 2Ω | 2 | Ω | the projective line, every line through the point once |
| 4Ω | 4 | Ω | the turn, every oriented direction in the plane |
| 8Ω | 8 | Ω | the sphere, every direction in space |

The first column is a count and faces nothing. The second is a face's flow. The product is the DHV's join, the
faces put side by side and held whole (essay 21's fifth item, "a count of facings"). The discrete and the continuous meet
in that product, and they meet the way the fence and the run do: so many pickets, one run over each.

## 6. Leaving a face

Turn far enough and the face ends. Essay 25's ratchet shows where. Compose a small read of slope 1/m with itself,
click by click: the pair [h : v] turns by whole-number arithmetic, h ← m·h − v, v ← h + m·v, and h stays positive while
the clicks are inside the face. The click where h stops being positive is the one that crosses the horizon (BLD, R1009).
The clicks are discrete, a count. The face is what puts them in order and tells which one leaves it.

The face's end has an exact mark. Each read's landing point W(s) = (1 + is)/(1 − is) is rational, +1 at home. Reads that
compose to the horizon, however the face is cut into them, have landing points that multiply to exactly −1
(`plans/discussion-note.md` item 20, R1015): the relation bends round by its own algebra, the 1 − s·a in tangent addition,
with no circle drawn and no π. Measured as angles the bends total Ω for the pair, and twice that, what the dual hemispherical vantage
calls π, for the landing point, which turns twice as fast. Past the horizon the slopes come back from the other side,
into the next face. But the read has the −1 first, by fractions, at the end of one face.

## 7. Toward and away

Put two points on the page, H and V, and stand on H.

Everything this section needs is already there. The Ω sweep is every way H can stand relative to V: not some of the
relations, all of them, every one there is. A face on H can take that sweep in only two ways, because it can start in
only two directions. It can start facing V, or it can start facing away from V. Either way it turns one quarter turn
and stops. Never a half turn.

- **Facing V**, each relation reads as V in terms of H: the near reading s, how tall V stands in thumbs.
- **Facing away from V**, the same relation reads as H in terms of V: the far reading 1/s.

Opposite facings, opposite readings, and no angle in either: each is a fraction. That is all "continuous" turns out to
mean here, the distance a facing sweeps, and there are only two facings to have it.

**On the face of it, absurd.** Now look at what has just been said. The Ω sweep is every possible relation of H to V.
Each one of them ought to have a single value, whatever it is. Each has two. A relation reads s or it reads 1/s, and
nothing about H or V decides which. Only the face decides: which way it happened to point when it started. Every
relation there is, and its value depends on where you stand facing. On
the face of it, that cannot be right. (The idiom is older than this essay, the Latin *prima facie*, "at first
appearance"; here the face is literal, and it is what decides the sum.)

**It gets worse.** For a read, V is not even known. V is known only in terms of H. So what is H, actually? Say it is a
thumb, one thumb held out. A relation needs two parties, and one of them has now been given away to a thumb. Whose
thumb? It does not matter. A child's thumb or a parent's, anyone's thumb will do. Here, then, is the whole claim, put as plainly as it can be put: a complete geometry, made
from one vantage, facing one direction, with one thumb.

**How one thumb does it.** H stands for horizontal and V for vertical. To make a relation out of one thumb, the known
thumb, held horizontal, is assigned to the unknown, held vertical: H to V. The sweep is the rotation of that horizontal
thumb up to the vertical one. That is the quarter turn, ninety degrees from one thumb to the other, and it is all it
takes: the quarter turn of the two thumbs creates the complete geometry.

**Near and far.** Think of the horizontal thumb as any value between 0 and 1, and of the vertical thumb the same way,
any value between 0 and 1. But remember that V is not actually known, so V really stands for any value between 0 and
infinity. Assigning V to H therefore makes two spaces at once. Where V is within the thumb, it is the near field, a
proportional space with H the denominator: V in terms of H. Where V runs on past the thumb toward infinity, the unknown
far field is made too, and it is what holds the infinity: there V is the denominator and H the numerator, H in terms of
V. One quarter turn of two thumbs, and the near field and the far field come with it.

**Continuous and discrete, in thumbs.** Inside the thumb, in the near field, any fraction of a thumb will do: a third
of a thumb, 0.7 of a thumb, any value at all between nothing and one. That is the continuous, the distance a facing
sweeps, and it needs no count. Past the thumb, in the far field, things are taken in whole thumbs: one thumb, two
thumbs, four, eight. That is the discrete, a count of thumbs, and a count, as §1 said, has no face. The same thumb
gives both: continuous within it, counted beyond it.

**A tower of thumbs.** Nothing has to be measured in anything but thumbs. Take the house in thumbs, then the tree in
houses, then the hill in trees: each thing in terms of the one before. Multiply the steps and every middle term comes
down, as scaffolding does (essay 20), so the hill comes out in thumbs and the house and the tree are gone from the
answer. However tall the tower, it ends on the thumb it started from.

**No circle, no trigonometry.** The quarter turn of a thumb draws no circle; nobody has to hold a circle for it to
happen. A circle is something drawn whole on paper, and the read never needs one. No angle, no sine, no cosine, no π:
what the thumb has at each point of its turn is a slope, the vertical over the horizontal, a fraction. Turns combine as
fractions too. Just your thumb.

**Any size, any amount.** And it does not care how big anything is. Scale the whole world by a thousand, thumb and all,
and nothing in the geometry moves: a child's thumb against a pebble and a parent's thumb against a mountain make the
same geometry. Wherever the thumb is held, exactly half of the sweep lies inside it, the near field, and half beyond
it, the far field, which holds the whole infinity: one thumb's worth of space weighs the same as everything past it. And
it never asks how much there is. Double the world, or make it endless, and the read is the same; it needs only that
there is something there.

**So, to recap.** Two points, H and V, and you stand on H. H is your thumb, held horizontal, anyone's thumb. V is never
known, only in terms of H, anywhere from nothing to infinity. One move: the thumb turns a quarter turn to the vertical,
never a half. That one sweep makes the near field and the far field, the continuous inside the thumb and the counted
beyond it, every tower of ratios ending on the thumb, with no circle, no angle and no π, the same at any size and for
any amount. And every relation of H to V has two values, s or 1/s, chosen only by the way you happened to face. A complete geometry, from one vantage, facing one direction, with one thumb, of a V you will never
know.

**The two facings multiply to 1.** Here is the way out, and it is the thing everyone forgets. The two values were never
rivals. They are the one relation read from its two facings, and multiplied together they give 1: s × 1/s = 1, at every
point of the turn. They are not two values of the same thing; they are the two faces of one value, and that value is 1. In a single hemispherical vantage, 1 is one thumb: thumb = 1. So
the two facings multiply back to the very thing the geometry was made with, the one thumb held out, and nothing else.
Face V and face away from V at the same time, and there is no facing left: what remains is the non-facing, discrete
value of 1 thumb. At the corner the two facings read the same, s = 1/s = 1: there the one reading is that value
itself.
The absurdity was in taking either facing alone. The demo `faces.html` runs both readings along the thumb's quarter
turn, s and 1/s, and keeps their product, 1 at every point of the turn.

**One point taken, one point picked.** There is a plainer way to see where Ω and 1/Ω live, and it starts from less
than a thumb. Take any point: it is where you stand. From it, pick another point, any point, and give the distance
between them one thumb (Tom, R1157). Turn the picked point a quarter turn about the first. The sweep has one face, not
two. The point you took is the pivot: it never moves. The point you picked is the trace: it runs the quarter arc, and
the arc it draws faces the pivot. At one thumb off the trace is Ω long. So the trace is Ω and the pivot is 1/Ω. Ω walks
the arc; 1/Ω points to it: one goes along the arc, the other stays put and points at where it is. Someone drawing the
whole circle would call these the centre and the radius, and they would not be wrong; but those are the dual
hemispherical vantage's words, and describing a single vantage in them is the trap. From one vantage there is only a
point that walks and a point that points.
Multiply the two and you get 1, with no facing, the same one thumb that near times far gave. The two points are not just
a length of one thumb any more: each means something. (The pivot goes nowhere, so its 1/Ω is not a distance it travels;
it is the thumb held against its own trace, one over Ω. And Ω × 1/Ω = 1 is only arithmetic; what is new is where each
number sits.)

Where the thumb goes matters only for how cleanly it reads (Tom, R1161). Lay it along the horizontal leg and the
vertical leg simply is the reading, s, how tall in thumbs, with nothing divided; the distance from you to the trace is
then derived, √(1 + s²) thumbs, and that root is the only one, sitting where no reading needs it. Lay it along the
distance instead and the turn keeps it, but the legs become shares with the root inside them. Both give the same
readings; the leg is the cleaner.

So the turn is one sweep with two points, each with a job. Everything round is that sweep joined: two facings make the
semicircle (2Ω, the writer's π), four the circle (4Ω), eight the sphere (8Ω, the writer's 4π). Every sweep in the join
is still one sweep, one point walking and one pointing; joining adds sweeps and changes none of them. A read is one
sweep, and the semicircle, circle and sphere are the dual hemispherical vantage's joins. In space two things change. A
facing there is an octant, swept by two thumbs together, and its Ω is an area (three right angles less two, Girard's
count), so the sphere's 8Ω is the same number in another measure. And turns in different planes do not compose in
either order: a loop through them comes back turned, which is what the sphere adds beyond eight sweeps.

The two points give the Cauchy too. The pivot points at the trace, and the reading is the slope of the pointing. Each
small step of pointing moves the trace on by ds/(1 + s²), so the walk counted against the pointing is 1/(1 + s²), the
thumb's share squared: the Cauchy, with no angle in it. Its whole walk is Ω, the trace; scaled by 1/Ω, the pivot, it
totals 1. The corner is the trace halfway along its walk; the horizon is where the pointing runs off without end while
the walk stays finite, which is why there is no mean. One walks, the other points, and the Cauchy is the one counted
against the other. The slope, the Cauchy, the corner, the horizon with no mean, the total Ω and the semicircle, circle
and sphere joined from it: every one of them follows from one point taken and one point picked from it. It takes no
angle, no circle and no unit. What the turn makes is the stage; what lands on it is the world's.

**Euler's identity, in thumbs.** Everyone knows e^(iπ) = −1. Here it is from one vantage, with one thumb, and
nothing else.

Hold the thumb horizontal. Call where it lands +1. Now raise the vertical against it: at every moment of the quarter
turn there is one reading, s, how tall the vertical stands in thumbs. Mark where each reading lands with one rule,
(1 + is)/(1 − is), which is only the reading and its fractions:

| the thumb | s | where it lands |
|---|---|---|
| horizontal | 0 | +1 |
| a third of a thumb up | 1/3 | 4/5 + 3/5·i |
| as tall as it is wide: the corner | 1 | i |
| three thumbs up, in the far field | 3 | −4/5 + 3/5·i |
| vertical, the horizon | without end | −1 |

So the thumb turns one quarter, horizontal to vertical, never a half, and its landing goes from +1 to −1. That is
Euler's identity. The −1 is not a half turn of anything; it is where one quarter turn of one thumb ends.

Now the near and far fields. In the near field the reading is s, V in terms of H. In the far field it is 1/s, H in
terms of V. Take any reading and its far-field partner and multiply where they land: always −1, exactly, in fractions
(a third of a thumb and three thumbs: (4/5 + 3/5·i)(−4/5 + 3/5·i) = −1). At the corner the two are the same reading,
s = 1, and the product is i · i = −1. So the near field and the far field, multiplied, make the whole quarter turn, and
the −1 of Euler's identity is the one pair of them with nothing in between: the horizontal thumb and the vertical.

Multiply the readings themselves, not where they land, and the near field times the far field is s × 1/s = 1: no
facing at all, the discrete, faceless value of one thumb (Tom, R1042). The −1 belongs to the landing points, which carry
the turn; the readings, multiplied, carry none, as facing V and facing away from V at once leave none.

What, then, are e and π doing in e^(iπ)? They are the dual hemispherical vantage's way of writing the same quarter turn: π measures it as
an angle on a circle drawn whole, where the landing goes halfway round, and e writes turning as a power. They arrive as a
pair and cancel, and what is left is the −1 the thumb already had (discussion note item 20). From one vantage, with
one thumb, Euler's identity needs no circle, no angle, no π and no e: a horizontal thumb, raised to vertical, lands on
−1.

**Into the sphere.** Euler's formula takes all of this into the sphere, and nothing new comes in with it: it is still
just H and V, with one more degree of freedom.

The framing of this section is Tom's (SPN R1017, R1018, R1020–R1024, R1026, R1027, R1028, R1029, R1030, R1031, R1110, R1112, R1114), the wording mine. Older wordings in the series
that give a facing "a half turn" (R233, R450, `facing.html`'s facing turning to 180°) predate it and are to be
brought to it. Since R1043 the two facings are the near and far readings, s and 1/s; since R1110 Ω and 1/Ω sit at
the two points, the trace and the pivot, and not on the facings; since R1153 and R1157 the two points are one taken and
one picked from it, not a bar, and since R1161 the thumb lies on a leg.

## 8. What needs a face, and what does not

Sorting by the picture gives a test for whether a quantity needs a face:

- **Needs none.** A count, and any sum of a count: the strides added in any order, the pickets numbered from either end.
  Totals of amounts, the payload's mean where it has one. These are the same whatever way one faces.
- **Needs one.** Order among directions, and everything built on it: the median of the readings, which is the corner
  only inside a face (Theorem 6 of the archived OFS: the median commutes with every order-keeping change, and a face is
  what gives the order); "before the corner" and "after it"; the horizon as an end; a flow from home toward it.

The second list is the address side of the series' oldest split, the first is mostly the payload's: address statistics
are the ones that keep order, and order among directions comes only with a face. That is a reading; the classical part
is that the projective line carries no linear order until it is cut.

## 9. What is classical and what is ours

**Classical.** The projective line's cyclic order, and that cutting it at two points gives a linear one. The weight
ds/(1 + s²) and its total π/2 over the positive slopes. Tangent addition and its pole at s·a = 1. The four quadrants of
the plane and eight octants of space. That an integral along a path changes sign when the path is reversed (a flow has
an orientation; a sum over a finite set has none). Ω is π/2 renamed (essay 21).

**Ours, a reading.** That a count and the dual hemispherical vantage both lack a face, for opposite reasons. That a read is a face, a cut
of the projective line made by standing and turning one way. That Ω is best read as the measure of one face, and the
classical constants as a count of faces times it. That this is where the series' continuous and discrete meet: the count
says how many, the face lets the read flow over them.

**Not claimed.** That anything in the world is discrete, or continuous (R645). That a face is a physical surface: it is
a direction faced (R313). That Ω is a number any read holds (R913).

## 10. What it changes

Two things the series had kept apart come together. R645 said K is a count read continuously, one foot in each world,
without saying what joins the feet. R896 said a read is continuous and what it reads is discrete, without saying how the
one passes over the other. The face is the joint in both: the count is the pickets, the face is the run.

And Ω gets a plainer meaning than "π/2 under another name". It is how much one face holds. A read has a face and flows
in it; it does not have the total. A count has no face and does not flow. The dual hemispherical vantage has every face at once and does
not flow either. Ω belongs to the one thing that does: a single vantage, turned one way, passing from home toward a
horizon over whatever is there.

---

## Sources

- Tom, 15 November 2026: "Ok. New essay about Omega.. discreteness has no face . To flow continuously over
  discreteness, you need a face."
- Essay 21 (`21-omega.md`): Ω, the kit, a count of facings. Essay 25 (`25-counted-toward.md`): the ratchet (BLD).
  Essay 20 (`20-scaffolding.md`): scaffolding.
- *Reads and Writes* (`../readers-and-writers.md`) §1 (the two-by-two table; "Four things"), §9 ("Ω of relations and four
  facings make a circle").
- `plans/discussion-note.md` items 18–20; `plans/bld-plan.md`; `plans/cpx-plan.md`.
- SPN rulings cited: R313, R645, R798, R896, R909, R913, R922, R967, R1009, R1015, R1016, R1017, R1018, R1019, R1020, R1021, R1022, R1023, R1024, R1025, R1026, R1027, R1028, R1029, R1030, R1031, R1110, R1112, R1114.
