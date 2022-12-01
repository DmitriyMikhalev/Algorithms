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
from typing import Union


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
        self.size = 0
        self.top = None

    def is_empty(self) -> bool:
        """Check size is equal to 0. Returns bool answer."""
        return self.size == 0

    def peek(self) -> Union[None, str, int]:
        """
        Returns None if stack is empty else returns value from top node (str or
        int) and delete that node.
        """
        return None if self.top is None else self.top.value

    def pop(self) -> Union[None, str, int]:
        """
        Returns None if stack is empty else returns value from top node (str or
        int) and delete this.
        """
        if self.is_empty():
            return None

        self.size -= 1
        first_elem = self.top
        self.top = self.top.next_node
        first_elem.next_node = None

        return first_elem.value

    def push(self, item: Union[str, int]) -> None:
        """
        Push element into stack.
        Required params: item -- str or int variable.
        Returns None.
        """
        self.top = Node(value=item, next_node=self.top)
        self.size += 1


def calculate(expression: list[Union[int, str]]) -> int:
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


def input_data() -> list[str]:
    """
    Get data from stdin stream. Returns list of str variables splited by space.
    """
    return sys.stdin.readline().strip().split(' ')


def is_number(string) -> bool:
    """Check if given str variable is number. Returns bool answer."""
    return string.isdigit() or string[1:].isdigit() and string[0] == '-'


def main() -> None:
    """
    The main function in which incoming data is read and transmitted to
    receive a solution to the problem into output.
    Returns None.
    """
    data: list[str] = input_data()
    expression: list[Union[str, int]] = prepare_data(data)
    res = calculate(expression)
    sys.stdout.write(str(res))


def prepare_data(data: list[str]) -> list[Union[str, int]]:
    """
    Get prepared data.
    Required params: data -- list of str variables.
    Returns new list (with str and int variables) with same elements but they
    were casted to int if it was possible.
    """
    return [i for i in map(lambda x: int(x) if is_number(x) else x, data)]


if __name__ == '__main__':
    main()
