#!/usr/bin/env python3
"""This module use async operation in python"""


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """This is an async function to measure func time"""
    start = time.perf_counter()
    asyncio.run((wait_n(n, max_delay)))
    end = time.perf_counter() - start
    return end / n
