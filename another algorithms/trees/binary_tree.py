from __future__ import annotations

from typing import Any


class Node:
    def __init__(self: Node, data: Any = None, left: Node | None = None,
                 right: Node | None = None):
        self.data = data
        self.right = right
        self.left = left

    def _is_leaf(self: Node) -> bool:
        return all(child is None for child in (self.right, self.left))


class Tree:
    def __init__(self: Tree, root: Node | None = None) -> None:
        self.root = root

    def delete(self: Tree, data: Any) -> Node | None:
        node, parent, is_found = self._find(self.root, parent=None, data=data)
        if is_found is False:
            return None

        if node._is_leaf():
            # 0 childs
            return self._delete_leaf(node, parent)
        elif node.left is not None and node.right is not None:
            # 2 childs
            return self._delete_two(node, parent)
        else:
            # 1 child
            return self._delete_one(node=node, parent=parent)

    def insert(self: Tree, data: Any) -> Node:
        if self.root is None:
            self.root = Node(data)
            return self.root

        node, *_ = self._find(self.root, None, data)
        if node is not None:
            new_node = Node(data)
            if data < node.data:
                node.left = new_node
            else:
                node.right = new_node

        return new_node

    def print_direct(self: Tree, node: Node | None) -> None:
        if node is None:
            return

        self.print_direct(node.left)
        self.print_direct(node.right)
        print(node.data, end=' ')

    def print_LMR(self: Tree, node: Node | None) -> None:
        if node is None:
            return

        self.print_LMR(node.left)
        print(node.data, end=' ')
        self.print_LMR(node.right)

    def print_RML(self: Tree, node: Node | None) -> None:
        if node is None:
            return

        self.print_RML(node.right)
        print(node.data, end=' ')
        self.print_RML(node.left)

    def _delete_leaf(self: Tree, node: Node, parent: Node) -> Node:
        if parent.left is node:
            parent.left = None
        else:
            parent.right = None

        return node

    def _delete_one(self: Tree, node: Node, parent: Node) -> Node:
        if parent.left is node:
            parent.left = node.left or node.right
        else:
            parent.right = node.left or node.right

        return node

    def _delete_two(self: Tree, node: Node, parent: Node) -> Node:
        """
        The node replacing the one being deleted can always have only the right
        child, since it has the smallest value located in the right subtree of
        the node being deleted.
        If the node in question has a left child, then it is necessary to move
        to the left until the present minimum element is reached.
        """
        min_node, min_node_parent = self._find_min(
            node=node.right,
            parent=parent
        )
        node.data = min_node.data

        return self._delete_one(node=min_node, parent=min_node_parent)

    def _find(self: Tree, node: Node, parent: Node,
              data: Any) -> tuple[Node, Node, bool]:
        """
        Returns:
            * the deepest node with passed data (or None if it not exists),
            * parent of that node (if node is None returns parent of that node
              in case it exists)
            * boolean answer to the question 'Is it found'?
        """
        if node is None:
            return None, parent, False

        if data == node.data:
            while node.right is not None and node.right.data == data:
                parent = node
                node = node.right
            return node, parent, True
        elif data < node.data:
            if node.left is not None:
                return self._find(node=node.left, parent=node, data=data)
        else:
            if node.right is not None:
                return self._find(node=node.right, parent=node, data=data)

        return node, parent, False

    def _find_min(self: Tree, node: Node, parent: Node) -> tuple[Node, Node]:
        if node.left is not None:
            return self._find_min(node=node.left, parent=node)

        return node, parent


def main() -> None:
    tree = Tree(Node(0))
    vals = [-3, 1, -5, 42, 4, -6, 8, -5, -7, 2, -6, -1, -1, -2]
    # vals = [8, 19, 3, 10, 17, 25, 1, 4, 9, 11, 16, 18, 23, 27]
    for val in vals:
        tree.insert(val)

    tree.print_direct(tree.root)
    tree.delete(-3)
    print()
    tree.print_direct(tree.root)


if __name__ == '__main__':
    main()
