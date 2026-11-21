# LNK: how a word's link to another falls with distance

20 Nov 2026. SPN R1148. Tom: "Not all links the same, maybe close links are better" (R1147), then "Yes" to an exact count.
No training (R1139): counts on a text.

## The question

In a record of writes (a text, R1145) are close links worth more than far ones, and does the fall follow the paper's
near and far field on the record's order? Two forms are put to it:
- **the Cauchy in distance** (R703, the overlay laid on positions): heat ∝ 1/(1 + (d/H)²), flat inside a thumb H, falling
  as 1/d² past it (each doubling of d a quarter);
- **a power law** d^(−β) with no corner (the classical form for text, Lin and Tegmark 2017, from memory, not opened).

## Set-up

WikiText-2 (train split, `Salesforce/wikitext`, wikitext-2-v1, cached from CAH), split on spaces, the 2,000 commonest
words kept and the rest one symbol. For each distance d in 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256,
384, 512: the mutual information I(d) in bits between the word at i and the word at i + d (plug-in counts), less the same
with the second word's positions shuffled (seeded; the counting bias), and its spread from five equal parts of the text.
A distance counts only where I(d) is above three spreads of the shuffled control.

## Predictions (committed before the script is written)

- **L1 (close links count more).** I(d) falls from each listed d to the next, within twice the spread. Killed if it rises
  by more anywhere.
- **L2 (the Cauchy in distance).** One H makes I(d) = I(1)·(1 + 1/H²)/(1 + (d/H)²) agree within 25% at every counted d.
  Killed if no H does.
- **L3 (a power law with no corner).** Over the counted d from 8 on, log I against log d is fitted better by a straight
  line (two numbers) than by L2's form with its scale also free (two numbers), by squared log error. Killed if not.
- **L4 (the far field by ratios).** From d = 16 on, the ratio I(2d)/I(d) stays within 0.15 of one value. Killed if not.

A killed prediction stays killed; a fix is a new run with its own prediction.

## Runs

### Run 1 (20 Nov 2026)

`python3 runs/lnk/lnk.py` (about a minute); output `runs/lnk/lnk-results.json`. 2,051,910 words. I(d) in bits, the
counting bias (0.403 bits, the shuffled control) taken off:

| d | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 |
|---|---|---|---|---|---|---|---|---|---|---|
| I(d) | 1.246 | 0.484 | 0.139 | 0.056 | 0.033 | 0.024 | 0.019 | 0.015 | 0.014 | 0.011 |

Slope of log I against log d between neighbours: −1.4 to −1.8 for d up to 4, about −1 at 8, then −0.2 to −0.5 from 12 on.

- **L1 not killed:** I(d) falls at every counted step.
- **L2 killed:** the best single H (1.67) misses by 81% somewhere; the near links fall far faster than the far ones, not
  flat then 1/d².
- **L3 not killed:** from 8 to 32 a straight line in log (slope −0.59) beats the Cauchy form with its scale free.
- **L4 not killed, but barely a test:** only one ratio, I(32)/I(16) = 0.75, fell inside the counted range.

My set-up limited the counted range: the rule required I(d) above three spreads of the shuffled control *taken over
fifths of the text*, where the counting bias is about five times larger and spreads 0.0075; on the whole text the
control was 0.403 at every d to within 0.001, and every I(d) to 512 lies well above that. So only d ≤ 32 counted, and L3
and L4 rest on few points. The table above is the full measurement; the verdicts are by the rule as written.

**Reading, after the run, not a test.** Close links count for much more (R1147): the next word tells 1.25 bits, the
fourth 0.14, the sixteenth 0.03. The fall is not the Cauchy in distance (no flat near field), and not one power law
either: two regimes, a steep one over the first eight words or so (about d^(−1.5)) and a shallow one past it (about
d^(−0.3)), a knee near d ≈ 8–12, roughly a sentence's reach. Read on the paper's terms, the knee is a corner of the
record's own, with the near links falling fast and the far links holding by slow ratios (about 0.8 a doubling); a
thumb in positions of about ten words. A post hoc reading of one text; a run 2 with the counting rule fixed, and another
text, would test it.
