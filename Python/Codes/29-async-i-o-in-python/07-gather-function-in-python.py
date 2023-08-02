# How to use asyncio.gather() to Run Multiple Asynchronous Operations :
import asyncio

async def coro_1():
   await asyncio.sleep(2)
   return 'Result of coro 1'

async def coro_2():
   await asyncio.sleep(1)
   return 'Result of coro 2'

async def main():
   results = await asyncio.gather(coro_1(), coro_2())
   print('Results:', results)

asyncio.run(main())