"""DVA run 1 (plans/dva-plan.md): blind D/A tags crossed with NTN's and NTX's notation verdicts (by their checkers)."""
import re, subprocess
tags = {'NTN': {}, 'NTX': {}}
sec = None
for line in open('runs/dva/tags.md', encoding='utf-8'):
    if line.startswith('## NTN'): sec = 'NTN'
    elif line.startswith('## NTX'): sec = 'NTX'
    m = re.match(r'\s*(\d+)\.\s*\**([DA])\b', line)
    if m and sec: tags[sec][int(m.group(1))] = m.group(2)
def notation(path):
    out = subprocess.run(['python3', path], capture_output=True, text=True).stdout
    return set(int(x) for x in re.search(r'all notation: \[(.*)\]', out).group(1).split(', '))
nota = {'NTN': notation('runs/ntn/check.py'), 'NTX': notation('runs/ntx/check.py')}
res = {}
for L in ('NTN', 'NTX'):
    t, n = tags[L], nota[L]
    D = [k for k in t if t[k] == 'D']; A = [k for k in t if t[k] == 'A']
    dn, an = len(set(D) & n), len(set(A) & n)
    res[L] = (dn / len(D), an / len(A), len(D) / len(t))
    print(f'{L}: {len(t)} tagged; D {len(D)} ({dn} notation, {dn/len(D):.1%}); A {len(A)} ({an} notation, {an/len(A):.1%}); '
          f'notation tagged A: {sorted(set(A) & n)}; untagged notation: {sorted(n - set(t))}')
alln = [(L, k) for L in nota for k in nota[L]]
inD = sum(1 for L, k in alln if tags[L].get(k) == 'D')
print(f'D1 (NTN D>=60%, A<=10%): {"not killed" if res["NTN"][0] >= .6 and res["NTN"][1] <= .1 else "KILLED"}')
print(f'D2 (NTX D>=60%, A<=10%): {"not killed" if res["NTX"][0] >= .6 and res["NTX"][1] <= .1 else "KILLED"}')
print(f'D3 (notation tagged D >= 85%): {inD}/{len(alln)} = {inD/len(alln):.1%} {"not killed" if inD/len(alln) >= .85 else "KILLED"}')
gap = res['NTN'][2] - res['NTX'][2]
print(f'D4 (D share NTN - NTX >= 20 pts): {res["NTN"][2]:.1%} - {res["NTX"][2]:.1%} = {gap:.1%} {"not killed" if gap >= .2 else "KILLED"}')
