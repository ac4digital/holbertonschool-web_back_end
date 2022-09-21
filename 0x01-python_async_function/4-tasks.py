#!/usr/bin/env python3
""" Script take code from wait_n and alter it into
    new function task_wait_n """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of delayed float values
        using wait_random coroutine """
    tasks: List[float] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    return [await process for process in asyncio.as_completed(tasks)]
