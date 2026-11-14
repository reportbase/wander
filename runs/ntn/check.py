"""NTN step 2: check runs/ntn/restate.py (plans/ntn-plan.md). A law counts as notation only if every pair agrees to
10^-30 and the restatement's text and its Python function carry no forbidden token. Run from the repository root."""
import importlib.util, inspect, re, sys
import mpmath as mp

mp.mp.dps = 50
spec = importlib.util.spec_from_file_location('restate', 'runs/ntn/restate.py')
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)
FORB = re.compile(r"π|Ω|\bpi\b|\be\b(?!\w)|\bexp|\bln\b|\blog|\bsin|\bcos|\btan|\bsec\b|\bcot|arctan|\batan|\basin|\bacos|"
                  r"\bsinh|\bcosh|\btanh|\bsech|\bgd\b|Γ|gamma\(|expj|mpf\('?2\.71|mp\.e\b")
pie = {}
for line in open('runs/pie/blind-class.md', encoding='utf-8'):
    m = re.match(r'\s*(\d+)\.\s*([ALX])', line)
    if m:
        pie[int(m.group(1))] = m.group(2)
notation, none, failed = [], [], []
for L in R.LAWS:
    n = L['n']
    if L['verdict'] != 'notation':
        none.append(n)
        continue
    try:
        src = inspect.getsource(L['new'])
    except (OSError, TypeError):
        src = ''
    # the 'new' source: only the lambda or def body after its name
    body = src.split(':', 1)[1] if ':' in src else src
    bad_text = FORB.findall(L['restated'])
    bad_code = [t for t in FORB.findall(body) if t not in ('e',)]  # a bare e as a variable name is allowed in code
    errs = []
    for x in L['points']:
        a, b = L['orig'](x), L['new'](x)
        errs.append(abs(mp.mpmathify(a) - mp.mpmathify(b)))
    ok = max(errs) < mp.mpf(10) ** -30 and not bad_text and not bad_code and len(L['points']) >= 3
    (notation if ok else failed).append(n)
    if not ok:
        print(f'FAIL {n}: err {mp.nstr(max(errs), 3)}, text tokens {bad_text}, code tokens {bad_code}')
print(f'notation {len(notation)}, NONE {len(none)}, failed checks {len(failed)}')
grp = {'proj+id': [21, 34, 35, 48, 53, 58, 61, 88, 80, 93, 108], 'holonomy+Kepler': [89, 90, 92, 102, 83]}
for k, v in grp.items():
    print(f'{k}: notation {sorted(set(v) & set(notation))} ({len(set(v) & set(notation))} of {len(v)})')
for c in 'AL':
    mem = [n for n in pie if pie[n] == c]
    nt = sorted(set(mem) & set(notation))
    print(f'PIE class {c}: {len(nt)} of {len(mem)} notation: {nt}')
print('all notation:', sorted(notation))
