import asyncio

from util import delay, async_timed


@async_timed()
async def main() -> None:
    t1 = asyncio.create_task(delay(3))
    t2 = asyncio.create_task(delay(2))
    t3 = asyncio.create_task(delay(1))
    results = await asyncio.gather(t1, t2, t3)
    print(results)

asyncio.run(main())
