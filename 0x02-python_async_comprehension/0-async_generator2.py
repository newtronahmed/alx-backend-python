#!/usr/bin/env python3
""" Task 0 module"""

import random
import asyncio
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    ''' Gernerates random in 10 time'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

