#!/usr/bin/env python3

'''Let's execute multiple coroutines at the same time with async'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Simulates waiting for n random amounts of time'''
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay_list = [await task for task in asyncio.as_completed(tasks)]

    return delay_list
