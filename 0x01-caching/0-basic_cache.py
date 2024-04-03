#!/usr/bin/env python3
"""The basic cache class module"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Simple caching method"""
    def put(self, key, item):
        """Input the data into the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve the data from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
