"""TPI run 4: the third mark, a sweep. Scores Q3 (plans/tpi/classification-q3.md) with run 3's Q2 and run 2's routes.
See plans/tpi-plan.md. Run: python3 -I plans/tpi/run4.py plans/tpi/classification.md plans/tpi/classification-q3.md
"""
import sys, re
# run 2's routes by occurrence, as in run3.py (copied, so that run3's scoring does not run on import)
ROUTE = dict(K1='E', K2='E', K3='E', K4='H', K5='E', K6='E', K7='H', K8='E', K9='H', K10='H', K11='E', K12='E', K13='E',
             K14='E', K15='E', K16='S', K17='S', K18='H', K19='E', K20='H',
             C1='E', C2='U', C3='E', C4='E', C5='E', C6='E', C7='H', C8='P', C9='E', C10='H', C11='H', C12='H', C13='H',
             C14='E', C15='E', C16='E', C17='E', C18='E', C19='E', C20='E', C21='E', C22='E', C23='E', C24='E', C25='S',
             C26='U', C27='H', C28='E', C29='S', C30='S', C31='E', C32='S', C33='E', C34='E', C35='E', C36='E', C37='E',
             C38='E', C39='E', C40='E', C41='E', C42='E', C43='E', C44='S', C45='E')

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
