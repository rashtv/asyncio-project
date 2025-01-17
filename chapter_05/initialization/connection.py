import asyncpg
import asyncio


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
    await connection.close()


asyncio.run(main())
