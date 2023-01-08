#!/usr/bin/env python3
'''ANNOTATION OF FUNCTIONS
'''

from typing import List, Tuple, Sequence, Iterable

Ti = Tuple[Sequence, int]
Si = List[Ti]


def element_length(lst: Iterable[Sequence]) -> Si:
    '''I annotated this function
    '''
    return [(i, len(i)) for i in lst]
