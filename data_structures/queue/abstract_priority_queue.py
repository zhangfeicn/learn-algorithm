"""
Abstract base class to represent priority queues
"""

_created = "2020-05-02"


class PriorityQueueBase:
    """Abstract base class for a priority queue"""
    class _Item:
        __slots__ = '_key', '_value'
        """Lightweight composite to store priority queue items"""
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0

    def add(self, key, value):
        """Insert an item with key k and value v into priority queue"""
        raise NotImplementedError("must be implemented by subclass")

    def min(self):
        """Return a tuple, (k,v), representing the key and value of an
        item in priority queue P with minimum key (but do not remove
        the item); an error occurs if the priority queue is empty """
        raise NotImplementedError("must be implemented by subclass")

    def remove_min(self):
        """Remove an item with minimum key from priority queue P,
        and return a tuple, (k,v), representing the key and value of the
        removed item; an error occurs if the priority queue is empty. """
        raise NotImplementedError("must be implemented by subclass")
