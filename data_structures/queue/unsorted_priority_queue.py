"""A min-oriented priority queue implemented with an unsorted list"""

from abstract_priority_queue import PriorityQueueBase
from data_structures.list.positional_list import PositionalList

_created = "2020-05-03"


class UnsortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, k, v):
        self._data.add_last(self._Item(k, v))

    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)

    def _find_min(self):
        """Return Position of item with minimum key"""
        if self.is_empty():
            raise ValueError('priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        # traversal the list
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small


def _main():
    print("Unsorted Priority Queue Operations:\n")
    pq = UnsortedPriorityQueue()
    pq.add(5, 'A')
    pq.add(9, 'C')
    pq.add(3, 'B')
    print("Removed minimum item:", pq.remove_min())
    print("Next minimum item:", pq.min())
    print("Priority Queue length:", len(pq))


if __name__ == "__main__":
    _main()
