# The corner follows the gaze: a note, and a draft for OFS

*25 October 2026. Tom, in order: "visually, our far field looks proportional, it does not look like the merkator map.";
"why would readers care that much about the far or near field anyways? we are concerned about what we are focused on.
its highly likely that the corner is constanly adjusted to follow our point of gaze."; "the far and near fields, are
useful as a signal about what to focus on next."; "what we are focused on, we want maximum possible fidelity. only
enough fidelity in the near and far fields to discriminate about where to focus next."; then "yes, 1,2,3" (record it,
draft the OFS paragraph in a note first, and run the exact check, FOV). SPN R495. Not in OFS until Tom has read this.*

## The four points

1. **A picture's far field is proportional, not Mercator's.** Ground at distance h, seen from eye height v, appears at
   atan(v/h) below the horizon. Near (h < v) the angle from straight down goes as h/v, in proportion; far (h > v) the
   angle from the horizon goes as v/h, in proportion to the reciprocal: 26.6°, 14.0°, 7.1° at 2v, 4v, 8v, each doubling
   half the room of the last. That is the turn's row of OFS §6's table (the reciprocal a reflection), and the in-place
   lay 2 − 1/s. Mercator's logarithm, a doubling ln 2 wide, is distance laid by the count of addresses: it needs the
   distances, which are amounts.
2. **The corner follows the gaze.** H is chosen, a zoom; OFS already puts the best H at the corner of what is read
   (Proposition 13, §8). On the turn a cell's relative width is (π/2K)(s + 1/s), least at s = 1, so a corner on the
   thing looked at gives it the finest relative grain the reader has. Near and far mean nearer than and farther than
   what is looked at; they move with the gaze.
3. **The fields are a signal for the next look.** Every direction is still held, coarser off the corner: enough to say
   that something is there, roughly where, and that its paint changed. Moving the corner there is a new zero (OFS §2,
   "Sweeping from zero"), and the fields round the new focus are the next signals.
4. **Fidelity at the focus, only enough in the fields.** FOV (`plans/fov-plan.md`, run 1, exact, nothing killed): with
   K addresses, every cell of the focus [0, F] at most δ wide and every cell past it within a factor ρ, the fewest cells
   are ⌈F/δ⌉ + ⌈log_ρ(X/F)⌉. The focus is laid in proportion, the field in levels of ratio ρ, and the corner is at the
   focus's edge. The field costs only log_ρ(X/F) addresses (6 at X/F = 64, ρ = 2), whatever K is, so the rest go to the
   focus (δ = F/58 at K = 64). The reader's lay, 1 + ln s, is the case where the field's first cell matches the focus's
   grain. The turn with its corner at F gives the focus about a third of that fidelity (2.78 times wider at its edge) and
   breaks the factor of 2 near s = 2K/π.

## Where Mercator's logarithm belongs

Point 4 lays the levels on x, the angle away from the gaze, not on distance. On angle the field ends at a fixed angle (the
far side of the sphere, or the octant's edge), so X is known with no amount carried in, which distance never gave
(SKT, R494). Proportional at the focus and logarithmic past it, laid on angle and conformal in two dimensions, is
Schwartz's log-polar map, w = log(z + a), the visual field on the cortex. Horton and Hoyt's fit, 17.3/(E + 0.75) mm per
degree, integrates to ln(1 + E/0.75): its corner is about 0.75°, the matched-grain case of point 4. That fit is in
`plans/neighbours.md` §2, which holds Tom's ruling of 8 October: "the human eye is engineering more than fundemental
geometry." A neighbour, not evidence; check Schwartz 1977, 1980 and Horton and Hoyt 1991 before any citation.

So Mercator's logarithm is real, but it is the angle's, laid about the gaze, not the distance's laid about the reader.

## A draft paragraph for OFS (not yet placed)

*Where it would go: after Proposition 13 in §8, or as a closing paragraph of "A fixed count, aimed by H". Normal paper
voice, no ruling numbers, no file paths.*

> **The corner follows the focus.** Nothing in the geometry fixes where the reader puts its corner; H is its own
> choice. The finest relative grain is at the corner, (π/2K)(s + 1/s) at its least where s = 1, so a reader should put
> the corner on what it is looking at, and near and far then mean nearer than and farther than that. The rest of the
> field is not lost: every direction is still held, coarser away from the corner, which is enough to show that
> something is there and where to look next. Moving the corner there is a new zero. If the aim is the most fidelity on
> what is looked at, an extent F, and only enough elsewhere to place a thing within a factor ρ, the fewest addresses do
> it this way: cells of one width across F and cells of ratio ρ past it. The corner is then the focus's edge, and the
> field costs about log_ρ(X/F) addresses whatever the total, X the field's extent. Laid on the angle from the gaze that
> extent is fixed and needs no amount. The reader's lay, proportion and then levels, is the case in which the field's
> first cell matches the focus's grain. The view a reader sees is the turn: its far field is proportional to the
> reciprocal of distance, each doubling of distance given half the room of the last. The logarithmic far field belongs
> to distance laid by the count of addresses, which needs the distances.

## Near and far held alike (25 October, later; SPN R496)

Tom: "the cauchy supports maximim fidelity at the focus point, however, it does so evenly acrros the far and near
fields, and they are very different."; "it is useful to know roughly how far away the mountain range is. is it a 1 day
hike or a 1 month hike."; "but you could just turn your head to move you focused corner to the mountain range."; then
"yes, so it is logical that a reader would give benefit from equal attention to the near and far fields. they are
maintained at enougth fidelity know know where to look next."

- **The two corners.** Turning the head moves the corner in direction: the range comes to the focus and its outline,
  ridges and width over height are read at full fidelity, free. It gives no distance (a turn in place has no parallax).
  Designating the range draws it at H, which puts it at the corner of distance too, free, but as mountain equals thumb.
- **How far is the sizing, not grain.** Whether the range is a day's hike (about 30 km) or a month's (about 900 km) is
  V*/H, a factor of 30, about 5 doublings: needed only as levels, and always carried in (a baseline of about 2εd, 18 m
  and 540 m at ε = 1 arcmin for a factor of 2; a known kind, mountains 1 to 5 km tall; or the horizon, a 3 km peak gone
  past about 200 km). No field holds it, near or far.
- **So the fields need only direction grain, and they are held alike.** Their one job is to say where to look next.
  The reader does not know on which side the next thing will be, so nothing favours one side: the exchange, the
  reader's ignorance of which side a reading falls on, gives them equal attention. The Cauchy's evenness across near
  and far is then what the fields should have, not a fault. The differences between near and far (room, occlusion,
  count, change) are the world's, met in the payload and in the sizing, not in how the addresses are spread.
- **How much the fields get in all is FOV's question, a separate one.** FOV run 1: they need only about log_ρ(X/F)
  addresses to place a thing within a factor ρ, whatever K is. The turn gives them half of K, which is more than
  enough. Equal attention between near and far does not require half of everything for the fields together.

The draft paragraph above stands, with two changes: "near and far then mean nearer than and farther than that" is
followed by "and the two are held alike, since the next look may fall on either"; and the last sentence on distance is
replaced by "How far the focus is lies outside every reading: designating it puts it at the corner, and its distance,
needed only roughly, is carried in."

## Open, for Tom

- Placing the paragraph, and whether OFS §6's framing of Mercator's height as the reader's lay of distance should be
  reworded (point 1).
- `flight.html` draws the 1 + ln lay of ground distance at bottom left; the picture's own lay could go beside it.
- Whether the levels on angle from the gaze replace, or stand beside, the levels on distance in §8.
