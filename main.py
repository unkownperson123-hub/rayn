import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION

# Bot Client
bot = Client(
    "rayn-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Assistant Client
assistant = Client(
    "rayn-assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

# Voice Chat Client
call = PyTgCalls(assistant)

async def main():
    await bot.start()
    await assistant.start()
    await call.start()

    print("✅ RAYN Music Bot Started Successfully")

    await asyncio.Event().wait()

if name == "main":
    asyncio.run(main())
