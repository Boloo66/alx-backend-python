#!/usr/bin/env python3
'''Asynio module
'''
import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[int, float]:
    '''This function will delay between 0 and max_delay sec
    '''
    value = await asyncio.sleep(random.uniform(0, max_delay))
    return value
