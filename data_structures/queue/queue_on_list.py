"""
Queue is a collection of objects that are inserted and removed according to the
first-in, first-out (FIFO) principle.
"""

_created = "2020-03-28"


class Queue:
    """
    Implementing a queue with a Python list. The front element is at index 0

    The Queue ADT(Abstract Data Type)
        Queue() - creates a new queue that is empty.
        q.enqueue(item) - Add element e to the back of queue.
        q.dequeue() - Remove and return the first element from queue
        q.first() - Return a reference to the element at the front of queue
        q.is_empty() - Return True if queue Q does not contain any elements.
        q.size() - returns the number of items on the queue.
    """

    def __init__(self):
        self._items = []

    def __bool__(self):
        """ Return bool(self) """
        return bool(self._items)

    def __str__(self):
        """ Return str(self) """
        return "<" + str(self._items)[1:-1] + ">"  # strip away '[' ']'

    def __len__(self):
        """ Return len(self) """
        return len(self._items)

    def is_empty(self):
        """ Check if a queue is empty. """
        return not bool(self._items)

    def enqueue(self, item):
        """ Append the item to the rear """
        self._items.append(item)

    def dequeue(self):
        """Dequeue always pops the 1st item from the front"""
        if self.is_empty():
            raise QueueEmptyError("pop from an empty queue")
        return self._items.pop(0)

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise QueueEmptyError("queue is empty")
        return self._items[0]

    def size(self):
        """ Return the size of the queue. """
        return len(self._items)


"""
Double-Ended Queue - is an ordered collection of items similar to the queue.
It has two ends, a front and a rear, and the items remain positioned in the
collection. In a sense, this hybrid linear structure provides all the
capabilities of stacks and queues in a single data structure.

An implementation of a deque class is available in Python’s standard
collections module.

collections.deque - list-like container with fast appends and pops on either
end
"""


class Deque:
    """
    The Deque ADT(Abstract Data Type)
        Deque() - creates a new deque that is empty.
        dq.add_front(item) - Add element to the front of deque
        dq.add_rear(item) - Add element to the rear of deque
        dq.remove_front() -  Remove and return the first element from deque
        dq.remove_rear() -  Remove and return the last element from deque
        dq.is_empty() - Return True if deque D does not contain any elem
        dq.first() - Return (but do not remove) the first element of deque
        dq.last() - Return (but do not remove) the last element of deque
        size() - returns the number of items on the queue.
    """

    def __init__(self):
        self._items = []

    def __bool__(self):
        """ Return bool(self) """
        return bool(self._items)

    def __str__(self):
        """ Return str(self) """
        return "<" + str(self._items)[1:-1] + ">"

    def __len__(self):
        """ Return len(self) """
        return len(self._items)

    def is_empty(self):
        """ Check if a de-queue is empty. """
        return not bool(self._items)

    def add_front(self, item):
        """ Append the item to the front"""
        self._items.insert(0, item)

    def add_rear(self, item):
        """ Append the item to the rear"""
        self._items.append(item)

    def remove_front(self):
        """ Pop the 1st item from the front"""
        if self.is_empty():
            raise QueueEmptyError("pop from an empty de-queue")
        return self._items.pop(0)

    def remove_rear(self):
        """ Pop the 1st item from the rear"""
        if self.is_empty():
            raise QueueEmptyError("pop from an empty de-queue")
        return self._items.pop()

    def first(self):
        """ Return (but do not remove) the first element of deque"""
        if self.is_empty():
            raise QueueEmptyError("de-queue is empty")
        return self._items[0]

    def last(self):
        """ Return (but do not remove) the last element of deque"""
        if self.is_empty():
            raise QueueEmptyError("de-queue is empty")
        return self._items[-1]

    def size(self):
        """ Return the size of the deque. """
        return len(self._items)


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


def _main_deque():
    dequeue = Deque()
    for i in range(10):
        dequeue.add_rear(i)

    # operate on the queue
    print("De-Queue demonstration:\n")
    print("Initial de-queue: " + str(dequeue))
    print("remove_front(): " + str(dequeue.remove_front()))
    print("remove_last(): " + str(dequeue.remove_rear()))
    print(
        "After remove_front() and remove_last(), the de-queue is now: ",
        str(dequeue))
    print("first(): " + str(dequeue.first()))
    print("last(): " + str(dequeue.last()))
    dequeue.add_front(0)
    print("After add_front(0), the de-queue is now: " + str(dequeue))
    dequeue.add_rear(9)
    print("After add_rear(9), the de-queue is now: " + str(dequeue))
    print("is_empty(): " + str(dequeue.is_empty()))
    print("size(): " + str(dequeue.size()))


if __name__ == "__main__":
    _main_queue()
    _main_deque()
