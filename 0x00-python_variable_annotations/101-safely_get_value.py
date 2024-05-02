#!/usr/bin/env python3
"""Advanced task 2"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """get value of key"""
    if key in dct:
        return dct[key]
    else:
        return default
