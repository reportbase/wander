# God mode and a vantage: what a walk on whole numbers showed

*The twenty-second of a series of essays on what can be known from where one stands. Draft, 13 November 2026, brought up
to date 14 November. It gathers what one page, `thumbs-walk.html`, showed over nineteen runs in two days (TWK,
`plans/twk-plan.md`; SPN R930–R955), about the difference between classical geometry's view from nowhere and a read from
somewhere.*

Open a map on a phone and pinch. The streets come, then the buildings, then the house numbers; pinch the other way and
the city goes, then the country, then the coast of a continent. Nobody believes the phone holds the planet. It holds what
the screen can show, fetched as the fingers move, and whatever is too small to see is not fetched at all. A game that lets
a player walk from one horizon to the next does the same: it streams the ground near the player and makes the rest from
a seed when it is needed.

That is engineering, and good engineering. This essay is about the geometry under it. One page was built to see how far a
first-person view can go on whole numbers alone, with no trigonometry and no list of things stored, and over nineteen runs it
kept showing the same thing from different sides: classical geometry is a view with no standpoint, very powerful, and
everything it gives it gives by holding the whole; a read has a standpoint, holds a fixed amount, and does not need the
whole to exist as a count anywhere it can reach.

The order: what the blueprint is good for (§1), a view on whole numbers (§2), the tower and the scaffolding (§3), keeping
by size on the screen (§4), each scale its share (§5), what nearness and distance cost (§6), something to read (§7), what is classical
and what is ours (§8), set beside a blueprint thing for thing (§9), things that move (§10), a view that holds still
while the look moves (§11), and what it changes (§12).

*Demo: `thumbs-walk.html` (W A S D walk, G half way to the thing under the crosshair, B back, M the menu; desktop only).*

---

## 1. God mode

Classical geometry is god mode. It stands nowhere. It holds every point at once, in amounts of one unit, with both signs
of every axis, both hemispheres of every turn, the circle closed and π its number. From there it can add: the area of a
field, the volume of a room, the total mass of a galaxy, the sum of a series. It can join: two maps made from two places
become one map. It can say where everything is before anyone looks.

This series calls that view the blueprint, and sets it beside a read only for comparison. It is not a criticism. The
blueprint is why bridges stand. It is used because it is so strong.

What it costs is that everything it gives, it gives by holding the whole. A total needs every term. A join needs both
pieces in one frame, which means the size of each. A map of everything needs a count of everything, or at least a bound
on where the counting stops. In a world laid out by a person, that is no trouble: the world has an N and the blueprint
holds it. The question the page was built for is what a view from one place needs when nobody hands it an N.

## 2. A view on whole numbers

The page draws a wireframe field of boxes, towers and pyramids, seen from an eye a little above the ground. Every vertex
is a whole point (or a half), made from its ground cell by a hash; no list of things is stored anywhere. Three thumbs,
square to each other, come out of the eye, and the look runs down their diagonal, so the crosshair is the triple corner
where the three thumbs' sweeps meet.

The thumbs are not set by angles. Each is a column of a product of turns, and each turn is given by a half-slope p/q: its
two parts are (q² − p²)/(q² + p²) and 2pq/(q² + p²), both fractions, and their squares add to 1. The three thumbs are then
square to each other exactly, in fractions, with no rounding. The look itself is held as whole numbers: a count of
quarter turns and two half-slopes in 128ths. Dragging the mouse steps a half-slope. Past an eighth of a turn the
half-slope passes to the next quarter by tangent subtraction, (u − 1)/(1 + u), rounded to the nearest 128th. The screen's
edge is a slope of 6/5 from the look. Walking is a stride of 1/4 along a heading that is itself a rational direction.

Run 3 checked this by replacing every trigonometric function in the page with a counter and walking, turning and looking
for 300 steps. The count was 0. The only place an arctangent is called is in showing each pair's share of its sweep out
of Ω, which is a limit and is labelled as one.

