"""
The game "Simulator for high-speed printing" is a field of 4x4 keys. In it,
a configuration of numbers and dots appears on each round. Either a dot or
a number from 1 to 9 is written on the key.

At time T, the player must simultaneously press all the keys on which the
number T is written. Gosha and Timofey can press K keys each at one time.
If all the necessary keys are pressed at time T, then the players receive
1 point.

Find the number of points that Gosha and Timofey can earn if they press
the keys together.

The first line contains an integer K (1 <= K <= 5).
The next 4 lines specify the type of simulator -- 4 characters in each line.
Each character is either a dot or a digit. The characters of one
line are consecutive and are not separated by spaces.

Print a single number - the maximum number of points that 2 players can score.

-------------+---------------+
Sample input | Sample output |
3            | 2             |
1231         |               |
2..2         |               |
2..2         |               |
2..2         |               |
-------------+---------------+
4            | 1             |
1111         |               |
9999         |               |
1111         |               |
9911         |               |
-------------+---------------+
4            | 0             |
1111         |               |
1111         |               |
1111         |               |
1111         |               |
-------------+---------------+

*You have to get count of digits which less or equal to 2 * K - for example,
players can't press 13 times '4' button if they have 8 'fingers' together at
T = 4 moment.
"""
import sys


def get_scores(field: str, fingers_count: int) -> int:
    """
    Get solution to the problem.
    Required params:
        field: str -- string of field (concatenated lines)
        fingers_count: int -- count of buttons that can be pushed
    Returns scores -- integer.

    Algorithm:
    1. If count of digit at field is less or equal to fingers_count players
       can push every button and earn 1 score -- update counter.

    2. Do step #1 for every digit.

    3. Return scores.
    """
    scores = 0
    for digit in '123456789':
        if 0 < field.count(digit) <= fingers_count:
            scores += 1

    return scores


def main() -> None:
    """
    The main function in which incoming data is read and transmitted to
    receive a solution to the problem into output.
    Returns None.
    """
    fingers_count, field = read_data()
    scores = get_scores(
        field=field,
        fingers_count=fingers_count*2
    )
    sys.stdout.write(str(scores))


def read_data() -> tuple[int, str]:
    """
    Read 5 lines from stdin stream. Returns a tuple with int and str
    For example, (1, '....\n....\n....\n....\n').
    """
    fingers_count = int(sys.stdin.readline())
    field = ''
    for _ in range(0, 4):
        field += sys.stdin.readline()

    return fingers_count, field


if __name__ == '__main__':
    main()
