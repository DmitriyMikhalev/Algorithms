"""
The task is related to the reverse Polish notation. It is used for parsing
arithmetic expressions. It is also sometimes called postfix notation.

In postfix notation, operands are placed before the operation signs.

Example 1:
3 4 +
means 3 + 4 and equals 7

Example 2:
12 5 /
Since the division is integer, we get 2 as a result.

Example 3:
10 2 4 * -
means 10 - 2 * 4 and is equal to 2

The sign * stands immediately after the numbers 2 and 4, so you need to apply
to them the operation that this sign denotes, that is, multiply these two
numbers. As a result, we get 8.

After that , the expression will take the form:

10 8 -

The "minus" operation must be applied to the two numbers in front of it, that
is, 10 and 8. As a result, we get 2.

In the current problem, it is guaranteed that there is no division by a
negative number.

Input format
A single line contains an expression written in reverse Polish notation.
Numbers and arithmetic operations are written separated by a space.

The following operations can be applied to the input: +, -, *, / and numbers
modulo no more than 10000.

It is guaranteed that the value of intermediate expressions in the test data
modulo no more than 50000.

Output format
Print a singular number — the value of the expression.

--------------+---------------+
Sample input  | Sample output |
2 1 + 3 *     | 9             |
--------------+---------------+
7 2 + 4 * 2 + | 38            |
--------------+---------------+
"""
import sys
from typing import List, Union


class Node:
    """Linked-list node class. Provides only initalize method."""
    def __init__(self, value, next_node=None) -> None:
        self.value = value
        self.next_node = next_node


class Stack:
    """
    Linked-list based stack. Provides push, peek, pop and check for emptiness.
    Stack's top node is head of list (tail is first element added to stack)
    so insert operation has O(1) complexity: we have only to create new head
    node and set pointer to next node (previous head) and refresh size
    attribute. Pop operation also has O(1) complexity - the element to be
    deletde is head.
    """
    def __init__(self) -> None:
        self.__size = 0
        self.__top = None

    def __is_empty(self) -> bool:
        """Check size is equal to 0. Returns bool answer."""
        return self.__size == 0

    def peek(self) -> Union[str, int]:
        """
        Get a top item from the stack.
        Raises StackEmptyException if it was empty when user tried to get.
        Returns value from top node.
        """
        if self.__is_empty():
            raise StackEmptyException('Stack was empty!')

        return self.__top.value

    def pop(self) -> Union[str, int]:
        """
        Get and delete a top item from the stack.
        Raises StackEmptyException if it was empty when user tried to delete.
        Returns value from top node and delete this.
        """
        if self.__is_empty():
            raise StackEmptyException('Stack was empty!')

        self.__size -= 1
        first_elem = self.__top
        self.__top = self.__top.next_node
        first_elem.next_node = None

        return first_elem.value

    def push(self, item: Union[str, int]) -> None:
        """
        Push element into stack.
        Required params: item -- str or int variable.
        Returns None.
        """
        self.__top = Node(value=item, next_node=self.__top)
        self.__size += 1


class StackEmptyException(Exception):
    """Use it if the user tried to pop or peek an item from an empty stack."""
    pass


def calculate(expression: List[Union[int, str]]) -> int:
    """
    Get result of expression given in reverse poland notation.
    Required params: expression - list of int or str variables, where int is
                     number and str is operation.
    Returns int variable as a result.
    Algorithm:
      1. Create stack and operation functions.
      2. Iterate over expression list, if current element is int, add it to
         stack, else (element is operation) get 2 last numbers from stack and
         transform them using current operation, add result into stack.
      3. Return first element from stack.

    >>> calculate([2, 1, '+', 3, '*'])
    9
    >>> calculate([7, 2, '+', 4, '*', 2, '+'])
    38
    """
    operations = {
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
        '-': lambda x, y: x - y,
        '+': lambda x, y: x + y,
    }
    stack = Stack()
    for elem in expression:
        if isinstance(elem, int):
            stack.push(elem)
        else:
            right_operand = stack.pop()
            left_operand = stack.pop()
            stack.push(operations[elem](left_operand, right_operand))

    return stack.pop()


def input_data(stream=sys.stdin) -> List[str]:
    """
    Get data from stdin stream. Returns list of str variables splited by space.
    """
    if isinstance(stream, str):
        stream = open(encoding='utf-8', file=stream, mode='r')
    data = stream.readline().strip().split(' ')
    stream.close()

    return data


def is_number(string) -> bool:
    """
    Check if given str variable is number.
    Returns bool answer.

    >>> is_number('123')
    True
    >>> is_number('-12')
    True
    >>> is_number('1f')
    False
    >>> is_number('string')
    False
    """
    return string.isdigit() or string[1:].isdigit() and string[0] == '-'


def main() -> None:
    """
    The main function in which incoming data is read and transmitted to
    receive a solution to the problem into output.
    Returns None.
    """
    data: List[str] = input_data()
    expression: List[Union[str, int]] = prepare_data(data)
    try:
        res = calculate(expression)
        output_data(str(res))
    except StackEmptyException as e:
        output_data(str(e))


def output_data(data, stream=sys.stdout) -> None:
    """
    Write data into given stream (by default is sys.stdout).
    Required params: data -- str, data to be written.
    Returns None.
    """
    if isinstance(stream, str):
        stream = open(encoding='utf-8', file=stream, mode='w')

    stream.write(data)


def prepare_data(data: List[str]) -> List[Union[str, int]]:
    """
    Get prepared data.
    Required params: data -- list of str variables.
    Returns new list (with str and int variables) with same elements but they
    were casted to int if it was possible.

    >>> prepare_data(['13', '7', '-'])
    [13, 7, '-']
    >>> prepare_data(['13', '7'])
    [13, 7]
    >>> prepare_data(['/', '+', '-'])
    ['/', '+', '-']
    >>> prepare_data([])
    []
    """
    return [i for i in map(lambda x: int(x) if is_number(x) else x, data)]


if __name__ == '__main__':
    main()
