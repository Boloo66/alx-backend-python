#!/usr/bin/env python3
'''Asyncio module for multiple coroutines
'''
import random
import asyncio
from typing import List, Union, Any


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' spawn wait_random coroutine from with
    '''
    my_list: List[Union[float, Any]] = []
    for _ in range(n):
        task1 = asyncio.create_task(wait_random(max_delay))
        value = await task1
        my_list.append(value)
    return my_list.sort()
