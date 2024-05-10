#!/usr/bin/python3
"""
Create a class LFUCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching class """

    def __init__(self):
        """ Initialize LFU cache """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find the least frequency used item (LFU algorithm)
            min_freq = min(self.frequency.values())
            least_freq_keys = [k for k, v in self.frequency.items() if v == min_freq]

            if len(least_freq_keys) > 1:
                # If there are multiple keys with the least frequency, use LRU algorithm
                lru_key = min(self.cache_data, key=self.cache_data.get)
                print("DISCARD: {}".format(lru_key))
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
            else:
                lfu_key = least_freq_keys[0]
                print("DISCARD: {}".format(lfu_key))
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]

        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency
        self.frequency[key] += 1

        return self.cache_data[key]


# Example usage:
cache = LFUCache()

# Adding 10 items
for i in range(1, 11):
    cache.put(i, str(i))

cache.print_cache()
