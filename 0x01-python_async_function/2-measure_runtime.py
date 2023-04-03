#!/usr/bin/env python3
"""approximate elapsed time Measure the runtime"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    integers n and max_delay as arguments 
    total execution time for wait_n(n, max_delay)
    returns total_time / n
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start_time
    return elapsed / n
