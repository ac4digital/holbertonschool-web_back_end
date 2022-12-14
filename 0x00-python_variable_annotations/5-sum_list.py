#!/usr/bin/env python3
""" Script takes a list input_list of floats as
    argument and returns their sum as a float
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns the sum of all the elements of a list
    """
    return sum(input_list)
