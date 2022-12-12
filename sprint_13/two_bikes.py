"""
Vasya decided to save up money for two identical bicycles — for himself and his
sister. Vasya has a piggy bank into which he can add money every day (if, of
course, he has such a financial opportunity). In the process of accumulation,
Vasya does not take money out of the piggy bank.

You have information about the growth of Vasya's savings — how much money Vasya
had in his piggy bank on each of the days.

Your task is to determine the value of the bike for a given price

the first day in which Vasya could buy one bike,
and the first day in which Vasya could buy two bikes.
Hint: the solution should work in O(logn).

The first line contains the number of days n for which observations of Vasya's
accumulations were conducted. 1 <= n <= 10^6.

The next line contains n non-negative integers. The numbers are in
non-decreasing order. Each of the numbers does not exceed 10^6.

The third line contains a positive integer s — the cost of the bike. This
number does not exceed 10^6.

You need to output two numbers — the numbers of days according to the condition
of the task.

If the required amount was not found in the piggy bank, you need to return -1
instead of the day number.
"""
import sys
from typing import Any, List, Tuple, Union


def binary_search_recursive(
    array: List[Union[int, str]],
    to_find: Union[int, str],
    left_index: int,
    right_index: int
) -> int:
    if left_index >= right_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if array[mid_index] >= to_find and (array[mid_index - 1] < to_find or
                                        mid_index == 0):
        return mid_index + 1
    elif to_find > array[mid_index]:
        return binary_search_recursive(
                array,
                to_find,
                mid_index + 1,
                right_index
            )
    else:
        return binary_search_recursive(
            array,
            to_find,
            left_index,
            mid_index
            )


def input_data(stream=sys.stdin) -> Tuple[int, List[Union[int, str]], int]:
    """
    Read data from the given stream (by default is sys.stdin).
    Returns tuple of 3 items:
        - size of list
        - list of int (line splited by space)
        - price of bike
    """
    if isinstance(stream, str):
        stream = open(encoding='utf-8', file=stream, mode='r')

    size = int(stream.readline())
    array = [int(i) for i in stream.readline().strip().split(' ')]
    price = int(stream.readline())
    stream.close()

    return size, array, price


def main() -> None:
    args: Tuple[int, List[int], int] = input_data()
    res = solution(*args)
    output_data(res)


def output_data(data: Any, stream=sys.stdout) -> None:
    """
    Write data into given stream (by default is sys.stdout).
    Required params: data -- str, data to be written.
    Returns None.
    """
    if isinstance(stream, str):
        stream = open(encoding='utf-8', file=stream, mode='w')

    stream.write(data)


def solution(size: int, array: List[Union[int, str]], price: int) -> str:
    left_index = 0
    first = binary_search_recursive(array, price, left_index, size)
    second = binary_search_recursive(array, price*2, left_index, size)
    return f'{first} {second}'


if __name__ == '__main__':
    main()
