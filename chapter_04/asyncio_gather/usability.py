import aiohttp
import asyncio

from util import async_timed


@async_timed()
async def fetch_status(
    session: aiohttp.ClientSession,
    url: str,
) -> int:
    async with session.get(url) as response:
        return response.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        requests = [fetch_status(session=session, url=url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


asyncio.run(main())
