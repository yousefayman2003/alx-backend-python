#!/usr/bin/env python3
"""Module containing sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        sums the list

        Args:
            mxd_lst (list): list of floats and integers

        Returns:
            the sum
    """
    return sum(mxd_lst)
