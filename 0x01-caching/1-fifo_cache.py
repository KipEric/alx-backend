#!/usr/bin/env python3
"""
FIFOCache that inherit from BaseCache
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class that inherit from BaseCaching
    """

    def __init__(self):
        """
        Initialize FIFOCache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add item to cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first_key = self.queue.pop(0)
                self.cache_data.pop(first_key)
                print("DISCARD:", first_key)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Get item by key
        """
        if key is not None:
            return self.cache_data.get(key)
