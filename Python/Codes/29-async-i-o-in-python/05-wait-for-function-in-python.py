# Waiting for a Single Coroutine Using Python asyncio.wait_for() :
import asyncio

async def long_operation():
   print('Long operation started')
   await asyncio.sleep(5)
   print('Long operation completed')
   return 'Long operation result'

async def main():
   print('Main started')
   try:
       result = await asyncio.wait_for(long_operation(), timeout=3)
   except asyncio.TimeoutError:
       print('Timeout occurred')
   else:
       print('Result:', result)
   print('Main completed')


asyncio.run(main())