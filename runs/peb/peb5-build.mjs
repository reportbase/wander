// PEB run 5: run 4's event copy with the full signature recorded (plans/peb-plan.md, run 5). The motion is run 4's;
// only what is recorded grows: each grip's choice, each phase end, each side spin's end. node runs/peb/peb5-build.mjs
import fs from 'fs';
let src = fs.readFileSync('runs/peb/play-trick-slope3.html', 'utf8'), eng = fs.readFileSync('runs/peb/peb4-engine.js', 'utf8');
const rep = (s, a, b, n = 1) => { if (s.split(a).length !== n + 1) throw new Error('patch point: ' + a.slice(0, 60)); return s.split(a).join(b); };
src = rep(src, 'SUB = 4, HEAD', 'SUB0 = 4, HEAD');
src = rep(src, "    const G = 154, E_TABLE = 0.5;", "    let SUB = SUB0;   // PEB run 4: the tick's substeps, set for Q1\n    const G = 154, E_TABLE = 0.5;");
src = rep(src, 'function pairs(B, log) {', 'function pairs(B, log, force) {');
src = rep(src, 'if (!(rr * rr > d2) || d2 === 0) continue;', 'if (!force && (!(rr * rr > d2) || d2 === 0)) continue;');
src = rep(src, 'if (!(ib.v + ia.v > 1)) continue;', 'if (!force && !(ib.v + ia.v > 1)) continue;');
// the ball grip's choice (stick 'B' or slip 'b'), recorded only while __br is an array
src = rep(src, 'J = Math.min((muB ?? gripOf(ss)) * Jn, ss / (k * im)),', 'J = (window.__br && window.__br.push((muB ?? gripOf(ss)) * Jn < ss / (k * im) ? "b" : "B"), Math.min((muB ?? gripOf(ss)) * Jn, ss / (k * im))),');
// the rail grip's choice, and side spin's end, in the event engine
eng = rep(eng, 'if (ss > 1e-12) { const Jt = Math.min(MU_C * Jn, 2 / 7 * ss),', 'if (ss > 1e-12) { window.__br.push(MU_C * Jn < 2 / 7 * ss ? "r" : "R"); const Jt = Math.min(MU_C * Jn, 2 / 7 * ss),');
eng = rep(eng, 'const d = MU_SP * dt / b.r; b.wy = Math.abs(b.wy) <= d ? 0', 'const d = MU_SP * dt / b.r; if (Math.abs(b.wy) <= d) window.__spin.push({ n: b.n, tc: Math.abs(b.wy) * b.r / MU_SP }); b.wy = Math.abs(b.wy) <= d ? 0', 2);
eng = rep(eng, '            B.forEach((b, i) => advance(b, M[i], dt,', '            window.__spin = [];\n            B.forEach((b, i) => advance(b, M[i], dt,');
eng = rep(eng, '            t += dt; events++;\n', '            window.__spin.sort((p, q) => p.tc - q.tc).forEach(s => ev.push({ key: "W" + s.n, g: 1 }));\n            t += dt; events++;\n');
eng = rep(eng, "phases.push({ t, n: b.n, ph: M[i].ph }); }); continue; }", "{ phases.push({ t, n: b.n, ph: M[i].ph }); ev.push({ key: (M[i].ph === 'slide' ? 'S' : 'R') + b.n, g: 1 }); } }); continue; }");
// pockets: g the radial share of the ball's speed as it enters
eng = rep(eng, "sunk.push({ n: b.n, pocket: e.p, t }); ev.push({ key: 'P' + b.n + '@' + e.p, g: 1 }); }", "sunk.push({ n: b.n, pocket: e.p, t }); const pk = POCKETS[e.p], P = [b.x - pk[0], b.z - pk[1]], V = [e.v[0], e.v[1]], pv = Math.hypot(...P) * Math.hypot(...V); ev.push({ key: 'P' + b.n + '@' + e.p, g: pv > 0 ? -(P[0] * V[0] + P[1] * V[1]) / pv : 1 }); }");
eng = rep(eng, "const b = B[e.i]; if (b.sunk) continue; b.sunk = true;", "const b = B[e.i]; if (b.sunk) continue; e.v = [b.vx, b.vz]; b.sunk = true;");
// contacts: the grips' choices in the key; g the least of the graze share and the closing speed over the shot's
eng = rep(eng, "                    pairs([a, c], null, true);\n", "                    window.__br = []; pairs([a, c], null, true); const brs = window.__br.join(''); window.__br = null;\n");
eng = rep(eng, "ev.push({ key: 'B' + B[e.i].n + '-' + B[e.j].n, g: wn / ws });", "ev.push({ key: 'B' + B[e.i].n + '-' + B[e.j].n + brs, g: Math.min(wn / ws, wn / power) });");
// cushions likewise; the rail's normal speed against the shot's
eng = rep(eng, "if (cushionOne(b, c, bb => cushions.push({ n: bb.n, t }))) ev.push({ key: 'C' + b.n + ':' + e.c, g: Math.abs(un) });", "window.__br = []; const vn0 = Math.abs(b.vx * c[0] + b.vz * c[1]); if (cushionOne(b, c, bb => cushions.push({ n: bb.n, t }))) ev.push({ key: 'C' + b.n + ':' + e.c + window.__br.join(''), g: Math.min(Math.abs(un), vn0 / power) }); window.__br = null;");
src = rep(src, '    window.__trick = {', eng + '    window.__trick = { simulateEvent, setSub: n => { SUB = n; },');
fs.writeFileSync('runs/peb/play-trick-event5.html', src);
console.log('built');
