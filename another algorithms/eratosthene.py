"""
Get all prime numbers from 0 to N (include N).

The first line contains an integer N (0 <= N <= 10^9).

Print every prime number from [0, N].

-------------+---------------------------+
Sample input | Sample output             |
7            | 2 3 5 7                   |
-------------+---------------------------+
30           | 2 3 5 7 11 13 17 19 23 29 |
-------------+---------------------------+
1            |                           |
-------------+---------------------------+
"""
import sys


def eratosthene(n: int) -> list[int]:
    """
    Get solution to the problem.
    Required params:
        n: int -- the right border of the range.
    Returns list[int] -- list with prime numbers.

    Algorithm:
    1. Create array from 0 to N + 1, so index is equal to number, for example:
       arr[0] = 0
       arr[18] = 18
       arr[N] = N

    2. Replace 0 and 1 numbers to False, cause they're not prime.

    3. Bypass the given array by linear traversal:
       If current elemet isn't False, this element is prime number, and then
       mark every number that is a divisible of this as False (start from
       value^2 with step value). For example, if current array value is 7
       (not False), mark 49, 56, 63, 70, 77, ... as False.
       Don't think about numbers that less than value^2, they were marked using
       another values (for example with 7: 14 is marked from 2, 21 from 3, ..).

    4. Return new array excluding False values from previous array.
    """
    numbers = [i for i in range(0, n + 1)]
    numbers[0] = numbers[1] = False

    for num in range(1, n + 1):
        if numbers[num] is not False:
            for divisible in range(num * num, n + 1, num):
                numbers[divisible] = False

    return [prime for prime in numbers if prime is not False]


def main() -> None:
    """
    The main function in which incoming data is read and transmitted to
    receive a solution to the problem into output.
    Returns None.
    """
    n = read_data()
    for prime in eratosthene(n):
        sys.stdout.write(str(prime) + ' ')


def read_data() -> int:
    """Read 1 line from stdin stream. Returns given integer."""
    return int(sys.stdin.readline())


if __name__ == '__main__':
    main()
