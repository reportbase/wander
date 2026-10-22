// POR: load pool.html's script (read only; the file is never written) into node with a do-nothing DOM, and hand back
// window.__pool, with stepRef, stepSit and the constants exposed. With k ≠ 1 the in-memory copy has every length and
// every speed multiplied by k (table, radii, pockets, the rack's and the field's gaps, the strike, the cloth's
// deceleration); the clock (FRAME, SUB) is untouched.
import fs from 'fs'; import vm from 'vm';
export function loadPool(k = 1, file = 'pool.html') {
  const html = fs.readFileSync(file, 'utf8');
  let src = html.slice(html.lastIndexOf('<script>') + 8, html.lastIndexOf('</script>'));
  const rep = (a, b) => { if (!src.includes(a)) throw new Error('not found: ' + a); src = src.split(a).join(b); };
  if (k !== 1) {
    const K = `(${k})`;
    rep('const LX = 20, LZ = 10, R0 = 0.45, R_HEAVY = 0.6, POCK = 0.85, MU = 0.6,',
        `const LX = 20*${K}, LZ = 10*${K}, R0 = 0.45*${K}, R_HEAVY = 0.6*${K}, POCK = 0.85*${K}, MU = 0.6*${K},`);
    rep('SPEED = 14', `SPEED = 14*${K}`);
    rep('2 * R_HEAVY + 0.02', `2 * R_HEAVY + 0.02*${K}`);
    rep('[0, -LZ / 2 - 0.2]', `[0, -LZ / 2 - 0.2*${K}]`);
    rep('[0, LZ / 2 + 0.2]', `[0, LZ / 2 + 0.2*${K}]`);
    rep('b.r + r + 0.02', `b.r + r + 0.02*${K}`);
  }
  rep('window.__pool = {', 'window.__pool = { stepRef, stepSit, FRAME, LX, ');
  const fn = function () {};
  const any = new Proxy(fn, { get: (t, p) => p === Symbol.toPrimitive ? () => 0 : p === Symbol.iterator ? function* () {} : p === 'value' ? '0' : any,
                               set: () => true, apply: () => any, construct: () => any });
  const win = { document: { getElementById: () => any, querySelector: () => any, createElement: () => any },
    addEventListener() {}, requestAnimationFrame() {}, location: { search: '' }, devicePixelRatio: 1, getComputedStyle: () => any };
  win.window = win;
  vm.runInContext(src, vm.createContext({ ...win, window: win, URLSearchParams, Math, console }));
  return win.__pool;
}
