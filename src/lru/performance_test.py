"""Performance tests of LRU cache implementation."""
import time
from functools import wraps

from lru import lru_cache


def timed(title):
    """Decorate function and print its execution time to stdout.

    :param title: Title to be print before execution time output.
    :return: Decorated function.
    """
    def decorator(func):
        """Decorator.

        :param func: Function to be decorated.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Wrap decorated function.

            :param args: Positional arguments to be passed to original
            function.
            :param kwargs: Keyword arguments to be passed to original
            function.
            :return: Result execution of original function.
            """
            start_time = time.time()

            result = func(*args, **kwargs)

            print('{name} ({title}): {result_time}'.format(
                name=func.__name__,
                title=title,
                result_time=time.time() - start_time
            ))
            return result

        return wrapper

    return decorator


cache_sizes = (1000, 10000, 100000, 1000000)

for size in cache_sizes:
    @lru_cache(size)
    def test_func(p1, p2):
        """Test cache."""
        return p1 + p2

    @timed(size)
    def fill_cache():
        """Fill empty cache."""
        for idx in xrange(size):
            test_func(idx, idx + 1)

    fill_cache()

    @timed(size)
    def replace_cache():
        """Replace all values in fully stocked cache with the new ones."""
        for idx in xrange(size):
            test_func(idx + 1, idx)

    replace_cache()
