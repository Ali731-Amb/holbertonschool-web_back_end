#!/usr/bin/env python3
"""This module provides a function to create multiplier functions."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a given multiplier.
    Args:
        multiplier (float): The multiplier value.
    Returns:
        Callable[[float], float]: A function
        that multiplies its input by the multiplier.
    """
    def multiply(x: float) -> float:
        """Multiply a float by the outer multiplier.
        Args:
            x (float): The number to multiply.
        Returns:
            float: The result of x multiplied by the multiplier.
        """
        return x * multiplier
    return multiply
