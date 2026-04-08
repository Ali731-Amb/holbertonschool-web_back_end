#!/usr/bin/env python3
"""This module provides a function to return the
length of each element in an iterable of sequences."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with each sequence and
    its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence
        objects.
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
