"""
Alla received a task related to monitoring the operation of various servers. It
is necessary to understand how long certain requests are processed on specific
servers. This information should be stored in a matrix, where the column number
corresponds to the request ID, and the row number corresponds to the server ID.
Alla mixed up rows and columns in places. It happens to everyone. Help her fix
the bug.

There is a matrix of size M * N. You need to write a function that transposes
it.

The transposed matrix is obtained from the original by replacing rows with
columns.

The first row contains the number N — the number of rows of the matrix.
The second row contains M — the number of columns, M and N do not exceed 1000.
In the next N lines, a matrix is given. The numbers in it do not exceed modulo
1000.

Print the transposed matrix in the same format that is specified in the input
data. Each row of the matrix is displayed on a separate line, the elements are
separated by spaces.
"""
import sys


def input_data():
    rows_count = int(sys.stdin.readline())
    _ = sys.stdin.readline()
    matrix = []
    for _ in range(0, rows_count):
        matrix.append(sys.stdin.readline().strip().split(' '))

    return matrix


def main():
    matrix = input_data()
    for row in transponse_matrix(matrix):
        for elem in row:
            print(elem, end=' ')
        print()


def transponse_matrix(matrix):
    return zip(*matrix)


if __name__ == '__main__':
    main()
