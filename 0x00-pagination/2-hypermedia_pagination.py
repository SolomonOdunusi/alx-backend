#!/usr/bin/env python3
"""get_hyper_index module"""
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Calculate start and end indices for pagination."""

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return(start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset."""
        if (
            not isinstance(page, int) or
            not isinstance(page_size, int) or
            page <= 0 or page_size <= 0
        ):
            raise AssertionError

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Implement a get_hyper method
        Return:

        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        dataset = self.dataset()
        total_pages = len(dataset) // page_size +
        (len(dataset) % page_size > 0)
        start_index, end_index = index_range(page, page_size)
        data = dataset[start_index:end_index]
        next_page = page + 1 if end_index < len(dataset) else None
        prev_page = page - 1 if start_index > 0 else None
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
