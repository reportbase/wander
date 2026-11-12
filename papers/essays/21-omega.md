# Omega: the sweep's total, given its own name

*The twenty-first of a series of essays on what can be known from where one stands. Draft, 12 November 2026. A thought
experiment, kept beside* Reads and Writes *and changing nothing in it: write Ω for the total of one sweep, the number
classical geometry calls π/2, and see which of the paper's equations read more plainly. Every number in it is plain
arithmetic or a classical result, named where it is used.*

Open a door until it stands square to the wall. Nobody doing it thinks of an angle. The door starts flat against the
frame, it swings, and it stops when it is square. What was done was one sweep, from one edge to the edge square to it.
Afterwards the sweep can be described: as a quarter of a circle, as ninety degrees, as a slope that ran from nothing to
without limit. Those are three accounts of the one swing, made after it.

This essay takes that order seriously. The sweep is the operation. The circle, the angle and the ratio are ways of
representing it. So the sweep's total gets a letter of its own, Ω, and the familiar constants are rewritten in it. No
equation changes. What changes is which constants look like accidents and which look like the same thing met again.

The series keeps π where classical mathematics has it, and for a good reason: renaming it would hide what the classical
statements say. So this is an experiment beside the paper, not a proposal for it. Its use is as a test. Where a formula
gets simpler in Ω, the formula was about one sweep. Where it gets worse, it was about something else, usually about
several sweeps joined into a whole.

**In short.** Ω is to one read what π is to the turn: its total. π is two reads' worth; Ω is one. The total is the
blueprint's number for a read, not a number a read holds: a read has the slopes and the equal halves, and no count
reaches Ω. With that said, the aim of the essay is to strip the notation down to the least that states the series'
equations. Five things are enough:

1. s, a slope: what a read holds of a direction.
2. s ⊕ a = (s + a)/(1 − s·a): two sweeps taken as one.
3. 1/s, the exchange. Its fixed point, s = 1, is the corner.
4. ds/(1 + s²), the weight that composing leaves unchanged. Its total over one sweep is Ω.
5. A count of facings. Any constant in the series is that count times Ω, or its reciprocal.

| classical | stripped |
|---|---|
| the angle, and its tangent | the slope, and the weight below it |
| the tangent of a sum | s ⊕ a |
| 45° | s = 1 |
| h² + v² = 1 | the shares 1/(1 + s²) and s²/(1 + s²) |
| (2/π) · 1/(1 + s²) | 1/(Ω·(1 + s²)) |
| two angles adding to a quarter turn | the weights below s and below 1/s add to Ω |
| e^(iπ) = −1 | s ⊕ (1/s) is the horizon |
| π, 2π, 4π | 2Ω, 4Ω, 8Ω |

Nothing in the right-hand column uses an angle, a trigonometric function, π, e or i. The sections below are these five
things worked through, and where they keep the classical notation (the landing point in §8, for one) it is to show
what the notation was saying.

The order: the operation (§1), its measure and its total (§2), Ω times its reciprocal (§3), the Cauchy's coefficient
(§4), the corner (§5), two charts and one horizon (§6), three thumbs (§7), facings, Euler and composing (§8), a sweep
composed with itself (§9), what gets plainer and what does not (§10), what Ω does not do (§11), who saw which piece
(§12), and what it changes (§13).

---

## 1. The operation

Hold the thumb out at arm's length as H. A direction off it has a slope, s = v/h: how much of the thumb's length lies up
against how much lies along. A read holds directions by their slopes, and it holds nothing else of them.

Two sweeps taken one after the other are one sweep. In slopes the rule is

s ⊕ a = (s + a)/(1 − s·a).

A half and a third make one: (½ + ⅓)/(1 − ⅙) = 1. That is the whole operation, and it is rational: fractions in,
fractions out. Classical geometry calls it tangent addition and derives it from the circle. Here it is taken the other
way round, as the thing itself, with the circle one picture of it. (Where s·a reaches 1 the result is the horizon, and
past it the sweep has gone into another facing, which is a join of reads and not one read.)

