_created = "2020-04-21"


class Queue:
    """
    Queue implementation using a singly linked list for storage
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
        self._tail = None
        # the length of empty stack is 0
        self._length = 0

    # String representation/visualization of a Queue
    def __repr__(self):
        current = self._head._next
        string_repr = "FRONT -> "
        while current:
            string_repr += f"<{current} {current._next}> "
            current = current._next
        return string_repr + "TAIL"

    # The length of the stack
    def __len__(self):
        return self._length

    # whether the stack is empty
    def is_empty(self):
        return not bool(self._length)

    def enqueue(self, item):
        """ Append the item to the rear """
        new_node = self._Node(item)
        # operate on the head pointer for the 1st element. then always on tail.
        if self.is_empty():
            self._head._next = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._length += 1

    def dequeue(self):
        """Dequeue always pops the 1st item from the front"""
        if self.is_empty():
            raise QueueEmptyError("pop from an empty queue")
        temp = self._head._next
        self._head._next = temp._next
        self._length -= 1
        # specific logic if there is only 1 element
        if self.is_empty():
            self._tail = None
        return temp

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise QueueEmptyError("queue is empty")
        temp = self._head._next
        return temp

    def size(self):
        """ Return the size of the queue. """
        return self._length


class QueueEmptyError(BaseException):
    pass


def _main_queue():
    queue = Queue()
    for i in range(10):
        queue.enqueue(i)

    # operate on the queue
    print("Queue demonstration:\n")
    print("Initial queue: " + str(queue))
    print("dequeue(): " + str(queue.dequeue()))
    print("After dequeue(), the queue is now: " + str(queue))
    print("first(): " + str(queue.first()))
    queue.enqueue(100)
    print("After enqueue(100), the queue is now: " + str(queue))
    print("is_empty(): " + str(queue.is_empty()))
    print("size(): " + str(queue.size()))


if __name__ == "__main__":
    _main_queue()
