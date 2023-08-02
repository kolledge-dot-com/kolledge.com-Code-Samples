# Using Python asyncio Future with Await :
import asyncio

async def coro(fut):
   result = await fut
   print('Result:', result)

async def main():
   print('Main started')
   fut = asyncio.Future()
   asyncio.create_task(coro(fut))
   fut.set_result('Future result')
   print('Main completed')

asyncio.run(main())