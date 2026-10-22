# WVR: the wave results revisited, sorted by address and central reading

*22 October 2026. A revisit, asked by the session's lead agent: WVP, DUO, QBT, QSO and `runs/thl/waves.py` were matched to
"outer/inner", "exterior/interior" and "wave-like/particle-like" (R265, R269, R270) before OFS settled the split into
the inscribed sweep (the address reader: a party's direction at θ, the stereographic chart s = v/h, unbounded, read by
order) and the central sweep (the payload reader: the pair's middle at 2θ, the square ½(h + iv)², bounded, read by means;
OFS §3.1 "One read, two results", §4 "The address points at the payload", "Why there are two sweeps, and only two", "What
each sweep reads"; R307 the central reading an amount; R389 the Cauchy the turn's). Physics, so for `physics.md`, not OFS
(R201). Exact arithmetic only; no data read. Nothing here is new quantum mechanics.*

## Known beforehand

- **QBT** (exact): the state ψ = (h, e^{iα}v) is the inscribed direction at θ; its Bloch point n = (sin 2θ cos α,
  sin 2θ sin α, cos 2θ) is the central point at 2θ, on the real slice (2hv, 0, h² − v²); Born's rule P(0) = h² is the
  central foot; ζ = ψ₁/ψ₀ the stereographic chart; a mixture lies inside the ball.
- **DUO** (data): a foil keeps √a of the fringe (a pure pair, V² + P² = 1), a chopper a (a mixture, inside). The sech form
  V = sech(ln k), P = tanh(ln k) is in print (Bramon, Garbarino and Hiesmayr 2004; Krause, Fischbach and Rohrbach 2014).
- **WVP** (simulation, then real photons): uniform-turn draws find the corner by median at spread (π/2)/√N and have a
  mean that climbs (2/π)·ln 10 a decade; on real photons the contrast sits below the slits' 2hv; "not run": read per
  arrival as tan(φ/2), the mean of |s| should climb (1 − C)·(2/π)·ln 10 a decade.
- **QSO** (exact): the weak value's Bloch form A_w = (n_z + m_z + i(m × ẑ)·n)/(1 + m·n); its foot-weighted mean is
  ⟨σz⟩ (W2); pre-selected on the equator with m uniform on the sphere (even in height) its law is ½(1 + x²)^(−3/2),
  superweak share 1 − 1/√2, and QSO said in passing that the even turn "would give the Cauchy" (not computed there).
  A phase twirl loses the visibility and keeps the predictability (F1).
- **Textbook:** the Möbius image of a Cauchy is a Cauchy, its parameter z = m + iγ carried by the same map (McCullagh
  1996; ADR here); weak values of a qubit with uniformly distributed post-selection have Lorentzian laws (Berry and
  Shukla 2010, search results only); the weak-value sum rule Σ_f p_f A_w = ⟨A⟩ and Σ_f p_f |A_w|² = ⟨A²⟩ for a pure
  state (Dressel et al., Rev. Mod. Phys. 86, 307, 2014); the weak value of a mixed state Tr(Π_f A ρ)/Tr(Π_f ρ)
  (Wiseman 2002); the relativistic addition of velocities tanh(a + b).

## The reading to test

One read, two breakdowns. On the real slice of a qubit (amplitudes h, v, unit relations), the sort is:
- **address** (inscribed, a direction, read by order): s = v/h = tan θ, the ratio of amplitudes; any Möbius image of it,
  in particular the relative address tan(θ_f − θ_i) of one state against another; and, the claim here, the **weak
  value**, which is the relative address carried by one fixed Möbius map;
- **central reading** (the square at 2θ, bounded, averaged, an amount in R307's sense): the Bloch point; the visibility
  V = 2hv = sin 2θ (its height, doubled) and the signed predictability n_z = h² − v² = cos 2θ (its foot's offset from the
  middle, doubled); Born's probability h² (the foot); every overlap |⟨f|i⟩|² = cos²(θ_f − θ_i) (the foot of the relative
  address);
- **payload:** what arrives weighted by Born's rule; the **bridge** is the Born rule, which turns a central foot into a
  frequency of counts.

If this holds, the address law's parameter must be the central point itself: the weak value, laid by a uniform turn of
the post-selection, should be the Cauchy whose median is ⟨σz⟩ and whose half-width is the visibility, and Born's weight
should turn that unbounded address into a payload with a mean and a variance whose sum of squares is the duality
equality. A mixture (central point inside the circle) should lose the address's horizon. A phase twirl, which averages
the central point (a mean, the payload's operation), should leave the weak value as an addition of levels.

## Predictions (written 22 Oct about 10:45, before any computation)

Real slice throughout: states (cos θ, sin θ), the post-selection f at θ_f, A = σz, A_w its weak value (real here). A
"uniform turn" of the post-selection is θ_f uniform on [0, π) (every real ray once). For a density matrix
ρ = (I + n_x σx + n_z σz)/2 (n_y = 0, |n| ≤ 1), A_w = Tr(Π_f σz ρ)/Tr(Π_f ρ). The Born weight on f is ⟨f|ρ|f⟩, normalized
over the uniform turn (its integral over dθ_f/π is ½, so the weight is 2⟨f|ρ|f⟩). mpmath at 50 digits; samples seeded.

- **P1. The weak value is a relative address, and its Cauchy's point is the Bloch point.** For a pure pre-selection at
  θ_i, A_w = n_z − V·tan(θ_f − θ_i) identically, with n_z = cos 2θ_i, V = sin 2θ_i. So under a uniform turn A_w is
  Cauchy with median n_z = ⟨σz⟩ and half-width (half the interquartile range) V, no mean; and the superweak share
  P(|A_w| > 1) is exactly ½ for every pure pre-selection (the spectrum's edge |A_w| = 1 is the median of |A_w|).
  *Killed if* the identity is off by more than 10⁻⁴⁰ at 30 seeded (θ_i, θ_f), or the law's quantiles at 0.1, 0.25, 0.5,
  0.75, 0.9 (computed by root-finding on A_w(θ_f), not from the Cauchy formula) differ from Cauchy(n_z, V)'s by more than
  10⁻³⁰ at 8 values of θ_i, or the superweak share is off ½ by more than 10⁻³⁰ at any, or 10⁶ seeded samples put the
  median or either quartile more than 3 standard errors off.
- **P2. Born's weight makes the address a payload, and the duality equality is its second moment.** Born-weighted, the
  law of t = (n_z − A_w)/V is (2/π)/(1 + t²)² (a Student t with 3 degrees of freedom, scaled by 1/√3): mean n_z,
  variance V², so ⟨A_w²⟩_Born = n_z² + V² = 1 = ⟨σz²⟩. V² + P² = 1 is the Born-weighted weak value's variance plus its
  squared mean. *Killed if*, at the same 8 θ_i, any of the density (at 5 values of t, from the pushed-forward measure),
  the mean, the variance or ⟨A_w²⟩ is off by more than 10⁻³⁰.
- **P3. A mixture loses the address's horizon, not its median.** For |n| < 1 the weak value is bounded (no superweak
  tail to infinity); its unweighted median under a uniform turn is still n_z exactly; its superweak share is
  (1/π)·arctan(2n_x/(1 − |n|²)), below ½ and tending to ½ as |n| → 1 (on the equator, n_z = 0, this is (2/π)·arctan|n|,
  the uniform turn's own share g at the Bloch length); its Born-weighted mean is n_z; its Born-weighted ⟨A_w²⟩ is
  strictly below 1. *Killed if*, at 12 seeded mixed states with n_x > 0, the largest |A_w| is infinite or above
  (1 + |n_z|)/(1 − |n|), the median or the superweak share is off by more than 10⁻²⁵ (shares measured by locating every
  crossing on a grid of 4,000 refined by bisection), the Born mean is off by more than 10⁻²⁵, or any Born ⟨A_w²⟩ ≥ 1.
- **P4. Without a phase reference the weak value adds levels.** After the phase twirl (n_x → 0, QSO F1),
  A_w = (m_z + n_z)/(1 + m_z n_z) = tanh(artanh m_z + artanh n_z) with m_z = cos 2θ_f: the post- and pre-selection's
  predictabilities added as rapidities (each artanh n_z = −ξ, the level ln(v/h) with its sign turned), |A_w| ≤ 1, no
  superweak values, median n_z. *Killed if* the identity is off by more than 10⁻⁴⁰ at 30 seeded pairs, or the share with
  |A_w| > 1 is not 0, or the median off n_z by more than 10⁻²⁵ at 5 values of n_z.
- **P5. A fringe's arrivals read as addresses split by the visibility.** Arrivals of a two-path pattern at phase φ with
  density (1 + V cos φ)/2π (the payload, Born-weighted), read per arrival as the inscribed reading t = tan(φ/2), have
  density V·(2/π)/(1 + t²)² + (1 − V)·(1/π)/(1 + t²): a share V laid as a payload (P2's law, with a mean) and a share
  1 − V laid by the bare turn (the Cauchy, none). So the median of t is 0 at every V, and the truncated mean of |t| over
  |t| ≤ T climbs (1 − V)·(2/π)·ln 10 a decade as T → ∞ (WVP's stated, unrun number). *Killed if* the density is off by
  more than 10⁻³⁰ at 5 t and 4 V, the median off 0, or the climb from T = 10⁸ to 10⁹ is off (1 − V)·(2/π)·ln 10 by more
  than 10⁻⁶ at V = 0, 0.3, 0.7, 1 (at V = 1, off 0 by more than 10⁻⁶).
- **P6. The re-sort's bookkeeping.** Under a uniform turn of the state θ on [0, π/2]: the address s = v/h has median 1 and
  a truncated mean climbing (2/π)·ln 10 a decade; V = 2hv and P = |h² − v²| are bounded, each with mean 2/π and mean
  square ½. The phase twirl over N = 2..7 equally spaced phases leaves every member's visibility |n_⊥| = V and its
  predictability n_z, and averages n_⊥ to 0: the visibility is lost by a mean taken over the group (the payload's
  operation), while no member's reading changes. *Killed if* any is off by more than 10⁻³⁰ (the climb by more than 10⁻⁶
  between T = 10⁸ and 10⁹).

What a kill would mean: every prediction is an identity of textbook quantum mechanics or of the Cauchy family, so a kill
is my derivation or my set-up. P1, P3 and P5 are the content: that the weak value's Cauchy is centred on the central
point, that the address's horizon belongs to the pure state only, and that a fringe's visibility is the share of its
arrivals that carry payload weight.

## Runs

### Run 1 (22 Oct about 11:00, `runs/wvr/wvr.py`, output in `runs/wvr/wvr-run1.txt`; 45 s)

A first start stopped on a ZeroDivisionError before any verdict was printed: at θ_i = π/4 the bisection in the share
routine landed exactly on the weak value's pole. The routine now returns a huge value there (a pole is a boundary like a
root); no prediction or tolerance changed. The output file is the second start's.

- **P1 not killed.** A_w = n_z − V·tan(θ_f − θ_i) to 9·10⁻⁵⁰ at 30 pairs. At 8 pre-selections the shares of the uniform
  turn below Cauchy(n_z, V)'s quantiles, found by root-finding on A_w itself, are 0.1, 0.25, 0.5, 0.75, 0.9 to 3·10⁻⁵¹,
  and the superweak share is ½ to 3·10⁻⁵¹ at every one, from V = 0.20 (θ_i = 0.1) to V = 1. Samples (10⁶ each): the
  median and quartiles within 1.9 se; superweak 0.49929 and 0.50024 (se 0.0005).
- **P2 not killed.** Born-weighted, the law of t is (2/π)/(1 + t²)² to 2·10⁻⁵¹; the mean n_z, the variance V², and
  ⟨A_w²⟩ = 1 at every θ_i (worst 2·10⁻⁵¹).
- **P3 not killed.** At 12 mixed states (|n| 0.13–0.91) the largest |A_w| is finite (1.009–2.35, under the bound); the
  share at or below n_z is ½ (3·10⁻⁵¹); the superweak share is (1/π)·arctan(2n_x/(1 − |n|²)) to 7·10⁻⁵¹ (0.085–0.470),
  and on the equator (2/π)·arctan|n| (0.2952, 0.4665, 0.4968, 0.4997 at |n| = 0.5, 0.9, 0.99, 0.999); the Born mean is
  n_z; Born ⟨A_w²⟩ is 0.502–0.861, all below 1.
- **P4 not killed.** After the phase twirl A_w = tanh(artanh m_z + artanh n_z) to 4·10⁻⁵¹; no superweak values; median n_z.
- **P5 not killed.** The fringe's arrivals read as t = tan(φ/2) have the split density to 7·10⁻⁵²; median 0; the truncated
  mean of |t| climbs 1.46587, 1.02611, 0.43976 and 6·10⁻¹⁷ a decade at V = 0, 0.3, 0.7, 1: (1 − V)·(2/π)·ln 10 to 10⁻¹⁶.
- **P6 not killed.** s: median 1, climb (2/π)·ln 10; V and P: means 2/π, mean squares ½; the phase twirl keeps every
  member's |n_⊥| = V and averages n_⊥ to 0 (to 2·10⁻⁵¹).

Post hoc, not predicted: Born ⟨A_w²⟩ for a mixture is ½ at |n| → 0 and rises toward 1 only as the state turns pure; I did
not fit its form.

## What run 1 shows

Nothing here is new quantum mechanics (the weak-value sum rules are Dressel et al.'s; the Möbius closure of the Cauchy is
McCullagh's). What is new is where each piece falls once the address and the central reading are kept apart.

1. **The weak value is an address, and its law's point is the Bloch point.** On the real slice, A_w = n_z − V·tan(θ_f − θ_i):
   the relative address of the post-selection against the pre-selection, carried by one fixed map. Laid by a uniform turn
   it is Cauchy with z = m + iγ = ⟨σz⟩ + i·V: the central point (foot offset and height) is the address law's standpoint.
   Its median is the expectation; its half-width is the visibility; it has no mean. The superweak share is ½ for every
   pure state: the spectrum's edge |A_w| = 1 is the median of |A_w|, the corner. (QSO's ½(1 + x²)^(−3/2) and 1 − 1/√2
   are the same weak value under a sphere uniform in height, not under the turn; QSO said in passing the turn "would give
   the Cauchy", and it does, centred on the Bloch point.)
2. **Born's rule is the bridge from address to payload.** Weighted by the foot |⟨f|i⟩|² the same weak values have a mean
   (n_z) and a variance (V²), and ⟨A_w²⟩ = 1. The duality equality V² + P² = 1 is that second moment split into variance
   and squared mean: the visibility is the spread of the weighted addresses, the predictability their mean.
3. **The horizon belongs to the pure state.** A mixture (its central point inside the circle) has bounded weak values,
   keeps the median at n_z and the Born mean at n_z, loses the tail: its superweak share is (1/π)·arctan(2n_x/(1 − |n|²)),
   on the equator (2/π)·arctan|n|, the uniform turn's own share g at the Bloch length, ½ only at |n| = 1.
4. **A missing phase reference is a mean, and leaves levels adding.** The twirl changes no member's V; it averages n_⊥ to
   0 (a payload operation). What is left of the weak value is the rapidity sum tanh(artanh m_z + artanh n_z): the two
   predictabilities' levels added, bounded, no superweak values.
5. **A fringe's visibility is the share of arrivals carrying payload weight.** Real arrivals are Born-weighted. Read per
   arrival as the inscribed reading tan(φ/2), a fraction V of them follows the payload's law (with a mean) and 1 − V the
   bare turn's Cauchy (none), so the mean climbs (1 − V)·(2/π)·ln 10 a decade, as WVP stated without running.

### The re-sort

| quantity | sort | why |
|---|---|---|
| s = v/h, ζ = ψ₁/ψ₀ (QBT Q5) | address | the stereographic chart, unbounded, median, no mean |
| the weak value A_w (QSO W1–W4; P1) | address | a Möbius image of the relative address tan(θ_f − θ_i) |
| the Bloch point n, at 2θ (QBT Q1) | central | the square ½(h + iv)², bounded, means |
| visibility V = 2hv = sin 2θ = sech ξ (DUO, WVP Q4′) | central | the Bloch point's height (doubled); the address law's half-width |
| predictability P = \|h² − v²\| (DUO) | central | the foot's offset from the middle (doubled); its signed form n_z the address law's median |
| Born's P(0) = h² (QBT Q2), an overlap \|⟨f\|i⟩\|² (QSO F3) | central, the bridge | the foot; a frequency only through Born's rule |
| counted arrivals, a fringe pattern 1 + V cos φ (WVP runs 3–4, DUO) | payload | Born-weighted; read per arrival, V of them payload and 1 − V bare turn |
| the fringe phase φ estimated by arg Σ e^{iφ} (WVP Q3′) | central | the angle at the centre, read by a circular mean |
| WVP runs 1–2's uniform draws of θ | address law alone | no payload at all; their squares h² are the central foot under the turn (arcsine) |
