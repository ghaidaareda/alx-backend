#!/usr/bin/python3
"""
Create a class FIFOCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A cache with First In, First Out
    """

    def __init__(self):
        """ init class"""
        super().__init__()  # inherit from parent class

    def put(self, key, item):
        """
        remove oldest item from cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            # Check if the cache is full
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removed_key = self.get_oldest_key()
                print(f'DISCARD: {removed_key}')
                del self.cache_data[removed_key]
            self.cache_data[key] = item

    def get_oldest_key(self):
        """Retrieve the key of the oldest item in the cache."""
        return next(iter(self.cache_data))

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