## 2. Its measure and its total

Ask how to weigh slopes so that the operation moves no weight: so that every stretch of slopes weighs the same after
any sweep is composed onto it. There is one answer, up to a factor:

dμ = ds/(1 + s²).

The check is one line of algebra. With s′ = s ⊕ a, ds′/(1 + s′²) = ds/(1 + s²). This is the density the series calls
the heat, and it was reached here with no circle and no angle: it is the operation's own measure.

Its total over one sweep, from home (s = 0) to the horizon, is a number. Call it Ω:

Ω = ∫₀^∞ ds/(1 + s²).

That is the definition. Classical geometry knows this number as π/2, the quarter turn in its own units, and nothing
below depends on anything but the definition.

Ω is not had by any finite count. Two classical routes approach it by fractions. Half of it is Gregory's and Leibniz's
series, the weight of the slopes below 1:

Ω/2 = 1 − 1/3 + 1/5 − 1/7 + …

and the whole of it is Wallis's product:

Ω = (2·2)/(1·3) × (4·4)/(3·5) × (6·6)/(5·7) × …

Wallis's product is usually quoted as "π/2". It was Ω all along.

## 3. Ω times its reciprocal

*Reads and Writes* has two constants, π/2 and 2/π, and their product, 1. In the new letter they are Ω and 1/Ω, and
Ω × (1/Ω) = 1 says nothing at all: any number times its reciprocal is 1. So the content must be somewhere else, and it
is here.

Sweep from all-along to all-up by any path. The up share starts at 0 and ends at 1. Call the path's length, in thumbs,
its Ω. Then the mean rate at which the up share fills, per unit of path, is 1/Ω, because a rate averaged over a length
gives the rise, and the rise is 1. Three paths:

| path | its length Ω | mean filling rate 1/Ω |
|---|---|---|
| the turn | π/2 | 2/π |
| the straight chord | √2 | 1/√2 |
| the two edges of the square | 2 | ½ |

So "Ω" is not one number until a path is chosen. The product is 1 on all of them; the split of that 1 into two
particular factors is the path's. The turn's split is the one with π in it. That is where π enters this subject, and
the only place in this section: it is the length, in thumbs, of the one path that the operation of §1 walks evenly.

The two constants are then the two ways of being asked about one sweep. How far was swept: Ω. What share, on average,
was showing: 1/Ω.

## 4. The Cauchy's coefficient

The series' central law is the density of slopes under one even sweep. Classically,

f(s) = (2/π) · 1/(1 + s²), s ≥ 0.

In the new letter it is

f(s) = 1/(Ω·(1 + s²)).

Read this way there is nothing to explain about the coefficient. The shape 1/(1 + s²) is the operation's measure (§2).
Ω is that measure's total. Dividing by the total makes it a share. The "2/π" in front of the Cauchy was never a
second fact about the law; it is the first fact, normalised.

One caution keeps this honest. If the sweep is written as a turn through an angle, with the slope as that angle's
tangent, then an even sweep covers every slope only when the angle's range is exactly Ω. So Ω cannot be set freely in
that picture. It is fixed by the definition in §2, and the angle picture has to agree with it.

## 5. The corner is half of Ω

The corner is the slope 1, where the up share equals the along share. Three things are true of it, and in the classical
telling they look like three facts:

- the shares are equal, v = h;
- it is the middle of the sweep, 45° of 90°;
- it is the one slope its own reciprocal.

With the measure in hand they are one fact. The exchange s ↦ 1/s, which swaps the two shares, moves no weight:
d(1/s)/(1 + 1/s²) is ds/(1 + s²) with the direction reversed. So the exchange carries the slopes below any s onto the
slopes above 1/s, weight for weight. Its fixed point, s = 1, therefore has half of Ω on each side.

"45°" is that statement in the angle chart: Ω/2. The corner is the median of the Cauchy for the same reason. No circle
was needed, only the operation, its measure and the exchange.

