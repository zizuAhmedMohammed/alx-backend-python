#!/usr/bin/env python3
""" An asynchronous function `wait_n` that waits for multiple random delay tasks to complete. """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for `n` tasks with maximum delay
    
    of `max_delay` seconds
    """
    
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
