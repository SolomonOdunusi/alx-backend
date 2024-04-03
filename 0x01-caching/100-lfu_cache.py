#!/usr/bin/env python3
"""LFU Caching Module"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU caching method"""
    def __init__(self):
        """Initialize the LFU caching method"""
        super().__init__()
        self.freq_tracker = {}
        self.access_tracker = {}

    def put(self, key, item):
        """Input the data into the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu_val = min(self.freq_tracker.values())
            lfu_keys = [i for i, j in self.freq_tracker.items() if j == lfu_val]

            if len(lfu_keys) > 1:
                lru_key = min(lfu_keys, key=lambda i: self.access_tracker.get(i, 0))
                print("DISCARD: ", lru_key)
                del self.cache_data[lru_key]
                del self.freq_tracker[lru_key]
                del self.access_tracker[lru_key]
            else:
                lfu_key = lfu_keys[0]
                print("DISCARD: ", lfu_key)
                del self.cache_data[lfu_key]
                del self.freq_tracker[lfu_key]
                del self.access_tracker[lfu_key]

        self.cache_data[key] = item
        self.freq_tracker[key] = self.freq_tracker.get(key, 0) + 1
        self.access_tracker[key] = self.access_tracker.get(key, 0) + 1

    def get(self, key):
        """Retrieve the data from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.freq_tracker[key] = self.freq_tracker.get(key, 0) + 1
        self.access_tracker[key] = self.access_tracker.get(key, 0) + 1
        return self.cache_data[key]
