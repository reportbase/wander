# OFS review 11: ChatGPT on the Gaussian outside and the Cauchy inside

*Shared by Tom, 15 October 2026, about 18:31 MDT, after SPN R271–R275 (two sweeps; the address points at the payload;
the density in full). Kept as received; the response and what was made follow.*

## As received

I think the key to your question is that the Gaussian outside and Cauchy inside may not be two competing descriptions of the same distribution. They may be the results of two different ways of sweeping the same visible hemisphere.
The thing to explain is not merely why one curve has lighter tails than the other. It is why changing the observational relationship—from outside the arc to inside it—changes the law.
There is a promising geometric lead in your framework:

* Outside sweep → Gaussian: the observer has the payload values themselves and can aggregate them. A Gaussian often emerges when many contributions are combined under suitable independence and finite-variance conditions.
* Inside sweep → Cauchy: the observer has addresses to payloads. The angular geometry transforms those addresses into ratios, and ratios can produce heavy-tailed distributions. In your construction, the Cauchy law is associated with \(s=\tan\theta\), not necessarily with the distribution of the payload values.

The important qualification is that neither result follows from “outside” or “inside” alone. A Gaussian needs assumptions about how contributions combine; a Cauchy distribution needs a particular mapping and sampling measure. Your geometry may supply those assumptions—but that is precisely what we need to establish.
There is a particularly interesting mathematical connection here that may give you the missing “why.”
The Gaussian-to-Cauchy bridge
Suppose the outside payload is represented by two Gaussian components, \(X\) and \(Y\), with equal variance, zero means, and rotational symmetry.
1. Outside: Gaussian values
The outside has the actual magnitudes. Under suitable conditions, contributions combine into a Gaussian distribution. In two dimensions, rotational symmetry means the direction is uniform even though the radius is not.
2. Inside: ratio address
The inside does not need the radius. It reads the relationship between the components:
\[ s=\frac{X}{Y}=\tan\theta \]
A uniformly distributed angle, transformed by tangent, produces a Cauchy distribution.
MathOverflow
+1

That gives us a possible structural explanation:
The Gaussian describes magnitudes; the Cauchy describes ratios that discard magnitude and retain direction.
The Cauchy is not necessarily a second population of physical values. It can arise from the same underlying Gaussian values when the observer's operation changes from reading magnitudes to reading ratios.
There are important conditions here: the two Gaussian components must have the appropriate rotational symmetry, and the ratio must be formed in the right way. The standard result is that the ratio of two independent, zero-mean Gaussian variables with equal variance is Cauchy.
en.wikipedia.org
+1

How this might fit your two sweeps
Your geometry already has the key operation:
\[ s=\frac{v}{h}=\tan\theta \]
So the research question becomes very specific:

* Does the outside sweep preserve the payload's magnitude information and yield a Gaussian law under defined aggregation assumptions?
* Does the inside sweep remove magnitude information and retain only the ratio, yielding the Cauchy address law?
* Does the visible-hemisphere geometry itself guarantee the required angular sampling, or does that require an additional assumption?

The third question is the crucial one. A Gaussian distribution does not automatically imply a Cauchy distribution for every ratio. The rotational symmetry is what makes the connection work.
And there is one further distinction: this explains a Gaussian-to-Cauchy relationship, but it does not yet prove that the outside calculates a mean while the inside calculates a median. That would need its own derivation.
My strongest current hypothesis is that the reason lies in the change of invariant: the outside retains magnitude, while the inside retains proportion. Your paper may already contain the geometry of that change. The next step is to determine whether it derives the Gaussian side as well, or whether that side still needs an independent premise.

## Response (Claude, 15–16 October)

The bridge is correct and classical: the ratio of two independent zero-mean normals is a Cauchy, standard when the
spreads are equal (X/Y = tan θ with θ even). It goes further than the comment says, because the Gaussian side need not be
assumed. By the Herschel–Maxwell theorem (Herschel 1850, Maxwell 1860), a law of two independent components that every
turn leaves unchanged is the isotropic normal. OFS already grants the turns (Proposition 3(e), Jaynes's group); the one
premise added is that the payload's two components vary independently. So the third question ("does the visible-hemisphere
geometry itself guarantee the required angular sampling?") is answered: the turns give the even direction, and
independence gives the normal. Two consequences the comment did not draw:
- unequal spreads leave the ratio a Cauchy of scale σ_v/σ_h, OFS Proposition 5(d) with c = σ_v/σ_h, so equal spreads
  are the drawing V = H;
- for the isotropic normal the size is independent of the direction, the payload and its address separating exactly
  (OFS Theorem 6(a)); a payload off centre is no longer read as a Cauchy (R275).
Its caution stands: the geometry shows which law each sweep gets, not that a reader computes a mean; the mean belongs to
the normal and the median to the Cauchy as their natural centres.

## Made (SPN R276)

- `plans/hmx-plan.md` (+ `hmx/`): predictions first, exact (mpmath). P1 killed by my set-up (the unit circle never left the
  uniform's support); P1′ on a circle of radius 1.2 not killed; P2–P5 not killed.
- OFS §7.1, "Why the payload is Gaussian", after "When the density varies with direction"; §3.1's "Two sweeps, two
  results" points to it; references Herschel 1850 and Maxwell 1860.
