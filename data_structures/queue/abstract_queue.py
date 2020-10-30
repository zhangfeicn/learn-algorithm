"""
Abstract base class to represent queues
"""

_created = "2020-04-22"


class QueueBase:

    def __len__(self):
        """
        Return the number of elements in the queue.
        """
        raise NotImplementedError("must be implemented by subclass")

    def is_empty(self):
        """ Check if a queue is empty. """
        return len(self) == 0

    def enqueue(self, item):
        """ Append the item to the rear """
        raise NotImplementedError("must be implemented by subclass")

    def dequeue(self):
        """Dequeue always pops the 1st item from the front"""
        raise NotImplementedError("must be implemented by subclass")

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        raise NotImplementedError("must be implemented by subclass")

    def size(self):
        """ Return the size of the queue. """
        return len(self)
