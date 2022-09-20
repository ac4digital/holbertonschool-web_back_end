#!/usr/bin/env python3
""" Script that returns values, add type annotations
    to the function """
from typing import Union, Any, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """ Checks if key exists in a dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
