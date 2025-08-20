import time
from multiprocessing import Process


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.time()
    print(f'counter {counter} took {end - start} seconds')
    return counter


if __name__ == '__main__':
    start_time = time.time()

    to_100_000_000 = Process(target=count, args=(100_000_000,))
    to_200_000_000 = Process(target=count, args=(200_000_000,))

    to_100_000_000.start()
    to_200_000_000.start()

    to_100_000_000.join()
    to_200_000_000.join()

    end_time = time.time()
    print(f'total time {end_time - start_time} seconds')
