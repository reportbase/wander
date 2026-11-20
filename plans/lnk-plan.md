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
