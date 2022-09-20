#!/usr/bin/env python3
""" Script takes a string k and an in OR float v as
    arguments and returns a tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple (k,v)
    """
    return (k, v ** 2)
