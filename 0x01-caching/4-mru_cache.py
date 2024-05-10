#!/usr/bin/python3
"""
Create a class LIFOCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU caching class """

    def __init__(self):
        """ Initialize MRU cache """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the most recently used item (last accessed)
            mru_key = max(self.cache_data, key=self.cache_data.get)
            print("DISCARD: {}".format(mru_key))
            del self.cache_data[mru_key]

        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as most recently used
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
