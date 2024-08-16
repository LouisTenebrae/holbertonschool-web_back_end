#!/usr/bin/env python3
"""Function element_length that takes a list lst of strings as argument"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing the string and its length"""
    return [(i, len(i)) for i in lst]
