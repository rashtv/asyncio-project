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
    try:
        async with connection.transaction():
            insert_brand = "INSERT INTO brand VALUES(9999, 'big_brand');"
            await connection.execute(insert_brand)
            await connection.execute(insert_brand)
    except asyncpg.PostgresError:
        logging.exception('Error while executing transaction')
    finally:
        query = "SELECT brand_name FROM brand WHERE brand_name LIKE 'big_%'"
        brands = await connection.fetch(query)
        print(f'Result: {brands}')
        await connection.close()


asyncio.run(main())