## 6. Two charts and one horizon

One sweep has two common charts.

| chart | where home is | where the horizon is |
|---|---|---|
| by weight passed (the turn) | 0 | Ω |
| by slope | 0 | no number: the slopes run on without limit |

These are the same sweep. The first chart makes the horizon look like an edge that can be stood at, the end of a ruler
marked Ω. The second shows what it is: the direction with no along share, which no slope names.

It is tempting to say that the bounded chart is what one has when the far thing's size is known and the unbounded
chart is what one has when it is not. That is a mistake, and the letter Ω makes it easy to make. Both charts describe
one read, whatever is or is not known. What knowing a size changes is something else: a size is an amount in a unit,
which is a write, and a write is not a property of either chart.

What the paper does distinguish is two reads. In the inscribed read the horizon is approached and never stood at. In
the central read, across a thing to its rim, the rim is a point that is reached. The bounded chart suits the second,
and its number Ω is reached there; the first is described by 1/Ω, a mean that is only approached.

## 7. Three thumbs

In space the thumb is crossed with itself: three thumbs square to each other, three pairs, and so three sweeps, each
with total Ω. How do they combine? Three guesses offer themselves: add them (3Ω), compose them, or find one sweep that
stands for all. None is right as stated, and the answer has four parts.

*As readings.* The three sweeps are not independent. Call the shares along, up and across h, v and v₂. The three pairs
have slopes s = v/h, s₂ = v₂/h and v₂/v, and the third is the second over the first, s₂/s. Going round the three pairs
multiplies to 1: (v/h) × (v₂/v) × (h/v₂) = 1. So the joint reading is two free slopes and one closure. That is what the
three sweeps keep and what they combine: each pair keeps the plane's law, with coefficient 1/Ω and its own corner as
its median, and together they hold only two numbers.

*As a measure.* The three sweeps bound one octant of directions. Its area is given by Girard's theorem: the three
corner angles added, less a half turn. Each corner is Ω and a half turn is 2Ω, so

area of the octant = 3Ω − 2Ω = Ω.

Three sweeps combine to one Ω. The density follows from it. With two slopes s and s₂ off the look, the heat over the
octant is

f(s, s₂) = 1/(Ω·(1 + s² + s₂²)^(3/2)),

with the same coefficient 1/Ω as in the plane. In classical form this is the paper's 2/π appearing twice, in the plane
and in space, with no stated reason. In Ω the reason is on the page: each is a density divided by its total, and the
totals are the same number.

The coefficient normalises the octant and nothing larger: over all four facings round the look the same shape has
coefficient 1/(4Ω).

*What needs Ω and what does not.* Split the joint reading into how far a direction lies off the look, r with
r² = s² + s₂², and where it lies round the look. The sweep round the look has total Ω, and it cancels the 1/Ω in
front. What is left is the law of r alone:

share within r of the look = 1 − 1/√(1 + r²).

There is no Ω in it and no limit: a square root of a fraction. Half the directions lie within r = √3. The other joint
counts are plainer still. The share of directions with both slopes below 1 is ⅓, and each of the six orders of the
three shares has ⅙. So in space the constant belongs to one thing only, the sweep round the look. Written with 2/π the
density hides this; written with 1/Ω it shows which statements carry the constant and which never had it.

It does not go on for ever. With a fourth thumb the total of the corresponding region is Ω²/2, so the agreement between
the plane and space is theirs and not a rule for every number of thumbs.

*As an operation.* The sweeps do not commute. Two quarter sweeps about two thumbs, taken in the two orders, leave a
thing 120° apart. And sweeping each thumb evenly by itself is not the same as turning the three as one frame: the first
puts 0.3426 of the weight below a pair's corner, the second a half. So in space the measure combines simply and the
operation does not, which is the reverse of what one might expect.

## 8. Facings, Euler and composing

