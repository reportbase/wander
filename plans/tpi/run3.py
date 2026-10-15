"""TPI run 3: score the blind classification (plans/tpi/classification.md) against run 2's routes. See plans/tpi-plan.md.
Run: python3 -I plans/tpi/run3.py plans/tpi/classification.md
"""
import sys, re

# run 2's routes, by occurrence (E even turn in the derivation, H hidden, S circle as a shape, P pole, U undetermined);
# C10 had two rows in run 2 (C10, C10b); C26, C39, C41 had none (U, E, E: the correction before run 3)
ROUTE = dict(K1='E', K2='E', K3='E', K4='H', K5='E', K6='E', K7='H', K8='E', K9='H', K10='H', K11='E', K12='E', K13='E',
             K14='E', K15='E', K16='S', K17='S', K18='H', K19='E', K20='H',
             C1='E', C2='U', C3='E', C4='E', C5='E', C6='E', C7='H', C8='P', C9='E', C10='H', C11='H', C12='H', C13='H',
             C14='E', C15='E', C16='E', C17='E', C18='E', C19='E', C20='E', C21='E', C22='E', C23='E', C24='E', C25='S',
             C26='U', C27='H', C28='E', C29='S', C30='S', C31='E', C32='S', C33='E', C34='E', C35='E', C36='E', C37='E',
             C38='E', C39='E', C40='E', C41='E', C42='E', C43='E', C44='S', C45='E')
ROWS2 = [k for k in ROUTE if k not in ('C26', 'C39', 'C41')] + ['C10']        # run 2's 63 rows (C10 twice)

q1, q2 = {}, {}
for line in open(sys.argv[1]):
    cells = [c.strip() for c in re.split(r'(?<!\\)\|', line)]          # cells may hold escaped pipes (|x|)
    if len(cells) > 6 and re.fullmatch(r'[KC]\d+', cells[1]):
        q1[cells[1]] = cells[3]
        q2[cells[1]] = re.match(r'(a|b|c|n/a)', cells[5]).group(1)
assert len(q1) == 65, len(q1)

want = {'E': 'a', 'H': 'a', 'S': 'b', 'P': 'c'}
match = [k for k in ROWS2 if want.get(ROUTE[k]) == q1[k]]
miss = [k for k in ROWS2 if want.get(ROUTE[k]) != q1[k]]
print(f"P5: {'not killed' if len(match) >= 57 else 'KILLED'}. routes agree on {len(match)} of {len(ROWS2)} rows (needs 57)")
print("  disagreements: " + ", ".join(f"{k} ({ROUTE[k]} vs {q1[k]})" for k in sorted(set(miss), key=lambda x: (x[0], int(x[1:])))))
S = [k for k in ROUTE if ROUTE[k] == 'S']
print(f"P6: {'not killed' if all(q1[k] == 'b' for k in S) else 'KILLED'}. route S on Q1: " + ", ".join(f"{k} {q1[k]}" for k in S))
turn = [k for k in ROUTE if ROUTE[k] in 'EH']
used = lambda ks: [k for k in ks if q2[k] != 'n/a']
infer = lambda ks: [k for k in ks if q2[k] in ('b', 'c')]
st, ss = len(infer(turn)) / len(used(turn)), len(infer(S)) / len(used(S))
print(f"P7: {'not killed' if st > ss else 'KILLED'}. inferring an unknown (Q2 b or c): turn entries {len(infer(turn))} of "
      f"{len(used(turn))} with a use ({st:.3f}; {len(infer(turn))} of {len(turn)} counting identities, "
      f"{len(infer(turn)) / len(turn):.3f}), route S {len(infer(S))} of {len(used(S))} ({ss:.3f})")
both = infer(turn)
print(f"both marks (a turn, and used to infer): {len(both)}: " + ", ".join(f"{k} ({q2[k]})" for k in both))
print("identities (no use): " + ", ".join(k for k in ROUTE if q2[k] == 'n/a'))
