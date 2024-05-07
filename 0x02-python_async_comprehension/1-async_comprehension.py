#!/usr/bin/env python3
"""Module containing  a coroutine called async_comprehension"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """created a list of 10 random numbers"""
    return [n async for n in async_generator()]
