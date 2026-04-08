#!/usr/bin/env python3
"""This module provides a function to create a
key-value tuple with a squared value."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the
    square of a number as a float.
    Args:
        k (str): The key string.
        v (Union[int, float]): The value to square.
    Returns:
        Tuple[str, float]: A tuple with the string
        and the squared value as a float.
    """
    return (k, v ** 2)
