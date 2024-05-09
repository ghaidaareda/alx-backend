#!/usr/bin/python3
"""
Create a class LRUCache that inherits from BaseCaching
and is a caching system
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """ discard the least recently used item (LRU algorithm)"""
        if key is not None and item is not None:
            # If key already exists, move it to the end (most recently used)
            if key in self.cache_data:
                del self.cache_data[key]
            # If cache is full, remove the least recently used item
            elif len(self.cache_data) >= self.MAX_ITEMS:
                oldest_key = next(iter(self.cache_data))
                del self.cache_data[oldest_key]
                print(f'DISCARD: {oldest_key}')
            self.cache_data[key] = item

    def get(self, key):
        """ retrieve data"""
        if key is not None and key in self.cache_data:
            # Move the accessed key to the end (most recently used)
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
