#!/usr/bin/env python3
'''Run time for four parallel comprehensions'''

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures the runtime of four parallel async comprehensions'''
    start = time.time()

    tasks = [(async_comprehension()) for _ in range(0, 4)]

    await asyncio.gather(*tasks)

    end = time.time()
    return end - start
