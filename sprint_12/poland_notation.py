import sys
from typing import Union


class Node:
    def __init__(self, value, next_node=None) -> None:
        self.value = value
        self.next_node = next_node


class Stack:
    def __init__(self) -> None:
        self.size = 0
        self.top = None

    def push(self, item: Union[str, int]) -> None:
        self.top = Node(value=item, next_node=self.top)
        self.size += 1

    def peek(self) -> Union[None, str, int]:
        return None if self.top is None else self.top.value

    def pop(self) -> Union[None, str, int]:
        if self.is_empty():
            return None

        self.size -= 1
        first_elem = self.top
        self.top = self.top.next_node
        first_elem.next_node = None

        return first_elem.value

    def is_empty(self) -> bool:
        return self.size == 0


def calculate(expression) -> int:
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
    return sys.stdin.readline().strip().split(' ')


def is_number(string) -> bool:
    return string.isdigit() or string[1:].isdigit() and string[0] == '-'


def main() -> None:
    data = input_data()
    expression = prepare_data(data)
    res = calculate(expression)
    sys.stdout.write(str(res))


def prepare_data(data: list[str]) -> list[str, int]:
    return [i for i in map(lambda x: int(x) if is_number(x) else x, data)]


if __name__ == '__main__':
    main()
