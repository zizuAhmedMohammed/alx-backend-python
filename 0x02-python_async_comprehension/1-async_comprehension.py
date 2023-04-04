#!/usr/bin/env python3
"""A coroutine called async_comprehension that takes no arguments"""
import asyncio


async def async_generator():
    """
    coroutine will collect 10 random numbers using
    an async comprehensing over async_generator
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)


async def async_comprehension():
    """return the 10 random numbers"""
    random_numbers = [number async for number in async_generator()]
    return random_numbers
