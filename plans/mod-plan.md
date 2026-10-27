# MOD: each system its own unit, worked exactly

27 Oct 2026. Tom: "it seems to me that each system is self defined by its own ratios. the system may have used physics as
it constraints, why it used one breadth for another, or why it standardized on a specific set of breaths … they are their
units, based on its constraints."; then "yes, work out the exact cases". From `plans/tower-note.md` §2½.

## The claim

A system's unit is one of its own breadths (its module); every other breadth is a ratio to it; the ratios are chosen by
the system's constraint, stated in the system's own terms; tying the system to the outside is one written amount, and
the system does not change when it is written. Four cases where the constraint is mathematical: paper (ISO 216, 269),
preferred numbers (ISO 3), music (intervals and concert pitch), screw threads (ISO 68-1, 261).

## Data

Fetched 27 Oct from Wikipedia's wikitext (`action=raw`), kept in the scratchpad, not committed; sha256:

- `Paper_size` 980dbda84f750d06211aa1108b0ef91c335f14803cd5d5022c0a019bd452d9cf (A0–A10, B0–B10, C0–C10 in mm)
- `Renard_series` 3c69f9ada3a44b666ef0886725afd52e181c1ac868a8e1952403711f3f5345b7 (R5, R10, R20, R40, least rounded)
- `ISO_metric_screw_thread` 9d2ea50487090421f6ce8747b7a8dca57261509a6a7a8a1a4892b643d11e3096 (ISO 68-1's profile; ISO
  262's sizes and coarse pitches)
- `Concert_pitch` 9371b94460d26aa017fd6c271598cb827d3b7a84687a1ef8c6441eba326ed52a (435 Hz, 1859; 440 Hz, ISO 16)

The tables were read before these predictions were written (they are the input). While writing, I computed by hand two
things predicted below: R10's 1.60 is 0.95% above 10^(1/5), and a few A, B and C sizes follow the halving rule of M1(b).

## Predictions (written before any script)

Exact arithmetic (sympy and mpmath at 50 digits) unless a prediction says otherwise.

- **M1 (paper: the constraint gives √2, one amount gives the size).** (a) A rectangle halved across its long side keeps
  its shape exactly when its aspect r satisfies r² = 2. (b) Every listed size follows from three written amounts and
  one rule: A0 of area 1 m², B0 of short side 1 m, C0 the geometric mean of A0 and B0, each rounded to the nearest mm;
  then each next size's long side is the last one's short side and its short side the last one's long side halved and
  rounded down. All 66 listed values (A, B, C, 0–10, two sides each) come out exactly. (c) Every listed value is within
  1 mm of the exact size (A_n short side 2^(−1/4 − n/2) m, and so on). (d) A_n, C_n, B_n and A_(n−1) have sides in the
  exact ratios 1 : 2^(1/8) : 2^(1/4) : 2^(1/2): the three series are one system (ratio √2, halving) written with three
  amounts (areas 1, 2^(1/4), 2^(1/2) m²). Kill: any part off.
- **M2 (halving is an exchange, √2 its corner).** For any rectangle, halving sends its aspect r to 2/r exactly, so a
  halving series alternates r, 2/r, r, …; in units of √2 (x = r/√2) halving is x ↦ 1/x, the reciprocal, fixed only at
  x = 1. US Letter (8.5 × 11 in) alternates 1.2941 and 1.5455, and the geometric mean of its two shapes is √2 exactly.
  Kill: any of these off.
- **M3 (preferred numbers: equal steps in ratio, no unit at all).** (a) The listed R5, R10, R20 and R40 values are
  nested (each list contains the coarser ones). (b) Each listed value is within 1.3% of its exact 10^(k/n), the largest
  in R10 being 1.60's +0.95%. (c) Products and quotients of two listed R10 values, brought into [1, 10) by a power of
  10, fall within 3δ of a listed R10 value, δ the largest single deviation in (b). (d) 8 of the 10 listed R10 values
  are exactly 2^i·10^j (all but 3.15 and 6.30), because 2^10 = 1.024·10^3: the series' decades and doublings nearly
  coincide. (e) The series needs no written amount: it is the same list in any unit (it is written only when a unit is
  attached to it). Kill: any part off.
- **M4 (music: the string's modes give the ratios, one amount the pitch).** (a) A string's modes are n times its
  fundamental, whatever the string's length or tension, so the consonant intervals are ratios of small whole numbers
  (2/1, 3/2, 4/3, 5/4, 6/5, 5/3). (b) No number of pure fifths equals any number of octaves (3^k ≠ 2^m); twelve fifths
  over seven octaves is 531441/524288, 23.460 cents. (c) Asking for one set of pitches that transposes to every step
  alike with the octave pure forces equal steps, 2^(1/n): the fifth in twelve steps is 1.955 cents flat, the major
  third 13.686 sharp, the minor third 15.641 flat; the continued fraction of log₂(3/2) has convergents with
  denominators 1, 2, 5, 12, 41, 53, 306, and 53 steps leave the fifth 0.068 cents flat. (d) Concert pitch is the one
  written amount: moving A from 415 to 435 or 440 Hz multiplies every frequency by one factor and moves no interval
  (cents identical to 10⁻⁴⁰); 440·2^(−1/12) = 415.305 Hz, so baroque pitch is equal temperament's semitone below.
  Kill: any number off in its last stated digit, or an interval moved.
- **M5 (threads: the profile is ratios of the pitch; the pitch is not a ratio of the diameter).** (a) ISO 68-1's
  coefficients 0.649519 and 1.082532 are 3√3/8 and 5√3/8 to six places: the profile is stated in the pitch P alone
  (the 60° triangle of height √3/2·P, cut at 1/8 and 1/4 of it), the thread's own module. (b) The first-choice coarse
  pitches against their diameters (M1 to M64) are not one ratio: P/D falls from 0.25 to below 0.1, and a fitted power
  P ∝ D^a has a between 0.6 and 0.9. So between the profile and the diameter the link is a table of written amounts,
  one a size, not a ratio fixed by one constraint: a counter-case to "one ratio, one amount". Kill: (a) off, or (b) a
  within 5% of 1 (one ratio) or outside its band.

## Not claimed

Nothing about why each committee chose as it did beyond the constraint stated in each standard's own definition (R364);
the reading (module, constraint, one amount) is ours.

## Runs

### Run 1 (27 Oct; `runs/mod/mod.py`, output `runs/mod/mod-run1.txt`)

Killed by my code in three places, nothing about the predictions: the A2 row ends `&nbsp;||` with no space, so my pattern
skipped it and every later size was compared with the next one's (M1); the R10 value 1.60 held as the fraction 8/5 was
compared with the string '1.60' (M3); the convergents' denominators were compared as a list, where the continued fraction
gives 1 twice (0/1, 1/1) and the prediction listed distinct values (M4). The numbers M2 and M5 rest on were right.

### Run 2 (`runs/mod/mod-run2.txt`)

M1, M2, M4, M5 not killed. M3 killed by my code again (3.15 and 6.30 held as 63/20 and 63/10, compared as strings).

### Run 3 (`runs/mod/mod-run3.txt`; the numbers identical to run 2's)

- **M1 not killed.** √2 is the only aspect halving keeps. All 66 listed A, B and C sizes come out of three written
  amounts (A0 1 m², B0's short side 1 m, C0 their geometric mean), rounded to the mm, and one rule (the next size's long
  side the last one's short side, its short side the last one's long side halved and rounded down); the worst listed
  value is 0.78 mm from the exact size. A, C, B and the next A stand at 1 : 2^(1/8) : 2^(1/4) : 2^(1/2); the three
  series are one system written with areas 1, 1.1892 and 1.4142 m².
- **M2 not killed.** Halving sends r to 2/r; in units of √2 that is the reciprocal, fixed only at √2. US Letter
  alternates 1.2941 and 1.5455, and their geometric mean is √2 exactly.
- **M3 not killed.** The four series are nested; the largest deviations from 10^(k/n) are 0.95% (1.60, in R5 and R10),
  1.22% (1.80, R20) and 1.26% (1.70, R40); products and quotients of R10 values land within 2.4% of R10 (bound 2.86%);
  8 of the 10 R10 values are 2^i·10^j, all but 3.15 and 6.30 (2^10/10^3 = 128/125).
- **M4 not killed.** A string's modes give p/q whatever its fundamental; no pure fifths close on octaves; the comma
  23.460 cents; twelve equal steps leave the fifth 1.955 cents flat, the major third 13.686 sharp and the minor third
  15.641 flat; the convergents of log₂(3/2) have denominators 1, 2, 5, 12, 41, 53, 306, and 53 steps leave the fifth
  0.068 cents flat; a new A moves no interval (3·10⁻⁴⁸); 440·2^(−1/12) = 415.305 Hz.
- **M5 not killed.** ISO 68-1's 0.649519 and 1.082532 are 3√3/8 and 5√3/8: the profile is stated in the pitch alone.
  The 21 first-choice coarse pitches fall from P/D = 0.25 (M1) to 0.094 (M64), fitted P ∝ D^0.794: not one ratio.

## What MOD says

In three of the four cases the system is stated by its own constraint in its own terms, every breadth a ratio, and one
written amount ties it to the outside without changing it. Paper's constraint (a half keeps the shape) gives √2, and the
sheet is the module; A, B and C are one system written three times. The halving map is r ↦ 2/r, so in units of √2 it
is the reciprocal and √2 its fixed point: the standard sits at the halving's corner, and a sheet off it (Letter)
alternates between two shapes whose geometric mean is that corner. Preferred numbers need no written amount at all: equal
steps in ratio, the same list in any unit; their decades and doublings nearly coincide (2^10 ≈ 10^3), which is why most
of R10 is 2^i·10^j. Music's ratios come from the string's own modes, whatever its length; closing twelve keys forces
equal steps; concert pitch is the one amount, and moving it moves no interval. Threads are the counter-case Tom asked
for: the profile is ratios of the pitch (the thread's module), but the pitch against the diameter is a table of
amounts, one a size, P ∝ D^0.79, not one constraint's ratio. A system can be ratios within a level and amounts between
levels: there the link between levels is written, not read.
