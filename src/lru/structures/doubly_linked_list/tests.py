"""Tests of doubly linked list."""
import unittest

from lru.structures.doubly_linked_list import DoublyLinkedList, Node


class TestDoublyLinkedList(unittest.TestCase):
    """Tests of doubly linked list."""

    def assertListItemsEqual(self, linked_list, items):
        """Assert if items in linked list don't equal to list of items."""
        items_in_list = []
        node = linked_list.first_node
        while node is not None:
            items_in_list.append(node.object)
            node = node.next
        self.assertListEqual(items, items_in_list)

    def test_creation_from_list(self):
        """Test list creation."""
        linked_list = DoublyLinkedList()

        self.assertIsNone(linked_list.first_node)
        self.assertIsNone(linked_list.last_node)

    def test_insert_beginning(self):
        """Test insertion at the beginning of a list."""
        linked_list = DoublyLinkedList()
        first_node = Node(1)

        linked_list.insert_beginning(first_node)

        self.assertEqual(first_node, linked_list.first_node)
        self.assertEqual(first_node, linked_list.last_node)
        self.assertEqual(first_node.object, linked_list.first_node.object)

        next_first_node = Node(2)

        linked_list.insert_beginning(next_first_node)

        self.assertEqual(next_first_node, linked_list.first_node)
        self.assertEqual(first_node, linked_list.last_node)

    def test_insert_end(self):
        """Test insertion at the end of a list."""
        linked_list = DoublyLinkedList()
        new_node = Node(1)

        linked_list.insert_end(new_node)

        self.assertEqual(new_node, linked_list.first_node)
        self.assertEqual(new_node, linked_list.last_node)
        self.assertEqual(new_node.object, linked_list.first_node.object)

    def test_insert_after(self):
        """Test insertion after a node."""
        linked_list = DoublyLinkedList()
        linked_list.insert_beginning(Node(1))
        node = linked_list.first_node

        for i in xrange(2, 4):
            new_node = Node(i)
            linked_list.insert_after(node, new_node)
            node = new_node

        self.assertListItemsEqual(linked_list, [1, 2, 3])

        new_node = Node(10)
        linked_list.insert_after(linked_list.first_node, new_node)

        self.assertListItemsEqual(linked_list, [1, 10, 2, 3])

    def test_insert_before(self):
        """Test insertion before a node."""
        linked_list = DoublyLinkedList()
        linked_list.insert_beginning(Node(1))
        node = linked_list.first_node

        for i in xrange(2, 4):
            new_node = Node(i)
            linked_list.insert_before(node, new_node)
            node = new_node

        self.assertListItemsEqual(linked_list, [3, 2, 1])

        new_node = Node(10)
        linked_list.insert_before(linked_list.last_node, new_node)

        self.assertListItemsEqual(linked_list, [3, 2, 10, 1])

    def test_remove(self):
        """Test removing of a node from a list."""
        linked_list = DoublyLinkedList()
        first_node = Node(1)
        linked_list.insert_beginning(first_node)
        node_to_remove = Node(2)
        linked_list.insert_after(first_node, node_to_remove)
        linked_list.insert_end(Node(3))

        linked_list.remove(node_to_remove)

        self.assertListItemsEqual(linked_list, [1, 3])
