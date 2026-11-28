# The Born draft re-read against reads and writes

*28 November 2026, SPN R1290. Tom: "Let's revisit the born rule and quantum. We have an old pair about born in archive
folder", then "Re-read it against the new framing". The draft is `papers/archive/born-rule-draft.md` (October 2026;
judged not usable as written on 24 October, SPN R474, and its twin `plans/grok-born-note.md`, R288–R289). These are
Claude's readings, not rulings; nothing was run. The arithmetic below is textbook and was checked by hand.*

## In one paragraph

The draft looked for Born's rule in the Cauchy, which is the read's heat over the whole hemisphere: a density that sums
to an arctangent and needs π for its total. In the current framing Born's weight is not a heat. It is the share of one
read between its two ends. For a ray [h : v] with slope s = v/h, the two outcomes get 1/(1 + s²) and s²/(1 + s²), the
first of R801's four identities. These are rational in the slope, with no angle, no trigonometry and no π. A click is a
write, and a frequency is a count laid over clicks. The draft's one "identification", outcome = chord coordinate, puts a
continuous read where QM has a discrete write. Every one of its errors follows from that, or from the heat/share
confusion R289 already named.

## Section by section

| Draft | What it says | Re-read now |
| --- | --- | --- |
| Abstract, §1 | Derives Born's rule from geometry; QM's difficulties come from a "view from nowhere" | No derivation is on offer (R1229: the framing derives the same results, never new physics). The DHV is a synthesis, and its results are not wrong (R1239); QM's Hilbert-space statement is that synthesis, not an error. |
| §2 | A reader with h² + v² = 1 and "a known breadth H"; vantages completed, parallel, serial; the "unique map" x = tan θ; Haar dθ/π | H is chosen, not known (R226). The three vantages and parallel/serial are gone (R268, R578). The reader maps nothing: its reading is the slope s itself (R306, R793), and tan is the writer's chart joining s to an angle. The even turn in the read's own terms is ds/(1 + s²); its total π is the DHV's completion (R807). By R796's grades, s needs nothing, the shares need the one-length circle (V = H), and the angle needs π. |
| §3 | ρ(x) = 1/(π(1 + x²)); "the square is the curvature of the projection" | The arithmetic is right: this is the read's heat (R706, R728), given and not computed, the SHV's by definition (R1286). But it is a heat over every direction from one standpoint. Born's number is about one direction. |
| §4 | One identification: "measurement outcomes correspond to chord coordinates" | This is where it fails. A qubit measurement has two outcomes, and each click is discrete and lasting, met by anyone who looks at the detector: a write (R1039, R1174). Counting clicks is the counter's bookkeeping (R1174, R1176). A frequency is a count, and no finite count is the share (as no count is π, R922); it tends to it. The outcome is not a read's coordinate at all. |
| §5 | cos²(θ/2) as the inverse Jacobian; Fubini–Study; the qubit case "Gleason leaves open"; |Ψ|² = g_tt | The Jacobian's value matching cos² is sec² = 1 + tan² (R288). Summed, the Cauchy gives P(x ≤ tan 0.55) = 0.675 against Born's 0.727 at a Bloch angle of 1.1. Fubini–Study is circular. The qubit case is not open: POVM forms of Gleason cover it (Busch 2003; Caves et al. 2004; from memory, to check). The metric route has no content stated. |
| §6 | "The arc is undisturbed; measurement changes only the reader's position"; entanglement as shared arc content | This is backwards in the new terms. A read changes nothing (R659), but a write changes the world (R898), and a measurement is a write: the system after it faces the apparatus. "Shared arc content" is a local common cause, which Bell excludes (R288). The framing sorts the singlet's numbers (below); it gives no mechanism for them and must not claim one. |
| §7 | Interference from "depth fields"; open questions | Interference is the doubled point's height 2hv (QBT, WVP, duality V² + P² ≤ 1). It is already sorted and needs no depth field. |

## What the re-read gives, sorted

