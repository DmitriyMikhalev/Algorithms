"""
You need to write the MyQueueSized class, which takes the max_size parameter,
which means the maximum allowed number of items in the queue.

Implement a program that will emulate the operation of such a queue.
The functions that need to be supported are described in the input format.

The first line contains one number — the number of commands, it does not
exceed 5000. The second line specifies the maximum allowed queue size, it does
not exceed 5000. Next come the commands, one per line. Commands can be of the
following types:
  - push(x) — add the number x to the queue;
  - pop() — remove a number from the queue and print it;
  - peek() — print the first number in the queue;
  - size() — return the queue size;

If the allowed queue size is exceeded, you need to output "error". When calling
pop() or peek() operations for an empty queue, output "None".

Print the results of executing the necessary commands, one per line.
"""
import sys


class MySizedQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.head = self.tail = self.size = 0
        self.items = [None] * max_size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return self.items[self.head]

    def push(self, item):
        if self.size != self.max_size:
            self.items[self.tail] = item
            self.size += 1
            self.tail = (self.tail + 1) % self.max_size

    def pop(self):
        if self.is_empty():
            return None

        self.size -= 1
        item = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_size

        return item


def input_data():
    commands_count = int(sys.stdin.readline())
    max_size = int(sys.stdin.readline())
    commands = []
    for _ in range(0, commands_count):
        commands.append(sys.stdin.readline().strip().split(' '))

    return max_size, commands


def main():
    max_size, cmds = input_data()
    queue = MySizedQueue(max_size)
    for cmd in cmds:
        if cmd[0] == 'push':
            if queue.size == queue.max_size:
                print('error')
            queue.push(int(cmd[-1]))
        elif cmd[0] == 'pop':
            print(queue.pop())
        elif cmd[0] == 'peek':
            print(queue.peek())
        else:
            print(queue.size)


if __name__ == '__main__':
    main()
