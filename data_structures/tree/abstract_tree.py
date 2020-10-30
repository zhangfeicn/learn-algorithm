"""
Abstract base class to represent trees

No update method in the public interface
"""

_created = "2020-04-10"


class Tree:
    """
    Abstract base class representing a tree structure
    """

    class Position:
        """
        An abstraction representing the location of a single element
        """
        def __eq__(self, other):
            """
            Return True if other Position represents the same location
            """
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """
            Return True if other does not represent the same location
            """
            return not (self == other)

        def element(self):
            """
            Return the element stored at this Position.
            """
            raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """
        Return the total number of elements in the tree
        """
        raise NotImplementedError("must be implemented by subclass")

    def __iter__(self):
        """
        Generate an iteration of the tree s elements
        """
        for p in self.positions():
            yield p.element()

    def root(self):
        """
        Return Position representing the tree's root (or None if empty)
        """
        raise NotImplementedError("must be implemented by subclass")

    def is_root(self, p):
        """
        Return True if Position p represents the root of the tree.
        """
        return self.root() == p

    def parent(self, p):
        """
        Return Position representing p's parent (or None if p is root)
        """
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """
        Return the number of children that Position p has.
        """
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """
        Generate an iteration of Positions representing p's children
        """
        raise NotImplementedError("must be implemented by subclass")

    def is_leaf(self, p) -> bool:
        """
        Return True if Position p does not have any children
        """
        return self.num_children(p) == 0

    def is_empty(self) -> bool:
        """
        Return True if the tree is empty
        """
        return len(self) == 0

    def element(self, p):
        """
        Return the element stored at this Position.
        """
        return p.element()

    def depth(self, p) -> int:
        """
        Return the number of levels separating Position p from the root

        Recursion:
            If p is the root, then the depth of p is 0.
            Otherwise, the depth of p is one plus the depth of the parent of p.
        """
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def height(self, p=None) -> int:
        """
        Return the height of the subtree rooted at Position p. -> degree

        Recursion:
            If p is a leaf, then the height of p is 0.
            Otherwise, the height of p is one more than the maximum of the
            heights of p’s children.
        """
        # If p is None, return the height of the entire tree.
        if p is None:
            p = self.root()
        return self._height(p)

    def _height(self, p):
        """
        Return the height of the subtree rooted at Position p.

        The height of a nonempty tree T is equal to the maximum of the depths
        of its leaf positions.
        """
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height(c) for c in self.children(p))

    def positions(self):
        """
        Generate an iteration of the tree's positions
        """
        return self.preorder()

    def preorder(self):
        """
        Generate a preorder iteration of positions in the tree
        """
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """
        Generate a preorder iteration of positions in subtree rooted at p
        """
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        """
        Generate a postorder iteration of positions in the tree
        """
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """
        Generate a postorder iteration of positions in subtree rooted at p
        """
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p


class BinaryTree(Tree):
    """
    Abstract base class representing a binary tree structure
    """
    def left(self, p):
        """
        Return a Position representing p 's left child.

        Return None if p does not have a left child.
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """
        Return a Position representing p's right child.

        Return None if p does not have a right child.
        """
        raise NotImplementedError("must be implemented by subclass")

    def sibling(self, p):
        """
        Return a Position representing p's sibling (or None if no sibling)
        """
        parent = self.parent(p)
        if parent is None:
            return None
        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        """
        Generate an iteration of Positions representing p's children
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """
        Generate an inorder iteration of positions in the tree
        """
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """
        Generate an inorder iteration of positions in subtree rooted at p
        """
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def positions(self):
        """
        Generate an iteration of the tree s positions
        """
        return self.inorder()
