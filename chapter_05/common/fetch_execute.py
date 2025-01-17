from typing import List

import asyncpg
import asyncio

from asyncpg import Record


async def main():
    connection = await asyncpg.connect(
        host='localhost',
        port=5432,
        database='products',
        user='postgres',
        password='password',
    )
    version = connection.get_server_version()
    print(f'Connected! Postgres Version is {version}')

    # await connection.execute("INSERT INTO brand VALUES (DEFAULT, 'Levis')")
    # await connection.execute("INSERT INTO brand VALUES (DEFAULT, 'Seven')")

    brand_query = "SELECT brand_id, brand_name FROM brand"
    results: List[Record] = await connection.fetch(brand_query)

    for brand in results:
        print(f'id: {brand["brand_id"]}, name: {brand["brand_name"]}')

    await connection.close()


asyncio.run(main())
