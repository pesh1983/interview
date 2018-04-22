"""Tests of LRU cache."""
import unittest

from lru import LruCache


class TestLruCache(unittest.TestCase):
    """Tests of LRU cache."""

    def test_set_item(self):
        """Test putting item in cache."""
        cache = LruCache(3)

        cache['k1'] = 100
        cache['k2'] = 200
        cache['k3'] = 300
        cache['k4'] = 400

        self.assertEqual(len(cache), 3)
        self.assertListEqual(list(cache.items()), [
            ('k2', 200), ('k3', 300), ('k4', 400)
        ])

    def test_update_item(self):
        """Test update item in cache."""
        cache = LruCache(3)

        cache['k1'] = 100
        cache['k2'] = 200
        cache['k1'] = 300

        self.assertEqual(len(cache), 2)
        self.assertListEqual(list(cache.items()), [
            ('k2', 200), ('k1', 300),
        ])

    def test_get_item(self):
        """Test getting item from cache."""
        cache = LruCache(3)

        cache['k1'] = 100

        self.assertEqual(cache['k1'], 100)

    def test_get_non_existed_item(self):
        """Test getting non-existed item from cache."""
        cache = LruCache(3)

        with self.assertRaises(KeyError):
            cache['k1']
