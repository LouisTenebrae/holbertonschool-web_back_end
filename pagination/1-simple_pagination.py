
#!/usr/bin/env python3
'''Simple pagination'''

from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Returns start and end indices for a given page'''
    start_index = (page - 1) * page_size
    end_index = (start_index + page_size)

    return (start_index, end_index)


class Server:
    '''Server class'''
    DATA_FILE = 'Popular_Baby_Names.csv'

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        '''Returns the dataset'''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Returns the page of data'''
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)

        data = self.dataset()

        data = data[start_index:end_index]

        return data
