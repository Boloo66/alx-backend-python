#!/usr/bin/env python3
'''Asyncio module for multiple coroutines
'''
import asyncio
import time


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Determine the run time of wait_n func
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return float(end_time - start_time) / n
