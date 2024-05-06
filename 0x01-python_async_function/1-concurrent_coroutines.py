#!/usr/bin/env python3
"""Module contains an async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay. You will spawn wait_random
n times with the specified max_delay."""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        an asynchronous coroutine that  return the list of
        all the delays (float values)
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await t for t in asyncio.as_completed(tasks)]
