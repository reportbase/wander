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

