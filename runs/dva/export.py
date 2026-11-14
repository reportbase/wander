"""Gather NTN's 82 and NTX's 107 laws into one JSON for notation.html: name, formula, the blind D/A tag (DVA), the blind
A/L/X class (PIE, NTX), the notation verdict by each list's checker, and the restatement or the reason none was found.
Run from the repository root: python3 runs/dva/export.py > runs/dva/laws.json"""
import importlib.util, json, re, subprocess

def load(path):
    spec = importlib.util.spec_from_file_location('m', path); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return {L['n']: L for L in m.LAWS}

def listed(path):
    out = {}
    for line in open(path, encoding='utf-8'):
        m = re.match(r'\s*(\d+)\.\s*\*\*(.+?)\*\*:\s*(.+?)\s*$', line)
        if m: out[int(m.group(1))] = (m.group(2).strip(), m.group(3).strip())
    return out

def classes(path):
    out = {}
    for line in open(path, encoding='utf-8'):
        m = re.match(r'\s*(\d+)\.\s*\**\s*([ALX])\b', line)
        if m: out[int(m.group(1))] = m.group(2)
    return out

def notation(path):
    out = subprocess.run(['python3', path], capture_output=True, text=True).stdout
    return set(int(x) for x in re.search(r'all notation: \[(.*)\]', out).group(1).split(', '))

tags = {'NTN': {}, 'NTX': {}}; sec = None
for line in open('runs/dva/tags.md', encoding='utf-8'):
    if line.startswith('## NTN'): sec = 'NTN'
    elif line.startswith('## NTX'): sec = 'NTX'
    m = re.match(r'\s*(\d+)\.\s*\**([DA])\b', line)
    if m and sec: tags[sec][int(m.group(1))] = m.group(2)

src = {
    'NTN': ('runs/pie/flagged.md', 'runs/pie/blind-class.md', 'runs/ntn/restate.py', 'runs/ntn/check.py'),
    'NTX': ('runs/ntx/laws.md', 'runs/ntx/blind-class.md', 'runs/ntx/restate.py', 'runs/ntx/check.py'),
}
rows = []
for lst, (lp, cp, rp, kp) in src.items():
    names, cls, rs, nota = listed(lp), classes(cp), load(rp), notation(kp)
    for n in sorted(tags[lst]):
        name, formula = names[n]
        if lst == 'NTX':  # drop the field note, e.g. "(analysis)", "(number theory; π(x) the prime count)"
            formula = re.sub(r'\s\((?=[a-z])[^()]*(?:\([^()]*\)[^()]*)*\)$', '', formula)
        L = rs.get(n, {})
        rows.append({'list': lst, 'n': n, 'name': name, 'formula': formula, 'tag': tags[lst][n], 'cls': cls.get(n),
                     'notation': n in nota, 'restated': L.get('restated') if n in nota else None,
                     'reason': L.get('reason')})
print(json.dumps(rows, ensure_ascii=False, indent=0))
