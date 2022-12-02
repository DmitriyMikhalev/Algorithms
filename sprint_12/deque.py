"""
Gosha implemented the data structure of the deque, the maximum size of which is
determined by a given number. The push_back(x), push_front(x), pop_back(),
pop_front() methods worked correctly. But if there were a lot of elements in
the soundboard, the program worked for a very long time. The fact is that not
all operations were performed in O(1). Help Gosha! Write an effective
implementation.

Attention: When implementing, use a ring buffer.

The first line contains the number of commands n — an integer not exceeding
10^5. The second line contains the number m — the maximum size of the deque.
It does not exceed 50000. The following n lines contain one of the commands:

  * push_back(value) – add an element to the end of the deque. If the deque
    already contains the maximum number of elements, print "error".

  * push_front(value) – add an element to the beginning of the soundboard. If
    the deque already contains the maximum number of elements, print "error".

  * pop_front() – output the first element of the deque and delete it. If the
    deque was empty, then output "error".

  * pop_back() – output the last element of the deque and delete it. If the
    deque was empty, then output "error".

Value is an integer modulo no more than 10^3.

Print the result of each command on a separate line. For successful
push_back(x) and push_front(x) requests, nothing needs to be output

----------------+---------------+
Sample input    | Sample output |
4               | 861           |
4               | -819          |
push_front 861  |               |
push_front -819 |               |
pop_back        |               |
pop_back        |               |
----------------+---------------+
7               | -855          |
10              | 0             |
push_front -855 | 844           |
push_front 0    |               |
pop_back        |               |
pop_back        |               |
push_back 844   |               |
pop_back        |               |
push_back 823   |               |
----------------+---------------+
6               | 20            |
6               | 102           |
push_front -201 |               |
push_back 959   |               |
push_back 102   |               |
push_front 20   |               |
pop_front       |               |
pop_back        |               |
----------------+---------------+
"""
import sys
from typing import Any, List, Tuple


class Deque:
    """
    Double-ended queue. Allows to add an item to the head or tail of the queue
    or pop item from there, check for emptiness or fullness. Every operation
    takes O(1) complexity.

    Attributes
      * head     |    int    | index of current head
      * max_size |    int    | max count of items
      * tail     |    int    | index of current tail
      * items    | list[Any] | storage of items

    Implementation:
      * At start list of given size is filled with None values.

      * Head and tail store indexes of current values (not next None-value).

      * push_back:
          - If the deque is full return False as the operation status.
          - If deque is empty, first element must be head and tail at the same
            time that means tail is not changing. Else tail index is moving by
            '-1' (by modulo the size, so it walks around the list in a circle).
          - Set item at current tail index at list.
          - Change size to '+1'.
          - Return True as the operation status.

      * push_front:
          - If the deque is full return False as the operation status.
          - If deque is empty, first element must be head and tail at the same
            time that means head is not changing. Else head index is moving by
            '+1' (by modulo the size, so it walks around the list in a circle).
          - Set item at current head index at list.
          - Change size to '+1'.
          - Return True as the operation status.

      * pop_back:
          - If the deque is empty return None.
          - Change size to '-1'.
          - Store item value at current tail index.
          - If the deque is still has size > 0 tail index have to be moved by
            '+1' (by modulo the size, so it walks around the list in a circle).
          - Return stored item value. Note that this value wasn't changed to
            None at list, but there's no ways to get that.

      * pop_front:
          - If the deque is empty return None.
          - Change size to '-1'.
          - Store item value at current tail index.
          - If the deque is still has size > 0 head index have to be moved by
            '+1' (by modulo the size, so it walks around the list in a circle).
          - Return stored item value. Note that this value wasn't changed to
            None at list, but there's no ways to get that.
    """
    def __init__(self, max_size: int) -> None:
        """
        Initalize deque object.
        Required params: max_size -- int, max count of items at object.
        Returns None.
        """
        self.items = [None] * max_size
        self.max_size = max_size
        self.size = self.head = self.tail = 0

    def is_empty(self) -> bool:
        """Is the deque empty? Returns bool variable."""
        return self.size == 0

    def is_full(self) -> bool:
        """Is the deque full? Returns bool variable."""
        return self.size == self.max_size

    def pop_back(self) -> Any:
        """
        Delete item from back of the deque and return it.
        Returns None if deque is empty, else returns item.
        """
        if self.is_empty():
            return None

        self.size -= 1
        item = self.items[self.tail]
        if not self.is_empty():
            self.tail = (self.tail + 1) % self.max_size

        return item

    def pop_front(self) -> Any:
        """
        Delete item from front of the deque and return it.
        Returns None if deque is empty, else returns item.
        """
        if self.is_empty():
            return None

        self.size -= 1
        item = self.items[self.head]
        if not self.is_empty():
            self.head = (self.head - 1) % self.max_size

        return item

    def push_back(self, item: Any) -> bool:
        """
        Push item into back of the deque.
        Required params: item -- Any, item to be stored.
        Returns bool variable as the opertaion status.
        """
        if self.is_full():
            return False

        if not self.is_empty():
            self.tail = (self.tail - 1) % self.max_size

        self.items[self.tail] = item
        self.size += 1
        return True

    def push_front(self, item: Any) -> bool:
        """
        Push item into front of the deque.
        Required params: item -- Any, item to be stored.
        Returns bool variable as the opertaion status.
        """
        if self.is_full():
            return False

        if not self.is_empty():
            self.head = (self.head + 1) % self.max_size

        self.items[self.head] = item
        self.size += 1
        return True


def get_solution(max_size: int, commands: List[List[str]]) -> None:
    """
    Get solution to the problem.
    Required params:
      max_size -- int, max count of items at deque
      commands -- list[str], commands to operate deque.
    Returns None.
    """
    deque = Deque(max_size)
    for command in commands:
        if command[0] == 'pop_back':
            sys.stdout.write(deque.pop_back() or 'error')
        elif command[0] == 'pop_front':
            sys.stdout.write(deque.pop_front() or 'error')
        elif command[0] == 'push_back':
            if not deque.push_back(command[-1]):
                sys.stdout.write('error')
        else:
            if not deque.push_front(command[-1]):
                sys.stdout.write('error')


def input_data() -> Tuple[int, List[List[str]]]:
    """
    Read data from stdin stream.
    Returns a tuple with size of deque and list of commands (also stored at
    list) to operate it.
    """
    commands_count = int(sys.stdin.readline())
    max_size = int(sys.stdin.readline())
    commands = []
    for _ in range(0, commands_count):
        commands.append(sys.stdin.readline().strip().split(' '))

    return max_size, commands


def main() -> None:
    """
    The main function in which incoming data is read and transmitted to
    receive a solution to the problem into output.
    Returns None.
    """
    size: int
    cmds: List[List[str]]
    size, cmds = input_data()
    get_solution(max_size=size, commands=cmds)


if __name__ == '__main__':
    main()
