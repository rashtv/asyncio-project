import asyncio
import logging

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
            asyncio.create_task(fetch_status(session, 'python://')),
            asyncio.create_task(fetch_status(session, 'https://www.google.com')),
        ]
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)

        print(f'Number of done tasks: {len(done)}')
        print(f'Number of pending tasks: {len(pending)}')

        for done_task in done:
            if done_task.exception() is None:
                print(f'Task {done_task} result: {done_task.result()}')
            else:
                logging.error(f'Exception raised', exc_info=done_task.exception())

        for pending_task in pending:
            pending_task.cancel()
        

if __name__ == '__main__':
    asyncio.run(main())
