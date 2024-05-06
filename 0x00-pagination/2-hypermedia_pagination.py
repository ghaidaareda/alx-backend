#!/usr/bin/env python3
"""
Main file
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    return the range of indices for the current page.
    """
    # calculate the starting point of this page's data
    start_index = (page - 1) * page_size
    # calculate one past the ending point of this page's data
    end_index = start_index + page_size

    # if we are on the last page, make sure our end index is within the total
    # number of items
    if page == "last":
        end_index = None

    # create a tuple with the start and end indices
    result = (start_index, end_index)
    return result


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get page with index_range"""
        assert isinstance(page, int), "page must be a signed integer"
        assert isinstance(
            page_size, int) and page_size > 0, "page_size must be an integer"
        result = index_range(page, page_size)
        dataset = self.dataset()
        if page == "last":
            end_index = None
            return []
        else:
            return dataset[result[0]: result[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        total_items = len(self.dataset())
        result_dict = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if end_index < total_items else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_items
        }
        return result_dict
