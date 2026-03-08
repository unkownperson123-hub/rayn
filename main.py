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

# Voice Chat Player
call = PyTgCalls(assistant)

@bot.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text(
        "🎵 Rayn Music Bot Online\n\nUse /play to play music in VC."
    )

async def main():
    await bot.start()
    await assistant.start()
    await call.start()
    print("Rayn Music Bot Started")

    await idle()

from pyrogram.idle import idle
import asyncio
asyncio.get_event_loop().run_until_complete(main())
