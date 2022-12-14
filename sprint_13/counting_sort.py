"""
Rita decided to keep her clothes in only three colors: pink, yellow and
crimson. After things of other colors were removed, Rita wanted to sort her new
wardrobe by colors. First things should go pink, then yellow, and at the end
- crimson. Help Rita cope with this task.

Note: try to solve the problem in one pass through the array!

The first line specifies the number of items in the wardrobe: n -- it does not
exceed 10^6. In the second line, an array is given in which the color for
each item is specified. Pink color is indicated by 0, yellow - 1, crimson - 2.

It is necessary to print the colors of objects in the correct order in a line
separated by a space.

>>> counting_sort([0, 2, 1, 2, 0, 0, 1], 3)
['0', '0', '0', '1', '1', '2', '2']

>>> counting_sort([2, 1, 2, 0, 1], 3)
['0', '1', '1', '2', '2']

>>> counting_sort([2, 1, 1, 2, 0, 2], 3)
['0', '1', '1', '2', '2', '2']
"""
import sys
from typing import List, Optional, Tuple


def counting_sort(array: List[int], range_values: int) -> List[str]:
    """O(N + K) time complexity and O(K) space complexity."""
    values = [0] * range_values
    for elem in array:
        values[elem] += 1

    res = []
    for i in range(len(values)):
        elem = values[i]
        while elem:
            res.append(str(i))
            elem -= 1

    return res


def input_data(stream=sys.stdin) -> Optional[Tuple[int, List[List[str]]]]:
    """
    Read data from the given stream (by default is sys.stdin).
    Returns array of ints or None if array is empty.
    """
    if isinstance(stream, str):
        stream = open(encoding='utf-8', file=stream, mode='r')

    size = int(stream.readline())
    if not size:
        return None

    return [int(i) for i in sys.stdin.readline().strip().split(' ')]


def main() -> None:
    range_values = 3
    array = input_data()
    if array is None:
        return
    res = counting_sort(array, range_values)
    sys.stdout.write(' '.join(res))


def output_data(data, stream=sys.stdout) -> None:
    """
    Write data into given stream (by default is sys.stdout).
    Required params: data -- str, data to be written.
    Returns None.
    """
    if isinstance(stream, str):
        stream = open(encoding='utf-8', file=stream, mode='w')

    stream.write(data)


if __name__ == '__main__':
    main()
