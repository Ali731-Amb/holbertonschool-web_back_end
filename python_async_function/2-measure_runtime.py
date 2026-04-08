#!/usr/bin/env python3
"""Measure the average execution time of wait_n."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Run wait_n and return the average elapsed time per coroutine."""
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - start) / n
