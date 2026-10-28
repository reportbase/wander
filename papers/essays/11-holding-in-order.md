# Holding in order

*The eleventh of a series of essays on what can be known from where one stands. Draft, 28 October 2026.*

Stand on a pier and watch the water against a post. Every few minutes you glance at it. Is it higher than last time,
or lower? At some glance the answer changes: it was rising, now it is falling. The tide has turned. You have not
measured anything. You do not know the water's height in metres, or how far it rose, or what the gauge on the pier
says. You held one thing, where the water was at your last glance, and compared the next glance with it. That was
enough to say when the tide turned, and two people on the pier, one counting in feet and one in metres, one glancing
every five minutes and one every ten, would agree that it did.

Every essay so far has read from one standpoint at one moment, or from several standpoints at once. This one is about
reading in time: arrivals that come one after another, a reader that holds only what it has seen and has to decide what
to keep between looks. Its source is a paper of 21 August, *The Unit Rule*, which built such a reader from almost
nothing and raced it against cleverer ones. That paper was restated in the present frame on 26 October, and parts of it
were tested again, exactly and on recorded tides. This essay tells both.

Its one-line result: **a reader that holds one value and compares each arrival with it finds the turns of a stream
by order alone, and order is the one thing no change of units, no gain and no unknown scale can move.**

---

## 1. A stream through an unknown gain

Make the pier into a broadcast. A screen receives a stream of amounts, one at a time, each multiplied somewhere along the
way by a gain no one recorded. The same broadcast, sent through another chain, arrives a thousand times larger. What can
a reader holding one slot say truthfully about such a stream?

Apply the first essay's test, scale the world. Multiply every arrival by k and see what moves.
- **An arrival moves.** It is an amount, in a unit the reader was never given.
- **A difference of two arrivals moves too.** It is an amount as well.
- **A ratio of two arrivals does not move.** It is a reading.

So the first thing the reader can say about the broadcast, rather than about the chain it came through, is one arrival
in terms of another. And the very first arrival, alone, says nothing. It fails the test. It founds what the reader will
hold, and that is all.

The same test sorts instruments. A balance passes it: its field cancels from the equilibrium, so a balance that reads
equal on the moon reads equal on the earth, and sweeping the field over twelve decades leaves the reading where it was.
Bias one pan and the reading drifts at once, which shows the cancellation is doing work. A spring scale fails: it reads
mass times field over stiffness, so it must be calibrated, and only where it was calibrated. The reader in this essay is
a balance. Whatever settles each comparison decides *that* a result occurs and contributes nothing to its value.

---

## 2. One slot

To read an arrival against something, the reader must already hold something. Call it **the hold**. Each look states one
reading: the arrival in terms of the hold. In the second essay's notation that is a direction,

  [hold : arrival],  with v/h = arrival ÷ hold.

The landmarks are the ones every essay has met.
- **Home**: the arrival is nothing, v/h = 0. The screen shows black, truthfully.
- **The corner**: the arrival equals the hold, v/h = 1. Nothing has changed.
- **The horizon**: the hold becomes small against the arrival. A register of finite size cannot follow the reading
  there; past its last level everything reads the same, and that clip is the register's edge, not an error.

*The Unit Rule* specified its reader as a short list of capabilities, each paid for in state, never in a unit.

| | capability | what it needs |
|---|---|---|
| 0 | reception: arrivals in order | nothing |
| 1 | relation: the arrival read against the hold | one held value |
| 2 | representation: the reading named by its level | a step g |
| 3 | continuity: something held across the gaps | a carry rule |
| 4 | landmark: the corner crossed, and counted | a direction bit and two counters |

No row needs the stream's scale. What grows down the table is memory.

**Holding is its own axis.** The earlier essays said that a reader receives either amounts along given directions or
directions alone, and that either may be held at once or in order. This essay is about one corner of that second axis:
holding in order, with one slot. It is not a claim about how readers in general work. A camera holds a whole frame at
once; this reader holds one value and the next arrival.

---

## 3. The levels, and the step

The register names each reading by a whole number of steps of a ratio g greater than 1: the level n nearest
log_g(arrival ÷ hold). The run of those numbers is the record.
- **The step is the reader's, not the stream's.** Nothing in the broadcast recommends a g. A finer step buys resolution
  and costs levels.
- **One step, repeated, is the only discrete design.** Every discrete set of ratios closed under multiplication is the
  powers of one ratio. Two unrelated ratios together, 2 and 3, are dense: their products come as close as you like to any
  ratio at all. The fourth essay's "levels are one ratio repeated" is this.