What this buys is exactness. For the thing under the crosshair, its three reaches along the thumbs are fractions, and so
every pair of them gives a slope that is a fraction. The checks run on those fractions in BigInt arithmetic: the three
pair slopes multiply to exactly 1; for each pair, w(s)·w(1/s) = −1, with w(s) = (1 − s² + 2is)/(1 + s²), so the
simplified Euler's identity holds digit for digit; scaling the world and the eye together by 2, 7 or 1/3 changes no slope;
changing the thumb H, the length the observer holds out, changes no slope either. Every machine running the page gets the
same fractions.

What it does not buy is speed. Nothing here says a page without sines is faster than a page with them. Graphics hardware
computes sines very quickly. The point is that nothing a read needs requires them.

## 3. The tower comes down; the scaffolding stays up

A frame built from many turns is a product, and a product of fractions grows its denominators with every factor. If the
page multiplied the new turn onto the old frame at each step of the mouse, the frame's fractions would grow without
bound. It does not: it recomputes the frame from the one current turn each time. However the look got where it is, the
history cancels. This is the tower of ratios: a/b times b/c is a/c, and the middle comes down.

The eye's place is different. It is a running total of strides, each along whatever heading was current, and a total
keeps every term. Run 2 walked a seeded path of 200 legs, turning between them. With the eye left as its running total,
its longest denominator reached 102 digits by leg 50 and 129 at its most; the target's slopes, read from that eye, reached
136 digits. With the eye put down on the nearest point of a 1/16 grid at each new heading, its denominator never passed
6 digits and the slopes stayed under 10. Every check held both ways.

Putting the eye down on a grid is a write: a mark made, an amount stated in a unit. It gives up one thing, the exact path
back to where the walk began. No reading from where the eye now stands uses that path. The tower's middle terms cancel by
themselves; the place's terms have to be taken down by hand, and taking them down is a write.

Essay 20 called a denominator scaffolding: needed for each reading to be made, gone from what the readings give together.
Here the two sides are on one screen. The frame is a chain of ratios and comes down for free. The place is a sum of
amounts and stays up until it is written over.

## 4. Keeping by size on the screen

A blueprint of an endless field is an endless list. Run 4 replaced the field near the eye with a field at every scale:
scale j has cells 24·2^j wide, each holding at most one thing with every length times 2^j. A thing is kept when its
breadth b is at least a grain g times its distance d, and when the eye is not inside it, compared in squares, b² ≥ g²d²
and d² ≥ b², so with no root and no angle. Since b at scale j is at most 32·2^j, a kept thing lies within 1,024·2^j
units, and the same number of cells is scanned at every scale.

The run found about 480 things kept at each scale, at the start and at five seeded places up to 10⁵ units out, and
exactly 6,077 cells scanned a scale, wherever the eye stood. No kept thing was below the grain, and no thing past the scan
would have qualified. What is held is set by the grain and the number of scales, never by how far the world goes.

This is classical level of detail. Games and maps have kept things by their size on screen for decades, and they stream
and generate their worlds rather than load them whole. The run shows only that the page does what they do, on fractions.

But it leaves a cost. Each scale held about 480 things, so nine scales held 4,351 and every scale added costs as much
again. A world at every scale, up and down without end, would still be a sum without end.

## 5. Each scale its share

The read already has a law for how its attention falls off with distance, from essay 4 and *Reads and Writes* §7: per
ratio of distance, the heat of a read is (1/π)·sech(ln(d/H)), hottest at one thumb out (d = H) and falling off as one in
2, 4, 8 thumbs past it, and the same inside it. Run 5 gave each scale that share. At k scales from the focus (the scale of
what is under the crosshair), the grain is widened by √cosh(k·ln 2), computed as √((2^k + 2^−k)/2), so the count kept
there goes as sech(k·ln 2).

Predicted first and then measured: scales 0 to 4 from the focus kept 1.00, 1.02, 1.01, 1.00 and 1.10 of the predicted
counts. Raising the top scale from 8 to 40 raised the total by 0.2%. Taking the bottom from −10 down to −40 changed
nothing. The total held was about 4.5 times the focus scale's count, against the ideal π/ln 2 ≈ 4.53, the sum of sech
over every scale. Two of the run's own predictions were killed, one by a bound of mine that was too tight (the scales
below 0 added more than I said), one by my reasoning (§6).

