import logging
import sys
from logging import StreamHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(funcName)s - %(lineno)d - %(name)s - %(message)s'
)
handler = StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


def main():
    size = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split(' ')))
    print(' '.join(map(str, get_zero_range(arr, size))))


def get_zero_indexes(arr):
    zero_indexes = []
    for index, value in enumerate(arr):
        if value == 0:
            zero_indexes.append(index)

    logger.debug(f'get_zero_indexes вернула {zero_indexes=}')
    return zero_indexes


def get_min_zero_range(zeroes, index):
    if len(zeroes) == 1:
        return abs(zeroes[0] - index)

    for i in range(0, len(zeroes) - 1):
        if index < zeroes[i]:
            return zeroes[i] - index
        elif zeroes[i] < index < zeroes[i + 1]:
            return min(index - zeroes[i], zeroes[i + 1] - index)

    return abs(zeroes[-1] - index)
    # [98, 0, 10, 77, 0, 59, 28, 0, 94]
    # [1, 4, 7]


def get_zero_range(arr, size):
    zeroes = get_zero_indexes(arr)
    for i in range(0, size):
        if arr[i] != 0:
            arr[i] = get_min_zero_range(zeroes, i)

    logger.debug(f'get_zero_range вернула {arr=}')
    return arr


if __name__ == '__main__':
    main()