- **The ray is the read.** Physical states are rays: a direction with no length, unmoved by scaling the amplitudes. That
  is a read exactly (D2). Its reading is the slope s = ψ₁/ψ₀, real on the quarter-turn slice and complex in general (ζ, the
  Bloch sphere's stereographic chart, QBT).
- **Normalisation is the one-length circle.** Σ|ψ|² = 1 puts both amplitudes in one unit: R796's middle grade, V = H. It
  is the writer's convention giving shares, and it moves no ray.
- **Born's weight is a share, rational in the read.** p₀ = 1/(1 + |ζ|²), p₁ = |ζ|²/(1 + |ζ|²). With n outcomes,
  p_k = |s_k|²/(1 + Σ|s_j|²), shares over one shared denominator (SHD, R1045; "more parties", R225). No trigonometry and
  no π (R793, R1253: the read holds exactly what is rational in its slopes).
- **The two outcomes are home and the horizon.** s = 0 is outcome 0 certain, and s = ∞ is outcome 1 certain. The exchange
  s ↔ 1/s swaps them (p ↔ 1 − p), and the corner s = 1 gives even odds. Within one facing an orthogonal state is the
  exchange (−1/s, with the sign dropped).
- **Spin-½'s half angle is the half-slope.** For a spin direction at Bloch angle φ the amplitude slope is tan(φ/2), R793's
  join s = tan(φ/2). Born's weight 1/(1 + t²) = (1 + cos φ)/2 is the foot h² of the doubled point (QBT). The half angle that
  makes qubits feel strange is the read's own half-slope.
- **Malus's law is the same share.** Prepared at one direction and analysed at another, the share is 1/(1 + s²) for the
  relative slope s, got by tangent subtraction. Both directions are apparatus in the world. Their relation is read, and
  each click is a write.
- **The singlet's correlation is rational in the half-slope.** E = −cos φ = −(1 − t²)/(1 + t²) for analysers φ apart
  (t = tan(φ/2)). The CHSH value 2√2 lands on the one root, √(1 + s²) at s = 1 (R793). This is sorted, not explained:
  why no local list of writes reproduces it is Bell's, and the framing adds nothing there.
- **What the Cauchy is in QM.** It does not enter Born's rule. It enters where a reading is laid by a turn: the weak value
  as a Cauchy at ⟨σz⟩ + iV (WVR, QSO), and a two-pole line shape. R1240's caution holds here too: "Cauchy" is only a name
  for a density.
- **The state is inferred, not read.** No one standpoint reads a single system's ray: no-cloning, and tomography counts
  writes over many copies. So by R827 the state is what counted writes fix, not a read anyone takes. Whose read the ray
  is, the preparer's apparatus or no one's, is left open.

## What this does not do

It derives nothing. That a count of clicks tends to the share is the bridge, Born's rule itself, as QBT said (R286). The
re-read only says where each piece sits:
- the ray is the read;
- normalisation is the one-length circle;
- the weight is a share;
- the click is a write;
- the frequency is a count;
- the Bloch sphere held whole, every basis at once, is the DHV.

The known routes to Born's rule (Gleason, Zurek's envariance, Deutsch–Wallace, Hardy's and Masanes–Müller's axioms) each
take a premise this sorting does not supply. It is consistent with them and not a rival.

## Offered, not run

1. An exact check (fractions) of the rational forms above: n-outcome shares, Malus by tangent subtraction, the singlet's E
   and CHSH from half-slopes, against the angle forms. These are identities, so the check could fail only by my
   arithmetic.
2. A test that can fail, on open data: photon-polarisation or qubit counts at rational relative slopes. Prediction: the
   frequencies are the rational shares and the count's scatter is binomial, with no Cauchy anywhere in a projective
   measurement's outcome law. A Cauchy-shaped tail in outcome frequencies would be against this re-read.
3. Archive notes: a pointer under `born-rule-draft.md`'s entry in `plans/archive-gems.md`. The archived file stays
   unedited.
