"""
Implement a queue written using a linked list. All operations must be performed
in O(1). The queue must support the execution of 3 commands:
  - get() — output the element located at the head of the queue and delete it.
    If the queue is empty, then output "error".
  - put(x) — add the number x to the queue
  - size() — output the current queue size

The first line contains the number of commands N — an integer not exceeding
1000. In each of the following N lines, commands are written one line at a
time.

Print the answer to each query one per line.
"""
import sys


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def pop(self):
        if self.size == 0:
            return None

        first_elem = self.head

        if first_elem is self.tail:
            self.tail = None

        self.head = self.head.next_node
        self.size -= 1

        return first_elem.value

    def push(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = self.tail = new_node

        self.size += 1


def input_data():
    commands_count = int(sys.stdin.readline())
    commands = []
    for _ in range(0, commands_count):
        commands.append(sys.stdin.readline().strip().split(' '))

    return commands


def main():
    queue = Queue()
    cmds = input_data()
    for cmd in cmds:
        if cmd[0] == 'put':
            queue.push(int(cmd[-1]))
        elif cmd[0] == 'get':
            pop_item = queue.pop()
            print('error') if pop_item is None else print(pop_item)
        else:
            print(queue.size)


if __name__ == '__main__':
    main()
