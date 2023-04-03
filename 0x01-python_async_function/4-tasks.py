#!/usr/bin/env python3
"""An asynchronous function and a corresponding task function."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates `n` tasks that wait for a random delay up 
    to `max_delay` seconds, and returns the sorted 
    list of resulting delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return sorted(delays)
