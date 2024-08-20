#!/usr/bin/env python3

'''New Tasks'''

from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Creates a task that waits for n random amounts of time'''
    return await wait_n(n, max_delay)
ame 