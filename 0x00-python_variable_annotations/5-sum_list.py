#!/usr/bin/env python3
'''This module sums a list in an func
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''sums up a lsit of floating numbers
    '''
    return sum([i for i in input_list])