- **The count of levels is a logarithm in whole numbers.** "How many steps of g from the hold to the arrival" is log_g,
  rounded. The reader computes no logarithm. The logarithm is what its count becomes when the steps are made fine. This
  is the fourth essay's lay past the corner, 1 + ln s by count of addresses, met in time.
- **A logarithm of one amount is not formed.** A level needs two magnitudes, a hold and an arrival. "The logarithm of
  five metres" is not forbidden; it is not yet a reading.
- **The count does not carry the world's size.** Scaling the stream shifts the hold's level and leaves every reading
  where it was. The reader's count of levels is fixed beforehand, the fourth essay's K, apart from whatever N the stream
  has.

**Odd and even K.** The fourth essay noted that with an even number of levels the corner, v/h = 1, falls on a boundary,
and with an odd number one level is centred on it. For this reader the choice is not a matter of taste. Show a one-slot
reader a still scene and it is handed its own hold, look after look, with its reading sitting exactly on the corner. With
31 levels it returns the hold times 1.00000. With 32 it must round half a step one way or the other, and returns the hold
times 1.01815: a twitch on every look of a scene that is not moving. A reader that must be able to say "nothing changed"
needs an odd K. Other readers need not.

---

## 4. The unit rule

At the end of a look, the reader's stock is the old hold, in a slot; the arrival just read, in a slot; and the count of
looks. Nowhere is there a rate, a trend or a step toward the future. "Carry the hold forward by s" needs an s, which is an
amount. "Continue the motion" needs a motion, which is a difference, which is also an amount. The only magnitude the
reader holds is the one that just arrived.

So the rule:

> **Hold the arrival that filled you, until the next one says otherwise.**

It assumes nothing about the stream and costs one slot. It is the rule a reader given nothing can run. The held value is
the reader's unit for the moment, which is where the rule's name comes from.

It has two outputs.
- **A level.** Each arrival is placed against the hold, which is what makes the stream readable at all.
- **The corner, as an event.** The look at which the reading crosses 1. Two readers with different steps and different
  gains find the same look, because a crossing of 1 needs no scale. That is the pier: the turn of the tide, agreed by
  people counting in feet and in metres.

**Reference and carry are two jobs.** Any rule governs two things: the reference, what each arrival is read against;
and the carry, what is held between looks when nothing arrives. The unit rule does both with one value. Rules that try
to beat it usually change the reference, with a forecast or a trend. A rule told the stream is smooth fills in the
carry. Only the carry matters in the gaps, and the gaps are where section 7 finds the rules apart.

**The space of rules is open.** For every known stream, some tailored rule beats this one, and pays for its advantage
with information about the stream. The unit rule is the one member of the space a reader given nothing can run.

---

## 5. Reading is seeking

A reader with a finite register has to keep its hold near the arrivals, or the arrivals run off the edge. *The Unit Rule*
proved that this is not optional. Its premises: the reading is the arrival's level less the hold's; the register reads
while that difference is at most R and clips otherwise; the stream steps at most J levels a look and is told nothing
about the reader; the reader knows no window the stream will stay in, since that would be a unit.
- **A hold that never moves** is clipped after finitely many looks, for some stream.
- **A reader reads every stream** exactly when its hold tracks the arrivals, within R. It must keep returning to the
  corner.
- **"Hold while the reading is within one level, else move the hold to the arrival"** keeps the reading within J, with
  no model of the stream. The price of knowing nothing is a lateness of one of the stream's own steps.

This is the fourth essay's "the corner follows the focus", met in time. And the band, hold until the reading leaves ±1,
is a device found twice: a playground study of a first-person view found that re-laying the corner only when the look
had left a band of 0.4 levels about it moved the corner on one look in twenty, for 1% more coarseness. A reader moves
its corner only when the look has left a band about it.

What the snap buys is not accuracy but **stretches of agreement**. At the look where the hold moves, the reading is
exactly 1. Until the next look contradicts it, one statement holds for the whole stretch, and the record is the list of
the stretches' ends. A predicting rule moves its hold every look, so it has no stretches and no ends. On a random walk the
predictor's reading changes sign at 67% of looks: a beat. The unit rule's changes sign at 31%: a drift. Over 2,000 looks
it held 1,622 times and moved 378. Where a model is exactly right, a constant trend, the predictor sits at agreement every
look and the unit rule wobbles. A predictor's stillness is borrowed from its premise. The unit rule's holds whenever
nothing has left the band.

