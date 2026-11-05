# Reads and writes in computing: a note

*Moved out of* Reads and Writes *on 3 November 2026 (SPN R641). Tom: "A machine is engineered to blur the distinction of
reading and writing. It does both. Move the computer sections into a note." The passages are kept below as they stood in
the paper, for reference; they predate R640 (a read is continuous, a write is a count) and R641, so where they call a
machine a reader, read it as a machine doing both.*

A machine counts: its numbers are finite, its memory laid out with a size, its operations steps. By R640 that is writing.
It also keeps to order, holds a direction as a pair [h : v] and composes without summing amounts, which is how a read
behaves; that is engineering made to serve both acts, as a cache, an index or a float's exponent is. So a machine is
neither a reader nor a writer: it is built to do both, and the line between them is where its designers put it.

## From §1, "Read and write in computing"

**Read and write in computing.** Computer science has used these words for longer, and the likeness is real. A computer's
read takes an address and returns what is stored there, changing nothing; that is this paper's split of address and
payload, met in hardware. A computer's write stores at an address a value that came from somewhere else; a write here
likewise needs an amount carried in from outside. But the two pairs part in five places.

- *Who lays out the addresses.* A computer's address space is laid out before anything is read: a known size, indices
  counted from 0 to N − 1, an end. That layout is a writer's work (an array whose `sizeof` is known is held by a writer).
  A reader's addresses are given by the turn, uniform by the turn's own measure, from home toward a horizon that is never
  reached; there is no N, no last address, and no end to fall off. What it holds is K, its own resolution, read
  continuously (§6, "K and N").
- *What a read returns.* A computer's read returns an amount in a unit: bytes, a float, a count. A read here returns a
  direction and the paint arriving along it, with every amount along that direction already gone. Nothing in it would
  change if the world were k times as large.
- *What a write changes.* A computer's write changes the memory, and the next read sees it. A write here states amounts
  (the room is 15 metres wide); it changes the world only when it is acted on, as moving the furniture is.
- *What stays the same.* A computer's read is repeatable: read the same address twice, with no write between, and the
  value is the same. A read here has a stronger sameness, across worlds: scale the world, and no reading moves.
- *Where caching falls.* In a computer, keeping a value read (a cache, a variable) is a write into another place. Here too:
  to keep a reading as a number, a length in a unit, a value in a table of known size, is to write it.

So the computing words are the writer's frame applied to both acts: memory is a written world, and a computer's read is
an address looked up in it. The read of this paper comes before any such layout; it is what a reader has when no one has
written the memory yet.

## From §2, after the capped mean

A machine's Cauchy, capped by its largest number, has one for the same reason.

## From §5, "A machine is a reader here"

**A machine is a reader here.** Every floating-point number is rational, an integer times a power of two. The machine's π
is 884279719003555/2⁴⁸, within 1.2·10⁻¹⁶ of π and not π. Every operation a machine does on numbers is monotone and finite, so
order statistics come out as the true ones rounded, and sums of amounts do not. Where the infinity is a horizon, kept as a
pair [h : v] or as a turn, and the computation keeps to order, the machine is faithful. Where it sits in a sum of amounts,
the machine's Cauchy, truncated, has a mean that the true one lacks.


## Why reads do not race (4 Nov 2026, SPN R658)

Tom: "the speculation is that is why geometry has no race conditions, it has a clean, free, non-algorithimic and a
clean seperation between reading and writing." A speculation, recorded as one.

Computing already has the precise form. Bernstein's conditions (1966): two operations may run in either order, or at
once, with the same result if neither writes what the other reads or writes. Pure reads always meet them; the PRAM
models say the same (concurrent reads allowed, only concurrent writes need a rule: CREW, concurrent read, exclusive
write). In the paper's terms:

- read with read: no race, ever. A read adds nothing to the paper (R653), so the order of two reads cannot matter; that
  is also why order between reads exists only once it is written (R652);
- read with write, write with write: where races live, a mark being made while something else reads or makes it;
- geometry: given whole and never written to (R458), so any number of reads of it commute. Being free and being
  race-free are one fact seen from two sides.

What makes geometry race-free is that nothing writes to it, not that it is scale-free: scale invariance sorts reading
from writing, immutability lets reads run together. A reading of a known result, no claim about physics: an actual
reading registers somewhere, and so writes (Bennett's point), which is where a physical race could come back.

## The projection is the dereference (5 Nov 2026, SPN R705)

A comparison from Gemini, pasted by Tom, recorded corrected (Tom: "Yes"). Kept: "the projection is the dereference". In
memory an address and its value share one representation, bits, and need a step between them (`*p`, a load); for the
reader the address is a direction and what reaches it is paint, two kinds with no arithmetic between them, and pointing
is already being met by what arrives (the first thing met the world's, the payload's).

| | Memory | The reader |
|---|---|---|
| Address | an integer in a layout of N slots (a writer's layout) | a direction [h : v], no length |
| What it reaches | a value, an amount in a unit | paint: what arrives, no length in it |
| Between them | an explicit dereference | none: pointing is the dereference |
| Races | where a write meets a read or a write on one place | none among reads; a payload write moves no address |

Corrected from the pasted text:

- its table gave the payload as V* and memory's as V, and the address as N: V* is a true breadth, an amount no read
  carries, not the payload; N is a count, not an address (keep the case, R226, R533);
- "the machine cannot tell them apart" holds for raw bits and untyped code, not for typed languages, tagged
  architectures or capability hardware (CHERI), which build the separation back;
- races come from concurrent writes to shared data whatever the representation; virtual memory is isolation and
  translation, not this. The paper's claim stays the narrower one (§1, "Reads do not conflict", R659–R661), a design
  argument, not a proof;
- "reading expends no cycles" is the geometry being given (R658); a machine does both acts (R641), so the cost of a
  dereference is a fact about machines, not a contest the geometry wins.

In essay 16 §1, "The projection is the dereference". Not in *Reads and Writes* (R641, R658).
