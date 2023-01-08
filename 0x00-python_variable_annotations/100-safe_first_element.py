#!/usr/bin/env python3
'''Annonate this module
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' Using Any annotation
    '''
    if lst:
        return lst[0]
    else:
        return None
