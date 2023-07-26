#!/usr/bin/env python3
"""
Class that inherits from BaseCaching
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class that inherits from BaseCaching
    """
    def put(self, key, item):
        """
        Add item to cach
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item key
        """
        if key is not None:
            return self.cache_data.get(key)
