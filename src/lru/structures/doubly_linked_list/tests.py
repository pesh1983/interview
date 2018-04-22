"""Tests of doubly linked list."""
import unittest

from lru.structures.doubly_linked_list import DoublyLinkedList, Node


class DoublyLinkedListTestCase(unittest.TestCase):
    """Tests of doubly linked list."""

    def test_creation_from_list(self):
        """Test list creation."""
        linked_list = DoublyLinkedList()

        self.assertIsNone(linked_list.first_node)
        self.assertIsNone(linked_list.last_node)

    def test_insert_beginning(self):
        """Test insertion at the beginning of a list."""
        linked_list = DoublyLinkedList()
        new_node = Node(1)
        linked_list.insert_beginning(new_node)

        self.assertEqual(new_node, linked_list.first_node)
        self.assertEqual(new_node, linked_list.last_node)
        self.assertEqual(new_node.object, linked_list.first_node.object)

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

        result = []
        node = linked_list.first_node
        while node is not None:
            result.append(node.object)
            node = node.next

        self.assertListEqual([1, 2, 3], result)

    def test_insert_before(self):
        """Test insertion before a node."""
        linked_list = DoublyLinkedList()
        linked_list.insert_beginning(Node(1))
        node = linked_list.first_node
        for i in xrange(2, 4):
            new_node = Node(i)
            linked_list.insert_before(node, new_node)
            node = new_node

        result = []
        node = linked_list.first_node
        while node is not None:
            result.append(node.object)
            node = node.next

        self.assertListEqual([3, 2, 1], result)

    def test_remove(self):
        """Test removing of a node from a list."""
        linked_list = DoublyLinkedList()
        first_node = Node(1)
        linked_list.insert_beginning(first_node)
        node_to_remove = Node(2)
        linked_list.insert_after(first_node, node_to_remove)
        linked_list.insert_end(Node(3))

        linked_list.remove(node_to_remove)

        result = []
        node = linked_list.first_node
        while node is not None:
            result.append(node.object)
            node = node.next

        self.assertListEqual([1, 3], result)
