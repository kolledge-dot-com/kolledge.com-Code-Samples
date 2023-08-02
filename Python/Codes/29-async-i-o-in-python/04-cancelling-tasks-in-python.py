# How to cancel an Asynchronous Task in python :
import asyncio

async def long_operation():
   print('Long operation started')
   await asyncio.sleep(5)
   print('Long operation completed')
   return 'Long operation result'

async def main():
   print('Main started')
   long_op_task = asyncio.create_task(long_operation())
   await asyncio.sleep(3)
   long_op_task.cancel()
   print('Long operation cancelled')
   try:
       await long_op_task
   except asyncio.CancelledError:
       print('Long operation was cancelled')
   else:
       print('Long operation result:', long_op_task.result())
   print('Main completed')


asyncio.run(main())