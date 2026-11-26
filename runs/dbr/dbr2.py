"""DBR run 2: D2' at K = 48. Run from the repository's root."""
src = open('runs/dbr/dbr.py').read().split("CENTRES = [")[0]
g = {}; exec(src, g)
CENTRES = [1e1, 1e3, 1e6, 1e9, 1e12]
out, errs, ok = [], [], True
for c in CENTRES:
    g['TRIG']['n'] = 0; g['counting'](True)
    e, el, terms, nl = g['l2_window'](c, 4.0, 48, g['f_ratio'])
    calls = g['TRIG']['n']; g['counting'](False)
    errs.append(e); ok &= terms == 48 and calls == 0
    out.append(f'c = {c:.0e}: sup error {e:.2e}  terms {terms}  trig calls {calls}')
ok &= max(errs) <= 1e-6 and max(errs) / min(errs) <= 2
out.append("D2' " + ('not killed' if ok else 'KILLED') + ' (largest / smallest %.2f)' % (max(errs) / min(errs)))
print('\n'.join(out)); open('runs/dbr/dbr-run2.txt', 'w').write('\n'.join(out) + '\n')
