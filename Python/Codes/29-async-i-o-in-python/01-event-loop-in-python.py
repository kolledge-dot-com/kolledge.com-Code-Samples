# How the Event Loop Works in Python :
import asyncio

async def hello():
   print("Hello")
   await asyncio.sleep(1)
   print("World!")

async def main():
   await asyncio.gather( hello(), hello(), hello() )

asyncio.run(main())
