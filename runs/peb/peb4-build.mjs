// PEB run 4: build the event-driven copy from run 3's copy (runs/peb/play-trick-slope3.html), the original untouched.
import fs from 'fs';
let src = fs.readFileSync('runs/peb/play-trick-slope3.html', 'utf8');
const rep = (a, b) => { if (src.split(a).length !== 2) throw new Error('patch point: ' + a.slice(0, 60)); src = src.replace(a, b); };
rep('SUB = 4, HEAD', 'SUB0 = 4, HEAD');
rep("    const G = 154, E_TABLE = 0.5;", "    let SUB = SUB0;   // PEB run 4: the tick's substeps, set for Q1\n    const G = 154, E_TABLE = 0.5;");
rep('function pairs(B, log) {', 'function pairs(B, log, force) {');
rep('if (!(rr * rr > d2) || d2 === 0) continue;', 'if (!force && (!(rr * rr > d2) || d2 === 0)) continue;');
rep('if (!(ib.v + ia.v > 1)) continue;', 'if (!force && !(ib.v + ia.v > 1)) continue;');
rep('    window.__trick = {', fs.readFileSync('runs/peb/peb4-engine.js', 'utf8') + '    window.__trick = { simulateEvent, setSub: n => { SUB = n; },');
fs.writeFileSync('runs/peb/play-trick-event.html', src);
console.log('built');
