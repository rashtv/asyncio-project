import asyncio
import aiohttp

from util import async_timed


async def fetch_status(
    session: aiohttp.ClientSession,
    url: str,
) -> int:
    async with session.get(url) as response:
        return response.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'https://www.google.com')),
            asyncio.create_task(fetch_status(session, 'https://www.google.com')),
        ]
        done, pending = await asyncio.wait(fetchers)

        print(f'Number of done tasks: {len(done)}')
        print(f'Number of pending tasks: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(f'Task {done_task} result: {result}')


if __name__ == '__main__':
    asyncio.run(main())
