// ENG run 2: the stop and the order taken off the referee, in a copy of play-trick.html served here (plans/eng-plan.md)
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs';
let html = fs.readFileSync('play-trick.html', 'utf8');
const sub = (a, b) => { if (html.split(a).length !== 2) throw new Error('anchor: ' + a.slice(0, 60)); html = html.replace(a, b); };
sub('function pairs(B, log) {', `function pairs(B, log) {
        const V = window.__V; if (V.mode !== 'tog') return pairsSeq(B, log);
        const F = ['x', 'z', 'y', 'vx', 'vz', 'vy', 'wx', 'wy', 'wz'], S = B.map(b => ({ ...b })), dl = B.map(() => F.map(() => 0)), hits = B.map(() => 0);
        for (let i = 0; i < B.length; i++) for (let j = i + 1; j < B.length; j++) {
            const a = { ...S[i] }, c = { ...S[j] }; pairsSeq([a, c], log);
            let ch = false; F.forEach((f, k) => { const da = a[f] - S[i][f], dc = c[f] - S[j][f]; if (da || dc) ch = true; dl[i][k] += da; dl[j][k] += dc; });
            if (ch) { hits[i]++; hits[j]++; }
        }
        if (hits.some(n => n >= 2)) V.doubles++;
        B.forEach((b, i) => F.forEach((f, k) => { b[f] += dl[i][k]; }));
    }
    function pairsSeq(B, log) {`);
sub('for (let f = 0; f < 60 * 45 && moving(); f++)', 'for (let f = 0; f < 60 * 45 && (window.__V.stop === \'own\' || moving()); f++)');
sub('const B = B0.map(b => ({ y: 0, vy: 0, wx: 0, wy: 0, wz: 0, ...b }))', 'const B = (window.__V.rev ? B0.slice().reverse() : B0).map(b => ({ y: 0, vy: 0, wx: 0, wy: 0, wz: 0, ...b }))');
const srv = http.createServer((q, r) => { r.writeHead(200, { 'content-type': 'text/html' }); r.end(html); }).listen(0);
const b = await chromium.launch(); const p = await b.newPage();
await p.addInitScript(() => { window.__V = { mode: 'seq', stop: 'all', rev: false, doubles: 0 }; });
await p.goto(`http://localhost:${srv.address().port}/`); await p.waitForFunction(() => window.__trick);
const out = await p.evaluate(() => {
  const T = window.__trick, V = window.__V;
  let seed = 12345; const rnd = () => { seed = (seed * 1103515245 + 12345) >>> 0; return seed / 2 ** 32; };
  const fin = s => s.final.map(b => ({ n: b.n, x: b.x, z: b.z, sunk: b.sunk })).sort((a, c) => a.n - c.n);
  const play = (mode, stop, rev) => { Object.assign(V, { mode, stop, rev, doubles: 0 }); const s = T.preview(); const r = { fin: fin(s), doubles: V.doubles, contacts: s.contacts.length }; Object.assign(V, { mode: 'seq', stop: 'all', rev: false }); return r; };
  const shots = [];
  const one = label => shots.push({ label, base: play('seq', 'all', false), own: play('seq', 'own', false), tog: play('tog', 'all', false), revSeq: play('seq', 'all', true), revTog: play('tog', 'all', true) });
  for (const L of ['rack', 'scatter', 'line', 'jump', 'masse']) for (let i = 0; i < 9; i++) {
    T.setLayout(L); T.aim(-30 + 60 * rnd()); T.power(6 + 30 * rnd()); T.tip(0.5 * (rnd() - 0.5), 0.5 * (rnd() - 0.5)); T.elev(L === 'jump' || L === 'masse' ? 20 + 40 * rnd() : 0); one(L + i); }
  T.elev(0);
  const ch = [];
  for (const c of T.challenges) { T.setChallenge(c.id); T.solve(); one('ch:' + c.id);
    const res = {}; for (const [k, m, st] of [['base', 'seq', 'all'], ['own', 'seq', 'own'], ['tog', 'tog', 'all']]) { Object.assign(V, { mode: m, stop: st, rev: false }); res[k] = T.check(); }
    Object.assign(V, { mode: 'seq', stop: 'all', rev: false }); ch.push({ id: c.id, ...res }); }
  return { shots, ch };
});
await b.close(); srv.close();
const diff = (A, B) => { let m = 0; for (let i = 0; i < A.length; i++) { if (A[i].sunk !== B[i].sunk) return Infinity; if (!A[i].sunk) m = Math.max(m, Math.abs(A[i].x - B[i].x), Math.abs(A[i].z - B[i].z)); } return m; };
const L = []; const S = out.shots;
const v1 = S.filter(s => diff(s.base.fin, s.own.fin) !== 0), v1c = out.ch.filter(c => c.own !== null);
L.push(`shots ${S.length}`);
L.push(`V1: own stop differs on ${v1.length} shots (${v1.map(s => s.label + ' ' + diff(s.base.fin, s.own.fin)).join(', ') || 'none'}); challenges unsolved with it: ${v1c.map(c => c.id).join(', ') || 'none'}; base unsolved: ${out.ch.filter(c => c.base !== null).map(c => c.id).join(', ') || 'none'}`);
L.push(`  ${v1.length === 0 && v1c.length === 0 ? 'V1 not killed' : 'V1 KILLED'}`);
const single = S.filter(s => s.tog.doubles === 0), dbl = S.filter(s => s.tog.doubles > 0);
const v2 = single.filter(s => diff(s.base.fin, s.tog.fin) !== 0);
L.push(`V2: ${single.length} shots with no ball in two contacts in a substep; together differs on ${v2.length} (${v2.map(s => s.label + ' ' + diff(s.base.fin, s.tog.fin)).join(', ') || 'none'})`);
L.push(`  ${v2.length === 0 ? 'V2 not killed' : 'V2 KILLED'}`);
const solvedTog = out.ch.filter(c => c.tog === null).length;
L.push(`V3: together solves ${solvedTog} of ${out.ch.length} reference shots; unsolved: ${out.ch.filter(c => c.tog !== null).map(c => c.id + ' (' + c.tog + ')').join('; ') || 'none'}`);
L.push(`  measured: ${dbl.length} shots with a ball in two contacts in a substep (substeps: ${dbl.map(s => s.label + ':' + s.tog.doubles).join(' ')})`);
L.push(`  their outcomes moved (largest final place change, Infinity = a different pocket): ${dbl.map(s => s.label + ' ' + diff(s.base.fin, s.tog.fin).toExponential(2)).join(', ')}`);
L.push(`  ${solvedTog >= 13 ? 'V3 not killed' : 'V3 KILLED'}`);
const seqMoved = S.filter(s => diff(s.base.fin, s.revSeq.fin) > 1e-6), togKept = S.filter(s => diff(s.tog.fin, s.revTog.fin) <= 1e-9);
L.push(`V4: reversed order moves a final place > 1e-6 under the original rule on ${seqMoved.length} shots (${seqMoved.map(s => s.label).join(' ')}); under together, within 1e-9 on ${togKept.length} of ${S.length}`);
L.push(`  together reversed, largest change per shot: ${S.map(s => diff(s.tog.fin, s.revTog.fin)).map(x => x === 0 ? '0' : x.toExponential(1)).join(' ')}`);
L.push(`  ${seqMoved.length >= 1 && togKept.length >= 0.9 * S.length ? 'V4 not killed' : 'V4 KILLED'}`);
console.log(L.join('\n'));
