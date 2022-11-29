"""
You need to implement the StackMax class, which supports the operation of
determining the maximum among all elements in the stack. The class must support
push(x) operations, where x is an integer, pop() and get_max().

The first line contains one number N — the number of commands that does not
exceed 10^4. In the next N lines there are commands. Commands can be of the
following types:

push(x) — add a number x to the stack;
pop() — remove a number from the top of the stack;
get_max() — print the maximum number in the stack;

If the stack is empty, when calling the get_max() command, print "None", for
the pop() command, "error".

For each get_max() command, print the result of its execution. If the stack
is empty, type "None" for the get_max() command. If there is a deletion from
an empty stack, type "error".
"""
import sys


class StackMax:
    def __init__(self):
        self.items = []

    def get_max(self):
        if len(self.items) == 0:
            return 'None'

        return max(self.items)

    def pop(self):
        if len(self.items) == 0:
            return None

        return self.items.pop()

    def push(self, item):
        self.items.append(item)


def input_data():
    commands_count = int(sys.stdin.readline())
    commands = []
    for _ in range(0, commands_count):
        commands.append(sys.stdin.readline().strip().split(' '))

    return commands


def main():
    stack = StackMax()
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
