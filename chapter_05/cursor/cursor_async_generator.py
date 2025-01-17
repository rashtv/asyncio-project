import asyncio

import asyncpg
from asyncpg import Connection


async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count > to_take - 1:
            return
        item_count += 1
        yield item


async def main():
    connection: Connection = await asyncpg.connect(
        host='localhost',
        port=5432,
        database='products',
        user='postgres',
        password='password',
    )
    product_number = 5

    async with connection.transaction():
        query = "SELECT product_id, product_name FROM product"
        product_generator = connection.cursor(query=query)

        async for product in take(product_generator, product_number):
            print(product)
        print(f'Received first {product_number} product.')

    await connection.close()


asyncio.run(main())
