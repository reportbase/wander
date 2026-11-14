"""NTX step 4: check runs/ntx/restate.py (plans/ntx-plan.md); NTN's checker with the paths changed. A law counts as notation only if every pair agrees to
10^-30 and the restatement's text and its Python function carry no forbidden token. Run from the repository root."""
import importlib.util, inspect, re, sys
import mpmath as mp

mp.mp.dps = 50
spec = importlib.util.spec_from_file_location('restate', 'runs/ntx/restate.py')
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)
FORB = re.compile(r"π|Ω|\bpi\b|\be\b(?!\w)|\bexp|\bln\b|\blog|\bsin|\bcos|\btan|\bsec\b|\bcot|arctan|\batan|\basin|\bacos|"
                  r"\bsinh|\bcosh|\btanh|\bsech|\bgd\b|Γ|gamma\(|expj|mpf\('?2\.71|mp\.e\b")
pie = {}
for line in open('runs/ntx/blind-class.md', encoding='utf-8'):
    m = re.match(r'\s*(\d+)\.\s*\**\s*([ALX])\b', line)
    if m:
        pie[int(m.group(1))] = m.group(2)
notation, none, failed = [], [], []
for L in R.LAWS:
    n = L['n']
    if L['verdict'] != 'notation':
        none.append(n)
        continue
    # the names the restatement's own code uses (not its source line, which it shares with 'orig')
    bad_text = FORB.findall(L['restated'])
    BADN = {'pi', 'e', 'exp', 'expj', 'log', 'ln', 'sin', 'cos', 'tan', 'sec', 'cot', 'csc', 'atan', 'atan2', 'asin',
            'acos', 'sinh', 'cosh', 'tanh', 'sech', 'asinh', 'atanh', 'gamma', 'quad', 'nsum', 'nprod', 'limit', 'arg'}
    names, todo = set(), [L['new'].__code__]
    while todo:
        c = todo.pop(); names |= set(c.co_names); todo += [k for k in c.co_consts if hasattr(k, 'co_names')]
    bad_code = sorted(names & BADN)
    errs = []
    for x in L['points']:
        a, b = L['orig'](x), L['new'](x)
        a, b = (a, b) if isinstance(a, (list, tuple)) else ([a], [b])
        errs += [abs(mp.mpmathify(u) - mp.mpmathify(v)) for u, v in zip(a, b)]
    ok = max(errs) < mp.mpf(10) ** -30 and not bad_text and not bad_code and len(L['points']) >= 3
    (notation if ok else failed).append(n)
    if not ok:
        print(f'FAIL {n}: err {mp.nstr(max(errs), 3)}, text tokens {bad_text}, code tokens {bad_code}')
print(f'notation {len(notation)}, NONE {len(none)}, failed checks {len(failed)}')
print(f'listed {len(R.LAWS)}: notation share {len(notation)}/{len(R.LAWS)} = {len(notation)/len(R.LAWS):.3f}')
for c in 'ALX':
    mem = [n for n in pie if pie[n] == c]
    nt = sorted(set(mem) & set(notation))
    print(f'PIE class {c}: {len(nt)} of {len(mem)} notation: {nt}')
print('all notation:', sorted(notation))
