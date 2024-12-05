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
            fetch_status(session, 'https://www.google.com', 1),
            fetch_status(session, 'https://www.google.com', 10),
        ]
        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


asyncio.run(main())
