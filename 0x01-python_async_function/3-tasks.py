#!/usr/bin/env python3
"""do not create an async function, use the regular function syntax"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that waits for 
    a random delay up to max_delay seconds.
    """
    return asyncio.create_task(wait_random(max_delay))
