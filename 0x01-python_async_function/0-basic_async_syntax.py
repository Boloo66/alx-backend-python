#!/usr/bin/env python3
'''Asynio module
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''This function will delay between 0 and max_delay sec
    '''
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
