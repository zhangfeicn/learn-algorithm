"""
A list is a collection of items where each item holds a relative position with
respect to the others. \n
"""

_created = "2020-04-03"


# Singly Linked List
class SLinkedList:
    """
    The List ADT(Abstract Data Type)
        List() - creates a new list that is empty.
        append(item) - adds a new item to the end of the list.
        is_empty() - tests to see whether the list is empty.
        pop() - removes and returns the last item in the list.
        pop(pos) - removes and returns the item at position pos.
        reverse() - reverse the items in the linked list
        insert(pos, item) - adds a new item to the list at position pos.
        remove(item) - removes the item from the list.
        index(item) - returns the position of item in the list.
    Used head node to simplify the operation on 1st node.
    Otherwise, need special logic when operation on 1st node
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
        # the length of empty list is 0
        self._length = 0

    # Indexing Support. Used to get a node at particular position
    def __getitem__(self, index):
        current = self._head._next
        # If LinkedList is empty
        if current is None:
            raise IndexError("The Linked List is Empty")

        if index > self._length - 1:
            raise IndexError("Index out of range.")
        # moving index
        for _ in range(index):
            current = current._next

        return current

    # Used to change the data of a particular node
    def __setitem__(self, index, data):
        current = self._head._next
        # If LinkedList is empty
        if current is None:
            raise IndexError("The Linked List is Empty")

        # If the LinkedList ends before reaching specified node
        if index > self._length - 1:
            raise IndexError("Index out of range.")
        # moving index
        for _ in range(index):
            current = current._next
        current._data = data

    # String representation/visualization of a Linked Lists
    def __repr__(self):
        current = self._head._next
        string_repr = "START -> "
        while current:
            string_repr += f"<{current} {current._next}> "
            current = current._next
        return string_repr + "END"

    # The length of the linked list
    def __len__(self):
        return self._length

    # insert item to the position pos in the linked list
    def insert(self, pos, item):
        current = self._head

        # moving index before pos
        for _ in range(pos):
            # If the LinkedList ends before reaching specified node
            if current._next is None:
                raise IndexError("Index out of range.")
            current = current._next

        new_node = self._Node(item)
        # pointer changes. new.next = cur.next, cur.next = new
        new_node._next = current._next
        current._next = new_node
        # increase the length
        self._length += 1

    # add item to the end of the linked list
    def append(self, item):
        new_node = self._Node(item)
        current = self._head
        # traverse the list to the end
        while current._next:
            current = current._next
        current._next = new_node
        # increase the length of the linked list
        self._length += 1

    # whether the linked list is empty
    def is_empty(self):
        return not bool(self._length)

    # pop the element in pos from the linked list
    def pop(self, pos=None):
        current = self._head
        # If LinkedList is empty
        if current._next is None:
            raise IndexError("The Linked List is Empty")

        # pop the last item
        if pos is None:
            pos = self._length - 1
        # moving index before pos
        for _ in range(pos):
            # If the LinkedList ends before reaching specified node
            if current._next is None:
                raise IndexError("Index out of range.")
            current = current._next

        # pointer changes. pop item is the current item's next
        temp = current._next
        current._next = temp._next
        self._length -= 1
        return temp

    # reverse the element in the linked list
    def reverse(self):
        prev_node = None
        current = self._head._next

        while current:
            # store the current node's next node
            next_node = current._next
            # Make the current node's next point backwards
            current._next = prev_node
            # Make the previous node be the current node
            prev_node = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self._head._next = prev_node

    # remove item from the linked list
    def remove(self, item):
        # logic is same as index
        current = self._head._next
        previous = self._head
        while current:
            if current._data == item:
                # change the pointer
                previous._next = current._next
                self._length -= 1
                break
            else:
                previous = current
                current = current._next
        else:
            raise ValueError(f"{item} is not in list")

    # get the index of item in linked list
    def index(self, item):
        current = self._head._next
        position = 0
        while current:
            if current._data == item:
                return position
            else:
                current = current._next
                position += 1
        else:
            return - 1
            # return -1 instead of raising error
            # return ValueError(f"{item} is not in list")


# Doubly Linked List
class DLinkedList(SLinkedList):
    """
    A Doubly Linked List (DLL) contains an extra pointer, typically called
    previous pointer, together with next pointer and data which are there
    in singly linked list.
    It can be traversed in both forward and backward direction
    Delete operation is more efficient
    """
    class _Node(SLinkedList._Node):
        __slots__ = "_previous"

        """ create a node """
        def __init__(self, data=None):
            super().__init__(data)
            self._previous = None

    # initialize head and point to an empty node
    def __init__(self, header=None):
        super().__init__(header)

    # String representation/visualization of a Linked Lists
    def __repr__(self):
        current = self._head._next
        string_repr = "START -> "
        while current:
            string_repr += f"<{current._previous} {current} {current._next}> "
            current = current._next
        return string_repr + "END"

    # insert item to the position pos in the linked list
    def insert(self, pos, item):
        current = self._head

        # moving index before pos
        for _ in range(pos):
            # If the LinkedList ends before reaching specified node
            if current._next is None:
                raise IndexError("Index out of range.")
            current = current._next

        new_node = self._Node(item)
        # next of new node as the next of current node
        new_node._next = current._next
        # next of current node as new node
        current._next = new_node
        # previous of new node as current node
        new_node._previous = current
        # change previous of current node's next to current
        if new_node._next is not None:
            new_node._next._previous = new_node
        # increase the length
        self._length += 1

    # add item to the end of the linked list
    def append(self, item):
        new_node = self._Node(item)
        current = self._head
        # traverse the list to the end
        while current._next:
            current = current._next
        current._next = new_node
        new_node._previous = current
        # increase the length of the linked list
        self._length += 1

    # pop the element in pos from the linked list
    def pop(self, pos=None):
        current = self._head
        # If LinkedList is empty
        if current._next is None:
            raise IndexError("The Linked List is Empty")

        # pop the last item
        if pos is None:
            pos = self._length - 1
        # moving index before pos
        for _ in range(pos):
            # If the LinkedList ends before reaching specified node
            if current._next is None:
                raise IndexError("Index out of range.")
            current = current._next

        # pointer changes. pop item is the current item's next
        temp = current._next
        current._next = temp._next
        if temp._next is not None:
            temp._next._previous = current
        self._length -= 1
        return temp

    # remove item from the linked list
    def remove(self, item):
        # logic is same as index
        current = self._head._next
        previous = self._head
        while current:
            if current._data == item:
                # change the pointer
                previous._next = current._next
                if current._next is not None:
                    current._next._previous = previous
                self._length -= 1
                break
            else:
                previous = current
                current = current._next
        else:
            raise ValueError(f"{item} is not in list")

    # reverse the element in the linked list
    def reverse(self):
        current = self._head._next
        prev_node = None
        while current:
            # store the current node's next node
            next_node = current._next
            # Make the current node's next point backwards
            current._next = prev_node
            current._previous = next_node
            # Make the previous node be the current node
            prev_node = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        # move the head to the last node
        self._head._next = prev_node
        prev_node._previous = self._head


# Circular Singly Linked List
class CSLinkedList(SLinkedList):
    """
    Class to represent the Circular Singly LinkedList.
    Circular linked list is a linked list where all nodes are connected
    to form a circle.
    """
    # initialize head and point to an empty node
    def __init__(self, header=None):
        super().__init__(header)
        # set tail pointer
        self._head._next = self._head

    # String representation/visualization of a Linked Lists
    def __repr__(self):
        current = self._head._next
        string_repr = "START -> "
        while current is not self._head:
            string_repr += f"<{current} {current._next}> "
            current = current._next
        return string_repr + "END"

    # insert item to the position pos in the linked list
    def insert(self, pos, item):
        current = self._head

        # moving index before pos
        for _ in range(pos):
            # If the LinkedList ends before reaching specified node
            if current._next is self._head:
                raise IndexError("Index out of range.")
            current = current._next

        new_node = self._Node(item)
        # pointer changes. new.next = cur.next, cur.next = new
        new_node._next = current._next
        current._next = new_node
        # increase the length
        self._length += 1

    # add item to the end of the linked list
    def append(self, item):
        new_node = self._Node(item)
        current = self._head
        # traverse the list to the end
        while current._next is not self._head:
            current = current._next
        current._next = new_node
        new_node._next = self._head
        # increase the length of the linked list
        self._length += 1

    # pop the element in pos from the linked list
    def pop(self, pos=None):
        current = self._head
        # If LinkedList is empty
        if current._next is self._head:
            raise IndexError("The Linked List is Empty")

        # pop the last item
        if pos is None:
            pos = self._length - 1
        # moving index before pos
        for _ in range(pos):
            # If the LinkedList ends before reaching specified node
            if current._next is self._head:
                raise IndexError("Index out of range.")
            current = current._next

        # pointer changes. pop item is the current item's next
        temp = current._next
        current._next = temp._next
        self._length -= 1
        return temp

    # reverse the element in the linked list
    def reverse(self):
        prev_node = self._head
        current = self._head._next

        while current is not self._head:
            # store the current node's next node
            next_node = current._next
            # Make the current node's next point backwards
            current._next = prev_node
            # Make the previous node be the current node
            prev_node = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self._head._next = prev_node

    # remove item from the linked list
    def remove(self, item):
        # logic is same as index
        current = self._head._next
        previous = self._head
        while current is not self._head:
            if current._data == item:
                # change the pointer
                previous._next = current._next
                self._length -= 1
                break
            else:
                previous = current
                current = current._next
        else:
            raise ValueError(f"{item} is not in list")

    # get the index of item in linked list
    def index(self, item):
        current = self._head._next
        position = 0
        while current is not self._head:
            if current._data == item:
                return position
            else:
                current = current._next
                position += 1
        else:
            return - 1
            # return -1 instead of raising error
            # return ValueError(f"{item} is not in list")


# Circular Doubly Linked List
class CDLinkedList(SLinkedList):

    class _Node(SLinkedList._Node):
        __slots__ = "_previous"

        """ create a node """
        def __init__(self, data=None):
            super().__init__(data)
            self._previous = None

    # initialize head and point to an empty node
    def __init__(self, header=None):
        super().__init__(header)
        self._head._next = self._head

    def __repr__(self):
        current = self._head._next
        string_repr = "START -> "
        while current is not self._head:
            string_repr += f"<{current._previous} {current} {current._next}> "
            current = current._next
        return string_repr + "END"

    # insert item to the position pos in the linked list
    def insert(self, pos, item):
        current = self._head

        # moving index before pos
        for _ in range(pos):
            # If the LinkedList ends before reaching specified node
            if current._next is self._head:
                raise IndexError("Index out of range.")
            current = current._next

        new_node = self._Node(item)
        # next of new node as the next of current node
        new_node._next = current._next
        # next of current node as new node
        current._next = new_node
        # previous of new node as current node
        new_node._previous = current
        # change previous of current node's next to current
        if new_node._next is not self._head:
            new_node._next._previous = new_node
        # increase the length
        self._length += 1

    # add item to the end of the linked list
    def append(self, item):
        new_node = self._Node(item)
        current = self._head
        print(current._previous, current, current._next)
        # traverse the list to the end
        while current._next is not self._head:
            current = current._next
        current._next = new_node
        new_node._previous = current
        new_node._next = self._head
        # increase the length of the linked list
        self._length += 1

    # pop the element in pos from the linked list
    def pop(self, pos=None):
        current = self._head
        # If LinkedList is empty
        if current._next is self._head:
            raise IndexError("The Linked List is Empty")

        # pop the last item
        if pos is None:
            pos = self._length - 1
        # moving index before pos
        for _ in range(pos):
            # If the LinkedList ends before reaching specified node
            if current._next is self._head:
                raise IndexError("Index out of range.")
            current = current._next

        # pointer changes. pop item is the current item's next
        temp = current._next
        current._next = temp._next
        if temp._next is not self._head:
            temp._next._previous = current
        self._length -= 1
        return temp

    # reverse the element in the linked list
    def reverse(self):
        current = self._head._next
        prev_node = self._head
        while current is not self._head:
            # store the current node's next node
            next_node = current._next
            # Make the current node's next point backwards
            current._next = prev_node
            current._previous = next_node
            # Make the previous node be the current node
            prev_node = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        # move the head to the last node
        self._head._next = prev_node
        prev_node._previous = self._head

    # remove item from the linked list
    def remove(self, item):
        # logic is same as index
        current = self._head._next
        previous = self._head
        while current is not self._head:
            if current._data == item:
                # change the pointer
                previous._next = current._next
                if current._next is not None:
                    current._next._previous = previous
                self._length -= 1
                break
            else:
                previous = current
                current = current._next
        else:
            raise ValueError(f"{item} is not in list")

    # get the index of item in linked list
    def index(self, item):
        current = self._head._next
        position = 0
        while current is not self._head:
            if current._data == item:
                return position
            else:
                current = current._next
                position += 1
        else:
            return - 1


def _main_linked_list(s):
    for i in range(5):
        s.append(i)
    # operate on the queue
    print("Linked List Demonstration:\n")
    print("Initial list: ", s)
    print("The length is:", len(s))
    s.insert(0, 10)
    print("After insert 10 to the front:", s)
    s.insert(4, 9)
    print("After insert 9 to the 4:", s)
    print("The length is:", len(s))
    print("Pop from the tail:", s.pop())
    print("After pop from tail:", s)
    print("Pop from the front:", s.pop(0))
    print("After pop from front:", s)
    print("The length is:", len(s))
    s.remove(3)
    print("After remove 3:", s)
    s.remove(1)
    print("After remove 1:", s)
    print("The index of 2 is:", s.index(2))
    print("The length is:", len(s))
    print("isEmpty:", s.is_empty())
    s[0] = 3
    print('Change s[0] to 3', s)
    print("s[1]=", s[1])
    s.reverse()
    print("After reverse", s)


if __name__ == "__main__":
    _main_linked_list(SLinkedList("HEAD"))
    _main_linked_list(DLinkedList("HEAD"))
    _main_linked_list(CSLinkedList("HEAD"))
    _main_linked_list(CDLinkedList("HEAD"))
