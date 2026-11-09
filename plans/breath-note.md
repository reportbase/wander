# Observation as breathing: the read and the write on Euler's plane

9 Nov 2026. Tom: "the most intersting idea is that unexplored idea is that observation is like breathing, the read/write
being the inhale/exhale. Eulers best captures that idea." Then "yes", to starting a note.

A working note, to iterate on. A reading, not a ruling, and not in any paper until it earns a place (SPN R727 recorded the
metaphor on 6 Nov "so we dont forget it"; R778 opens this note). The mathematics below is classical; the reading of it as
breathing is ours, and it claims no new physics. Each statement marked *(check)* is to be checked exactly before it goes
anywhere else.

## 1. The two axes

Euler's plane, as `euler.html` and essay 18 draw it: a point at distance d and turn θ from the standpoint is

  w = ln(z/H) = ln(d/H) + iθ,

H the thumb held out. Its two directions are not alike.

- **Up, iθ: the read (the inhale).** A turn. Within one read it is the quarter turn from home toward a horizon never
  reached (R696): bounded, open at its far end. It wraps (θ and θ + 2π one place) only when turns are joined, and joining
  is the writer's (R656, R717: π a line's half-turn period, 2π an oriented turn's).
- **Across, ln(d/H): the write (the exhale).** Scale. Unbounded both ways, measured in thumbs: one thumb out is 0, two
  thumbs ln 2, four thumbs 2 ln 2. Scaling the world slides along it (the scale test lives on this axis, R580); a count of
  thumbs or strides is a step along it.

