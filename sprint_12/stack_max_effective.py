"""
Create stack that allows to push, pop and find max value for O(1).

The first line contains one number — the number of commands, it does not exceed
10^5. Next come the commands, one per line. Commands can be of the following
types:

push(x) — add a number x to the stack;
pop() — remove a number from the top of the stack;
get_max() — print the maximum number in the stack;

If the stack is empty, when calling the get_max command, you need to print
"None", for the pop command — "error".

For each get_max() command, print the result of its execution. If the stack is
empty, type "None" for the get_max() command. If there is a deletion from an
empty stack, type "error".
"""
import sys


class Stack:
    def __init__(self):
        self.items = []

    def peek(self):
        if len(self.items) == 0:
            return None

        return self.items[-1]

    def pop(self):
        if len(self.items) == 0:
            return None

        return self.items.pop()

    def push(self, item):
        self.items.append(item)


class StackEffective:
    def __init__(self):
        self.items = []
        self.max_values_stack = Stack()

    def get_max(self):
        return self.max_values_stack.peek()

    def pop(self):
        if len(self.items) == 0:
            return None

        if self.max_values_stack.peek() == self.items[-1]:
            self.max_values_stack.pop()

        return self.items.pop()

    def push(self, item):
        self.items.append(item)
        max_value = self.max_values_stack.peek()
        if max_value is None or max_value <= item:
            self.max_values_stack.push(item)


def input_data():
    commands_count = int(sys.stdin.readline())
    commands = []
    for _ in range(0, commands_count):
        commands.append(sys.stdin.readline().strip().split(' '))

    return commands


def main():
    stack = StackEffective()
    cmds = input_data()
    for cmd in cmds:
        if cmd[0] == 'push':
            stack.push(int(cmd[-1]))
        elif cmd[0] == 'pop':
            if stack.pop() is None:
                print('error')
        else:
            print(stack.get_max())


if __name__ == '__main__':
    main()
