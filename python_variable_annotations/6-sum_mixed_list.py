#!/usr/bin/python3
"""Function sum_mixed_list that takes a list mxd_lst of floats and integers"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the list of floats and integers"""
    return sum(mxd_lst)