Measured over 20,000 looks with a register of 15 levels and a stream that steps at most one: a fixed hold is clipped on
18,087 looks of a random walk, 19,975 of a trend and 18,350 of a stream that turns every 200. The unit rule is never
clipped; its worst readings are 1.99, 1.20 and 1.80 levels. A linear predictor is never clipped either, and its worst are
1.98, 0.60 and 1.80. Its advantage is gone once the stream turns.

---

## 6. The side bit: the median, at the corner

An arrival above the hold or below it is one bit, and it needs no collecting. Step the hold a little toward whichever
side keeps winning, and it settles on the arrivals' median. That is Robbins and Monro's sign rule (Robbins and Monro
1951), the oldest stochastic approximation there is.

The median, and not the mean, is the reading's centre for the third essay's reason: the median commutes with every
increasing change of what arrives, and the mean does not. On a heavy-tailed test stream of median 10 (heavy-tailed so
that its mean would not settle), the drift of the hold changes sign exactly at the median: +0.77 a look with the hold at
2, −0.02 at 10, −0.93 at 40. The hold settles at 9.25 while the running mean wanders to 16.09. On a lognormal stream of
median 1 the hold settles at 1.11, with the mean at 1.69.

Once the hold sits at the median, the far arrivals cancel: of 50,335 arrivals past 16, 24,145 were above the hold and
26,190 below. That says they no longer move the hold. It does not license ignoring them. A reader that clips before its
hold has settled strands itself: told to ignore arrivals four levels from its start, it ignored 99.8% of looks and left
its hold at −101 on a stream of median 10.

---

## 7. The races

*The Unit Rule* raced its rule against rules meant to beat it, on 49 recorded test signals, each of which returns to
where it began, so an honest record should add up to zero. Those measurements were made there and not run again; they
price the rule, and they answer a writer's question, how closely the held values track the stream's amounts.
- **The rule's own frontier.** Its median error falls as about 2 to the minus the number of bits it spends a look, with no
  knee: 0.0132 at 0.635 bits, 0.0064 at 1, 0.00020 at 4.5. Any rival has to beat that line.
- **A tailored step,** like a camera's auto-exposure, is 2.3 times better at the median and 3 times worse at the worst
  look, and its records close on 2 of the 49 signals against the unit rule's 49 of 49. A step that changes during the run
  states its symbols in different units, and the sum stops adding up.
- **The unit rule with more levels** at the same bill beats the tailored step's worst look sixfold and still closes on all
  49.
- **An oracle** given the whole schedule in advance is 28 times better. Four fifths of that is a finer level, which the
  unit rule can buy too. Offset the oracle by one sample and it clips 536 times.

The paper's summary stands: **at a matched bill, with every guarantee kept, sophistication buys about 1.2 times.** Every
larger figure was more levels in disguise, a handicapped baseline or a guarantee given up. Beating the rule costs
information about the stream, and when that information is wrong the cost is paid in the worst look, the clips and the
checksum.

---

## 8. The turn as a landmark

The question where the rule wins by much more than 1.2 is not "what was the level" but "where did the stream turn". A
turn is the sign of the reading changing: the arrival stops exceeding the hold and starts falling short. Two readers with
different steps and gains agree that it happened. A count of looks between two turns is a duration in the stream's own
terms, so the reader carries a reference it was never handed. That is designating, not sizing: the turn is a place in
the stream, not a size of anything.

**The race in the gaps.** The rules differ only across missing looks, so looks were dropped, singly and in bursts, with
the same machine and the same turn logic and only the carry different. The error in the turn's place:

| looks dropped | unit rule | carry the trend | decayed blend |
|---|---|---|---|
| none | 1.61% | 1.61% | 2.44% |
| one in five | 2.08% | 2.01% | 2.82% |
| half | **3.01%** | 60.58% | 4.31% |
| four in five | **6.55%** | 27.28% | 8.91% |
| bursts of 20 | **1.72%** | 23.41% | 2.56% |
| bursts of 200 | **1.66%** | 11.24% | 2.51% |

The reason is structural. **A carry that extrapolates is most wrong exactly at a turn**, the one place where "it went on
as it was" is false by construction. The unit rule's carry grows wrong in size across a gap, but it asserts no direction,
and direction is all a turn needs.

