from positional_list import PositionalList

_created = "2020-04-28"

"""
Use positional_list as storage to implement a favourite list
"""


class FavoritesList:
    """
    List of elements ordered from most frequently accessed to least
    """
    class _Item:

        __slots__ = '_value', '_count'

        def __init__(self, e):
            self._value = e
            self._count = 0

        def __repr__(self):
            return f"value={self._value}, count={self._count}"

    def __init__(self):
        """Create an empty list of favorites"""
        # will be list of Item instances
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        """
        Access element e, thereby increasing its access count
        """
        # locate position of e
        p = self._find_position(e)

        if p is None:
            # place at the end if new
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        # consider moving forward
        self._move_up(p)

    def remove(self, e):
        """
        Remove element e from the list of favorites
        """
        # locate position of e
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        """
        Generate sequence of top k elements in terms of access count
        """
        if not 1 <= k <= len(self):
            raise ValueError(f"Illegal value for k={k}")
        walk = self._data.first()
        for _ in range(k):
            item = walk.element()
            yield item
            walk = self._data.after(walk)

    def _find_position(self, e):
        """
        Search for element e and return its Position (or None if not found)
        """
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """
        Move item at Position p earlier in the list based on access count
        """
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                # shift forward
                while (walk != self._data.first() and
                       cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))


def _main():
    pl = FavoritesList()
    for i in range(30):
        pl.access(i % 4)
    print("Favorites List Demonstration:\n")
    print(pl._data)
    for e in pl.top(3):
        print(e)


if __name__ == "__main__":
    _main()
