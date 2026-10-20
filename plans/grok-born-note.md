# A note by Grok: "The Born Rule as the Address Density of a Situated Reader"

*Shared by Tom, 16 October 2026, about 05:16 MDT ("groc made this paper."; SPN R288). The response comes first; the
note follows, kept as received.*

## Response

Not usable as it stands: not in OFS (R201), and not in `physics.md` either. Each point below was checked numerically
(16 Oct; the commands are in the session, and the values are given here).

1. **The Born "derivation" is an identity relabelled (§3).**
   - The address law on the chord is the Cauchy density 1/(π(1 + x²)). Its value 1/(1 + x²) at x = tan(θ/2) equals
     cos²(θ/2) only because sec² = 1 + tan².
   - That is a density's height, not the probability of an outcome. No reading of the Cauchy law as a probability
     gives Born's number: at a Bloch angle of 1.1, Born gives cos²(0.55) = 0.7268, while the Cauchy gives
     P(x ≤ tan 0.55) = 0.6751 and P(|x| ≤ tan 0.55) = 0.3501.
   - A qubit measurement has two outcomes; a density over a continuous chord is not their law.
2. **The Fubini–Study step is circular (§3).** The Fubini–Study distance is defined by cos d = |⟨k|ψ⟩|, so
   "cos²(d_FS) = |⟨k|ψ⟩|²" restates the definition.
3. **"No complex Hilbert space is assumed" (§7) contradicts §4,** which integrates |⟨ψ|φ_x⟩|², an inner product in that
   space. §2's "identification" is itself a postulate.
