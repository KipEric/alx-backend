#!/usr/bin/env python3
"""
MRUCache that inherit from BaseCache
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Class that inherit from BaseCaching
    """

    def __init__(self):
        """
        Initialize LRUCache
        """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """
        Add item to cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                mru_key = self.mru_order.pop()
                self.cache_data.pop(mru_key)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item

            # Move the most recently used key to the end of the list
            if key in self.mru_order:
                self.mru_order.remove(key)
            self.mru_order.append(key)

    def get(self, key):
        """
        Get item by key
        """
        if key is not None and key in self.cache_data:
            self.mru_order.remove(key)
            self.mru_order.append(key)
            return self.cache_data.get(key)
        return None
