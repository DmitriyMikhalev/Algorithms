"""
Find the next Fibonacci number (starts at 0).
The solution must be implemented recursively.

The input is an N — integer in the range from 0 to 32.

You need to output F(N).
F(0) = F(1) = 1
F(1) = 1
F(2) = 2
F(3) = 3
F(4) = 5
...
"""
import sys


def fibonacci_recursive(n):
    if n == 1 or n == 0:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def input_data():
    return int(sys.stdin.readline())


def main():
    n = input_data()
    res = fibonacci_recursive(n)
    sys.stdout.write(str(res))


if __name__ == '__main__':
    main()
