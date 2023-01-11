#!/usr/bin/env python3
'''Asyncio module for multiple coroutines
'''
import asyncio
from typing import List, Union, Any

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' spawn wait_random coroutine from with
    '''
    wait_time = await asyncio.gather(
        *list(map(lambda _: task_wait_random(max_delay), range(n))))
    return sorted(wait_time)
