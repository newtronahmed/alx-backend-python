#!/usr/bin/env python3
"""Task 8 module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable:
    """takes a float multiplier as argument and returns a function """
    return lambda x:x * multiplier
