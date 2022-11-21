"""
Create function to get sum of 2 numbers in a given numeral system (<= 10).
Special case: test this function with binary system.

Two numbers in binary notation, each on a separate line. The length of each
number does not exceed 10^4 characters.

-------------+-----------------+
Sample input | Sample output   |
1010         | 10101           |
1011         |                 |
-------------+-----------------+
1            | 10              |
1            |                 |
-------------+-----------------+
1100         | 111011          |
101111       |                 |
-------------+-----------------+
"""
import sys


def main() -> None:
    """
    The main function in which incoming data is read and transmitted to
    receive a solution to the problem into output.
    Returns None.
    """
    a, b = read_data()
    for i in sum_numeral_sys(a=a, b=b):
        print(i, end='')


def read_data() -> tuple(str, str):
    """Read 2 lines from stdin stream. Returns given str values as tuple."""
    line_1 = sys.stdin.readline().strip()
    line_2 = sys.stdin.readline().strip()
    return line_1, line_2


def sum_numeral_sys(a: str, b: str, base: int = 2) -> list[int]:
    """
    Get solution to the problem.
    Required params:
        a: str -- first num.
        b: str -- second num.
    Optional params:
        base: int (by default is 2) -- base of numeral system.
    Returns list[int] -- list with sum of the numbers.

    Algorithm:
    1. Create an empty array for result num.
       Create 2 arrays with digits of numbers. If numbers have different count
       of digits smallest number is completing with insignificant zeros.
       Create overflow variable (at start is 0).

    2. Check that the numbers don't contain digits greater or equal to base.

    3. Bypass the given array by linear traversal from end to start:
       Sum digits and overflow at this index as 'value'.
       Set overflow to integer value of 'value' divided by base.
       Add the remainder of dividing 'value' by base

       For example, if base is 10: a = 19 [1, 9], b = 3 [3].
       By steps: numbers are [1, 9] and [0, 3], overflow is 0.
       value = 9 + 3 + 0 = 12
       overflow = 12 // 10 = 1 (will be transmitted to next digits)
       result = 12 % 10 = 2 (result of summing digits)

    4. If overflow is not 0, we need to add new digit at a result number.

    5. Reverse the created array (it was created from end to start) and return
       it.
    """
    res = []
    max_len = max(len(a), len(b))
    a = [int(i) for i in a.zfill(max_len)]
    b = [int(i) for i in b.zfill(max_len)]

    if any(i >= base for i in a) or any(i >= base for i in b):
        raise ValueError('Incorrect base: number has digit >= base!')

    overflow = 0
    for i in range(max_len - 1, -1, -1):
        digits_sum = overflow + a[i] + b[i]
        overflow = digits_sum // base
        res.append(digits_sum % base)

    if overflow:
        res.append(overflow)

    return res[::-1]


if __name__ == '__main__':
    main()
