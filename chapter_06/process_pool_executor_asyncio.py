import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import List


def count(count_to: int) -> int:
    counter = 0
    while counter < count_to:
        counter += 1
    return counter


async def main() -> None:
    with ProcessPoolExecutor() as executor:
        loop: AbstractEventLoop = asyncio.get_running_loop()
        nums = [1, 100, 100_000, 100_000_000, ]
        calls: List[partial[int]] = [partial(count, num) for num in nums]
        call_coroutines = []

        for call in calls:
            call_coroutines.append(loop.run_in_executor(executor=executor, func=call))

        results = await asyncio.gather(*call_coroutines)

        for result in results:
            print(result)


if __name__ == '__main__':
    asyncio.run(main())
