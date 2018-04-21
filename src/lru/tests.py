"""Tests for LRU cache mechanism."""
from unittest import TestCase

from lru import lru_cache


class TestLruCache(TestCase):
    """Tests for LRU cache mechanism."""

    def test_cache_with_default_size(self):
        """Test cache without specifying size."""
        @lru_cache
        def func(p1, p2):
            return p1 + p2

        self.assertEqual(func(1, 2), 3)

        @lru_cache()
        def func(p1, p2):
            return p1 + p2

        self.assertEqual(func(1, 2), 3)

    def test_cache_with_given_size(self):
        """Test cache without specifying size."""
        @lru_cache(200)
        def func(p1, p2):
            return p1 + p2

        self.assertEqual(func(1, 2), 3)
