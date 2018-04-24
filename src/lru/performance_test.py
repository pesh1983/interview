"""Performance tests of LRU cache implementation."""
from six.moves import range

from lru import lru_cache
from utils import timed

cache_sizes = (1000, 10000, 100000, 1000000)

for size in cache_sizes:
    @lru_cache(size)
    def test_func(p1, p2):
        """Test cache."""
        return p1 + p2

    @timed(size)
    def fill_cache():
        """Fill empty cache."""
        for idx in range(size):
            test_func(idx, idx + 1)

    fill_cache()

    @timed(size)
    def replace_cache():
        """Replace all values in fully stocked cache with the new ones."""
        for idx in range(size):
            test_func(idx + 1, idx)

    replace_cache()
