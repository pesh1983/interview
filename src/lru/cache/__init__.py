"""LRU cache implementation."""
from lru.structures.doubly_linked_list import DoublyLinkedList, Node


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

    __slots__ = ('_age_cnt', '_storage', '_size', '_items_sorted_by_age')

    def __init__(self, cache_size):
        """Initialize cache.

        :param cache_size: Maximum cache size.
        """
        super(LruCache, self).__init__()

        self._size = cache_size
        self._age_cnt = 0
        self._storage = {}

        # linked list is used to store items ordered by age
        # this allows significantly decrease cost of searching LRU item
        self._items_sorted_by_age = DoublyLinkedList()

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
        node = self._storage[key]
        node.object.value = value
        self._update_age(node)

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
                self._remove_item(lru_item_key)

        # create new cache object
        cache_obj = CacheObj(age=None, key=key, value=value)
        node = Node(cache_obj)
        self._set_age(node)
        # add new item to cache
        self._storage[key] = node

    def _remove_item(self, key):
        """Remove a value from cache under given key.

        :param key: Key under which a value must be removed.
        """
        node = self._storage[key]
        del self._storage[key]

        self._items_sorted_by_age.remove(node)

    def _update_age(self, node):
        """Update age of given cache object.

        It sets the next available age to a given object.
        :param node: A node with cache object which age must be updated.
        """
        self._items_sorted_by_age.remove(node)
        self._set_age(node)

    def _set_age(self, node):
        """Set age of given cache object.

        It sets the next available age to a given object.
        :param node: A node with cache object which age must be set.
        """
        next_age = self._get_next_age()
        node.object.age = next_age

        self._items_sorted_by_age.insert_end(node)

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
        node = self._items_sorted_by_age.first_node
        return node.object.key if node else None

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
            node = self._storage[key]
            self._update_age(node)
            return node.object.value

        raise KeyError

    def __len__(self):
        """Get amount of values in cache."""
        return len(self._storage)

    def items(self):
        """Get generator that iterates over items in cache.

        Each returned variable is a tuple of (key, value). Items are returned
        from least to most recently used.
        :return: Generator.
        """
        node = self._items_sorted_by_age.first_node
        while node is not None:
            cache_obj = node.object
            yield cache_obj.key, cache_obj.value
            node = node.next