**A machine with four registers.** A rod turning steadily is read once a look by its projected length. The corner, where
the rod's two projections are equal at 45°, falls a quarter of the way along each half turn. Four registers find it: the
hold, the direction bit, a counter from the last low reversal, and the previous leg's count. The quarter needs no
division: a counter that ticks every fourth look holds the count quartered. On a clean signal it finds the corner to 1.9%,
all of it the lateness of noticing a reversal; on a noisy one, 1.9% at 0.4% noise, 3.1% at 1%, failing at 2%. A reader
that keeps every arrival and sorts them does better, 0.05%. The four-register machine is not more accurate. It is possible
on a stream without end, with memory that does not grow.

---

## 9. Tested since: why order wins

The races were measurements. On 26 October the question of why the unit rule wins in the gaps was put as predictions,
written first, and run exactly and then on recorded data. Five carries were raced: the unit rule, the median of the last
three, an additive trend, a ratio trend and a blend.

**Exact streams.** A carry's turns are unchanged by exactly those changes of what arrives that its reference commutes
with.
- The unit rule and the median of three hold order alone, so no strictly increasing change of the stream moves a turn
  they report.
- The ratio trend holds the ratio's motion, so powers of the stream leave it and other changes move it.
- The additive trend and the blend hold amounts, so every change that is not a straight-line one moves them.

The unit rule reported every turn once, with no false turn, within the two received looks after it, whatever the gaps.
The trend rules reported inflections instead, a fixed fraction of a cycle off. So the advantage in the gaps is not
tuning. It is the third essay's theorem in a stream: a turn is an order statistic of the arrivals, and a reference built
from amounts answers a different question. (The first run was killed by floating-point ties, the bounds I had set and my
scoring window; the second, at 60 digits, killed nothing.) Scaling the world does not separate the rules, since every one
of them is unchanged by it. The order test does.

**Noise and a threshold.** A threshold is an amount, and the unit it is written in decides what it costs. A debounce on
order alone, three opposite signs in a row, keeps every increasing change. A threshold in levels keeps only the scale of
the world. A threshold in amounts keeps neither. The price of order alone is noise: it makes false turns once the noise is
a few percent of a look's change, where a threshold in levels makes none at five times that noise or more.

**A recorded tide.** Then the pier, for real: NOAA's six-minute water levels for September 2026 at San Francisco and
Boston, with NOAA's own published highs and lows as the independent record of when the tide turned. The split held
exactly on data no one made for the test.
- Order alone gave the same turns under a change of datum, metres to feet, and a cube of the heights.
- A threshold in amounts kept the datum and lost the unit.
- A threshold in levels kept the unit and lost the datum.

Order alone, with no threshold, reported exactly one turn between each pair of NOAA's highs and lows at Boston every six
minutes, and at both stations every eighteen. It was the earliest of the detectors there. Where the water wiggled more in
a look than the tide moved, at San Francisco every six minutes, it made extra reports. Looking less often bought order
back, with no threshold at all.

**How often to look.** A rate of looking is a choice of looks, not an amount, so it costs no invariance. Three more runs
asked which rate makes order alone exact.
- At five stations read every 1 to 30 minutes, a rule from the noise's size and persistence was right where the noise
  held its direction, and four to five times too cautious where the noise was new every minute: order is not fooled by
  noise that keeps no direction. Temperatures changed from Celsius to Fahrenheit kept their turns only under order.
- A rule fitted on September failed on August, but each station behaved the same from month to month, and after the fact
  the behaviour lined up with how much the water wiggled on the scale of 10 to 60 minutes against how sharply the tide
  turns.
- That rule, fitted on September and August, was tested on July at ten stations, five of them new. It called the class
  right at 9 of 10, the starting rate within a factor of 2 at all five it called exact and equal at three, and ranked the
  stations with correlation 0.93. One late report, at one of ten offsets at Juneau, killed the clause "exact at every rate
  past the start".

The pier, then, in one sentence:

> **Holding order alone with one slot keeps every increasing change of what arrives, on real data as on exact streams.
> Its one setting is how often it looks, and the wiggle near a turn, against how sharply the signal turns, says which.**

That rule for the rate was fitted on tides and has not been tested on anything else.

---

## 10. Every rule's corner marks what it believes

Every rule holds something, so every rule has a look where the arrival meets what it holds. What that look is about
depends on what is held.
- **The unit rule** holds the last arrival. Its corner says the stream did not change: a statement about the stream.
- **A trend rule** holds a forecast. Its corner says the forecast came true: a statement about the reader.

On a turning rod, the unit rule's corners gather at the turns (31.5% near a turn against 13.4% on a flank) and the trend
rule's on the straight stretches (21.2% against 41.5%). The same law names the unit rule's blind spot. A stream climbing
exactly one level a look is as quiet to it as a still one: a steady geometric ramp is all corners under every rule.

---

