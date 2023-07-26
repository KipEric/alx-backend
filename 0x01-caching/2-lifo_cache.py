#!/usr/bin/env python3
"""
LIFOCache that inherit from BaseCache
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Class that inherit from BaseCaching
    """

    def __init__(self):
        """
        Initialize LIFOCache
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add item to cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_key = self.stack.pop()
                self.cache_data.pop(last_key)
                print("DISCARD:", last_key)
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """
        Get item by key
        """
        if key is not None:
            return self.cache_data.get(key)
