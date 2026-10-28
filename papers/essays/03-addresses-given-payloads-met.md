# Addresses given, payloads met

*The third of a series of essays on what can be known from where one stands. Draft, 28 October 2026.*

The first essay found that a reader with no second length still has a circle, and that read from where it stands the
circle is the Cauchy distribution. The second showed how one length turned gives that circle, and how two sweeps of it
read the same point twice. This essay is about the Cauchy itself: what it is a law *of*.

The usual answer is that it is a law of something measured: noise, a spectral line, a ratio of two measurements. The
answer here is that it is the law of the places where measurements can be put, the reader's *addresses*, fixed before
anything is measured at all. What arrives at those places, the *payload*, is a different thing with a law of its own.
That one distinction explains a habit practice already has, and says when the habit stops being right.

---

## 1. A hand at a window

Stand inside a church and hold your hand up against a stained-glass window, fingers spread from flat to upright. Each
finger lines up with one pane, and each is lit by the colour that pane lets through: red here, blue there, gold at the
top.

Two different things are on your hand.

The fingers are one. They point in fixed directions, spread from flat to upright, and they would point the same way in
any church, at any window, in the dark. Nothing the window does moves them. They are the places the colour can be put.

The colour is the other. It is whatever came through the glass along each finger's line. Change the window and every
colour changes. Turn off the sun and they all go dark. The colour tells you about the window. It tells you nothing about
how far away the glass is, or how large: a window twice the size, twice as far off, lights your fingers in exactly the
same way.

The essays call the fingers **addresses** and the colour the **payload**. The claim of this essay is that the Cauchy
distribution belongs entirely to the fingers. It is the law of how the fingers are spread, and nothing the window does
can change it.

*Demo: the central reader, step 1 (the hand, its fingers laid by the turn, painted by the light).*

---

## 2. How the Cauchy is usually read

The Cauchy law has been read in five main ways, and each is correct on its own terms.

**A counterexample.** It entered probability as an exception. Poisson met it in 1824, as Stephen Stigler has recounted,
as a case where averaging many observations is no better than one: the mean of any number of independent Cauchy
variables has exactly the law of a single one. Cauchy returned to it in 1853 in a dispute over least squares. Textbooks
keep it in that role, the standard example of a law with no mean and no variance, which the central limit theorem does
not reach. "Pathological" is the word often used.

**A stable law, and a ratio.** It is the stable law of index one: add independent copies and the shape is kept, only
the scale grows. It is the law of the ratio of two independent centred normal variables, and Student's t with one degree
of freedom. In these readings it is a law of amounts, numbers that add, divide and are averaged, which happen to have
heavy tails.

**A tail to guard against.** In statistics it is the stress test for estimators. The sample mean fails on it; the
median, and the robust estimators built in the 1960s to bound the influence of any one observation, do not. The heavy
tail is read as a fact about the data, outliers that come with them, and the remedy is to read the data by their order.

**A line shape.** In physics it is the Lorentzian, the profile of a resonance or of a decaying state's spectral line,
falling to half its height one half-width from the centre. There it is read as a property of the system: the line is
broad because the state decays.

**The tangent of a uniform angle.** Geometrically it is the tangent of an angle turned at a steady rate. A lighthouse
lamp turns, flashes at random moments, and its flashes land along a straight shore; their places are Cauchy. This is the
lighthouse problem of the Bayesian textbooks. The law is carried into itself by every map that moves points of a line
while keeping it a line, and it is where a randomly wandering particle released above a line first touches it. This
reading is the nearest to the one here. It makes the law a fact about directions, but about the directions of a lamp or
a wandering path, not about the places at which a reader meets what it reads.

---

## 3. What the readings share, and the other place a law can live

In every one of those readings, the Cauchy is a law of something measured: values that lack a mean, data with outliers,
a system's response, a lamp's flashes. Its missing mean is then a defect in what is measured. Robust methods manage it,
or the physics explains it.

