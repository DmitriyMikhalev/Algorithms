"""
Determine how much code the next intern will write find the last k digits of
the number Fn.

How to find the k last digits

To calculate the last k digits of some number x, it is enough to take the
remainder of its division by the number 10k. This operation is denoted as x
mod 10k. Find out how the operation of taking the remainder modulo is written
in your programming language.

Also pay attention to the possible overflow of integer types, if this happens
in your language.

In the first line, two integers n (0 <= n <= 10^6) and k (1 <= k <= 8) are
written separated by a space.

Print a single number – the last k digits of the number Fn.

If the number you are looking for is less than k digits, then print the number
itself without leading zeros.
"""
import sys


def fibonacci(n):
    cache = [1, 1]
    if n == 0 or n == 1:
        return 1

    for i in range(2, n + 1):
        cache[i % 2] = cache[0] + cache[-1]

    return cache[n % 2]


def input_data():
    return [int(i) for i in sys.stdin.readline().split(' ')]


def main():
    n, k = 921756, 5
    res = fibonacci(n)
    print(res % 10**k)


if __name__ == '__main__':
    main()
