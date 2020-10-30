_created = "2020-04-20"


class Stack:
    """
    LIFO Stack implementation using a singly linked list for storage
    """
    class _Node:
        __slots__ = "_data", "_next"

        """ create a node """
        def __init__(self, data=None):
            self._data = data
            self._next = None

        # string representation of a Node
        def __repr__(self):
            return f"Node({self._data})"

    def __init__(self, header=None):
        # initialize head and point to an empty node
        self._head = self._Node(header)
        # the length of empty stack is 0
        self._length = 0

    # String representation/visualization of a Stack
    def __repr__(self):
        current = self._head._next
        string_repr = "TOP -> "
        while current:
            string_repr += f"<{current} {current._next}> "
            current = current._next
        return string_repr + "BOTTOM"

    # The length of the stack
    def __len__(self):
        return self._length

    # whether the stack is empty
    def is_empty(self):
        return not bool(self._length)

    # Add element item to the top of the stack
    def push(self, item):
        new_node = self._Node(item)
        # pointer changes. new.next = cur.next, cur.next = new
        new_node._next = self._head._next
        self._head._next = new_node
        # increase the length
        self._length += 1

    # Remove and return the element from the top of the stack
    def pop(self):
        if self.is_empty():
            raise StackEmptyError("pop from an empty stack")
        temp = self._head._next
        self._head._next = temp._next
        self._length -= 1
        return temp

    # Peek at the top-most element of the stack.
    def peek(self):
        if self.is_empty():
            raise StackEmptyError("pop from an empty stack")
        temp = self._head._next
        return temp

    def size(self):
        """ Return the size of the stack. """
        return self._length


class StackEmptyError(BaseException):
    pass


def _main():
    stack = Stack()
    for i in range(10):
        stack.push(i)

    # operate on the stack
    print("Linked List Stack demonstration:\n")
    print("Initial stack: " + str(stack))
    print("pop(): " + str(stack.pop()))
    print("After pop(), the stack is now: " + str(stack))
    print("peek(): " + str(stack.peek()))
    stack.push(100)
    print("After push(100), the stack is now: " + str(stack))
    print("is_empty(): " + str(stack.is_empty()))
    print("Size(): " + str(stack.size()))


if __name__ == "__main__":
    _main()
