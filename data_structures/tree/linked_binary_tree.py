"""
Implement Binary Tree on Linked Structure
"""

from abstract_tree import BinaryTree

_created = "2020-04-11"


class LinkedBinaryTree(BinaryTree):
    """
    Linked representation of a binary tree structure
    """

    # nonpublic class for storing a node
    class _Node:
        __slots__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

        def __repr__(self):
            return f"Node({self._element})"

    class Position(BinaryTree.Position):
        """
        An abstraction representing the location of a single element
        """

        def __init__(self, container, node):
            self._container = container  # the tree itself
            self._node = node

        def __eq__(self, other):
            """
            Return True if other is a Position representing the same location
            """
            return type(other) is type(self) and other._node is self._node

        def __repr__(self):
            temp = f"<p={self._node._parent} l={self._node._left} " \
                f"r={self._node._right} e={self._node}>"
            return temp

        def element(self):
            """
            Return the element stored at this Position
            """
            return self._node._element

        def add_left(self, e):
            if self._node._left is not None:
                raise ValueError("left child exists")
            self._container._size += 1
            self._node._left = self._container._Node(e)
            self._node._left._parent = self._node
            # new instance
            return self.left()

        def add_right(self, e):
            if self._node._right is not None:
                raise ValueError("right child exists")
            self._container._size += 1
            self._node._right = self._container._Node(e)
            self._node._right._parent = self._node
            # new instance
            return self.right()

        def left(self):
            # any way to get ride of this LinkedBinaryTree.Position()?
            return self._container.Position(
                self._container, self._node._left)

        def right(self):
            return self._container.Position(
                self._container, self._node._right)

        def parent(self):
            return self._container.Position(
                self._container, self._node._parent)

        def replace(self, e):
            old = self._node._element
            self._node._element = e
            return old

    def __init__(self):
        """
        Create an initially empty binary tree
        """
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        """
        Return the root Position of the tree (or None if tree is empty)
        """
        return self._make_position(self._root)

    def parent(self, p=None):
        """
        Return Position representing p's parent (or None if p is root)
        """
        node = self._validate(p) if p is not None else self._root
        return self._make_position(node._parent)

    def left(self, p=None):
        """
        Return Position representing p's left (or None if p is root)
        """
        node = self._validate(p) if p is not None else self._root
        return self._make_position(node._left)

    def right(self, p=None):
        """
        Return Position representing p's right (or None if p is root)
        """
        node = self._validate(p) if p is not None else self._root
        return self._make_position(node._right)

    def num_children(self, p=None):
        """
        Return the number of children of Position p
        """
        node = self._validate(p) if p is not None else self._root
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def add_root(self, e):
        """
        Place element e at the root of an empty tree and return new Position
        """
        if self._root is not None:
            raise ValueError("root exists")
        self._size += 1  # in order to detect the size error
        self._root = self._Node(e)
        return self._make_position(self._root)

    def add_left(self, e, p=None):
        """
        Create a new left child for Position p, storing element e
        """
        node = self._validate(p) if p is not None else self._root
        if node._left is not None:
            raise ValueError("left child exists")
        self._size += 1
        node._left = self._Node(e)
        node._left._parent = node
        return self._make_position(node._left)

    def add_right(self, e, p=None):
        """
        Create a new right child for Position p, storing element e
        """
        node = self._validate(p) if p is not None else self._root
        if node._right is not None:
            raise ValueError("right child exists")
        self._size += 1
        node._right = self._Node(e)
        node._right._parent = node
        return self._make_position(node._right)

    def replace(self, e, p=None):
        """
        Replace the element at position p with e, and return old element
        """
        node = self._validate(p) if p is not None else self._root
        old = node._element
        node._element = e
        return old

    def delete(self, p):
        """
        Delete the node at Position p, and replace it with its child, if any

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            # child's grandparent becomes parent
            child._parent = node._parent
        if node is self._root:
            self._root = child  # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node  # deprecated this node
        return node._element

    def attach(self, p, lt, rt):
        """
        Attach trees lt as left and rt as right subtrees of external p
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("p must be a leaf")
        if not type(self) is type(lt) is type(rt):
            # all 3 trees must be same type
            raise TypeError('trees type must match')
        self._size += len(lt) + len(rt)
        # attach lt as left subtree
        if not lt.is_empty():
            lt._root._parent = node
            node._left = lt._root
        if not rt.is_empty():
            rt._root._parent = node
            node._right = rt._root

    def _make_position(self, node):
        """
        Return Position instance for given node (or None if no node)
        """
        return self.Position(self, node) if node is not None else None

    def _validate(self, p):
        # Return associated node, if position is valid
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node


def _main():
    t = LinkedBinaryTree()
    """
            0
          /    \\
         1      2
        / \\   /  \\
       3   4   5   6
    """
    root = t.add_root(0)
    left = t.add_left(1)
    print(t.add_left(3, left))
    print(t.add_right(4, left))
    right = root.add_right(2)
    print(right.add_left(5))
    print(right.add_right(6))
    print(root)
    print(left)
    print(right)
    print(f"height = {t.height()}")
    print(f"lenght = {len(t)}")
    print('pre order:')
    print(" ".join(repr(v.element()) for v in t.preorder()))
    print('post order:')
    print(" ".join(repr(v.element()) for v in t.postorder()))
    print('in order:')
    print(" ".join(repr(v.element()) for v in t.inorder()))


if __name__ == "__main__":
    _main()
