#!/usr/bin/env python3
"""Module containing make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        creates a multiplier function

        Args:
            multiplier (float): multiplier to multiply with

        Returns:
            a function that multiplies a float by multiplier
    """
    def f(x: float) -> float:
        """
            multiplies x by multiplier

            Args:
                x (float): number

            Returns:
                x * multiplier
        """
        return x * multiplier
    return f
