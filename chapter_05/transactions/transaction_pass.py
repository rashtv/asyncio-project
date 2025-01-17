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
        await connection.execute(
            "INSERT INTO brand VALUES (DEFAULT, 'brand_1')",
        )
        await connection.execute(
            "INSERT INTO brand VALUES (DEFAULT, 'brand_2')",
        )

    query: str = "SELECT brand_name FROM brand WHERE brand_name LIKE 'brand%'"
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()


asyncio.run(main())
