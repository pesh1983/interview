"""Tests for LRU cache mechanism."""
from unittest import TestCase

from mock import mock

from lru import lru_cache


class TestLruCache(TestCase):
    """Tests for LRU cache mechanism."""

    def test_decorator_itself_with_default_size(self):
        """Test decoration without specifying size."""
        @lru_cache
        def func(p1, p2):
            return p1 + p2

        self.assertEqual(func(1, 2), 3)

        @lru_cache()
        def func(p1, p2):
            return p1 + p2

        self.assertEqual(func(1, 2), 3)

    def test_decorator_itself_with_given_size(self):
        """Test decoration without specifying size."""
        @lru_cache(200)
        def func(p1, p2):
            return p1 + p2

        self.assertEqual(func(1, 2), 3)

    def test_cache_works(self):
        """Test that cache works for any combinations of arguments."""
        func_mock = mock.Mock(return_value=1)
        func_decorated = lru_cache(func_mock)

        func_decorated(1, 2, param1=1, param2=2, param3=3)
        func_decorated(1, 2, param3=3, param2=2, param1=1)

        func_mock.assert_called_once_with(1, 2, param1=1, param2=2, param3=3)

    def test_lru(self):
        """Test that LRU mechanism works correctly."""
        func_mock = mock.Mock(return_value=1)
        func = lru_cache(2)(func_mock)

        func(1)  # call function and put value in cache
        # cache has 1, cache is filled on half
        func(2)  # call function and put value in cache
        # cache has 1, 2, cache is full
        func(2)  # get from cache, not calling the function
        func(3)  # call function and put value in cache, removing 1
        # cache has 2, 3
        func(3)  # get from cache, not calling the function
        func(4)  # call function and put value in cache, removing 2
        # cache has 3, 4
        func(1)  # call function and put value in cache, removing 3
        # cache has 4, 1
        func(4)  # get from cache, not calling the function
        func(1)  # get from cache, not calling the function
        func(2)  # call function and put value in cache, removing 4
        # cache has 1, 2

        self.assertEqual(func_mock.mock_calls, [
            mock.call(1),
            mock.call(2),
            mock.call(3),
            mock.call(4),
            mock.call(1),
            mock.call(2),
        ])
