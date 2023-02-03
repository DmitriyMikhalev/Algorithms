"""Alla really liked the algorithm for calculating the polynomial hash. Help
her write a function that calculates the hash of the string s. In this task, it
is necessary to use their codes in the ASCII table as the values of individual
characters.

A polynomial hash is calculated by the formula:
h(S) = (S1 * a^(n-1) + S2 * a^(n-2) + ... + Sn-1 * a) mod m

Input format
In the first line, the number a (1 <= a <= 1000) is given -- the base by which
the hash is calculated.

The second line contains the number m (1 <= m <= 10^9) -- the module.

The third line contains the string s (0 <= |s| <= 10^6), consisting of large
and small Latin letters.

Output format
Output a non-negative integer -- the hash of the given string.

-------------+-----------------+
Sample input | Sample output   |
123          | 97              |
100003       |                 |
a            |                 |
-------------+-----------------+
123          | 6080            |
100003       |                 |
hash         |                 |
-------------+-----------------+
123          | 56156           |
100003       |                 |
HaSH         |                 |
-------------+-----------------+
"""
import sys


def hash(base: int, module: int, value: str) -> int:
    """
    Get solution to the problem.
    """
    if not value:
        return 0

    res = ord(value[0])
    for i in range(0, len(value) - 1):
        res = res * base + ord(value[i + 1])

    return res % module


def main() -> None:
    """
    The main function in which incoming data is read and transmitted to
    receive a solution to the problem into output.
    Returns None.
    """
    data = read_data()
    res = hash(*data)
    sys.stdout.write(str(res))


def read_data() -> tuple[int, int, str]:
    """
    Read 3 lines from stdin stream. Returns given values as tuple
    [int, int, str].
    """
    line_1 = int(sys.stdin.readline().strip())
    line_2 = int(sys.stdin.readline().strip())
    line_3 = sys.stdin.readline().strip()
    return line_1, line_2, line_3


if __name__ == '__main__':
    main()
