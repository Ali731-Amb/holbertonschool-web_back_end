#!/usr/bin/env python3
"""Async routine that spawns wait_random n times and returns sorted delays."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return all delays in ascending order."""
    delays: List[float] = []

    async def collect(delay: float) -> None:
        """Collect a delay and insert it in order."""
        result = await wait_random(delay)
        index = 0
        while index < len(delays) and delays[index] < result:
            index += 1
        delays.insert(index, result)

    await asyncio.gather(*[collect(max_delay) for _ in range(n)])
    return delays
