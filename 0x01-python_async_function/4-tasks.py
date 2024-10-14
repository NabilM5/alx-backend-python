#!/usr/bin/env python3
<<<<<<< HEAD
'''
 a new function task_wait_n. The code
=======
''' 
a new function task_wait_n. The code
>>>>>>> b392e62640fc054d27c5df1cf2e45a0474d074ce
is nearly identical to wait_n
except task_wait_random is being called.

'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
