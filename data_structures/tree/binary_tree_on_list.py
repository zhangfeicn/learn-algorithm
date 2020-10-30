"""
In a list of lists tree, store the value of the root node as the first element
of the list.

The second element of the list will itself be a list that represents
the left subtree.

The third element of the list will be another list that represents the right
subtree.
"""

_created = "2020-04-10"


class BinaryTree:
    """"
    Implementing a binary tree with a Python list
    """

    def __init__(self, value):
        # 0 -> root, 1 -> left subtree, 2 -> right subtree
        self._root = [value, None, None]

    def __repr__(self):
        return repr(self._root)

    def insert_left(self, new_left):
        t = self._root.pop(1)
        new_tree = BinaryTree(new_left)
        if t is not None:
            new_tree.set_left_child(t)
        self._root.insert(1, new_tree)

    def insert_right(self, new_right):
        t = self._root.pop(2)
        new_tree = BinaryTree(new_right)
        if t is not None:
            new_tree.set_right_child(t)
        self._root.insert(2, new_tree)

    def get_root(self):
        return self._root[0]

    def set_root(self, value):
        self._root[0] = value

    def get_left_child(self):
        return self._root[1]

    def set_left_child(self, value):
        self._root[1] = value

    def get_right_child(self):
        return self._root[2]

    def set_right_child(self, value):
        self._root[2] = value


def _main():
    print('Binary Tree Demonstration')
    root = BinaryTree(3)
    root.insert_left(4)
    root.insert_left(5)
    root.insert_right(6)
    root.insert_right(7)
    print(root)
    left = root.get_left_child()
    print(left)
    left.set_root(9)
    print(root)
    left.insert_left(11)
    print(root)
    print(root.get_right_child().get_right_child())

    x = BinaryTree('a')
    x.insert_left('b')
    x.insert_right('c')
    x.get_right_child().insert_right('d')
    x.get_right_child().get_right_child().insert_left('e')
    print(x)


if __name__ == "__main__":
    _main()
