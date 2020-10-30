"""A min-oriented priority queue implemented with a sorted list"""

from abstract_priority_queue import PriorityQueueBase
from data_structures.list.positional_list import PositionalList

_created = "2020-05-03"


class SortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, k, v):
        # insert the new node to the right position
        new_item = self._Item(k, v)
        walk = self._data.last()  # walk backward looking for smaller key
        while walk is not None and new_item < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(new_item)  # new key is smallest
        else:
            self._data.add_after(walk, new_item)  # newest goes after walk

    def min(self):
        if self.is_empty():
            raise ValueError('priority queue is empty')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError('priority queue is empty')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)


def _main():
    print("Unsorted Priority Queue Operations:\n")
    pq = SortedPriorityQueue()
    pq.add(5, 'A')
    pq.add(9, 'C')
    pq.add(3, 'B')
    print("Removed minimum item:", pq.remove_min())
    print("Next minimum item:", pq.min())
    print("Priority Queue length:", len(pq))


if __name__ == "__main__":
    _main()
