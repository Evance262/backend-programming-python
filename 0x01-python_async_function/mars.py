#!/usr/bin/env python3

import asyncio

async def launch():
    print('Shuttle launching in 5 sec:')
    await asyncio.sleep(2)
    print("Dispatch!")
    return {'data': 1}

async def print_numbers():
    for i in range(5):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(launch())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2

asyncio.run(main())
