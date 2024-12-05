import asyncio
import aiohttp

from util import async_timed


@async_timed()
async def fetch_status(
    session: aiohttp.ClientSession,
    url: str,
    seconds: int = 0
) -> int:
    await asyncio.sleep(seconds)
    async with session.get(url) as response:
        return response.status


@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://www.google.com', 1),
            fetch_status(session, 'https://www.google.com', 5),
            fetch_status(session, 'https://www.google.com', 10),
        ]
        for done_task in asyncio.as_completed(fetchers, timeout=3):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print('Timeout Error')

    for task in asyncio.all_tasks():
        print(task)

if __name__ == '__main__':
    asyncio.run(main())