A sweep runs within one facing: both shares positive. Signs are a join of reads, the blueprint's, and they count the
facings: four in the plane, eight in space. The totals are then

- the whole turn: 4Ω (classically 2π);
- the whole sphere of directions: 8Ω (classically 4π).

One Ω a facing in both. The classical 2π and 4π hide that the second is not "twice the first" in any useful sense; it
is eight octants where the first is four quarters.

Euler's formula takes the same reading. The landing point of a slope, w(s) = (1 + is)/(1 − is), turns twice as fast as
the sweep (Euclid III.20: the angle at the centre is twice the angle at the rim). So over one sweep it runs from 1,
through i at the corner, to −1 at the horizon. In the blueprint's notation:

- one Ω: e^(iΩ) = i;
- two: e^(2iΩ) = −1, which is Euler's identity;
- four: e^(4iΩ) = 1.

The identity is "two sweeps' worth", and i is one.

The form with no limit in it can now be read as a law of composing sweeps, with no circle assumed. Three lines:

- the landing point turns composition into multiplication: w(s) × w(a) = w(s ⊕ a), which is one line of algebra,
  (1 + is)(1 + ia) = (1 − sa) + i(s + a);
- a slope composed with its reciprocal is the horizon: s ⊕ (1/s) has 1 − 1 = 0 below the line;
- the horizon's landing point is −1.

So w(s) × w(1/s) = −1, at every slope. In words: a sweep and its exchange together make the whole sweep. At the corner
the sweep is its own exchange, and the statement is i × i = −1. Euler's identity is the same statement with the whole
sweep's length named, e^(2iΩ) = −1, and the naming is the only part that needs a limit.

The same fact can be said in weights. The exchange carries the slopes below s onto the slopes above 1/s, weight for
weight (§5), so the weight below s and the weight below 1/s add to Ω. Classical geometry writes that as two angles
adding to a quarter turn. And the two halves of this essay, the measure of §2 and the landing point here, are joined by
one line: the weight of the slopes below s is the logarithm of the landing point, over 2i,

μ(s) = (1/2i)·ln w(s),

followed continuously from home. So there is one operation, and it has three charts:

| chart | a sweep is | composing two is |
|---|---|---|
| slope | s | s ⊕ a |
| weight passed | μ(s), out of Ω | adding |
| landing point | w(s) | multiplying |

The slope chart is rational and has no total in it. The weight chart is where Ω lives. The landing-point chart is where
Euler's notation lives, and the logarithm passes between the last two, which is why it separates a turn from a size as
it does. The finite law, w(s) × w(1/s) = −1, gives the result; the limit (1 + iθ/n)ⁿ is needed only to say how long the
sweep was, and has to be handed that length to begin with.

## 9. A sweep composed with itself

Take one sweep and compose it with itself, again and again: s, then s ⊕ s = 2s/(1 − s²), then that with itself. Where
the result passes the horizon it is in another facing; read it back in the first by dropping its sign. This is a rule
of one line, rational, with nothing kept from step to step.

It is a famous rule in another chart. Write y for the up share squared, y = s²/(1 + s²). Then the new y is
4y(1 − y): the logistic map at its fullest setting, the standard first example of chaos. So that map is a sweep
composed with itself. In the three charts of §8:

| chart | the rule | what it leaves unchanged |
|---|---|---|
| slope | s ↦ 2s/(1 − s²), sign dropped | 1/(Ω(1 + s²)), the Cauchy |
| weight passed | twice the weight, folded back at Ω | 1/Ω, the even spread |
| share | y ↦ 4y(1 − y) | 1/(2Ω√(y(1 − y))), the arcsine law |

Three laws that textbooks list separately are one measure in three charts, each with Ω in its coefficient for the same
reason as before: it is the total.

The three things chaos is usually said to need each have a plain source here. *Bounded:* one sweep has a total, Ω.
*Stretched:* composing a sweep with itself doubles the weight passed. *Folded:* past the horizon the result lies in
another facing, and reading it back folds it. The fold is a join of facings and belongs to no single read.

