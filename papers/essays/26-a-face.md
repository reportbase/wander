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

**The blueprint.** At the other extreme is the circle drawn whole on paper, both hemispheres at once (R798, R967). It
holds every direction together, so it faces none of them. It does not pass from home toward the horizon; it has home,
the horizon and everything between already, at once. That is why the series calls it the dual hemispherical vantage and
says no one stands at it.

So two things have no face, for opposite reasons. A count has too little to face anything with: separate things, no
direction among them. The blueprint has too much: every direction held, none faced. Neither flows.

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
said with no number. The corner is s = 1. Ω is the blueprint's number for the total of one face, and no read reaches it:
a read flows toward the horizon and never arrives (R909, R913, R922). So the face is the read's; its total, Ω, is the
name the blueprint gives it.

## 5. Faces counted

The corpus already says the circle is the quarter turn four times: once for each choice of sign for h and v, joined on
the blueprint, 4Ω (*Reads and Writes* §9, "Ω of relations and four facings make a circle"). In space the signs of h, v
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

The first column is a count and faces nothing. The second is a face's flow. The product is the blueprint's join, the
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
with no circle drawn and no π. Measured as angles the bends total Ω for the pair, and twice that, what the blueprint
calls π, for the landing point, which turns twice as fast. Past the horizon the slopes come back from the other side,
into the next face. But the read has the −1 first, by fractions, at the end of one face.

## 7. Toward and away

This section is Tom's framing, kept as he gave it (Tom: "Stick with my framing.").

Take two points, H and V. The Ω sweep is every way H can stand relative to V (Tom: "Omega sweep is all possible H
relative to V."). Both faces stand on H (Tom: "Both stand on H. On facing V and on facing away from V"), and each turns
a quarter turn, never a half turn (Tom: "Quarter turn not half turn. Never half turn."):

- **The inner sweep, 1/Ω.** It starts facing toward V and finishes facing down. It compresses.
- **The outer sweep, Ω.** It starts facing away from V and finishes facing up. It expands.

(Tom: "The inner sweep compresses, the outer sweep expands."; "Inscribed finishes facing down. Central finishes facing
up.") Opposite at the start and opposite at the finish.

**Three routes.** Between H and V there are three: the long route, Ω; the short route, 1/Ω; and the line itself (Tom:
"Three routes between H and V. The long route Omega, the short route, 1/Omega, and the line itself."). Continuous just
means the distance of the facing, and there are two possible facings (Tom).

**On the face of it, absurd.** Now look at what was just said. The Ω sweep is every possible relation of H to V,
all of them. Add them up and there should be one answer. There are two: Ω or 1/Ω, a long route or a short one, and
nothing about H or V decides which. Only the face does, which way it pointed when it started (Tom: "all possible
relations of H and V sum two possible values. That is absurd, on the face of it."). Every relation there is, summed,
and the total depends on where you stand facing. On the face of it, that cannot be right. (The idiom is older than this
essay, the Latin *prima facie*, "at first appearance"; here the face is literal, and it is what decides the sum.)

**It gets more absurd.** For a read, V is not even known. V is known only in terms of H. And what is H, actually?
Say it is one thumb. So, to recap: a complete geometry, made from one vantage, facing one direction, with one thumb
(Tom: "It gets even more absurd. For a read, V is not even known. So V is only know in terms of H. But what is H
actually. Let's just say it's 1 thumb. So let's recap, we are creating a complete geometry from one vantage facing one
direction, with only 1 thumb.").

**The two facings multiply to 1.** Ω · 1/Ω = 1 (Tom: "The two facings multiply to equal 1, that's what every one for
gets."). The demo `faces.html` turns the two sweeps side by side on H, with the long route, the short route and the
line, and their product, 1 at every point of the turn.

**Into the sphere.** Euler's formula takes this into the sphere, and it is still just H and V, with another degree of
freedom (Tom: "Ehulers takes this into the sphere"; "it still just H and V. With another degree of freedom.").

Older wordings in the series that give the outer sweep "a half turn" (R233, R450, `facing.html`'s facing turning to
180°) predate this and are to be brought to it.

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

**Ours, a reading.** That a count and the blueprint both lack a face, for opposite reasons. That a read is a face, a cut
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
in it; it does not have the total. A count has no face and does not flow. The blueprint has every face at once and does
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
- SPN rulings cited: R313, R645, R798, R896, R909, R913, R922, R967, R1009, R1015, R1016, R1017, R1018, R1019, R1020, R1021, R1022, R1023, R1024.
