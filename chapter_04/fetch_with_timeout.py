import asyncio
import aiohttp


async def fetch_status_with_timeout(
    session: aiohttp.ClientSession,
    url: str,
) -> int:
    ten_millis = aiohttp.ClientTimeout(total=1.5)
    async with session.get(url, timeout=ten_millis) as response:
        return response.status


async def main():
    session_timeout = aiohttp.ClientTimeout(total=3, connect=1.5)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        await fetch_status_with_timeout(session, 'https://example.com')

asyncio.run(main())
