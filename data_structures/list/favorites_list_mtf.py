"""
Implementing the Move-to-Front Heuristic
"""

from favorites_list import FavoritesList

_created = "2020-04-29"


class FavoritesListMTF(FavoritesList):
    """List of elements ordered with move-to-front heuristic"""

    def _move_up(self, p):
        """Move accessed item at Position p to front of list."""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

    def top(self, k):
        """Generate sequence of top k elements in terms of access count"""
        # this list if not sorted, need to rebuild the method
        pass
