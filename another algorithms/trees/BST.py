"""Check the tree is binary search tree."""
import sys

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(node) -> bool:
    def check(node, min, max):
        if node is None:
            return True

        if node.value <= min or node.value >= max:
            return False

        return check(
            node.left,
            min,
            node.value
        ) and check(node.right, node.value, max)

    return check(node, -sys.maxsize, sys.maxsize)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    #node2.value = 5
    #assert not solution(node5)


if __name__ == '__main__':
    test()
