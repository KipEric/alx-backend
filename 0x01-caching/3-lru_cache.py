#!/usr/bin/env python3
"""
LRUCache that inherit from BaseCache
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Class that inherit from BaseCaching
    """

    def __init__(self):
        """
        Initialize LRUCache
        """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """
        Add item to cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = self.lru_order.pop(0)
                self.cache_data.pop(lru_key)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.lru_order.append(key)

            # Move the most recently used key to the end of the list
            if key in self.lru_order:
                self.lru_order.remove(key)
            self.lru_order.append(key)

    def get(self, key):
        """
        Get item by key
        """
        if key is not None and key in self.cache_data:
            self.lru_order.remove(key)
            self.lru_order.append(key)
            return self.cache_data.get(key)
        return None
