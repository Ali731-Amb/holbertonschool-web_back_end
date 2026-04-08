#!/usr/bin/env python3
"""Create an asyncio Task from wait_random."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def _create_task(max_delay: int) -> asyncio.Task:
    """Helper to create task inside running loop."""
    return asyncio.create_task(wait_random(max_delay))


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio Task that wraps wait_random."""
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
