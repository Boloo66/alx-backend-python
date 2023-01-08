#!/usr/bin/env python3
'''closure in python
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Takes a float and return multiplier for float obj
    '''
    def inner(num: float) -> float:
        return num * multiplier
    return inner