## 11. What the record is

**A projection, not a loop.** Every value the unit rule holds is a level of the lattice anchored at the founding arrival,
and rounding from any level lands on the level nearest the arrival. So the held run is the nearest-level projection of
the stream, the same whatever path led there. That was verified in exact integer arithmetic on every sample of 56 scenes.
A held value grows stale within a gap; it does not decay across a run.

**Continuity is the reader's.** Arrivals come one at a time; the held run is unbroken because the reader holds something
between looks. What is forced is that there is a carry rule. Even "hold nothing" is one, and gives a strobe. Which rule is
not forced. Continuity in a record is the carry rule, whatever it is.

**Two checksums, both needed.** The sum of the symbols telescopes to zero on a scene that returns, and ignores order. The
sequence of crossings, corners passed and clips, must come round to where it began, and keeps order. Neither implies the
other, and both can only refute: a scene ending within half a level of its start rounds to "returned".

> **An open record proves the scene did not return. A closed record does not prove it did, and how much it can refute is
> set by the step.**

Closing also needs the horizon resolved. On a loop 40 levels high, every register from 64 levels down to 4 closes while
the largest step between looks is 1.1 levels. At 40 looks a lap, a register of 4 is clipped on 152 looks and the record
sums to −30, the same −30 every lap: the excursion past the horizon, lost the same way each time. The corner agreed makes
the sum telescope; the horizon resolved makes it telescope to the right total.

---

## 12. Periods, and what a shape does to them

One more result from the August paper reads cleanly in this frame. Divide a stream by its own increment. For anything
locally like a sine wave, the ratio is the tangent of the phase: an address, with the gain cancelled. From that, the
period of a single tone comes back from 55 Hz to 3 kHz within about 1%, unmoved by any scaling of the stream, and cross
ratios come back exact to 10⁻¹⁰ or better on every stream tried, video included.

The paper put the lesson well: **if the shape survived into the reading, the rate could not be recovered.** Swept at one
rate and read as a direction, a circle, an egg, a clover and a burr give one period, a spread of nothing. Read keeping the
shape, they spread over seventy percentage points. That is the third essay's theorem again: the reach of what arrives
cancels from every reading.

And the frame is exact over any arrivals at all: white noise gives a crossing and a cross ratio as cleanly as a tone.
**Its exactness is no evidence that it refers to anything.**

---

## 13. Open

Four questions are left.
1. Does the corner found this way follow a change in the world, or only a change in the sampling?
2. Do two readers at different rates agree, once each counts in levels from its own corner? For turns this is partly
   answered: readers holding order alone at any rate inside a station's exact window report the same turns, one between
   each pair of the tide's highs and lows. Counts in levels from each reader's corner were not compared.
3. Does the frame earn anything where a unit is available anyway?
4. Is the unit rule's ±1 band the same reader as the first-person view's band of 0.4 levels? A test would race them on one
   trace.

---

## 14. What it comes to

**Reading and writing.** A reader holding in order with one slot holds only readings: each arrival in terms of the last.
It can say when the stream turned, how many looks lay between turns, where the stream's median is, and whether its record
closed. It cannot say how high the water was. That needs a gauge and a datum, a unit and a zero carried in: a writing.
The races priced the difference. Rules that hold amounts track the amounts better, by about 1.2 at a fair bill, and lose
the turns in the gaps by seven to fourteen times.

**The Cauchy.** It does not appear in a stream as a law of the arrivals; the arrivals are whatever they are. It appears,
as everywhere in these essays, in what the reader keeps: order and the median, the corner as a crossing, a statistic that
no increasing change of what arrives can move. The tide was a test of exactly that, and it held at ten stations.

Back to the pier. You glanced at the water and compared it with your last glance, and at one glance the answer changed.
You did not know how high the water was, and you did not need to. Two people counting in different units, glancing at
different rates, found the same turn, because a turn is the one thing about the tide that no unit can move.

---

## Sources

- Robbins, H. and Monro, S. (1951). A stochastic approximation method. *The Annals of Mathematical Statistics* 22(3),
  400–407.
- NOAA Center for Operational Oceanographic Products and Services (CO-OPS): verified water levels and published highs
  and lows, July–September 2026, as recorded with their retrieval dates and checksums in `plans/unr-plan.md`.

The August paper is kept as received in `papers/archive/the-unit-rule.md`. Its restatement in the present frame, with every
measurement quoted here and the seven readings it corrected, is `papers/unit-rule.md`. The runs of 26 October are in
`plans/unr-plan.md` and `runs/unr/`.
