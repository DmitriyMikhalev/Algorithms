"""Insert a node with a given key, return the root."""
LOCAL = True

if not LOCAL:
    from node import Node

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def insert(node, key) -> Node:
    def insert_node(node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(value=key)
            else:
                insert_node(node.left, key)
        elif key >= node.value:
            if node.right is None:
                node.right = Node(value=key)
            else:
                insert_node(node.right, key)

    insert_node(node, key)
    return node


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == '__main__':
    test()
