# One share, and the shape of a law

*The twenty-third of a series of essays on what can be known from where one stands. Draft, 14 November 2026. It gathers
one day's work: the inverse square from one vantage (SPN R977, R979; ISX), the same share in other classical situations
(R982; RWX), the tower's cancellation read as what a geometric law is (R985), and a sort of the laws *Reads and Writes*
states, in which the prediction was killed (R986; LWS).*

Hold a reading lamp close over a page and the page is evenly bright under it; move it up the wall and the light falls
off, a quarter for each doubling of the distance. Everyone has seen both. They are usually told as two facts, the near
field and the inverse square, joined somewhere in between by a formula. This essay is about the one quantity they both
are, a share of directions, and about what the same share does in places that have nothing to do with lamps. It ends on
a question the share raised: what a law is, read this way, and how many of the laws the series uses have the shape it
suggests. The answer to the last was smaller than predicted, and that is part of the result.

The order: the lamp over the page (§1), two ends reading each other (§2), only a round source pairs (§3), the same share
elsewhere (§4), counting ticks (§5), the tower (§6), what a law is (§7), sorting the laws (§8), what is classical and what
is ours (§9), and what it changes (§10).

*Demos: `thin.html` (the same signal, a smaller share), `shv.html` (one vantage, the bounce), `slide-rule.html` (a tower of
readings).*

---

## 1. The lamp over the page

Take the lamp to be a flat disc of radius a, evenly bright, and the page a point on its axis at distance d. The light the
point gets, counted with its own cosine as a page counts it, is a textbook formula: πL·a²/(a² + d²), L the disc's
brightness. Write s = d/a and it is

  E/(πL) = 1/(1 + s²).

That is the Cauchy's heat of the direction with slope s: the disc's share of the page's front hemisphere, weighted as a
flat receiver weighs directions. Nothing in it is an amount. The lamp's brightness L sits outside as the one thing the
share is a share of.

Two charts of one share. Close up, s small, the share is nearly 1: the near field, flat. Far off, s large, it is nearly
1/s² = a²/d²: the inverse square. Neither is an approximation of the other; each is the share read at one end, and the
exact share is off from the inverse square by exactly 1/(1 + s²), a millionth at a thousand radii.

The exchange s ↔ 1/s pairs the two ends:

  E(s) + E(1/s) = πL,

exactly, at every s. The lamp at d and the lamp at a²/d light the page by complementary shares. At d = a, the corner,
each gets half. Checked by direct quadrature over the disc at five distances (to 10⁻⁵⁰) and in exact fractions on thirty
rational slopes (ISX, `plans/isx-plan.md`).

Scale the world and nothing moves: a and d together times k leave s, and so the share, as they were. The inverse square
in d appears only when a is held fixed while d moves, which is to say only when a size is carried in. Then d → kd
changes the light by (1 + s²)/(1 + k²s²), which is 1/k² only far off. The law everyone learns is the scale test with the
source's size held: the read is the share, and the 1/d² is what the share looks like to a writer who has fixed the disc.

## 2. Two ends reading each other

Put a second disc where the page was, facing the first. Each disc reads the other: of the light leaving one, a share
reaches the other. Radiative transfer calls these view factors and has a rule for them, reciprocity: A₁F₁₂ = A₂F₂₁. Read
as two reads, it says the ratio of the two shares is the ratio of the areas, with the distance gone; and far apart the
product of the two shares is the areas over (πd²)², with the sizes gone into their geometric mean. The ratio of the reads
takes down the shared distance and leaves the sizes against each other; the product takes down the sizes and leaves the
distance. Checked at five geometries to 5·10⁻⁵⁰, the far product within 10⁻⁶ of its limit.

That is the denominator paradox's exchange (*Each Sees the Other Smaller*): two people each see the other smaller in terms
of their own hand, and dividing the two reads leaves the hands, multiplying them leaves the distance. The discs do it with
light.

## 3. Only a round source pairs

Is the exchange a property of light, or of the disc? A square plate of half-side b, on its axis at s = d/b, has an exact
share too. Its near and far shares do not add to one: E(s) + E(1/s) runs from 1.0045 πL at s = 10 to 1.108 πL at the
corner. The pairing is the round source's.

The reason is one line. From the axis the disc's rim is one cone, of half-angle α with tan α = 1/s, and the disc's share
is sin²α. The exchange takes α to 90° − α, so the two shares are sin²α + cos²α = 1: a round cap and its complement. A
square's rim is not one cone, so its near and far shares overlap at the corner and are complements nowhere. A sphere,
seen from outside, gives (a/d)² exactly at every d ≥ a, the plain inverse square: its s below 1 is inside the body, so it
has no partner to pair with.

## 4. The same share elsewhere

