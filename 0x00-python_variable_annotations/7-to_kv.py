#!/usr/bin/env python3
'''to_kv module
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    '''return a tuple item
    '''
    return(tuple(k, v**2))
