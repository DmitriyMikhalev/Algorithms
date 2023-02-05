"""Output non-decreasing all keys from L to R."""
LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def print_range(node, min, max):
    res = []

    def lmr(node, left, right, res):
        if node.value >= left and node.left is not None:
            lmr(node.left, left, right, res)

        if left <= node.value <= right:
            res.append(node.value)

        if node.value <= right and node.right is not None:
            lmr(node.right, left, right, res)

    lmr(node, min, max, res)
    print(*res)


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8


if __name__ == '__main__':
    test()
