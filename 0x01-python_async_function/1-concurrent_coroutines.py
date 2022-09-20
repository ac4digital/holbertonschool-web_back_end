#!/usr/bin/env python3
""" Script takes an integer argument between 0 and max_delay
"""

import asyncio
from concurrent.futures import process
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list time to delay """
    delays: List[float] = []

    for _ in range(n):
        delays.append(wait_random(max_delay))

    return [await process for process in asyncio.as_completed(delays)]
