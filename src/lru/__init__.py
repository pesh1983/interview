"""Task2.

Implementation of LRU cache mechanism.
"""


def lru_cache(max_size=None):
    """
    Decorate a function and add LRU cache mechanism to it.

    It is allowed to be applied to a function only.
    :param max_size: Maximum cache size. It is optional and equals to 100
    by default.
    :return: Decorated function.
    """
    default_max_size = 100

    if callable(max_size):
        # if decorator is applied without parameters
        # the first argument will be a function
        func = max_size
        max_size = default_max_size

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper
    else:
        if max_size is None:
            max_size = default_max_size

        def decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator
