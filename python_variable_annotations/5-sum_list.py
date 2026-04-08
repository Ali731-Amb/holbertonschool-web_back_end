#!/usr/bin/env python3
"""This module provides a function to sum a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of all floats in a list.

    Args:
        input_list (List[float]): The list of floats to sum.
    Returns:
        float: The sum of all elements in the list.
    """
    return sum(input_list)
