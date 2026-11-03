// TXT step 3: read every slipped text back and measure how far it moved (plans/txt-plan.md).
//   node runs/txt/txt_read.cjs <draw dir> <forms.json> <slips.json> <dist.json>
'use strict';
const fs = require('fs');
const L = require('./txt_lib.cjs');
const [drawDir, formsIn, slipsIn, out] = process.argv.slice(2);
const { tvf } = L.loadDraw(drawDir);
const forms = JSON.parse(fs.readFileSync(formsIn, 'utf8'));
const P = Object.fromEntries(forms.map(f => [f.key, f.P]));
const slips = JSON.parse(fs.readFileSync(slipsIn, 'utf8'));
const res = [];
let n = 0;
for (const s of slips) {
    const ref = P[s.key];
    const d = R => (R ? L.hausdorff(ref, R) / 1000 : null);
    const r = { key: s.key, form: s.form, kind: s.kind, i: s.i };
    if (s.form === 'tvf') {
        const lenient = L.readTvf(s.text, false, tvf, 1024);
        r.dist = d(lenient);
        r.closed = !!lenient;
        r.strict = !!L.readTvf(s.text, true, tvf, 64);
    } else {
        r.dist = d(L.readSvg(s.text));
    }
    res.push(r);
    if (++n % 2000 === 0) process.stderr.write(n + '\n');
}
fs.writeFileSync(out, JSON.stringify(res));
