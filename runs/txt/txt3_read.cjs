// TXT run 3, step 3: every slipped text read back; its distance from the figure and the share disturbed.
//   node runs/txt/txt3_read.cjs <draw dir> <forms3.json> <slips3.json> <dist3.json>
'use strict';
const fs = require('fs');
const L = require('./txt_lib.cjs');
const F = require('./txt3_formats.cjs');
const [drawDir, formsIn, slipsIn, out] = process.argv.slice(2);
const { tvf } = L.loadDraw(drawDir);
const P = Object.fromEntries(JSON.parse(fs.readFileSync(formsIn, 'utf8')).map(f => [f.key, f.P]));
const slips = JSON.parse(fs.readFileSync(slipsIn, 'utf8'));
const res = [];
for (const s of slips) {
    const r = { key: s.key, form: s.form, kind: s.kind, i: s.i, dist: null, share: null };
    let R = null;
    try { R = F.read(s.form, s.text, tvf); } catch (e) { R = null; }
    if (R && R.every(p => isFinite(p[0]) && isFinite(p[1]))) {
        const W = L.walk(R, Array.from({ length: 1024 }, (_, i) => i / 1024));
        const ref = P[s.key];
        const d = L.nearestAll(W, ref, true);
        let mx = 0, far = 0;
        for (const v of d) { if (v > mx) mx = v; if (v > 10) far++; }
        r.dist = Math.max(mx, L.directed(ref, W, true)) / 1000;
        r.share = far / d.length;
    }
    res.push(r);
}
fs.writeFileSync(out, JSON.stringify(res));
