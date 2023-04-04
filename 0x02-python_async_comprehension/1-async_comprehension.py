#!/usr/bin/env python3
"""A coroutine called async_comprehension that takes no arguments"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_compression - function that takes no arguments
    Return: the 10 random numbers"""
    random_numbers = [number async for number in async_generator()]
    return random_numbers
