#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self,
        index: int = None,
        page_size: int = 10
    ) -> Dict[str, Union[int, List[List], Optional[int]]]:
        """
        Return hypertext metadat for the specified start index of dataset
        """
        assert index is None or (isinstance(index, int) and index >= 0)
        assert isinstance(page_size, int) and page_size > 0

        total_items = len(self.indexed_dataset())
        total_pages = math.ceil(total_items / page_size)

        if index is None:
            index = 0
        elif index >= total_items:
            return {
                "index": index,
                "data": [],
                "page_size": page_size,
                "next_index": None
            }

        dataset = self.indexed_dataset()
        if index not in dataset:
            return {
                "index": index,
                "data": [],
                "page_size": page_size,
                "next_index": None
            }

        end_index = index + page_size
        while end_index not in dataset and end_index < total_items:
            end_index += 1

        data = [dataset[i] for i in range(index, end_index)]

        next_index = end_index

        hypermedia_data = {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index if next_index < total_items else None
        }

        return hypermedia_data
