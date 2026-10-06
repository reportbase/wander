"""Turn Chan and Mazzocco's OSF file (osf.io/kqe2w, NLE_OSF_Public.xlsx) into the trial CSVs nle.py reads, following
plans/nle-plan.md's section for this dataset (fixed before the data was seen):
    one CSV per time (pre, post) and line (100, 20), the line's two kinds (with and without the labelled midpoint)
    pooled, targets past the line's end left out.

    python3 plans/nle/chan_mazzocco.py NLE_OSF_Public.xlsx OUTDIR
    python3 plans/nle/nle.py OUTDIR/pre_100.csv --max 100      # the run that carries the kill
"""
import csv
import os
import re
import sys

import openpyxl

COL = re.compile(r'^(Pre|Post)_NLE(20|100)m?_Est_(\d+)$')


def main(xlsx, outdir):
    ws = openpyxl.load_workbook(xlsx, read_only=True, data_only=True)['NLE_OSF_Clean']
    rows = ws.iter_rows(values_only=True)
    head = list(next(rows))
    cols = []
    for i, name in enumerate(head):
        m = COL.match(str(name or ''))
        if m:
            time, line, target = m.group(1).lower(), int(m.group(2)), int(m.group(3))
            if target <= line:
                cols.append((i, time, line, target))
    os.makedirs(outdir, exist_ok=True)
    out = {}
    for row in rows:
        pid = row[head.index('Subject.ID')]
        if pid is None:
            continue
        for i, time, line, target in cols:
            v = row[i]
            if isinstance(v, (int, float)):
                out.setdefault((time, line), []).append((pid, target, v))
    for (time, line), trials in sorted(out.items()):
        path = os.path.join(outdir, f'{time}_{line}.csv')
        with open(path, 'w', newline='') as fh:
            w = csv.writer(fh)
            w.writerow(['participant', 'target', 'estimate'])
            w.writerows(trials)
        print(f'{path}: {len(trials)} trials, {len({t[0] for t in trials})} children')


if __name__ == '__main__':
    main(*sys.argv[1:3])
