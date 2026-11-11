# Fifteen constructions (answers withheld)

Each result is written as "= C" or "→ C". The constants are in `answers.md`; the checks in `check.py`.

1. **Two points in a square tile** (geometry). Two points are chosen independently and uniformly by area inside a square of side 1 in the plane. Their straight-line distance is averaged over all pairs (a four-dimensional integral, reducible to two dimensions over the coordinate differences). The mean distance = C.

2. **Nobody gets their own hat** (combinatorics). Count the permutations of n objects in which no object stays in its own place (by inclusion and exclusion over the sets of objects that do stay), and divide by the number of all permutations of n objects. Take n to infinity. The proportion → C.

3. **Two points in a round plate** (geometry). Two points are chosen independently and uniformly by area inside a disc of radius 1 in the plane. Their straight-line distance is averaged over all pairs, a four-dimensional integral over the two positions. The mean distance = C.

4. **The imaginary unit raised to itself** (analysis). Take the imaginary unit i, a quarter turn on the unit circle in the complex plane, and raise it to the power i, using the principal branch of the complex logarithm (the logarithm of i being the integral of dz/z along a path from 1 to i that does not cross the negative real axis). The result is a real number, = C.

5. **An endless ladder of resistors** (physics). A ladder network is built from identical 1-ohm resistors: each section has one resistor in series along the top rail followed by one resistor across the rails, and the sections repeat without end. Adding one more section to the front of an infinite ladder leaves it unchanged, which gives a self-consistency equation for the resistance seen at the input terminals. That input resistance, in ohms, = C.

6. **A product of two logarithms** (analysis). On the unit interval take the natural logarithm of x and the natural logarithm of 1 − x and multiply them. Integrate the product over x from 0 to 1 (one dimension; both endpoints are integrable singularities). The integral = C.

7. **Cubes over factorials** (analysis). Sum the terms n³/n! over all integers n from 0 to infinity (a one-dimensional series, each term a cube divided by a factorial). Equivalently, the third moment of a count of independent rare events whose mean count is 1, multiplied by the reciprocal of the probability of no event. The sum = C.

8. **Growth of continued-fraction denominators** (dynamics / number theory). Expand a real number x in (0, 1) as a continued fraction and let q_n be the denominator of its n-th convergent. For almost every x (with respect to length), the n-th root of q_n tends to one and the same limit, obtained as an average of −ln x over the invariant density 1/((1 + x) ln 2) of the map x ↦ fractional part of 1/x, then undoing the logarithm. That limit → C.

9. **Integers with no repeated prime factor** (number theory). Count the positive integers up to N that are divisible by no perfect square other than 1, and divide by N. Equivalently, for each prime p independently discard the integers divisible by p², and multiply the surviving proportions over all primes. Take N to infinity. The limiting proportion → C.

10. **An inverse tangent over its argument** (analysis). For x between 0 and 1 take the angle whose tangent is x (in radians) and divide it by x. Integrate over x from 0 to 1 (one dimension). Equivalently, integrate term by term the series for the inverse tangent, giving an alternating sum over the odd numbers of their inverse squares. The integral = C.

11. **Where an infinite tower of powers stops settling** (dynamics). For a base a between 0 and 1, iterate the map x ↦ aˣ starting from x = 1 (the tower a, a^a, a^(a^a), …). For a close to 1 the iterates settle on a fixed point; for small a they fall into a cycle of period two. The change happens where the fixed point's multiplier reaches −1. The smallest base for which the tower still converges = C.

12. **A cosine under a rational weight** (analysis). Integrate cos x divided by (1 + x²) over the whole real line, x from −∞ to +∞ (one dimension). The integrand oscillates with period fixed by the cosine and decays as 1/x²; the standard derivation closes the contour in the upper half-plane around the single pole there. The integral = C.

13. **Total of a thermal spectrum** (physics). A cavity in thermal equilibrium emits radiation whose energy per unit frequency is the cube of the frequency times the Bose occupation factor, 1/(exponential of the scaled frequency, minus 1). In the dimensionless variable x (frequency scaled by temperature) one integrates x³/(exponential of x, minus 1) over x from 0 to infinity. This one-dimensional integral, the dimensionless factor in the total radiated power, = C.

14. **Time spent in the lead** (probability). A fair coin is tossed 2n times and a running score goes up or down by 1 at each toss. Record the fraction of the time the score is on the positive side. As n goes to infinity this fraction has a limiting distribution on [0, 1] that piles up at both ends. The limiting probability that the fraction is at most one quarter → C.

15. **Draws until the total passes one** (probability). Independent numbers are drawn uniformly from the interval [0, 1] and added up one at a time. Stop at the first draw at which the running total exceeds 1, and record how many draws were made. The probability that n draws have not yet passed 1 is the volume of the corner simplex of the n-dimensional unit cube. The expected number of draws = C.

