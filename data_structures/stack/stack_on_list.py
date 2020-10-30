"""
A stack is a collection of objects that are inserted and removed according to
the last-in, first-out (LIFO) principle.
"""

_created = "2020-03-28"


class Stack:
    """
    Implementing a stack with a Python list, storing the top element in the
    rightmost cell.

    The Stack ADT(Abstract Data Type)
        Stack() - creates a new stack that is empty.
        s.push(item) - add a new item to the top of the stack S.
        s.pop() - remove the top item from the stack.
        s.peek() - returns the top item from the stack but does not remove it.
        s.is_empty() - test to see whether the stack is empty.
        s.size() - returns the number of items on the stack.
    """

    def __init__(self, limit=100):
        self._items = []
        self._limit = limit

    def __bool__(self):
        """ Return bool(self) """
        return bool(self._items)

    def __str__(self):
        """ Return str(self) """
        return str(self._items)

    def __len__(self):
        """ Return len(self) """
        return len(self._items)

    def is_empty(self):
        """ Check if a stack is empty. """
        return not bool(self._items)

    def push(self, item):
        """ Push an element to the top of the stack. """
        if (self.size() >= self._limit):
            raise StackOverflowError("push to a full stack")
        self._items.append(item)

    def pop(self):
        """ Pop an element off the top of the stack. """
        if self.is_empty():
            raise StackEmptyError("pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """ Peek at the top-most element of the stack. """
        if self.is_empty():
            raise StackEmptyError("stack is empty")
        return self._items[-1]

    def size(self):
        """ Return the size of the stack. """
        return len(self._items)


class StackOverflowError(BaseException):
    pass


class StackEmptyError(BaseException):
    pass


def _main():
    stack = Stack()
    for i in range(10):
        stack.push(i)

    # operate on the stack
    print("Stack demonstration:\n")
    print("Initial stack: " + str(stack))
    print("pop(): " + str(stack.pop()))
    print("After pop(), the stack is now: " + str(stack))
    print("peek(): " + str(stack.peek()))
    stack.push(100)
    print("After push(100), the stack is now: " + str(stack))
    print("is_empty(): " + str(stack.is_empty()))
    print("size(): " + str(stack.size()))


if __name__ == "__main__":
    _main()
