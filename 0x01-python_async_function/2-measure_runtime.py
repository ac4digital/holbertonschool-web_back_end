#!/usr/bin/env python3
""" Script with integers n and max_delay measures
    the total execution time """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures wait_n execution time """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total = time.perf_counter() - start
    return total / n