There is another place a law can live, and E. T. Jaynes pointed to it in 1968. Jaynes was working on a hard problem:
what probabilities to assign when you know almost nothing. His answer was to ask what transformations of the problem you
genuinely cannot detect. Can you tell which way you are turned? Can you tell what unit your ruler is in? Whatever you
cannot detect, your assignment must not depend on. The transformations you cannot detect form a group, and a group
leaves exactly one measure unchanged. Jaynes called it the *invariant measure* and wrote it m(x). He was clear about its
status. It is not a belief about any outcome, and not a frequency of outcomes. It is a reference, there before any data,
against which other distributions are measured.

This essay puts the Cauchy in that place. For a reader at a standpoint, two things cannot be detected from the readings
alone: which way it happens to face, and how large anything is. Turns and rescalings. The turns leave one measure on the
directions, the steady turn; read as the slope v/h, that measure is the Cauchy. It is the law of the reader's addresses,
fixed by the standpoint and the turn, before anything arrives.

On this reading the missing mean is not a defect of anything measured. It belongs to the scale on which the directions
are written. Write a direction as its slope v/h and the scale runs to infinity at the vertical, and there the law has a
median and no mean. Write the same direction as its angle, a bounded scale from 0 to 90°, and the same law has a mean
like any other. The missing mean belongs to the chart that sends the horizon to infinity, not to the world.

The five earlier readings stay correct. What this reading adds is a way to say which of their facts belong to the
addresses and which to what is met at them.

---

## 4. An address is not a payload

The two are different kinds of thing.

An **address** is a point: a direction, a place on the reader's layout. A **payload** is what is found at that point: an
amount, a colour, a strength. The law of the addresses, the Cauchy, is a measure on the points. It is fixed by the
standpoint and the turn alone. No payload enters it.

Whatever arrives can be swapped for anything else, at any address, and the addresses and their law do not move. So
nothing the Cauchy says, its median, its spread, its missing mean, is a statement about the payload, and nothing about
the payload can be read from it. The two share one place, the point where an address meets what it points at, and
nothing passes between them there.

Why say this out loud? Because a number on a page carries no mark of which it is. Write a direction as a single value
x = tan θ, a number on the real line, and the same number is both *where* a reading is made and *what* is read. Nothing
in the notation separates them. Mathematics separates direction from magnitude in many other places: polar coordinates,
a unit vector and its length, the projective line where a direction is a ratio [x : y] and not a value. A Cauchy
variable written as a plain number is not among them. So the law of the turn gets read as a law of amounts, and a mean is
asked of it.

This is a point about notation, not about anyone's results. Unmarked, the two kinds of thing look identical. Marked,
they separate exactly.

---

## 5. The theorem, in plain words

The separation can be stated as a theorem. Each part is elementary; the content is in reading them together.

**Nothing that arrives changes the addresses.** Suppose that whatever arrives along each direction lies at some distance,
different from direction to direction and unknown to the reader. Its two components are that distance times h and that
distance times v, and the reading is their ratio, v/h. The distance cancels. It cancels from every single reading, not
on average. So the readings, and their Cauchy law, are the same whatever arrives, and they are fixed before anything does.

**Order survives every change of payload.** Take any set of readings and apply any transformation that keeps their order:
stretch them, square them, take logarithms, anything that never swaps two of them. Their ranks do not change, so their
median, their quartiles and every statistic built from order pick out the same element as before. And ranks keep exactly
what survives every such change, and nothing more.

**Sums do not.** The mean is different. Among all the order-keeping transformations, only the straight-line ones,
stretching and shifting, commute with the mean on every set of readings. Any other changes the answer. The mean belongs
to amounts, which can be added. It does not survive a change of what the numbers stand for.

**The Cauchy is an address law.** Over a quarter turn its median is v/h = 1, the corner. Its quartiles are √2 − 1 and
√2 + 1, about 0.414 and 2.414, a reciprocal pair, mirror images across the corner. It has no mean: the running average
grows without bound.

