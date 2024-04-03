#!/usr/bin/env python3
"""MRU Caching Module"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ A class MRUCache that inherits from
        BaseCaching and is a caching system
    """
    def __init__(self):
        """ Initialize a new FIFOCache. """
        super().__init__()
        self.all_keys = []

    def put(self, key, item):
        """Input the data into the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.all_keys:
                self.all_keys.append(key)
            else:
                self.all_keys.append(self.all_keys.pop(
                    self.all_keys.index(key)))
            if len(self.all_keys) > BaseCaching.MAX_ITEMS:
                # MRU algorithm
                most_recently_used = self.all_keys.pop(-2)
                del self.cache_data[most_recently_used]
                print("DISCARD: {}".format(most_recently_used))

    def get(self, key):
        """Retrieve the data from the cache"""
        if key is not None and key in self.cache_data:
            self.all_keys.append(self.all_keys.pop(
                self.all_keys.index(key)))
            return self.cache_data[key]
        return None
