#!/usr/bin/env python3


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of start and end indexes for a given page and page_size."""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
