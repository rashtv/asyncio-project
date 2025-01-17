import asyncio

import asyncpg
from asyncpg import Connection


async def main():
    connection: Connection = await asyncpg.connect(
        host='localhost',
        port=5432,
        database='products',
        user='postgres',
        password='password',
    )
    query = 'SELECT product_id, product_name FROM product'

    async with connection.transaction():
        async for product in connection.cursor(query=query):
            print(product)
    await connection.close()


asyncio.run(main())
