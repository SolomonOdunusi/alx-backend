#!/usr/bin/env python3
"""FIFO Caching Module"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching method"""
    def put(self, key, item):
        """Input the data into the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = list(self.cache_data)[0]
                self.cache_data.pop(discard)
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """Retrieve the data from the cache"""
        return self.cache_data.get(key)
