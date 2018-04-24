"""Task2.

Implementation of LRU cache mechanism.
"""
from functools import wraps

from lru.cache import LruCache


def lru_cache(max_size=None):
    """
    Decorate a function and add LRU cache mechanism to it.

    It is allowed to be applied to a function only.
    :param max_size: Maximum cache size. It is optional and equals to 100
    by default.
    :return: Decorated function.
    """
    default_max_size = 100

    def get_key_from_args(*args, **kwargs):
        """Generate a key from positional and keyword arguments.

        :param args: Positional arguments.
        :param kwargs: Keyword arguments.
        :return: Generated key.
        """
        return args + tuple(sorted(kwargs.items()))

    func = None
    if callable(max_size):
        # if decorator is applied without parameters
        # the first argument will be a function
        func = max_size
        max_size = default_max_size
    else:
        # if decorator is executed before applied
        if max_size is None:
            # if maximum size is not specified
            # set it to default
            max_size = default_max_size

    cache = LruCache(max_size)

    def decorator(func):
        """Decorate a function.

        :param func: A function to be decorated.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Wrap a function.

            :param args: Positional arguments for the function.
            :param kwargs: Keyword arguments for the function.
            :return: Result of execution of the function.
            """
            cache_key = get_key_from_args(*args, **kwargs)
            if cache_key in cache:
                return cache[cache_key]
            else:
                value = func(*args, **kwargs)
                cache[cache_key] = value
                return value

        return wrapper

    return decorator(func) if func else decorator
