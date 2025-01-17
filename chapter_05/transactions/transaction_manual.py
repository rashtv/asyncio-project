import asyncio
import asyncpg
from asyncpg.transaction import Transaction


async def main():
    connection: asyncpg.Connection = await asyncpg.connect(
        host='localhost',
        port=5432,
        database='products',
        user='postgres',
        password='password',
    )
    transaction: Transaction = connection.transaction()
    await transaction.start()
    try:
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_1')")
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_2')")
    except asyncpg.PostgresError:
        print('Error: transaction cancelled!')
        await transaction.rollback()
    else:
        print('Transaction successful!')
        await transaction.commit()

    query = "SELECT brand_name FROM brand WHERE brand_name LIKE 'brand%'"
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()


asyncio.run(main())
