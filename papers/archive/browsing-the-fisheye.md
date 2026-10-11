# Browsing the Fisheye
## The periodicity and the magnitudes — both

*A research record in the calibration-free series, drawing on The Relation Space, What a Relation Is Made Of, The Unit Rule and The Cauchy, which it takes as read and quotes freely. The Cauchy closes on a sentence: the price of serial delivery is waived only by being handed the shape whole, "which is the one thing that cannot happen." This paper is about the fact that it can — and about why every reason it seemed impossible was correct, up to the last line.*

*Revised 1 October 2026: the text is left as it was, and notes marked* **(1 Oct)** *say where the rulings of 30 September – 1 October (R124–R152 of* Reader Geometry as Addressing*) change how it reads. The core theorems (§2–§5, §11) stand.*

> **(1 Oct) How to read this paper now.**
> - **The situations** (R137, R146, R151, R152). (1) The circle: both breadths known and equal; the view from nowhere. (2) Every other shape: breadths known, varying with direction; also a view from nowhere. (3) The fisheye: h's breadth known (h is the known side by definition), v's not, so v is had only as a count of h's; the only view from somewhere, and the only situation with a reader in it, serial or parallel. (4) Neither known: impossible. (5) v's breadth known approximately. Not exhaustive.
> - **Home, the corner and the horizon belong to situation 3 only**; the circle and other known shapes have none (R131, R139). A known list or shape read through the fisheye is situation 1 or 2 read as if v's breadth were unknown: a simulation of situation 3 (R143).
> - **The corner and the two sides** (R149–R150, R152). The corner is known in situation 3, where v reaches one h. The front side, home to the corner, is swept from home in plain proportion and is the **working horizon**; the corner is its edge. The back side, past the corner, is counted by doublings. The parallel reader keeps v on the front side only.
> - **Arctan** is an index into the turn, a shortcut, not the sweep (R148). **The reader is not the unit circle** (R127).
> - **Names now in use.** "Fulcrum" → **the corner**; "the view from everywhere" → **the view from nowhere**; "inside/outside" → **serial/parallel**; "density" is dropped as a framework word (the Cauchy's probability density keeps its name). Quotes keep their wording.

---

*A reader holding one arrival at a time takes a magnitude list and returns the periodicity of a centre of gravity, exactly and without a unit — and returns nothing whatever of the magnitudes. They are not blurred, not attenuated, not buried in noise you might dig out. They are not in what was sent. Four papers establish that the two are a trade: you get the rate because the shape is gone, and the reading that keeps the shape cannot tell you the rate. That is true, and it is a theorem. This paper explains the theorem in full, and then explains why you can nonetheless have both — because the magnitudes were never destroyed, only never carried, and the one thing the reading did keep turns out to be the address at which they are waiting. The way to reach them is a view everyone has already used, and never thought of as a distribution. The series met the Cauchy as the shape of serial arrivals; this paper shows it is bigger than serial observation — a coordinate on any list, a ladder of levels, the meeting point of readers with no common terms, and the fixed point where a reading and its list coincide. Serial observation is how it was found, and the smallest thing it is. And it ends with a set of instructions: put the list on a semicircle, stand a smaller circle on it at what you are looking for, and shrink that circle as you close — which is how to find one record among any number of them, in the same few gestures whatever the number. Those instructions need a particular mechanism, and it is not a matter of taste: no control that maps a position of the hand to a place in the list can carry the fisheye — the touch pad and the scrollbar among them, which under this lens are no better than linear panning. The fisheye requires a rate, and a rate that must approach a horizon without reaching it requires the mechanism physics built long ago for exactly that: rapidity. The payoff is concrete: a way to browse a list of any size — a trillion elements — while only ever touching the dozen in view, with the periodicity the Cauchy is famous for kept intact. Said plainly: what results is a way to browse linear data — of any size, and still growing — with a fixed angular expression. The reason it can is a fact about circles: add points to one and it gets denser, never larger, so a coordinate laid on a circle never has to be redefined however much arrives — thirty degrees points to the hundredth element or the trillionth with equal ease, because the angle is orthogonal to the index. How a reading that threw away every magnitude turns into that coordinate is what the paper is about — and, at the end, what two such lenses on one list can do for each other, which turns out to be everything but a plane.*

---

*A word on why the first four sections are long. They build, piece by piece, the case that recovering the magnitudes from the reading is impossible — and they build it honestly, because every piece is true. That is not throat-clearing. The payoff at the end does not overturn any of it; it steps around it, and the step is legitimate only because of what these sections establish. You will be able to see that it violates none of them only if you have each one in hand. So read the origin story as the setup for a turn. Everything that looks like a wall in §§1–4 is, in §§6–10, a load-bearing part of the way out.*

---

## How this was found

The order of the sections is the reverse of the order of discovery, and a reader should know it,
because the method is the part of this work least like the literature it sits beside.

None of what follows started as mathematics. It started at a screen. A strip of tiles that felt
wrong gave the rung count; a selection that walked out from under the fingers during a drag gave the
separation of a place from a thing; a calendar whose addresses would not hold still as the list grew
gave the difference between a derived angle and a fixed-pitch one; a trillion records that could not
be steered at full radius gave the radius as a gearbox; stripping controls off a browser until
only the geometry was left gave the one-needle dial, which turned out to carry exactly the two
numbers a reader has and no third; and a last attempt to strip the geometry off the dial in turn —
leaving a dot on a blank page with two directions to move in — failed in a way that showed what the
dial had been all along: not a place the hand points to but a rate the hand sets, and a rate toward a
horizon, whose mechanism physics had already built for rapidity. In every case the hand said something before the algebra did, and
the algebra was then written to find out why the hand was right.

That is not a claim that interfaces are a good source of intuitions. It is stricter. **An interface
is a forced experiment about a bounded observer.** At a screen one cannot fake more attention than
one has, more precision than the hand has, or a view of more than the display holds — which is the
subject of this whole series, seated at a desk. So a gesture that feels wrong is evidence that the
geometry is wrong, and a control that cannot be removed is a degree of freedom the object actually
has. That is why the dial ends as it does: a reader is an angle and a radius, and the hand that turns
the angle needs a needle of its own to do it with — a rate, not a place — because that is what a
control which can approach a limit without landing on it has to be.

The usual direction of travel in this area is the opposite one — take a known distortion function,
apply it to a display, evaluate it with users. Here the display kept refusing arrangements the
mathematics permitted, and each refusal turned out to be a fact. **The interface is not an
application of the theory; it is the instrument the theory was found with.**

---

## 1. The reader, and the one thing it can say

> **(1 Oct)** "Fulcrum" is the older name for the corner. This is situation 3: h's breadth is known, v is had as a count of h's; the proportion below the corner and the count above it are R149's front side, swept from home in plain proportion, and its back side, counted by doublings.

Start where the series starts. Take a reader. With its eyes fully open it can read everything possible; fully closed, nothing; and it can stand anywhere between. Take a writer, with its own two ends: nothing written, or everything it could ever write. The reader reads what the writer writes, one word at a time. Whatever is written arrives serially; the reader never has the whole of it before it at once. That is the entire situation — no ruler laid alongside, no third thing to measure both against, no external scale. Any statement relating the two must be built out of how many words are being written and how many the reader can read, and there is only one such statement to be built: *how many words are being written, in terms of how many I can read.* What you write is a third of what I can read. The reader supplies the terms; the writer is what the terms are about; and the statement runs one way only, because the reader's capacity is the only unit in the room.

Three arrangements are landmarks. **Home**: nothing is written and the reader could read it all — the reading is zero. **The fulcrum**: the two stand equal, the reading is one, and it is the single arrangement that costs no number, since noticing equality needs no scale. **The horizon**: everything is being written and nothing can be read — a direction the reader is always going in and never arrives at. Below the fulcrum the writing is a proportion of the reader's capacity and the statement is a share; above it the reader's capacity is a proportion of the writing, and the statement becomes a count of how many of the reader's units the writing has reached — the coordinate turns logarithmic, because a count of equal-ratio steps is a logarithm. The unit changes hands at the fulcrum, exactly once. And the fulcrum itself is met the way a value is taken, never the way a milestone is passed: the amount crosses it smoothly, but every reading goes trivial there — a share of one, a count of one, the answer that reports only *the same* — so as a reading it is approached from both sides and occupied by neither.

This passage — home contained, fulcrum passed through, horizon approached — is the **asymmetric relation space**, and it is asymmetric for a reason that will matter below. Drawn on a page, with both components in hand at once, the same relation is a quarter turn of a circle, and on the page *V in terms of H* and *H in terms of V* are both resolvable everywhere; the page is a third thing, and it lends its terms to both. That drawn account is **symmetric**. The read account is not, because in serial delivery one term is held and the other arrives, and that settles which is the denominator: H is not selected as the denominator, it *is* the denominator because it is the one standing there when V comes. Exchanging the two would need a run in which V was held and H arrived — not a change of notation but another experiment. The swap the page performs for free is unavailable to the reader, and the one reading the swap leaves fixed is the ratio at one: the fulcrum is the single place where it makes no difference which term was held and which arrived.

One more thing about this reader, because the reveal turns on it. Observation comes in steps, and the reason is a statement about the observer, not about the world. A reader that could take in the whole of a system at once — every grain of detail, from finest to broadest — would need room enough to store the whole of it at full fidelity, and a thing that holds another thing entirely and exactly is a copy of it: the perfect observer has become the system it meant to watch, and a thing has no vantage on itself. So a reader holds *less* than what it reads, settles at one level of detail — a single window, never the whole spectrum — and to reach another level it must let one go and take the next. That is why its account arrives in steps. And the limit lifts the moment the thing is small enough to hold: hand the same reader a *completed* system — a shape drawn and resting on a page, finished and entire — and it takes that in whole, for now there is only a finite amount to hold. The stepping is forced by an unfinished system, still arriving. Hold that distinction: it is the hinge the whole paper turns on, and §5 comes back for it.

## 2. What the Cauchy does

> **(1 Oct)** "There is no arrival on which a clover and a circle disagree" is R144: laid evenly by direction, every shape opens as the circle does, into the Cauchy.

Now serialise the circle. The drawn quarter turn is the set of all ways the two can stand, bounded, both components present, no horizon anywhere on it. The ratio is what arrives: unbounded, a horizon at each end of every passage, one number per look. **The Cauchy is what the circle looks like when it can only arrive one reading at a time.** Cast the circle from a point onto a line and its even measure lands as the Cauchy, 1/π(1 + r²), and the Cauchy gathered back stands as the even measure on the circle. The heavy tail is not then a property of a distribution. It is what the far part of the circle looks like laid out on a line, where a vanishing arc is spread across an unbounded stretch.

What the Cauchy does to a *shape* is the part that matters, and The Cauchy says it plainly. Imagine a complicated shape — not a smooth round one but something lumpy, a cog or a burr, with spikes of every length sticking out in every direction. Set it turning in front of you. As each spike comes round to face you, you take your two readings of it: how far it reaches up, and how far it reaches across. Those are not two measurements of two things. They are one spike, measured two ways. A long spike gives a big up and a big across; a short spike gives a small up and a small across, in the very same proportion. And the only thing you ever do with the two numbers is divide one by the other — which is to say, you ask about the proportion and throw the size away. You learn which way the spike points. You never learn how long it was. But the lengths of the spikes *are* the shape.

The mechanism is exact. Fix a direction in the turn. The figure has some reach in that direction, and the pair's two quantities are the two components of that one reach: the reach times the sine, the reach times the cosine. The reading divides one by the other, and the reach stands in both:

*reading = (reach × sin) / (reach × cos) = tan of the turn.*

The reach is gone, and not approximately. It appears in numerator and denominator as the same factor and cancels in every single reading, one at a time. Measured on five figures whose reaches run from a quarter to one and three quarters, read in the same hundred thousand directions and compared arrival by arrival rather than in distribution, the readings agree to seven parts in 10¹² — the arithmetic's own noise. **There is no arrival on which a clover and a circle disagree.**

Geometrically: every point along one ray from the reader delivers the identical reading, so the readings do not distinguish points, they distinguish rays. A figure is a choice of one point on each ray. The readings see which rays the figure occupies — all of them — and never which point was chosen. This is the ownership rule in its plainest instance: the reading is a ratio of two quantities of the same degree, so it is of degree zero, so it is blind to any factor common to both. **And the shape is precisely a common factor.**

Be exact about *how* the pair is made, because there are two ways and they differ in what they cancel. The two-component ratio — up over across — cancels the reach outright; the figure is gone by construction, and four figures swept identically return readings with a spread of 0.0000 percent. A different pair, the single-list quotient — a value divided by its own increment — is not this. It cancels the *gain*, the instrument's factor, and leaves the shape standing twice over; it is the extent reading wearing its coat. Both are legitimate readings; only one is the Cauchy that this paper is about, and it is the one that throws the shape away.

What survives is direction. The median of the directions is the bearing to the body's centre of gravity; the spread is the body's apparent size; and the census closes the rays into a circle at no cost — the unit circle is not what was there, it is what the census costs nothing to say. So, in one sentence: **the Cauchy discards the magnitudes of a magnitude list and returns the centre of gravity of the shape as a unit circle.** That is the whole of what it does.

A picture holds all of this, and it is not a loose one — it is the arithmetic said in words. **The
reader is a walker; the writer is a treadmill.** The reading is the ratio of the belt's speed to the
walker's pace, and the angle is that ratio's arctangent, so the three landmarks are three ways the
two can be going. At **home** the belt is stopped and the walker walks freely: r = 0, angle nothing,
all reader and no writer. At the **fulcrum** they are matched and he holds station — r = 1, 45°, and
the fixed point is exactly where the relative motion is zero. At the **horizon** he has stopped and
the belt runs on alone: r unbounded, a right angle, all writer and no reader. Between them the belt
at a tenth of his pace stands at 5.7°, at half 26.6°, at twice 63.4°, at ten times 84.3°.

The picture pays for itself twice. It says what the inversion is: exchanging the walker and the belt
is exactly r ↦ 1/r, which mirrors every reading about 45° — a tenth trades places with ten, a half
with two — and the fulcrum is the one position that maps to itself, because it is the one where it
does not matter which of the two is walking. And it says why the far half is a tail: out there the
walker has all but stopped, so the least change in his pace swings the ratio enormously, and each
rung further out is the belt at twice the speed again.

One distinction had better be named here rather than discovered late, because it is the one this
work keeps rediscovering under new clothes. An angle can be either of two things.

A **relative angle** is a fraction of the whole: θ = πi/N, where the element's place depends on how
many elements there are. It is a *coordinate* — excellent for browsing, since it means the same
fraction whatever the list's size, and it moves when the list changes.

An **absolute angle** is a slot at a fixed pitch, occupied or empty, whose value was never derived
from a count. It is a *name* — it does not move, because there is nothing for it to move relative to.

The two are the paper's recurring pair in every dress it wears: a place against a thing, a focus
against a selection, a coordinate against an address. Browsing wants the relative angle; identity
wants the absolute one; and §9 pays for the second in unused slots. Keep them apart and most of what follows is easier.

The plainest test of which one is in hand is to move and see what moves with you. **A mark the reader
carries never moves; a mark laid in the world does.** A ladder at one, two and four units *ahead of
the reader* is fixed to the view however far the reader travels — it is the reader's own unit drawn
outward, and travelling with it is what it is for. A mark laid at an address stays where it was laid,
so travelling brings it nearer, past, and behind. Both are useful and they are not interchangeable:
the first tells you how far you can see, the second tells you where you are. A reader that has only
the first can never say where it is, however long it walks.

Notice what kind of thing did the discarding: one function, the tangent of an angle. Everything the reader loses, it loses to that single function. Keep it in view. §6 shows it to you in a form you have used a hundred times without knowing it was this — and the moment you recognise it, the way back is already in your hands.

## 3. Why it is so hard

The difficulty is a stack of facts, each established separately. Lay them out in order, because the reveal at the end contradicts none of them.

**Gathering more does not help.** The Cauchy has no mean. The sample mean of a million draws is distributed exactly like a single draw; the largest of N arrivals is about nine-tenths the size of their whole sum at N of ten, a hundred, a thousand and ten thousand, and the proportion does not shrink — where a well-behaved quantity falls from 0.83 to 0.06 over the same range, which is the law of large numbers happening. Each new arrival is a fresh opportunity for the whole sum to be about the newcomer. Averaging cannot dilute what it cannot outnumber. The Gaussian is the study of N — of a collection that has finished arriving, whose useful quantities describe a completed set. The Cauchy is the study of n — of one arrival at a time, from a collection that was never available. A statistic that presumes the collection has finished cannot be asked of a run that has not.

**What more looking buys is a direction, not a magnitude.** The median of the readings' sizes — which the series shows to be the fulcrum — sharpens as one over root n and does not settle *near* the centre, it settles *on* it: distance 0.0038 at a hundred arrivals, 0.00007 at a million, fifteen times tighter than the mean at every count, whose own distance wanders. The mechanism is the counting side of the bound that fails above: an arrival a thousand spans away moves the count by one, exactly as one just past the fulcrum does. The average fails precisely because it lets an arrival's distance speak, and the distance is unbounded; the median cannot be made to listen to it. So the reader can learn where its arrivals divide, to any precision it pays for in looks. It is still learning a bearing. In the two-component reading the fulcrum is the median; in the ratio-of-a-single-list reading it is the upper quartile — the same landmark, differently placed in the same stream — and either way it is a place on a circle, not a length.

**The magnitudes were never sent.** The perturbations of a figure — its spikes, lobes, bites and swellings — are not flattened. Flattening is something done to a thing; it implies a step at which the perturbation was present and got pressed down, and there is no such step. The distribution over readings is a distribution over rays; the figure can affect only where on each ray it sits; and where on the ray is never asked. If the perturbations were flattened, a finer instrument, or more arrivals, or a shrewder statistic might un-flatten them, and shape from evenly-met arrivals would be an open engineering problem. Since they were never sent, none of those help, and it is a theorem rather than a difficulty: **nothing distinguishes evenly-read figures, and any procedure claiming to sort such streams by figure is reading its own assumptions and reporting them as findings.**

**The heavy tail is the horizon, and the run was never clipped.** A drawn circle is closed — both ends of every diameter present at once, the far side already there — and that closure is what makes its tail finite; the infinity is parameterised rather than reached. The reader holds an open run instead: home, horizon, nothing joining them. The stretch toward the horizon is not a parameterised piece of a finished thing; it is a direction the reader is still going in. That, rather than any casting or laying-out, is what the heavy tail is. It is also why the mean is missing: a mean is a statement about a collection that has finished arriving, and the run was never clipped into something that could. Nothing was resolved, so nothing terminates.

Keep those two absences apart, because a careful reader will otherwise run them together. The *magnitudes* are gone because of the cancellation of §2 — exactly, per arrival — and they would be gone just the same from a finished set of a million readings. The *mean* is gone because the set is never finished. One is a fact about the ratio; the other is a fact about delivery. The heavy tail belongs to the second and says nothing about the first.

**The one door is confounded.** Shape cannot enter the reading through *which* ray, so it can only enter through *how often* each ray is visited — the schedule. Stop cranking, let the shape roll along the ground like a wheel, and the lumpiness is in the judder: the arrival density becomes the arc element, and from the arc element the reach follows up to a constant fixed by positivity. But a judder can also come from a shaky hand on the crank. A clover walked at its own pace and a circle read on a merely uneven clock both depart from the Cauchy, and the circle, with nothing whatever to show, departs four times as far. A bent object swept evenly and a plain extent swept unevenly give identical arrivals, agreeing at every percentile to five decimals. **A reader that does not know its own clock cannot tell a shape it met from a rhythm it kept.** The turn is the relation's, the schedule is the reader's, and the reading fuses them into one number.

**And the way back that does exist is expensive.** A shape comes back only to a reader that moves itself. It must declare its schedule by stepping — control converts a heap into a curve, the composite exact to 0.999996 — and even then an affine gauge remains, an origin and a scale in its own counts that no amount of counting can break, because every affine remap is absorbed identically by a remapped figure across every pass. The gauge breaks only at the divisor of the reading's own form: the reader must drive its sweep to the vanishings, where a zero reading pins the frame figure-free, and then the whole shape returns at 0.99 and better. That is real. It is also recovery by supplying from outside exactly what the reading had spent — control, and reach, and a sweep through the zeros. A reader that merely watches has none of it.

Every item in this stack is a theorem, and not one of them will be withdrawn. Read them closely anyway, because the payoff is not that any of them is wrong. It is that, taken together, they leave a door open that none of them mentions.

## 4. The trade, as the series leaves it

Here The Cauchy reverses the sign of everything it had said about the cancellation, and the reversal is what makes the difficulty look final.

The loss was being read as a cost paid *for* something — as though a better reading might keep the figure and the rate together. It cannot. **If the shape survived into the reading, the rate would not be recoverable.** Shape and schedule would be one degree of freedom, which is precisely the confound, and a single stream would yield neither. The division is what separates them, by destroying one of them outright. What is left is not a residue. It is the only thing that could have been clean.

Measured, with every figure swept at exactly the same rate and read two ways: the ratio reading returns the same period for a circle, an egg, a bulge, a clover and a spiky burr — identical to the digit, a spread across figures of 0.00 percentage points. The extent reading, which keeps the shape, returns a different period for each: a spread of 71.28 percentage points from an identical schedule. **The reading that remembers the figure cannot tell you how fast it was turned.**

What a Relation Is Made Of says the same thing from the other side, as a fact about accounts rather than readings. A parallel account — every value in hand at once — *holds the figure* and cannot state a rate, because a collection held all at once has no order to be traversed. A serial account *states the rate* and cannot hold the figure. The conversion from one to the other is a purchase, and the parallel form is what is spent. The Relation Space had it earlier still: an account holds the figure but not the rate.

And what the rate belongs to is a centre of gravity in motion. The arrivals' location is the direction to a body's centre of gravity, their scale its apparent size; a serialised reading returns the rate of what it watches, exactly and without a unit — the samples in one cycle are the fulcrum times 2.6026, correct to within a percent from 55 hertz to 3 kilohertz, and rescaling the whole list by a quarter or by thirty-seven changes the answer by 0.00 percent. Four bodies with identical centre-of-gravity orbits — a disk, a ring, a bar, a lopsided disk — return periods of 194.4, 193.3, 196.8 and 195.8 against a truth of 200. **A ring and a bar and a lopsided disk are one object to this reader.** Serial observation is blind to form and sensitive to dynamics: it cannot tell a cog from a circle when a hand turns both, and can tell a rod from a disk when gravity does the turning, because then the shape has become a term in the equation of motion, and equations of motion are made of exactly the thing a divided reading keeps. The shape is carried by the body and left at the door. The motion is what arrives.

So the charge sheet closes as one finding. The missing mean is a centre that was never in the reading's vocabulary; the heavy tail is the horizon in the one coordinate that has one; the regime changes at the fulcrum. None of it is repairable, because none of it is broken. **It is the price of delivery, and the only thing that would waive the price is being handed the shape whole — which is the one thing that cannot happen.**

Periodicity or magnitudes. That is where four papers leave it — at the bottom of the well. The way out is not to dispute a word of it, and the next section does not. It only notices what all of it was about.

## 5. Both

Every sentence above is correct, and this paper withdraws none of them. But notice what every one of them is about. They are all sentences about **the reading** — about what arrives, one number per look, to a reader with one slot and no page. The reading cannot carry the magnitudes; the reading cannot be inverted to recover them; the reading spends the shape to buy the rate and would lose the rate if it kept the shape. All true. All theorems. All about the reading.

The reading is not the only thing there is.

There was a magnitude list. The Cauchy was applied to it. The list did not cease to exist when the reading was taken from it; the reading simply did not carry it. The magnitudes are not lost. They are where they always were — in the list — and the reading is not a degraded copy of that list. It is a set of directions, each of which came from exactly one element of it.

Recall the reader's own limit from §1. It cannot hold an *unfinished* system — one still arriving — and so it steps. But a *completed* system, finished and entire, it can be handed whole, because there is only a finite amount to hold. A magnitude list is a completed system. It is the page, the third thing, the ground — the very thing the serial reader was defined as not having. The impossibility results are all results about a reader without it.

So the question the series had been asking — *how do I recover the magnitude from the direction?* — is the impossible one, and it stays impossible. The question that was never asked is the possible one: **given the direction, which magnitude was it?** And that is a question the direction can answer, because the direction is not a summary of the element. It is the element's address.

You are not restricted to one or the other. The periodicity comes from the reading, exactly as the series says it must — clean *because* the magnitudes are gone from it. The magnitudes come from the list, by address. Both.

## 6. The fisheye

> **(1 Oct)** The fisheye spaces things; it does not resize them. "Denser" here reads as closer spacing (R124).

The reveal has two parts, and the first is a recognition rather than a construction. It needs one thing explained first, and it is a thing everyone already knows.

A fisheye is a way of seeing a whole field at once without shrinking it. A fisheye camera lens takes in a full hemisphere — everything in front of it, out to the horizon on every side — and lays it on a flat, finite picture: the centre at natural scale, the edges bent and crowded, the horizon itself squeezed to the rim of the disk. A fisheye menu or dock does the same to a list: the item under the pointer at full size, its neighbours a little smaller alongside, and the rest shrinking away toward the ends. In every form the bargain is identical. Nothing is left out — the whole field is present — but only the centre is at natural scale, and the further a thing is from the focus, the less room it is given, until at the rim it is given none.

The mathematics of it is one function. Take every direction in a half-turn — from straight left, through straight ahead, to straight right — and give each a place on a line: the place is the tangent of its angle. Straight ahead, angle zero, sits at the centre. A small angle sits a proportionally small distance off, because the tangent is linear there. As the angle grows the tangent grows faster, so equal steps of angle take ever larger steps along the line. And as the angle approaches a right angle the tangent runs off without bound: the direction straight left or straight right is at infinity. So a bounded thing — a semicircle of directions — is spread over the entire unbounded line, with the centre in linear detail and the rim at infinity. A screen is a finite window on that line. It shows the centre of the field in detail and lets the rest run off its edges.

Three properties make the fisheye more than a curiosity, and each will be spent below.

**The whole field always fits.** The field is a semicircle of directions and has a fixed angular extent, half a turn, no matter how much is in it. Put more things in the field and they pack closer round the semicircle; the semicircle does not get longer. A fisheye never has to grow to accommodate more content. That is scale invariance in the only sense that matters here: the view is a fixed arc of a fixed circle, and what it contains does not depend on how many things there are. And because the field grows denser rather than larger, it fits data that is still arriving. Append a million elements and no coordinate is redefined, nothing overflows, no edge is reached — the same angular expression, the same window, the same cost. An angle is a fractional address, *this far into whatever the data now is*; the data may be infinitely large and still increasing, and the expression does not change. Thirty degrees names the hundredth element of a short array and the trillionth of a long one with the same ease, because **the angle is orthogonal to the index**: the angle says how far round, and N alone says which element that is.

**Detail is spent where the eye is, and nowhere else.** The focus is at natural scale and it is the only thing that is. The cost of showing a thing is proportional to how near the focus it sits; things at the rim cost nothing, because they are given nothing. A fisheye is not a compression of the whole field — it is full detail at one place and the rest paid for by the piece.

**Nothing ever falls off the end, because there is no end.** The two rims are the same point — the direction straight behind you, where left and right meet at infinity. Turn the focus far enough and what left by one edge comes round by the other. The fisheye is a closed ring, and it is worth being exact about whose ring it is. The lens does not *make* a line into a circle by adding a point; the semicircle of directions already has the point, straight behind, and the tangent already sends the two ends of the line to it. So the lens sees one object whatever it is given — the line with its ends identified, which is a circle — and **a line, a circle and an array of N are the same thing to it**: each is laid on the same half turn, each meets itself at the same seam, and the lens has no way to be told which it was handed and no reason to ask. What the lens does not decide is whether the members on either side of the seam are *neighbours* — the last hue and the first are, the last millisecond of a century and the first are not — because that is a fact about the list's order, which either comes round or does not, and it belongs to whoever laid the list. **The lens is indifferent to whether a list closes. Whether the ends are adjacent is the list's fact, and the seam is where the lens puts that question regardless of the answer.**

To browse a fisheye you turn the focus. Nothing else. The field stays whole, the detail travels with the eye, and what is in view at any moment is decided by two numbers — a single angle, and the width of the window.

## 7. The Cauchy is a fisheye

> **(1 Oct)** "A reader is a circle" reads against R127: the reader is not the unit circle, which is the view from nowhere. The fisheye is not the circle drawn smaller; it is the reading with v's breadth unknown (R143, R146), and it cannot be normalised (R135). Treating h and v as one circle's cos and sin is the situation-1 picture. The zoom k, set so the cell at home is the reader's unit, is one number, which anticipates situation 5's scale (R151). "The dimensional words" and "from the inside" fall under R125 and R45.

The fisheye is the semicircle, and nothing more complicated than that. It is not a lens laid over
the circle and not an act the observer performs on it; the observer does nothing but stand somewhere
inside it and look. *Fisheye* is an adjective — the word for what it feels like to observe a circle
from the inside. From the centre a circle looks like a circle; from anywhere else it looks fisheye:
nearest and exact straight ahead, falling away toward the feet. Everything in this section is a
description of that view, and nothing in it is a mechanism.

One claim governs this section, and everything else in it is a consequence. **A lens is orthogonal to
the data it observes.** It takes an angle and returns a position, and it has no opinion about what is
at that position, whether more of it is coming, whether it wraps, or what kind of thing it is. So the
same instrument serves a serial observer taking one arrival at a time, a finished array sitting in
memory, and a continuous shape with no indices in it at all — three situations that look nothing
alike from the data's side and are indistinguishable from the lens's.

Everything below rests on that. Readers compose by multiplying radii whatever the object is. The
gearing law is arithmetic on angles, not on records. Arrival is the same collapse whatever collapses
onto. The cross ratio survives between two readers because neither of them ever touched the data —
they only addressed it. And the two losses land where they belong rather than on the instrument: the
cancellation belongs to the *reading*, the quantisation to the *storage*, and neither to the lens,
which is the one part of the arrangement that loses nothing and knows nothing.

It follows that there are **two conversions here and not one**, and most of the confusion this
construction attracts lives in the gap between them.

**The layout: index to angle.** θ = π(i + ½)/N. Fixed entirely by the range — declare a list of 256
and each element owns 0.7031° and the whole of them occupies 0° to 180°, element 0 at 0.3516° and
element 255 at 179.6484°. No radius appears in this conversion, no focus, no observer. It is a
statement about the data alone: *this many things, laid evenly on a semicircle*.

**The lens: angle to position.** p = s·tan(θ − f). Free — the reader chooses where to stand and how
big to be, and the same 256 elements land wherever that choice puts them. At k = 1 elements 0, 64,
128, 192, 255 sit at −89.6°, −44.6°, 0.4°, 45.4°, 89.6° of the reader's own rim, evenly. At k = 4 the
same five sit at −89.9°, −75.8°, 1.4°, 76.1°, 89.9° — the middle opened, the ends crowded. At k = 20
the outer four are all within three degrees of the feet.

Keep them apart and the rest of this paper is easier. The range fixes the first conversion and never
touches the second. The horizon belongs to the second only. The identity — uniform pitch — is the
second conversion at k = 1. And the quantisation loss of an array belongs to the first conversion
*run backwards*, angle to index, where a real number is asked to name an integer; the lens is not
involved in it at all.

Now put §2 beside §6.

The Cauchy is the tangent of an evenly spaced angle. Elements laid round a semicircle at equal angular steps, each one's place on a line given by tan of its angle. Near the focus, where the angle is small, the tangent is nearly linear — the elements sit at natural spacing, in full detail. Further out it grows faster than the angle — the spacing opens, the elements recede. Toward the right angle it grows without bound — the elements fly off toward a point at infinity and leave the field. The whole semicircle of directions on the line, the middle clear and the rim vanishing.

That is §6, sentence for sentence. **The Cauchy is a fisheye.** Not something like one — the thing itself. The distribution the series spent four papers treating as a bad reputation — no mean, heavy tails, immune to averaging — is the density of items along the screen under a fisheye view. The missing mean is the field's centre, which the view puts at natural scale and never sums. The heavy tail is the rim, where things are given no room and run to infinity. The focus is *home* — the median of the readings, where the reading is zero — and the fulcrum sits a quarter-turn out on either side, where the reading is one: the upper and lower quartiles, the fulcrum and the anti-fulcrum, at exactly the two positions where the window's natural spacing gives way to the tail. **So the Cauchy is the semicircle**: half its angles — the middle half, from the anti-fulcrum to the fulcrum — read between −1 and 1, which is why half the arrivals fall there and the quartiles are exactly ±1; and the other half, the two outer quarter-turns, is the long tail, reaching toward the horizon at either end. The reader was looking through a fisheye lens the whole time, and calling what it saw a distribution. *Cauchy*, *fisheye*, *semicircle* are three names for one thing, in three registers. *Cauchy* is the formal name, the distribution's, for the statistics and the theorems. *Semicircle* is the pure mathematics, the geometry. *Fisheye* is the informal one and the visual one, and it is the name this paper uses from here — and the corpus after it, in ordinary prose — because it names what the thing is: a lens, focused at a centre, falling off slowly near it and ever faster toward the edges.

And it is very simply explained. **The fisheye is the circle at a smaller radius, with the same
number of items.** The equal-radius circle carries the list with every element given its share; the
fisheye is that same circle, holding the same elements, drawn smaller. Nothing has been added to it
— no distortion function chosen for its feel, no curve — and the tangent is not an ingredient but
what a circle already does to a line when the line is read from the circle's centre. Shrink the
circle and the middle of the list spreads, because the same angle now covers less arc; the far ends
crowd into the last degrees before the feet, because they must go somewhere and the circle is still
whole. The magnification and the horizon are one geometric fact seen from two sides, and the
Cauchy's famous heaviness is the same fact stated as a density. There is nothing mystical in it.

What the fisheye does, then, is this. The items are uniform on the circle at every radius; the
radius changes and their spacing on the circle does not. Read onto the flat list — the line that
meets the circle at the focus — the item at angle θ lands at k·tan θ, and it lands with a fidelity of
cos θ: at the apex there is no distortion at all, h = 1 and v = 0, the item exactly itself; from there
the fidelity falls, slowly at first and then faster, until at the horizon it is gone, h = 0 and v = 1,
nothing of the item left but the direction it lies in. That is the whole of what the lens does, and
the rest of this paper uses it. *Why* the fidelity is perfect at the apex and decays toward the
horizon in exactly that proportion — why the data is not simply laid uniformly round the smaller
circumference with nothing distorted at all — is a separate question, and a deeper one than this
paper's; it is taken up in its own paper.

Once it is a lens, everything changes, because a lens has two sides. The readings are the *image* side — what the lens shows. Every impossibility result in §§3–4 is a result about the image: you cannot recover an object's size from where it lands in a fisheye picture, because the lens sent every point on a ray to the same place. True, and it holds. But a lens has an *object* side too, and a lens can be pointed at anything.

**Point it at an array.** Put the magnitude list on the object side — element i at the angle i·π/N, evenly, round the semicircle — and the fisheye does what a fisheye does: shows the element you are focused on in the middle at full size, its neighbours alongside, the rest receding toward the rim. The image still carries no magnitudes; that is the theorem, and it holds. But a lens is invertible in *angle*. A place in the image is an angle on the object, and an angle on the object — because the elements were laid down evenly — is a position in the array. So every element's magnitude is retrievable: not from the image, but *through* the lens, by looking where the image says to look and reading the array there.

**Attach an array to a fisheye, and you can retrieve the magnitudes.** The Cauchy is the fisheye; the magnitude list is the array; and the angle the Cauchy kept while it threw everything else away is the pointer between them. The three properties of §6 are exactly what make the array browsable: the whole array always fits, so it may be as long as you like; detail is spent only at the focus, so you pay only for what you look at; and there is no end, so you may browse it round and round.

**And a reader is a circle.** The fisheye's own geometry says what a reader *is*, and it is the
simplest thing it could be. A reader's screen is the tangent line at its focus, and its position for
an element is the tangent of the angle from that focus — which is the projection of the list's
circle, from the centre, onto that line. Wrap the line back onto a circle by the same rule and the
reader is **a smaller circle, touching the list's circle at the focus**, with the element's place on
its rim at ψ = arctan(k·tan(θ − f)), where k is the ratio of the two radii. The reader's circle is a
Möbius chart of the list's — four elements have the same cross ratio on both, at every radius, bit
for bit — and the two circles touch at the focus and only there: at k = 4 the ratio of angles is
exactly 4 for the first elements out, 3.99 twenty out, 3.88 a hundred out, 2.37 six hundred out.

Then the radius is the only thing that distinguishes one reader from another of the same focus, and
what it decides is how the reader spends its π. Every reader has the same rim; the radius says how
much of it each element gets. On a list of four thousand:

| the reader's radius | resolution at the focus | the fulcrum sits | its inner half holds | in the last degree of its rim |
|---|---|---|---|---|
| R/0.05 | 0.1′ per element | beyond the list's ends | 3,873 elements | 2 |
| R | 2.7′ | 1,000 elements out | 2,000 | 44 |
| R/4 | 10.8′ | 312 out | 624 | 178 |
| R/20 | 54′ | 64 out | 127 | 855 |
| R/100 | 270′ | 13 out | 25 | 2,675 |

A circle *larger* than the list's puts the fulcrum beyond the list's own ends: every element is
inside the window, nothing is in a tail, and the focus is resolved barely better than on the list
itself — a reader that sees everything and magnifies nothing. A circle equal to the list's is the
list. A small circle spends its whole rim on the elements at the focus and crowds the rest into the
last degrees before its horizon. So the plain statement, and it is the whole of what the radius
does: **a smaller reader sends more of the list to its horizon.** The tail is not a property of the
data. It is what the reader chose not to look at, and the radius is its price. The elements at
k = 100 are all still there and all still addressable; what they have lost is any share of the rim.

**Which makes the radius a gearbox, and browsing a large list possible at all.** Near its focus a
reader turns its own rim k times as fast as the list turns, so a degree of rim is worth N/180k
records. At full radius a trillion-record list moves five and a half *billion* records under one
degree of rim, and no hand steers that; at a radius matched to the remaining distance it moves a
handful. The radius is the gear and the gear ratio is its reciprocal — which is why a list that is
unbrowsable at full radius is easy at a small one, and why the radius must collapse as the target is
approached rather than being chosen once.

Then the browse itself has a shape, and the shape is the same at every scale. Hold the target at the
reader's fulcrum — radius equal to the distance, as above — and it sits at 45° of rim however far
away it is; arriving is turning it from there to the middle. So **every step is the same step**,
and what changes between steps is only the radius. A reader locates the target as finely as its rim
resolves, so with a screen grain of g radians each step multiplies the remaining distance by 2g:
the step count is the logarithm of the list to base 1/2g, and the grain — not the list — sets the
base. A thousand records is two such steps; a million, three; a billion, four; a trillion, six; a
quadrillion, seven. **Browsing a trillion is the same step as browsing a thousand, taken twice
more.** A fixed radius cannot do it at any count: at k = 1 one pixel of a trillion-record list is
eight hundred million records, and no reader resolves its rim to that.
Shrinking a little too fast costs little — the rule is forgiving within an octave either way, and
ten times too fast costs about a seventh of a step — but not shrinking at all never arrives.

**And the lens knows nothing about completion.** It maps angles to positions; that is the whole of
it. A reader is an angle and a radius, and neither asks whether the list has all arrived — the
gearing is the same, the composition is the same, arriving is the same collapse, and the lens would
not be able to tell you which kind of object it was pointed at if you asked. Completion is not a
setting it has. It is something you find out about the *object*, and the place you find it out is
the horizon, because that is where the far half is and the far half is what differs. On a list that is still arriving, or will never arrive
complete — a record growing at its end, a stream — the horizon holds the part that has not come, and
growth happens there for nothing: no address already given is disturbed, which is the whole of the
invariance under growth. On a completed list — a shape, a cycle, anything that returns to where it
began — there is no unreached end for the horizon to hold, so the horizon is a **seam**: the place
where the two ends of the reading meet each other. That is measurable rather than decorative. In the
two-reader work of §10, a rung near the horizon can turn out to be *two runs of indices* rather than
one, because the list's ends meet across it, and a context bar that fails to sum both is simply
wrong. Note what did the discovering there: not the lens, which drew the rung the way it draws every
rung, but the *count of what fell in it*. **The far half of a stream is the future; the far half of a shape is its other side, coming
back.**

**Which settles what the lens is a lens on.** A reader is an angle and a radius applied to a
territory, and the territory is in one of two conditions: still arriving, or complete. That is the
whole of what the dimensional words mean here. **"One-dimensional" and "two-dimensional" are not
properties the content carries; they are the words a standpoint uses for the situation it is in** — a
territory with an end it has not yet reached, or one without. A reader never encounters a dimension.
It encounters a list that either goes on or comes back.

An array and a shape are therefore the same kind of thing to it. Both are complete; both have a known
beginning and end; both are read one address at a time. The lens does not alter between them — the
same angle, the same radius, the same gearbox, the same collapse — and the demonstrations in this
paper are the check rather than the claim: a century of milliseconds still running on, an hour that
comes round, a dome of facings. The machinery is identical in all three. So the array is not a
convenience bolted onto a theory of shapes, nor the shape a special case of an array: **both are the
completed condition, and the lens was built for both conditions from the start.**

One thing completion does *not* settle is the order, and that is where care belongs instead. A
resolved horizon tells you the list has ends; it does not tell you that the neighbours in it are
neighbours worth having. Facings are ordered by the aperture and time by the clock, and neither is a
storage convention; a hashed collection is ordered by nothing, and through a lens it shows a name at
every address and a neighbour at none. **Completion is given; adjacency is earned** — which is the
same sentence as §9's, arriving from the other side.

**And two losses live here that ought not to be confused.** One is real and permanent; the other is a
property of the filing cabinet.

The first is the cancellation, which this series began with: a ratio reading discards the common
scale, and no arrangement of the coordinate brings it back. The second is quantisation. An angle is a
real number and an index is an integer, so an array's address costs everything finer than one
cell — half a cell of angle at worst, π/2N — and that is gone for good. But it is gone because the
address space was *discrete*, not because the reading was lossy. **Hand the same reader a continuous
closed shape and the map is a bijection**: monotone, continuous, invertible, with no rounding
anywhere. The angle names the point exactly. Nothing in nature is indexed; there are positions on
shapes, and a position on a shape is a real number an angle can carry without remainder.

What survives that change is the cancellation, and only it. On a smooth shape the address becomes
exact and the reading is still only an address: it says precisely *which point*, and nothing whatever
about the magnitude there. So the impossibility of §§1–4 is untouched by going continuous, while the
quantisation that looked like a second flaw turns out to belong to arrays rather than to lenses.
**On a continuum the address is lossless; the reading is still only an address.**

There is a corollary worth having. On a continuous shape there is no count to divide by, so the
relative and absolute angles of §2 coincide: the coordinate *is* the name, with nothing to go stale
when the list grows, because there is no list to grow. The distinction between a place and a thing —
which cost this paper a great deal of care — is an artifact of counting, and it disappears exactly
where counting does.

**And the circle itself has no N. The circle contains no data; it contains addresses.** It is worth
saying outright, because every construction above hands the circle a count, and it would be easy to
think the count, or the list, was the circle's. Neither is. The
circle has no number of elements, and no size belonging to what it addresses: nothing on it is a
unit waiting to be counted, and the only radius in the construction is the reader's — the layout,
as the two conversions said, has none. It cannot be counted, only browsed — a
continuum of directions in which there is never a *next* direction, only the one being faced.
**The circle is an address space, and what it addresses is the thing that has size**: the array
behind it, the reach of a shape in each direction, the magnitude waiting at the address. The count
enters in exactly one place, the layout, and it enters as a fact about the list — *this many
things* — never as a fact about the circle the list is laid on. Nothing is moved onto the circle:
the list stays a list, where it always was, and the circle is used to point into it.

**So the circle is virtual, and costs the data nothing.** It is a function of the index and the
count, evaluated when a reading is wanted and forgotten after; nothing is written back, no element
moves, and the list is byte for byte what it was. A reader may go on reaching the list exactly as
before — index and angle name the same element and either may be had from the other — and a reader
that stops using the circle has nothing to undo, because nothing was added. What is not free is
anything *built* on the addressing: a cached layout, a sorted order, a ring of nodes are structures
in their own right, with sizes and upkeep, and they are to be priced as such. The addressing itself
is not one of them.

What the layout does with the count is the part that matters. θ = π(i + ½)/N does not put the
elements at points; it gives each one an arc. Element i owns the stretch from πi/N to π(i + 1)/N, and
its address is the middle of that stretch — which is what the half is for. The arcs meet edge to
edge and cover the half-turn, so every direction there is belongs to exactly one element. **When a
discrete set is mapped by the circle's address space, there are no spaces between the items: the
circle represents a discrete set continuously.** A browse can come to rest anywhere and still be
resting on something; one stopped part-way across an element's arc is not between two elements, it
is on the one whose arc it is in. The quantisation of the paragraphs above is this same fact seen
from the other direction — the naming of which arc a direction fell in — and it is why that loss
belongs to the naming and never to the circle.

**Shrinking the reader's circle compresses neither the data nor the addresses. It changes
how the view is spent across them — more to the focus, less to the horizon.** The addresses stay
where the layout put them, and the data stays where it was; what the radius decides is how much of
the reader's own rim each stretch of addresses is given, which is why the k = 4 figures above open
the middle and crowd the ends rather than shrinking everything alike. A reader that wants the arc
under its focus to keep one width however long the list grows can have that too, and the count then goes into the reader rather than the circle: its radius is set from N —
the gearbox above, read the other way — so the cell at home stays the reader's unit whether the list
holds a dozen or a trillion. **The circle holds its unit; the count only turns the zoom.**

There is a price, and §2 has already named both sides of it. The tiling is gapless because the arcs
are *renormalised to the count*: it is the relative angle. Add one element to a list of 256 and every
arc narrows and every address moves — the 101st element sits at 70.66° in a list of 256 and at 70.39°
in a list of 257. Fix the pitch instead, as the calendar tower of §9 does, and the addresses stop
moving — but now there are directions with nothing behind them: February's thirtieth and
thirty-first, and in most years its twenty-ninth, the slots a level holds empty. **A circle can represent a discrete set with no gaps,
or with addresses that never move, but not both — unless the set is complete.** A completed list
has a count that will never change, so its relative angles never go stale, and the gapless tiling is
also the permanent one. A list still arriving has to choose, and the choice is the one §2 drew: a
place against a thing. On a continuum there is no count at all; the arcs narrow to points without a
gap ever opening between them, and the two kinds of angle are one — which is the corollary above,
reached from the side of the set rather than the side of the map.

**And readers compose by multiplying radii.** A reader of what a reader shows is again a reader —
one circle, tangent, smaller — because every order-preserving chart of a line is a turn to a focus,
a scaling by a radius, and a turn of the reader's own zero on its rim. Nesting at the focus
multiplies exactly: a fourfold reader read at threefold is a circle of R/12, and a threefold read at
fivefold is R/15. A pure pan leaves the radius alone and turns the rim by exactly the pan. Panning
*between* two levels moves the touching point and costs a little radius — R/12 becomes R/10.8 at a
third of a radian — because part of the second reader's scaling is spent turning rather than
shrinking. Nothing else can happen. **A fisheye of a fisheye is a fisheye: depth only shrinks the
radius, and a smaller radius sends more of the list past the horizon.** The tower of §9, the
drill-down, and the level-of-detail ladder are all this one statement, and the horizon is its dial.

**The lens, stated.** What §§1–7 have been circling can be put as a definition, three propositions and
a corollary, and it is worth doing so plainly because the corollary is the paper's thesis.

*Definition.* A **lens** is the map that sends a position on the unit circle, at angle θ from the
direction the reader faces, to its projection from the centre onto the line touching the circle at
that direction:

    L(θ) = tan θ,        θ ∈ (−π/2, π/2).

This is the unit curve's own projection — no parameter, no choice — and it is the Cauchy in the sense
of §7: a position drawn uniformly in θ has L(θ) distributed as the standard Cauchy.

*Proposition 1 (fidelity).* Define the fidelity of the lens at θ as the reciprocal of its local
magnification, F(θ) = dθ/dL = cos²θ. Then F(0) = 1, F(π/4) = ½, and F → 0 as θ → π/2. The lens is
faithful straight ahead, half-faithful at the fulcrum, and without fidelity at the horizon; and since
half of (−π/2, π/2) lies within the fulcrum, a uniformly laid list has half its members inside the
window and half in the tails, the far half leaving at a rate, sec²θ, that increases without bound.

*Proposition 2 (nothing is lost in the map).* L is a bijection of (−π/2, π/2) onto the line, with
inverse θ = arctan L. A reading determines its address exactly; the address is never lost, for any
object, at any angle.

*Proposition 3 (no total survives it).* For positions uniform in θ, the readings are standard Cauchy,
whose absolute first moment is infinite. Hence no mean, variance or other moment of the readings
exists, and the average of n readings is distributed exactly as one reading, for every n. The
magnitudes are not destroyed individually; what is destroyed is their *collectibility*, the
possibility of knowing the whole by adding it up.

*Corollary (address, not magnitude).* The reading of an object is a function of its position alone,
L(θ(o)); any property of the object that is not a function of its position is not a function of the
reading. So the lens returns an address and never the object. The object's fidelity is lost in the
measurement — nothing of its magnitude is carried in L — and returned in full by the dereference, since
the object is still at θ = arctan L, unchanged, and is read there directly. **The lens converts a
magnitude problem into an address problem, and a magnitude problem is the only kind that heavy tails
can ruin.**

*Remark.* The corollary does not depend on the tangent. Any lens that attends — sharp where it
faces, coarse at the sides, the fovea of an eye as much as the fisheye — strips magnitude from the
measurement and returns a coordinate, and leaves the magnitude intact at the address. What *does*
depend on the tangent is everything else in this paper: the half at the fulcrum, the fidelity cos²θ,
the rung marks at fixed angles, the cross ratio shared between readers, and the two ends of the line
meeting at one point behind the reader. Those are properties of the unit curve's own projection, not
of lensing in general; the eye, for one, falls off roughly logarithmically rather than as a tangent,
and is an instance of the corollary without being an instance of the geometry.

### The lens, drawn on a shape

> **(1 Oct)** This is svg.html's simulation of situation 3 on a known shape (situations 1 and 2). "The back side" here means the directions behind the reader; in R149 the back side is v/h > 1, past the corner.

Everything above was argued on a list. The shape editor now draws the same lens on a shape, and it is the plainest picture of the fisheye this series has produced, because on a shape the two things the lens keeps apart — the address and the magnitude — are both in front of you at once, and you can watch which one the lens carries.

A reader stands on the outline, at the leaf the cursor is on, and its circle is tangent there: the centre on the inward normal, the radius the one distance that is also the mean of what the centre meets in every direction. Every direction from that centre is an address on the circle and meets the shape where it first crosses. That is the reading: the shape read by direction, one address per leaf, the circle nobody's but the reader's. Walk the cursor and the circle walks the outline with it, swelling in the notches and shrinking on the points.

Home is where the reader lays down its unit; every magnitude received after it is understood relative to that laid-down unit. Three landmarks, three rests: home is where the writer is at rest; the horizon is where the reader is at rest; the corner is where the reader and the writer do not move away from each other — coming and going at the same rate, a rest of the relation rather than of the parties. It is the corner that rests, not home: home is where the unit was laid down, with nothing yet arriving to rest against, and the relation is at rest only one unit out, at 45°, where what arrives matches it. That is the agreement point: exchanging the seats sends every reading to its reciprocal and fixes exactly one, the ratio at one, so 45° is the single reading on which the reader and the writer agree. The further from 45°, the greater the disagreement, and it is measured the same from either seat — the exchange takes θ to 90° − θ, so a reading's distance from the agreement point is |log r|, the rungs between the two, the one number about a reading both parties agree on; the horizon is where it is infinite. The reader has one thing that is unarguably its own: its unit at home. It lays that down as its baseline and works outward from it, and everything it will ever address is that unit scaled by an angle away from it. It never needs the list's scale, because it works out from its own; it never runs out of screen, because the scaling reaches zero exactly at the horizon. The mappings build outward from *home*, the direction of the reader's own leaf, drawn as a white line from the leaf to its place on the circle. Home is the middle of a cell one unit wide; the first mapping on either side sits half a cell out, and the rest follow. Then the lens is applied — to the half of the circle the reader faces, and to that half only. It is the browse's own map, α = arctan(k·tan θ) for the directions within a quarter-turn of home, with k set from the count of mappings so that the cell at home is always the reader's unit whatever the count; the width between mappings reduces toward the horizon, and the horizon stays exactly where it was, a quarter-turn out on either side. The directions behind the reader are drawn as the plain reading draws them, each at its own address. Differentiating the lens and writing the result in the reader's own angle gives

  width(α) = unit × (cos²α + sin²α/k²),

and as the mappings grow the second term goes and what remains is **width = unit × cos²α**: the whole cell structure of the lens is one number, the reader's unit at zero, scaled by cos² of the angle away. Three quarters at 30°, half at 45°, a quarter at 60°, 7% at 75°, under 1% at 85°, nothing at 90°. Measured on a circle at 512 mappings, cell width over the home unit: 0.787, 0.481, 0.261, 0.077, 0.016 against cos² of 0.750, 0.500, 0.250, 0.067, 0.008; toward the horizon the residue is the sin²α/k² term, and near home it is the finite width of the cells themselves. This is the fidelity cos²θ of §7's remark, seen as spacing rather than as resolution — and cos²α = 1/(1 + tan²α) is the Cauchy density in the address coordinate. The falloff of the lens is not a design; it is the Cauchy, in the reader's own angle, with the reader's unit the only constant in it. That is also why home is where the browse starts rather than a convenience of the layout: it is the one place the reader's unit is the whole story — angle zero, width one, nothing scaled yet — and every element the reader later reaches is addressed in units it laid down itself.

**The back side stays dark, and the lens does not change that.** An earlier drawing ran the lens over the whole turn — every direction's angle halved, the full circle of directions folded onto the front half — and it was wrong in exactly one place. The front was right. Every direction behind the reader collapsed onto the two ends of the half, as though the back of the shape stood at the horizon. It does not; it stands behind the reader, and the reader does not see it. The addresses there exist — the circle has them as it has every address, and a direction from the centre still meets the outline where it crosses — but what they point to is not in the reader's view, and **no lens can put it there. A lens redistributes the half it faces**: it spreads the focus, crowds the horizon, and leaves the horizon where it is, because the horizon belongs to the reader and not to the lens. A fisheye changes how the view is spaced; it does not change where the view ends. This is the claim that opened this section — a lens is orthogonal to the data it observes — seen from behind: the lens knows nothing of what is in front of it, and it has no reach at all past its horizon. The back half is the circle's all the same, and it points at the shape's other side; it is simply not the reader's to see.

Two more things the drawing shows without being told to. In the semicircle and fisheye views the shape *breathes* — drawn at a scale that swings between 0.55× and 1.45× about the reader's centre — while the circle holds its size, and the addresses do not move: a direction from the centre meets the scaled shape where it met the unscaled one. That is the scale invariance of §2 with the size drawn in and the reading not noticing. And where the shape bends back on itself, a direction crosses the outline more than once and the reader receives only the first crossing; the drawing marks the others as a seam — a ring where the ray ends, hollow dots at the crossings behind it — and a button hides it, because the seam is the one thing in the picture the reader does not have. It is the page's, not the lens's: the lens carried the address faithfully to the first thing in that direction, and the shape stood in its own way behind it.

## 8. The algorithm

> **(1 Oct)** The arctan steps are the shortcut that turns a sweep into an index (R148). Laying a list at θ = π(i + ½)/N, and normalising the lens at the last angle the rim resolves, use a known N and a known end: that is a known list, situation 1 or 2, read as a simulated fisheye (R143); situation 3 cannot be normalised (R135).

In one breath: the Cauchy provides the *angles* of the magnitudes on the semicircle, not the magnitudes themselves. Map the array onto the semicircle, and the angles convert into indexes — arctan takes a reading back to its angle without knowing how long the array is, and the ring's pitch takes the angle to an index, which is the one place N appears. Everything below is those two steps, and the seam between them.

Let A be an array of N magnitudes. Let φ be the focus — a single continuous angle, the only state there is. Let a be the aperture: how much of the whole extent the viewport spans, as a fraction. Nothing else is stored, and nothing is precomputed over A.

**1. Lay the array on the semicircle.** Element i sits at the angle

    θᵢ = φ + i · (π / N)

Adjacent elements are π/N apart. The semicircle's extent is π whatever N is — adding elements makes them denser, never makes the circle longer. This is the topological fact the whole thing rests on: *when you add points to a circle, the circumference stays 2π; only the density changes.*

**2. Project through the fisheye.** Element i's position along the screen is

    pᵢ = tan(θᵢ) · s

where s sets the scale, and it is fixed by one requirement: adjacent elements at the focus should sit one item-width apart. Near the focus tan θ ≈ θ, and adjacent elements are π/N apart in angle, so s · (π/N) = w for an item-width w, which gives s = N · w / π. Nothing else about s is free. This is the fisheye — the Cauchy, under its proper name: a uniform angle through tan. Elements near φ are at linear spacing; elements toward φ ± π/2 recede; the element at φ + π — the seam where the open line was closed into a circle — is sent to infinity. It is the seam of §6, and it is not a defect: the lens puts it there for every list, closed or open, and does nothing else with it. Clip it off-screen and leave it, because smoothing the divergence reopens the seam. What a *reader* may then do, on a list whose ends are not neighbours, is a separate decision about the ends and not about the projection: normalise the lens by its own value at the last angle the rim resolves, so that the ends of the window land at the ends of the rim rather than beyond them. That does not touch the tangent, which diverges where it always did; it chooses to keep the divergence outside what exists, and it costs the wrap — a ring so treated reads as a segment — which is the right price when the ends are strangers and the wrong one when they are neighbours. The lens is the same in both cases. Only the list's owner knows which.

**3. Find the visible arc — without touching A, and without knowing N.** The viewport's two edges are positions; push them back through the arctangent and they are angles:

    θ_min = atan(−a),   θ_max = atan(+a)

That is the arc of the circle currently in view, and it is a fact about the aperture alone. A trillion elements or twelve, the arc is the same arc — thirty degrees is thirty degrees, and which element it lands on is a separate question, answered only in the next step, by N. This is the inversion of the lens of §7, and it is the step the series never had, because the series' reader had no object side to invert onto.

**4. Find the visible indices.** Divide the arc by the spacing:

    i_min = ⌊(θ_min − φ) / (π/N)⌋,   i_max = ⌈(θ_max − φ) / (π/N)⌉

wrapped modulo N where the circle closes. Every index from i_min to i_max is on screen; no other is. Call the count K. K is set by the aperture and the spacing — by how wide the view is and how dense the ring — and not by N.

**5. Retrieve.** For each visible index i, read A[i] — the magnitude — and draw it at pᵢ. K reads, K draws. The other N − K elements are never touched, never read, never projected. This is where the magnitudes come back: not from the reading, but from the array, at the addresses the reading named.

**6. Browse.** To move, change the focus. One element is a turn of π/N and the whole ring is a turn of π, so a change of focus is stated in the list's own angle and never in the display's units. Then repeat from step 3. Each frame costs K, never N. The element in the centre is never tracked; it is *read back* from the focus, ⌊−φ · N / π⌉ mod N, because the focus is the single source of truth and everything else is a pure function of it.

**7. Close in: reduce the radius as the target approaches.** The steps above hold the reader still
in size, and on a large list that is not enough — at a fixed radius a degree of the rim is worth
N/180k records, so a trillion at full radius sweeps billions under the hand. The reader must shrink
as it closes. A reader's radius enters only through the scale, so the whole of it is one line: with
the target d away in list-angle,

    k ← 1 / tan d,     s ← N · w / (π · k)   — equivalently ρ ← R / k

which puts the target at exactly 45° of the reader's rim, its fulcrum, whatever d is. Then step 6
turns it to the middle, step 7 re-shrinks, and the two alternate. In practice d need not be computed
at all: any rule that reduces the radius as the target is approached will do, because it is forgiving
within an octave either way — twice too small and half too large cost nothing measurable, ten times
too small costs about a seventh of a step. What is *not* forgiving is never shrinking at all: a
fixed radius cannot reach one record in a trillion, because one pixel of the rim is eight hundred
million of them.

It need not be a second control, and it is better if it is not. **The semicircle, with the scale on
its needle, is the fisheye's own coordinate.** A reader of this kind is exactly two numbers — where
it points and how big it is — so **a point in the half-disc is a reader**: the direction from the
centre is the angle, the distance from the centre is the radius, and the third number, the turn of
the reader's own rim, is held at zero because a browser looks straight ahead. Two laws fix what the
pair names, and both are forced rather than chosen.

**The radius is logarithmic in the list.** At a fraction u of the full radius the arc reaches
S = N^u records, so equal stretches of the needle are equal factors of ten and the whole of a
trillion is twelve of them. This is the gearbox of §7 stated on the other side of the same
equality: shrinking the reader by k and facing it at a list of S = N/k are the same thing near the
focus, and they differ only at the rim, where the first keeps every record on the arc with the far
ones starved of it and the second keeps the arc for the window and sends the remainder past the
horizon entire. Either spends the radius; the drill-down of §9 is the second.

**And the window may not leave the list.** That second law is what lets one coordinate do two jobs
without a mode. At full radius S is N, the window is pinned to the whole list, and the angle names a
record absolutely: the feet are the first and last records, the middle is the middle, and the
tangent spreads the rest between them. At any smaller radius the window is free, and it re-centres
on the record already under the needle, so **the radius changes the scale and never the record**.
Nothing switches between the two behaviours. The clamp is the switch, and it is the same clamp that
keeps a window inside its data at every level.

**The angle cannot be a position of the hand, and a surface that makes it one is no better than
linear panning.** It is tempting, once a reader is two numbers, to lay them on any surface with two
directions — a touch pad, with the angle up and down and the radius across; or a scrollbar, carrying
the two by turns — and let where the hand is be where the reader points. Both were built, and both
fail in the same way, for a reason that has nothing to do with how the surface is drawn. A position
control gives every place on it a fixed share of the window, whether that share is spread evenly or
by the tangent; so the hand's tremor is a tremor in the record, a record cannot be held still while
the list is examined around it, and the horizon can only be *arrived at*, by moving the hand to the
edge, never approached. Spread by the tangent, such a surface is linear panning with the pixels
rearranged — finer in the middle, coarser at the edges, the same reach in total. The scrollbar is the
one-dimensional case of the same thing and inherits it whole; giving it a second degree of freedom
buys the radius and nothing else. Neither can carry the fisheye. The fisheye is not a way of spreading
a window under a finger; it is a way of approaching a horizon, and approach is a rate.

**The fisheye requires a rate, and a rate toward a horizon requires rapidity.** So the dial has two
needles. The gold needle is the hand. Its angle is a rate, and the rate follows the tangent: nothing
at the apex, so the reader can be held exactly still; barely anything just off it; gentle out to 45°;
hard toward the horizon. Let go and it springs back to the apex. What it adds while held is not a
speed but a *rapidity* ζ, at tan θ per unit time. The blue needle is where the reader points. Its
angle is the gudermannian of the rapidity — sin θ = tanh ζ — so it moves toward the horizon for as
long as the hand pushes and never reaches it, and when the hand lets go it stays. The value is read
off the blue needle through the fisheye: the window's centre plus half the window times tan θ,
normalised so that the horizon is the window's end. Near the apex the value barely moves; at 45° it
has covered a few percent of the half-window; it reaches the end only as the needle reaches the
horizon. At full radius the window is the whole list and the blue needle is an absolute place on it —
the arc is the dataset; at any smaller radius the window sits where the last click put it. A click
re-centres: the radius is set where the click lands, the window is put on the record under the blue
needle, and the blue needle comes home; a press that pans is the gold needle and leaves the radius
alone. The radius remains the gain, and the two laws above are untouched.

This is the speed-of-light dial, and not by analogy. Write θ for the blue needle's angle: sin θ = β,
the speed as a fraction of the limit; tan θ = sinh ζ = γβ, the celerity, which is what the value
reads; sec θ = cosh ζ = γ; and ζ = artanh(sin θ) is the rapidity. The horizon at 90° is the speed of
light, and the gudermannian is why the needle approaches it for ever: no finite rapidity reaches it.
The gold needle is proper acceleration, and rapidity is what proper acceleration adds linearly in the
mover's own time. The reason the mechanism has to be this one is the reason physics needed it:
quantities bounded by a limit do not add — a hand adding *speed* at a constant rate reaches the limit
in finite time and must be stopped by a wall, and a wall is where a control locks. Rapidities add,
and a control that accumulates rapidity needs no wall, because the limit is at infinity in the
quantity the hand actually moves. The only cap left is the rim's last pixel, and a push held past it
piles up nothing, so the way back is as short as the way out. Everything the paper has said about the
lens — the fulcrum at 45° where β = 1/√2 and γ = √2, the half of the list in the window, the horizon
that is never removed but only positioned — is the same set of facts read off this dial.

**The mathematics that makes it work is short, and every step of it is used.** Take the limit as
the unit, so speeds are numbers β in (−1, 1). Two speeds along a line do not add; they compose by
Einstein's rule, β = (β₁ + β₂)/(1 + β₁β₂), which is what keeps the result inside the limit. That rule
is the addition formula for the hyperbolic tangent — tanh(a + b) = (tanh a + tanh b)/(1 + tanh a
tanh b) — so if every speed is written as β = tanh ζ the rule becomes ζ = ζ₁ + ζ₂. **The rapidity ζ
= artanh β is the quantity in which speeds add**, and it is unbounded: β → 1 is ζ → ∞. A body pushed
with constant proper acceleration *a* gains rapidity at a constant rate in its own time, dζ/dτ = a,
so ζ = aτ and β = tanh(aτ): it approaches the limit for ever and never reaches it. Push on *speed*
instead, dβ/dt = a, and β reaches 1 at t = 1/a — in finite time, at a wall. That one difference is
the whole reason the dial's hand adds ζ and not β: a control that accumulates a bounded quantity
must be stopped, and a control that is stopped locks at its stop.

The dial angle is the way of drawing a rapidity on a half-circle so that its limit is a place on the
rim. Define θ by sin θ = tanh ζ. Then cos θ = √(1 − tanh²ζ) = 1/cosh ζ, and tan θ = sinh ζ. The
map ζ ↦ θ is the gudermannian, gd ζ = arctan(sinh ζ) = arcsin(tanh ζ); it carries the whole real line
onto (−90°, 90°), so the unreachable limit ζ = ∞ becomes the foot of the arc at 90°, reachable to
look at and never to land on. In the physics γ = 1/√(1 − β²) = cosh ζ, so sec θ = γ, and tan θ =
sinh ζ = γβ is the *celerity* — the momentum per unit mass, the spatial component of the four-velocity,
the quantity that grows without bound as β creeps toward 1. **Reading the value off the blue needle
through the tangent is therefore reading the celerity**: the fisheye's tan θ and relativity's γβ are
the same number, and the fisheye's horizon and the speed of light are the same place. At 45° they
give β = 1/√2, γ = √2, γβ = 1 — the fulcrum, where the value equals the rapidity's own unit — which
is why "gentle until 45°" is not a tuning but where the curve turns over.

The gold needle uses the same curve once more. Its angle θ_g is the hand's, and what it adds per unit
time is tan θ_g · κ of rapidity: nothing at the apex, κ at 45°, unbounded toward its own horizon. So
the hand's angle is itself a celerity — a proper acceleration read through the same tangent — and the
whole dial is one function, the tangent, applied three times: to the hand for the rate, to the reader
for the place, and to the place for the value. The window's scale is the only free number, and it
is the radius. Nothing in the chain is a choice about how browsing should feel; it is the unique way
a hand pushing at a finite rate can carry a reader toward a limit it must never reach, and physics
had it written down a century before there was a list to browse.

**A boundary belongs here, because the coordinate does not settle it.** This lens is for browsing,
not for addressing. If the index is already known, the tower of §9 beats it outright and does not
need it: give each decimal place its own rung — twelve rungs for a trillion, ten directions each —
and the places may be set in any order, none disturbing another, the last as easily as the first.
Reduced to its plainest form the number *is* the ladder, and nothing in that is a fisheye. The lens
is for the other problem, the one an address cannot express: when what is wanted is something that
would be recognised rather than something that can be named, and the neighbourhood must be visible,
the whole still in view, and detail where the eye is. **An address is reached by its digits; a place
is found by looking.** The step-7 schedule above quietly assumes the first, since it computes the
distance to the target; what the lens offers, and what no ladder of digits gives, is the second.

The pair of steps is the whole browse, and it terminates:

    while the radius is not zero:
        k ← 1 / tan(distance to the target)          # gear to what remains
        turn the focus until the target is centred   # the same step, every time
    # the radius is zero: the reader is a point, and the point is the destination

Note what the loop tests. Not "is the target close enough", which would need a tolerance chosen from
outside; the radius *is* the distance, so **arriving is the radius reaching zero**, and that is a
definition rather than a threshold. At radius zero the reader has no rim to spend: no other element
has any share of it, every one of them is at the horizon, and the reader is a point standing on the
element it was looking for. The destination is not a place the reader has moved to. It is the reader,
collapsed.

Each pass multiplies the remaining distance by twice the screen's grain, so the number of passes is
the logarithm of N to base 1/2g — a thousand in two, a billion in four, a trillion in six — and the
*step* never changes with N at all. Only the radius does.

**And written as a recursion, the same collapse is the base case.**

    find(reader, target):
        if reader.radius is zero:  return the element it stands on
        k ← 1 / tan(distance to the target)         # gear to what remains
        aim the focus as well as the rim resolves
        return find(the smaller reader, target)

**And the schedule does not depend on the lens.** The fisheye's resolution falls as one over the
square of the distance from the focus; other lenses fall otherwise — the eye's cortical
magnification falls as one over the distance, a soft window falls like a Gaussian, a crude one is a
box that sees everything inside its edge and nothing beyond. State the rule in the lens's *own*
terms — hold the target where the lens has fallen to half, shrink as it closes, stop when the radius
is zero — and the shape cancels: at that half-point every lens resolves at half its own centre
value, so every step leaves twice the grain times what remained, whatever the falloff. Measured on
all four, the step counts are identical to the digit: four, eight, twelve and seventeen calls for a
thousand, a million, a billion, a trillion at a coarse grain; one, two, four and five at a fine one.
**The collapse is a schedule, not an optics.** The fisheye is the lens this paper is about; the way
of arriving would work through any of them.

The recursion is worth writing out because it says what the browse *is* when nobody is watching it. The
recursion is a search, and which search is set by nothing but how finely the reader's rim can be
read. A reader that can only say *which side* — a quarter-radian rim, g = ¼ — halves the distance
each call, so the base is 2 and the count is log₂N: eight calls for a thousand, twenty-eight for a
billion, thirty-eight for a trillion. **That is binary search.** A reader with a fine rim says
*where*, not merely which side, and the base rises with the resolution: at a milliradian the count
is five calls for a trillion. **That is interpolation search.** A caution on how far this goes: the
counts above come from the aiming model of this section — that a reader lands within its own rim's
resolution — and not from a theorem about either algorithm, so the defensible claim is that the
collapse generates a *family* of searches whose convergence factor is the observer's resolution,
with the side-only reader at one end of it. Within that family they are not different algorithms;
they are the same collapse at two grains, and the constant that separates them is
the one the geometry already had — how much of its rim the reader can resolve. What is common to
both, and what neither usually states, is the base case: the recursion ends when the radius is zero,
and a zero radius is exactly one element.

Two properties of the inverse are worth stating rather than hiding. It is *lossy*: an arctangent of a screen position must be clamped and rounded, because infinite positions have to land on finite indices and the real line does not embed in the integers. The forward direction is exact; the return is quantised. And the visible arc must be capped at one turn: a wide view over few elements asks for several laps of the ring and names the same element once per lap, and the deduplication that follows flips between occurrences mid-turn. One lap is all there is to show.

**Cost.** Two arctangents to find the arc, independent of N. K projections and K reads to fill it. Nothing walks the array. A recordset of a trillion magnitudes is browsed, end to end and round again, with the same dozen operations per frame as a list of twenty. **Browse a trillion by angle. Render K by index.** And the array may grow while it is being browsed — appended to without bound — because the semicircle absorbs growth as density: the expression from angle to index is unchanged in form, the window is unchanged in angle, and an element the reader means to keep in view is kept by its index, its angle re-derived as N grows.

**Essentially, that is what the whole construction is: the fisheye lets you browse linear data with angles — and because circles get denser rather than larger, data that is infinitely large and still increasing, with a fixed angular expression.** And it takes two numbers, not one: **a turn of the circle and a shrinking of it** — the first moves the reader, the second decides how much of the list a turn is worth.

## 9. The angle, in rungs

> **(1 Oct)** R77 keeps the two infinities apart: the far point along the road is the vanishing point, at home; "the horizon" is the reading's infinity at the sides. The working horizon is the front side, home to the corner (R149). The speed comparison with a hash map is engineering framing, outside the paper's scope since 27 September.

The angle browses the array. What the angle is *made of* is the other half of the corpus — the register's rungs, a rung being one doubling of the reading — and putting the two together says something about detail that neither says alone.

Read the Cauchy in rungs. Take u = log₂ of the reading, and the fisheye's density becomes a sech: symmetric about rung zero, which is where the reading is one — the fulcrum — and falling by exactly one half per rung on either side. That is the recurrence ladder The Cauchy finds in its §7 — each recursive fulcrum halves the share still outside it, and the fulcrums sit log 2 apart — stated as a shape: **in rungs, the fisheye is a pyramid of halvings with the fulcrum at its peak.** The side toward home and the side toward the horizon are mirror images in rungs, which is the exchange's reflection about the centre, drawn.

Now read the fisheye in rungs. The k-th element from the focus has reading ≈ kπ/N, so its rung is ≈ log₂ k plus a constant: **the rung of an element is the logarithm of its distance from the focus, counted in elements.** Each rung outward spans twice as many elements as the one before — the nearest alone at the deepest rung, then one, then two, four, eight. That is an octave pyramid, the structure a mipmap has, and the fisheye's angle is what indexes it. The angle says *where*; the rung says *how much*; and the fisheye is the distribution that makes uniform-in-elements come out as halving-per-rung, so the two coordinates agree.

The Relation Space's two regimes fall onto the screen, and they are §7's two halves of the semicircle. Below the fulcrum — the inner half, reading under one, negative rungs — the *element* is the unit: individual items at natural spacing, the proportional side, the window. Above the fulcrum — the outer half, the long tail — the *octave* is the unit: aggregates, counting in doublings, the logarithmic side, the context. The unit changes hands at the fulcrum exactly as that paper says, and the fulcrum sits a quarter-turn from the focus — N/4 elements out, a quarter of a million on a million — which is the fisheye's quartile landing where it must: the fulcrum is the upper quartile of the arrivals, and on the array it is the quartile of the elements. So the visible window lives entirely in the proportional regime and everything beyond it is the logarithmic one. The window is the individuals; the context is the octaves. And at zero rungs everything reads as one — the unit circle — which is the placeholder for context too far to resolve: as the level-of-detail work found, not a crude answer but the absence of one, wearing the one shape a reader can still name.

And the rungs are fixed angles, independent of N, because the rung of an element is log₂ tan of its angle from the focus and that depends on the angle alone. Rung zero is at forty-five degrees; rung one at sixty-three, two at seventy-six, three at eighty-three, closing on the horizon at ninety; rung minus one at twenty-seven, minus two at fourteen, minus three at seven, closing on the focus at zero. Each rung inward halves the angle; each outward halves what is left to the horizon. Add a trillion elements and not one of these marks moves. **The pyramid is orthogonal to the index exactly as the angle is**: N sets only how many elements each rung holds — doubling from rung to rung while far from the fulcrum, levelling off as it nears (the two rungs that flank 45° hold the most, and equally, since they are mirror images about the fulcrum), and halving after, toward the horizon.

Detail, then, is in the rungs twice over. The register's rung *count* is how much detail there is — a finer register resolves a finer figure, and at one rung every figure is the unit circle. And in the fisheye the rungs also become *position*: the fine rungs are spent nearest the focus and the coarse ones furthest away. The fisheye's "detail is spent where the eye is" stops being a property of the view and becomes an instruction to the renderer: draw each thing at a level of detail set by its rung from the focus — full detail at the focus, one rung less per octave outward, a unit circle at the edge — and beyond the window draw not elements but octaves, the k-th rung outward showing 2ᵏ elements as one. A window of K elements is log₂ K rungs deep. The whole way to the fulcrum on a trillion is about thirty-eight. **Browse a trillion with forty rungs.**

Put shortest: **the level of detail is the long tail of the fisheye.** In rungs the tail is a straight exponential — half the share beyond each rung, forever — and a structure that halves at every step is self-similar under doubling, which is exactly what a level-of-detail ladder is: every level is the level below it, twice. The window's pyramid toward home is that tail read inward, its mirror image under the exchange, since the reflection about the fulcrum turns rungs toward the horizon into rungs toward the focus. And the fisheye's missing mean is the same structure once more: each rung outward holds half the mass at twice the magnitude, so every level contributes equally and there are infinitely many of them — the mean grows as the logarithm of how far one looks, which The Cauchy measured, and which is nothing but a ladder of equal weights with no top. The fisheye has no mean because it is a level-of-detail pyramid with infinitely many equally weighted levels. The tail, the ladder, and the missing mean are one thing.

None of which contradicts §§2–4, and the section must say why, because it looks as if it does. *Level of detail* has two nouns, and the fisheye supplies only one. It supplies the **levels** — the ladder, the fixed angular marks, the halving per rung — and it supplies them identically for every figure, because they are a fact about how the turn was met and not about what was met. It supplies no **detail**: the reach cancels in every reading, and there is nothing in the ratio to resolve at any rung, as the level-of-detail work found before this paper did. So the fisheye is the scaffold with nothing standing on it, and what stands on it is the array's, by index — §8 once more. The two halves fit for the reason §4 gave: the ladder is universal, the same marks for a clover as for a circle, *precisely because* the shape was thrown away. Had the ratio kept the figure, the ladder would have varied with the figure and could not have been an address. The loss of shape is what makes the levels a fact.

Which raises the natural question: if the fisheye supplies only the levels, what content fits them? Compare a figure's detail per level with the tail's weight per level and the answer is measured. The tail weighs every level the same — mass times magnitude per rung is flat out in the tail (1.50, 1.54, …) and vanishes toward home, which is the missing mean living past the fulcrum, as The Cauchy found. A smooth figure does nothing of the kind: an egg has all its detail in the first harmonic octave, a clover in the third, a star in the fourth, a burr in the fourth with a fifth of an octave and a twentieth trailing after — one or two levels filled and the deep ones empty, which is why a smooth shape collapses to the circle so quickly at a coarse register. But a rough figure — a cog whose bumps fall off as one over frequency, the spectrum natural signals tend to have — puts nearly equal energy into every octave (1.00, 0.83, 0.76, 0.73, 0.71, 0.70, 0.70, 0.70, 0.69) and fills the scaffold level for level. Equal energy per octave is the tail's equal contribution per rung, and the logarithmically divergent total of such a signal is the fisheye's logarithmically divergent mean. **The tail is shaped like natural detail.** Smooth shapes are poorer than it; a natural signal is its equal — so the levels the fisheye offers are exactly the levels natural data has, and one can keep zooming and keep finding detail as far as the tail goes. This is a comparison of two spectra octave by octave and is graded as that: a structural match with a measurement behind it, not a derivation.

**An application: drilling down by list size.** The natural zoom for a fisheye is not a change of item width but a change of *list*. Let the semicircle always span the S elements around the focus, and let S be the zoom: shrink it and the same angular expression browses a smaller neighbourhood, with the element you were on staying in the middle. Each halving of S is one octave down a tower of fisheyes on one list, and a single element of a billion is thirty halvings away. The window is the invariant of the whole tower — the same few dozen individuals at the same spacing at every level, a turn of one element per item-width everywhere — and only what lies *beyond* the window changes meaning: the rest of a billion at the top, the rest of a few dozen at the bottom. That is "detail is spent where the eye is" in its cleanest form: the eye's window never changes; the levels do. And a drill can be made exact by taking the next level's list to be this level's window — S becomes K, *the K of the previous fisheye is the N of the next* — which, repeated, is a geometric descent (63, 40, 28, 21 …), because a window is an arc of the semicircle and is never the whole of it until the list is a handful. The tower draws itself: the whole list as the outer semicircle, each level's sub-list as an arc nested inside it, all of them centred on the one focus.

Geometrically it is §7's picture nested: each level is a circle touching its parent at the parent's focus,
and drilling multiplies the radii. The same construction runs across a hierarchy rather than down one list. Let the elements of a fisheye be lists — games of positions, folders of files, years of days — and give each visible element an inner fisheye over its own list, its window K set by the outer rung: the full register at the focus, halving per octave out, one element at the far rung. Then what the outer fisheye stores as a *magnitude* is the inner fisheye's *rung count*: what is detail at one level is levels at the next, and a place in the hierarchy is a tuple of angles, one per depth. The nesting is native to the object — the Cauchy's tail is itself a Cauchy, which is what the recurrence ladder said — and it has a two-dimensional form: a fisheye of fisheyes laid side by side rather than stacked is a semicircle by a semicircle, a table browsed by two angles.

**An application: the calendar tower, and what fixes an address.** The tower raises a question the
drill-down does not: can the angles *be* the id? A dotted list of angles — 30·45·65 — resolves to an
object in one multiply and one array read per level, no table and no search, and a million such
lookups ran seven times faster than a hash map keyed by strings. But an angle derived from a count is
a place, not a name: the element a third of the way through a level sits at 30.334°, and it sits
somewhere else the moment the level grows. So a derived angle cannot be an id, and the fix is to stop
deriving it. Give every level a *fixed pitch* — a fixed number of directions, whatever the level
happens to hold — and an element's angle is the slot it occupies, an integer, static forever: growth
fills empty directions, and a full level opens a slot into the next level down. That is positional
notation with a fixed radix, which is exactly what makes digits stable; assigning slots by arrival
gives a positional id, and assigning them by the id's own hash gives the hash-array-mapped trie, the
angle of an angle with a hash supplying the digits. The cost is the radix trie's: unused directions
are held empty.

The instance everyone already uses is a timestamp. Years, months, days, hours, minutes, seconds are
levels of fixed pitch — a century of a hundred, twelve, thirty-one, twenty-four, sixty, sixty — and
2026·9·3·14·30·15 is a dotted address of directions that names the same second forever, because
nothing in it was ever derived from a count. September is the ninth direction of twelve in any year.
The only growing level is the top, and it grows at the end, which is the one kind of growth an angle
never minds: *now* is the head reader, a place at the end of the year level, following the growth for
free. And each level is a semicircle of its own, browsed *separately*: turn the month and the day
level redraws for that month while the day and hour already set stay where they are; a clock face was
always a fixed-pitch level drawn as a circle with the focus as its hand. On the bench, a log of twelve
thousand entries placed by timestamp grew by six hundred with no address changed, and the tower
counted the entries at every depth of one address — year, month, day, hour, minute, second — which is
what a tower is for.

**An application: a century of milliseconds.** A worked instance is worth the space, because it shows the two halves of this paper meeting on one screen. Take the list to be the milliseconds of a century — 2000 to 2100, three million million of them — and browse it with the one dial of §8: a semicircle, a needle whose angle is the place, and a radius that is the scale. At full radius the arc is the century itself, its feet the first and last millisecond of it; at nine tenths of the radius the arc reaches a year and a bit, then six days, then two hours, then a hundred seconds, then a second, and at the last a millisecond or two — each level centred on the millisecond the level above it left under the needle. The date is not a control anywhere in it. It is what the index *reads as*, computed from the offset as it is drawn, and the fields and dials of a calendar never appear.

That arrangement answers a question a tower of named levels has to work at: the twenty-ninth of February. Given the day as a field of its own, that level must change length with the month — twenty-eight, twenty-nine, thirty, thirty-one — and a day already chosen must be clamped when the month beneath it grows shorter. Given one flat list of milliseconds, none of that exists: the list is uniform and the irregularity lives entirely in the reading, so it cannot produce a state that is wrong. Index 762,523,200,000 reads as noon on the twenty-ninth of February 2024; the same arithmetic says 2100 has no such day; nothing had to be arranged for either. **Milliseconds do not have leap days; calendars do.** Where the levels are named and regular, the tower is the better instrument and the lens is not needed — but where they are irregular, the flat list with a lens over it is at once simpler and harder to break.


**And the general form of it: find the quantum, and the rest is a reading.** The calendar's
millisecond is not special. A quantum is whatever the data is *stored in units of*, and an array
supplies one by construction — its index. So the recipe is short: take the finest unit the situation
already has, count it, lay the count on the semicircle, and let every name above it be a reading of
that count rather than a level of structure. What that costs is remarkably flat, because the dial
crosses decades and domains do not have many:

| the situation | its quantum | how many | decades | passes at the dial |
|---|---|---|---|---|
| a century | millisecond | 3.16 × 10¹² | 12.5 | 5 |
| the human genome | base pair | 3.1 × 10⁹ | 9.5 | 4 |
| the IPv4 space | address | 4.3 × 10⁹ | 9.6 | 4 |
| a day of a busy log | a line | 4.3 × 10⁸ | 8.6 | 4 |
| a music track | a sample | 8.6 × 10⁶ | 6.9 | 3 |
| all of Unicode | a code point | 1.1 × 10⁶ | 6.0 | 3 |
| a novel | a character | 5 × 10⁵ | 5.7 | 3 |
| a film | a frame | 1.7 × 10⁵ | 5.2 | 3 |

Twelve decades and five decades are two rungs apart. **The size of the thing barely matters**,
which is the practical content of an angle being orthogonal to a count.

The condition that does the work is not the quantum, which the storage gives you, but the **order**.
The list must be laid in an order whose adjacency you actually care about, because the lens's whole
offer is the neighbourhood: what is near the thing you are looking at. Time has such an order and so
does a genome and so does a novel. A frame of video has a perfect quantum — 8.3 million pixels — and
no such order: laid row by row it gets a total order that destroys half of the adjacency that
mattered, since the pixel above is now a screen-width away. A collection of documents has no natural
order at all; one can be imposed by hashing, and then every element has a name and nothing has a
neighbour. **The quantum is free; the order is what must be earned.**

**And a list that factors does not need a lens at all — it needs one arc per factor.** A reader takes
one angle per dimension: time is one dimension and gets an arc; hue against shade is two and gets a
dome, the semicircle by a semicircle of §9. Colour in its three channels is three, and three angles
do not fit on a dome — but they do not need to, because each channel is only 256 values, two and a
half decades, and a reader that lands within a third of a per cent of an arc buys that in one turn.
Three uniform arcs, three turns, exact. A lens across them would buy crowding at the ends and
nothing at the middle. **The lens earns its place by decades**: below about three of them uniform
pitch wins, which is why the calendar's month arc should stay uniform and the century arc should not.
Sixteen million colours sounds like a case for the lens and is not, because the sixteen million
factor into three small axes — and factoring is exactly what removes the need.

That example carries three properties at once and it is worth saying which of them is doing the work,
because the wrong one is the easier reading. A channel is **bounded** — every address known, nothing
still to arrive. It is **factored** — three axes rather than one. And it is **few decades** — 2.4 of
them. Only the last is the criterion. Boundedness is irrelevant: a century of milliseconds is bounded
in exactly the same sense, fully defined with every address known, and it wants the lens badly at
3.16 trillion. Factoring matters only because it cuts decades — three axes of 2.4 in place of one of
7.2 — and a single axis of a million is just as finite, just as fully defined, and cannot be indexed
by hand at all.

And declaring a range does not abolish the horizon, which is the tempting conclusion and a false one.
Run the tangent over 0 to 255 and the horizon is exactly where it always is, with the last values
crowding toward it; the lens never consults the range. What has happened is that the window is wider
than the data, so nothing is *sent* past the horizon — the horizon is still there and has been made
irrelevant, which is a different thing from being removed. **The lens is a device for spending
attention across decades. Where there are few decades, spend none.**

The general form is worth stating, because both moves are legitimate and they are the same move.
**The horizon is never removed, only positioned.** It belongs to the coordinate rather than to the
data — the tangent diverges at a right angle whatever list it is pointed at — so nothing done to the
data can abolish it. What can be done is to place it. Bound the data small enough and the horizon
falls *outside* what exists: still in the coordinate, still exactly where it always was, and with
nothing out there for it to hold. That is what a definitional range buys, and irrelevant is all
anyone ever needed from it. Or leave the data alone and shrink the radius, and the horizon comes
*inside*, holding more and more of what exists until it holds all but the element under the focus.
Those are one dial turned in opposite directions. In neither case is anything lost: the elements past
the horizon are ordinary elements at their ordinary addresses, and what has changed is only how much
of its rim the reader is spending on them. **Nothing is removed by being unattended.**

**And the oldest instance of all of this is a picture of a road.** Stand beside a straight road at a
perpendicular distance h — the standoff, and the only length in the construction — and the post at
distance x along it stands at the angle θ from the foot of the standoff with tan θ = x/h. That is
this paper's map with its two sides renamed: the reader's unit is the standoff, the corner at 45° is
the post one standoff along, and the direction parallel to the road, which no post ever occupies, is
the horizon. It is the vanishing point. Looking down the road instead of across it puts the same map
on a picture plane — a point at depth Z lands at f·h/Z, the perspective divide — and the ladder falls
out identically: the posts at 1, 2, 4, 8, 16 standoffs land at 45°, 63.4°, 76.0°, 82.9° and 86.4°,
each one halfway from the last to the vanishing point. A road of evenly spaced posts is a uniform list
seen through the lens, and the crowding at the horizon is the same crowding, for the same reason.

Three things follow that are worth having. The vanishing point holds no data: every line parallel to
the road meets it, so it names a *direction* rather than a place, which is the projective point at
infinity and the cleanest possible case of §7's claim — nothing stands there, and nothing ever
arrives. The horizon line of a picture is the whole address space of directions, the dial drawn on a
picture plane. And the perspective divide is not an analogy for the lens but an instance of it, which
means the nineteenth-century projective geometers were working this same relation from the
picture-plane end, before there was a reader to put at the focus.

## 10. Two fisheyes on one list

> **(1 Oct)** Each fisheye is already a view from somewhere (R146); two of them are two situated readers.

Everything so far is one lens. Put two on the same list — each with its own focus, its own item width, its own pixel grain — and ask what they can do for each other. The answer has a structure, and it was measured on a bench built for it.

Two fisheyes on one list are two Möbius charts of one line. Element i sits at tan(θᵢ − φ₁)·s₁ in one and tan(θᵢ − φ₂)·s₂ in the other, and those two maps are related by a linear-fractional transformation, since tan of a shifted angle is linear-fractional in tan of the angle. So the invariance sheet of the series applies verbatim. Screen positions do not transfer between them — the same two elements sat 96 pixels apart in one view and 48 in the other — and pixel distances, focus and aperture are private. The cross ratio of any four elements' positions is identical in both, to floating precision, for any pair of foci and widths whatever.

**Three shared elements fix the whole relationship.** A projectivity of a line has three degrees of freedom, so once the two views agree on three landmarks, each can predict where *every* element lands in the other: an element's cross ratio against the landmarks, read in one view, solved in the other. On the bench, twenty-six shared elements were predicted to 0.000 pixels with the grain off, and to the grain with it on. This is the line's version of what the companion paper calls transfer, and it is cheaper in every way — three elements rather than seven, no ambiguity, no third party. Two fisheyes that have shared three elements know each other completely, with no shared scale, zoom or origin. One number sent from one view — the cross ratio against the frame — lands on the same element in the other, and it works for elements the sender cannot see; the receiver turns its focus until the element with that address is centred. The one condition is that the frame be in view in both: zoom past it and there is nothing to measure against, which gives shared addressing a zoom range — bounded below by the frame's visibility and above by its separation.

The grain prices it, and the price came out in two laws where one was expected. At a pixel grain the *address number's* relative error follows one over the frame's separation — 22.2, 11.1, 6.1, 3.0, 1.6 and 0.85 per cent at separations of 1, 2, 4, 8, 16 and 32 elements, against the survey's 21.4, 12.9, 6.7, 3.2, 1.7 and 0.87 for the same law measured in rungs — an independent reproduction. But the *recovered element's* error is flat in separation and set by the grain alone, about 0.12 elements per pixel, because solving the address back to a position has a sensitivity that grows with separation and cancels the address's shrinking error exactly. The wall stands: a frame narrower than the grain gives no address at all.

**A fourth shared element is an audit.** Its cross ratio must agree in both views, or one chart is not Möbius. On the bench, a quadratic warp applied to one view's chart displaced its shared elements by barely a pixel — 1.1 pixels at the median, 1.55 at most — which the eye would never catch, and moved the fourth element's cross ratio from zero to 0.93. Two fisheyes detect a broken chart; they cannot say which of them broke. A third would. And the audit separates the two things a single fisheye cannot tell apart: when the *list* changes — an element written, its magnitude bumped by half — both views change and the cross ratio holds; when a *chart* changes, one view changes and the cross ratio fires. The data moved, or I moved: one lens cannot say, two can.

**Two grains beat one, by more than they should.** Locate an element by sending its address in both directions — from the first view solved in the second, and from the second solved in the first — and average the two estimates. At a one-pixel grain the median error falls from 0.107 and 0.127 elements alone to 0.047 together, a gain of 2.3 to 2.7 times where two independent errors would give 1.4. The excess is measured: the two directions' errors are anticorrelated, −0.72, because each view's quantisation enters the two estimates with opposite sign and the average cancels it to first order. The exchange of roles between sender and receiver is an involution, and its fixed point is the error-cancelling estimate — the series' swap, put to work.

**And a wide fisheye is a narrow one's context.** Two apertures are two rungs of the pyramid of §9, and the wider view already holds what the narrower view would show beyond its window: the octaves. Drawn beneath each window as one bar per rung — the octave's mean magnitude and its spread, an O(1) summary from prefix sums built once — the counts per octave on a list of five thousand read 25, 50, 98, 192, 348, 512, 513, 348, 192, 98, 50, 25, 12: doubling outward, peaking at the two rungs that flank the fulcrum, halving toward the horizon. The sech of §9, on a screen.

The scope is exact. One list is one line, and no number of fisheyes on it buys a standpoint or a plane — that requires the list to have a second dimension behind it, which is another paper's subject. What two fisheyes share is the levels: the same angles, the same rungs, the same invariants. What stands on the levels is the list's, and the list is one.

## 11. The same lens, under other names

One more thing is worth recording, because it bears on how this paper should be read. The object it
describes has been found repeatedly, in fields that do not read each other, and named after whatever
was at hand each time. None of what follows is new here; all of it is standard in its own discipline.
What is not standard is the observation that these are one map.

The map is: an angle, its tangent, and a scaling — $\tan(\text{out}/2) = k\,\tan(\text{in}/2)$, the
Möbius maps of a line or a circle. Four of the identifications below were checked while writing this
section, and are marked; the rest are quoted from their own fields.

| the name it goes by | the field | what $k$ is there |
|---|---|---|
| **fisheye lens** | optics | the lens's angular compression |
| **fisheye view**, degree of interest | interface design, Furnas 1986 | how sharply attention falls off |
| **the Cauchy**, the Lorentzian, the Breit–Wigner line | statistics, spectroscopy | the width — *checked: the Cauchy is the tangent of a uniform angle* |
| **stereographic projection**, the planisphere | cartography, since Ptolemy | the sphere's radius against the plane's |
| **gnomonic projection** | cartography | the tangent plane's distance |
| **Möbius transformation**, the projective line | complex analysis, geometry | the multiplier |
| **relativistic aberration**, the headlight effect | special relativity | the Doppler factor $\sqrt{(1+\beta)/(1-\beta)}$ |
| **Bondi's $k$-calculus** | special relativity | $k$ itself — *checked: composing multiplies, and that is velocity addition* |
| **the true anomaly from the eccentric** | orbital mechanics, since Kepler | $\sqrt{(1+e)/(1-e)}$ — *checked: the same formula as aberration, with eccentricity for speed* |
| **Mercator's northing** | navigation, 1569 | *checked: $\ln\tan(45^\circ + \varphi/2) = \operatorname{artanh}(\sin\varphi)$ — Mercator's chart is the rapidity of the latitude* |
| **the bilinear transform**, frequency prewarping | signal processing | the sample rate — *checked: the prewarp is $2\tan(\omega/2)$* |
| **the Smith chart** | electrical engineering | the reference impedance |
| **the Cayley transform**, the Poincaré disc | matrix analysis, hyperbolic geometry | the disc's radius |
| **the hyperbolic browser** | interface design, Lamping & Rao 1995 | the disc again, as a control |
| **the half-angle substitution** | calculus, Weierstrass | nothing — the map without a parameter |
| **the vanishing point** | perspective drawing, since Alberti | the picture plane's distance |

One of those names deserves its own paragraph, because it is ours. The distribution called the
Cauchy was not discovered by Cauchy and was never mischaracterised by him; the story is stranger than
that. The curve was studied geometrically by Fermat in 1659 and later went about as the witch of
Agnesi. The first explicit analysis of the distribution's properties was published by Poisson in
1824, who noticed that the mean of such observations does not converge and did not think it
especially important. Cauchy's name became attached only during an academic controversy in 1853 —
and the controversy was not about this object at all: Bienaymé was attacking Cauchy's method of
interpolation and defending least squares, and the distribution entered as ammunition. **The name we
use for the coordinate at the centre of this paper is an accident of a quarrel about fitting
methods.**

Nothing said in that quarrel was false. The object has no mean, and everyone involved was right about
that. What happened was not error but **filing**: the thing arrived inside a dispute over error laws,
so it was entered into mathematics as a *distribution* — and a distribution is judged by its moments,
which is precisely what this one has not got. Two centuries of describing it by what it lacks
followed, and its standing job became the canonical pathology of a first probability course. Read
instead as a coordinate, the same object is a bounded observer's address into a magnitude list; the
construction *is* the ray at a uniformly distributed angle rather than a curiosity about it; and the
missing mean stops being a defect and becomes the statement the whole series has been making anyway
— **that direction was kept and magnitude was not**.

Three consequences follow immediately, and they are worth stating because each dissolves something
that has always been treated as a difficulty. **An address is not supposed to have an average.** The
mean of 10, 100 and 10,000 Main Street is not an address and its meaninglessness is not a pathology
of the street; nobody has ever thought otherwise about house numbers, and the only reason it seems
remarkable here is that the object was filed where averages are the point. **And the infinity belongs
to the chart, not to the thing addressed.** As the angle approaches a right angle its tangent
diverges, which is a fact about the coordinate at its boundary and not a claim that anything out
there is enormous; the elements near the horizon are perfectly ordinary elements, and what has grown
without bound is the number their address is written with. **And the cancellation was never a loss of
information in the first place.** The earlier result — that the magnitude cancels and only the ratio
survives — reads differently once the surviving quantity is an address: the reader discarded the
magnitude because it was never carrying the magnitude, only where, directionally, the magnitude sits
relative to it. What survives is exactly and only what an address requires.

The pattern in the naming is worth a sentence. Each field names the lens after its own instrument —
*fisheye*, *planisphere*, *Smith chart*, *hyperbolic browser* — or after what it seems to distort —
*aberration*, *prewarping* — or after the distribution it leaves behind — *Cauchy*, *Lorentzian*,
*Breit–Wigner*. Almost none of them name it after what it *is*: the way a bounded observer with an
angle for a coordinate must see an unbounded line. That is why the same object could be found a dozen
times without the finders meeting: a name taken from the instrument does not travel, and each field
was solving its own problem — Kepler an orbit, Mercator a course to steer, Bondi a light signal,
Furnas a screen too small for a file tree.

For this paper the consequence is practical rather than proprietary. The construction here is not
offered as a discovery; the arithmetic has been available since Ptolemy and the group since Möbius.
What is offered is that the same map, taken as a *reader* rather than as a projection or a
distribution or a chart, brings its own results with it — the fulcrum, the horizon's price, the
rungs, the composition law, the invariance of the cross ratio — and those results then hold in every
field on the list without being proved again there. **The lens has been discovered many times. What
has not been carried across is what it costs to look through it.**

## 12. What was actually impossible, and what was not

> **(1 Oct)** Both readers are in situation 3 and neither knows N; the parallel reader keeps v on the front side only (R152). Browsing an array whose N is known is a view from nowhere read through a simulated fisheye.

It is worth closing on the exact boundary, because the reveal is only as strong as the theorem it does not violate.

What is impossible, and stays so: recovering a magnitude from a reading. A reader with one slot, holding one arrival at a time and nothing else, has a direction and can never have the length behind it. The Cauchy proves this per arrival, to seven parts in 10¹², and the confound proves that not even the schedule can be trusted to smuggle it back. Every word of that stands.

What was never impossible: recovering a magnitude from the *list*, given a reading. That needs the list — the completed system, the page, the ground — which is exactly what the serial reader was defined as lacking, and exactly what a reader with a recordset has. The fisheye is the bridge between them. It serialises the reader's *view* of the list — K at a time, the focus in detail, the rest receding — while the list itself stays whole behind the lens. The reader still reads in steps, because it must; but the thing it steps through is finished, so any step can be answered exactly.

So the two results sit together without strain. The periodicity is the fisheye's, and it is clean because the magnitudes are gone from the reading — that is the mechanism of §4, untouched. The magnitudes are the array's, and they are retrievable because the Cauchy is a fisheye and a fisheye is a lens with an object side — that is §7. Both, at once, from one angle: the one the Cauchy kept.

It is worth adding what the boundary does not divide. The fisheye is not a serial thing or a parallel thing; it is the semicircle, and it serves both. Serially it is the *shape* of the arrivals — each reading is the tangent of an angle, so the data come with their angles, and a reader places each arrival on the semicircle as it lands, in a rung, on a side, in the window or in the tail, needing no count to do it. In parallel it is the *layout* of the array — each element is assigned an angle by its index. The machinery is the same in both, tan and arctan, the two halves, the fixed rung marks, the window as an arc, because all of it lives on the angle side and the angle is orthogonal to the count. That is why it works the same on a known array, on one still growing, and on a stream whose length nobody knows. What differs is only what stands on the angles: serially the reader has the levels and the address of each arrival and never its magnitude, which is §§2–4; with the array it has the magnitude too, by index, which is §8. The fisheye works equally well on serial and on parallel data — exactly true of the angles, and exactly false of what stands on them.

**And a uniform address space cannot report position at all.** Take a list every element of which
holds the same thing, lay it on the circle, and browse it: the view at one address is the view at
every other, so no amount of travelling changes anything the reader can see. Nothing is broken — the
addresses are all there, each distinct, each reachable — but the reader cannot tell them apart by
looking, and its position is knowable only from the address itself. This is the figure-blindness of
§11 arriving from the other end: there the reading discarded what stood at the address, here the
addresses hold nothing that differs. The consequence for anything built this way is sharp. **What
makes a list browsable is not that its addresses are distinct but that what stands at them is**, and
an address space whose contents are everywhere alike is indistinguishable, from inside, from standing
still.

It also settles what a finer grain on the reading is worth, once the magnitudes are gone. It buys
nothing about the circle — at every grain a reader of the ratio holds its own unit circle, and the
circle has nothing more to say — but it sharpens three things that are not magnitudes. **Finer
addresses:** each reading names a direction, and a finer grain tells more directions apart, which
alone is worth nothing and with the array behind it is the whole of this paper, because the address
is the one thing the array needs from the reading. **A sharper frame:** the fulcrum and the cross
ratio are located only as finely as the grain, and the geometry a reader can build on them sharpens
with it. **Sharper timing:** landmarks, turns and the period arrive as events and are placed more
exactly — the periodicity the fisheye contributes, and the one channel by which a shape reaches a
reader that has cancelled it, where the physics sets the schedule. A finer grain is precision about
where and when, never about what; the what is the array's, by index.

And there is one list for which even that distinction closes. If the data is the unit curve itself — every magnitude one, the circle — then nothing stands on the angles, because there is nothing to stand: **the angle points to the value on the circle itself**, the point at that angle, and address and content are one. On the unit curve the serial reading loses nothing, since it had no magnitude to lose; the census returns it because the reading is exactly consistent with it; and a level-of-detail ladder bottoms out on it because at one rung every reach reads the same. It is the fixed point of the whole construction — the one list whose reading is itself — which is why it is what a reader finds whenever the magnitudes are gone: not a guess about the list, but the list that the angles alone already are.

And the fixed point nests. A fisheye *of* the unit circle reads an angle whose value is itself an angle — the angle of an angle — so its elements can each be the focus of a further unit circle, and that one's elements of a further one: a tower of pure indirection, an address of an address of an address, with no magnitude at any level. That is a positional notation whose digits are directions. With N elements per circle a place at depth d is d angles; with two per circle it is the binary expansion, and the rungs are its digits. The data enters only at the bottom. The drill-down of §9 is this tower with one list underneath; the hierarchy is this tower with a list at every level; and the bare tower of unit circles is the coordinate system the two share — which is why browsing with angles is a coordinate system at all, and not a trick that happens to work.

Now say it without the rhetoric, because the paper has earned the right to be plain. **This is not a recovery of the Cauchy.** Nothing is recovered from the reading, and nothing here weakens the theorems of §§3–4 by a hair: the reading still carries no magnitude, and never will. Nor were the magnitudes recovered from anywhere else — they were never lost. The list was in hand the whole time. To call a lookup into a list you already hold a *recovery* would be a stretch, and the paper does not need the stretch. What the algorithm actually buys is narrower than a reversal of the theorem and a good deal more useful: **O(K) browsing of any array of data, using the fisheye** — a fixed cost per view whatever N is, the whole array navigable by turning one angle, and never a scan. That is the entire claim, and the title states it. The fisheye contributes the periodicity, exactly as the series says. The array contributes the magnitudes, because you kept it. And the fisheye is what lets a reader with a finite screen move over the one while the other stays whole behind it. None of that is serial observation, and all of it is the fisheye: what the series found as the shape of one reader's arrivals is a coordinate, a ladder, a common language and a fixed point, and the reading was the first of its faces rather than the whole of it.

The series' closing line was that the price is waived only by being handed the shape whole. It is — not by the reading, which cannot, but by the array behind it, which was there all along, and which the reading, being a fisheye, was pointing at.

## 13. How to browse without end

One sentence carries everything the paper found, and it is a set of instructions.

**Put the list on a semicircle, stand a smaller circle on it at what you are looking for, and shrink
that circle as you close.** Nothing else is needed, and each half of the sentence is a result rather
than a preference. The semicircle is forced: the Cauchy *is* the fisheye, so a list laid at equal
angles and read by the tangent is not a design but the distribution the series had already met. The
smaller circle is a reader, and every reader is one — touching at its focus, its radius its zoom.
The shrinking is the browse, and its rule is that the radius equals the distance, which keeps what
you are looking for exactly at the reader's fulcrum for as long as you are looking for it.

The instructions also fix their own mechanism, and it is not optional. Standing the circle at what
you are looking for is not pointing at it: a control that maps the hand's position to a place in the
list — a touch pad, a scrollbar, anything that makes the angle a position — spreads the window under
the finger and can do nothing else, and spread by the tangent it is linear panning with the pixels
rearranged. Approaching a horizon is a rate, and a rate toward a limit is rapidity. **The fisheye
requires the mechanism physics developed long ago for rapidity**: a needle for the hand whose angle
is a rate through the tangent, a needle for the reader whose angle is the gudermannian of what the
hand has added, and the value read off the second through the fisheye. Two needles and a radius —
the speed-of-light dial — and nothing that points.

What that buys is worth stating plainly, since it is what the whole construction was for. The
coordinate never rescales: an angle means the same fraction of a list of a thousand and of a
trillion, and a list that is still growing at its end changes no address it has already given. The
view costs a fixed number of reads — the elements in the window, and a logarithm of octaves for
everything else, so a view of a billion costs what a view of a thousand costs. The whole is never
lost, because the rest of the list is on the rim rather than off the screen; what a smaller radius
does is send more of it to the horizon, which is a decision about attention and not a loss of
access. And arriving takes the same step every time, at every scale — the target at 45° of rim,
turned to the middle — so the work per step does not grow with the list at all, only the number
of steps does, and that grows like a logarithm whose base is set by the grain of the screen rather
than by the size of the data. A thousand is two such steps; a trillion is six.

So the answer to the question the series left open is not a recovery and not a trick. It is a
posture, and it has an end condition that is a definition rather than a tolerance:
**arriving is the radius reaching zero.** Face the list from a circle small enough to steer, and let
the circle collapse as you close; when it reaches zero the reader is a point standing on one element,
and every other record in the list is at its horizon — still there, still addressable, and for the
moment none of your business. It is also where the nesting of §7 ends: readers compose by
multiplying radii, so a tower of them has a limit, and the limit is a point. **The destination is
not a place the reader arrives at; it is the reader, collapsed.** That is what it is to find one thing among any number of
things, and the fisheye has been telling us so since it was only a bad reputation with no mean.

## Where the numbers came from

A record for our own use, not a methods section. Every figure quoted above was produced by one of
these, and each is kept beside the paper so a challenged number can be re-run rather than re-argued.
Where a claim is a reading of an existing paper rather than a measurement, that is said instead.

| the claim | where it came from |
|---|---|
| a reader is a tangent circle; the radius is the zoom; tangency at the focus only | `tangent-semicircles.mjs` |
| the lens on a shape: cell width = unit × cos²α, measured 0.787 / 0.481 / 0.261 / 0.077 / 0.016 at 30°–85° on the front-half lens (0.785 / 0.478 / 0.258 / 0.070 / 0.010 on the earlier whole-turn map) | `reading-lens-cells.js`; earlier `second-standpoint-tests/test-cos2.js` |
| the front-half lens: the horizon lands at exactly ±90°, the home cell unchanged at 7.49°, the back half the plain reading, no jump at the horizon | `reading-lens-map.js` |
| the relative angle moves as the list grows: the 101st element at 70.66° of 256, 70.39° of 257 | arithmetic: 180·100.5/N |
| the home cell is the reader's unit at every count; the first mappings at ±½ unit; Shift+wheel doubles the leaves and the mappings | `second-standpoint-tests/test-unit.js`, `test-homecells.js` |
| the shape breathes 0.55×–1.45× and the addresses do not move | `second-standpoint-tests/test-breath.js` |
| the radius table — fulcrum, inner half, the last degree, at k = 0.05 … 100 | `what-the-radius-does.mjs` |
| every chart is rot · scale · rot; ×4 then ×3 = R/12; a pan turns the rim | `every-reader-a-circle.mjs` |
| the tower collapses; nesting off-focus needs the third number | `readers-of-readers.mjs` |
| the one-parameter family; the cross ratio constant along it; the three kinds | `readers-between.mjs` |
| k\* = 1/tan(π/2M); equal spacing wins 7–10×; a mixture is worse | `placing-readers.mjs` |
| the radius is the distance; each step multiplies by 2g; a fixed radius never arrives | `arriving.mjs` |
| records per degree of rim; the same 45° step at every scale | `the-radius-is-a-gearbox.mjs` |
| the recursion's step counts; the side-only reader at base 2 | `the-collapse-as-a-base-case.mjs` |
| the navigation dial: a gold needle adding rapidity through the tangent, a blue needle at its gudermannian, the value read through the fisheye, the radius by click | `fisheye-ladder.html`, `calendar-dial.html` |
| the collapse is lens-independent (Cauchy, hyperbolic, Gaussian, box) | `any-lens.mjs` |
| the eye's falloff is 1/d and not 1/d² — the profile does *not* transfer | `is-the-eye-a-fisheye.mjs` |
| two fisheyes on one list: transfer at three elements, the audit, the alignment detector | `two-fisheyes-core.js`, `multi-fisheyes-1-2.js` |
| the context identity to 1.1e−14, and the seam near the horizon | `multi-fisheyes-1-2.js` |
| the tower against a tree of nodes (objects, resolve, append) | `tree-vs-angles.js` |
| the √2 cascade, the walls r_k = √(2^k − 1), the spherical Cauchy | *read from the 2D paper's §4.4–4.5, not measured here* |
| Kepler's anomaly relation, Mercator's northing, the bilinear prewarp, Bondi's k | checked while writing §11; the identities are standard in their own fields |

Two cautions belong with the table. The step counts in §8 come from **an aiming model** — that a
reader lands within its own rim's resolution — and not from a theorem about search; they are a
property of this construction, not of binary search. And the interface figures throughout are
**geometry, not ergonomics**: what a turn of the rim is worth in records is computed, while what a
reader can actually land within is assumed at a third of a per cent of an arc and has not been
measured on anybody.

---

*The reader, the relation space, the fulcrum and the horizon, and why observation comes in steps: The Relation Space, §§1–5, 9–10, 20. The six constituents, the parallel/serial purchase, the asymmetric passage as a Cauchy-distributed sequence: What a Relation Is Made Of, §§8, 12, 14. The register, the rungs, the fulcrum located by counting, the samples-per-cycle result and its exactness caveat: The Unit Rule, §§4–5, 14a, 17–18. The circle serialised, the cancellation and its mechanism, the missing mean, the confound, the trade and the centre of gravity: The Cauchy, §§1–7, 11, 13, 14b–15. The recurrence ladder: The Cauchy §7. The level of detail as the register's step and the unit curve as the coarse limit: the rung arc's bench pages, "the figure, rung by rung" and "where the geometry goes". The expensive way back for a reader that can move: The Reach.*
