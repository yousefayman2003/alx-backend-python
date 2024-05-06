#!/usr/bin/env python3
"""Module contains task_wait_n"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        an asynchronous coroutine that  return the list of
        all the delays (float values)
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await t for t in asyncio.as_completed(tasks)]