The share 1/(1 + s²) is not the lamp's alone. It turns up wherever two things are compared by their ratio, and it turns up
on two charts, which give two kinds of corner (RWX, `plans/rwx-plan.md`; each case computed from its own physics,
impedances, conservation laws, boundary conditions, not from the share's formula).

*On the ratio itself: a crossover.* An RC divider driven at ω passes |H|² = 1/(1 + s²) across the capacitor and
s²/(1 + s²) across the resistor, s = ωRC. The two are complements; s ↔ 1/s swaps them; at s = 1 each passes half; the
phase's tangent is s. Low against high, near against far: the lamp's exchange, in a circuit.

*On the level of a ratio: a best point.* An elastic collision of m₁ onto m₂ at rest passes the share 4m₁m₂/(m₁ + m₂)²
of the energy. A source of resistance R_s delivers to a load R_L the share 4R_sR_L/(R_s + R_L)² of the most it could.
Light at normal incidence crosses from index n₁ into n₂ with the share 4n₁n₂/(n₁ + n₂)². With k the pair's ratio, all
three are exactly

  4k/(1 + k)² = sech²(½ ln k) = 1/(1 + s²),  s = sinh(½ ln k).

On this chart k ↔ 1/k is s ↔ −s, which leaves the share unchanged: the corner is not a crossover but a stationary best
point, at k = 1, with zero slope in ln k. Equal masses pass all the energy; the matched load takes the most; light passes
whole between equal indices, and what is reflected is tanh²(½ ln k). A driven series RLC is the same shape:
P/P_max = 1/(1 + s²) with s = Q·(ω/ω₀ − ω₀/ω) = 2Q·sinh(ln(ω/ω₀)), unchanged by ω ↔ ω₀²/ω, half power at s = ±1.

MOT (`../../plans/mot-plan.md`, run 2) had found these two kinds of corner in motion, a change of regime and a stationary point. Here they are one
share read on two charts: the ratio, where the exchange makes a complement, and the sinh of the level, where it makes a
mirror. Which chart a situation uses is set by whether its pair is read directly (ωRC, d/a) or through the ratio's level
(½ ln k, ln(ω/ω₀)). In every case the share is a read: scale the pair together and it does not move.

## 5. Counting ticks

Two classical cases do something else. A pendulum's period in units of √(ℓ/g) depends on its swing alone (2π/AGM(1,
cos(θ₀/2)), Legendre's): 6.2871 at a small swing, 6.6999 at one radian, 10.3232 at 2.5, the same at every length. A Kepler
orbit's period in units of √(a³/GM) is 2π at every eccentricity. From one standpoint the ticks read no size: a pendulum
seven times as long, under seven times the pull, swings in the same ticks.

Carry in g, or GM, and a counted period writes the length, or the orbit's size. That is the bounce's move (essay 22 §13)
and the candle's (essay 1 §5): an amount carried in lets a count write a length. The lamp, the circuit and the collision
are reads; the pendulum and the orbit are counts waiting for an amount.

## 6. The tower

Behind all of these is one thing done with denominators. A table three quarters of a door, a door two fifths of a wall:
the table is three tenths of the wall, and the door is in neither end (essay 20 §4):

  a/b · b/c = a/c.

The door was needed for both readings and is in neither result. Three things keep this exact rather than merely neat.
Within one read nothing cancels: a reading's denominator is its "in terms of", and set to zero it gives the horizon, not
a reading. The last "in terms of" stays: a/c is still in terms of c, so a tower ends on the thumb, a kept step or an
agreed unit, and that last storey is why one amount must be carried in to get a size. And a loop closes to 1: read round
and back, everything cancels, and a remainder is a misread link, seen and not located.

The day's cases do the same move. The two discs' ratio cancels the distance, their product the sizes. In 4k/(1 + k)²
only the pair's ratio survives; the common amount has cancelled, which is why scaling the pair moves nothing. On the walk
(essay 19) the ratios of successive looks telescope to the two end reads, so the strides between need not be kept.

## 7. What a law is

*Reads and Writes* §1 calls a geometric law what the geometry has in place of memory: it covers every chain of any length
at once by one finite expression with an empty place (R864, R871, R881). The cancellation says how. Read this way, a
geometric law is what is left of a chain when every middle denominator has cancelled: the ends, and the last "in terms
of", which is the law's empty place. It needs no memory because what memory would keep, which middle steps were taken, is
exactly what cancels.

Euler's identity, in the series' rational form, is a cancellation. With w(s) = (1 + is)/(1 − is),

  w(1/s) = (s + i)/(s − i) = i(1 − is)/(−i(1 + is)),

