from data_structures.queue.abstract_priority_queue import PriorityQueueBase

_created = "2020-05-04"


class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap"""
    def __init__(self):
        self._data = []  # Array Based

    def __len__(self):
        return len(self._data)

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self)

    def _has_right(self, j):
        return self._right(j) < len(self)

    def _swap(self, i, j):
        # swap the data at indices i and j
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)  # recur at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def add(self, k, v):
        self._data.append(self._Item(k, v))
        self._upheap(len(self) - 1)

    def min(self):
        if self.is_empty():
            raise ValueError('priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError('priority queue is empty')
        self._swap(0, len(self) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)


def _main():
    print("Heap Priority Queue Operations:\n")
    pq = HeapPriorityQueue()
    pq.add(5, 'A')
    pq.add(9, 'C')
    pq.add(3, 'B')
    print("Removed minimum item:", pq.remove_min())
    print("Next minimum item:", pq.min())
    print("Priority Queue length:", len(pq))


if __name__ == "__main__":
    _main()
