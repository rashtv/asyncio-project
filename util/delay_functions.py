import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'starting delay {delay_seconds}')
    await asyncio.sleep(delay_seconds)
    print(f'finished delay {delay_seconds}')
    return delay_seconds
