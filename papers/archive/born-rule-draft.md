# The Born Rule as the Density of Addresses of a Situated Reader

Tom Brinkman  
Draft, October 2026

## Abstract

We derive the Born rule from the geometry of a situated reader. A bounded observer whose reach is a finite number of steps of turn on a circle possesses addresses that are the directions of those steps. The unique map from equal steps of turn to a linear reading is the tangent projection. The unique invariant measure on the arc, pushed forward by this map, is the Cauchy density on the chord. Identifying a measurement outcome with the chord coordinate returned by the map converts the inverse Jacobian of the projection into the probability of the outcome. In angular coordinates the same quantity is \(\cos^2\theta\); on the projective space of pure states it is \(|\langle k|\psi\rangle|^2\). The square is the curvature of the forced map, not a postulate about amplitudes. The arc remains undisturbed; measurement changes only the reader’s position among the addresses. Collapse, superposition, and entanglement are reread as consequences of reading an undisturbed arc from a bounded chord.

## 1. Introduction

Standard quantum mechanics treats the Born rule as a postulate relating the squared modulus of an amplitude to the probability of a measurement outcome. The measurement problem asks why a measurement appears to select one outcome from a superposition. Both difficulties arise, we claim, from describing the situation as if a view from nowhere were available.

A situated reader is a bounded observer. Its reach is a finite number of steps of turn on a circle or sphere. Its addresses are the directions of those steps. Its readings of the world are the projections of those directions onto a linear chord. Nothing in this geometry requires a completed view of the circle, nor a description that is independent of the reader’s position. The quantum phenomena, we propose, are the consequences of reading an undisturbed arc from such a chord.

The derivation proceeds in two steps. First, pure geometry forces a unique map and a unique induced density: equal steps of turn, read as \(x=\tan\theta\), produce the Cauchy density on the chord. Second, a single physical identification—that a measurement returns a chord coordinate—converts that density into a probability rule. The familiar expressions \(\cos^2(\theta/2)\) and \(|\langle k|\psi\rangle|^2\) are recovered as evaluations of the same Jacobian. No further probability postulate is introduced.

## 2. Geometry of the Situated Reader

A situated reader has a unit relation \((h,v)\) with \(h^2+v^2=1\) and a known breadth \(H\). The corner is the fixed point of the flip \(v=h\). The reader’s addresses are the directions of equal steps of turn on the circle. The three vantages of the present paper—completed, parallel, and serial—correspond to the three ways the reader may hold the relation between its own breadth and the world. Only the serial vantage, in which the reader turns before the object is held, produces the Cauchy addresses.

The unique admissible map from angular positions \(\theta\in(-\pi/2,+\pi/2)\) on the arc to coordinates \(x\in\mathbb{R}\) on the chord is
\[
x=\tan\theta.
\]
It is forced by centrality, bijectivity with divergence at the endpoints, odd symmetry, and minimal degree. No other map satisfies the constraints. The unique rotation-invariant measure on the arc is the Haar measure \(d\theta/\pi\).

## 3. The Induced Density

Let the prior on configurations be the invariant measure \(d\mu=d\theta/\pi\). Observations are reported in the chord coordinate \(x\). The change-of-variable formula then forces the density on the observation space to be
\[
\rho(x)=\Bigl|\frac{d\theta}{dx}\Bigr|=\frac{1}{\pi(1+x^2)}.
\]
The Jacobian of the map is
\[
J(\theta)=\frac{d}{d\theta}\tan\theta=\sec^2\theta=1+x^2,
\]
so the inverse Jacobian is
\[
\frac{1}{J(\theta)}=\cos^2\theta=\frac{1}{1+x^2}.
\]
The square is the curvature of the projection expressed as a density transformation. Any map between curved and flat space with a quadratic Jacobian produces a squared density under change of variables. No additional rule is used.

In angular coordinates the same density reads
\[
\rho(\theta)=\frac{\cos^2\theta}{\pi/2}.
\]
This is the unique density consistent with the invariant measure on the arc and the forced map to the chord.

## 4. Identification with Measurement

The geometry so far is pure. To connect it to experiment one physical identification is introduced:

