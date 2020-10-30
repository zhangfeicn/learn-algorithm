from data_structures.list.abstract_list import ListBase

_created = "2020-04-23"


class PositionalList(ListBase):
    class _Node:
        __slots__ = "_data", "_next", "_previous"

        """ create a node """
        def __init__(self, data=None, prev=None, next=None):
            self._data = data
            self._previous = prev
            self._next = next

        # string representation of a Node
        def __repr__(self):
            return f"Node({self._data})"

    class Position(ListBase.Position):
        """
        A position maintains a reference to the associated node, and also a
        reference to the list instance that contains the specified node.
        """
        def __init__(self, container, node):
            self._container = container  # the list itself
            self._node = node

        def __eq__(self, other):
            """
            Return True if other is a Position representing the same location
            """
            return type(other) is type(self) and other._node is self._node

        def __repr__(self):
            temp = f"<p={self._node._previous} c={self._node} " \
                f"n={self._node._next}>"
            return temp

        def element(self):
            """
            Return the element stored at this Position
            """
            return self._node._data

    def __init__(self):
        self._header = self._Node()
        self._trailer = self._Node()
        self._header._next = self._trailer
        self._trailer._previous = self._header
        self._length = 0

    def __len__(self):
        return self._length

    def __repr__(self):
        return 'START ->'+' '.join(repr(v) for v in self)+'END'

    def _validate(self, p):
        # Return associated node, if position is valid
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """
        Return Position instance for given node (or None if no node)
        """
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._previous)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._previous)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def _insert_between(self, e, predecessor, successor):
        """
        Add element between existing nodes and return new Position
        """
        new_node = self._Node(e, predecessor, successor)
        predecessor._next = new_node
        successor._previous = new_node
        self._length += 1
        return self._make_position(new_node)

    def _delete_node(self, node):
        """
        Delete nonsentinel node from the list and return its element
        """
        predecessor = node._previous
        successor = node._next
        predecessor._next = successor
        successor._previous = predecessor
        self._length -= 1
        element = node._data
        # deprecate node for recycle
        node._previous = node._next = node._data = None
        return element

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._previous, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._previous, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._data
        original._data = e
        return old_value

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def sort(self):
        """
        sort the list, no return value
        """
        self._insert_sort()

    def _insert_sort(self):
        """
        implementation of insert sort strategy
        """
        if self._length > 1:
            maker = self.first()
            while maker != self.last():
                # check the next element after rightmost of the sorted
                pivot = self.after(maker)
                if pivot.element() > maker.element():
                    maker = pivot
                else:
                    # move pivot to the sorted
                    walk = maker
                    # cannot use is the compare the position as they are all
                    # new instances
                    while (walk != self.first() and
                           self.before(walk).element() > pivot.element()):
                        # move walk to the leftmost which is greater than pivot
                        walk = self.before(walk)
                    else:
                        self.add_before(walk, pivot.element())
                        # implement a method to change the pointers instead of
                        # creating new node
                        self.delete(pivot)


def _main():
    pl = PositionalList()
    for i in range(5):
        pl.add_last(i)
    pl.add_first(9)
    pl.add_first(7)
    pl.add_first(6)
    # operate on the queue
    print("Positional List Demonstration:\n")
    print("Initial list: ", pl)
    print("The length is:", len(pl))
    pl.add_first(10)
    print("After add 10 to the front:", pl)
    pl.sort()
    print("After sort:", pl)


if __name__ == "__main__":
    _main()
