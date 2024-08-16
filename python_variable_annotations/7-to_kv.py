#!/usr/bin/env python3
"""Function to_kv that takes a string k and an int OR float v as arguments"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with k and the square of v"""
    return (k, v * v)
