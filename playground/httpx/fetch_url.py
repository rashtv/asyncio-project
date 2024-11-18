import asyncio

import httpx

from util import async_timed


@async_timed()
async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url, timeout=3)
        return response


@async_timed()
async def main() -> None:
    url = 'https://www.google.com'

    for i in range(5):
        task = asyncio.create_task(fetch_url(url=url))
        try:
            response = await asyncio.wait_for(task, timeout=1)
            if response.status_code == 200:
                print(response.text)
                break
        except asyncio.TimeoutError:
            if task.cancelled():
                print('Task cancelled')
            else:
                print('Impossible result achieved!')


if __name__ == '__main__':
    asyncio.run(
        main(),
        # Pretty cool feature in case of
        # forgotten await or something else
        debug=True,
    )
