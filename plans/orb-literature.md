# ORB: prior work on the orbit's stage, its standpoint and aberration's form

25 November 2026 (Tom: "Proceed", to the search offered after ORB runs 4–5). One search by a fresh agent, read-only,
at search-engine depth, not a citation trace. "Opened" means the source's own text was read; "snippet" means a search
summary only. Not found is not absent (R925). My expectations were committed before the search ran; nothing above the
"Search" line is edited afterwards.

## What I expect, before the search

- **X1. The map itself is textbook.** tan(ν/2) = √((1 + e)/(1 − e))·tan(E/2) is in every celestial-mechanics text.
  Expected found.
- **X2. β is classical.** β = (1 − √(1 − e²))/e = e/(1 + √(1 − e²)) is the ratio in the series ν − E =
  2·Σ βⁿ·sin(nE)/n (Lagrange, Laplace, Brouwer and Clemence). Expected found; I do not expect it called a standpoint.
- **X3. The stage as a wrapped Cauchy.** That uniform E pushed to ν is a wrapped Cauchy (a Möbius image of the uniform
  circle, McCullagh 1996; Kato and Jones), with ρ = β: I expect it found in circular statistics or in a paper on random
  orbital phases, at most once or twice. Even odds.
- **X4. The likeness to aberration.** That the E → ν map has the form of relativistic aberration, tan(θ′/2) =
  √((1 + v)/(1 − v))·tan(θ/2), with e as the speed and e = tanh η: I expect it in print somewhere (a teaching note, a
  paper on the Kepler problem's hidden symmetry, or the hyperbolic geometry of the eccentric anomaly). Better than
  even odds found.
- **X5. Composition by velocity addition.** That two such maps compose as eccentricities added by (e₁ + e₂)/(1 + e₁e₂):
  expected found only if X4 is, and less often.
- **X6. The heat and the paint.** That time per direction is the wrapped Cauchy times r/a, and Kepler's equation its sum
  over the stage, said as a law of directions times a payload: expected not found in those terms; the pieces (dt/dν
  ∝ r², dM = (r/a)·dE) are textbook.

## Search

About fifteen queries by a fresh agent. Opened: Wikipedia's "True anomaly", "Eccentric anomaly", "Equation of the
center" and "Relativistic aberration"; Savransky, Cady and Kasdin, "Parameter distributions of Keplerian orbits",
*ApJ* 728:66 (2011), arXiv:1012.1526; Lavenda's blog post below. Brouwer and Clemence, Battin and Gauss not opened;
Fitzpatrick's notes did not answer (HTTP 503).

| | verdict | sources |
| --- | --- | --- |
| X1 the map | found | Battin, *An Introduction to the Mathematics and Methods of Astrodynamics* (AIAA 1999), §5; Smart, *Textbook on Spherical Astronomy* (1977), p. 120; Roy, *Orbital Motion* (2005), via Wikipedia (opened). Sato, *Astron. J.* 116 (1998), generalises it to tan(Θ/2) = λ·tan(u/2) (snippet) |
| X2 β | partly | β = (1 − √(1 − e²))/e defined in Brouwer and Clemence (1961), p. 62, via Wikipedia's "Equation of the center" (opened), used there in the series in M. tan((ν − E)/2) = β·sin E/(1 − β·cos E) and √(1 − e²)/(1 − e·cos u) = 1 + 2Σβʲ·cos(ju) in snippets (Fitzpatrick's "Elliptic expansions"; arXiv:1006.5130). No attribution to Lagrange or Laplace found; β = tan(φ/2) not seen stated, though Gauss's tan(ν/2) = tan(45° + φ/2)·tan(E/2) (*Theoria Motus*, 1809, from memory) gives it; β as a point of the disc not found |
| X3 the stage a wrapped Cauchy | not found | Savransky et al. take M uniform, not E. The pieces are McCullagh, *Ann. Statist.* 24(2), 787–808 (1996), doi:10.1214/aos/1032894465 (abstract): the wrapped Cauchy family closed under Möbius maps of the circle; Kato and McCullagh, *Bernoulli* 26(4) (2020). The E → ν map is such a map, so the result follows; no source joining them found |
| X4 aberration's form | not found | Wikipedia's aberration article (opened) has the half-angle form, nothing on Kepler. Nearest: B. Lavenda, "The analogy between the Kepler problem and retarded electrodynamic potentials" (blog, bernardlavenda.org, opened): the cos/sin relations in E "look like an aberration formula", e as the relative velocity; no half-angle form, rapidity or Möbius map; unrefereed |
| X5 composition by velocity addition | not found | |
| X6 the heat times the paint | not found as such | dM = (r/a)·dE and dt/dν ∝ (1 + e·cos ν)^(−2) textbook (Tatum, LibreTexts, snippet) |

## What this leaves

X1 held, X2 held in part (β is Brouwer and Clemence's, but I did not see the E-series or β = tan(φ/2) in an opened
source), X5 and X6 held. X3 at its even odds fell on not found. **X4 was wrong**: I expected aberration's form in print and
found only Lavenda's hint, which names a likeness without the half-angle map. So not found, in one search: the stage as
a wrapped Cauchy from −β, the E → ν map as a hyperbolic translation by artanh e with aberration's form, its composition
by velocity addition, and time per direction as the stage times r/a. Every piece under them is classical (the map,
β, McCullagh's closure, aberration's half-angle form), and one search does not make the joins new (R925).

