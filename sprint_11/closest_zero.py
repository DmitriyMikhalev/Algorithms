"""
The first line contains the length of the street -- N (1 <= N <= 10^6).
The next line contains N non—negative integers - house numbers and designations
of empty areas on the map (zeros). It is guaranteed that there is at least one
zero in the sequence. House numbers (positive numbers) are unique and do not
exceed 10^9.

For each of the sections, print the distance to the nearest zero. Print the
numbers in one line, separating them with spaces.

-------------+---------------+
Sample input | Sample output |
5            | 0 1 2 1 0     |
0 1 4 9 0    |               |
-------------+---------------+
6            | 0 1 2 3 4 5   |
0 7 9 4 8 20 |               |
-------------+---------------+
"""
import sys


def get_zero_range(arr: list[int], size: int) -> list[int]:
    """
    Get solution to the problem.
    Required params:
        arr: list[int] -- list of ints (area's number, has at least one 0)
        size: int -- size of list
    Returns a new list (given arr wasn't changed) of ints as the problem's
    solution.

    Algorithm:
    1. Create a new array of 0 with the same size.

    2. Create pointers to the left and right zero indexes. Both of them
       are always defined (array has at least one 0). At start they have equal
       value - first 0 index at array.

    3. Bypass the given array by linear traversal:
       If value is 0, left pointer is moving to this index and right pointer
       is moving right to the first 0 value (and then cycle stops) or
       to the end of array (out of values), then right pointer sets to None.

       Else if value isn't 0, and right pointer isn't None, the result value at
       this index sets to minimum of the modules of the difference between the
       current index and the left and right pointers (distance to the near 0).

       Else (value is not 0, right pointer is None) the last 0 at array (the
       closest one to all next values) is behind the current index, so result
       value at this index sets to difference between this index and left
       pointer.

    4. Return new array.
    """
    res = [0] * size
    right_zero_index = left_zero_index = arr.index(0)

    for i in range(0, size):
        if arr[i] == 0:
            left_zero_index = i
            while True:
                right_zero_index += 1
                if right_zero_index == size:
                    right_zero_index = None
                    break
                elif arr[right_zero_index] == 0:
                    break
        elif right_zero_index is not None:
            res[i] = min(abs(i - left_zero_index), abs(right_zero_index - i))
        else:
            res[i] = i - left_zero_index

    return res


def main() -> None:
    """
    The main function in which incoming data is read and transmitted to
    receive a solution to the problem into output.
    Returns None.
    """
    args: tuple[list[int], int] = read_data()
    sys.stdout.write(
        ' '.join([str(elem) for elem in get_zero_range(*args)])
    )


def read_data() -> tuple[list[int], int]:
    """
    Read data from stdin stream.
    Returns a tuple with array of ints and its' size, for example ([-1, 4], 2).
    """
    size = int(sys.stdin.readline())
    arr = [int(elem) for elem in sys.stdin.readline().split(' ')]

    return arr, size


if __name__ == '__main__':
    main()
