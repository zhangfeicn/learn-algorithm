"""
Abstract base class to represent stacks
"""

_created = "2020-04-22"


class StackBase:
    def __len__(self):
        """ Return len(self) """
        raise NotImplementedError("must be implemented by subclass")

    def is_empty(self):
        """ Check if a stack is empty. """
        return len(self) == 0

    def push(self, item):
        """ Push an element to the top of the stack. """
        raise NotImplementedError("must be implemented by subclass")

    def pop(self):
        """ Pop an element off the top of the stack. """
        raise NotImplementedError("must be implemented by subclass")

    def peek(self):
        """ Peek at the top-most element of the stack. """
        raise NotImplementedError("must be implemented by subclass")

    def size(self):
        """ Return the size of the stack. """
        return len(self)
