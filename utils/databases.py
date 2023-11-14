import aiosqlite
import disnake


class UsersDataBase:
    def __init__(self):
        self.name = 'dbs/users.db'

    async def create_table(self):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = '''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                ruble INTEGER,
                dollar INTEGER,
                euro INTEGER
            )'''
            await cursor.execute(query)
            await db.commit()

    async def get_user(self, user: disnake.Member):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'SELECT * FROM users WHERE id = ?'
            await cursor.execute(query, (user.id,))
            return await cursor.fetchone()

    async def add_user(self, user: disnake.Member):
        async with aiosqlite.connect(self.name) as db:
            if not await self.get_user(user):
                cursor = await db.cursor()
                query = 'INSERT INTO users (id, ruble, dollar, euro) VALUES (?, ?, ?, ?)'
                await cursor.execute(query, (user.id, 10000, 100, 10))
                await db.commit()

    async def update_money(self, user: disnake.Member, ruble: int, dollar: int, euro: int):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE users SET ruble = ruble + ?, dollar = dollar + ?, euro = euro + ? WHERE id = ?'
            await cursor.execute(query, (ruble, dollar, euro, user.id))
            await db.commit()