**The median needs only fairness.** The last part drops the circle and the steady turn altogether. Take any path from all
of h to all of v, with any weighting, provided both are unchanged when the two parties swap roles. Then the corner is the
median, whatever the path. If, in addition, the path reaches all the way to the vertical with some weight there, the
mean does not exist. So the median at the corner and the missing mean are not special to the Cauchy. They come from
fairness between the two parties and from reaching the horizon. What the steady turn on the circle adds is only the
Cauchy's exact shape.

Taken together: the addresses are given before anything arrives, and nothing that arrives moves them. That holds for
every single reading and for every statistic of their order, and no statistic of size can be read from them. The Cauchy
is where the reader can put what arrives, never what arrives.

**The geometry creates the reader.** It is tempting to picture the reader doing this work: taking two amounts and dividing
one by the other, so that the scale cancels. It does not. The geometry removes the scale before anything is read. A
direction arrives as a direction, with the distance along it already gone; the projection did the dividing, not the
reader. What the light paints on a direction arrives as paint, never as so many units. So the reader manages no
magnitudes at all, neither the size of the other party nor the size of what arrives. It has no unit to manage them in.
Its one length, H, is its own unit: measured in itself it is 1, and what it is in metres is something only a writer can
say. The reader has no scale whatsoever. Every magnitude, and the unit it is stated in, belongs to the writer.

*Demo: Theorem 6 at a glance: scale, reshape, reshuffle or thin what arrives, and no address moves.*

---

## 6. Once a Cauchy, always a Cauchy

A law that is really the reader's layout of directions should survive everything the reader can do to directions. It
does.

| what the reader does | what the law does |
|---|---|
| starts again from a new zero (a turn) | stays Cauchy |
| swaps the two parties (the reciprocal) | stays Cauchy |
| rescales its drawing, or zooms | stays Cauchy, at another scale |
| relays through a standpoint in between | stays Cauchy (this is the sum) |
| averages several readings | stays the same Cauchy: nothing gained, nothing lost |

Each operation moves only the law's one point, written m + iγ: the foot of the standpoint and its height above the line.
These closure properties are classical. The reading is that the family is closed because it is the reader's addresses,
and that its one parameter is where the reader stands.

The sum deserves a word, because it looks like amounts being added, and is not. Picture a standpoint at height γ₁ + γ₂
above a line. Turn steadily from it and land on a line at height γ₂; take that landing as a new standpoint and turn again
down to the bottom line. Where you land is the sum of two Cauchys, of scales γ₁ and γ₂. It is exactly where one steady
turn from the first standpoint would have landed. What adds is the heights of the standpoints. The sum itself is still a
direction from the combined standpoint, with no mean. A sum of Cauchys is a relay of standpoints.

The normal distribution is the Cauchy's counterpart among amounts. It is closed under sums and rescalings, the
operations on amounts, and not under ratios or turns. Take the ratio of two independent centred normals and you get a
Cauchy. Taking a ratio carries the one law into the other.

### What breaks it

Only operations that are not operations on directions. Squaring a reading. Cutting the line off at an edge, as a flat
screen of finite width does. Multiplying each reading by an amount that varies. Adding an amount to each reading, as the
thermal motion of atoms adds a Doppler shift to every address of a spectral line, which turns its profile into Voigt's,
normal near the centre and Lorentzian in the wings. Pooling readings taken from different standpoints without relaying
them. Counting the turn against a lopsided clock. In every case an amount has entered.

And there is a pattern in how it breaks. When an amount of limited spread is added, the Cauchy is lost first near its
centre and last at the horizon: the far tails keep their Cauchy form to the end. That is why astronomers can still read
a spectral line's natural half-width from the far wings of a Voigt profile. Only cutting the line at an edge, or taking a
power of the reading, takes the tails.

Those three properties together are what make the Cauchy usable as a set of addresses.
- A reader can sweep with it and stay in the family.
- The payload can be changed at every address and no address moves.
- Where an amount enters, the law gives way from the middle outward and keeps its horizon to the last.

---

## 7. A test: find the turn, find the amount

