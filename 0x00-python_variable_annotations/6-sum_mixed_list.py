#!/usr/bin/env python3
""" Script takes a list mxd_lst of integers and
    floats as arguments and returns their sum as a float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns the sum of every element in a list
    """
    return sum(mxd_lst)
