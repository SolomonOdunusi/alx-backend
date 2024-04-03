#!/usr/bin/env python3
"""MRU Caching Module"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU caching method"""
    def __init__(self):
        super().__init__()
        self.access_count = 0
        self.access_tracker = {}

    def put(self, key, item):
        """Input the data into the cache"""
        if key is None or item is None:
            return
        if BaseCaching.MAX_ITEMS <= len(self.cache_data):
            most_key = max(self.access_tracker, key=self.access_tracker.get)
            print("DISCARD: ", most_key)
            del self.cache_data[most_key]
            del self.access_tracker[most_key]

        self.cache_data[key] = item
        self.access_count += 1
        self.access_tracker[key] = self.access_count

    def get(self, key):
        """Retrieve the data from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.access_count += 1
        self.access_tracker[key] = self.access_count
        return self.cache_data[key]