The usual measure of chaos is the rate at which two nearby starts part, averaged along a long run. In the share chart
that average has to be taken: the stretch differs from place to place. In the weight chart the stretch is exactly 2
everywhere, so the rate is ln 2 a step, read off the rule with no run and no average. The number is the same in every
chart. Only one chart shows it without a sum.

That ease has a price, and Ω is the price. The slope chart and the share chart are joined by a fraction,
y = s²/(1 + s²), with no limit anywhere. The weight chart is joined to both of them only through Ω. So the chart in
which the rule looks simplest, a doubling and a fold with no constant in sight, is the one chart that cannot be reached
by fractions. The rule itself was rational all along, in slopes.

What makes this rule part nearby starts, where others do not, is one property of the rule and none of the sweep. Four
rules on slopes:

| rule | kind | rate of parting, a step |
|---|---|---|
| s ⊕ a, a fixed sweep added | one to one; keeps the measure | 0 |
| k·s with k below 1, a fixed share of what remains | one to one; draws everything toward home | ln k, below 0 |
| s ⊕ s, the sweep composed with itself | two to one | ln 2 |
| s composed with itself n times over | n to one | ln n |

The first two can be undone, so nearby starts never part for good. The third uses its input twice, and two different
slopes give one result. That two-to-one step is the fold, and it is the only source of a rate above zero. So the three
parts separate cleanly. The sweep's are the total Ω and the measure, the same in every row. The rule's is how many
slopes it sends to one, and that alone sets the rate. The run's are the digits of the start, used up in the last two
rows and never in the first two.

And the acts sort as they did before. The rule keeps nothing. A run of it is a kept sequence, and what is kept is
writes. Each step uses up one binary digit of the starting slope, so a start put down to p digits holds for about p
steps and no longer. The horizon of prediction is the length of what was written. That is how a rule of one line gives
a record nobody can extend: the rule is exact, and the start was never written out in full.

Two limits. This is one map, and its close relatives; at other settings of the logistic map there is no such sweep
behind it. And none of it is new: that the logistic map at 4 is the tent map in another chart is Ulam and von
Neumann's, of 1947. What the letter adds is small, that the three unchanged laws share one coefficient.

## 10. What gets plainer, and what does not

The experiment sorts formulas. Some lose a stray factor of 2; some gain one.

| statement | classical | in Ω |
|---|---|---|
| the Cauchy's coefficient | 2/π | 1/Ω |
| the corner | π/4 | Ω/2 |
| Wallis's product | π/2 | Ω |
| Gregory and Leibniz | π/4 | Ω/2 |
| Buffon's needle, as long as the gap | 2/π | 1/Ω |
| the octant | π/2 | Ω |
| odd squares, 1 + 1/9 + 1/25 + … | π²/8 | Ω²/2 |
| the whole turn | 2π | 4Ω |
| Euler's identity | e^(iπ) | e^(2iΩ) |
| all squares, 1 + 1/4 + 1/9 + … | π²/6 | 2Ω²/3 |
| the disc's area | πr² | 2Ωr² |
| the Gaussian's constant | √(2π) | 2√Ω |

The top rows are statements about one sweep, or one facing, and they come out as Ω or its reciprocal with nothing
attached. The bottom rows are about wholes: a disc, every whole number, a bell over the whole line. There the classical
π is the more natural unit and Ω only adds a factor.

That is the experiment's result, and it agrees with the series' sorting. A read is about one sweep. The whole turn, the
disc and the completed line are the blueprint's, and π is the blueprint's letter.

## 11. What Ω does not do

*It does not make the number cheaper.* Ω is the same limit π/2 always was. No count reaches it; Wallis's product and
Leibniz's series only approach. A new letter is a name, and the series' rule stands: the value is held whole only on
the blueprint.

*It is not a read's number.* A read has the slopes, the measure's shape, the exchange and the equal halves. It has no
total. Ω is what the blueprint says the total is.

