import time
from concurrent.futures import ProcessPoolExecutor


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.time()
    print(f'counter {counter} took {end - start} seconds')
    return counter


if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        numbers = [1, 100, 10_000, 1_000_000, ]
        for result in executor.map(count, numbers):
            print(result)
