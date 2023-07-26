#!/usr/bin/env python3
"""
LFUCache that inherit from BaseCache
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Class that inherit from BaseCaching
    """

    def __init__(self):
        """
        Initialize LFUCache
        """
        super().__init__()
        self.frequency = {}
        self.min_frequency = 0

    def put(self, key, item):
        """
        Add item to cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    self.lfu_discard()
                self.cache_data[key] = item
                self.frequency[key] = 1
                self.min_frequency = 1

    def lfu_discard(self):
        """
        Discard lfu items
        """
        if not self.cache_data:
            return False

        lfu_keys = [
            key for key in self.cache_data
            if self.frequency[key] == self.min_frequency
        ]
        lru_key = None
        for key in self.cache_data:
            if key in lfu_keys:
                if lru_key is None or \
                        self.frequency[key] < self.frequency[lru_key]:
                    lru_key = key

        if lru_key is not None:
            self.cache_data.pop(lru_key)
            self.frequency.pop(lru_key)

        self.min_frequency = min(self.frequency.values())

    def get(self, key):
        """
        Get item by key
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
