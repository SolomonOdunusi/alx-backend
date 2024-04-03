#!/usr/bin/env python3
"""FIFO Caching Module"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching method"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Input the data into the cache"""
        if key is None or item is None:
            return
        if BaseCaching.MAX_ITEMS <= len(self.cache_data):
            first_item = next(iter(self.cache_data))
            print("DISCARD: ", first_item)
            del self.cache_data[first_item]

        self.cache_data[key] = item

    def get(self, key):
        """Retrieve the data from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
