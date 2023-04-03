#!/usr/bin/env python3
""" Asynchronous coroutine that takes in an inetger argument """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ 
    Generate a random delay between 0 and max_delay (inclusive)
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
