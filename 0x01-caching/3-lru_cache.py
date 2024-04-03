#!/usr/bin/env python3
"""LRU Caching Module"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU caching method"""
    def __init__(self):
        super().__init__()
        self.access_tracker = {}

    def put(self, key, item):
        """Input the data into the cache"""
        if key is None or item is None:
            return
        if BaseCaching.MAX_ITEMS <= len(self.cache_data):
            least_key = min(self.access_tracker, key=self.access_tracker.get)
            print("DISCARD: ", least_key)
            del self.cache_data[least_key]
            del self.access_tracker[least_key]

        self.cache_data[key] = item
        self.access_tracker[key] = len(self.access_tracker)

    def get(self, key):
        """Retrieve the data from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.access_tracker[key] = len(self.access_tracker)
        return self.cache_data[key]
