#!/usr/bin/env python3
"""Spawn task_wait_random n times and return sorted delays."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return all delays in
    ascending order."""
    delays: List[float] = []

    async def collect(delay: float) -> None:
        """Collect a delay and insert it in order."""
        result = await task_wait_random(delay)
        index = 0
        while index < len(delays) and delays[index] < result:
            index += 1
        delays.insert(index, result)

    await asyncio.gather(*[collect(max_delay) for _ in range(n)])
    return delays