Then the eye was scaled down by 2⁻²⁰, a millionth, standing among things a millionth the size, and the counts were the
same counts to within 4%: the view a millionth deep is the same view.

So scales without end, both ways, cost a fixed amount, set by the grain and the share law, and not by how many scales
there are. That is the Cauchy's tail doing what it does in every essay of this series: it gives each far stretch the same
share as the last one in and the next one out, so an endless run of them has a finite total.

## 6. Nearness and distance cost the place, not the read

I expected depth to cost digits in the readings. At 2⁻²⁰ the coordinates of the eye and the things are fractions with
twenty more binary digits, and I predicted the target's slopes would carry four to thirty more decimal digits. They
carried 22 to 26 digits deep down, against 22 to 26 at the start. The prediction was killed, and the reason is plain once
said: a slope is a ratio of two reaches, and the factor 2⁻²⁰ is in both, so it cancels. It is the scale test of the whole
series, scaling the world moves no read, showing up in a count of digits.

The depth's cost was in the eye's own coordinates, about six more digits at 2⁻²⁰. The place pays; the read does not.

Run 6 made it visible on the page. G moves the eye half way to the thing under the crosshair, in exact fractions along
the line to its centre, so its direction does not move and its breadth on the screen doubles; B goes back to twice as far.
On a box 23 of its own breadths off, four halvings left the three pair slopes the same fractions, digit for digit, and
then stopped, since a fifth would put the eye inside its breadth. Four presses of B put the eye back exactly where it began.
The eye's fractions gained a binary digit a halving. A menu panel shows both counts side by side: the place, a write, paying
by the digit; the read paying nothing for being near.

Distance from the start is the same story. Until run 7 the page held its view only to about 10¹² units from where it
began, because it read the eye's exact place as a double when choosing which cells to look at, and past 2⁵³ a double
cannot count cells one by one. Now every cell is found from the eye's exact place and everything else is worked out from
the eye, the classical floating origin done in fractions. 10¹⁰⁰ units out, and a millionth of the size there, it holds
the same two thousand or so things, the same checks hold and the slopes have the same 22 to 26 digits. The eye's place
takes 101 digits.

## 7. Something to read, and K of it

What, then, does a read assume about the world? Not that the world is finite, and not that it is infinite. Tom's words
(R935): "reader math says nothing about N, other than there is an N, we just only ever know K of it."

On the page this is literal. No count of things exists in the program. A thing exists at a cell when a hash of the cell
says so; the hash is a rule, and a rule is not asked for a total. The program holds K things, about 2,000 to 2,200 at the
poses tried, and K does not change whether the field is taken to end at the edge of the scan or to go on forever.
Whether the world comes counted is the blueprint's question. A read holds K of whatever there is to read; that there is
something to read is all it says about N.

What scales, then, is whatever has a vantage: the read scales because it holds its share at each scale and the share is
summable; the write pays by the digit, for each place it puts down. The blueprint does not scale in this sense, because it
has no standpoint from which a share could fall off.

## 8. What is classical, and what is ours

Tom asked, partway through, whether this is the proof that the read's mathematics has a computational advantage over the
classical. My answer was no, and it should be said here.

- Keeping things by their size on screen is classical level of detail. Streaming and generating a world from a seed is
  what open-world games do. Exact rational turns from half-slopes are as old as Pythagorean triples. Tangent subtraction
  is a textbook identity. The grain test in squares is a classical trick for avoiding a root.
- A page with sines is not slower. The page without them is exact, and gives the same fractions on every machine; that
  is a different virtue.
- And none of this is purely theoretical: it runs, in a browser, at a few tens of milliseconds a frame.

What is ours is two things. The share law: each scale held at its Cauchy share sech(k·ln 2), so scales without end cost a
fixed total, about π/ln 2 times one scale's count. And the sorting: no count of the world enters anything the page reads;
the readings take no more digits at any depth; what pays is the place, which is a write. The classical view has the same
arithmetic available. What it does not have is a standpoint to fall off from.

## 9. Set beside a blueprint, thing for thing

