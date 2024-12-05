import asyncio
import aiohttp

from util import async_timed


@async_timed()
async def fetch_status(session: aiohttp.ClientSession, url: str) -> int:
    async with session.get(url) as response:
        return response.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url: str = 'https://example.com'
        status = await fetch_status(session, url)
        print(f'Status for {url} is {status}')


asyncio.run(main())
