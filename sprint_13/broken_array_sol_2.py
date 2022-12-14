"""
Also see solution #1: recursive quick-sort and binary search that equals to
O(n*log(n) + log(n)) <-> O(log(n)*(n + 1)) <-> O(n*log(n)).

Alla made a mistake when copying from one data structure to another. It stored
an array of numbers in a ring buffer. The array was sorted in ascending order,
and an element could be found in it in logarithmic time. Alla copied the data
from the ring buffer into a regular array, but shifted the data of the original
sorted sequence. Now the array is not sorted. Nevertheless, it is necessary to
provide the ability to find an element in it for O(log(n)).
It can be assumed that there are only unique elements in the array.

Input format
The function takes an array of natural numbers and the desired number k. The
length of the array does not exceed 10^4. The array elements and the number k
do not exceed 10^4 in value.

In the examples:
The first line contains the number n -- the length of the array. The second
line contains a positive number k is the desired element.
Next, n natural numbers are written into the string separated by a space – the
elements of the array.

Output format
The function should return the index of an element equal to k, if there is one
in the array (numbering from zero). If the element is not found, the function
should return -1. The array cannot be changed.
To cut off inefficient solutions, your function will run from 10^5 to 10^6
times.

>>> broken_search([9, 0, 1], 8)
-1

>>> broken_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0], 1)
0

>>> broken_search([19, 21, 100, 101, 1, 4, 5, 7, 12], 5)
6

>>> broken_search([5, 1], 1)
1

>>> broken_search([], 0)
-1

>>> broken_search([8, 10, 0, 2, 4], 4)
4
"""
from typing import Any, List


def broken_search(array: List[Any], target: Any) -> int:
    """
    Get index of element. Complexity: O(log(n)).
    Required params:
        - array: List[Any], array of any type you can compare using 2 objects.
        - target: Any, target whose index is searching.
        Note, that target and any arrays' element should by equal types.

    Returns int index of element searching for (-1 if it doesn't exist).

    [19, 21, 100, 101, 1, 4, 5, 7, 12]
     |______________|  |____________|
            |                 |
        right NBA         left NBA
        (left BA)        (right BA)

    [1, 4, 5, 7, 12, 19, 21, 100, 101]
     |____________|  |______________|
           |                |
        left NBA        right NBA
    """
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if array[mid_index] == target:
            return mid_index
        # Left part of not broken array (NBA).
        elif array[left_index] > array[mid_index]:
            # Target at this part of NBA, cut off left part of BA.
            if array[mid_index] < target <= array[right_index]:
                left_index = mid_index + 1
            # Target is not at this part of NBA, cut off right part of BA.
            else:
                right_index = mid_index - 1
        # Right part of NBA.
        else:
            # Target at this part of NBA, cut off right part of BA.
            if array[left_index] <= target < array[mid_index]:
                right_index = mid_index - 1
            # Target is not at this part of NBA, cut off left part of BA.
            else:
                left_index = mid_index + 1

    return -1


def main() -> None:
    assert broken_search([19, 21, 100, 101, 1, 4, 5, 7, 12], 5) == 6
    print('It\'s working.')


if __name__ == '__main__':
    main()
