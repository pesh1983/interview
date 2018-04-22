"""Doubly linked list."""


class Node(object):
    """Node for a doubly linked list."""

    __slots__ = ('object', 'next', 'prev')

    def __init__(self, obj):
        """Initialize a node.

        :param obj: Object to be stored in a node.
        """
        self.object = obj
        self.next = None
        self.prev = None


class DoublyLinkedList(object):
    """Doubly linked list.

    It implements a linked data structure that consists of a set of
    sequentially linked records called nodes. Each node contains two fields,
    called links, that are references to the previous and to the next node
    in the sequence of nodes
    (see https://en.wikipedia.org/wiki/Doubly_linked_list).
    """

    __slots__ = ('_first_node', '_last_node')

    def __init__(self):
        """Initialize a list."""
        super(DoublyLinkedList, self).__init__()

        self._first_node = None
        self._last_node = None

    @property
    def first_node(self):
        """Get the first node in the list."""
        return self._first_node

    @property
    def last_node(self):
        """Get the last node in the list."""
        return self._last_node

    def insert_beginning(self, new_node):
        """Insert new node at the beginning of the list.

        :param new_node: New node to be inserted.
        """
        if self._first_node is None:
            self._first_node = new_node
            self._last_node = new_node
            new_node.prev = None
            new_node.next = None
        else:
            self.insert_before(self._first_node, new_node)

    def insert_end(self, new_node):
        """Insert new node at the end of the list.

        :param new_node: New node to be inserted.
        """
        if self._last_node is None:
            self.insert_beginning(new_node)
        else:
            self.insert_after(self._last_node, new_node)

    def insert_after(self, node, new_node):
        """Insert new node after the given one.

        :param node: A node after which the new one must be inserted.
        :param new_node: New node to be inserted.
        """
        new_node.prev = node
        if node.next is None:
            new_node.next = None
            self._last_node = new_node
        else:
            new_node.next = node.next
            node.next.prev = new_node
        node.next = new_node

    def insert_before(self, node, new_node):
        """Insert new node before the given one.

        :param node: A node before which the new one must be inserted.
        :param new_node: New node to be inserted.
        """
        new_node.next = node
        if node.prev is None:
            new_node.prev = None
            self._first_node = new_node
            new_node.next.prev = new_node
        else:
            new_node.prev = node.prev
            node.prev.next = new_node
        node.prev = new_node

    def remove(self, node):
        """Remove given node from the list.

        :param node: A node that must be removed.
        """
        if node.prev is None:
            self._first_node = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self._last_node = node.prev
        else:
            node.next.prev = node.prev
