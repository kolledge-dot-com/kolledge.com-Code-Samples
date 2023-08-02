# Running Other Tasks While Waiting :
import asyncio


async def long_operation():
    print('Long operation started')
    await asyncio.sleep(3)
    print('Long operation completed')
    return 'Long operation result'


async def task1():
    print('Task 1 started')
    await asyncio.sleep(1)
    print('Task 1 completed')
    return 'Task 1 result'


async def task2():
    print('Task 2 started')
    await asyncio.sleep(2)
    print('Task 2 completed')
    return 'Task 2 result'


async def main():
    print('Main started')
    long_op_task = asyncio.create_task(long_operation())
    task1_task = asyncio.create_task(task1())
    task2_task = asyncio.create_task(task2())
    await long_op_task

    print('Long operation result:', long_op_task.result())
    await task1_task

    print('Task 1 result:', task1_task.result())
    await task2_task

    print('Task 2 result:', task2_task.result())
    print('Main completed')


asyncio.run(main())