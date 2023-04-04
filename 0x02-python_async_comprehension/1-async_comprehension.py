#!/usr/bin/env python3

import asyncio
import random

async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)

async def async_comprehension():
    random_numbers = [number async for number in async_generator()]
    return random_numbers
