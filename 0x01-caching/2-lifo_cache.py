#!/usr/bin/env python3
"""LIFO Caching Module"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching method"""
    def put(self, key, item):
        """Input the data into the cache"""
        if key and item:
            if self.cache_data:
                discard = list(self.cache_data)[-1]
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                self.cache_data.pop(discard)
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """Retrieve the data from the cache"""
        return self.cache_data.get(key)
