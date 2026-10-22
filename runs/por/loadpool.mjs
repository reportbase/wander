// POR: load pool.html's script (read only) in node with a do-nothing DOM, and hand back window.__pool.
import fs from 'fs'; import vm from 'vm';
export function loadPool(file = 'pool.html') {
  const html = fs.readFileSync(file, 'utf8');
  const src = html.slice(html.lastIndexOf('<script>') + 8, html.lastIndexOf('</script>'));
  const fn = function () {};
  const any = new Proxy(fn, { get: (t, k) => k === Symbol.toPrimitive ? () => 0 : k === Symbol.iterator ? function* () {} : k === 'value' ? '0' : any,
                               set: () => true, apply: () => any, construct: () => any });
  const win = { document: { getElementById: () => any, querySelector: () => any, createElement: () => any },
    addEventListener() {}, requestAnimationFrame() {}, location: { search: '' }, devicePixelRatio: 1, getComputedStyle: () => any };
  win.window = win;
  const ctx = vm.createContext({ ...win, window: win, URLSearchParams, Math, console });
  vm.runInContext(src, ctx);
  return win.__pool;
}