After that answer Tom asked for results rather than statements (R940): "let others make those statements. lets actually
prove it with undeniable results." So the page was set beside a blueprint and the two were compared, thing for thing,
and nothing on the page says which is better (R939).

- **The same things.** A blueprint was made about the eye from every cell out to twice the read's reach, each thing kept
  by the read's own rule applied to its exact centre. The read, storing nothing, held exactly those: 0 missing, 0 extra,
  at the start and 10¹⁰⁰ units out (run 8), and at every one of 300 poses of three seeded walks (run 9).
- **The same picture.** Segment for segment, what the read draws and what the blueprint's own record draws differ by at
  most 4.5·10⁻¹³ of a pixel (run 10). The walks also found a fault: the key that backs off could take the eye below the
  ground. It now stops first.
- **What each costs.** A blueprint stored from the start out to the eye, at the scales the read holds, has 10⁵ cells ten
  units out, 10⁵² at 10²⁶ and 6·10²¹⁰ at 10¹⁰³, four times as many for each doubling of the distance; the read scans
  between 28,700 and 29,100 cells at every one of those distances and stores none (run 11, and the U key on the page).
- **A denser world.** With D things to a cell, the blueprint stored over the same square holds 35,013 × D. With its grain
  fixed the read holds D times as many things from the same cells. Held to a count K by its own tally, moving its grain
  only by what it holds, it holds between 2,045 and 2,108 things at every D from 1 to 16, looking at 1.45 times as many
  things at D = 16 as at D = 1, and still 0 missing and 0 extra against a blueprint made about the eye (run 13).
- **Two ways, the same walk.** Drawn the page's way and a classical way (yaw and pitch as floats, the frame from sines and
  cosines), 300 poses give pictures within 2.4·10⁻¹² of a pixel; the page made no trigonometric call and the classical
  way 2,400 sines and cosines (run 14). Both lay the world on a signed grid of cells and hold the eye in it.
- **Where pipelines break.** Plain float pipelines break where their formats say: single precision about 1.8·10⁵ units
  from the origin, double precision about 10¹⁴, turns drifting off square, the standard depth buffer losing a percent
  past 2·10⁴. With the classical fixes on (a moving origin over a 64-bit sector index, re-squaring or an integer heading,
  reversed depth) nothing broke out to 10¹⁰⁰; what was left were choices of width, none of them due to trigonometry or the
  two hemispheres (PWL). The page passed every one of those walls by holding more digits, and had one wall of its own: its
  rounding where a turn crossed an eighth of a full turn left 93 of 100 long walks a step off on the way back, where the
  integer heading came back exactly. Its heading is now one whole count of steps, nothing is rounded, and 100 of 100
  retraced walks come back exactly, still with no trigonometric call (run 12).

Those are the results. What they are worth beside the classical tools is for others to say.

## 10. Things that move

Everything so far stood still. The next runs put things in the sky that move, to see whether a read from somewhere still
needs no list once places change with time.

- **One velocity a scale.** Boxes at every scale, each scale moving at one rational velocity, a mover's place at tick T
  its start plus the velocity times T, exactly. The read looks at the cells about the eye less the velocity times T and
  steps nothing. Set beside every mover stored and stepped one tick at a time: 0 missing, 0 extra, places equal exactly,
  standing still, walking and from T = 10³⁰. The read looked at 29,085 cells every tick and held about 165 movers; the
  stepped list held 3,477 movers and made 695,400 additions over 200 ticks (run 15).
- **Each thing its own loop.** Then each mover was given its own path, a rectangle about its home cell with its own sides,
  heading, direction round, speed and phase, its place at tick T worked out from T alone. The read looks at the cells
  within its reach plus three. Against every mover stored and stepped: 0 missing, 0 extra, places exactly equal, still,
  walking and from T = 10³⁰; 35,833 cells every tick, 166 to 175 movers held, 95 to 106 distinct velocities among them;
  the stepped list 4,184 movers and 836,800 steps over 200 ticks (run 16). Straight flights that never end were not done:
  the cells to look at would grow with T.
