"""
A sequence of brackets is given. It's necessary to check whether it's correct.

We will adhere to this definition:
  - an empty string is the correct bracket sequence;
  - a correct bracket sequence, taken in brackets of the same type, is a
    correct bracket sequence;
  - a correct bracket sequence with the correct bracket sequence assigned to
    the left or right is also correct.

A sequence of brackets of three types is supplied to the input: [], (), {}.
Write the is_correct_bracket_seq() function, which takes a bracket sequence as
input and returns True if the sequence is correct, otherwise False.

A single string containing a bracket sequence is supplied to the input. The
brackets are written in a row, without spaces.

Output "True" or "False".
"""
import sys


class Stack:
    def __init__(self):
        self.items = []
        self.length = 0

    def pop(self):
        if self.length == 0:
            return None

        self.length -= 1
        return self.items.pop()

    def push(self, item):
        self.items.append(item)
        self.length += 1

    def peek(self):
        if self.length == 0:
            return None

        return self.items[-1]


def is_correct_bracket_seq(string):
    if len(string) % 2 != 0:
        return False

    stack = Stack()
    for char in string:
        if char in '({[':
            stack.push(char)
        else:
            if stack.peek() == '[' and char != ']':
                return False
            elif stack.peek() == '{' and char != '}':
                return False
            elif stack.peek() == '(' and char != ')':
                return False
            if stack.pop() is None:
                return False

    return True


def main():
    string = sys.stdin.readline().strip()
    print(is_correct_bracket_seq(string))


if __name__ == '__main__':
    main()
