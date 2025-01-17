import asyncio

import asyncpg

from util import async_timed

product_query: str = \
    """
    SELECT
    p.product_id,
    p.product_name,
    p.brand_id,
    s.sku_id,
    pc.product_color_name,
    ps.product_size_name
    FROM product as p
    JOIN sku as s ON s.product_id = p.product_id
    JOIN product_color as pc ON pc.product_color_id = s.product_color_id
    JOIN product_size as ps ON ps.product_size_id = s.product_size_id
    WHERE p.product_id = 100
    """


async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)


@async_timed()
async def query_product_synchronously(pool, queries):
    return [await query_product(pool) for _ in range(queries)]


@async_timed()
async def query_product_concurrently(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)


async def main():
    async with asyncpg.create_pool(
        host='localhost',
        port=5432,
        database='products',
        user='postgres',
        password='password',
        min_size=6,
        max_size=6,
    ) as pool:
        # await asyncio.gather(
        #     query_product(pool),
        #     query_product(pool),
        # )
        await query_product_synchronously(pool, queries=10000)
        await query_product_concurrently(pool, queries=10000)


asyncio.run(main())
