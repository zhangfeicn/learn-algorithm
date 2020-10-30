"""Using two sentinel nodes - header and trailer. The use of sentinel nodes
would eliminate the special operation on boundaries. """

_created = "2020-04-22"


class Deque:
    class _Node:
        __slots__ = "_data", "_next", "_previous"

        """ create a node """
        def __init__(self, data=None):
            self._data = data
            self._next = None
            self._previous = None

        # string representation of a Node
        def __repr__(self):
            return f"Node({self._data})"

    def __init__(self):
        self._header = self._Node()
        self._trailer = self._Node()
        self._header._next = self._trailer
        self._trailer._previous = self._header
        self._length = 0

    # String representation/visualization of a Deque
    def __repr__(self):
        # 1st element
        current = self._header._next
        string_repr = "FRONT -> "
        # if trailer, current._next is None
        while current._next:
            string_repr += f"<{current._previous} {current} {current._next}> "
            current = current._next
        return string_repr + "TAIL"

    def __bool__(self):
        """ Return bool(self) """
        return bool(self._length)

    def __len__(self):
        """ Return len(self) """
        return len(self._length)

    def is_empty(self):
        """ Check if a de-queue is empty. """
        return not bool(self._length)

    def add_front(self, item):
        """ Append the item to the front"""
        new_node = self._Node(item)
        new_node._next = self._header._next
        new_node._previous = self._header
        new_node._next._previous = new_node
        self._header._next = new_node
        self._length += 1

    def add_rear(self, item):
        """ Append the item to the rear"""
        new_node = self._Node(item)
        new_node._next = self._trailer
        new_node._previous = self._trailer._previous
        new_node._previous._next = new_node
        self._trailer._previous = new_node
        self._length += 1

    def remove_front(self):
        """ Pop the 1st item from the front"""
        if self.is_empty():
            raise QueueEmptyError("pop from an empty de-queue")
        temp = self._header._next
        # update the pointers
        self._header._next = temp._next
        temp._next._previous = self._header
        self._length -= 1
        # deprecate the temp node
        temp._next = temp._previous = None
        return temp

    def remove_rear(self):
        """ Pop the 1st item from the rear"""
        if self.is_empty():
            raise QueueEmptyError("pop from an empty de-queue")
        temp = self._trailer._previous
        # update the pointers
        temp._previous._next = self._trailer
        self._trailer._previous = temp._previous
        self._length -= 1
        # deprecate the temp node
        temp._next = temp._previous = None
        return temp

    def first(self):
        """ Return (but do not remove) the first element of deque"""
        if self.is_empty():
            raise QueueEmptyError("de-queue is empty")
        return self._header._next

    def last(self):
        """ Return (but do not remove) the last element of deque"""
        if self.is_empty():
            raise QueueEmptyError("de-queue is empty")
        return self._trailer._previous

    def size(self):
        """ Return the size of the deque. """
        return self._length


class QueueEmptyError(BaseException):
    pass


def _main_deque():
    dequeue = Deque()
    for i in range(10):
        dequeue.add_rear(i)

    # operate on the queue
    print("De-Queue demonstration:\n")
    print("Initial de-queue: ", dequeue)
    print("remove_front(): ", dequeue.remove_front())
    print("remove_last(): ", dequeue.remove_rear())
    print(
        "After remove_front() and remove_last(), the de-queue is now: ",
        dequeue)
    print("first(): ", dequeue.first())
    print("last(): ", dequeue.last())
    dequeue.add_front(0)
    print("After add_front(0), the de-queue is now: ", dequeue)
    dequeue.add_rear(9)
    print("After add_rear(9), the de-queue is now: ", dequeue)
    print("is_empty(): ", dequeue.is_empty())
    print("size(): ", dequeue.size())


if __name__ == "__main__":
    _main_deque()