The reading gives a rule, offered as a reading and not as a law of nature. A Cauchy variable is a direction, never an
amount. Where a Cauchy appears beside an amount, the two are separate factors: the amount is the payload, the Cauchy is
where it lands.

So for any Cauchy met in practice there is a test: **find the turn, and find the amount.**

- **The lighthouse.** The lamp turns; that is the turn. The flash is the amount.
- **A ratio of two normal measurements.** The pair of measurements is a point in the plane. Its direction is uniform,
  because two independent normals of equal spread look the same in every direction. That is the turn. Its length is the
  amount, and it cancels from the ratio.
- **A spectral line.** Spectroscopy already writes a line as a strength times a profile. The strength is an amount, in
  physical units, and the strengths of separate lines add. The profile of a resonance is laid by a phase that turns
  through half a turn as the frequency crosses the line; that is the turn. Spectroscopists read the profile by its centre
  and its half-width, which for a Cauchy is half the distance between the quartiles, and they read the strength by its
  integral. That is the address by its order and the amount by its sum, which is exactly how the theorem says each must
  be read.

Practice got there first. The reading says why it got it right.

---

## 8. What the reading changes

The theorem is classical in its parts. Here are four cases where the reading lets one say something cleanly. Their
answers are known. What the reading adds is where each answer's facts belong.

**Water and wine.** Richard von Mises posed it in 1928: a glass holds wine and water, and the ratio of wine to water is
somewhere between a third and three. What is the chance it is at most two? Spread your ignorance evenly over the ratio
and you get 5/8. Spread it evenly over the inverse ratio, water to wine, and you get 15/16. It is the standard case of
the principle of indifference contradicting itself, and Jaynes left it open. Read as an address, the ratio is a direction,
[water : wine]. Swapping the liquids carries it to its reciprocal, so every answer that treats them alike puts the chance
of at most one at exactly a half: the corner, whatever else is assumed. And if one law must hold on every range of the
ratio, as Jaynes required in his own problems, the only law left is the one even in levels, and the answer is ln 6 over
ln 9, about 0.816.

**The marginalization paradox.** In the 1970s Philip Dawid, Mervyn Stone and James Zidek showed that, under certain
improper priors, two reasoners from the same data can disagree. One integrates an unknown scale out of the likelihood;
the other reasons only from statistics free of the scale. Read with the reader's own measure on the unknown size, the
one even in levels, they cannot disagree. The second reasoner is reading the data's direction, its address, and the
scale's invariant measure is exactly what makes the two routes agree, whatever the law of the data.

**Bertrand from a standpoint.** Joseph Bertrand asked in 1889 for the chance that a chord drawn "at random" in a circle is
longer than the side of the inscribed equilateral triangle. He got three answers, ⅓, ½ and ¼, from three procedures, and
concluded that "at random" means nothing until a procedure is named. Jaynes answered ½, from the requirement that the
answer survive turning, resizing and moving the circle; straws he tossed onto a circle agreed. A reader standing
somewhere cannot move the circle, because its lines all pass through where it stands. For a circle whose centre is a
distance D away, D at least its radius R, the reader's share of long chords is arcsin(R/2D) divided by arcsin(R/D). Seen
from a point on the circle it is ⅓. As the circle recedes it rises to ½. Jaynes's answer is the far reader's; one of
Bertrand's is the near reader's. The answer depends on where the circle lies relative to the one who asks.

**Directions are read by their order.** Robust statistics treats a Cauchy tail as outliers, to be resisted. Read as
addresses, the same readings need no defence. A ratio of two amounts, a slope, the tangent of a bearing: each is a
direction, and on the slope scale its law has a median and no mean. Over a steady turn the median stays at 1, while the
part of the mean contributed by readings up to any reach climbs by the same amount, about 1.47, for every tenfold
further the reach goes, and never settles. So: to summarize directions, take
the median or the quartiles. To combine two, compose them as turns. To average, average the angle, which is bounded.

*Demo: sweeping from zero, the turn counted against itself and against other clocks.*

