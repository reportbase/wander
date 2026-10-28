// The reader's situation recreated in code (essay 12 §6, SPN R573). Run from the repo root: node runs/arr/reader.mjs
const colourOf = i => `c${(i*2654435761>>>0)%997}`;
function* world(n=Infinity, scale=1, paintOf=colourOf){ for(let i=0;i<n;i++) yield {pos:i*scale, paint:paintOf(i)}; }
class Reader{ constructor(K){this.K=K;this.paint=new Array(K).fill(null);} receive(s,p){ if(this.paint[s]===null)this.paint[s]=p; } }
function deliver(w,r,H){ let n=0; for(const {pos,paint} of w){ n++; const s=Math.floor(r.K*(2/Math.PI)*Math.atan2(pos,H)); r.receive(s,paint); if(s===r.K-1)break;} return n; }
const K=32,H=10;
const run=(w,h=H)=>{const r=new Reader(K);const n=deliver(w,r,h);return {r,n};};
const a=run(world(1e6)), b=run(world(2e6)), c=run(world());
console.log('elements read', a.n, b.n, c.n, 'same', JSON.stringify(a.r.paint)===JSON.stringify(b.r.paint) && JSON.stringify(a.r.paint)===JSON.stringify(c.r.paint));
const d=run(world(Infinity,7),H*7); console.log('scaled same', JSON.stringify(d.r.paint)===JSON.stringify(c.r.paint));
const e=run(world(),H*4); console.log('H changed differs', JSON.stringify(e.r.paint)!==JSON.stringify(c.r.paint));
const f=run(world(Infinity,1,i=>'x'+i)); console.log('slots painted', f.r.paint.filter(p=>p).length, 'of', K);
const g=run(world(100)); const last=g.r.paint.findLastIndex(p=>p!==null); console.log('finite N=100: paint stops at slot', last, 'reading N/H in', Math.tan(last*Math.PI/2/K), Math.tan((last+1)*Math.PI/2/K));
// empty slots in near field? count nulls in c
console.log('empty slots endless', c.r.paint.filter(p=>p===null).length);