so in w(s)·w(1/s) each factor's denominator cancels the other's numerator, and what is left is i/(−i) = −1: the corner's i
over its mirror. Exactly −1 at s = 1/3, 2 and 5/7 in Gaussian fractions. Tangent addition is the same, read as turns
between landing points: the turn from x to y is w(y)/w(x), and (w(y)/w(x))·(w(z)/w(y)) = w(z)/w(x), the middle landing
point gone, so n turns compose to one.

But not every law is a chain. The complements, 1/(1 + s²) + s²/(1 + s²) = 1, and the one-length circle, h² + v² = 1, are
sums over one shared denominator that stays: it is the one length, the last storey, and the law is that the numerators
fill it. Parallax, 1/(d/B) = 1/s₁ + 1/s₂, is a sum of the reads taken inward. So at least two shapes: products, where the
middle denominators cancel, and sums over a shared denominator, where it stays.

## 8. Sorting the laws

That reading made a prediction, and the prediction could fail, so it was tested (LWS, `plans/lws-plan.md`). The method and
the guesses were written down first: at least three quarters of the laws *Reads and Writes* states would be chains or
shared sums; every composition of turns or slopes a chain; every complement a shared sum; a few laws neither. A fresh
agent, not shown the categories, listed every law the paper states, 125 of them; I sorted them by a test written before
the list, and checked every chain and shared sum exactly.

The main prediction was killed. Chains 23, shared sums 10, neither 92: 26%, not 75%. Every complement was a shared sum, and
every composition of turns was a chain, but only when read as turns between landing points, which is my reading. All 86
exact checks of the 33 passed.

The 92 that are neither fall, looking back, into a handful of groups: densities and measures (19, a heat per something,
not a relation between two expressions), changes of chart (20: tan, gd, sech, the Cayley map, Mercator, aberration),
formulas that give one quantity from reads (13: parallax, contact, the walk), limits and series (8), the holonomy laws
where a loop leaves a remainder (4), and other invariances, transforms and laws among amounts (28). The agent listed
broadly, which pads the last pile, but even the true identities split three ways.

So the claim narrows. Chains and shared sums are how laws look that relate reads to each other: they compose them, or
fill one length with them. A change of chart is a third common shape, one read under another name, where nothing cancels
and nothing is shared because there is only one read. And holonomy is what a chain leaves when it does not close. That
last sentence is a reading and is untested. The sort was not blind: I wrote the categories.

## 9. What is classical and what is ours

Classical: the disc's irradiance (Lambert, radiometry), view-factor reciprocity, the RC divider, the collision's energy
share, maximum power transfer, Fresnel's normal incidence, the RLC resonance, Legendre's pendulum, Kepler's third law,
telescoping products and the Cayley form of tangent addition. Every number in this essay is one of those, computed.

Ours: the sorting. That the near field and the inverse square are one share read at two ends, paired by the exchange,
and that the pairing is the round source's; that the crossover and the best point are one share on two charts; that the
pendulum and the orbit are the bounce's move; that a law of the chain shape is what the cancellation leaves; and that
this shape covers a quarter of the paper's laws, not three quarters. The sort of the cases into types is mine and not
blind.

## 10. What it changes

The inverse square is the far end of a share, and its exact form has a near end the textbook law leaves out; the 1/d² is
a writer's, appearing only when the source's size is held. The same share runs through circuits, collisions and light
at a boundary, and the two places its exchange can fall, a crossover and a best point, are two charts of it. And a
geometric law of the chain shape is a chain with its middle taken down: which is why it needs no memory, and why its one
empty place is the last denominator, the one that never comes down. Most of the paper's laws are not of that shape, and
the next question is what the third shape, the change of chart, is for a read.

---

## Sources

- `../../plans/isx-plan.md`, `../../runs/isx/`: the disc's share, the exchange, the coaxial discs, the square plate, the
  sphere (ISX run 1).
- `../../plans/rwx-plan.md`, `../../runs/rwx/`: the RC divider, the collision, the matched load, Fresnel, the RLC, the
  pendulum and Kepler (RWX run 1).
- `../../plans/lws-plan.md`, `../../runs/lws/`: the 125 laws, the sort and the checks (LWS run 1).
- `../../plans/discussion-note.md` item 17: the tower's cancellation and what a law is (R985).
- `../inverse-square.md`, "From one vantage"; *Reads and Writes* (`../readers-and-writers.md`) §1 "A law in place of
  memory" and "A denominator is scaffolding", §7 "Near and far, one share and its exchange" and "The same share
  elsewhere"; *Reads and Writes in Physics* §7.2.
- Essay 1 §5 (the candle and the bounce), essay 4 §13 (the two kinds of corner), essay 19 (the
  walk), essay 20 (scaffolding), essay 22 §13 (the bounce); *Each Sees the Other Smaller* (`../denominator-paradox.md`).
- Demos: `../../thin.html`, `../../shv.html`, `../../slide-rule.html`.