So the asymmetry R727 asked for is the plane's own: one axis bounded and closing only when joined, the other open and
counted. Breathing is nearly symmetric (R727's caveat); the plane is not, which suits the read and the write better than
the lungs do.

## 2. A breath is a loop

Read, write, read back, write back: a rectangle on the plane, θ up by α, ln d across by λ, then both undone.

- **In the plane it closes.** A turn and a scaling commute (e^(iα)·e^(λ) = e^(λ)·e^(iα)), so the loop comes home with
  nothing left over, whatever α and λ (R738; essay 18 §7). A cycle that leaves nothing can repeat without drifting: steady
  breathing.
- **In space it does not.** Two turns about two axes, taken and undone in turn (h, v, back, back), leave a turn of about
  α·β about the third axis, to second order (R738's loop, `euler.html` `?loop=1`) *(check: sign and the next order;
  TWG run 3 has the round loop exactly, 4·arcsin(sin²(ε/2)·|sin φ|))*. Each breath in space comes home turned.
- **That leftover is holonomy** (HOL, R775–R777): transport round a loop on the sphere of directions turns by the enclosed
  solid angle, in the plane by none; Leek et al. 2007's qubit read it as a phase (slope 1.013 ± 0.003 against 2Θ). So
  today's test is, in this note's words, a measurement of what one breath in space leaves behind.

## 3. The read's law, heard as a breath that fades

The Cauchy from a standpoint z = m + iγ (the read's heat on a line, R706) has the characteristic function

  E[e^(itX)] = e^(imt − γ|t|),

an oscillation at rate m that dies away at rate γ (R753; OPL found the Cauchy's the only pure phasor among the laws tried).
In Euler's terms the exponent is i·m·t (a turn, the breath's rhythm) plus −γ|t| (a scale, the breath fading). Pure i is a
breath that neither grows nor fades; the real part is growth or decay. The standpoint z sets both: m how fast, γ how soon it
is gone.

*(check)*: whether the |t|, which makes the fading the same forward and backward in t, says anything about which way a breath
goes. It probably says the opposite: the read's law has no arrow, the arrow is the write's (R649: time is the step between
reads).

## 4. What the plane keeps from R727

- **A single read does not cycle.** The quarter turn never closes on its own; the θ axis wraps only for the writer, who
  joins turns. Cycles are joins (read, write, read again, R644; the turn closing; a loop of steps closing).
- **Motion hides the asymmetry, rest reveals it.** A moving reader writes as it goes (a step is counted, R627), so it moves
  across the plane all the time and up and down at once, and the two blur into one diagonal. At rest only the up-and-down is
  left: one standpoint writes nothing (no parallax; RWT's nullity).
- **The read holds no time.** "An ongoing encounter" gives the read a duration, which is the writer's account (R649, R651,
  R652). On the plane: the loop's sides are reads and writes, its order and its time a writer's statement about them.

## 5. The mountain walk on Euler's plane

9 Nov, later. Tom: "keep addding", with a ChatGPT note: walk toward a broad mountain on its centreline, the thumb held out
the whole way (`approach.html`, R650); the edges' span α = 2θ grows from 0 toward a half turn; written as Z = e^(iα) it goes
from 1 toward e^(iπ) = −1, each half reaching e^(iπ/2) = i and i·i = −1; the read is the present span, the write joins the
spans (∏ e^(iΔα_j) = e^(iΣΔα_j)); π the endpoint, e the law of accumulation, −1 the algebraic result; "an application of
Euler's mathematics to a model of the mountain walk, not a proof that the mountain itself obeys a special Euler law."

Most of it fits the corpus as it stands. Three things sharpen it.

**(a) Z is not a chosen representation: it is the read squared.** A breadth V* at distance d reads, on each edge, the ratio
s = (V*/2)/d against the thumb's line of sight. Then

  Z = (1 + is)/(1 − is) = e^(2i·arctan s) = e^(iα),

rational in the reading (R752, R580: the square map; `one-read.html`'s landing point). No angle, no π and no e are needed to
have Z: they are needed only to *name* α, which is the writer's (R584: angles are the writer's, readers have rates). Far off
s ≈ 0 and Z ≈ 1; at the pair's corner s = 1 (the mountain one half-breadth off per half-breadth of span) and Z = i; at the
foot s → ∞ and Z → −1, the image of the horizon. ChatGPT's i·i = −1 is (1 + is)²/(1 + s²) at s → ∞ seen half by half.
Checked to 10⁻¹⁶ (s from 0.01 to 100).

**(b) The write's product telescopes; the sum is the writer's.** ∏ Z_(j+1)/Z_j = Z_N/Z_0: the record of the walk needs only
its first and last reads, each a ratio. Writing it as e^(iΣΔα) is the writer's form (R596: Euler's formula and the lay's
logarithm are the writer's formulas for the reader's things). The reader's own composition of the steps is tangent addition
on s (R327), which needs no angle either.

**(c) The walk is a curve on Euler's plane, and it is Mercator's.** Put x = ln(V*/2d), the distance in thumbs with the
mountain's half-breadth as H (R599, "the thing itself as H"). Then

  α = π/2 + gd(x),  dα/dx = sech x,

gd the Gudermannian (checked to 10⁻¹⁶). Each stride is a step across the plane (the exhale, counted); the read climbs up it
(the inhale) by sech x per thumb: most at the corner (x = 0, α = π/2, Z = i), dying away both far off and close in, never
reaching π in any number of strides. That sech is the read's heat in distance, sech(ln(d/H)) (R702, R703's overlay), here
with H = V*/2. So the breath in this walk is uneven in exactly the way the near and far fields are: the turn taken in per
thumb walked is largest where the mountain fills the thumb's own share, and the half turn is a horizon, not an arrival
(R651: "getting closer" and arriving are the writer's).

Corrections to the note as pasted: "as you approach … the mountain occupies a larger angle" is the writer's account of
reads joined (R651); each read is one present s, with no "approaching" in it. And π and e are given the corpus's roles
already (R626, R597): π with the turn closing (the address), e with the open scale (the payload's and the write's axis);
they meet at e^(iπ) = −1 because that is where the up axis's half turn sits on the across axis's unit circle.

## 6. Open, in order

1. Check §2's leftover exactly: the plane's loop closes to rounding; the space loop's leftover against α·β and TWG's exact
   form; and the qubit's phase as the same leftover (nothing new, a link).
2. Ask whether a breath has a natural size: a loop whose up side is the whole quarter turn (home to horizon) and whose
   across side is one thumb (ln 2 for one in two, or 1). Probably not: H is chosen, and "one breath" would be the writer's
   unit.
3. Ask what an *unsteady* breath is: a loop that does not close in the plane needs the up and across moves not to commute,
   which in the plane they always do; so an unclosed breath in the plane is a write that changed what the next read turns
   through (the paint, not the address?). To be thought through, not assumed.
4. A breathing view on `euler.html` (the loop drawn as it is breathed, in the plane and in space) only once 1 is checked.
5. §5 (c) on `approach.html` or `euler.html`: the walk drawn as its gd curve on Euler's plane, the read climbing by sech per
   thumb, the corner at Z = i and the foot as the horizon Z = −1. Whether a stride's count (strides from the corner to the
   foot write V*, R650) is the area under that curve, or something else, to be worked out before drawing.

## Classical anchors (from memory, to check)

Euler 1748 (*Introductio*, e^(ix) = cos x + i sin x); Mercator's chart as the plane's picture of the globe's loxodromes;
Lie's commutators (the leftover of a small loop the bracket of its two generators, Lie–Trotter, R647); Gauss–Bonnet for the
leftover on the sphere; Berry 1984 for the phase; Lévy and Cauchy for the characteristic function.
