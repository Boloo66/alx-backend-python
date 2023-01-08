#!/usr/bin/env python3
'''Annonate this module
'''
from typing import Any, Sequence, Union, Tuple, List, TypeVar


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Annotate a zoom_array function prperly
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