---

## 9. What is observed, and a test that can fail

The address law is not the law of anything observed, and it is easy to run the two together. Every Cauchy met in
practice, a ratio of measurements, a heavy-tailed sample, a line's profile, is the law of something observed. The reading
relates them.

Counted against what arrives, the readings' law is the turn's law *weighted by how what arrives is spread over the
directions*. It is the Cauchy exactly when what arrives is spread evenly over the reader's addresses, as a pair of
independent normal measurements of equal spread is. Otherwise it departs from the Cauchy, and the departure is that
spread, which can be measured on its own.

That makes a claim the usual readings do not, and the claim can fail. An observed law of Cauchy type should have a steady
turn behind it: a rotation, a phase advancing steadily, or the direction of a pair of independent amounts of equal
spread. Its departure from the Cauchy should be accounted for by the spread of what arrives, measured independently. Its
median should stay at the corner exactly when that spread weighs the two sides alike. A Cauchy-type law with no turn to
be named behind it, or a departure the measured spread does not explain, counts against the reading. Writing a law as the
tangent of something does not pass the test; the turn has to be there.

### The second test

The first essay gave a test for reading against writing: scale the world, and see what moves. Here is its partner, for
address against payload.

**Change what arrives, and keep the directions.** Replace what arrives along each direction with something else. A
quantity that does not change belongs to the addresses. A quantity that changes belongs to the payload.

Together the two tests sort any fact four ways: readings of the addresses (the corner, the quartiles of directions),
readings of what arrives (a colour, a ratio of intensities), and writings of either (a range in metres, a flux in a
unit). Neither test needs this essay's vocabulary to run.

---

## 10. Three cases in data

**Gravitational-wave noise.** The LIGO detectors at Hanford and Livingston record a strain that, after whitening, is
mostly noise. Take one detector alone, sample by sample, and a Cauchy fits its values far better than a normal
distribution does, which might suggest a Cauchy in the noise. Read the other way, it is not. The tail is finite, made by
one loud transient: a Student t with about sixteen degrees of freedom fits far better than either. Averaged over blocks,
the values shrink as one over the square root of the block length, which nothing with a Cauchy law could do. The values
are amounts, and they behave like amounts.

The Cauchy is elsewhere: in the *direction* of the pair, Livingston against Hanford, read at the same instant. That
direction is close to uniform by turn. Drawn at one length by each channel's own spread, the median ratio sits at 0.999,
the quartiles at −0.998 and +1.000, and averaging over blocks of up to a thousand samples does not shrink its spread at
all. Its small departure from uniform is the test. Pair each sample of one detector with the other's from eight seconds
away. That keeps each channel's own law and destroys their joint timing, changing what arrives together while keeping
each direction's ingredients. The departure comes back to within a ten-thousandth, on two separate stretches of data,
with the predictions written down before the data were fetched. So the departure belongs to each channel's own spread,
not to anything the two share. The reading said where to look, in the direction and not in the amount, and what a
departure would mean.

**The quasar dipole.** An observer moving through a sky of distant sources counts more of them ahead than behind. With no
limit on brightness, that census is a count of directions alone, and the motion turns a uniform sky into a Cauchy on the
sphere. The count's dipole is twice the speed, to first order: the "2" that George Ellis and John Baldwin derived in 1984.
Every real census is cut at a brightness limit, and the cut adds a second term that depends on how the counts and the
sources' spectra change with brightness. That term belongs to the payload. On a large catalogue of quasars from the WISE
satellite, four disjoint brightness slices give one speed, as one motion should. Three colour slices disagree with each
other, which no single motion can do, so part of the dipole belongs to the sources themselves. The sort does not settle
the dipole's origin. It says where to look.

**One photon at a time.** In a double-slit experiment lit one photon at a time, each photon lands at one place and the
fringes build up over many. With the two paths' amplitudes as h and v, the fringes' visibility can be at most 2hv, and the
which-path predictability is the difference of their squares. That is the central sweep's height and foot from the
second essay, a known bound in quantum optics. In published frames the two slits' shares put the pair at its corner, where
the bound is 1. The measured contrast falls below it, short by the source's coherence. The bound is set by the two shares
alone, which is geometry. How far below it a pattern falls belongs to the source, what arrives.

