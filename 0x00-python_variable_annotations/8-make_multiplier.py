#!/usr/bin/env python3
""" Script takes a float multiplier as argument and
    returns a function that multiplies a float by
    multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function
    """
    def mult(m):
        """Multiplies a float by another float
        """
        return m * multiplier
    return mult
