#!/usr/bin/env python3
""" Task 0 module"""
import random
import asyncio

async def wait_random(max_delay=10) -> float:
   """waits for a random delay between 0 and max_delay""" 
    rand = random.random() * max_delay
    await asyncio.sleep(rand)
    return rand 
