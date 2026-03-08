import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION

bot = Client(
    "rayn-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

assistant = Client(
    "rayn-assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

call = PyTgCalls(assistant)

async def main():
    await bot.start()
    await assistant.start()
    await call.start()
    print("Bot started successfully")
    await asyncio.Event().wait()

asyncio.run(main())
