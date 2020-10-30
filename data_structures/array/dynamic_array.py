"""
Dynamic Array
"""

import ctypes  # provides low-level arrays ctypes.py_object

_created = "2020-04-15"


class DynamicArray():
    def __init__(self):
        """
        create an empty array
        """
        self._n = 0         # count actual elements
        self._capacity = 1  # default array capacity
        self._items = self._make_array(self._capacity)

    def __len__(self):
        """
        return the number of items in the array
        """
        return self._n

    def __getitem__(self, i):
        # to support negative index
        if i >= self._n or i < -self._n:
            raise IndexError("invalid index")
        if i < 0:
            i = self._n + i
        return self._items[i]

    def __setitem__(self, i, value):
        if i >= self._n or i < -self._n:
            raise IndexError("invalid index")
        if i < 0:
            i = self._n + i
        self._items[i] = value

    def __repr__(self):
        return '['+', '.join(repr(v) for v in self)+']'

    def __iter__(self):
        for i in range(self._n):
            yield self._items[i]

    def append(self, value):
        if self._n == self._capacity:
            # increase the capacity
            self._resize(2 * self._capacity)
        self._items[self._n] = value
        self._n += 1

    def insert(self, i, value):
        '''
        insert operation can be optimized by shifting elements into their
        final position during resizing.
        '''
        if not 0 <= i <= self._n:
            raise IndexError("invalid index")
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        # shift rightmost element
        for k in range(self._n, i, -1):
            self._items[k] = self._items[k - 1]
        self._items[i] = value
        self._n += 1

    def remove(self, value):
        for i in range(self._n):
            if self._items[i] == value:
                # shift others to fill the gap
                for j in range(i, self._n - 1):
                    self._items[j] = self._items[j + 1]
                self._items[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError("value not found")

    def remove_all(self, value):
        '''
        invoke remove(value) isn't efficient
        '''
        raise Exception('method will be implemented soon')

    def pop(self, pos=None):
        '''
        pop operation can be optimized by shrinking the capacity.
        '''
        if self._n == 0:
            raise IndexError('empty array')
        value = self._items[self._n - 1]
        self._items[self._n - 1] = None
        self._n -= 1
        return value

    def is_empty(self):
        return not bool(self._n)

    def index(self, value):
        for i in range(self._n):
            if self._items[i] == value:
                return i
        raise ValueError('value not found')

    def sort(self):
        self._insert_sort()

    def _resize(self, size):
        new_array = self._make_array(size)
        for i in range(self._n):
            new_array[i] = self._items[i]
        self._items = new_array
        self._capacity = size

    def _make_array(self, size):
        return (size * ctypes.py_object)()

    def _insert_sort(self):
        for i in range(1, self._n):
            j = i
            cur = self._items[i]
            # find the correct index for current within 0 to j
            while j > 0 and self._items[j-1] > cur:
                self._items[j] = self._items[j - 1]
                j -= 1
            self._items[j] = cur


def _main(n: int):
    print('Dynamic Array Demonstration:')
    data = DynamicArray()
    for i in range(10):
        data.append(i*i)
    print("Initial array: ", data)
    print("The length is:", len(data))
    data.insert(0, 10)
    print("After insert 10 to the front:", data)
    data.insert(4, 10)
    print("After insert 9 to the 4:", data)
    print("The length is:", len(data))
    print("Pop from the tail:", data.pop())
    print("After pop from tail:", data)
    print("The length is:", len(data))
    data.remove(10)
    print("After remove 10:", data)
    print("The index of 4 is:", data.index(4))
    print("The length is:", len(data))
    print("isEmpty:", data.is_empty())
    data[0] = 3
    print("Change data[0] to '3':", data)
    print("data[1]=", data[1])
    data.sort()
    print('After sort:', data)


if __name__ == "__main__":
    _main(10)
