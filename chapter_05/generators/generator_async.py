import asyncio

from util import delay, async_timed


async def positive_integers_async(until: int):
    for integer in range(until):
        await delay(integer)
        yield integer

@async_timed()
async def main():
    async_generator = positive_integers_async(3)
    async for integer in async_generator:
        print(f'Number received: {integer}')


asyncio.run(main())
