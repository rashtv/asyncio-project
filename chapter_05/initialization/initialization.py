from typing import List

import asyncpg
import asyncio

from chapter_05.initialization.statements import (
    CREATE_BRAND_TABLE,
    CREATE_PRODUCT_TABLE,
    CREATE_PRODUCT_COLOR_TABLE,
    CREATE_PRODUCT_SIZE_TABLE,
    CREATE_SKU_TABLE,
    SIZE_INSERT,
    COLOR_INSERT,
)


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

    statements: List = [
        CREATE_BRAND_TABLE,
        CREATE_PRODUCT_TABLE,
        CREATE_PRODUCT_COLOR_TABLE,
        CREATE_PRODUCT_SIZE_TABLE,
        CREATE_SKU_TABLE,
        SIZE_INSERT,
        COLOR_INSERT,
    ]
    print('Database products initialization...')
    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    print('Database products initialized!')
    await connection.close()


asyncio.run(main())
