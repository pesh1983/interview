"""Task2.

Implementation of LRU cache mechanism.
"""
import sys


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
        __slots__ = ('age', 'key', 'value')

        def __init__(self, age, key, value):
            super(CacheObj, self).__init__()

            self.age = age
            self.key = key
            self.value = value

    class LruCache(object):
        __slots__ = ('_age_cnt', '_storage', '_size')

        def __init__(self, cache_size):
            super(LruCache, self).__init__()

            self._size = cache_size
            self._age_cnt = 0
            self._storage = {}

        def __setitem__(self, key, value):
            next_age = self._get_next_age()

            if key in self._storage:
                cache_obj = self._storage[key]
                cache_obj.value = value
                cache_obj.age = next_age
            else:
                cache_obj = CacheObj(age=next_age, key=key, value=value)
                if len(self._storage) < self._size:
                    self._storage[key] = cache_obj
                else:
                    lru_item_key = self._find_lru_item_key()
                    del self._storage[lru_item_key]
                    self._storage[key] = cache_obj

        def _get_next_age(self):
            self._age_cnt += 1
            return self._age_cnt

        def _find_lru_item_key(self):
            min_age = sys.maxsize
            lru_key = None
            for key, cache_obj in self._storage.items():
                if min_age > cache_obj.age:
                    min_age = cache_obj.age
                    lru_key = key
            return lru_key

        def __contains__(self, key):
            return key in self._storage

        def __getitem__(self, key):
            """Get

            :param args:
            :return:
            """
            if key in self._storage:
                cache_obj = self._storage[key]
                cache_obj.age = self._get_next_age()
                return self._storage[key].value

            raise KeyError

    def get_key_from_args(*args, **kwargs):
        return args + tuple(sorted(kwargs.items()))

    if callable(max_size):
        # if decorator is applied without parameters
        # the first argument will be a function
        func = max_size
        cache = LruCache(default_max_size)

        def wrapper(*args, **kwargs):
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
            def wrapper(*args, **kwargs):
                cache_key = get_key_from_args(*args, **kwargs)
                if cache_key in cache:
                    return cache[cache_key]
                else:
                    value = func(*args, **kwargs)
                    cache[cache_key] = value
                    return value

            return wrapper

        return decorator
