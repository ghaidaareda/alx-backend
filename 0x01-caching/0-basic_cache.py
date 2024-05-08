#!/usr/bin/python3
"""
Basic class that inherits from BaseCaching creation.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic cache implementation."""

    def __init__(self):
        """Initialize the BasicCache."""
        super().__init__()  # Initialize the parent class

    def put(self, key, item):
        """Add an item to the cache."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
