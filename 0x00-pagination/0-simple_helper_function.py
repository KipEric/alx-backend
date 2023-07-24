#!/usr/bin/env python3
"""
A function that takes two integers and return a tuple
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return start and end index of the page
    """
    if page < 1 or page_size < 1:
        return (0, 0)
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
