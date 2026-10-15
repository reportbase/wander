"""TPI run 4: the third mark, a sweep. Scores Q3 (plans/tpi/classification-q3.md) with run 3's Q2 and run 2's routes.
See plans/tpi-plan.md. Run: python3 -I plans/tpi/run4.py plans/tpi/classification.md plans/tpi/classification-q3.md
"""
import sys, re
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from run3 import ROUTE          # noqa: E402  (run 2's routes by occurrence)

def table(path, col):
    out = {}
    for line in open(path):
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', line)]
        if len(cells) > col and re.fullmatch(r'[KC]\d+', cells[1]):
            out[cells[1]] = re.match(r'(a|b|c|n/a)', cells[col]).group(1)
    return out

q2 = table(sys.argv[1], 5)
q3 = table(sys.argv[2], 3)
assert len(q2) == 65 and len(q3) == 65, (len(q2), len(q3))
S = [k for k in ROUTE if ROUTE[k] == 'S']
ident = [k for k in ROUTE if q2[k] == 'n/a']
bad8 = [k for k in S + ident if q3[k] != 'c']
print(f"P8: {'not killed' if not bad8 else 'KILLED'}. route S and identities on Q3: "
      + ", ".join(f"{k} {q3[k]}" for k in S + ident) + (f"; not (c): {', '.join(bad8)}" if bad8 else ''))
turn = lambda k: ROUTE[k] in 'EH'
infer = lambda k: q2[k] in ('b', 'c')
three = [k for k in ROUTE if turn(k) and infer(k) and q3[k] == 'a']
print(f"P9: {'not killed' if len(three) >= 3 else 'KILLED'}. all three marks (turn, inferring, swept in order): "
      f"{len(three)}: {', '.join(three)}")
print("Q3 counts: " + ", ".join(f"{x} {sum(1 for k in q3 if q3[k] == x)}" for x in 'abc'))
print("by marks (turn / infer / Q3):")
from collections import defaultdict
grid = defaultdict(list)
for k in ROUTE:
    grid[('turn' if turn(k) else ROUTE[k], 'infer' if infer(k) else ('identity' if q2[k] == 'n/a' else 'compute'), q3[k])].append(k)
for key in sorted(grid):
    print(f"  {key[0]:5s} {key[1]:8s} {key[2]}: {len(grid[key]):2d}  {', '.join(grid[key])}")
