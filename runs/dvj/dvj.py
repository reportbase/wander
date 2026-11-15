"""DVJ (plans/dvj-plan.md): J3's expected share from the blind chart classes alone (`python3 runs/dvj/dvj.py expect`),
then, once the restatements exist, the chart classes crossed with the checker's verdicts (`python3 runs/dvj/dvj.py`)."""
import re, subprocess, sys
def read(path, pat):
    out = {}
    for line in open(path, encoding='utf-8'):
        m = re.match(pat, line)
        if m: out[int(m.group(1))] = m.group(2)
    return out
ent = read('runs/dvj/chart.md', r'\s*(\d+)\.\s*\**\s*(chart|other)\b')
laws = read('runs/dvj/laws.md', r'\s*(\d+)\.\s*\*\*(.+?)\*\*')
n = len(laws)
assert set(ent) == set(laws), (len(ent), n)
D = [k for k in laws if ent[k] == 'chart']; O = [k for k in laws if ent[k] == 'other']
expect = (0.92 * len(D) + 0.03 * len(O)) / n
print(f'{n} laws; class chart {len(D)}, other {len(O)}')
print(f'J3 expected share (0.92*{len(D)} + 0.03*{len(O)})/{n} = {expect:.4f}')
if len(sys.argv) > 1 and sys.argv[1] == 'expect': sys.exit()
out = subprocess.run(['python3', 'runs/dvj/check.py'], capture_output=True, text=True, env={**__import__('os').environ, 'DVJ_SPLIT': '1'}).stdout
print(out.strip())
nota = set(int(x) for x in re.search(r'all notation: \[(.*)\]', out).group(1).split(', ') if x)
d, o = sorted(set(D) & nota), sorted(set(O) & nota)
print(f'chart notation {len(d)} of {len(D)}; other notation {len(o)} of {len(O)} {o}')
print(f'chart content: {sorted(set(D) - nota)}')
if len(D) < 15: print('J1 void')
else: print(f'J1 (chart >= 85%): {len(d)/len(D):.1%}', 'not killed' if len(d)/len(D) >= .85 else 'KILLED')
if len(O) < 15: print('J2 void')
else: print(f'J2 (other <= 10%): {len(o)/len(O):.1%}', 'not killed' if len(o)/len(O) <= .10 else 'KILLED')
true = len(nota) / n
print(f'J3 (within 8 points of {expect:.1%}): {len(nota)}/{n} = {true:.1%}', 'not killed' if abs(true - expect) <= .08 else 'KILLED')