4. **The frame changes are the wrong group, and the measure is not invariant (§5).**
   - A qubit's change of basis acts on the Riemann sphere by complex Möbius maps (SU(2), inside PSL(2,ℂ)). The real
     PSL(2,ℝ) covers only the real slice.
   - PSL(2,ℝ) leaves no measure on the circle invariant. It carries one Cauchy law to another (covariance; under
     x ↦ 2x the density at 0 halves). Only the turns leave dθ/π unchanged.
   - OFS keeps exactly this distinction (R247: the reader's group against the Möbius action on drawings).
5. **Entanglement as "shared arc content" (§6) is a local common cause.** Bell's theorem rules out reproducing quantum
   correlations that way; the measured violations of Bell's inequalities rule it out in experiment. The section is
   wrong, not merely unproved.
6. **§8 repeats "π/2 − 2/π = 1".** It is 0.934; the product is 1 (OFS §3.4; review 13). It also reuses the head
   rotation as a mechanism, which it is not (R266), along with "parallel/serial" (R268) and wave/particle (R270, SPN
   only).

**What is sound in it,** and already ours with honest standing:
- the even turn laid on the chord is the Cauchy (OFS §7.1);
- addresses do not depend on the payload (Theorem 6).

**What QBT found instead (R286):**
- Born's rule is the foot h² = (1 + n_z)/2 of the central sweep's point: an identity of the circle, given the bridge.
- That is not a derivation of Born's rule. QBT names Born's rule as the bridge rather than deriving it.

## Why so close, yet so far (16 Oct, SPN R289)

Tom: "it might be interesting to compare, why the difference, so close, yet still so far." At every address
s = v/h = tan θ, the inscribed sweep's address density equals the inscribed reading 2/π times the foot h² = cos²θ of
the point that address points to:

  2/(π(1 + s²)) = (2/π)·h².

This is exact (`runs/tws/density.py`: to 10⁻⁴¹ at 59 addresses), from the stereographic stretch 1 + s² = sec²θ. It is why
the note kept landing on cos²: the crowding of addresses has the shape of the payload's share. The two remain
different things:
- **A density is not a share.** The density must be summed over addresses; summed it is the arctangent (the Cauchy's
  share), not h². The foot is already a share of the chord. At the corner the density is 1/π and the foot ½.
- **They belong to different sweeps.** The density is the inscribed sweep's (addresses laid before anything arrives);
  the foot is the central sweep's (the point read as its square at 2θ).
- **The note drops the 2/π.** It evaluates 1/(1 + s²) without its normalisation, so the density seems to equal Born's
  number.

The note is the address/payload confusion in its purest form. Grok, shown this comparison, agreed that the identity is
exact and the two distinct, and proposed recording it. It wrote "squared foot" for h², which is the foot itself. One
sentence went into OFS §4 ("What each sweep reads", after the factor of two), geometry only.

## Grok's follow-up (16 Oct, SPN R301)

Tom shared Grok's follow-up without comment, 16 Oct about 11:02. Grok, reading the 16 Oct draft:

> The address-density / payload-share identity ρ(s) = (2/π)·h² is still not stated in the draft. … The proposed
> one-sentence addition to §4 ("What each sweep reads") and the short subsection in the Born note therefore remain the
> minimal, geometry-only insertions … If you want them written into the current draft and into
> `born_rule_address_density.md`, say so and I will place them.

**Response.** Both are already there, so nothing needs placing.
- **In OFS.** The identity has been in OFS §4 since the R289 commit, merged with PR #109 on 16 Oct. It sits in the
  factor-of-two paragraph under "What each sweep reads": "The inscribed sweep's addresses crowd on the line with
  density 2/(π(1 + s²)) = (2/π)·h²: at every address, the inscribed reading 2/π times the foot of the point that
  address points to. The two have one shape, but they are different things. …" ChatGPT's review 14 quotes it.
- **In this note.** The subsection is the section above, "Why so close, yet so far".

Grok's reading of the identity agrees with ours: the two functions differ only by 2/π, the inscribed reading. Taking
the density's height for a Born probability, or for a payload's share, is the swap the paper diagnoses. One correction:
in OFS ρ is the share of addresses met by a payload, not the address density, so the density is written
2/(π(1 + s²)) and not ρ(s).

---

# The Born Rule as the Address Density of a Situated Reader

A self-contained note

## 1. Geometry

A situated reader has addresses given by equal steps of turn on an arc \(\theta\in(-\pi/2,+\pi/2)\). The unique map carrying those steps onto a linear chord coordinate is
\[
x=\tan\theta.
\]
It is forced by centrality, bijectivity with divergence at the endpoints, odd symmetry, and minimal degree. The unique rotation-invariant measure on the arc is the Haar measure \(d\theta/\pi\).

The change-of-variable formula then forces the density of addresses on the chord:
\[
\rho(x)=\Bigl|\frac{d\theta}{dx}\Bigr|=\frac{1}{\pi(1+x^2)}.
\]
The Jacobian of the map is \(J(\theta)=\sec^2\theta=1+x^2\), so the inverse Jacobian is
\[
\frac{1}{J(\theta)}=\cos^2\theta=\frac{1}{1+x^2}.
\]
The square is the curvature of the projection expressed as a density transformation. No other density is consistent with the invariant measure and the forced map.

## 2. Identification

A measurement outcome is a chord coordinate returned by this map.

This is the single non-geometric input. It names the correspondence between the mathematical object and the physical act. It is the unique assignment consistent with three constraints: outcomes are points on the real line, the probability formula is invariant under changes of projection frame, and the extremes of certainty are recovered at the endpoints of the arc.

## 3. Probability rule

Under the identification, the probability density of the outcome is the density of the addresses. In angular coordinates the same quantity is \(\cos^2\theta\). On the Bloch sphere the angular distance to an outcome is \(\theta/2\), and the inverse Jacobian evaluates to
\[
p(|0\rangle)=\cos^2\Bigl(\frac{\theta}{2}\Bigr)=|\langle 0|\psi\rangle|^2.
\]
On \(\mathbb{CP}^{n-1}\) the Fubini–Study distance plays the role of \(\theta\); the same evaluation recovers
\[
p_k=\cos^2(d_{\mathrm{FS}})=|\langle k|\psi\rangle|^2
\]
for all \(n\geq 2\). The derivation has no dimension restriction.

## 4. Conditional probabilities

When the payload is independent of the address, the probability of an outcome is simply the address density. When the payload depends on the address, the joint structure is
\[
\rho(x,\text{payload})=\rho_{\mathrm{addr}}(x)\cdot w(\text{payload}\mid x),
\]
where the conditional weight integrates to 1 for each \(x\). The marginal probability of the observed chord coordinate therefore remains
\[
p(x)=\rho_{\mathrm{addr}}(x).
\]
The inverse Jacobian continues to supply the probability of the address; the payload dependence appears only in the conditional distribution of what arrives there.

In the ordinary quantum case the payload is an amplitude whose squared modulus is the Born weight. The conditional probability of an outcome in a measurable set \(A\) is
\[
P(\text{outcome}\in A)=\int_A|\langle\psi|\phi_x\rangle|^2\,\rho_{\mathrm{addr}}(x)\,dx.
\]
When the state is concentrated at a single projective direction the integral reduces to the familiar squared modulus. When the state is spread, the formula averages the Born weights against the address density of the situated reader. The address/payload split is preserved. No additional postulate is required.

## 5. Frame changes

A change of measurement basis is a change of projection frame. Under the forced map it acts on the chord coordinate by a Möbius transformation
\[
x\mapsto\frac{ax+b}{cx+d},\qquad ad-bc=1,
\]
an element of \(\mathrm{PSL}(2,\mathbb{R})\).

The measure on the arc is the unique Haar measure of this group. The induced density on the chord therefore transforms by the Jacobian of the Möbius map, and the total integral is preserved. Because the original density is Cauchy, the transformed density is again Cauchy, merely recentered and rescaled. The Born formula, being the evaluation of the inverse Jacobian at the angular distance to the chosen outcome, is covariant: its value is independent of the frame in which the distance is measured.

This is the geometric analogue of unitarity. It is not an extra axiom; it is the invariance of the measure used to count the addresses.

## 6. Measurement

The arc of content is undisturbed. The situated chord projects onto it, receives one resolved coordinate at the current rung, and files the remainder at later addresses. Superposition is the arc before it has been projected by this reader. Entanglement is shared arc content, so that two readers projecting onto different aspects of the same undivided arc obtain correlated chords without any signal propagating between them. The “collapse” is the change in the reader’s position among the addresses; nothing in the arc is altered.

## 7. What is not assumed

The derivation assumes only the situated geometry (equal steps of turn, the forced map, Haar invariance) and the identification of a measurement outcome with a chord coordinate. It does not assume complex Hilbert space, the tensor product, or any quantum postulate beyond that identification. The Born rule is the inverse Jacobian of the projection that a situated reader is forced to use.

## 8. Wave, particle, and situation

The parallel (outside) reading and the serial (inside) reading are properties of the reader’s situation, not of the payload.

Let \(P\) be an arbitrary payload—an assignment of magnitudes to addresses. Let \(S\) be the reader’s situation, one of the three vantages:

- \(S_\parallel\): parallel/outside (maximal head rotation),
- \(S_\perp\): serial/inside (minimal head rotation),
- \(S_0\): unsituated (no head rotation).

Each situation induces a reading map that converts any payload into a scalar measure on the chord of true length 1:

\[
\begin{align*}
R_{S_\parallel}(P)&=\frac{\pi}{2},\\
R_{S_\perp}(P)&=\frac{2}{\pi},\\
R_{S_0}(P)&=1.
\end{align*}
\]

These values are independent of \(P\). They are the joint invariants of the straight walk and the head rotation that define the situation. By the payload-independence of the address density (the inverse Jacobian / Cauchy measure), the pair
\[
\bigl(R_S(P),\;\rho_{\mathrm{addr}}\bigr)
\]
is fixed once \(S\) is fixed, for every payload.

Consequently:

- under \(S_\parallel\) the payload is read as the \(\pi/2\) wave (received all at once);
- under \(S_\perp\) the payload is read as the \(2/\pi\) particle (accumulated point by point);
- under \(S_0\) the payload is read as the bare chord.

The Born rule supplies only the distribution of addresses once the situation has chosen the measure. It does not select the situation. The complementarity
\[
\frac{\pi}{2}-\frac{2}{\pi}=1
\]
remains a relation among situations, not among payloads. Whether any given payload appears as wave or as particle is therefore settled entirely by the reader’s facing.
