"""DVC (plans/dvc-plan.md): Q4's expected share from the blind tags and classes alone (`python3 runs/dvc/dvb.py expect`),
then, once the restatements exist, the cross of tags, classes and the checker's verdicts (`python3 runs/dvc/dvb.py`)."""
import re, subprocess, sys
def read(path, pat):
    out = {}
    for line in open(path, encoding='utf-8'):
        m = re.match(pat, line)
        if m: out[int(m.group(1))] = m.group(2)
    return out
tag = read('runs/dvc/tags.md', r'\s*(\d+)\.\s*\**\s*([DA])\b')
cls = read('runs/dvc/blind-class.md', r'\s*(\d+)\.\s*\**\s*([ALX])\b')
laws = read('runs/dvc/laws.md', r'\s*(\d+)\.\s*\*\*(.+?)\*\*')
n = len(laws)
assert set(tag) == set(laws) == set(cls), (len(tag), len(cls), n)
cells = {(t, l): [k for k in laws if tag[k] == t and (cls[k] == 'L') == l] for t in 'DA' for l in (False, True)}
dnl, anl = len(cells[('D', False)]), len(cells[('A', False)])
expect = (0.60 * dnl + 0.10 * anl) / n
print(f'{n} laws; tags D {sum(1 for k in tag if tag[k]=="D")}, A {sum(1 for k in tag if tag[k]=="A")}; '
      f'classes A {sum(1 for k in cls if cls[k]=="A")}, L {sum(1 for k in cls if cls[k]=="L")}, X {sum(1 for k in cls if cls[k]=="X")}')
print(f'cells: D no limit {dnl}, D limit {len(cells[("D", True)])}, A no limit {anl}, A limit {len(cells[("A", True)])}')
print(f'Q4 expected share (0.60*{dnl} + 0.10*{anl})/{n} = {expect:.4f}')
if len(sys.argv) > 1 and sys.argv[1] == 'expect': sys.exit()
out = subprocess.run(['python3', 'runs/dvc/check.py'], capture_output=True, text=True).stdout
print(out.strip())
nota = set(int(x) for x in re.search(r'all notation: \[(.*)\]', out).group(1).split(', ') if x)
for (t, l), ks in cells.items():
    y = sorted(set(ks) & nota)
    print(f'{t} {"limit" if l else "no limit"}: {len(y)} of {len(ks)}' + (f' = {len(y)/len(ks):.1%}' if ks else '') + f' {y}')
dn = len(set(cells[('D', False)]) & nota); an = len(set(cells[('A', False)]) & nota)
lim = set(cells[('D', True)]) | set(cells[('A', True)])
print('Q1 (no L law notation):', 'not killed' if not (lim & nota) else f'KILLED {sorted(lim & nota)}')
if dnl < 10: print('Q2 void: fewer than 10 D laws with no limit')
else: print(f'Q2 (D no limit 45-75%): {dn}/{dnl} = {dn/dnl:.1%}', 'not killed' if .45 <= dn/dnl <= .75 else 'KILLED')
print(f'Q3 (A no limit under 20%): {an}/{anl} = {an/anl:.1%}', 'not killed' if an/anl < .2 else 'KILLED')
true = len(nota) / n
print(f'Q4 (overall within 8 points of {expect:.1%}): {len(nota)}/{n} = {true:.1%}', 'not killed' if abs(true - expect) <= .08 else 'KILLED')
