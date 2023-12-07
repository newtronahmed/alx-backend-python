#!/usr/bin/env python3
"""Task 7 module"""
from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes str and an int or float as input and returns tuple"""
    return (k, float(v**2))
