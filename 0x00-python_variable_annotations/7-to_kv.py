#!/usr/bin/env python3
'''to_kv module
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''return a tuple item
    '''
    return (k, float(v**2))