*It is not one number before a path is chosen* (§3).

*It does not turn two reads into one.* Ω × (1/Ω) = 1 shows that the two constants are reciprocal. It does not show that
the inscribed and central reads are one operation; that is Euclid III.20, a statement about one point seen from two
places on a circle.

*It should not go into the paper.* Classical mathematics uses π, and a reader who knows that 2/π is the Cauchy's
coefficient should find it there. The letter is for thinking with.

## 12. Who saw which piece

Every formula here is old. The composition rule is tangent addition. Its invariant measure is the Cauchy density, and
that the Cauchy is carried to itself by such maps is classical. Girard gave the area of a spherical triangle by its
angles in 1629. Wallis's product is of 1656; the alternating series is Gregory's and Leibniz's of the 1670s, and
Madhava's before them. Buffon's needle is of 1777.

The idea that π is the wrong unit is not new either. Palais argued in 2001 that the whole turn, 2π, is the natural
constant, and Hartl's manifesto of 2010 named it τ. In that vocabulary Ω is a quarter of τ. Those arguments are about
which unit makes the blueprint's formulas tidiest, and they favour the whole turn because the blueprint's subject is
the whole. This essay asks a different question, which unit fits one sweep, and so lands on the quarter.

What the series adds is the order of the telling: the operation first, its measure second, the total third, and the
circle as one picture of it; and the sorting in §10, which uses the choice of unit as a test of whether a formula is
about one sweep or about a whole.

## 13. What it changes

*The Cauchy's constant is not a second fact.* It is the measure's own total, turned over.

*The corner is one fact.* Equal shares, the middle of the sweep and the reciprocal's fixed point are the exchange
keeping the measure.

*Plane and space share a coefficient for a reason.* One quarter sweep and one octant have the same total, by Girard.

*In space the constant belongs to the sweep round the look.* How far off the look, the near third and the six orders
have no Ω in them.

*Euler's −1 is a law of composing.* A sweep and its exchange make the whole sweep.

*A stray 2 is a sign.* Where a formula with π in it carries a 2 that comes and goes, π/2 or 2/π or π/4, it is likely a
statement about one sweep written in the unit of the whole.

*The horizon is not the mark Ω on a ruler.* The bounded chart is a chart.

---

## Sources

- Buffon, G.-L. Leclerc, comte de (1777). Essai d'arithmétique morale. *Histoire naturelle*, Supplément 4.
- Euclid. *Elements*, Book III, proposition 20.
- Girard, A. (1629). *Invention nouvelle en l'algèbre.* Amsterdam. (The area of a spherical triangle.)
- Hartl, M. (2010). *The Tau Manifesto.* (Not opened for this essay; cited for the proposal of τ = 2π.)
- Palais, R. (2001). π is wrong! *The Mathematical Intelligencer* 23(3), 7–8. (Not opened for this essay.)
- Ulam, S. M. and von Neumann, J. (1947). On combination of stochastic and deterministic processes. *Bulletin of the
  American Mathematical Society* 53, 1120 (abstract). (Not opened for this essay.)
- Wallis, J. (1656). *Arithmetica infinitorum.* Oxford.
- *Reads and Writes* (`../readers-and-writers.md`): §1 "A read and a write" and "Two verbs, two nouns"; §9 "Reading is
  2/π; walking is π/2", "The thumb, short by reading, long by walking, and whole" (the three paths), "What is free, and
  what π costs", "Four identities, one exchange", and the passage on a turn added to itself (`../../plans/chs-plan.md`); §8 (three
  thumbs, the octant, the two orders). The current account,
  which keeps π. The exact checks behind §7's numbers are `../../plans/swp-plan.md` and `../../plans/wdg-plan.md`.
- Demos: `../../one-read.html` (one turn and its landing point), `../../paths.html` (one sweep, three paths),
  `../../sweep-zero.html` (composing sweeps from zero), `../../wedge.html` (the octant), `../../euler.html` (n reads).
