import asyncio
import time

async def t1():
    await asyncio.sleep(2)
    print('Task1')
    
async def t2():
    await asyncio.sleep(1)
    print('Task2')
    
async def t3():
    await asyncio.sleep(3)
    print('Task3')   
    
async def main():
    print(f"started at {time.strftime('%X')}")
    await asyncio.gather(t1(), t2(), t3())      
    print(f"finished at {time.strftime('%X')}")
    print('Done')
    
asyncio.run(main())    