"""Task2.

Implementation of LRU cache mechanism.
"""
import sys
from functools import wraps


def lru_cache(max_size=None):
    """
    Decorate a function and add LRU cache mechanism to it.

    It is allowed to be applied to a function only.
    :param max_size: Maximum cache size. It is optional and equals to 100
    by default.
    :return: Decorated function.
    """
    default_max_size = 100

    class CacheObj(object):
        """Class for an object to be put in cache."""

        __slots__ = ('age', 'key', 'value')

        def __init__(self, age, key, value):
            """Initialize an instance.

            :param age: Age of cache object. It is used in LRU cache mechanism.
            :param key: A key.
            :param value: A value.
            """
            super(CacheObj, self).__init__()

            self.age = age
            self.key = key
            self.value = value

    class LruCache(object):
        """LRU cache.

        The class implements LRU cache mechanism
        (https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU).
        Usage example:

        .. code-block:: python

            >>> cache = LruCache(2)
            >>>
            >>> cache['key1'] = 'value1'
            >>> cache['key2'] = 'value2'
            >>> cache['key3'] = 'value3'
            >>>
            >>> assert cache['key2'] == 'value2'
            >>> assert cache['key3'] == 'value3'

        """

        __slots__ = ('_age_cnt', '_storage', '_size')

        def __init__(self, cache_size):
            """Initialize cache.

            :param cache_size: Maximum cache size.
            """
            super(LruCache, self).__init__()

            self._size = cache_size
            self._age_cnt = 0
            self._storage = {}

        def __setitem__(self, key, value):
            """Put a value under given key in cache.

            :param key: A key under which the value must be put in cache.
            :param value: A value to be put in cache.
            """
            if key in self._storage:
                # if key is in cache
                self._update_item(key, value)
            else:
                # if key is not in cache
                self._add_item(key, value)

        def _update_item(self, key, value):
            """Update a value in cache under given key.

            :param key: Key under which an item must be updated.
            :param value: New value to be put in cache.
            """
            cache_obj = self._storage[key]
            cache_obj.value = value
            self._update_age(cache_obj)

        def _add_item(self, key, value):
            """Add new value into cache under given key.

            :param key: Key under which a value will be added to cache.
            :param value: Value to be put in cache.
            :return:
            """
            if len(self._storage) >= self._size:
                # if overflow of capacity
                # find a key of least recently used item
                lru_item_key = self._find_lru_item_key()
                if lru_item_key is not None:
                    # if item is found, remove it from cache
                    del self._storage[lru_item_key]

            # create new cache object
            cache_obj = CacheObj(age=None, key=key, value=value)
            self._update_age(cache_obj)
            # add new item to cache
            self._storage[key] = cache_obj

        def _update_age(self, cache_obj):
            """Update age of given cache object.

            It sets the next available age to a given object.
            :param cache_obj: Cache object which age must be updated.
            """
            next_age = self._get_next_age()
            cache_obj.age = next_age

        def _get_next_age(self):
            """Get next age value.

            Each time the method is executed age counter is incremented by 1.
            :return: Next age value.
            """
            self._age_cnt += 1
            return self._age_cnt

        def _find_lru_item_key(self):
            """Find a key of least recently used value.

            :return: A key or None if no key is found. The latter can happen
            if cache is empty.
            """
            min_age = sys.maxsize
            lru_key = None
            for key, cache_obj in self._storage.items():
                if min_age > cache_obj.age:
                    min_age = cache_obj.age
                    lru_key = key
            return lru_key

        def __contains__(self, key):
            """Has cache a value under given key or not.

            :param key: A key to check.
            :return: True if cache has a value under given key,
            False otherwise.
            """
            return key in self._storage

        def __getitem__(self, key):
            """Get a value under the given key from cache.

            :param key: A key under which a result is needed.
            :raise KeyError: If there is no value in cache under the given key.
            :return: Value from cache.
            """
            if key in self._storage:
                cache_obj = self._storage[key]
                self._update_age(cache_obj)
                return cache_obj.value

            raise KeyError

    def get_key_from_args(*args, **kwargs):
        """Generate a key from positional and keyword arguments.

        :param args: Positional arguments.
        :param kwargs: Keyword arguments.
        :return: Generated key.
        """
        return args + tuple(sorted(kwargs.items()))

    if callable(max_size):
        # if decorator is applied without parameters
        # the first argument will be a function
        func = max_size
        cache = LruCache(default_max_size)

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
    else:
        cache = LruCache(default_max_size if max_size is None else max_size)

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

        return decorator
