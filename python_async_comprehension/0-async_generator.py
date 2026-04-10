#!/usr/bin/env python3
"""Async generator coroutine module."""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]: # type: ignore
    """Asynchronously yields 10 random floats between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
