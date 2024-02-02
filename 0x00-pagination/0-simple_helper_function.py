#!/usr/bin/env python3
"""
return a tuple containing a start index and an end index
"""


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
