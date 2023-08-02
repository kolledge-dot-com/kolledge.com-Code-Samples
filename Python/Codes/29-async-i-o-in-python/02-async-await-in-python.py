# How to pause a Python Co-routine using await keyword :
import asyncio


async def my_coroutine():
    print('Coroutine starting')
    await asyncio.sleep(1)
    print('Coroutine ending')


async def main():
    print('Main starting')
    await my_coroutine()
    print('Main ending')


asyncio.run(main())
