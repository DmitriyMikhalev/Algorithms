"""
The basic theorem of arithmetic says: any number is decomposed into the product
of prime factors in the only way, up to their permutation. For example:

The number 8 can be represented as 2 * 2 * 2.
The number 50 is like 2 * 5 * 5 (or 5 * 5 * 2, or 5 * 2 * 5). The three
variants differ only in the order of the multipliers.
The decomposition of a number into prime factors is called the factorization
of a number.

In a single line, the number N (2 <= N <= 10^9) is given, which needs to be
factorized.

Print in non-decreasing order the prime factors into which the number N is
decomposed.

-------------+-----------------+
Sample input | Sample output   |
8            | 2 2 2           |
-------------+-----------------+
13           | 13              |
-------------+-----------------+
100          | 2 2 5 5         |
-------------+-----------------+
45984        | 2 2 2 2 2 3 479 |
-------------+-----------------+
"""
import sys


def factorize(n: int) -> list[int]:
    """
    Get solution to the problem.
    Required params:
        n: int -- the number to factorize.
    Returns list[int] -- list with prime factors of the number.

    Algorithm:
    1. Create an empty array.
       Create divider variable (starts at 2 -- first prime number).

    If N == A * B and A < B, having found A we don't really need to test
    divide N by B. We know that it too divides N, because N/A == B implies
    N/B == A. So we only need to test while the potential factor A is less
    or equal (sqrt can be prime number) to the potential factor B.
    That is to say, until the square root of the number is reached.

    2. While divider <= sqrt(N), if current divider is true divider (remainder
    is equal to 0), append it to array and change N to N that divided by this.

    3. Append N value to array.
    Why we should to append N?
    For example, factorize 16. It's 2 * 2 * 2 * 2. Root is 4. Array is [].
    By steps:
        2 * 2 <= 16, 16 % 2 == 0 -- yes, [2],       N = 16 // 2 = 8
        2 * 2 <= 8, 8 % 2 == 0   -- yes, [2, 2],    N = 8 // 2 = 4
        2 * 2 <= 4, 4 % 2 == 0   -- yes, [2, 2, 2], N = 4 // 2 = 2
        2 * 2 <= 2 -- no, but we ignored the last divider. Add N = 2.

        Now array is [2, 2, 2, 2] and N is 2.

    For 25: it's 5 * 5, case with prime square root. Root is 5. Array is [].
    By steps:
        2 * 2 <= 25, 25 % 2 == 0 -- no, divider = 2 + 1 = 3
        3 * 3 <= 25, 25 % 3 == 0 -- no, divider = 3 + 1 = 4
        4 * 4 <= 25, 25 % 4 == 0 -- no, divider = 4 + 1 = 5
        5 * 5 <= 25, 25 % 5 == 0 -- yes, [5], N = 25 // 5 = 5
        5 * 5 <= 5 -- no, but we ignored the last divider. Add N = 5.

        Now array is [5, 5] and N is 5.
        That's why we should check dividers that less OR EQUAL to square root
        and ADD N to factors at the end of the algorithm.

    4. Return created array.
    """
    res = []
    divider = 2
    while divider * divider <= n:
        if n % divider == 0:
            res.append(divider)
            n //= divider
        else:
            divider += 1

    res.append(n)

    return res


def main() -> None:
    """
    The main function in which incoming data is read and transmitted to
    receive a solution to the problem into output.
    Returns None.
    """
    n = read_data()
    for prime in factorize(n):
        sys.stdout.write(str(prime) + ' ')


def read_data() -> int:
    """Read 1 line from stdin stream. Returns given integer."""
    return int(sys.stdin.readline())


if __name__ == '__main__':
    main()
