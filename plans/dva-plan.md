# DVA: is a law's π or e notation exactly where it relates directions?

14 November 2026. Tom: "1 2", to Claude's suggestions after NTX (R995): test NTX's post hoc reading, then narrow the
papers.

## The reading under test

NTX's post hoc reading (untested): a law's π or e is notation (NTN's rule) where the law relates directions or ratios of
like quantities among themselves, and content where an amount with a unit enters (a time, an energy over kT, a length, a
period counted in seconds), whether through a chart or a limit. If so, NTN's 30 of 82 and NTX's 18 of 107 differ because
*Reads and Writes* states mostly laws of the first kind and a textbook list mostly of the second.

## The borderline, settled before anything runs

A restatement that only renames an exponential of an amount (k = e^(−t/τ), so V = V₀(1 − k)) is not a restatement: the
law's input t is replaced by the transcendental function itself. NTX's verdicts (which called these NONE) stand as
counted; NTN's verdicts stand as counted (its law 2, e^(ln a + ln b) = ab, takes the ratios a and b as inputs, not an
amount). No restatement is rerun; the verdicts are NTN run 1's 30 and NTX run 1's 18, by the rule as fixed.

## Method (fixed before anything runs)

1. A fresh agent gets `runs/pie/flagged.md` (NTN's 82) and `runs/ntx/laws.md` (NTX's 107) and the definitions below, and
   none of the verdicts, restatements, classes, plans or papers, and tags each law **D** or **A**, writing
   `runs/dva/tags.md`:
   - **D**: every quantity the law relates is a direction or a ratio of like quantities, dimensionless by construction
     (an angle, a slope, a share, a cosine, a rapidity, a ratio of two lengths or two intensities), and the law relates
     them among themselves.
   - **A**: an amount with a unit enters the law (a time, a length, an energy, a mass, a temperature, a frequency, a
     charge, a count), including where it is divided by a scale to make an exponent or an argument (t/τ, E/kT, ωt, x/a),
     or where the law's constant normalizes a density over amounts.
2. `runs/dva/dva.py` crosses the tags with the verdicts.

## Predictions (committed before any run)

- **D1** On NTN's list: of laws tagged D, at least 60% are notation; of laws tagged A, at most 10%. Kill: either fails.
- **D2** On NTX's list: the same two bounds. Kill: either fails.
- **D3** Of all 48 notation laws (30 + 18), at least 85% are tagged D. Kill: fewer.
- **D4** The share tagged D is higher on NTN's list than on NTX's by at least 20 percentage points. Kill: less.

## Runs

(appended below as they come out; nothing above this line edited afterwards)

### Run 1 (14 Nov 2026; tags `runs/dva/tags.md` by a fresh agent, crossed in `runs/dva/dva.py`, output `runs/dva/dva-run1.txt`)

Tags: NTN's list D 66, A 16; NTX's list D 44, A 63. The verdicts are the two checkers' as run (30 and 18).

- **D1 killed**: on NTN's list 27 of 66 D laws are notation (40.9%, under 60%); 3 of 16 A laws (18.8%, over 10%: 2, 30,
  43).
- **D2 killed**: on NTX's list 14 of 44 D (31.8%); 4 of 63 A (6.3%, inside: 13 and 14, the laws of cosines and sines with
  sides as lengths; 91 the projectile's range; 101 the Breit–Wigner line, which carries no π).
- D3 not killed: 41 of the 48 notation laws are tagged D (85.4%, at its edge).
- D4 not killed: D is 80.5% of NTN's list against 41.1% of NTX's, 39 points.

Said plainly: relating directions is close to necessary for notation (85% of it) and far from sufficient (a third to two
fifths of D laws). Post hoc, untested, the blind classes of PIE and NTX run 1 (A/L/X) crossed with these tags: every one
of the 43 D laws classed L (a limit: series, products, integrals over a whole range, normalizing totals) is content, on
both lists; D laws not classed L are notation at 63% (27 of 43) on NTN's list and 58% (14 of 24) on NTX's; A laws not
classed L at 43% (3 of 7) and 10% (4 of 41). So the rate that carries from the paper's laws to a textbook's is for laws
that relate directions and take no limit, about three in five on either list; the difference in the overall rate (37%
against 17%) is mostly how many laws of that kind each list holds (43 of 82 against 24 of 107). The remaining D laws that
stay content without a limit are identities that state an angle's value (complementary arctangents, Machin's formula,
Euler's identity) or a chart taken as the subject (the natural logarithm as an integral, decibels, Tsiolkovsky, the
capstan). The two tags and the classes come from different blind agents; the cross was made after the counts.
