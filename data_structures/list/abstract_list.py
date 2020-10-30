"""
Abstract base class to represent lists
"""

_created = "2020-04-22"


# Abstract Data Type - ADT
class ListBase:
    class Position:
        """
        An abstraction representing the location of a single element.
        """
        def __eq__(self, other):
            """
            Return True if other Position represents the same location
            """
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """
            Return True if other does not represent the same location
            """
            return not (self == other)

        def element(self):
            """
            Return the element stored at this Position.
            """
            raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """
        Return the number of elements in the list.
        """
        raise NotImplementedError("must be implemented by subclass")

    def __iter__(self):
        """
        Return a forward iterator for the elements of the list.
        """
        cursor = self.first()
        while cursor is not None:
            yield cursor
            cursor = self.after(cursor)

    def first(self):
        """
        Return the position of the first element of L, or None if L is empty.
        """
        raise NotImplementedError("must be implemented by subclass")

    def last(self):
        """
        Return the position of the last element of L, or None if L is empty.
        """
        raise NotImplementedError("must be implemented by subclass")

    def before(self, p):
        """
        Return the position of L immediately before position p, or None
        if p is the first position.
        """
        raise NotImplementedError("must be implemented by subclass")

    def after(self, p):
        """
        Return the position of L immediately after position p, or None if
        p is the last position.
        """
        raise NotImplementedError("must be implemented by subclass")

    def is_empty(self):
        """
        Return True if list L does not contain any elements.
        """
        return len(self) == 0

    def add_first(self, e):
        """
        Insert a new element e at the front of L, returning the position
        of the new element.
        """
        raise NotImplementedError("must be implemented by subclass")

    def add_last(self, e):
        """
        Insert a new element e at the back of L, returning the position
        of the new element.
        """
        raise NotImplementedError("must be implemented by subclass")

    def add_before(self, p, e):
        """
        Insert a new element e just before position p in L, returning
        the position of the new element.
        """
        raise NotImplementedError("must be implemented by subclass")

    def add_after(self, p, e):
        """
        Insert a new element e just after position p in L, returning
        the position of the new element.
        """
        raise NotImplementedError("must be implemented by subclass")

    def replace(self, p, e):
        """
        Replace the element at position p with element e, returning
        the element formerly at position p.
        """
        raise NotImplementedError("must be implemented by subclass")

    def delete(self, p):
        """
        Remove and return the element at position p in L, invalidating
        the position.
        """
        raise NotImplementedError("must be implemented by subclass")
