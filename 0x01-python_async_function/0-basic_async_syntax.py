#!/usr/bin/env python3
'''an asynchronous coroutine that takes in an integer argument
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''an asynchronous coroutine that takes in an integer argument
    '''
    wait_delay = random.random()*max_delay
    await asyncio.sleep(wait_delay)
    return wait_delay
