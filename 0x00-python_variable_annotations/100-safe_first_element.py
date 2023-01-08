#!/usr/bin/env python3
'''Annonate this module
'''
from typing import Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Any:
    ''' Using Any annotation
    '''
    if lst:
        return lst[0]
    else:
        return None
