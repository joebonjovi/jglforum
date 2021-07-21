# Copyright (c) JGL Forum API 2021, JGL Technolgies

# --IMPORTS--

import asyncio
import aiohttp
import aiosqlite
import json
from aiohttp import web

# --GLOBAL DEFINITIONS / INITIALIZERS--



# --MAIN API CODE--

async def init():
    async with aiosqlite.connect("users.db") as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        body TEXT,
        user TEXT
        )""")
        
        await db.execute("""CREATE TABLE IF NOT EXISTS accounts(
        username TEXT PRIMARY KEY,
        password TEXT
        )""")

        await db.commit()

async def login(request):
    pass

loop = asyncio.new_event_loop()
loop.run_until_complete(init())
app = web.Application()
app.add_routes([web.get('/login', login)])
web.run_app(app)
