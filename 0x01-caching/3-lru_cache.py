#!/usr/bin/python3
"""
Create a class MRUCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A cache with First In, First Out
    """

    def __init__(self):
        """ init class"""
        super().__init__()  # inherit from parent class
        self.keys = []

    def put(self, key, item):
        """
        remove oldest item from cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.keys.append(key)
            # Check if the cache is full
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = len(self.keys) - 2
                discard = self.keys.pop(last_key)
                del self.cache_data[discard]
                print("DISCARD: " + discard)

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
