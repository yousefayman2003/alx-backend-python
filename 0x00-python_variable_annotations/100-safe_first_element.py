#!/usr/bin/env python3
"""Advanced task 1"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns first element of list if exists"""
    if lst:
        return lst[0]
    else:
        return None
