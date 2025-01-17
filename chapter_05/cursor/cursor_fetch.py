import asyncio
import asyncpg
from asyncpg import Connection
from asyncpg.cursor import Cursor


async def main():
    connection: Connection = await asyncpg.connect(
        host='localhost',
        port=5432,
        database='products',
        user='postgres',
        password='password',
    )

    async with connection.transaction():
        query = 'SELECT product_id, product_name FROM product'
        cursor: Cursor = await connection.cursor(query=query)
        await cursor.forward(500)
        products = await cursor.fetch(100)
        for product in products:
            print(product)
    await connection.close()


asyncio.run(main())