- **Things that touch.** A read of places from T alone needs a law in T. To see where that runs out, 16 balls on a ring
  were let collide elastically, worked exactly contact by contact, and set beside the free law, each ball's start plus its
  velocity times T. With equal masses the set of places is the free set, and ball k sits at the free place of rank
  W(T) + k, counted round the ring, W the free paths' total windings: exact at all 40 compared times in three seeds,
  nothing kept (the set is Jepsen's, 1965; the rank was derived before the run). With masses 1 and 2 the law breaks at the
  first unequal contact; 2 balls are off every free path at first, all 16 by T = 400 (run 17).
- **On the page, and in two dimensions.** The two rings now turn in the sky of the page, the equal one drawn from T
  alone and the other stepped, each ball red once it is off every free path; the read from T alone equals the stepped
  ring at 40 times (run 18). Then 16 hard squares on a torus, worked exactly the same way: with equal masses the law
  goes at the first contact that mixes two squares' other components, and all 16 are off every free path by T = 40;
  only the sets of velocity components are kept (runs 19, 19b). One dimension was special.

So interaction alone is not where a read from T stops. A law in T is: where there is one, the read needs no list; where
there is none, the state to keep spreads to everything that has touched, and each thing has to carry its own. On the page
that state would be a stored list; in the world there is no list, only the things, each carrying its own state, which the
read meets as paint (R950, R951). Classical geometry agrees with the read wherever both apply, since they share the
geometry; the runs matched it to the digit. The blueprint is the idealization that holds the whole at once, from no
standpoint; a read always has one.

## 11. A view that holds still while the look moves

Two faults in how the view was drawn were found by using it, and both came from the focus, the scale every other scale's
grain is counted from (§5).

- **Steps.** When the thing under the crosshair changed, the focus jumped to its scale at once, and every scale's grain
  jumped with it. The focus now glides over about a quarter of a second, and what is held is kept while the eye stays in
  its cells. What is held did not change: 2,195, 4,264 and 8,654 things at densities 1, 2 and 4, 0 missing and 0 extra
  against a blueprint made (R946).
- **Flicker.** A slight pan that brushed a thing of another scale still moved the focus, and hundreds of things at the
  keep line went and then came back. Panning one step at a time, the held set changed on 44 of 120 steps, 400 to 1,500
  things each time. Now a new focus is taken only after it has stood under the crosshair for 0.4 s, or at once for the
  thing being walked toward; the same pan changed nothing for its first 58 steps (R952).
- **Dissolve.** When the focus does move, each held thing is drawn with a strength set by how far it is past the keep
  line, nothing at the line and full at 1.3 times it. As the focus glides the line moves smoothly, so a thing crossing it
  fades. Resting on a thing of a new scale, 966 things switched at once without the fade and 4 changed by half or more in
  a frame with it; still 0 missing and 0 extra (R953).

None of these changes what a read holds at a given focus. They change when the focus moves and how a crossing is drawn.

## 12. What it changes

The blueprint is god mode, and the series has no quarrel with it. It is what anyone uses who has the whole, or a bound on
it, and wants totals, joins and a map of everything at once.

What the walk showed is where it stops. Its strength is that it holds every point in one frame, and that same strength is
what ties it to the count: a frame that holds every point holds how many there are. A read is weaker: it has a standpoint,
one thumb's length held out, a share that falls off with distance, and K of whatever is there. Being weaker in that way is
what lets it go on. It can walk from the size of a house to a millionth of it and see the same view, read the same
fractions, and hold the same number of things, while the only thing that grows is the record of where it has been.

The difference, stated once: the blueprint holds the world and states amounts; a read holds K of it from somewhere and
states ratios; the place an observer stands is the one thing that has to be written, and it is the one thing that pays.

---

## Sources

- `../../plans/twk-plan.md`: the plan and runs 1–19 (predictions, tables, kills).
- `../../plans/pwl-plan.md`: where float pipelines break, with and without the classical fixes (PWL runs 1–3).
- *Reads and Writes* (`../readers-and-writers.md`): §6 "K and N" and "Something to read, and K of it" (R935); §7, the
  read's heat per ratio.
- Essay 4 (near and far), essay 16 §10 ("A world made where the view reaches"), essay 20 (scaffolding).
- Demo: `../../thumbs-walk.html`.
