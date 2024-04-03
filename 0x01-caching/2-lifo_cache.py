#!/usr/bin/env python3
"""LIFO Caching Module"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching method"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Input the data into the cache"""
        if key is None or item is None:
            return
        if BaseCaching.MAX_ITEMS <= len(self.cache_data):
            last_item = next(reversed(self.cache_data))
            print("DISCARD: ", last_item)
            del self.cache_data[last_item]

        self.cache_data[key] = item

    def get(self, key):
        """Retrieve the data from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