None of these is new physics. Each is classical. What the reading supplies is the sort.

---

## 11. Why practice is right, and when it stops being right

Practice already reads Cauchy-type quantities correctly. No one reports the mean of a Cauchy sample. Statisticians
report the median and quartiles; spectroscopists report a line's centre and half-width; astronomers do the same; robust
methods were built to do the same wherever tails are heavy.

The usual reasons are that the mean does not exist and that the median is robust. Both are true, and both say only that
the median *works*. The reading says why it is the *right* summary. The quantity is a direction read from a standpoint;
its law, on the scale it is reported in, has a median and no mean; and the median is the corner, the place where the two
parties' readings meet. Reporting the median is reporting where the reader's own geometry puts the middle.

The reading also says when the median stops being right.

- **When what arrives weighs the two sides of the corner unequally,** the median moves off the corner, by exactly that
  weighting. The move is information about the payload, and it can be measured.
- **When an amount enters,** by an added offset, a varying scale, a cut at an edge or a pooling of standpoints, the law
  stops being a Cauchy, from its centre outward. Then the quantity is no longer a pure direction, and an amount-like
  summary may be called for, on the part that is an amount.

That is the whole of the advice. Read directions by their order and amounts by their sums, and know which is which. The
addresses are given before anything arrives. The payloads are met at them.

---

## Sources

- Jaynes, E. T. (1968). Prior probabilities. *IEEE Transactions on Systems Science and Cybernetics* 4(3), 227–241. And
  (1973), The well-posed problem, *Foundations of Physics* 3, 477–492.
- Stigler, S. M. (1974). Cauchy and the witch of Agnesi: an historical note on the Cauchy distribution. *Biometrika*
  61(2), 375–380.
- Lévy, P. (1925). *Calcul des probabilités*. Gauthier-Villars.
- Huber, P. J. (1964). Robust estimation of a location parameter. *Annals of Mathematical Statistics* 35, 73–101.
- Weisskopf, V. and Wigner, E. (1930). Berechnung der natürlichen Linienbreite auf Grund der Diracschen Lichttheorie.
  *Zeitschrift für Physik* 63, 54–73.
- Gull, S. F. (1988). Bayesian inductive inference and maximum entropy. In *Maximum-Entropy and Bayesian Methods in
  Science and Engineering*, vol. 1. Kluwer. (The lighthouse problem.)
- McCullagh, P. (1996). Möbius transformation and Cauchy parameter estimation. *Annals of Statistics* 24(2), 787–808.
- Bertrand, J. (1889). *Calcul des probabilités*. Gauthier-Villars.
- von Mises, R. (1928). *Wahrscheinlichkeit, Statistik und Wahrheit*. Springer.
- Dawid, A. P., Stone, M. and Zidek, J. V. (1973). Marginalization paradoxes in Bayesian and structural inference.
  *Journal of the Royal Statistical Society B* 35(2), 189–233.
- Abbott, R. et al. (2023). Open data from the third observing run of LIGO, Virgo, KAGRA and GEO. *Astrophysical Journal
  Supplement* 267, 29.
- Ellis, G. F. R. and Baldwin, J. E. (1984). On the expected anisotropy of radio source counts. *Monthly Notices of the
  Royal Astronomical Society* 206, 377.
- Secrest, N. J. et al. (2021). A test of the cosmological principle with quasars. *Astrophysical Journal Letters* 908,
  L51.
- Greenberger, D. M. and Yasin, A. (1988). Simultaneous wave and particle knowledge in a neutron interferometer.
  *Physics Letters A* 128, 391–394.

The theorem and its proof are in *Observation from Somewhere*, §7.2 (Theorem 6), with the closure table, what breaks
it, the four cases and the three cases in data; the background in §1.