> Measurement outcomes correspond to chord coordinates returned by the observation map \(x=\tan\theta\).

This is the only non-geometric input. It plays the structural role that “observables are Hermitian operators” plays in the standard formulation: it names the correspondence between the mathematical object and the physical act.

Probability is not a prior over \(\theta\), nor an ensemble average. It is the arc measure per unit chord coordinate—the Jacobian \(d\theta/dx=1/(1+x^2)\). Under the identification above, this Jacobian is the probability density of the outcome. The wave function is arc content (the outside description). A measurement returns a chord coordinate (the inside reading). Probability is the structural residue of the projection.

The identification is the unique assignment consistent with three constraints: outcomes are points on the real line, the probability formula is invariant under changes of projection frame (elements of \(\mathrm{PSL}(2,\mathbb{R})\)), and the extremes of certainty are recovered at \(\theta=0\) and \(\theta=\pi\).

## 5. Recovery of the Born Rule

For a qubit the state lives on the Bloch sphere. The angular distance from \(|\psi\rangle\) to the outcome \(|0\rangle\) is \(\theta/2\). Evaluating the inverse Jacobian at this angle yields
\[
p(|0\rangle)=\cos^2\Bigl(\frac{\theta}{2}\Bigr)=|\langle 0|\psi\rangle|^2.
\]
The same evaluation on \(\mathbb{CP}^{n-1}\) uses the Fubini–Study distance \(d_{\mathrm{FS}}=\arccos(|\langle k|\psi\rangle|)\). The gnomonic projection at the outcome is \(|z|=\tan(d_{\mathrm{FS}})\). The inverse Jacobian is again
\[
p_k=\cos^2(d_{\mathrm{FS}})=|\langle k|\psi\rangle|^2
\]
for all \(n\geq 2\). The derivation has no dimension restriction; it covers the qubit case that Gleason’s theorem leaves open.

A third route, independent of the Jacobian, identifies the probability with a component of the metric: if the depth field is \(\Psi=e^{-(\phi+i\theta)}\), then \(|\Psi|^2=e^{-2\phi}=g_{tt}\). The three routes—Jacobian of the forced map, angular evaluation on projective space, and metric component—overdetermine the same formula.

## 6. Implications for Foundations

The arc is undisturbed by the reading. The Conservation Law of the present paper states that nothing in the domain is created or destroyed. What changes is the reader’s position among the addresses. The “collapse” is the chord receiving one resolved coordinate at the current rung; the unresolved remainder is filed at calculable later addresses. Superposition is the arc before it has been projected by this reader. Entanglement is shared arc content: two situated readers projecting onto different aspects of the same undivided arc obtain correlated chords without any signal propagating between them.

Repeated measurement is rung descent. Each projection receives a fixed fraction of the remaining arc and files the rest at the next address. The single-shot residual is Cauchy; accumulated measurements converge to Gaussian at the rate fixed by the chord-arc central limit theorem. The product of the convergence rate and the accumulated variance is a constant fixed by the geometry, a fixed-product constraint of the same algebraic type as the uncertainty principle.

Quantum non-demolition is the general case: every measurement preserves the arc. The distinction between demolition and non-demolition is whether the reader retains the address of the unresolved remainder.

## 7. Scope and Open Questions

The derivation does not produce the numerical values of masses or coupling constants. It produces the form of the probability rule and the reading of measurement as navigation among addresses. Interference arises from the combination of depth fields prior to projection, not from the combination of the densities derived here; that combination is treated elsewhere.

The open work is to keep the address/payload distinction intact while the payload is allowed to depend on the address, and to confirm that the same Jacobian continues to supply the correct conditional probabilities in that case. The Euclidean assumption underlying the circle and sphere, and the precise status of the scale-invariance of the addresses, remain to be sharpened.

## 8. Conclusion

The Born rule is the inverse Jacobian of the unique map that carries equal steps of turn on the arc of a situated reader to a linear reading on the chord. The Cauchy density is the law of the addresses; under the identification that a measurement returns a chord coordinate, it is the probability of the outcome. The square is the curvature of the projection. The arc is undisturbed. Measurement changes only the reader’s position among the addresses. The quantum world, on this reading, is situated observation.
