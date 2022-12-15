"""
===============================================================================

Timofey decided to organize a sports programming competition to find talented
interns. Tasks are selected, participants are registered, tests are written. It
remains to figure out how the winner will be determined at the end of the
competition.

Each participant has a unique login. When the competition ends, two indicators
will be linked to it: the number of solved tasks Pi and the amount of the fine
Fi. The penalty is charged for unsuccessful attempts and the time spent on the
task.

Timofey decided to sort the results table as follows: when comparing two
participants, the one with more tasks solved will go higher. If the number of
solved problems is equal, the participant with the lesser penalty goes first.
If the penalties also match, then the first one will be the one whose login
goes earlier in alphabetical (lexicographic) order.

Timofey ordered hoodies for the winners and went to the store for them the day
before. In his absence, he instructed you to implement a quick sort algorithm
for the results table. Since Timofey loves sports programming and does not like
to waste RAM, your sorting implementation cannot consume O(n) additional memory
for intermediate data (such a modification of quick sorting is called
"in-place").

===============================================================================

Input format
The first line contains the number of participants n, 1 <= n <= 10^5. Each of
the following n lines contains information about one of the participants the
i-th participant is described by three parameters:

    * a unique login (a string of small Latin letters no longer than 20)
    * the number of solved problems Pi
    * the penalty Fi.

Fi and Pi are integers ranging from 0 to 10^9.

Output format
For a sorted list of participants, output their logins in order, one per line.

----------------+---------------+
Sample input    | Sample output |
5               | gena          |
alla 4 100      | timofey       |
gena 6 1000     | alla          |
gosha 2 90      | gosha         |
rita 2 90       | rita          |
timofey 4 80    |               |
----------------+---------------+
5               | alla          |
alla 0 0        | gena          |
gena 0 0        | gosha         |
gosha 0 0       | rita          |
rita 0 0        | timofey       |
timofey 0 0     |               |
----------------+---------------+

===============================================================================

Algorithm:
    1. Prepare data as [-tasks, negative_scores, login]. Why is the first
       element negative it is said further.
    2. Sort data using acsedning order. [TASKS, SCORES, LOGIN] is definition of
       the person. Persons logins and scores are sorting in ascending order.
       In contrast to this, persons with different tasks are sorting in
       decsending order, so key to sort an array is [d, a, a]. To sort persons
       correct, we have to change all orders to equal - the simpliest way is to
       change tasks count using negative value (it will be [a, a, a]).
    3. Output the data.

===============================================================================
"""

import random
import sys
from typing import List, Optional, Tuple

TASKS = 0
NEGATIVE_POINTS = 1
LOGIN = 2


def input_data(stream=sys.stdin) -> List[Tuple[int, int, str]]:
    """
    Read data from the given stream (by default is sys.stdin).
    Returns list of tuples.
    """
    if isinstance(stream, str):
        stream = open(encoding='utf-8', file=stream, mode='r')

    persons_count = int(stream.readline())
    persons = []
    for _ in range(persons_count):
        line: List[str] = stream.readline().strip().split(' ')
        line = (
            -1 * int(line[1]),
            int(line[2]),
            line[0]
        )
        persons.append(line)
    stream.close()

    return persons


def main() -> None:
    """
    The main function in which incoming data is read and transmitted to
    receive a solution to the problem into output.
    Returns None.
    """
    persons: List[Tuple[int, int, str]] = input_data()
    quick_sort(
        array=persons,
        key=lambda x: (x[TASKS], x[NEGATIVE_POINTS], x[LOGIN])
    )
    output_data(data=persons)


def output_data(data, stream=sys.stdout) -> None:
    """
    Write data into given stream (by default is sys.stdout).
    Required params: data -- list[tuples()], data to be written.
    Returns None.
    """
    if isinstance(stream, str):
        stream = open(encoding='utf-8', file=stream, mode='w')

    for i in data:
        stream.write(i[LOGIN] + '\n')


def quick_sort(
    array: List,
    left: Optional[int] = None,
    right: Optional[int] = None,
    *,
    desc: bool = False,
    key=lambda x: x
) -> None:
    """
    Quick sort an array (see wikipedia.org/wiki/Quicksort). Returns None.
    Note, that this function is changing given array.
    Time complexity:
        - O(n*log(n)) - best
        - O(n*log(n)) - average
        - O(n*n) - worst

    Space complexity:
        - O(1)

    Required params:
        - array: List, array to be sorted.

    Optional params:
        - left: int, index of start of array (by default is None).
        - right: int, index of end of array (by default is None).
        - (named) desc: bool, descending order? (by default is False.)
        - (named) key: Callable, key-function to define comparable part of
          object if that's not comparable type by default.

    """
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    if left >= right:
        return

    i, j = left, right
    pivot_index = random.randint(i, j)
    pivot_key = key(array[pivot_index])

    while i <= j:
        if desc:
            while key(array[i]) > pivot_key:
                i += 1
            while key(array[j]) < pivot_key:
                j -= 1
        else:
            while key(array[i]) < pivot_key:
                i += 1
            while key(array[j]) > pivot_key:
                j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    quick_sort(array=array, left=left, right=j, desc=desc, key=key)
    quick_sort(array=array, left=i, right=right, desc=desc, key=key)


if __name__ == '__main__':
    main()