## Second search (expectations committed before it ran)

25 November 2026, Tom: "1 2 3", the first being a proper confirmation of the first search. One fresh agent, the primary
texts opened where they can be reached: Gauss's *Theoria Motus* (1809; Davis's English translation, 1857, public
domain), Brouwer and Clemence (1961) if reachable, and the literature on the Kepler problem's hidden symmetry (Fock
1935, Bargmann 1936, Moser 1970; the SO(4) and SO(3,1) treatments, Cushman and Bates).

- **Y1.** Gauss writes the map as tan ½v = tan(45° + ½φ)·tan ½E. Expected found, opened.
- **Y2.** β = tan(φ/2) stated in so many words: expected not found (it follows from Y1 in one line).
- **Y3.** The E → ν map as aberration's form, or as a hyperbolic translation of the disc by artanh e: expected not found
  in the symmetry literature either, since those works lift the problem to momentum space or the four-sphere, not to
  the anomaly's disc. If found, the joins of ORB runs 4–5 are known and the essays are corrected.
- **Y4.** The ellipse e and the hyperbola 1/e sharing k (run 6's R3): expected not found as such.

### Second search: results

About fourteen searches and fetches. Opened: Gauss, *Theory of the Motion of the Heavenly Bodies*, C. H. Davis's
translation (1857), archive.org `theoryofmotionof00gausuoft` (OCR full text); the abstract of Hsu, arXiv:2602.12034.
Not opened: Brouwer and Clemence (archive.org lending only, 401).

| | verdict | sources |
| --- | --- | --- |
| Y1 Gauss's form | found, opened | Book I, Art. 8: "Greater elegance is attained in most of these formulas by introducing in the place of e the angle the sine of which = e"; formula VII, "tan ½E = tan ½v · tan(45° − ½φ)", with √((1 − e)/(1 + e)) = tan(45° − ½φ) |
| Y2 β = tan(φ/2) stated | not found | Gauss declines the series (Art. 11: "by no means so well suited to practical use"); sin ½φ, cos ½φ and tan(45° − ½φ) appear only as auxiliaries. The series with (1 + β)/(1 − β) = √((1 + e)/(1 − e)) in arXiv:1707.02088 (snippet) |
| Y3 aberration's form, the boost, velocity addition | not found, one lead unverified | An Academia.edu paper, "Gudermannian – Kepler Equations of Planetary Motion" (academia.edu/3832741; author and year unknown; the page refused, 403; an automatic summary only) says the anomalies can be written in a "Lorentz transformation" description and links the velocity parameterization to "light aberration equations". **The likeliest prior statement, and the one to confirm.** Hsu, arXiv:2602.12034 (2026; abstract opened): the Ligon–Schaaf regularization and the anomalies, no boost or velocity addition. Fock, Moser, Ligon–Schaaf, Milnor's hodograph, Stack Exchange: nothing |
| Y4 e and 1/e sharing k | not found as a statement, implied by Gauss | Gauss's hyperbola (Art. 21, formula III) uses ψ with cos ψ = 1/e′ and tan ½F = tan ½v·tan ½ψ (his F a circular angle, the gudermannian of today's hyperbolic anomaly); tan ½ψ = √((e′ − 1)/(e′ + 1)), which at e′ = 1/e is Art. 8's tan(45° − ½φ), ψ = 90° − φ. Art. 29 joins the elliptic and hyperbolic quantities by i = √−1, an analytic continuation of the same e, not an exchange of e with 1/e |

**What it leaves.** Y1, Y2 and Y4 held as expected (Y4 found implied, as Y2's identity is, by one line from Gauss).
Y3 is not settled: no opened source states the map as aberration's form or a boost, but one unopened paper's summary
says something close, and until it is read the aberration likeness of ORB runs 4–5 is marked as possibly in print.

**Then** (a web search for the paper's title, its abstract seen in the search's summary, the paper itself still not
opened): "Gudermannian – Kepler Equations of Planetary Motion" (academia.edu/3832741) writes the relation between the
true and the eccentric anomaly as Lorentz transformations, the anomalies as space-time coordinates, through the
Gudermannian (tan χ = sinh q, sin χ = tanh q), and calls the result "similar to light aberration equations". So the
likeness of the E → ν map to aberration is in print, in an unrefereed paper of unknown author and date; **Y3's "not
found" is withdrawn** and the claim that the joins of ORB runs 4–5 were not found is narrowed to the composition by
velocity addition and the stage as a wrapped Cauchy from −β, pending the paper's text.

**Then** (25 November; Tom, after the paper could not be downloaded: "It's not working. For the most part, we should
expect this idea to be well known if it was known and the well explained in wiki."): the paper is left unread. The
likeness is named once, in an unrefereed paper, and is not in the standard accounts (Wikipedia's "Relativistic
aberration", "Eccentric anomaly", "True anomaly", opened in the first search), so it is recorded as not well known.
Y3's withdrawal stands for "not in print"; the papers now say "named once, not in the standard accounts".
