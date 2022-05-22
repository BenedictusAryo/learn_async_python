import asyncio

async def file_reply():
    await asyncio.sleep(2)
    return {'file': 'file.txt'}

async def data_reply():
    await asyncio.sleep(2)
    return {'data': 100}

async def task1():
    print('Wait for data...')
    x = await data_reply()
    print(x)

async def task2():
    print('Waiting for file...')
    x = await file_reply()
    print(x)

async def main():
    # await asyncio.gather(task1(), task2())
    x = asyncio.create_task(task1())
    y = asyncio.create_task(task2())
    await x
    await y

asyncio.run(main())