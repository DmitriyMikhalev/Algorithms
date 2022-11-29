"""
Get node index with given value. If it doesn't exist, return -1.
"""
LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(head, value):
    index = 0
    node = head
    while True:
        if node.value == value:
            return index
        elif node.next_item is None:
            return -1

        node = node.next_item
        index += 1


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2


if __name__ == '__main__':
    test()
