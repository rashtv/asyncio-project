import logging
import asyncio
import asyncpg


async def main():
    connection: asyncpg.Connection = await asyncpg.connect(
        host='localhost',
        port=5432,
        database='products',
        user='postgres',
        password='password',
    )
    async with connection.transaction():
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'my_new_brand')")
        try:
            async with connection.transaction():
                await connection.execute("INSERT INTO product_color VALUES(1, 'black')")
        except asyncpg.PostgresError as err:
            logging.warning('Error while inserting color ignored', exc_info=err)

    await connection.close()


asyncio.run(main())
