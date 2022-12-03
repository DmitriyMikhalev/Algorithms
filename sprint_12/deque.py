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
from typing import Any, List, Optional, Tuple


class Deque:
    """
    Double-ended queue. Allows to add an item to the head or tail of the queue
    or pop item from there, check for emptiness or fullness. Every operation
    takes O(1) complexity.

      Attributes     types            meaning           access
      * head     |    int    | index of current head | protected |
      * max_size |    int    | max count of items    | protected |
      * tail     |    int    | index of current tail | protected |
      * items    | list[Any] | storage of items      | protected |

      Methods        return    access
      * is_empty   |  bool  | protected |
      * is_full    |  bool  | protected |
      * push_back  |  None  | public    |
      * push_front |  None  | public    |
      * pop_back   |  None  | public    |
      * pop_front  |  None  | public    |

    Implementation:
      * At start list of given size is filled with None values.

      * Head and tail store indexes of current values (not next None-value).

      * push_back:
          - If the deque is full raises DequeOverflowException.
          - If deque is empty, first element must be head and tail at the same
            time that means tail is not changing. Else tail index is moving by
            '-1' (by modulo the size, so it walks around the list in a circle).
          - Set item at current tail index at list.
          - Change size to '+1'.

      * push_front:
          - If the deque is full raises DequeOverflowException.
          - If deque is empty, first element must be head and tail at the same
            time that means head is not changing. Else head index is moving by
            '+1' (by modulo the size, so it walks around the list in a circle).
          - Set item at current head index at list.
          - Change size to '+1'.

      * pop_back:
          - If the deque is empty raises DequeEmptyException.
          - Change size to '-1'.
          - Store item value at current tail index.
          - If the deque is still has size > 0 tail index have to be moved by
            '+1' (by modulo the size, so it walks around the list in a circle).
          - Return stored item value. Note that this value wasn't changed to
            None at list, but there's no ways to get that.

      * pop_front:
          - If the deque is empty raises DequeEmptyException.
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
        """
        self.__items = [None] * max_size
        self.__max_size = max_size
        self.__size = self.__head = self.__tail = 0

    def __is_empty(self) -> bool:
        """Is the deque empty? Returns bool variable."""
        return self.__size == 0

    def __is_full(self) -> bool:
        """Is the deque full? Returns bool variable."""
        return self.__size == self.__max_size

    def pop_back(self) -> Any:
        """
        Delete item from back of the deque and return it.
        Raises DequeEmptyException if deque is empty.
        Returns item of any type.
        """
        if self.__is_empty():
            raise DequeEmptyException(
                'The queue was empty at the time the item was retrieved!'
            )

        self.__size -= 1
        item = self.__items[self.__tail]
        if not self.__is_empty():
            self.__tail = (self.__tail + 1) % self.__max_size

        return item

    def pop_front(self) -> Any:
        """
        Delete item from front of the deque and return it.
        Raises DequeEmptyException if deque is empty.
        Returns item of any type.
        """
        if self.__is_empty():
            raise DequeEmptyException(
                'The queue was empty at the time the item was retrieved!'
            )

        self.__size -= 1
        item = self.__items[self.__head]
        if not self.__is_empty():
            self.__head = (self.__head - 1) % self.__max_size

        return item

    def push_back(self, item: Any) -> None:
        """
        Push item into back of the deque.
        Required params: item -- Any, item to be stored.
        Raises DequeOverflowException if deque is full.
        Returns None.
        """
        if self.__is_full():
            raise DequeOverflowException('Deque is already full!')

        if not self.__is_empty():
            self.__tail = (self.__tail - 1) % self.__max_size

        self.__items[self.__tail] = item
        self.__size += 1

    def push_front(self, item: Any) -> None:
        """
        Push item into front of the deque.
        Required params: item -- Any, item to be stored.
        Raises DequeOverflowException if deque is full.
        Returns None.
        """
        if self.__is_full():
            raise DequeOverflowException('Deque is already full!')

        if not self.__is_empty():
            self.__head = (self.__head + 1) % self.__max_size

        self.__items[self.__head] = item
        self.__size += 1


class DequeEmptyException(Exception):
    """Use it if the user tried to pop an item from an empty deque."""
    pass


class DequeOverflowException(Exception):
    """Use it if the user tried to push an item into an filled deque."""
    pass


def get_command_result(command: List[str], deque: Deque) -> Optional[str]:
    cmd, *args = command
    func = getattr(deque, cmd)

    return func(*args)


def get_commands_res(commands: List[List[str]], max_size: int) -> str:
    """
    Get solution to the problem.
    Required params:
      commands -- list[list[str]], commands to operate deque.
      max_size -- int, max count of items at deque
    Returns generator that processes commands in turn.
    """
    deque = Deque(max_size)
    for command in commands:
        try:
            if res := get_command_result(command=command, deque=deque):
                yield res
        except (DequeEmptyException, DequeOverflowException):
            yield 'error'


def input_data(stream=sys.stdin) -> Tuple[int, List[List[str]]]:
    """
    Read data from the given stream (by default is sys.stdout).
    Returns tuple of 2 items: first line converted to int and list of splited
    by space into list lines, for example:
      (1, [
          ['line_1', '1'],
          ['line_2'],
          ['line_3', '5', 'asdasdsa', 'None', '0'],
          ...
      ])
    """
    if isinstance(stream, str):
        stream = open(encoding='utf-8', file=stream, mode='r')

    commands_count = int(stream.readline())
    max_size = int(stream.readline())
    commands = []
    for _ in range(commands_count):
        commands.append(stream.readline().strip().split(' '))
    stream.close()

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
    for command_res in get_commands_res(commands=cmds, max_size=size):
        output_data(data=command_res)


def output_data(data, stream=sys.stdout) -> None:
    """
    Write data and '\n' char into given stream (by default is sys.stdout).
    Required params: data -- str, data to be written.
    Returns None.
    """
    if isinstance(stream, str):
        stream = open(encoding='utf-8', file=stream, mode='w')

    stream.write(data + '\n')


if __name__ == '__main__':
    main()
